from django import forms
from django.forms import ModelForm, TextInput, EmailInput, DateTimeInput, Select, CharField
from .models import PreliminaryAssessment
from appointments.models import Appointment

class PreliminaryAssessmentForm(ModelForm):
    
    class Meta:
        model = PreliminaryAssessment
        fields = ['symptoms', 'assessment']


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
   
        labels = {
            'patient': 'Patient',
            'date_time': 'Appointment Date & Time',
            'reason': 'Reason for Appointment',
            'status': 'Status',
        }
        widgets = {
            'date_time': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'reason': TextInput(attrs={'class': 'form-control', 'placeholder': 'Reason'}),
            'status': Select(attrs={'class': 'form-select'}),
        }
    
class PreliminaryAssessmentForm(ModelForm):
    
    class Meta:
        model = PreliminaryAssessment
        fields = ['symptoms', 'assessment']
