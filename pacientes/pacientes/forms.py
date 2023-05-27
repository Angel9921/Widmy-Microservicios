from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'apellido',
            'fecha_nacimiento',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'fecha_nacimiento': 'Fecha_nacimiento',
        }
