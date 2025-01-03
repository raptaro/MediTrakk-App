from django.db import models
import random
import string


class Patient(models.Model):
    patient_id = models.CharField(max_length=8, unique=True, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    # address =    
    
    def generate_patient_id(self):
    # Generate a random 8-character alphanumeric string
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def save(self, *args, **kwargs):
        if not self.patient_id:
            self.patient_id = self.generate_patient_id()
            while Patient.objects.filter(patient_id = self.patient_id).exists():
                self.patient_id = self.generate_patient_id()                 
        super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class TemporaryStorageQueue(models.Model):
    PRIORITY_CHOICES = [
        ('Regular', 'Regular'),
        ('Priority', 'Priority Lane (PWD/Pregnant)')
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='patient_id' )
    priority_level = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Regular')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices = [
        ('Waiting', 'Waiting'), 
        ('Being Assessed', 'Being Assessed'), 
        ('Queued for Treatment', 'Queued for Treatment'),
        ('Completed', 'Completed'),
        ], default='Waiting')

    class Meta:
        unique_together = ('patient',)
class PreliminaryAssessment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='patient_id' )
    symptoms = models.TextField(max_length=200)
    assessment = models.TextField(max_length=200, default='No assessment provided yet')
    assessment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Preliminary Assessment for {self.patient.first_name} {self.patient.last_name}'

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

