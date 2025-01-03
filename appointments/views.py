from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Patient, Appointment, TemporaryStorageQueue
from .forms import PatientForm, AppointmentForm, PreliminaryAssessmentForm

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
            return redirect('registration_queueing')
    else:
        form = PatientForm()

    context = {'form' : form}
    
    return render(request, 'patient_register.html', context)
def registration_queueing(request):
    # Fetch queues based on priority level
    regular_queue = TemporaryStorageQueue.objects.filter(status='Waiting', priority_level='Regular').order_by('created_at')
    priority_queue = TemporaryStorageQueue.objects.filter(status='Waiting', priority_level='Priority').order_by('created_at')

    # Initialize variables for regular queue
    regular_current = regular_next1 = regular_next2 = None
    if regular_queue.exists():
        regular_current = regular_queue[0]
        regular_next_entries = regular_queue[1:3]
        regular_next1 = regular_next_entries[0] if len(regular_next_entries) >= 1 else None
        regular_next2 = regular_next_entries[1] if len(regular_next_entries) >= 2 else None

    # Initialize variables for priority queue
    priority_current = priority_next1 = priority_next2 = None
    if priority_queue.exists():
        priority_current = priority_queue[0]
        priority_next_entries = priority_queue[1:3]
        priority_next1 = priority_next_entries[0] if len(priority_next_entries) >= 1 else None
        priority_next2 = priority_next_entries[1] if len(priority_next_entries) >= 2 else None

    # Pass data to the template
    context = {
        'regular_current': regular_current,
        'regular_next1': regular_next1,
        'regular_next2': regular_next2,

        'priority_current': priority_current,
        'priority_next1': priority_next1,
        'priority_next2': priority_next2,
    }

    return render(request, 'queue/registration_queueing.html', context)


# patient accept
def accept_patient(request, patient_id):
    queue_entry = get_object_or_404(TemporaryStorageQueue, patient__patient_id=patient_id)
    queue_entry.status = 'Being Assessed'
    queue_entry.save()
    return redirect('preliminary_assessment', patient_id=patient_id)

# Preliminary Assessment View
def preliminary_assessment(request, patient_id):
    patient = Patient.objects.get(patient_id=patient_id)
    if request.method == 'POST':
        form = PreliminaryAssessmentForm(request.POST)
        if form.is_valid():
            assessment = form.save(commit=False)
            assessment.patient = patient
            assessment.save()
            # Update queue status to "TreatmentPending"
            queue_entry = TemporaryStorageQueue.objects.get(patient=patient)
            queue_entry.status = 'TreatmentPending'
            queue_entry.save()
            return redirect('treatment_queue')
    else:
        form = PreliminaryAssessmentForm()
    
    context = {'form': form, 'patient': patient}
    return render(request, 'queue/preliminary_assessment.html', context)


# Treatment Queue View
def treatment_queue(request):
    # Get all patients with status "TreatmentPending"
    regular_treatment_queue = TemporaryStorageQueue.objects.filter(status='TreatmentPending', priority_level = 'Regular').order_by('created_at')
    priority_treatment_queue =  TemporaryStorageQueue.objects.filter(status='TreatmentPending', priority_level = 'Priority').order_by('created_at')

    context = {
        'regular_treatment_queue': regular_treatment_queue,
        'priority_treatment_queue' : priority_treatment_queue
    }
    return render(request, 'queue/treatment.html', context)

# Mark Treatment Completed
def complete_treatment(request, patient_id):
    queue_entry = TemporaryStorageQueue.objects.get(patient__patient_id=patient_id)
    queue_entry.status = 'Completed'
    queue_entry.save()
    return redirect('treatment_queue')

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

def patient_list(request):
    patients = Patient.objects.all()
    context = {'patients' : patients}

    return render(request, 'patient_list.html', context)

def appointment_list(request):
    # patient = Patient.objects.get(patient_=pk)
    appointments = Appointment.objects.all()
    context = {'appointments' : appointments}

    return render(request, 'appointment_list.html', context)





