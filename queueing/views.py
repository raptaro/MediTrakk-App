from django.shortcuts import get_object_or_404, render, redirect
from .models import Patient, TemporaryStorageQueue
from .forms import PreliminaryAssessmentForm


# Create your views here.
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

def accept_patient(request, patient_id):
    queue_entry = get_object_or_404(TemporaryStorageQueue, patient__patient_id=patient_id)
    queue_entry.status = 'Being Assessed'
    queue_entry.save()
    return redirect('queueing:preliminary_assessment', patient_id=patient_id)

# Preliminary Assessment View
def preliminary_assessment(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id) # Use get_object_or_404
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
            return redirect('queueing:treatment_queue')
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
    return redirect('queueing:treatment_queue')