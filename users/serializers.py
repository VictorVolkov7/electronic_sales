from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user model.
    """

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        """
        Create a new User.
        """
        password = validated_data.pop('password', None)
        instance = User.objects.create(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance


class TokenDetailAndStatusSerializer(serializers.Serializer):
    """
    Serializer for drf-spectacular documentation for token.
    Shows what data, issues a request when the status is 200.
    """
    refresh = serializers.CharField()
    access = serializers.CharField()


class TokenDetailSerializer(serializers.Serializer):
    """
    Serializer for drf-spectacular documentation for token.
    Shows what data, issues a request when the status is 200.
    """
    access = serializers.CharField()
