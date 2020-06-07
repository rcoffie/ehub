from django.db import models
from django.conf import settings
from django.contrib.auth.models import User




# Create your models here.

class Ad(models.Model):
  title = models.CharField(max_length=50)

