from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cliente'),
    path('formulario/', views.formulario, name='form_cliente'),
    path('cadastrar/', views.insere_cliente, name='insere_cliente'),
]