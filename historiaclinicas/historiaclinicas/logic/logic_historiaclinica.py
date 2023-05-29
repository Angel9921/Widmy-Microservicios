from ..models import Historiaclinica

def get_historiaclinicas():
    queryset = Historiaclinica.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_historiaclinica(form):
    historiaclinica = form.save()
    historiaclinica.save()
    return ()
