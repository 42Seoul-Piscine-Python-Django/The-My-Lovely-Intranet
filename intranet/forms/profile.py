from typing import Any, Dict
from django import forms
from django.forms.widgets import Textarea


class ProfileForm(forms.Form):
    name = forms.CharField(
        max_length=32, help_text="Write your name.", required=True)
    surname = forms.CharField(
        max_length=32, help_text="Write your surname.", required=True)
    email = forms.EmailField(
        max_length=128, help_text='Write your email.', required=True)
    description = forms.CharField(
        widget=Textarea(),
        max_length=512, help_text='Write your description.', required=False)
    # TODO File form에 대해서 공부해서 알맞는 값으로 변경하기!
    profileImage = forms.FileField()

    # TODO: 프로파일 Clean Method 완성하기! 필요 없을 지도?????
    def clean(self) -> Dict[str, Any]:
        return super().clean()
