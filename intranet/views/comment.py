from typing import Any, Dict
from django import http
from django.contrib import messages
from django.http import request
from django.http.response import HttpResponse, Http404
from django.urls.base import reverse_lazy, reverse
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from intranet.models import User
from intranet.forms import CommentForm


class CommentView(LoginRequiredMixin, FormView):
    form_class = CommentForm
    
    def get(self, *args, **kwargs):
        raise Http404

    def get_initial(self) -> Dict[str, Any]:
        post: CommentModel = self.instance
        initial = super().get_initial()
        initial['comment'] = post.comment
        return initial

    def form_valid(self, form: CommentForm) -> HttpResponse:
        self.instance.comment = form.cleaned_data['comment'] #권한?? 흠...
        self.instance.save()
        return super().form_valid(form)

    def form_invalid(self, form: CommentForm) -> HttpResponse:
        return super().form_invalid(form)
