from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('search_category/', views.searchCategory, name='search-category'),
    path('search-location/', views.searchLocation, name='location'),
]
