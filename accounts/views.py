from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm

def register_user(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in!')
        return redirect('blog:articles')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user=user)
            messages.success(request, 'User registered successfully!')
            return redirect('blog:articles')
        else:
            messages.warning(request, 'Please correct the errors below:')
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)

def login_user(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in!')
        return redirect('blog:articles')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user=user)
                messages.success(request, 'Signed in successfully')
                return redirect('blog:articles')
            else:
                messages.warning(request, 'The Username or Password is incorrect. Please try again.')
    else:
        form = LoginForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, 'You successfully logged out.')
    return redirect('accounts:login')
