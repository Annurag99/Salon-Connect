"""
URL Configuration for salon_connect project.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("salon_admin.urls"))
]
