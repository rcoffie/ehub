from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime 
from django.utils import timezone


# Create your models here.
class Add(models.Model):
  Category=(
    ('Mobile Phone','Mobile Phone'),
    ('Audio/MP3','Audio/MP3'),
  )
  
  location=(
    ('kumasi','kumasi'),
    ('Accra','Accra'),
    ('Tamale','Tamale'),
  )
  Condition=(
    ('Used','used'),
    ('New','New'),
  )
  title = models.CharField(max_length=150)
  price = models.DecimalField(max_digits=6,decimal_places=2)
  brand = models.CharField(max_length=50)
  location = models.CharField(max_length=200, null=True,choices=location)
  category = models.CharField(max_length=200, null=True,choices=Category)
  condition = models.CharField(max_length=200, null=True,choices=Condition)
  description = models.TextField()
  negotiable  = models.BooleanField(default=False)
  default_image = models.ImageField(null=True)
  image_1 = models.ImageField(null=True)
  image_2 = models.ImageField(null=True)
  image_3 = models.ImageField(null=True,blank=True)
  image_4 = models.ImageField(null=True,blank=True)
  aproval = models.BooleanField(default=False)
  time   = timezone.now().day
  user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,default=User.id)
  
  
  def __str__(self):
    return self.title

  
  
  
  
  
  
  