from . import views

from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('accounts/signup/', views.SignUp, name='signup'),
    path('accounts/login/', views.Login.as_view(), name='login'),
    path('accounts/profile/<username>/', views.Profile, name='profile'),
    path('accounts/update-profile/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('posts/create/', views.PostCreate, name='post_create'),
    path('posts/<int:pk>/', views.PostView.as_view(), name='post'),
    path('posts/update-post/<int:pk>/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

