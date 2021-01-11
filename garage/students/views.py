from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def StudentsLogin(request):
    return render(request, 'students/login.html')
