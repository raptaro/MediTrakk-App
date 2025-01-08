from . import views
from django.urls import path

app_name = 'patient'

urlpatterns = [
    path('register_patient/', views.register_patient, name='register_patient'),
    path('patient_list/', views.patient_list, name='patient_list'),
    path('patient_view/', views.patient_view, name='patient_view')

]
