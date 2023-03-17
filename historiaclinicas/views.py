from django.shortcuts import render
from .forms import HistoriaclinicaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_historiaclinica import create_historiaclinica, get_historiaclinicas

def historiaclinica_list(request):
    historiaclinicas = get_historiaclinicas()
    context = {
        'historiaclinica_list': historiaclinicas
    }
    return render(request, 'Historiaclinica/historiaclinicas.html', context)

def historiaclinica_create(request):
    if request.method == 'POST':
        form = HistoriaclinicaForm(request.POST)
        if form.is_valid():
            create_historiaclinica(form)
            messages.add_message(request, messages.SUCCESS, 'Historiaclinica create successful')
            return HttpResponseRedirect(reverse('historiaclinicaCreate'))
        else:
            print(form.errors)
    else:
        form = HistoriaclinicaForm()

    context = {
        'form': form,
    }

    return render(request, 'Historiaclinica/historiaclinicaCreate.html', context)
# Create your views here.
