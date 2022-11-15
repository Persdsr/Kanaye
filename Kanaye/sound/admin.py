from django.contrib import admin

from . import models


@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    pass
