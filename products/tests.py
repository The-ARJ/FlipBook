from django.contrib.auth.models import User
from django.test import TestCase
from django.test import SimpleTestCase
from django.test import Client
from django.urls import reverse, resolve

from authentication.models import Contact

# Create your tests here.
from authentication.views import show
from products.views import product_create, deleteproduct


class TestUrls(SimpleTestCase):

    # Create Product Testing
    def test_case_product_create_url(self):
        url = reverse('product_create')
        self.assertEquals(resolve(url).func, product_create)

        # fetching testing

    def test_case_product_retrive_url(self):
        url = reverse('show')
        self.assertEquals(resolve(url).func, show)

        # Delete product Us Testing

    def test_case_deleteproduct_url(self):
        url = reverse('deleteproduct', args=[1])
        self.assertEquals(resolve(url).func, deleteproduct)


class TestViews(TestCase):
    def test_case_CreateProduct_views(self):
        client = Client()

        url = reverse('product_create')
        response = client.post(url,
                               {'image': 'image', 'bookname': 'book', 'authorname': 'author', 'bookdesc': 'desc',
                                'price': 'price'
                                })
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Dashboard/show.html')
        # Testing Contact Delete in Contact us view

    def test_case_DeleteProduct_views(self):
        client = Client()

        newlycreated = Contact.objects.create(
            {
                'image': 'image',
                'bookname': 'book',
                'authorname': 'author',
                'bookdesc': 'desc',
                'price': 'price',
            })
        print(newlycreated.id)
        url = reverse('deleteproduct', newlycreated.id)
        response = client.delete(url)

        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertRedirects(response, '/show')
