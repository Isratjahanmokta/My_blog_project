from django.contrib import admin
from App_blog.models import Blog, Comments, Likes

# Register your models here.
admin.site.register(Blog)
admin.site.register(Comments)
admin.site.register(Likes)
