from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.Serializer):
    name = serializers.CharField()
    note = serializers.CharField()
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Country.objects.create(validated_data)
