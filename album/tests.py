from django.test import TestCase
from .models import Picture, Location, Category


# Create your tests here.

class CategoryTestCase(TestCase):
    """Test case for Category model"""

    def setUp(self):
        """Set up for the models instances"""
        self.category = Category(name='Nature')

    def tearDown(self):
        """Method to clear the model objects in the db after each testcase"""
        Category.objects.all().delete()

    def test_instance(self):
        """Test case to check if created category is an instance of Category model class"""
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        """Test case to check if created category is being saved in our database"""
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_update_category(self):
        """Test case to check if a saved category is being updated successfully"""
        self.category.save_category()
        self.category.name = 'Food'
        Category.update_category(self.category)
        updated_category = Category.objects.get(id=self.category.id)
        self.assertEqual(updated_category.name, 'Food')

    def test_delete_category(self):
        """Test case to check if a saved category is being removed from our db when deleted."""
        self.category.save_category()
        test_category = Category(name='Travel')
        test_category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories), 1)


class LocationTestCase(TestCase):
    """Test case for Location model"""

    def setUp(self):
        """Set up for the models instances"""
        self.location = Location(name='Doha')

    def tearDown(self):
        """Method to clear the model objects in the db after each testcase"""
        Location.objects.all().delete()

    def test_instance(self):
        """Test case to check if created location is an instance of Location model class"""
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        """Test case to check if created location is being saved in our database"""
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_update_location(self):
        """Test case to check if a saved location is being updated successfully"""
        self.location.save_location()
        self.location.name = 'Wuhan'
        Location.update_location(self.location)
        updated_location = Location.objects.get(id=self.location.id)
        self.assertEqual(updated_location.name, 'Wuhan')

    def test_delete_location(self):
        """Test case to check if a saved location is being removed from our db when deleted."""
        self.location.save_location()
        test_location = Location(name='Cairo')
        test_location.save_location()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations), 1)


class PictureTestCase(TestCase):
    """Test case for Picture model"""

    def setUp(self):
        """Set up for the models instances"""
        self.category = Category(name='Nature')
        self.category.save()
        self.location = Location(name='Munich')
        self.location.save()
        self.picture = Picture(image='test.png', description='Image description', pub_date='2022-02-02 12:22:10',
                               category=self.category, location=self.location)

    def tearDown(self):
        """Method to clear the model objects in the db after each testcase"""
        Category.objects.all().delete()
        Location.objects.all().delete()
        Picture.objects.all().delete()

    def test_instance(self):
        """Test case to check if created picture is instance of Picture model class"""
        self.assertTrue(isinstance(self.picture, Picture))

    def test_save_picture(self):
        """Test case to check if created picture is being saved in our database"""
        self.picture.save_picture()
        pictures = Picture.objects.all()
        self.assertTrue(len(pictures) > 0)

    def test_update_picture(self):
        """Test case to check if a saved picture is being updated successfully"""
        self.picture.save_picture()
        self.picture.description = 'New description'
        Picture.update_picture(self.picture)
        updated_picture = Picture.objects.get(id=self.picture.id)
        self.assertEqual(updated_picture.description, 'New description')

    def test_delete_picture(self):
        """Test case to check if a saved picture is being removed from our db when deleted."""
        self.picture.save_picture()
        self.picture.delete_picture()
        pictures = Picture.objects.all()
        self.assertTrue(len(pictures) == 0)

    def test_get_picture_by_id(self):
        """Test case to check we can access the id of a saved image in the database."""
        self.picture.save_picture()
        picture = Picture.get_picture_by_id(self.picture.id)
        self.assertTrue(picture)

    def test_search_by_category(self):
        """Test case to check if we can search an image by category."""
        self.picture.save_picture()
        pictures = Picture.search_picture('Nature')
        self.assertEqual(len(pictures), 1)

    def test_filter_by_location(self):
        """Test case to check if we can filter an image by their location."""
        self.picture.save_picture()
        pictures = Picture.filter_by_location('Munich')
        self.assertEqual(len(pictures), 1)
