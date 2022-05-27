from django.shortcuts import render
from .models import Category, Picture


# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    pics = Picture.objects.all()
    return render(request, 'gallery.html', {'categories': categories, 'pics': pics})


def viewPhoto(request, picture_id):
    image = Picture.objects.get(id=picture_id)
    return render(request, '', {'image': image})


def uploadPhoto(request):
    return render(request, 'upload.html')
