from django.http import request
from django.http.response import HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import render
from intranet.models import PostModel
from intranet.forms import PostForm


class PostView(FormView):
    template_name = 'intranet/pages/post/post.html'
    form_class = PostForm
    success_url = reverse_lazy('intranet:main')

    def form_valid(self, form: PostForm) -> HttpResponse:
        post: PostModel = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

    def form_invalid(self, form: PostForm) -> HttpResponse:
        return super().form_invalid(form)
