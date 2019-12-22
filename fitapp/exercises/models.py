from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.FileField()


class Exercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

class MovementStep(models.Model):
    order = models.IntegerField()
    description = models.CharField(max_length=500)
    image = models.FileField()