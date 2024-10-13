from django.db import models
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']