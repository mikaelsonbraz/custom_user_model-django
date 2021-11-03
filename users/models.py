from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    idade = models.PositiveIntegerField(default=0, help_text="Digite sua idade")
