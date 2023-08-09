from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from inventory.serializers.inventory_serializers import InventoryOperationSerializer
from inventory.services.inventory_service import InventoryService, InventoryServiceException


# TODO: apply DRY to this code and service.

@api_view(['POST'])
def add_to_inventory(request: Request) -> Response:
    operation_serializer = InventoryOperationSerializer(data=request.data)
    operation_serializer.is_valid(raise_exception=True)

    service = InventoryService.create()
    try:
        service.add_product_to_inventory(
            product_id=operation_serializer.validated_data['product_id'],
            quantity=operation_serializer.validated_data['quantity'],
        )
    except InventoryServiceException as e:
        raise ValidationError(e)
    else:
        return Response(status=200)


@api_view(['POST'])
def remove_from_inventory(request: Request) -> Response:
    operation_serializer = InventoryOperationSerializer(data=request.data)
    operation_serializer.is_valid(raise_exception=True)

    service = InventoryService.create()
    try:
        service.remove_product_from_inventory(
            product_id=operation_serializer.validated_data['product_id'],
            quantity=operation_serializer.validated_data['quantity'],
        )
    except InventoryServiceException as e:
        raise ValidationError(e)
    else:
        return Response(status=200)
