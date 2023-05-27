from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    # path('pacientes/', views.paciente_list, name='pacienteList'),
    # path('pacientecreate/', csrf_exempt(views.paciente_create), name='pacienteCreate'),
    url(r'^pacientes/', views.PacienteList, name='pacienteList'),
    url(r'^pacientecreate/$', csrf_exempt(views.PacienteCreate), name='pacienteCreate'),
]
