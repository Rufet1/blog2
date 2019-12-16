from django.db import models
from django.contrib.auth.models import User


class UserProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()