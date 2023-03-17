from rest_framework import serializers
from . import models


class HistoriaclinicaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'paciente', 'alergias', 'medicamentos', 'condiciones_medicas','time',)
        model = models.Measurement
