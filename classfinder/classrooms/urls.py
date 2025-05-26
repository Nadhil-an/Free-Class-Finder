from django.urls import path
from .import views


urlpatterns = [
    
    path('freeclass/',views.freeclass,name='freeclass'),
    path('login/',views.login,name='login'),
   
]