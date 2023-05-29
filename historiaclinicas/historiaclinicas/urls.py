from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
from .views import historiaclinica_list, historiaclinica_create
urlpatterns = [
    path('historiaclinicas/', views.historiaclinica_list, name='historiaclinicas'),
    path('historiaclinicacreate/', csrf_exempt(views.historiaclinica_create), name='historiaclinicaCreate'),
    #path('historiaclinica/update/<int:historiaclinica_id>/', views.historiaclinica_update, name='historiaclinicaUpdate'),

]
