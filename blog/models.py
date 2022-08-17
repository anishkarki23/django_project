from ast import Name
import email
from unicodedata import name
from urllib import request
from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField( max_length= 100)
    address = models.CharField( max_length= 100)
    phone = models.CharField( max_length= 100)


