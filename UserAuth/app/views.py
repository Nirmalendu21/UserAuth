from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import UserProfile  
from .models import User
from django.http import HttpResponse

def register(request):
     if request.method == 'POST': 
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name'] 
        email = request.POST['email'] 
        username = request.POST['username'] 
        password = request.POST['password']

        users = User()
        users.first_name = first_name
        users.last_name = last_name
        users.username = username
        users.email = email
        users.set_password(password)
        users.save()

        return redirect('login')
     else:
        return redirect('register')
      
     return render(request, 'Users/register.html')

def verify(request): 
    if request.method == 'POST': 
        email = request.POST['email'] 
        otp = request.POST['otp']

        user = User.objects.filter(email=email).first()

        if not user or user.otp != otp:
          return render(request, 'Users/verify2.html', {'bad_login': 'Incorrect Password'})

        user.otp = None
        user.save()

    return render(request, 'success.html')
    else:
      return render(request, 'Users/verify1.html')

def login(request):
   if request.method == 'POST': 
        Username = request.POST['email'] 
        otp = request.POST['otp']

        user = User.objects.filter(email=Username).first()

        if not user or user.otp != otp:
          return render(request, 'Users/verify2.html', {'bad_login': 'Incorrect Password'})

        user.otp = None
        user.save()

    return render(request, 'success.html')
   
   

def forgot_password(request):
     if request.method == 'POST': 
         return render(request, 'register')
     
def reset_password(request):
    if request.method == 'POST': 
         return render(request, 'register')


     

