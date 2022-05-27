from django.shortcuts import render
from .models import Category, Picture, Location


# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    pics = Picture.objects.all()
    return render(request, 'gallery.html', {'categories': categories, 'pics': pics})


def uploadPhoto(request):
    return render(request, 'upload.html')
