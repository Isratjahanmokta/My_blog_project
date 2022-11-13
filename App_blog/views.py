from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, View, TemplateView, DeleteView, DetailView
from App_blog.models import Blog, Comments, Likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

# Create your views here.
class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_blog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image',)

    def form_valid(self, form):
        blog_obj = form.save(commit = False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

class Bloglist(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_blog/blog_list.html'
    queryset = Blog.objects.order_by('-publish_date')

