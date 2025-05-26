from django.shortcuts import render

# Create your views here.

def freeclass(request):
    return render(request,'base.html')

from django.shortcuts import render

def login(request):
    return render(request,'login.html')

