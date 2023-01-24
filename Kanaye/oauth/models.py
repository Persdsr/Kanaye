from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

from basic_services.service import get_path_upload_user


class AuthUser(AbstractUser):
    """Дабовок к абстрактному юзера"""
    bio = models.TextField(verbose_name='Обо мне', max_length=1000, blank=True)
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to=get_path_upload_user,
        validators=[FileExtensionValidator(['jpg', 'png'])],
        blank=True
    )
    country = models.CharField(verbose_name='Страна', max_length=20, blank=True)
    city = models.CharField(verbose_name='Город', max_length=20, blank=True)

    vk = models.URLField(verbose_name='Вконтакте', blank=True)
    youtube = models.URLField(verbose_name='Ютуб', blank=True)
    twitter = models.URLField(verbose_name='Твитер', blank=True)


class Follower(models.Model):
    """Подписки"""
    author = models.ForeignKey(AuthUser, verbose_name='Автор', on_delete=models.CASCADE, related_name='follower_author')
    sub = models.ForeignKey(AuthUser, verbose_name='Подписчик', on_delete=models.CASCADE, related_name='follower_sub')

    def __str__(self):
        return f'{self.sub} подписан на {self.author}'
