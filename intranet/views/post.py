from django.views import View
from django.shortcuts import render
from .models import PostModel

def post_list(request):
    posts = PostModel.objects
    return render(request, 'post_list.html', {'posts':posts})
