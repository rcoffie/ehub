from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *

# Create your views here.

"""def index(request):
  return HttpResponse("this is the index page")
  """
def index(request):
  return render(request, 'add/index.html')



def register(request):
  form = UserCreationForm()
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')
  context = {'form':form,}
  return render(request,'registration/register.html',context)



def adds(request):
  adds = Add.objects.all()
  context = {'adds':adds}
  return render(request,'add/adds.html',context)



def postAdd(request):
  form = AddForm()
  if request.method == 'POST':
    form = AddForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')
  context = {'form':form}
  return render(request,'add/post.html',context)