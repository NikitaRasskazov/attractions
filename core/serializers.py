from rest_framework import serializers

from core import models


class AttractionsPreview(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = models.Attractions
        fields = ('name', 'image', 'latitude', 'longitude')

    def get_image(self, obj: models.Attractions):
        first_image = obj.attraction_images.first()
        if first_image:
            return first_image.image.url
        else:
            return None


class AttractionImages(serializers.ModelSerializer):
    class Meta:
        model = models.AttractionImage
        fields = ('id', 'image')


class AttractionRead(serializers.ModelSerializer):
    image = AttractionImages(many=True, source='attraction_images')

    class Meta:
        model = models.Attractions
        fields = ('name', 'description', 'image', 'latitude', 'longitude')
