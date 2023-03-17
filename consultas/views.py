from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ConsultaForm
from .logic.consulta_logic import get_consultas, create_consulta

def consulta_list(request):
    consultas = get_consultas()
    context = {
        'consulta_list': consultas
    }
    return render(request, 'Consulta/consultas.html', context)

def consulta_create(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            create_consulta(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created consulta')
            return HttpResponseRedirect(reverse('consultaCreate'))
        else:
            print(form.errors)
    else:
        form = ConsultaForm()

    context = {
        'form': form,
    }
    return render(request, 'Consulta/consultaCreate.html', context)
# Create your views here.
