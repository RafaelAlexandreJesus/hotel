from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='adm'),
    path('formularioADM/', views.formulario , name='form_cliente_ADM'),
    path('editarADM/', views.editar , name='form_edita_cliente_ADM'),
    path('editar/', views.editar_banco , name='editar_adm'),
    path('cadastro_Cliente/', views.insere_cliente_adm , name='insere_cliente_adm'),

]