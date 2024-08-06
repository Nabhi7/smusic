from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import AdminUser
from django.core.mail import send_mail,EmailMultiAlternatives
import random
# Create your views here.

def home(request):
    return render(request, 'home.html')

def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            admin_user = AdminUser.objects.get(email=email)
            otp = random.randint(100000,999999)
            admin_user.otp = otp
            admin_user.save()
            sub = 'Sai Music Admin Verification'
            msg = '<p>Your OTP : <b>'+str(otp)+'</b></p>'
            femail = 'saswatkumar059@gmail.com'
            msg = EmailMultiAlternatives(sub, msg, femail,[email])
            msg.content_subtype='html'
            msg.send()
            return redirect('admin_verification', admin_user_id=admin_user.id)
        except AdminUser.DoesNotExist:
            return HttpResponse("Invalid email.")
        
    return render(request, 'admin_login.html')

def admin_verification(request, admin_user_id):
    admin_user = get_object_or_404(AdminUser, id=admin_user_id)
    if request.method == 'POST':
        otp = request.POST.get('otp')
        print(admin_user.otp)
        if int(otp) == int(admin_user.otp):
            admin_user.otp = None
            admin_user.save()
            return redirect('admin_dashboard')
        else:
            return HttpResponse("Invalid OTP.")
    return render(request, 'admin_verification.html', {'admin_user_id': admin_user.id})

def admin_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        admin_user = AdminUser(name=name, phone=phone, email=email)
        admin_user.save()
        return HttpResponse("Admin User created successfully!")
    return render(request, 'admin_create.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')