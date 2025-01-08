from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import  Appointment
from patient.models import Patient
from .forms import PatientForm, AppointmentForm, PreliminaryAssessmentForm

def schedule_appointment(request):  
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()

    context = {'form' :  form,}

    return render(request, 'schedule_appointment.html', context)

# def patient_list(request):
#     patients = Patient.objects.all()
#     context = {'patients' : patients}

#     return render(request, 'patient_list.html', context)

def appointment_list(request):
    # patient = Patient.objects.get(patient_=pk)
    appointments = Appointment.objects.all()
    context = {'appointments' : appointments}

    return render(request, 'appointment_list.html', context)





