from ..models import Paciente

def get_pacientes():
    queryset = Paciente.objects.all()
    return (queryset)

def create_paciente(form):
    measurement = form.save()
    measurement.save()
    return ()
