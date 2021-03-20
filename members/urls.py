from django.urls import path
from .views import UserRegister, UserEdit, PasswordsChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('edit_profile/', UserEdit.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'))
]