from django.contrib.auth.models import User
from django.test import TestCase
from django.test import SimpleTestCase
from django.test import Client
from django.urls import reverse, resolve

from authentication.models import Contact
from authentication.views import home, contactus, delete_contact, signup, delete_customer


# Create your tests here.
class TestUrls(SimpleTestCase):
    # Home page Testing, and It is Customer/User and Admin Signin Testing as well
    def test_case_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

        # Create Contact Us Testing

    def test_case_contactus_url(self):
        url = reverse('contactus')
        self.assertEquals(resolve(url).func, contactus)

        # Delete Contact Us Testing

    def test_case_delete_contact_url(self):
        url = reverse('delete_contact', args=[1])
        self.assertEquals(resolve(url).func, delete_contact)

        # Creating Signup or Customer registration Testing

    def test_case_signup_url(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

        # Delete Registered Customer Testing

    def test_case_delete_customer_url(self):
        url = reverse('delete_customer', args=[1])
        self.assertEquals(resolve(url).func, delete_customer)


class TestViews(TestCase):
    # Testing User Authentication in home view
    def test_case_home_views(self):
        user = User.objects.create(username='testcase')
        user.set_password('12345')
        user.save()
        client = Client()
        logged_in = client.login(username='testcase', password="12345")
        url = reverse('home')
        response = client.get(url)
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/index.html')

        # Testing Contact Create in Contact us view

    def test_case_CreateContact_views(self):
        client = Client()
        url = reverse('contactus')
        response = client.post(url, {
            'fullname': 'name',
            'email': 'email',
            'message': 'message',
        })

        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/contact.html')

        # Testing Contact Delete in Contact us view

    def test_case_DeleteContact_views(self):
            client = Client()

            newlycreated = Contact.objects.create(
                {
                    'fullname': 'name',
                    'email': 'email',
                    'message': 'message',
                })
            print(newlycreated.id)
            url = reverse('delete_contact', newlycreated.id)
            response = client.delete(url)

            print(response)
            self.assertEquals(response.status_code, 200)
            self.assertRedirects(response, '/show')
