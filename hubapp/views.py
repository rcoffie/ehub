from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

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