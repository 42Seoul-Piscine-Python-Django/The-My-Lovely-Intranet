from django.contrib.auth import login
from django.http.response import HttpResponse
from intranet.models.user import User
from django.contrib import messages
from django.urls.base import reverse_lazy
from intranet.forms.user import UserCreationForm
from django.views.generic import FormView


class RegisterView(FormView):
    template_name = 'intranet/pages/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('intranet:main')

    def form_valid(self, form: UserCreationForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Registration successful.")
        return super().form_valid(form)

    def form_invalid(self, form: UserCreationForm) -> HttpResponse:
        messages.error(self.request, "Registration unsuccessful.")
        return super().form_invalid(form)
