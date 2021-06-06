from django.forms.widgets import Textarea
from intranet.models.post import PostModel
from typing import Any, Dict
from django import forms


class PostForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget=Textarea())

    class Meta:
        model = PostModel
        fields = ['title', 'content']

