from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse

from basic_services.service import get_path_upload_track_cover, validate_size_image, get_path_upload_album, \
    get_path_upload_track_file
from oauth.models import AuthUser


class Genre(models.Model):
    """Жанр треков"""
    name = models.CharField(verbose_name='Жанр', max_length=55)
    cover = models.ImageField(
        verbose_name='Обложка жанры',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), validate_size_image],
        blank=True,
    )

    def __str__(self):
        return self.name


class Album(models.Model):
    """Модель альбомов для треков"""
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=50)
    tracks = models.ManyToManyField('Track', blank=True, related_name='album_tracks')
    description = models.TextField(max_length=1000)
    private = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to=get_path_upload_album,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), validate_size_image]
    )
    favorite_albums = models.ManyToManyField(AuthUser, verbose_name='Избранные альбомы', related_name='alboms_favorite',
                                             blank=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('album', kwargs={'album_slug': self.slug})

    def __str__(self):
        return self.name


class Track(models.Model):
    """Треки"""
    author = models.ForeignKey(AuthUser, verbose_name='Автор', on_delete=models.CASCADE, related_name='tracks_author')
    title = models.CharField(verbose_name='Название', max_length=55)
    file = models.FileField(
        verbose_name='Трек',
        upload_to=get_path_upload_track_file,
        validators=[FileExtensionValidator(['mp3', 'wav'])],

    )
    description = models.TextField(verbose_name='Описание', max_length=155)
    cover = models.ImageField(
        verbose_name='Обложка',
        upload_to=get_path_upload_track_cover,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), validate_size_image],
        blank=True,
    )
    genres = models.ManyToManyField(
        Genre,
        verbose_name='Жанры',
        blank=True,
        related_name='tracks_genres'
    )
    listening = models.PositiveIntegerField(verbose_name='Прослушивания', default=0)
    downloads = models.PositiveIntegerField(verbose_name='Скачиваний', default=0)
    private = models.BooleanField(verbose_name='Приватный', default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    # favorite = models.ManyToManyField(AuthUser, verbose_name='Добавили в избранное', related_name='tracks_favorite', blank=True,)
    likes = models.ManyToManyField(AuthUser, verbose_name='Лайкнули треки', related_name='tracks_likes', blank=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('track', kwargs={'track_slug': self.slug})

    def __str__(self):
        return self.title


class PlayList(models.Model):
    """Плейлист"""
    user = models.ForeignKey(AuthUser, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', max_length=33)
    description = models.TextField(verbose_name='Описание', max_length=300)
    tracks = models.ManyToManyField(Track, verbose_name='Треки')

