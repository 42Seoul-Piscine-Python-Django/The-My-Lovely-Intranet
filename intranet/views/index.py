from django.http.response import HttpResponse
from django.views import View
from django.shortcuts import render


class Index(View):
    template_name = 'pages/main/main.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return HttpResponse('hello world!')
