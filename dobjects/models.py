from django.db import models

from arche.models import Collection
from vocabs.models import SkosConcept


class DigitalContainer(models.Model):
    """extends arche.models.Collection to store domain specific information taken from
    metadata_ODEEG-archaeology.xslx"""

    belongs_to = models.OneToOneField(
        Collection, on_delete=models.CASCADE, primary_key=True,
        verbose_name='describes collection', related_name="described_by"
    )

    period_start_year = models.IntegerField(
        blank=True, null=True, verbose_name="Period [start] (date range) [AAT ID: 300081446]"
    )
    period_end_year = models.IntegerField(
        blank=True, null=True, verbose_name="Period [end] (date range) [AAT ID: 300081446]"
    )
    fabric = models.ManyToManyField(
        SkosConcept, blank=True, verbose_name="Fabric (as in BAPD)",
        related_name="is_fabric"
    )
    painting_style = models.ManyToManyField(
        SkosConcept, blank=True, verbose_name="Painting style/technique [AAT ID]",
        related_name="is_painting_style"
    )
    painting_sub_technique = models.ManyToManyField(
        SkosConcept, blank=True, verbose_name="Painting sub technique [AAT ID]",
        related_name="is_painting_sub_technique"
    )
    formating_technique = models.ManyToManyField(
        SkosConcept, blank=True, verbose_name="Forming technique [AAT ID: 300251415]",
        related_name="is_formating_technique"
    )
    collection_reference = models.URLField(
        blank=True, verbose_name="Collection reference [institution] [permalink]"
    )
    weight = models.IntegerField(
        blank=True, null=True, verbose_name="Weight [g] [AAT ID: 300056240]"
    )
    height = models.FloatField(
        blank=True, null=True, verbose_name="Height (max.) [mm] [AAT ID: 300055644]"
    )
    width = models.FloatField(
        blank=True, null=True, verbose_name="Width (max.) [mm] [AAT ID: 300055647]"
    )
    length = models.FloatField(
        blank=True, null=True, verbose_name="Length (max.) [mm] [AAT ID: 300055645]"
    )
    filling_height = models.FloatField(
        blank=True, null=True,
        verbose_name="Filling Height [mm] ['filling' AAT ID: 300053092; 'height': 300055644]"
    )
    filling_volume = models.FloatField(
        blank=True, null=True,
        verbose_name="Filling Volume [cm3] ['filling' AAT ID: 300053092; 'volume': 300055649]"
    )
    material_volume = models.FloatField(
        blank=True, null=True,
        verbose_name="Material Volume [cm3] ['material': AAT ID: 300010358; 'volume': 300055649]"
    )
    material_density = models.FloatField(
        blank=True, null=True,
        verbose_name="Material Density [g/cm3]\
        ['material': AAT ID: 300010358; 'density': 300056237]"
    )
    outer_volume = models.FloatField(
        blank=True, null=True,
        verbose_name="Outer Volume [cm3] ['volume' AAT ID: 300055649]"
    )

    def __str__(self):
        return self.belongs_to.has_title
