from django.forms import ModelForm
from .models import *

#create the form class 

class AddForm(ModelForm):
  class Meta:
    model = Add
    fields = '__all__'