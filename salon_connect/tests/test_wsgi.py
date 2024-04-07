from django.test import TestCase
from django.core.wsgi import get_wsgi_application
from django.conf import settings

class WSGIConfigTest(TestCase):
    def test_wsgi_application(self):
        """
        Test that the WSGI application is correctly configured.
        """
        # Get the WSGI application
        application = get_wsgi_application()
        print(application)
        
        # Check that the application is not None
        self.assertIsNotNone(application)
        
        # Check that the WSGI application is the same as the one defined in the WSGI config file
        self.assertEqual(application, settings.WSGI_APPLICATION)
