from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Status(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        CLIENT = 'client', 'Client'
        VIP_CLIENT = 'vip_client', 'Vip client'

    status = models.CharField(max_length=50, choices=Status.choices, default=Status.CLIENT)
    email = models.EmailField(unique=True)
