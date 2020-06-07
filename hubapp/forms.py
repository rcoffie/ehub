from django.forms import ModelForm
from .models import *

#create the form class 

class AddForm(ModelForm):
     class Meta:
         model = Ad
         exclude = ['user','aproval']
         #fields = '__all__'
       
       