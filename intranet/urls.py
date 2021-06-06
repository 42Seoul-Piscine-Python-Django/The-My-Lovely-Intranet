from django.urls import path
from intranet import views

app_name = "intranet"

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('post/', views.PostView.as_view(), name='post'),
    path('post/<int:post_id>', views.PostDetailView.as_view(), name='post-detail'),
    # path('post/<int:post_id>', views.PostDetailView.as_view(), name='post-detail'),
]
