from django import forms
from .models import Blog,Comment, Hashtag

class CreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'writer', 'content', 'hashtags', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']