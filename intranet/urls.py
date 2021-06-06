from django.urls import path
from intranet import views

app_name = "intranet"

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
]
