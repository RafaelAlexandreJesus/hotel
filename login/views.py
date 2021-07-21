from django.shortcuts import render
import conexao
c = conexao.conectar()

def index(request):
    return render(request, 'login/index.html')

def logar(request):
    email = request.POST.get("email")
    senha = request.POST.get("senha")
    with c.cursor() as logar:
        query = "select * from cliente where email = %s and senha = %s"
        existe = logar.execute(query, (email, senha))

        if existe != 0:
            lista = logar.fetchall()

            for dados in lista:
                if dados['tipo'] == 0 :
                    return render(request, 'administracao/index.html')
                else:
                    return render(request, 'login/index.html')

    return render(request, 'login/index.html')