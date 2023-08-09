from rest_framework import serializers

from inventory.models import Category
from inventory.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(source="category.id", read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "quantity", "category_id", "category_name"]


class CreateProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    category_id = serializers.IntegerField()
