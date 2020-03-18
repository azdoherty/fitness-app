from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.FileField()


class Exercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True)
    instruction = models.CharField(max_length=255, default='')
    instructions = ArrayField(instruction, default=list)
    
    def __str__(self):
        return self.title


class MovementStep(models.Model):
    Exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.IntegerField()
    description = models.CharField(max_length=500)
    image = models.FileField()


class Workout(models.Model):
    name = models.CharField
    exercises = models.ManyToManyField(Exercise)