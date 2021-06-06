from django.urls import path
from intranet import views

app_name = "intranet"

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('post/', views.PostView.as_view(), name='post'),
    path('login/', views.LoginView.as_view(), name='login')
]
