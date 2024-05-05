from django.db.models import Q, QuerySet
from django_filters import rest_framework as django_filters

from core import models


class AttractionsFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')
    order_by = django_filters.OrderingFilter(
        fields=(
            'id',
            'name',
            'description'
        )
    )

    class Meta:
        model = models.Attractions
        fields = [
            'id',
            'name',
            'description',
            'order_by',
        ]

    def filter_search(
        self,
        queryset: QuerySet,
        name: str,
        value: str
    ) -> QuerySet:
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value)
        )
