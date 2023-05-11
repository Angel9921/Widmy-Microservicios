from django.db import models
from pacientes.models import Paciente
from historiaclinicas.models import Historiaclinica

class Alarm(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=None)
    historiaclinica = models.ForeignKey(Historiaclinica, on_delete=models.CASCADE, default=None)
    alergias = models.TextField(null=True, blank=True)
    limitExceeded = models.FloatField(null=True, blank=True, default=None)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{"paciente": %s, "historiaclinica": %s, "limitExceeded": %s, "dateTime": %s}' % (self.paciente.nombre, self.historiaclinica.alergias, self.limitExceeded, self.dateTime)
    
    def toJson(self):
        alarm = {
            'id': self.id,
            'paciente': self.paciente.nombre,
            'historiaclinica': self.historiaclinica.alergias,
            'value': self.alergias,
            'dateTime': self.dateTime,
            'limitExceeded': self.limitExceeded
        }
        return alarm
