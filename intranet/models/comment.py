from intranet.models.post import PostModel
from django.conf import settings
from django.db import models

from .post import PostModel

# TODO: 대댓글 생각 해보고 나중에 변경하기!
class CommentModel(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='email')
    comment = models.CharField(
        max_length=512, null=False)
    creationDate = models.DateTimeField(
        auto_now_add=True, null=False)
    updateDate = models.DateTimeField(
        auto_now=True, null=False)

# yongjule - add comment (i dont know its work or not)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('creationDate',)

    def __str__(self):
        return self.comment

    def get_comments(self):
        return CommentModel.objects.filter(parent=self).filter(active=True)
