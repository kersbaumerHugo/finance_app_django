from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader


from .models import Entry

def index(request):
    latest_entry_list = Entry.objects.order_by("-date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_entry_list": latest_entry_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, "polls/detail.html", {"entry": entry})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
def registrar_transacao(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        categoria = request.POST.get('categoria')
        status = request.POST.get('status')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        data = request.POST.get('data')
        if not descricao or not valor or not data or not tipo:
            messages.error(request, "Todos os campos são obrigatórios")
            return redirect('registrar_transacao')
        if tipo == 'Entrada':
            Entry.objects.create(
                categoria = categoria,
                status = status,
                descricao = descricao,
                valor = float(valor),
                data = data
                )
        elif tipo == 'Saída':
            Exit.objeccts.create(
                categoria = categoria,
                status = status,
                descricao = descricao,
                valor = float(valor),
                data = data
                )










        
    
