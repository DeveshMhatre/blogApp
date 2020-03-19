from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_list, name='articles'),
    path('article/<int:article_id>', views.article_detail, name='article'),

    # User profile
    path('user', views.user_profile, name='user_profile'),

    # CRUD
    path('user/article/create', views.article_create, name='create_article'),
    path('user/articles', views.list_user_articles, name='user_articles'),
    path('user/article/update/<int:article_id>', views.update_user_article, name='update_article'),
    path('user/article/delete/<int:article_id>', views.delete_user_article, name='delete_article'),
]
