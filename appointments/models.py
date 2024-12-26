from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Appointment(models.Model):
    patient =  models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
        ])
    def __str__(self):
            return f"Appointment for {self.patient} on {self.date_time.strftime('%Y-%m-%d %H:%M')}"
