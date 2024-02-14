from rest_framework.routers import DefaultRouter

from network.api_views.network_link import NetworkLinkViewSet
from network.api_views.product import ProductViewSet
from network.apps import NetworkConfig

app_name = NetworkConfig.name

router = DefaultRouter()
router.register(r'network', NetworkLinkViewSet, basename='network-link')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    # add your additional urls
] + router.urls
