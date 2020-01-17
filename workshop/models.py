from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class Speciality(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('Speciality', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Submit(models.Model):
    sub = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sub')
    full_name = models.CharField(max_length=500)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    article =  models.FileField(upload_to='media/', null=True, blank=False)
    accepted = models.BooleanField(default=False)
    def __str__(self):
        return self.full_name
