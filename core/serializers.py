from rest_framework import serializers

from core import models


class AttractionsPreview(serializers.ModelSerializer):
    class Meta:
        model = models.Attractions
        fields = ('name', 'image')


class AttractionRead(serializers.ModelSerializer):
    class Meta:
        model = models.Attractions
        fields = '__all__'
