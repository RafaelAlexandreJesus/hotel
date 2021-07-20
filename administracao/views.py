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

def insere_cliente_adm(request):
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
    with c.cursor() as listar:
        sql = "select * from cliente"
        listar.execute(sql)
        lista = listar.fetchall()
    return render(request, 'administracao/index.html', {'listaC': lista})

def editar(request):
    editar = request.POST.get('editar')
    with c.cursor() as editaF:
        sql = "select * from cliente where id = %s"
        editaF.execute(sql, (editar))
        lista = editaF.fetchall()
    return render(request, 'administracao/editar_cliente.html', {'listaEdita': lista})

def editar_banco(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('telefone')
    profi = request.POST.get('profi')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    salva = request.POST.get('salva')

    with c.cursor() as listar:
        sql = "select * from cliente"
        listar.execute(sql)
        lista = listar.fetchall()

    with c.cursor() as editarB:
        sql = "update cliente set nome = %s, cpf = %s, telefone = %s, profissao = %s, email = %s, senha = %s where id = 1"
        execucao = editarB.execute(sql, (nome, cpf, telefone, profi, email, senha))
        if execucao != 0:
            return render(request, 'administracao/index.html', {'listaC': lista})

    return render(request, 'administracao/editar_cliente.html', {'listaEdita': lista})
