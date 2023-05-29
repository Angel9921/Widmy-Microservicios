from ..models import Historiaclinica

def get_historiaclinicas():
    queryset = Historiaclinica.objects.all()
    return (queryset)

def create_historiaclinica(form):
    historiaclinica = form.save()
    historiaclinica.save()
    return ()
