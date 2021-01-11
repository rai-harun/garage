from django.shortcuts import render

# Create your views here.
def ParentsLogin(request):
    return render(request, 'parents/login.html')