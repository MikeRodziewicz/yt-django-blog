from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditPostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


#TODO copy the context manager to other views. 
class HomeView(ListView):
    """Renders home page"""
    model = Post
    template_name = 'home.html'
    ordering = ['-publication_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
   

class PostDetail(DetailView):
    """Renders details view of a post"""
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        likes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = likes.total_likes()
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        return context
    

class AddPost(CreateView):
    """Create new post"""
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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


def CategoryView(request, cats):
    """View of posts per category"""
    category_posts = Post.objects.filter(category=cats.replace('-',' ').title())
    return render(request, 'categories.html', {'cats':cats.title().replace('-',' '), 'category_posts':category_posts})

def CategoryList(request):
    """List all categories"""
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

def LikePost(request, pk):
    """Like the post function"""
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user )
    return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))