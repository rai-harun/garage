from django.shortcuts import render

# Create your views here.
def SchoolAdminLogin(request):
    return render(request, 'schooladmin/login.html')