from django.db import models

from inventory.models import Product


class InventoryLedger(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
