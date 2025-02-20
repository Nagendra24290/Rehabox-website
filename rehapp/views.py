from django.shortcuts import render
from  django.http import HttpResponse
from .models import Patient


def home(request):
    return render(request,'index.html')
def patientportal(request):
    Post = Patient.objects.all()  # Fetch all patient records
    print(Post)  # Debug: Print the queryset to the console
    return render(request, 'patientportal.html', {'Post': Post})






