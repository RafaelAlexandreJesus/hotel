from django.shortcuts import render
import conexao
c = conexao.conectar()

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

