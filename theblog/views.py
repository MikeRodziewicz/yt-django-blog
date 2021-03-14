from django.shortcuts import render


def home(request):
    """render home page"""
    return render(request, 'home.html', {})