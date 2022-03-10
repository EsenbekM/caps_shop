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


class BestsellerSerializer(serializers.ModelSerializer):
    cap = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Bestsaller
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

class EventsSerializer(serializers.Serializer):
    cap = serializers.SlugRelatedField(slug_field='name', read_only=True)
    event_price = serializers.IntegerField()
    class Meta:
        model = Event
        fields = '__all__'
