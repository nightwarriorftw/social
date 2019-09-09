from django.test import SimpleTestCase
from django.urls import resolve, reverse
from accounts.views import feed, show_profile

class TestUrls(SimpleTestCase):

    def test_feed_url_resolves(self):
        url = reverse('accounts:feed')
        self.assertEqual(resolve(url).func, feed)
        
    def test_profile_url_resolved(self):
        url = reverse('accounts:profile', kwargs = {"username": "username"})
        self.assertEqual(resolve(url).func, show_profile)
