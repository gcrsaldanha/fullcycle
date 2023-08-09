from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


User = get_user_model()


class Command(BaseCommand):
    help = "Create a superuser if it does not exist"

    def handle(self, *args, **options):
        if not User.objects.filter(email="admin@user.com").exists():
            User.objects.create_superuser(username="admin", email="admin@user.com", password="123456")
            self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser already exists"))
