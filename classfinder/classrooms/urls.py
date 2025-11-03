from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('search/', views.searchclass, name='searchclass'),
    path('available/', views.available_classes, name='available_classes'),
    path('occupied/', views.occupied_classes, name='occupied_classes'),
    path('all/', views.all_classes, name='all_classes'),
]
