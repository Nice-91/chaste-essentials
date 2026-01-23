from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    help = "Create admin user if not exists"

    def handle(self, *args, **kwargs):
        username = "chaste"
        password = "Chaste@123"
        email = "chaste@gmail.com"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write("✅ Superuser created")
        else:
            self.stdout.write("ℹ️ Superuser already exists")
