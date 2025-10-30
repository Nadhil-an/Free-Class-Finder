from django.urls import path
from . import views

urlpatterns = [
    path('searchclass/', views.searchclass, name='searchclass'),
    path('all/', views.all_classes, name='all_classes'),
    path('available/', views.available_classes, name='available_classes'),
    path('occupied/', views.occupied_classes, name='occupied_classes'),
]
