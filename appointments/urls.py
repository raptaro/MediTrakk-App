from django.urls import path, include
from . import views

urlpatterns = [
    path('register_patient/', views.register_patient, name='register_patient'),
    path('schedule_appointment', views.schedule_appointment, name='schedule_appointment'),
    path('patient_list/', views.patient_list, name='patient_list'),

]

