from typing import Any, Dict
from django import http
from django.contrib import messages
from django.http import request
from django.http.response import Http404, HttpResponse
from django.urls.base import reverse_lazy, reverse
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from intranet.models import PostModel, CommentModel
from intranet.forms import PostForm, CommentForm


class PostUserCheckMixin:
    def dispatch(self, request: http.HttpRequest, post_id,  *args: Any, **kwargs: Any) -> HttpResponse:
        self.post_id = post_id
        try:
            post: PostModel = PostModel.objects.get(id=post_id)
        except PostModel.DoesNotExist:
            raise Http404()
        if post.author != request.user and not request.user.is_staff:
            messages.error(request, "permission denied")
            return redirect('intranet:main')
        self.instance = post
        return super().dispatch(request, post_id, *args, **kwargs)


class PostView(LoginRequiredMixin, FormView):
    template_name = 'intranet/pages/post/new.html'
    form_class = PostForm
    login_url = reverse_lazy('intranet:login')

    def get_success_url(self) -> str:
        return reverse('intranet:post-detail', args=[self.instance.id])

    def form_valid(self, form: PostForm) -> HttpResponse:
        post: PostModel = form.save(commit=False)
        post.author = self.request.user
        post.save()
        self.instance = post
        messages.success(self.request, 'Create post success!')
        return super().form_valid(form)

    def form_invalid(self, form: PostForm) -> HttpResponse:
        return super().form_invalid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'intranet/pages/post/post.html'
    login_url = reverse_lazy('intranet:login')
    model = PostModel
    pk_url_kwarg = 'post_id'

class PostEditView(LoginRequiredMixin, PostUserCheckMixin, FormView):
    template_name = 'intranet/pages/post/edit.html'
    form_class = PostForm
    login_url = reverse_lazy('intranet:login')

    def get_success_url(self) -> str:
        return reverse('intranet:post-detail', kwargs={'post_id': self.post_id})

    def get_initial(self) -> Dict[str, Any]:
        post: PostModel = self.instance
        initial = super().get_initial()
        initial['title'] = post.title
        initial['content'] = post.content
        return initial

    def form_valid(self, form: PostForm) -> HttpResponse:
        self.instance.title = form.cleaned_data['title']
        self.instance.content = form.cleaned_data['content']
        self.instance.save()
        return super().form_valid(form)

    def form_invalid(self, form: PostForm) -> HttpResponse:
        return super().form_invalid(form)
