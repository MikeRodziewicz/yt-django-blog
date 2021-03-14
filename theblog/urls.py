from django.urls import path
from .views import HomeView, PostDetail

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog_post/<int:pk>', PostDetail.as_view(), name="blog-detail" ),
]