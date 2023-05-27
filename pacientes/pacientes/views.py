from django.shortcuts import render
from .models import Paciente
# Create your views here.
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import PacienteForm
from .logic.paciente_logic import get_pacientes, create_paciente
from django.contrib.auth.decorators import login_required

# @login_required
# def paciente_list(request):
#     pacientes = get_pacientes()
#     context = {
#         'paciente_list': pacientes
#     }
#     return render(request, 'Paciente/pacientes.html', context)

def PacienteList(request):
    queryset = Paciente.objects.all()
    pacientes = list(queryset.values('id', 'nombre', 'apellido', 'fecha_nacimiento'))
    context = {
        'paciente_list': pacientes
    }
    return render(request, 'Paciente/pacientes.html', context)


# def paciente_create(request):
#     if request.method == 'POST':
#         form = PacienteForm(request.POST)
#         if form.is_valid():
#             create_paciente(form)
#             messages.add_message(request, messages.SUCCESS, 'Successfully created paciente')
#             return HttpResponseRedirect(reverse('pacienteCreate'))
#         else:
#             print(form.errors)
#     else:
#         form = PacienteForm()

#     context = {
#         'form': form,
#     }
#     return render(request, 'Paciente/pacienteCreate.html', context)

def PacienteCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        paciente = Paciente()
        paciente.nombre = data_json["nombre"]
        paciente.apellido = data_json["apellido"]
        paciente.fecha_nacimiento = data_json["fecha_nacimiento"]
        paciente.save()
        return HttpResponse("successfully created paciente")