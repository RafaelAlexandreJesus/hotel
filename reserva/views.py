from django.shortcuts import render
import conexao
c = conexao.conectar()

# Create your views here.


def index(request):
    with c.cursor() as lista:
        sql = "select * from quarto where status = 'Livre'"
        lista.execute(sql)
        listaQ = lista.fetchall()
    return render(request, 'reserva/index.html', {'listaQ': listaQ})


def reservar(request):
    r = request.POST.get('reservar')
    c = request.POST.get('reservarIDcli')
    print(r)
    print(c)
    with c.cursor() as reserva:
        sql = "update quarto set status = 'Ocupado' where numQuarto = %s"
        reserva.execute(sql, (str(r)))
        c.commit()

    with c.cursor() as reservaC:
        sql2 = "insert into reserva(idcliente, dataInicio, dataFinal, valorReserva, formaP, quarto) values(%s,'21/07/2021', '21/07/2021', '150.00', 'Cartão', %s)"
        reservaC.execute(sql2, (str(c), str(r)))
        c.commit()
    return index(request)
