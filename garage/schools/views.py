from django.shortcuts import render

# Create your views here.

def GarageLogin(request):
    return render(request, 'schools/login.html')
