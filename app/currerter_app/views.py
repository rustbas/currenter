from django.shortcuts import render
import requests
import sqlite3
from sqlite3 import Error
from os.path import abspath

# Create your views here.
NEEDED_CURRS = ['GBP', 'USD', 'EUR', 'JPY']
DATABASE=abspath('.') + '/currerter_app/sqlite3/database.sqlite3'

def exchange(request):

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    context = {'name':'guest', 'amount':'0'}

    if request.method == 'GET':

        return render(request=request, template_name='currerter_app/index.html', context=context)

    elif request.method == 'POST':

        update_database(cursor, request)

        context['amount'] = request.POST.get('amount')
        context['from_cur'] = request.POST.get('from_cur')
        context['to_cur'] = request.POST.get('to_cur')
        context['result'] = convert(
                                context['from_cur'],
                                context['to_cur'],
                                context['amount'],
                                cursor
                                )
        context['last_update'] = get_last_update(cursor)

        connection.close()

        return render(request=request, template_name='currerter_app/index.html', context=context)

def convert(from_cur, to_cur, amount, cursor):
    try:
        if from_cur == 'USD':
            coef = cursor.execute("SELECT coefficient FROM currs WHERE to_cur = ?", (to_cur,)).fetchall()[0][0]
            return round(float(coef) * float(amount),2)
        elif to_cur == 'USD':
            coef = cursor.execute("SELECT coefficient FROM currs WHERE to_cur = ?", (from_cur,)).fetchall()[0][0]
            return round( float(amount) / float(coef), 2)
        else:
            coef1 = cursor.execute("SELECT coefficient FROM currs WHERE to_cur = ?", (to_cur,)).fetchall()[0][0]
            coef2 = cursor.execute("SELECT coefficient FROM currs WHERE to_cur = ?", (from_cur,)).fetchall()[0][0]
        return round( float(amount) * float(coef1) / float(coef2), 2)

    except ValueError:
        return 0.0

def get_last_update(cursor):
    result = cursor.execute("SELECT last_update FROM updates ORDER BY last_update DESC LIMIT 1;").fetchall()
    if result == []:
        return "No last updates found!"
    else:
        return result[0][0]

def update_database(cursor, request):

    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()

    currs = response.get('rates')

    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("INSERT INTO updates (last_update) VALUES (strftime('%Y-%m-%d %H-%M-%S','now')); ")
    for key, value in currs.items():
        if key in NEEDED_CURRS:
            cursor.execute("UPDATE currs SET coefficient = ? WHERE to_cur = ?", (value, key))
    cursor.execute("COMMIT")
