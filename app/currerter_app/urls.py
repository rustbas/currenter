from django.urls import path
from .views import exchange, update_database

urlpatterns = [
        path('', exchange),
        path('', update_database),
]
