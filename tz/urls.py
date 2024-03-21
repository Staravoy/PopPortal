"""Шляхи для TZ"""
from django.urls import path, include
from . import views

app_name = 'tz'

urlpatterns = [
    path('', views.index, name='index'),  # Головна сторінка
    # Інспектор підрозділу
    path('tz_unit', views.tz_unit, name='tz_unit'),  # Головна сторінка інспектора підрозділу з ТЗ
    path('all_units_tz', views.all_units_tz, name='all_units_tz'),  # Усі ТЗ підрозділу
    path('all_car', views.all_car, name='all_car'),  # усі легкові
    path('all_minibus', views.all_minibus, name='all_minibus'),  # усі мікроавтобуси
    path('all_bus', views.all_bus, name='all_bus'),  # усі автобуси
    path('all_truck', views.all_truck, name='all_truck'),  # усі вантажівки
    path('all_armored', views.all_armored, name='all_armored'),  # уся броньована техніка
    path('all_pickup', views.all_pickup, name='all_pickup'),   # усі пікапи
    path('all_suv', views.all_suv, name='all_suv'),   # усі позашляховики
    path('add_tz', views.add_tz, name='add_tz'),   # додавання транспортного засобу
    path('edit_tz/<int:tz_id>/', views.edit_tz, name='edit_tz'),  # сторінка для редагування запису
    path('one_tz/<int:tz_id>/', views.one_tz, name='one_tz'),    # загальна сторінка для обробки одного запису
]



