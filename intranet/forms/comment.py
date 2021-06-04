from typing import Any, Dict
from django import forms


# TODO: 대댓글에 대한 구조는 추후에 다시 고민 해보기로!
class CommentForm(forms.Form):
    comment = forms.CharField(
        max_length=512, help_text="Please wirte comment.", required=True)

    # TODO: 댓글 Clean Method 완성하기! 필요 없을 지도?????
    def clean(self) -> Dict[str, Any]:
        return super().clean()
