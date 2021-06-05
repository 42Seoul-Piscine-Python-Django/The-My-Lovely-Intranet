from intranet.models.post import PostModel
from typing import Any, Dict
from django import forms


class PostForm(forms.ModelForm):
    title = forms.CharField(help_text="Please write title.")
    content = forms.CharField(
        help_text="Please write post content.")

    class Meta:
        model = PostModel
        fields = ['title', 'content']

    # TODO: 게시글 Clean Method 완성하기! 필요 없을 지도?????
    def clean(self) -> Dict[str, Any]:
        return super().clean()
