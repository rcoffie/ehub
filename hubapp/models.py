from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime 



# Create your models here.

class Add(models.Model):
  category=(
  ('Mobile Phone','Mobile Phone'),
  ('Audio/MP3','Audio/MP3')
  )
  
  location=(
    ('kumasi','kumasi'),
    ('Accra','Accra'),
    ('Tamale','Tamale')
    
    )
  title = models.CharField(max_length=150)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  location = models.CharField(max_length=200,choices=location)
  
  