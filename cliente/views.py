from django.shortcuts import render

# Create your views here.
def index(request):
    print("pimbaa")
    return render(request, 'home/listagem.html')