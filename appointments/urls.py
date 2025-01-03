from django.urls import path
from . import views

urlpatterns = [
    path('register_patient/', views.register_patient, name='register_patient'),
    path('schedule_appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('patient_list/', views.patient_list, name='patient_list'),
    path('appointment_list/', views.appointment_list, name='appointment_list'),

    # Queue
    path('registration_queueing/', views.registration_queueing, name='registration_queueing'),
    path('accept_patient/<str:patient_id>/', views.accept_patient, name='accept_patient'),
    path('preliminary_assessment/<str:patient_id>/', views.preliminary_assessment, name='preliminary_assessment'),
    path('treatment_queue/', views.treatment_queue, name='treatment_queue'),
    path('complete_treatment/<str:patient_id>/', views.complete_treatment, name='complete_treatment'),
]
