from typing import Any, Dict
from django import forms
from intranet.models.comment import CommentModel

class CommentForm(forms.ModelForm):
    parent = forms.CharField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = CommentModel
        fields = ['comment',]
