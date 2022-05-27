from django.shortcuts import render
from .models import Category, Picture, Location


# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    pics = Picture.objects.all()
    return render(request, 'gallery.html', {'categories': categories, 'pics': pics})


def searchCategory(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        search_results = Picture.objects.filter(category__name=searched.title())
        return render(request, 'searched.html', {'searched': searched, 'search_results': search_results})
    else:
        return render(request, 'searched.html')


def uploadPhoto(request):
    return render(request, 'upload.html')
