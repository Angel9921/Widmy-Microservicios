from django.db import models
from django.utils import timezone
from pacientes.models import Paciente
# Create your models here.
class Historiaclinica(models.Model):
    paciente = models.IntegerField(null=False, default=None)
    alergias = models.TextField(null=True, blank=True)
    medicamentos = models.TextField(null=True, blank=True)
    condiciones_medicas = models.TextField(null=True, blank=True)
    dateTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s' % (self.paciente, self.medicamentos)