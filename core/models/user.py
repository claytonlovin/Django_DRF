from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]