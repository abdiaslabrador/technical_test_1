from django.db import models

# Create your models here.
class JokeModel(models.Model):
    joke = models.TextField(null=True) 