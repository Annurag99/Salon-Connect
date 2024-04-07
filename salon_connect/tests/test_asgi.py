import os
from django.test import SimpleTestCase
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'salon_connect.settings')

class ASGITestCase(SimpleTestCase):
    def test_application_exists(self):
        """
        Test that the ASGI callable exists.
        """
        application = get_asgi_application()
        self.assertIsNotNone(application)

    def test_application_callable(self):
        """
        Test that the ASGI callable is indeed callable.
        """
        application = get_asgi_application()
        self.assertTrue(callable(application))
