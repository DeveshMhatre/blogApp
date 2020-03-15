from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:articles')
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user=user)
                return redirect('blog:articles')
    else:
        form = LoginForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('accounts:login')
