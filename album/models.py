from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Picture(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, null=True, blank=False, on_delete=models.SET_NULL)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)

    def save_picture(self):
        self.save()
        return self

    @classmethod
    def update_picture(cls, pic):
        picture = cls.get_picture_by_id(pic.id)
        picture.category = pic.category
        picture.location = pic.location
        picture.image = pic.image
        picture.description = pic.description
        picture.save_picture()

    def delete_picture(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location__name__icontains=location)
        return images
