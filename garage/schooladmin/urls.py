from django.urls import path
from . import views

urlpatterns = [
    path('', views.SchoolAdminLogin, name="schooladminlogin"),     
]
