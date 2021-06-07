from django.urls import path
from intranet import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "intranet"

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('post/', views.PostView.as_view(), name='post'),
    path('post/<int:post_id>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:post_id>/edit', views.PostEditView.as_view(), name='post-edit'),
    path('profile/<slug:user_id>', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/<slug:user_id>/edit', views.ProfileEditView.as_view(), name='profile-edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
