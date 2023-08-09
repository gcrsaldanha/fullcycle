from django.db import models

from inventory.models.category import Category


class CategoryDoesNotExist(Exception):
    pass


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)

    @classmethod
    def create_product(cls, name: str, category_id: int) -> "Product":
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:  # Avoid leaking Category model details to caller of product
            raise CategoryDoesNotExist(f"Category with id {category_id} does not exist.")

        return cls.objects.create(name=name, category=category)
