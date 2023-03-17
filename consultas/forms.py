from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = [
            'fecha',
	    'motivo',
	    'diagnostico',
        ]
        labels = {
            'fecha': 'Fecha',
	    'motivo' : 'Motivo',
	    'diagnostico' : 'Diagnostico',
        }
