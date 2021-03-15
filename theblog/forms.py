from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Form for creating posts"""
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'something'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    """Form for updating posts"""
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'something'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }
