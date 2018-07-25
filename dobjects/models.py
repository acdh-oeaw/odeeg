from django.db import models

from entities.models import Institution, Place
from arche.models import Collection
from vocabs.models import SkosConcept


class Period(models.Model):
    legacy_id = models.CharField(
        max_length=250, blank=True,
        verbose_name="excel row index",
        help_text="excel row index"
    )
    name = models.CharField(
        max_length=250, blank=True,
        verbose_name="Period [AAT ID: 300081446]",
        help_text="Period [AAT ID: 300081446]"
    )
    period_phase = models.CharField(
        max_length=250, blank=True,
        verbose_name="Period/Phase [abbreviation]",
        help_text="Period/Phase [abbreviation]"
    )
    period_url = models.CharField(
        max_length=250, blank=True,
        verbose_name="Period [Chronontology/PeriodO ID]",
        help_text="Period [Chronontology/PeriodO ID]"
    )
    period_start_year = models.IntegerField(
        blank=True, null=True, verbose_name="Period [start] (date range) [AAT ID: 300081446]"
    )
    period_end_year = models.IntegerField(
        blank=True, null=True, verbose_name="Period [end] (date range) [AAT ID: 300081446]"
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        else:
            return "{}".format(self.id)


class DigitalContainer(models.Model):
    """extends arche.models.Collection to store domain specific information taken from
    metadata_ODEEG-archaeology.xslx"""

    folder_name = models.CharField(
        max_length=300, blank=True
    )
    id_inv_nr = models.CharField(
        max_length=300, blank=True, verbose_name="ID Inv.Nr."
    )
    bapd_nr = models.CharField(
        max_length=300, blank=True, verbose_name="BAPD Nr."
    )
    related_object = models.ManyToManyField(
        'DigitalContainer', blank=True, related_name="has_related_object",
        verbose_name="Object is associated to [ID Inv.Nr.]"
    )
    belongs_to = models.OneToOneField(
        Collection, on_delete=models.CASCADE, primary_key=True,
        verbose_name='describes collection', related_name="described_by"
    )
    period = models.ForeignKey(
        Period, blank=True, null=True,
        verbose_name="Period", help_text="Period",
        related_name="is_periode_for", on_delete=models.SET_NULL
    )
    located_at = models.ForeignKey(
        Institution, blank=True, null=True,
        verbose_name="Collection [specific] [AAT ID: 300025976]",
        help_text="Collection [specific] [AAT ID: 300025976]",
        related_name="home_of_dobject", on_delete=models.SET_NULL
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
    pl_find = models.ForeignKey(
        Place, blank=True, null=True, related_name="finding_spot_of", on_delete=models.SET_NULL,
        verbose_name="Provenance: finding spot ['provenance' AAT ID: 300055863]"
    )
    pl_find_cert = models.CharField(
        max_length=300, blank=True, verbose_name="certaintiy AAT ID",
        help_text="Provenance: finding spot\
        [AAT ID 'possible', not all facts/scholars agree: 300404777;\
        'undetermined': 300379012; 'unavailable': 300400512]"
    )
    prov_attr_artist = models.TextField(
        blank=True, verbose_name="Provenance: attributed to artist/maker",
        help_text="Provenance: attributed to artist/maker ['provenance' AAT ID: 300055863]"
    )
    pl_prod_center = models.ForeignKey(
        Place, blank=True, null=True, related_name="production_spot_of", on_delete=models.SET_NULL,
        verbose_name="Provenance: production center/workshop ['provenance' AAT ID: 300055863]"
    )
    pl_acq = models.ForeignKey(
        Place, blank=True, null=True, related_name="acquisition_spot_of", on_delete=models.SET_NULL,
        verbose_name="Provenance: place of latest acquisition\
        [modern times] ['provenance' AAT ID: 300055863]"
    )
    cva_ref = models.CharField(
        max_length=500, blank=True, verbose_name="CVA Reference"
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
