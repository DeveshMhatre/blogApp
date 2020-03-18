from django.shortcuts import render, redirect, reverse,  get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Article
from .forms import CreateArticleForm, UserUpdateForm

def article_list(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {
        'latest_article_list': latest_article_list
    }
    return render(request, 'blog/article_list.html', context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article
    }
    return render(request, 'blog/article_detail.html', context)

# User profile
# View for user profile, from which a user can CRUD their articles
@login_required(login_url='accounts:login')
def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully.')
        else:
            messages.warning(request, 'Please correct the errors below:')
    
    else:
        form = UserUpdateForm(instance=user)

    context = {
        'form': form
    }

    return render(request, 'blog/user_profile.html', context)

@login_required(login_url='accounts:login')
def update_user_articles(request, user_id):
    user = User.objects.get(pk=user_id)

    articles = user.article_set.all()

    context = {
        'articles': articles
    }

    return render(request, 'blog/update_user_articles.html', context)

# Create
# View for creating new articles
@login_required(login_url='accounts:login')
def article_create(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            # In order to pre-assign user
            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            article_id = instance.user.article_set.all()[0].id
            messages.success(request, 'Article posted successfully.')
            return HttpResponseRedirect(reverse('blog:article', args=[article_id]))
        else:
            messages.warning(request, 'Please correct the errors below:')
    else:
        form = CreateArticleForm()

    context = {
        'form': form
    }
    
    return render(request, 'blog/article_create.html', context)

def delete_user_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()
    messages.success(request, 'Article deleted successfully.')
    return HttpResponseRedirect(reverse('blog:user_articles', args=[request.user.id]))