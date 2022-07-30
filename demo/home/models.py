import email
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    desc = models.TextField()