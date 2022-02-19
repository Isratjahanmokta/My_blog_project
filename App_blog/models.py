from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=264, verbose_name="put a title")
    slug = models.SlugField(max_length=200, unique=True)
    blog_content = models.TextField(verbose_name = 'What is in my mind?')
    blog_image = models.ImageField(upload_to= 'blog_image', verbose_name="image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name= 'blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_comment')
    Comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Likes(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE, related_name= 'liked_blog')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name= 'Liked_user')
