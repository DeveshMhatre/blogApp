from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import RegisterForm

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
