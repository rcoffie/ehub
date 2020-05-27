from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

"""def index(request):
  return HttpResponse("this is the index page")
  """
def index(request):
  return render(request, 'add/index.html')



def register(request):
  context = {}
  return render(request,'/registration/register.html',context)