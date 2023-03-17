from ..models import Consulta

def get_consultas():
    queryset = Consulta.objects.all()
    return (queryset)

def create_consulta(form):
    consulta = form.save()
    consulta.save()
    return ()
