from django.shortcuts import render


# Create your views here.
def gallery(request):
    return render(request, 'photos/templates/gallery.html')


def viewPhoto(request, pk):
    return render(request, 'photos/templates/photo.html')


def uploadPhoto(request):
    return render(request, 'photos/templates/upload.html')
