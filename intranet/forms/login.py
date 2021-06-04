from django.conf import settings
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ("username",  "password1", "password2")
