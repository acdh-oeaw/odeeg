import reversion
from django.db import models
from django.urls import reverse

from entities.models import Institution, Place, Person
from arche.models import Collection, Resource
from vocabs.models import SkosConcept


DATE_ACCURACY = (
    ('Y', 'Year'),
    ('YM', 'Month'),
    ('DMY', 'Day')
)


@reversion.register()
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

    @classmethod
    def get_listview_url(self):
        return reverse('dobjects:browse_periods')

    @classmethod
    def get_createview_url(self):
        return reverse('dobjects:period_create')

    def get_absolute_url(self):
        return reverse('dobjects:period_detail', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False


@reversion.register()
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
        Collection, on_delete=models.CASCADE, blank=True, null=True,
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

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.id_inv_nr

    @classmethod
    def get_listview_url(self):
        return reverse('dobjects:browse_digitalcontainers')

    @classmethod
    def get_createview_url(self):
        return reverse('dobjects:digitalcontainer_create')

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-belongs_to')
        if prev:
            return prev.first().id
        return False

    def get_absolute_url(self):
        return reverse('dobjects:digitalcontainer_detail', kwargs={'pk': self.id})

    def fetch_binaries(self, bin_type='photos'):
        try:
            search_string = "{}/{}/{}".format(self.belongs_to.acdh_id, bin_type, self.folder_name)
            return Resource.objects.filter(acdh_id__istartswith=search_string)
        except AttributeError:
            return None


@reversion.register()
class ThreeD(models.Model):
    """provides metadata about the production of 3D-Models"""

    digital_container = models.ForeignKey(
        DigitalContainer, blank=True, null=True,
        verbose_name="Vase Object (ID Inv.Nr.)", help_text="The 3d models source",
        related_name="has_threed", on_delete=models.SET_NULL
    )
    survey_location = models.ForeignKey(
        Institution, blank=True, null=True,
        verbose_name="3D Survey: location", help_text="3D Survey: location",
        related_name="survey_location_of", on_delete=models.SET_NULL
    )
    survey_location_comment = models.CharField(
        max_length=300, blank=True, verbose_name="3D Survey: location characteristics."
    )
    start_date = models.DateField(
        blank=True, null=True,
        verbose_name="3D Survey: date.",
        help_text="YYYY-MM-DD"
    )
    date_accuracy = models.CharField(
        blank=True,
        default="M", max_length=3, choices=DATE_ACCURACY,
        verbose_name="Accuracy of the Date"
    )
    survey_creator = models.ManyToManyField(
        Person, blank=True, related_name="creted_survey_of",
        verbose_name="3D Survey: author(s)"
    )
    survey_creator_inst = models.ManyToManyField(
        Institution, blank=True, related_name="creted_survey_of",
        verbose_name="3D Survey: institution"
    )
    img_technique = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="3D Survey: imaging technique",
        help_text="3D Survey: imaging technique [AAT ID]",
        related_name="is_img_technique_of", on_delete=models.SET_NULL
    )
    hardware = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="3D Survey: hardware",
        help_text="3D Survey: hardware ['hardware' AAT ID: 300312368]",
        related_name="hardware_for", on_delete=models.SET_NULL
    )
    fov = models.CharField(
        max_length=300, blank=True,
        verbose_name="fov"
    )
    resolution = models.CharField(
        max_length=300, blank=True,
        verbose_name="Resolution  [AAT ID: 300222980]"
    )
    accuracy = models.CharField(
        max_length=300, blank=True,
        verbose_name="Accuracy"
    )
    img_texture_acquisition = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Image texture acquisition [scanner/external camera]",
        help_text="Image texture acquisition [scanner/external camera]",
        related_name="is_img_texture_acquisition", on_delete=models.SET_NULL
    )
    img_texture_acquisition = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Image texture acquisition [scanner/external camera]",
        help_text="Image texture acquisition [scanner/external camera]",
        related_name="is_img_texture_acquisition", on_delete=models.SET_NULL
    )
    img_texture_color = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Image texture acquisition [colour/B&W]",
        help_text="Image texture acquisition [colour/B&W]",
        related_name="is_img_texture_color", on_delete=models.SET_NULL
    )
    img_texture_resolution = models.CharField(
        max_length=300, blank=True,
        verbose_name="Image texture resolution"
    )
    software = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Software acquisition",
        help_text="Software acquisition",
        related_name="software_of", on_delete=models.SET_NULL
    )
    nr_of_scans = models.IntegerField(
        blank=True, null=True, verbose_name="Nr. scans"
    )
    align_start_date = models.DateField(
        blank=True, null=True,
        verbose_name="3D data alignment/merging: date",
        help_text="YYYY-MM-DD"
    )
    align_creator = models.ManyToManyField(
        Person, blank=True, related_name="creted_align_of",
        verbose_name="3D data alignment/merging: author(s)"
    )
    align_creator_inst = models.ManyToManyField(
        Institution, blank=True, related_name="creted_align_of",
        verbose_name="3D data alignment/merging: institution)"
    )
    align_software = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="3D data alignment/merging: software",
        help_text="3D data alignment/merging: software",
        related_name="align_software_of", on_delete=models.SET_NULL
    )
    align_params = models.CharField(
        max_length=300, blank=True,
        verbose_name="3D data final alignment: parameters"
    )
    merging_params = models.CharField(
        max_length=300, blank=True,
        verbose_name="3D data merging: parameters"
    )
    lowres_start_date = models.DateField(
        blank=True, null=True,
        verbose_name="Low resolution 3D model post-processing: date",
        help_text="YYYY-MM-DD"
    )
    lowres_creator = models.ManyToManyField(
        Person, blank=True, related_name="creted_lowres_of",
        verbose_name="Low resolution 3D model post-processing: author(s)"
    )
    lowres_creator_inst = models.ManyToManyField(
        Institution, blank=True, related_name="creted_lowres_of",
        verbose_name="Low resolution 3D model post-processing: institution"
    )
    lowres_software = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Low resolution 3D model post-processing: software",
        help_text="Low resolution 3D model post-processing: software",
        related_name="lowres_software_of", on_delete=models.SET_NULL
    )
    lowres_params = models.CharField(
        max_length=300, blank=True,
        verbose_name="Low resolution 3D model post-processing: mesh"
    )

    class Meta:
        ordering = ['digital_container']

    def __str__(self):
        if self.digital_container:
            return "{} [3d model]".format(self.digital_container)
        else:
            return "{} [3d model]".format(self.id)

    @classmethod
    def get_listview_url(self):
        return reverse('dobjects:browse_threeds')

    @classmethod
    def get_createview_url(self):
        return reverse('dobjects:threed_create')

    def get_absolute_url(self):
        return reverse('dobjects:threed_detail', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-digital_container')
        if prev:
            return prev.first().id
        return False
