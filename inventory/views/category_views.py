from typing import Type

from rest_framework.generics import ListCreateAPIView

from inventory.models.category import Category
from inventory.serializers.category_serializers import CategoryListSerializer


class CategoriesListCreateView(ListCreateAPIView):
    pagination_class = None  # disable pagination for this endpoint
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    ordering_fields = ["name"]
