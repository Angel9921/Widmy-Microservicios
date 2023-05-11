from django.shortcuts import render, get_object_or_404
from .forms import HistoriaclinicaForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.logic_historiaclinica import create_historiaclinica, get_historiaclinicas
from .models import Historiaclinica
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

@login_required
def historiaclinica_list(request):
    role = getRole(request)
    if role == "Doctor":
        historiaclinicas = get_historiaclinicas()
        context = {
            'historiaclinica_list': historiaclinicas
        }
        return render(request, 'Historiaclinica/historiaclinicas.html', context)
    else:
        return HttpResponse("Unauthorized User")


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

def historiaclinica_update(request, historiaclinica_id):
    historiaclinica = get_object_or_404(Historiaclinica, pk=historiaclinica_id)
    if request.method == 'POST':
        form = HistoriaclinicaForm(request.POST, instance=historiaclinica)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Historiaclinica update successful')
            return HttpResponseRedirect(reverse('historiaclinicas'))
        else:
            print(form.errors)
    else:
        form = HistoriaclinicaForm(instance=historiaclinica)

    context = {
        'form': form,
    }

    return render(request, 'Historiaclinica/historiaclinicaUpdate.html', context)
# Create your views here.
