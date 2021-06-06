from django.http import request
from django.http.response import HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.detail import DetailView
from intranet.models import PostModel
from intranet.forms import PostForm


class PostView(LoginRequiredMixin, FormView):
    template_name = 'intranet/pages/post/new.html'
    form_class = PostForm
    success_url = reverse_lazy('intranet:main')
    login_url = reverse_lazy('intranet:login')

    def form_valid(self, form: PostForm) -> HttpResponse:
        post: PostModel = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

    def form_invalid(self, form: PostForm) -> HttpResponse:
        return super().form_invalid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'intranet/pages/post/post.html'
    login_url = reverse_lazy('intranet:login')
    model = PostModel
    pk_url_kwarg = 'post_id'
