import os
import sys
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tooltracker.settings')

if __name__ == '__main__':
    from django.contrib.auth.models import User
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin123")

    execute_from_command_line(sys.argv)

