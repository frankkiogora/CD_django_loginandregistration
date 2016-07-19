from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    return render(request, 'loginapps/index.html')

def register(request):
    if User.userManager.isValidRegistration(request.POST, request):
        passFlag = True
        return redirect ('/success')
    else:
        passFlag = False
        return redirect('/')

def success(request):
    return render(request, 'loginapps/success.html')

def login(request):
    if User.userManager.UserExistsLogin(request.POST, request):
        passFlag = True
        return redirect ('/success')
    else:
        passFlag = False
        return redirect ('/')
