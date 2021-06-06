from intranet.models.post import PostModel
from django.views.generic import ListView
from django.shortcuts import render


class Main(ListView):
    paginate_by = 10
    template_name = 'intranet/pages/main/main.html'
    model = PostModel
    queryset = model.objects.all().order_by('-id')
