from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('historiaclinicas/', views.historiaclinica_list),
    path('historiaclinicacreate/', csrf_exempt(views.historiaclinica_create), name='historiaclinicaCreate'),
]
