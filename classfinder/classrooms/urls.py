from django.urls import path
from .import views


urlpatterns = [
    
    path('searchclass/',views.searchclass,name='searchclass'),
    path('login/',views.login,name='login'),
   
]