from django.urls import path
from .views import HomeView, PostDetail, AddPost

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog_post/<int:pk>', PostDetail.as_view(), name="blog-detail" ),
    path('add_post/', AddPost.as_view(), name="add_post"),
]