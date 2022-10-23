from unicodedata import name
from  django.urls import path
from App_blog import views

app_name = 'App_blog'

urlpatterns = [
    path('', views.blog_list, name = 'blog_list'),
    path('write/', views.Creat_blog.as_view(), name = 'create_blog' ),
]
