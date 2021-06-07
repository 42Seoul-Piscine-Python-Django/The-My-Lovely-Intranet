from typing import Any, Dict
from django import http
from django.contrib import messages
from django.http import request
from django.http.response import HttpResponse, Http404
from django.urls.base import reverse_lazy, reverse
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from intranet.models import User
from intranet.forms import ProfileForm 

class ProfileUserCheckMixin:
    def dispatch(self, request: http.HttpRequest, user_id,  *args: Any, **kwargs: Any) -> HttpResponse:
        self.user_id = user_id
        try:
            user: User = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Http404()
        if user != request.user and not request.user.is_staff:
            messages.error(request, "permission denied")
            return redirect('intranet:main')
        self.instance = user
        return super().dispatch(request, user_id, *args, **kwargs)

class ProfileDetailView(LoginRequiredMixin ,DetailView):
    context_object_name = 'profile_user'
    template_name = 'intranet/pages/profile/profile.html'
    login_url = reverse_lazy('intranet:login')
    model = User
    pk_url_kwarg = 'user_id'

class ProfileEditView(LoginRequiredMixin, ProfileUserCheckMixin, FormView):
    context_object_name = 'profile_user'
    template_name = 'intranet/pages/profile/edit.html'
    login_url = reverse_lazy('intranet:login:edit')
    form_class = ProfileForm

    def get_success_url(self):
        return reverse('intranet:profile-detail', kwargs={'user_id': self.user_id})

    def get_initial(self):
        profile = self.instance 
        initial = super().get_initial()
        initial['name'] = profile.name
        initial['surname'] = profile.surname
        initial['email'] = profile.email
        initial['profile_image'] = profile.profile_image
        initial['description'] = profile.description
        return initial

    def form_valid(self, form):
        self.instance.name = form.cleaned_data['name']
        self.instance.surname = form.cleaned_data['surname']
        email = form.cleaned_data['email']
        self.instance.profile_image = form.cleaned_data['profile_image']
        self.instance.description = form.cleaned_data['description']
        
        if self.instance.email != email:
            try:
                User.objects.get(email=email)
                form.errors['email'] = ("email error", )
                return self.form_invalid(form)
            except User.DoesNotExist:
                pass
        self.instance.email = email
        self.instance.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
