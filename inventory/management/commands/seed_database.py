from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

import random

from django.db import transaction
from faker import Faker

from inventory.models import Category, Product


class Command(BaseCommand):
    help = "Seed the database"

    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS("Seeding database..."))
        if Category.objects.exists():
            self.stdout.write(self.style.SUCCESS("Database already seeded."))
        else:
            fake = Faker()

            CATEGORIES = ["Food", "Beverage", "Apparel", "Electronics", "Furniture"]
            num_products_per_category = 30

            with transaction.atomic():
                categories = []
                for category_name in CATEGORIES:
                    category = Category.objects.create(name=category_name)
                    categories.append(category)

                for category in categories:
                    for _ in range(num_products_per_category):
                        product_name = fake.word()  # Generate a random word as the product name
                        Product.objects.create(name=product_name, category=category, quantity=0)

            print("Seed script executed successfully!")
            self.stdout.write(self.style.SUCCESS("Finished seeding database."))
