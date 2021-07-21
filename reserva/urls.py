from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='reserva'),
    path('Reservar Quarto/', views.reservar, name="reservarQ")
]