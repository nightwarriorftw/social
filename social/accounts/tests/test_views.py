from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.views import auth_login, auth_register, auth_logout, \
    home, show_profile, feed

class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.home = reverse('home')
        self.login = reverse('login')
        self.register = reverse('register')
        self.logout = reverse('logout')
        self.show_profile = reverse('accounts:profile', args=['xyz'])
        self.feed = reverse('accounts:feed')

    def test_home(self):
        response = self.client.get(self.home)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'social/home.html')
