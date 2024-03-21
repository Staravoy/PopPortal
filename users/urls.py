"""Шляхи для users"""
from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # Додавання уставної URL auth (автентифікація)
    path('', include('django.contrib.auth.urls'))
]
