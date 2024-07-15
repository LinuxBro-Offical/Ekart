from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Enduser
from django.urls import reverse

class LoginAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Enduser.objects.create_user(mobile='+919961091067', password='testpassword')

    def test_login_success(self):
        # Make a POST request to the login API endpoint with valid credentials
        response = self.client.post('/signin', {'mobile': '+919961091067', 'password': 'testpassword'})

        # Assert that the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Assert that the response contains the expected data or redirects to the correct page
        # ...

    def test_login_failure(self):
        # Make a POST request to the login API endpoint with invalid credentials
        response = self.client.post('/signin', {'mobile': '+919961091067', 'password': 'incorrectpassword'})

        # Assert that the response status code is 401 (unauthorized)
        self.assertEqual(response.status_code, 401)

        # Assert that the response contains the expected data or error message
        # ...

class Home_viewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        # self.category1 = Category.objects.create(name='Category 1')

    def test_home_view(self):
        url = reverse('usersite_home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        # self.assertQuerysetEqual(response.context['category'], [repr(self.category1), repr(self.category2)])