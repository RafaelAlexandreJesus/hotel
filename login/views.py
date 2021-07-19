from django.shortcuts import render

def index(request):
    return render(request, 'login/index.html')

def logar(request):
    email = request.POST.get("email")
    senha = request.POST.get("senha")
    with c.cursor() as logar:
        query = "select * from cliente where email = %s and senha = %s"

        existe = logar.execute(query,(email, senha))

        if existe != 0:
            sql = "select * from cliente"
            logar.execute(sql)
            lista = logar.fetchall()
            return render(request, 'cliente/listagem.html', {'listaC':lista})
        else:
            return render(request, 'home/login.html')