from django.shortcuts import render
import conexao
c = conexao.conectar()

def index(request):
    return render(request, 'administracao/index.html')