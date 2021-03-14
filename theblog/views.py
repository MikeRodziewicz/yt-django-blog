from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class HomeView(ListView):
    """Renders home page"""
    model = Post
    template_name = 'home.html'


class PostDetail(DetailView):
    """Renders details view of a post"""
    model = Post
    template_name = "post_detail.html"
    