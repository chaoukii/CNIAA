from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.name
