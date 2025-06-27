from django.shortcuts import redirect, render
import sys
import io
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from .models import User
def home(request):
    return render(request, 'compiler/home.html')
def welcome(request):
    return render(request,'index.html')
def sign_page(request):
    return render(request, 'sign.html')
def login_page(request):
    return render(request, 'compiler\log.html')

def signup_view(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = make_password(request.POST['password'])  # 🔐 Hashed password

        # Save to DB
        user = User(fullname=fullname, email=email, password=password)
        user.save()
        print("Success")
        return render(request, 'success.html')  # You can create a success page or redirect as needed

    return render(request, 'sign.html')