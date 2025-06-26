from django.shortcuts import render
import sys
import io
from django.http import HttpResponse
def home(request):
    return render(request, 'compiler/home.html')
def welcome(request):
    return render(request,'index.html')
def sign_page(request):
    return render(request, 'sign.html')
def login_page(request):
    return render(request, 'compiler\log.html')