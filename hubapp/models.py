from django.db import models
from django.conf import settings
from django.contrib.auth.models import User




# Create your models here.

class Add(models.Model):
  title = models.CharField(max_length=50,)
  price = models.DecimalField(max_digits=6, decimal_places=2,default=True)
  used = models.BooleanField(default=False,)
  default_image = models.ImageField(null=True,)
  aproval = models.BooleanField(default=False,null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE,default=User.id)
  add_date = models.DateTimeField(auto_now_add=True,null=True)