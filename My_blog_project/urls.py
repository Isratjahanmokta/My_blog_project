from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
<<<<<<< HEAD
from django.conf import settings

=======
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
>>>>>>> 152a3f39e864c2cc767631392f1a1657c2b8a985

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include("App_login.urls")),
    path('blog/',include('App_blog.urls')),
    path('', views.Index, name='Index'),
]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_root)