from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=64)
    breed = models.CharField(max_length=128)
    age = models.IntegerField()
    favorite_human = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

def __str__(self):
    return f'{self.name}:{self.breed}:{self.age}'