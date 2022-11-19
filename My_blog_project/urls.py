from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('App_login.urls')),
    path('blog/',include('App_blog.urls')),
    path('',views.Index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)