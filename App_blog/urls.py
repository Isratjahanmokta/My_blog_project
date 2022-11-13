from unicodedata import name
from django.urls import path
from App_blog import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'App_blog'

urlpatterns = [
    path('', views.Bloglist.as_view(), name = 'blog_list'),
    path('write/', views.CreateBlog.as_view(), name = 'create_blog' ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
