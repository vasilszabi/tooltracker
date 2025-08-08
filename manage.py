#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tooltracker.settings")
    from django.core.management import execute_from_command_line

    # 🔹 Auto-vytvorenie admin používateľa, ak neexistuje
    try:
        import django
        django.setup()
        from django.contrib.auth.models import User
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                "admin", "admin@example.com", "admin123"
            )
            print("✅ Admin account created: admin / admin123")
        else:
            print("ℹ️ Admin account already exists, skipping creation.")
    except Exception as e:
        print(f"⚠️ Could not create admin automatically: {e}")

    execute_from_command_line(sys.argv)
