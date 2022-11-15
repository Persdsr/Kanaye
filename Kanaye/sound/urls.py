from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('album/<slug:album_slug>/', views.AlbumView.as_view(), name='album'),
]