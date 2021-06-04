from typing import Any, Dict
from django import forms


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=128, help_text="Please write title.", required=True)
    content = forms.CharField(
        help_text="Please write post content.", required=True)

    # TODO: 게시글 Clean Method 완성하기! 필요 없을 지도?????
    def clean(self) -> Dict[str, Any]:
        return super().clean()
