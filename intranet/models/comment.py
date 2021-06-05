from intranet.models.post import PostModel
from django.conf import settings
from django.db import models


# TODO: 대댓글 생각 해보고 나중에 변경하기!
class CommentModel(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username')
    comment = models.CharField(
        max_length=512, null=False)
    creationDate = models.DateTimeField(
        auto_now_add=True, null=False)
    updateDate = models.DateTimeField(
        auto_now=True, null=False)
