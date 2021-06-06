from typing import Any
from django import http
from django.urls import reverse_lazy
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseBase
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from intranet.forms.user import UserLoginFrom


class LogoutView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('intranet:main')
    login_url = reverse_lazy('intranet:login')

    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        logout(request)
        return super().get(request, *args, **kwargs)
