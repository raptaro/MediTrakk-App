from django import forms
from django.forms import ModelForm, TextInput, EmailInput, DateInput
from .models import Patient

class PatientForm(ModelForm):
    PRIORITY_CHOICES = [
        ('Regular', 'Regular'),
        ('Priority', 'Priority Lane (PWD/Pregnant)')
    ]
    COMPLAINT_CHOICES = [
        ('general_illness', 'General Illness'),
        ('injury', 'Injury'),
        ('checkup', 'Check-up'),
        ('other', 'Other'),
    ]
    priority_level = forms.ChoiceField(
        choices=PRIORITY_CHOICES, 
        label= "Priority Level",
        initial="Regular",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    complaint = forms.ChoiceField(
        choices=COMPLAINT_CHOICES,
        label= "Complaint",
        initial="checkup",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Patient
        exclude = ['patient_id']
        labels = {
            'first_name': 'First Name',
            'middle_name' : 'Middle Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'date_of_birth' : 'Date of Birth',
            'street_address': 'Street Address',
            'barangay': 'Barangay',
            'municipal_city': 'Municipal City',
        }
        help_texts = {
            'phone_number': 'Enter an 11-digit phone number without spaces or dashes.',
        }
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'middle_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'date_of_birth' : DateInput(attrs={'type' : 'date', 'placeholder' : 'd/mm/yyyy' }),
            'street_address': TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Address'}),
            'barangay': TextInput(attrs={'class': 'form-control', 'placeholder': 'Barangay'}),
            'municipal_city': TextInput(attrs={'class': 'form-control', 'placeholder': 'Municipal City'}),
        }