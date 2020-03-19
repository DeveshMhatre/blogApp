from django.shortcuts import render, redirect, reverse,  get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Article
from .forms import ArticleForm, UserUpdateForm

# Views for guest users
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
def user_profile(request):
    user_id = request.user.id

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

# Create
# View for creating new articles
@login_required(login_url='accounts:login')
def article_create(request):
    user_id = request.user.id

    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST)
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
        form = ArticleForm()

    context = {
        'form': form
    }
    
    return render(request, 'blog/article_create.html', context)

# Read
# View for listing articles posted by a user
@login_required(login_url='accounts:login')
def list_user_articles(request):
    user_id = request.user.id

    user = User.objects.get(pk=user_id)

    articles = user.article_set.all()

    context = {
        'articles': articles
    }

    return render(request, 'blog/list_user_articles.html', context)

# Update
# View for updating user articles
@login_required(login_url='accounts:login')
def update_user_article(request, article_id):
    user_id = request.user.id

    user = User.objects.get(pk=user_id)

    articles = user.article_set.all()

    article = get_object_or_404(articles, pk=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article updated successfully.')
        else:
            messages.warning(request, 'Please correct the errors below:')
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'form': form,
        'article': article
    }

    return render(request, 'blog/update_user_article.html', context)

# Delete
# View for deleting user articles
def delete_user_article(request, article_id):
    user_id = request.user.id

    user = User.objects.get(pk=user_id)

    articles = user.article_set.all()

    article = get_object_or_404(articles, pk=article_id)

    article.delete()
    messages.success(request, 'Article deleted successfully.')
    return redirect('blog:user_articles')
