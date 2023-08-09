from typing import Type

from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from inventory.models.category import Category
from inventory.serializers.category_serializers import CategoryListSerializer


class CategoriesListCreateView(ListCreateAPIView):
    pagination_class = None  # disable pagination for this endpoint
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    ordering_fields = ["name"]

    authentication_classes = [JWTAuthentication]
