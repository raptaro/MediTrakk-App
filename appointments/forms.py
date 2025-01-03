from django import forms
from django.forms import ModelForm, TextInput, EmailInput, DateTimeInput, Select, CharField
from .models import Patient, Appointment,PreliminaryAssessment

class PatientForm(ModelForm):
    PRIORITY_CHOICES = [
        ('Regular', 'Regular'),
        ('Priority', 'Priority Lane (PWD/Pregnant)')
    ]
    priority_level = forms.ChoiceField(
        choices=PRIORITY_CHOICES, 
        label= "Priority Level",
        initial="Regular",
        widget=forms.Select(attrs={'class': 'form-control'})

    )

    class Meta:
        model = Patient
        exclude = ['patient_id']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
        }
        help_texts = {
            'phone_number': 'Enter an 11-digit phone number without spaces or dashes.',
        }
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }
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
