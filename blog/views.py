from django.shortcuts import render, redirect, reverse,  get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Article
from .forms import CreateArticleForm

@login_required(login_url='accounts:login')
def article_list(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {
        'latest_article_list': latest_article_list
    }
    return render(request, 'blog/article_list.html', context)

@login_required(login_url='accounts:login')
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article
    }
    return render(request, 'blog/article_detail.html', context)

# Create
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
