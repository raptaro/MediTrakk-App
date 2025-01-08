from django.db import models
from patient.models import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='patient_id')
    date_time = models.DateTimeField()
    reason = models.CharField(max_length=255)
    # doctor = 
    status = models.CharField(max_length=50, choices=[
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ])

    def __str__(self):
        return f"Appointment for {self.patient} on {self.date_time.strftime('%Y-%m-%d %H:%M')}"

