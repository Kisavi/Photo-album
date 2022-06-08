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

    def save_image(self):
        self.save()
        return self

    def delete_image(self):
        self.delete()
