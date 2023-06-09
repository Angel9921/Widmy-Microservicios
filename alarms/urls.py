from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('alarms/', views.alarm_list),
    path('alarmsValidate/<int:paciente_id>', views.generate_alarm),
]
