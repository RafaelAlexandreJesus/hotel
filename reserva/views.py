from django.shortcuts import render
import conexao
c = conexao.conectar()

# Create your views here.
def index(request):
    with c.cursor() as lista:
        sql = "select * from quarto where status = 'Livre'"
        lista.execute(sql)
        listaQ = lista.fetchall()
    return render(request, 'reserva/index.html', {'listaQ':listaQ})

def reservar(request):
    r = request.POST.get('reservar')
    with c.cursor() as reserva:
        sql = "update quarto set status = 'Ocupado' where numQuarto = %s"
        reserva.execute(sql, (str(r)))
        c.commit()
    return index(request)