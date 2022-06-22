from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include("App_login.urls")),
    path('blog/',include('App_blog.urls')),
    path('', views.Index, name='Index'),
]
