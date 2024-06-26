#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import execute_from_command_line

def main():
    """Main function to execute Django administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'salon_connect.settings')
    try:
        execute_from_command_line(sys.argv)
    except ImportError:
        print(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?",
            file=sys.stderr
        )
        sys.exit(1)


if __name__ == '__main__':
    main()
