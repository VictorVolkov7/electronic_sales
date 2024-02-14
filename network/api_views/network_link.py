from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from network.filters import LinkCountryFilter
from network.models import NetworkLink
from network.paginator import NetworkPagination
from network.permissions import DebtUpdatePermission
from network.serializers.network_link import NetworkLinkSerializer, NetworkLinkCreateSerializer
from network.serializers.spectacular_serializers import CommonDetailSerializer, CommonDetailAndStatusSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Получить список звеньев сети.",
        responses={
            status.HTTP_200_OK: NetworkLinkSerializer,
            status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
            status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
            status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: CommonDetailSerializer,
        }
    ),
    retrieve=extend_schema(
        summary="Получить существующее звено сети по его идентификатору.",
        responses={
            status.HTTP_200_OK: NetworkLinkSerializer,
            status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
            status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
            status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
            status.HTTP_405_METHOD_NOT_ALLOWED: CommonDetailSerializer,
        }
    ),
    update=extend_schema(
        summary="Изменение существующего звена сети.",
        responses={
            status.HTTP_200_OK: NetworkLinkSerializer,
            status.HTTP_400_BAD_REQUEST: CommonDetailSerializer,
            status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
            status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
            status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
        }
    ),
    partial_update=extend_schema(
        summary="Частичное изменение существующего звена сети.",
        responses={
            status.HTTP_200_OK: NetworkLinkSerializer,
            status.HTTP_400_BAD_REQUEST: CommonDetailSerializer,
            status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
            status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
            status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
        }
    ),
    create=extend_schema(
        summary="Создание нового звена сети.",
        responses={
            status.HTTP_201_CREATED: NetworkLinkSerializer,
            status.HTTP_400_BAD_REQUEST: CommonDetailSerializer,
            status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
            status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
            status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
        }
    ),
    destroy=extend_schema(
        summary="Удаление существующего звена сети.",
        responses={
            status.HTTP_204_NO_CONTENT: '',
            status.HTTP_401_UNAUTHORIZED: NetworkLinkSerializer,
            status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
            status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
        }
    ),
)
class NetworkLinkViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Network Link model.
    """
    queryset = NetworkLink.objects.all()
    permission_classes = (IsAuthenticated, DebtUpdatePermission,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LinkCountryFilter
    pagination_class = NetworkPagination

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return NetworkLinkCreateSerializer
        else:
            return NetworkLinkSerializer
