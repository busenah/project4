from django.shortcuts import render

# Create your views here.

from .models import Doctor, Patient


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'project4/doctor_list.html', {'doctors': doctors})
