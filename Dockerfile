FROM python:3.11-alpine

COPY ./app /app

WORKDIR /app

COPY ./requirements.txt .

EXPOSE 80

RUN pip install --no-cache-dir -r requirements.txt && \
    ./manage.py migrate

ENTRYPOINT [ "./manage.py", "runserver", "0.0.0.0:80" ]
