from rest_framework import serializers

from core import models


class AttractionsPreview(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    categories = serializers.StringRelatedField()

    class Meta:
        model = models.Attractions
        fields = ('id', 'name', 'image', 'latitude', 'longitude', 'categories')

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
        fields = ('id', 'name', 'description', 'image', 'latitude', 'longitude', 'categories')


class Category(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class Castom(serializers.Serializer):
    file = serializers.FileField()
