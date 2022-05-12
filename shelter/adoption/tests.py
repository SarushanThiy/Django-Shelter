from urllib import response
from django.test import Client, TestCase
from django.urls import reverse

# Create your tests here.

from .models import Breed, Dog

class BaseTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_breed = Breed.objects.create(name='Dalmation')
        cls.dog = Dog.objects.create(name='Fido', breed=cls.test_breed)

class TestBasicViews(BaseTestCase):

    client = Client()

    def test_home(self):
        response = self.client.get(reverse('adoption-home'))
        assert 'home.html' in [t.name for t in response.templates]
    
    def test_dogs(self):
        response = self.client.get(reverse('adoption-dogs'))
        assert "doggos" in response.context
        assert response.context['doggos'].count() == 1
        assert "dogs.html" in [t.name for t in response.templates]
