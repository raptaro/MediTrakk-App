from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm
from django.contrib import messages
from queueing.models import TemporaryStorageQueue
from .models import Patient
from django.http import HttpResponseNotAllowed
from django.http import JsonResponse

# Create your views here.
def register_patient(request):

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()

            priority_level = form.cleaned_data['priority_level']

            TemporaryStorageQueue.objects.create(
                patient=patient, 
                priority_level=priority_level, 
                status = 'Waiting'
            )
            messages.success(request, f'Patient {patient.first_name} {patient.last_name} has been registered and added to the queue.')
            return redirect('queueing:registration_queueing')
    else:
        form = PatientForm()

    context = {'form' : form}
    
    return render(request, 'patient_registration.html', context)
def patient_list(request):
    patients = Patient.objects.select_related('temporarystoragequeue').all()

    context = {'patients': patients}
    return render(request, 'patient/patient_list.html', context)

def patient_view(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        patient = get_object_or_404(Patient, patient_id=patient_id)
        return render(request, 'patient/patient_view.html', {'patient': patient})
    return redirect('patients')  # Redirect if accessed without POST
