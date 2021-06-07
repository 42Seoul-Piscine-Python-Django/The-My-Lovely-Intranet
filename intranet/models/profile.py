from typing import Any, Dict
from django.db import models 
from intranet.models import User
from intranet.models.user import path_and_rename

class ProfileModel(models.Model):
    user = models.OneToOneField(User,
        on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    email = models.EmailField(
        max_length=128, null=True)
    name = models.CharField(
        max_length=64, null=True)
    surname = models.CharField(
        max_length=64, null=True)
    description = models.CharField(
        max_length=512, null=False)
    profile_image = models.ImageField(
            upload_to=path_and_rename, blank=True, null=False)

    class Meta:
        ordering = ('surname',)

    def __str__(self):
        return '{} Profile'.format(self.user.id)
