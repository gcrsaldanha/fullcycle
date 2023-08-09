from dataclasses import dataclass
from typing import Optional

from django.db import transaction
from django.db.models import QuerySet

from inventory.models import Product
from inventory.models.inventory import InventoryLedger


class InventoryServiceException(Exception):
    pass


class ProductDoesNotExist(InventoryServiceException):
    pass


class InsufficientProductQuantity(InventoryServiceException):
    pass


class InvalidRequest(InventoryServiceException):
    pass


class InventoryService:
    def __init__(self, product_repository: QuerySet[Product], inventory_ledger_repository: QuerySet[InventoryLedger]):
        self.product_repository = product_repository
        self.inventory_ledger_repository = inventory_ledger_repository

    def add_product_to_inventory(self, product_id: int, quantity: int) -> None:
        self._validate_quantity(quantity)
        with transaction.atomic():
            product = self._get_product(product_id)
            product.quantity += quantity
            product.save()
            self.inventory_ledger_repository.create(product=product, quantity=quantity)

    def remove_product_from_inventory(self, product_id: int, quantity: int) -> None:
        self._validate_quantity(quantity)
        with transaction.atomic():
            product = self._get_product(product_id)
            self._validate_sufficient_quantity(product, quantity)
            product.quantity -= quantity
            product.save()
            self.inventory_ledger_repository.create(product=product, quantity=-quantity)

    def _get_product(self, product_id: int) -> Product:
        try:
            return self.product_repository.get(id=product_id)
        except Product.DoesNotExist:
            raise ProductDoesNotExist(f"Product with id {product_id} does not exist.")

    def _validate_quantity(self, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

    def _validate_sufficient_quantity(self, product: Product, quantity: int):
        if product.quantity < quantity:
            raise InsufficientProductQuantity(
                f"Product with id {product.id} has insufficient quantity."
            )

    @classmethod
    def create(cls) -> "InventoryService":
        return cls(
            product_repository=Product.objects.all(),
            inventory_ledger_repository=InventoryLedger.objects.all(),
        )
