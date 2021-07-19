from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='adm'),
    path('formularioADM/', views.formulario , name='form_cliente_ADM'),
    path('editarADM/', views.editar , name='editarADM'),
]