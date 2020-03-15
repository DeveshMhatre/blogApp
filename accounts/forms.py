from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter username',
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter email address'
            }
        ),
    )
    password1 = forms.CharField(
        max_length=50,
        min_length=8,
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter password'
            }
        )
    )
    password2 = forms.CharField(
        max_length=50,
        min_length=8,
        label='Repeat password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm password'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')