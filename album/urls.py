from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery),
    path('photo/<str:pk>/', views.viewPhoto),
    path('add/', views.uploadPhoto),
]
