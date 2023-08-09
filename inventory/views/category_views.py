from typing import Type

from rest_framework.generics import ListCreateAPIView
from rest_framework.serializers import Serializer

from inventory.models.models import Category
from inventory.serializers.category_serializers import CategoryListSerializer, CategoryCreateSerializer


class CategoriesListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()

    def get_serializer_class(self) -> Type[Serializer]:
        """
        We use different serializers for the creation and listing of categories, as per requirements.
        """
        if self.request.method == "GET":
            return CategoryListSerializer
        return CategoryCreateSerializer
