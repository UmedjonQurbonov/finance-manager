from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from .models import *

def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        confirm = request.POST.get('confirm_password', None)
        if not username or not email or not password:
            return render(request, 'register.html', context={
                'username': username,
                'email': email,
                'error': 'All fields are requared!'
            })
        if password != confirm:
            return render(request, 'register.html', context={
                'username': username,
                'email': email,
                'error': 'Password do not match!'
            })
        hash_password = make_password(password)
        user = User(username=username, email=email, password=hash_password)
        user.save()
        return redirect('login') 
    
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')    
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if not username or not password:
            return render(request, 'login.html', context={
                'username': username,
                'error': 'All fields are requared!'
            })
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user=user)
            return redirect('index')
        return render(request, 'index.html', context={
            'username': username,
            'error': 'All fields are requared!'
        })    

def logout_view(request):
    try:
        logout(request)
        return redirect('login')
    except Exception as err :
        return HttpResponse(str(err))     

