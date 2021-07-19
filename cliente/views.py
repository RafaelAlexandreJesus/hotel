from django.http import request
from hotel.settings import TEMPLATES
from django.shortcuts import render
import conexao
c = conexao.conectar()

# Create your views here.
def index(request):
    return render(request, 'cliente/form_cliente.html')

def insere_cliente(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    profissao = request.POST.get('profi')
    tel = request.POST.get('telefone')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    with c.cursor() as inserir:
        sql = 'insert into cliente(nome, cpf, profissao, telefone, email, senha) values(%s,%s,%s,%s,%s,%s)'
        inserir.execute(sql,(nome, cpf, profissao, tel, email, senha))
        c.commit()
    return render(request, '../../home/templates/home/index.html')

def formulario(request):
    return render(request, 'cliente/form_cliente.html')

def home(request):
    return render(request, '../../home/templates/home/index.html')