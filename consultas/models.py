from django.db import models

# Create your models here.
class Consulta(models.Model):
    fecha = models.DateTimeField()
    motivo = models.TextField()
    diagnostico = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.motivo, self.diagnostico)
