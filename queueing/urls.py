from django.urls import path
from . import views

app_name = 'queueing'

urlpatterns = [
    path('registration_queueing/', views.registration_queueing, name='registration_queueing'),
    path('accept_patient/<str:patient_id>/', views.accept_patient, name='accept_patient'),
    path('preliminary_assessment/<str:patient_id>/', views.preliminary_assessment, name='preliminary_assessment'),
    path('treatment_queue/', views.treatment_queue, name='treatment_queue'),
    path('complete_treatment/<str:patient_id>/', views.complete_treatment, name='complete_treatment'),
]

