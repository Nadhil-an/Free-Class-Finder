from django.urls import path
from .import views


urlpatterns = [
    
    path('freeclass/',views.freeclass,name='freeclass'),
   
]