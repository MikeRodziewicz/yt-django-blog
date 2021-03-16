from django import forms
from .models import Post, Category

#TODO change so that we do not have restart the service each time a cat is added
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    """Form for creating posts"""
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    """Form for updating posts"""
    class Meta:
        model = Post
        fields = ('title', 'title_tag','category', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'something'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }
