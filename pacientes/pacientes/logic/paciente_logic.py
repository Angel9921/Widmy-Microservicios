from ..models import Paciente

def get_pacientes():
    queryset = Paciente.objects.all()
    return (queryset)

def get_paciente_by_id(id):
    queryset = Paciente.objects.get(id=id)
    return (queryset)

def create_paciente(form):
    measurement = form.save()
    measurement.save()
    return ()
