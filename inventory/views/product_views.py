from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from common.pagination import CustomPagination, PaginationSerializer
from inventory.models.product import Product, CategoryDoesNotExist
from inventory.serializers.product_serializers import ProductSerializer, CreateProductSerializer


class ProductsListCreateView(ListCreateAPIView):
    pagination_class = CustomPagination
    pagination_serializer_class = PaginationSerializer
    queryset = Product.objects.prefetch_related("category").all().order_by("name")
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            product = Product.create_product(**serializer.validated_data)
        except CategoryDoesNotExist as e:
            raise ValidationError({"category_id": [e]})
        return Response(ProductSerializer(product).data, status=201)


class ProductRetrieveView(RetrieveAPIView):
    queryset = Product.objects.prefetch_related("category").all()
    serializer_class = ProductSerializer
