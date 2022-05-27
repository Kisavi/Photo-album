from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('search_category/', views.searchCategory, name='search-category'),
    path('add/', views.uploadPhoto, name='upload'),
]
