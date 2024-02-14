from rest_framework import serializers

from network.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer class for Product model.
    """
    class Meta:
        model = Product
        fields = (
            'pk',
            'name',
            'model',
            'release_date',
        )
