from django import forms
from .models import Historiaclinica

class HistoriaclinicaForm(forms.ModelForm):
    class Meta:
        model = Historiaclinica
        fields = [
	    'paciente',
            'alergias',
	    'medicamentos',
	    'condiciones_medicas',
        ]
        labels = {
	    'paciente': 'Paciente',
            'alergias': 'Alergias',
	    'medicamentos': 'Medicamentos',
	    'condiciones_medicas': 'Condiciones_medicas',
        }
