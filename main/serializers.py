from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *


class CapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cap
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CapCreateValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=200)
    description = serializers.CharField()
    price = serializers.IntegerField()
    brand = serializers.IntegerField()
    size = serializers.ListField()

    def validate_brand(self, brand):
        try:
            Cap.objects.get(id=brand)
        except Cap.DoesNotExist:
            raise ValidationError("This brand doesn't exist!")

    def validate_title(self, name):
        if Cap.objects.filter(name=name):
            raise ValidationError("This cap already exist!")

class FavoriteSerializer(serializers.Serializer):
    
    class Meta:
        model = Favorites
        fields = '__all__'