from django.shortcuts import render
import conexao
c = conexao.conectar()

# Create your views here.
def index(request):
    print("pimbaa")
    return render(request, 'home/listagem.html')

def insere_cliente(request):
    with c.cursor() as inserir:
        # nome
        # cpf
        # profissao
        # tel
        sql = 'insert into cliente(nome, cpf, profissão, telefone) values(%s,%s,%s,%s)'
        inserir.execute(sql,())