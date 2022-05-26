from django.shortcuts import render


# Create your views here.
def gallery(request):
    return render(request, 'gallery.html')


def viewPhoto(request, pk):
    return render(request, 'photo.html')


def uploadPhoto(request):
    return render(request, 'upload.html')
