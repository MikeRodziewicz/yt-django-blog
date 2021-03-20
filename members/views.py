from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm


class UserRegister(generic.CreateView):
    """Creates a user object"""
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserEdit(generic.UpdateView):
    """Creates a user object"""
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user