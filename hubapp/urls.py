
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name="register"),
    path('adds',views.adds,name='adds')
]
