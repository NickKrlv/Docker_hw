from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.IntegerField(**NULLABLE, verbose_name='phone')
    city = models.CharField(max_length=50, **NULLABLE, verbose_name='city')
    avatar = models.ImageField(verbose_name='avatar', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return {self.email}

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
