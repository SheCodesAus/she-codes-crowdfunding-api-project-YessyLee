from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.CharField(blank=True, null=True, max_length=150)
    avatar = models.URLField(blank=True, null=True)
    
    def __str__(self): 
        return self.username

    