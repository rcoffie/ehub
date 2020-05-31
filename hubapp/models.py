from django.db import models


# Create your models here.
class Add(models.Model):
  Category=(
    ('Mobile Phone','Mobile Phone'),
    ('Audio','Audio'),
  )
  
  location=(
    ('kumasi','kumasi'),
    ('Accra','Accra'),
    ('Tamale','Tamale'),
  )
  Condition=(
    ('Used','used'),
    ('New'),('New')
  )
  title = models.CharField(max_length=150)
  price = models.DecimalField(max_digits=6,decimal_places=2)
  brand = models.CharField(max_length=50)
  description = models.TextField()
  negotiable  = models.BooleanField(default=False)
  image = models.ImageField(null=True)
  
  def __str__(self):
    return self.title

  
  
  
  
  
  
  