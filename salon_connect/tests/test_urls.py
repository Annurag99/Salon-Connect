# test_urls.py

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib import admin
from django.urls import include
from salon_connect.urls import urlpatterns

class TestUrls(SimpleTestCase):
    def test_admin_url_resolves(self):
        """
        Test that the admin URL resolves to the correct view.
        """
        url = reverse('admin:index')
        self.assertEquals(resolve(url).func, admin.site.urls.func)

    def test_salon_admin_url_resolves(self):
        """
        Test that the salon_admin URL resolves to the correct view.
        """
        url = reverse('salon_admin')
        self.assertEquals(resolve(url).func, include("salon_admin.urls").func)
