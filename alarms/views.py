from django.http import JsonResponse
from django.shortcuts import render

from pacientes.logic.paciente_logic import get_paciente_by_id
from .logic.logic_alarm import get_alarms, get_historiaclinicas_by_paciente, create_alarm

def alarm_list(request):
    alarms = get_alarms()
    context = list(alarms.values())
    return JsonResponse(context, safe=False)

def generate_alarm(request, paciente_id):
    paciente = get_paciente_by_id(paciente_id)
    historiaclinicas = get_historiaclinicas_by_paciente(paciente_id)
    createAlarm = False
    upperHistoriaclinica = None
    for historiaclinica in historiaclinicas:
        if len(historiaclinica.alergias) >= 10:
            createAlarm = True
            upperHistoriaclinica = historiaclinica
    if createAlarm:
        alarm = create_alarm(paciente, upperHistoriaclinica, 10)
        return JsonResponse(alarm.toJson(), safe=False)
    else:
        return JsonResponse({'message': 'No alarm created'}, status=200)
