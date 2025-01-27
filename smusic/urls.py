"""
URL configuration for smusic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin2/', admin.site.urls),
    path('', views.home, name='home'),
    path('admin/', views.admin_login, name='admin_login'),
    path('admin_create/', views.admin_create, name='admin_create'),
    path('admin_verification/<int:admin_user_id>/', views.admin_verification, name='admin_verification'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('check_status/', views.check_status, name='check_status'),

    # Booking
    path('booking/', views.booking, name='booking'),
    path('booking_dj/', views.booking_dj, name='booking_dj'),
    path('booking_others/', views.booking_others, name='booking_others'),
    path('booking_date/', views.booking_date, name='booking_date'),

    # Others
    path('comming_soon/', views.comming_soon, name='comming_soon'),
]
