from typing import Any, Dict
from django import forms
from intranet.models import CommentModel

# TODO: 대댓글에 대한 구조는 추후에 다시 고민 해보기로!


class CommentForm(forms.ModelForm):
    comment = forms.CharField(help_text="Please wirte comment.")

    class Meta:
        model = CommentModel
        fieds = ['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs = {'placeholder':'Comment here...', 'class':'form-control', 'rows':'5'}
    # TODO: 댓글 Clean Method 완성하기! 필요 없을 지도?????
    def clean(self) -> Dict[str, Any]:
        return super().clean()
