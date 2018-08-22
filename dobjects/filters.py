import django_filters
from django import forms

from dal import autocomplete

from dobjects.models import Period, DigitalContainer, ThreeD, Photo, Illustration
from vocabs.models import SkosConcept
from vocabs.filters import generous_concept_filter


class DigitalContainerListFilter(django_filters.FilterSet):
    id_inv_nr = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=DigitalContainer._meta.get_field('id_inv_nr').help_text,
        label=DigitalContainer._meta.get_field('id_inv_nr').verbose_name
        )
    fabric = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__icontains="fabric"
            ),
        help_text=DigitalContainer._meta.get_field('fabric').help_text,
        label=DigitalContainer._meta.get_field('fabric').verbose_name,
        method=generous_concept_filter,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'chbx-select-multi'})
        )
    painting_style = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__icontains="painting_style"
            ),
        help_text=DigitalContainer._meta.get_field('painting_style').help_text,
        label=DigitalContainer._meta.get_field('painting_style').verbose_name,
        method=generous_concept_filter,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'chbx-select-multi'})
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


class PhotoListFilter(django_filters.FilterSet):

    class Meta:
        model = Photo
        fields = "__all__"


class IllustrationListFilter(django_filters.FilterSet):

    class Meta:
        model = Illustration
        fields = "__all__"
