from django.views import View
from django.shortcuts import render


class Main(View):
    template_name = 'intranet/pages/main/main.html'

    def get(self, request):
        return render(request, self.template_name)
