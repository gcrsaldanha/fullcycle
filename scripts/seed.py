import random

from django.db import transaction
from faker import Faker

from inventory.models import Category, Product

fake = Faker()

CATEGORIES = ["Food", "Beverage", "Apparel", "Electronics", "Furniture"]


def seed_database(num_products_per_category=30):
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


if __name__ == "__main__":
    seed_database()
