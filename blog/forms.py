from django import forms

from .models import Article

class CreateArticleForm(forms.ModelForm):
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