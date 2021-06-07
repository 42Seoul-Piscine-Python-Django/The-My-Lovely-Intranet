from typing import Any, Dict
from django import forms
from django.forms.widgets import Textarea
from intranet.models import ProfileModel, User


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    profile_image = forms.ImageField(required=False)
    description = forms.CharField(max_length=512, required=False)
    class Meta:
        model = User 
        fields = ['surname','name','profile_image', 'description']
