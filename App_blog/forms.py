from django import forms 
from App_blog.models import Blog, Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)