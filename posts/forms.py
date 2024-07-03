from django import forms
from .models import Post,Review

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        #fields='__all__'
        exclude=('user',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        #fields='__all__'
        fields=['user','content','rate']

        
