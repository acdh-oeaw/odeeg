import django_filters
from dal import autocomplete

from dobjects.models import Period


class PeriodListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Period._meta.get_field('name').help_text,
        label=Period._meta.get_field('name').verbose_name
        )

    class Meta:
        model = Period
        fields = "__all__"
