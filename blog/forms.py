from django import forms
from django.contrib.auth.models import User

from .models import Article

class ArticleForm(forms.ModelForm):
    article_title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Title',
                'class': 'form__input--text',
            }
        ),
    )
    article_body = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Your article here...',
                'class': 'form__input--textarea',
                'rows': 7,
            }
        ),
    )
    class Meta:
        model = Article
        fields = ['article_title', 'article_body']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        labels = {
            'username': 'Your username',
            'email': 'Your email address',
            'first_name': 'Your first name',
            'last_name': 'Your last name'
        }

class PasswordUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']
        labels = {
            'password': 'Your old passoword',
        }
        widgets = {
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Enter your old password'
                }
            )
        }
