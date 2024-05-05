from rest_framework.viewsets import ReadOnlyModelViewSet

from core import models, filters, serializers


class Attractions(ReadOnlyModelViewSet):
    """Достопримечательности"""
    queryset = models.Attractions.objects.all()
    filterset_class = filters.AttractionsFilter

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return serializers.AttractionsPreview
        if self.action == 'retrieve':
            return serializers.AttractionRead
