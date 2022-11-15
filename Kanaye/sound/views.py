from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Track, Album


class HomeView(ListView):
    model = Track
    template_name = 'sound/index.html'
    context_object_name = 'tracks'


class AlbumView(DetailView):
    model = Album
    template_name = 'sound/album.html'
    context_object_name = 'albums'
    slug_url_kwarg = 'album_slug'

    def get_queryset(self):
        return Album.objects.filter(slug=self.kwargs.get('album_slug'))

