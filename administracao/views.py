from django.shortcuts import render
import conexao
c = conexao.conectar()

def index(request):

    with c.cursor() as listar:
        sql = "select * from cliente"
        listar.execute(sql)
        lista = listar.fetchall()
    return render(request, 'administracao/index.html', {'listaC':lista})

def formulario(request):
    return render(request, 'administracao/form_cliente.html')

def editar(request):
    return render(request, 'administracao/editar_cliente.html')