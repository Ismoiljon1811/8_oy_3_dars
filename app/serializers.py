from rest_framework import serializers
from .models import Travel, Hotel, Klass

from rest_framework import serializers


class TravelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    lifetime = serializers.IntegerField()
    price = serializers.IntegerField()
    klass = serializers.CharField()
    hotel = serializers.CharField()

    def create(self, validated_data):
        return Travel().objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.lifetime = validated_data.get('lifetime', instance.lifetime)
        instance.price = validated_data.get('price', instance.price)
        instance.klass = validated_data.get('klass', instance.klass)
        instance.hotel = validated_data.get('hotel', instance.hotel)
        instance.save()
        return instance

class HotelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    number_of_stars = serializers.IntegerField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Hotel().objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.number_of_stars = validated_data.get('number_of_stars', instance.number_of_stars)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class klassSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Klass().objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance