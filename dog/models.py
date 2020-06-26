from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=64)
    breed = models.CharField(max_length=128)

def __str__(self):
    return f'{self.name}:{self.breed}'