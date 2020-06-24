from rest_framework import serializers
from .models import UserApis


class UserApisSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.CharField()
    password = serializers.CharField()


    def create(self, validated_data):
        return UserApis.objects.create(**validated_data)
