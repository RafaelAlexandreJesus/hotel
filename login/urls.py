from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('login/', views.logar, name='logar'),
]