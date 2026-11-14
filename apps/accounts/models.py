from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class CustomUser(AbstractUser):
    """
    Модель пользователя.
    """
    def get_default_role():
        return Group.objects.get_or_create(name="Commoner")[0]

    username = models.CharField(
        max_length=24, unique=True, verbose_name="Имя пользователя"
    )
    email = models.EmailField(unique=True, verbose_name="Email")
    language = models.CharField(max_length=10, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE, verbose_name="Язык пользователя")
    preferred_language = models.CharField(max_length=10, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE, verbose_name="Предпочитаемый ползвателем язык")
    registrered_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время регистрации")

    display_name = models.CharField(
        max_length=24, unique=True, verbose_name="Видимое имя пользователя"
    )

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):

        self.preferred_language = self.language
        self.display_name = self.username

        super().save(*args, **kwargs)

        # Добавляем в группу Commoner если пользователь новый
        if not self.groups.filter(name="Commoner").exists():
            self.groups.add(self.get_default_role())
