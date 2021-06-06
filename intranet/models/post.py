from django.db import models
from django.conf import settings

class PostModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False)
    # TODO: User model에 대한 검증 후 다시 확인 하기!
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='email')
    content = models.TextField(null=False)
    creationDate = models.DateTimeField(auto_now_add=True, null=False)
    updateDate = models.DateTimeField(auto_now=True, null=False)
    # TODO: comments 객체와 One To Manny로 연결 할 것!
    # comments = ????

    # add comments
    class Meta:
        ordering = ('creationDate',)

    def __str__(self):
        return self.title

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True) # parent가 없고 걸러지지 않은 댓글
