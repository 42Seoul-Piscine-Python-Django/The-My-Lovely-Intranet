from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from intranet.models.post import PostModel
from django.views.generic import ListView
from django.shortcuts import render


class Main(LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('intranet:login')
    paginate_by = 10
    template_name = 'intranet/pages/main/main.html'
    model = PostModel
    queryset = model.objects.filter(is_active=True).order_by('-id')
