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
            msg = f'''
                <!DOCTYPE html>
                <html>
                <head>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            line-height: 1.6;
                            padding: 20px;
                        }}
                        .container {{
                            max-width: 600px;
                            margin: auto;
                            padding: 20px;
                            color: #ffffff;
                            background-image: linear-gradient(-45deg, rgb(113, 0, 0), black, black, rgb(109, 2, 109));
                            border-radius: 10px;
                            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        }}
                        .header {{
                            text-align: center;
                            margin-bottom: 20px;
                        }}
                        .header h1{{
                            font-size: 40px;
                            font-weight: bolder;
                            color: rgb(255, 196, 0);
                        }}
                        .otp {{
                            font-size: 24px;
                            font-weight: bold;
                            letter-spacing: 0.5cap;
                            color: rgb(255, 196, 0);
                            text-align: center;
                        }}
                        .button {{
                            display: inline-block;
                            margin-top: 20px;
                            padding: 10px 20px;
                            font-weight: bold;
                            background-color: rgb(255, 196, 0);
                            color: rgb(0, 0, 0);
                            text-decoration: none;
                            border-radius: 5px;
                        }}
                        .footer {{
                            margin-top: 30px;
                            text-align: center;
                            color: #666;
                            font-size: 12px;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            <h1>SAI MUSIC</h1>
                        </div>
                        <p>Hello,</p>
                        <p>To ensure the security of your account and To complete your verification, Please enter the following OTP provided below:</p>
                        <p class="otp">{otp}</p>
                        <p>Enter this code on the verification page to confirm your identity.It is valid for 2 minutes only.</p>
                        <center><a href="https://saimusic.pythonanywhere.com" class="button">Explore</a></center>
                        <div class="footer">
                            <p>If you did not request this verification, please ignore this email.</p>
                            <p>&copy; 2024 . SAIMUSIC . All rights reserved.</p>
                        </div>
                    </div>
                </body>
                </html>
                '''
            # '<p>Your OTP : <b>'+str(otp)+'</b></p>'
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

def check_status(request):
    return render(request, 'check_status.html')

def booking(request):
    return render(request, 'booking.html')

def booking_dj(request):
    return render(request, 'booking_dj.html')

def booking_others(request):
    return render(request, 'booking_others.html')
    
def booking_date(request):
    return render(request, 'booking_date.html')

def comming_soon(request):
    return render(request, 'comming_soon.html')