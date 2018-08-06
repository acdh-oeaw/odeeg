import django_filters
from dal import autocomplete

from dobjects.models import Period, DigitalContainer, ThreeD


class DigitalContainerListFilter(django_filters.FilterSet):
    id_inv_nr = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=DigitalContainer._meta.get_field('id_inv_nr').help_text,
        label=DigitalContainer._meta.get_field('id_inv_nr').verbose_name
        )

    class Meta:
        model = DigitalContainer
        fields = "__all__"


class PeriodListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Period._meta.get_field('name').help_text,
        label=Period._meta.get_field('name').verbose_name
        )

    class Meta:
        model = Period
        fields = "__all__"


class ThreeDListFilter(django_filters.FilterSet):

    class Meta:
        model = ThreeD
        fields = "__all__"
