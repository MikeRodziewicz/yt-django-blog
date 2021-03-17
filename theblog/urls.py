from django.urls import path
from .views import HomeView, PostDetail, AddPost, UpdatePost, DeletePost, AddCategory, ListCategory, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog_post/<int:pk>', PostDetail.as_view(), name="blog-detail" ),
    path('add_post/', AddPost.as_view(), name="add_post"),
    path('add_category/', AddCategory.as_view(), name="add_category"),
    path('blog_post/update_post/<int:pk>', UpdatePost.as_view(), name="update-post"),
    path('blog_post/<int:pk>/delete_post/', DeletePost.as_view(), name="delete-post"),
    path('categories/', ListCategory.as_view(), name="categories"),
    path('category/<str:cats>', CategoryView, name='category'),

]