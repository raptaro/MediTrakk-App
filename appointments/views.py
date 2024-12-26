from django.shortcuts import render, redirect
from .models import Patient, Appointment
from .forms import PatientForm, AppointmentForm

def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
        
    context = {'form' : form}
    
    return render(request, 'patient_register.html', context)

def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save() 
    else:
        form = AppointmentForm()

    context = {'form' :  form}

    return render(request, 'schedule_appointment.html', context)

def patient_list(request):
    patients = Patient.objects.all()
    context = {'patients' : patients}

    return render(request, 'patient_list.html', context)

def appointment_list(request):
    appointments = Appointment.objects.all()
    context = {'appointments' : appointments}

    return render(request, 'appointment_list.html', context)