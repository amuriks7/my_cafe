from django.urls import path
from .views import reservation_list

app_name = 'manager'

urlpatterns = [
    path('reservations/', reservation_list, name='reservations_list'),
]