from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def admin_create(request):
    return render(request, 'admin_create.html')