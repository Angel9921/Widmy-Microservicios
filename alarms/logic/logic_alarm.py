from historiaclinicas.historiaclinicas.models import Historiaclinica
from ..models import Alarm

def get_alarms():
    queryset = Alarm.objects.all().order_by('-dateTime')
    return (queryset)

def get_historiaclinicas_by_paciente():
    queryset = Historiaclinica.objects.filter(paciente=paciente).order_by('-dateTime')[:10]
    return (queryset)

def create_alarm(paciente, historiaclinica, limitExceeded):
    alarm = Alarm()
    alarm.paciente = paciente
    alarm.historiaclinica = historiaclinica
    alarm.alergias = historiaclinica.alergias
    alarm.limitExceeded = limitExceeded
    alarm.save()
    return alarm
