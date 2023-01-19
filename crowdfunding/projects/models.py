from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model() #get from setting.py

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField() #to check if the project is open
    date_created = models.DateTimeField(auto_now_add=True) #auto now add, add date time
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owner_projects" #related_name link backward
        )
    
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='pledges')
    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="supporter_pledges"
    )