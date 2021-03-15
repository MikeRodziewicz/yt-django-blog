from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditPostForm


class HomeView(ListView):
    """Renders home page"""
    model = Post
    template_name = 'home.html'


class PostDetail(DetailView):
    """Renders details view of a post"""
    model = Post
    template_name = 'post_detail.html'
    

class AddPost(CreateView):
    """Create new post"""
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePost(UpdateView):
    """Update existing post"""
    model = Post
    template_name = 'edit_post.html'
    form_class = EditPostForm


