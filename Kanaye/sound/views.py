from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Track, Album

from basic_services.scrap_vk import get_vk


class HomeView(ListView):
    model = Track
    template_name = 'sound/index.html'
    context_object_name = 'tracks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user_vk = self.request.user.vk
            vk_links = user_vk.replace('https://vk.com/', '')
            context['all_items'] = get_vk(vk_links)
        return context


class AlbumView(DetailView):
    model = Album
    template_name = 'sound/album.html'
    context_object_name = 'albums'
    slug_url_kwarg = 'album_slug'

    def get_queryset(self):
        return Album.objects.filter(slug=self.kwargs.get('album_slug'))

