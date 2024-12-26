from django.contrib import admin
from .models import Appointment, Patient

class PatientAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']  # Fields you want to search by

admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    search_fields = ['patient__first_name', 'patient__last_name', 'reason']  # Search by patient details
    autocomplete_fields = ['patient']  # Enables dropdown with search functionality

admin.site.register(Appointment, AppointmentAdmin)
