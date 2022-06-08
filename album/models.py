from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def save_category(self):
        self.save()

    @classmethod
    def get_category_by_id(cls, id):
        category = cls.objects.get(id=id)
        return category

    @classmethod
    def update_category(cls, cat):
        category = cls.get_category_by_id(cat.id)
        category.name = cat.name
        category.save_category()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def save_location(self):
        self.save()

    @classmethod
    def get_location_by_id(cls, id):
        location = cls.objects.get(id=id)
        return location

    @classmethod
    def update_location(cls, loc):
        location = cls.get_location_by_id(loc.id)
        location.name = loc.name
        location.save_location()

    def delete_location(self):
        self.delete()

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

    @classmethod
    def get_picture_by_id(cls, id):
        picture = cls.objects.get(id=id)
        return picture

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
    def search_picture(cls, category):
        pictures = cls.objects.filter(category__name__icontains=category)
        return pictures

    @classmethod
    def filter_by_location(cls, location):
        pictures = cls.objects.filter(location__name__icontains=location)
        return pictures

    def __str__(self):
        return self.category
