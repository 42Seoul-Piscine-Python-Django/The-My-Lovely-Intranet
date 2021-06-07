from typing import Any, Dict
from django import forms
from intranet.models import CommentModel

class CommentForm(forms.ModelForm):
    parent = forms.CharField(widget=forms.HiddenInput, required=False)
    comment = forms.CharField(help_text="Please wirte comment.")

    class Meta:
        model = CommentModel
        fields = ['comment',]
