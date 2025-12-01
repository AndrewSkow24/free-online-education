from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    email = models.EmailField(unique=True, max_length=255, verbose_name="E-mail")
    phone = models.CharField(max_length=32, verbose_name="номер телефона", null=True, blank=True)
    city = models.CharField(max_length=128, verbose_name="город", null=True, blank=True)
    avatar = models.ImageField(upload_to="users/avatars", verbose_name="аватар", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'User: {self.email}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"