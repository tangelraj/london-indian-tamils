import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


class Command(BaseCommand):

    help = "Create or update the production admin account"

    def handle(self, *args, **options):

        User = get_user_model()

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            raise CommandError(
                "Admin username or password is missing."
            )

        user, created = User.objects.get_or_create(
            username=username
        )

        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    "Admin account created successfully."
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    "Admin account updated successfully."
                )
            )