from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from network.models import Product
from network.paginator import ProductPagination
from network.serializers.product import ProductSerializer
from network.serializers.spectacular_serializers import CommonDetailAndStatusSerializer, CommonDetailSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Получить список продуктов.",
        responses={
            status.HTTP_200_OK: ProductSerializer,
            status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
            status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
            status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: CommonDetailSerializer,
        }
    ),
    retrieve=extend_schema(
        summary="Получить существующий продукт по его идентификатору.",
        responses={
            status.HTTP_200_OK: ProductSerializer,
            status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
            status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
            status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: CommonDetailSerializer,
        }
    ),
    update=extend_schema(
        summary="Изменение существующего продукта.",
        responses={
            status.HTTP_200_OK: ProductSerializer,
            status.HTTP_400_BAD_REQUEST: CommonDetailSerializer,
            status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
            status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
            status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
        }
    ),
    partial_update=extend_schema(
        summary="Частичное изменение существующего продукта.",
        responses={
            status.HTTP_200_OK: ProductSerializer,
            status.HTTP_400_BAD_REQUEST: CommonDetailSerializer,
            status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
            status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
            status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
        }
    ),
    create=extend_schema(
        summary="Создание нового продукта.",
        responses={
            status.HTTP_201_CREATED: ProductSerializer,
            status.HTTP_400_BAD_REQUEST: CommonDetailSerializer,
            status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
            status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
            status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
        }
    ),
    destroy=extend_schema(
        summary="Удаление существующего продукта.",
        responses={
            status.HTTP_204_NO_CONTENT: '',
            status.HTTP_401_UNAUTHORIZED: ProductSerializer,
            status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
            status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
        }
    ),
)
class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Product Model.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = ProductPagination
