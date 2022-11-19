from unicodedata import name
from django.urls import path
from App_blog import views

app_name = 'App_blog'

urlpatterns = [
    path('', views.Bloglist.as_view(), name = 'blog_list'),
    path('write/', views.CreateBlog.as_view(), name = 'create_blog'),
    path('<slug:slug>/', views.blog_details, name = 'blog_details'),
    path('liked/<pk>/', views.Liked, name = 'liked_post'),
    path('Unliked/<pk>/', views.Unliked, name = 'Unliked_post'),
    path('my_blogs/', views.MyBlogs.as_view(), name = 'my_blogs'),
    path('edit/<pk>/', views.UpdateBlog.as_view(), name = 'edit_blog'),
]
