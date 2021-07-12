from django.shortcuts import render
import conexao
c = conexao.conectar()

# Create your views here.
def index(request):
    with c.cursor() as listar:
        sql = "select * from cliente"
        listar.execute(sql)
        lista = listar.fetchall()
    return render(request, 'cliente/listagem.html', {'listaC' : lista})

def insere_cliente(request):
    with c.cursor() as inserir:
        # nome
        # cpf
        # profissao
        # tel
        sql = 'insert into cliente(nome, cpf, profissão, telefone) values(%s,%s,%s,%s)'
        inserir.execute(sql,())

