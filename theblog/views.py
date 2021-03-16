from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditPostForm
from django.urls import reverse_lazy

class HomeView(ListView):
    """Renders home page"""
    model = Post
    template_name = 'home.html'
    ordering = ['-publication_date']


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


class DeletePost(DeleteView):
    """Deleting single post entry"""
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCategory(CreateView):
    """Create new post category"""
    model = Category
    fields = "__all__"
    template_name = 'add_category.html'

class ListCategory(ListView):
    """Lists all available categories"""
    model = Category
    template_name = 'list_category.html'
