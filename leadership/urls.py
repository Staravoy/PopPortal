from django.urls import path
from . import views

app_name = 'leadership'

urlpatterns = [
    path('', views.leader_home, name='leader_home'),
    path('transport', views.transport, name='transport'),
    path('all_transport/<str:type>/', views.all_transport, name='all_transport'),
]
