from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import login, authenticate
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput
from django.http.request import HttpRequest

from intranet.models import User


class UserLoginFrom(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=PasswordInput)

    class AuthFail(Exception):
        def __str__(self) -> str:
            return 'authenticate fail'

    def login(self, request: HttpRequest):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        print(
            email, password
        )
        user = authenticate(
            request=request,
            email=email,
            password=password,
        )
        print(user)
        if user is None:
            raise self.AuthFail()
        return login(request, user)


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'name', 'surname')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'surname', 'description',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]
