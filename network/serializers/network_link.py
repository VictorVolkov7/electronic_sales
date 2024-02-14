from rest_framework import serializers
from network.models import NetworkLink
from network.serializers.product import ProductSerializer


class NetworkLinkSerializer(serializers.ModelSerializer):
    """
    Serializer class for NetworkLink model.
    """
    products = ProductSerializer(many=True, required=False)

    class Meta:
        model = NetworkLink
        fields = (
            'pk',
            'network',
            'name',
            'email',
            'country',
            'city',
            'street',
            'house_number',
            'products',
            'purveyor',
            'debt',
            'created_at',
            'hierarchy',
        )
        read_only_fields = ('created_at', 'hierarchy')


class NetworkLinkCreateSerializer(serializers.ModelSerializer):
    """
    Serializer class for Create/Update/Patch NetworkLink model.
    """
    def create(self, validated_data):
        products_data = validated_data.pop('products', [])
        network_link = NetworkLink.objects.create(**validated_data)
        network_link.products.set(products_data)
        network_link.clean()
        network_link.save()
        return network_link

    def update(self, instance, validated_data):
        products_data = validated_data.pop('products', [])
        super().update(instance, validated_data)
        instance.products.set(products_data)
        instance.clean()
        instance.save()
        return instance

    class Meta:
        model = NetworkLink
        fields = (
            'pk',
            'network',
            'name',
            'email',
            'country',
            'city',
            'street',
            'house_number',
            'products',
            'purveyor',
            'debt',
            'created_at',
            'hierarchy',
        )
        read_only_fields = ('created_at', 'hierarchy')
