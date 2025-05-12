# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('externo', 'Externo'),
    )
    rol = models.CharField(max_length=10, choices=ROLES, default='externo')

    def __str__(self):
        return f"{self.username} ({self.rol})"
