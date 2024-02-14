from rest_framework import serializers


class CommonDetailSerializer(serializers.Serializer):
    """
    Serializer for drf-spectacular documentation.
    Indicates what data, issues a request in different statuses.
    """
    detail = serializers.CharField()


class CommonDetailAndStatusSerializer(serializers.Serializer):
    """
    Serializer for drf-spectacular documentation.
    Indicates what data, issues a request in different statuses.
    """
    status = serializers.IntegerField()
    details = serializers.CharField()
