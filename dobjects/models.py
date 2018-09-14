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
    """Stores information about periods and phases associated with vases."""
    legacy_id = models.CharField(
        max_length=250, blank=True,
        verbose_name="excel row index",
        help_text="excel row index"
    )
    name = models.CharField(
        max_length=250, blank=True,
        verbose_name="Period",
        help_text="Period as defined by Getty AAT with ID 300081446: \
        The length of time during which something runs its course, characterized \
        by some prevalent or distinguishing condition, circumstance, or occurrence, \
        or by the rule of a particular government or dynasty; a distinct historical \
        or cultural portion or division of time. E.g. 'Late Geometric IB'."
    )
    period_phase = models.CharField(
        max_length=250, blank=True,
        verbose_name="Period/Phase",
        help_text="Abbreviation of period or phase, e.g. LG IB."
    )
    period_url = models.CharField(
        max_length=250, blank=True,
        verbose_name="Period ID",
        help_text="ID of a period from as suitable thesauris like PeriodO or \
        Chronontology. Include full permanent link, e.g. \
        'http://n2t.net/ark:/99152/p0ms2chk8gk' or \
        'http://chronontology.dainst.org/period/g2j1npCU5v10'."
    )
    period_start_year = models.IntegerField(
        blank=True, null=True, verbose_name="Period start",
        help_text="Start of period for date range in ISO format, e.g. -750"
    )
    period_end_year = models.IntegerField(
        blank=True, null=True, verbose_name="Period end",
        help_text="End of period for date range in ISO format, e.g. -740"
    )

    class Meta:
        ordering = ['period_start_year']

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        else:
            return "{}".format(self.id)

    # not yet in use, but might be needed
    def get_dates_str(self):
        if self.period_end_year:
            if self.period_end_year < 0:
                return "{} - {} {}".format(abs(self.period_start_year), abs(self.period_end_year), "BCE")
            elif self.period_start_year < 0:
                return "{} {} - {} {}".format(abs(self.period_start_year), "BCE", self.period_end_year, "CE")
            else:
                return "{} - {} {}".format(self.period_start_year, self.period_end_year, "CE")
        elif self.period_start_year:
            if self.period_start_year < 0:
                    "{} {}".format(self.period_start_year, "BCE")
            return "{}".format(self.period_start_year)
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
        max_length=300, blank=True, verbose_name="Folder name",
        help_text="Name of folder containing all files related to the vase."
    )
    shape_name = models.ManyToManyField(
        SkosConcept, blank=True, verbose_name="Shape",
        help_text="blrb",
        related_name="is_shape"
    )
    id_inv_nr = models.CharField(
        max_length=300, blank=True, verbose_name="ID Inv.Nr.",
        help_text="Inventory number of vase."
    )
    bapd_nr = models.CharField(
        max_length=300, blank=True, verbose_name="BAPD Nr.",
        help_text="Corresponding number of vase from Beazley Archive Pottery Database (BAPD)."
    )
    related_object = models.ManyToManyField(
        'DigitalContainer', blank=True, related_name="has_related_object",
        verbose_name="Object is associated to",
        help_text="Other objects associated with this object. \
        Relation is established with 'ID Inv.Nr'."
    )
    belongs_to = models.OneToOneField(
        Collection, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name='describes collection', related_name="described_by",
        help_text="?"
    )
    period = models.ForeignKey(
        Period, blank=True, null=True,
        verbose_name="Period", help_text="Period as defined by Getty AAT with ID 300081446. \
        Periods are stored in a separate table.",
        related_name="is_periode_for", on_delete=models.SET_NULL
    )
    located_at = models.ForeignKey(
        Institution, blank=True, null=True,
        verbose_name="Collection",
        help_text="Collection as defined by Getty AAT with ID: 300025976. \
        Collections are stored in a separate table.",
        related_name="home_of_dobject", on_delete=models.SET_NULL
    )
    fabric = models.ManyToManyField(
        SkosConcept, blank=True, verbose_name="Fabric (as in BAPD)",
        help_text="Fabric as used in the Beazley Archive Pottery Database.",
        related_name="is_fabric"
    )
    painting_style = models.ManyToManyField(
        SkosConcept, blank=True, verbose_name="Painting style/technique (AAT ID)",
        help_text="ID from Getty AAT describing painting style or technique.",
        related_name="is_painting_style"
    )
    painting_sub_technique = models.ManyToManyField(
        SkosConcept, blank=True, verbose_name="Painting sub technique (AAT ID)",
        help_text="ID from Getty AAT describing painting sub technique.",
        related_name="is_painting_sub_technique"
    )
    formating_technique = models.ManyToManyField(
        SkosConcept, blank=True, verbose_name="Forming technique",
        help_text="Forming technique as defined by Getty AAT with ID 300251415",
        related_name="is_formating_technique"
    )
    pl_find = models.ForeignKey(
        Place, blank=True, null=True, related_name="finding_spot_of", on_delete=models.SET_NULL,
        verbose_name="Find spot",
        help_text="Find spot for Provenance as defined by Getty AAT with ID 300055863."
    )
    pl_find_cert = models.CharField(
        max_length=300, blank=True, verbose_name="Certaintiy of find spot",
        help_text="Find spot certainty. Indicate with Getty AAT ID. E.g. \
        'possible', not all facts/scholars agree: 300404777;\
        'undetermined': 300379012; 'unavailable': 300400512"
    )
    prov_attr_artist = models.TextField(
        blank=True, verbose_name="Attributed to artist/maker",
        help_text="Artist or maker the object is attributed to."
    )
    pl_prod_center = models.ForeignKey(
        Place, blank=True, null=True, related_name="production_spot_of", on_delete=models.SET_NULL,
        verbose_name="Production center/workshop",
        help_text="Production center or workshop the object is associated with."
    )
    pl_acq = models.ForeignKey(
        Place, blank=True, null=True, related_name="acquisition_spot_of", on_delete=models.SET_NULL,
        verbose_name="Place of latest acquisition",
        help_text="Place of latest acquisition of object, mostly refers to modern place names."
    )
    cva_ref = models.CharField(
        max_length=500, blank=True, verbose_name="CVA Reference",
        help_text="Reference to publication of object in CVA series."
    )
    collection_reference = models.URLField(
        blank=True, verbose_name="Collection reference",
        help_text="Reference to online publication of object in collection, e.g. \
        web page of museum with object details. When possible provide permanent link."
    )
    weight = models.IntegerField(
        blank=True, null=True, verbose_name="Weight (g)",
        help_text="Weight of object in grams, as defined in Getty AAT with ID 300056240."
    )
    height = models.FloatField(
        blank=True, null=True, verbose_name="Height (max. mm)",
        help_text="Maximum height of object in millimetres, as defined by Getty \
        AAT with ID 300055644."
    )
    width = models.FloatField(
        blank=True, null=True, verbose_name="Width (max. mm)",
        help_text="Maximum width of object in millimetres, as defined by Getty AAT \
        with ID 300055647."
    )
    length = models.FloatField(
        blank=True, null=True, verbose_name="Length (max. mm)",
        help_text="Maximum lenght of object in millimetres, as defined by Getty AAT \
        with ID 300055645."
    )
    filling_height = models.FloatField(
        blank=True, null=True,
        verbose_name="Filling Height (mm)",
        help_text="Filling height of object in millimetres, as defined by Getty AAT \
        with ID 300053092 (filling) and 300055644 (height)."
    )
    filling_volume = models.FloatField(
        blank=True, null=True,
        verbose_name="Filling Volume (cm3)",
        help_text="Filling volume of object in cubic centimetres, as defined by Getty AAT \
        with ID 300053092 (filling) and 300055649 (volume)."
    )
    material_volume = models.FloatField(
        blank=True, null=True,
        verbose_name="Material Volume (cm3)",
        help_text="Material volume of object in cubic centimetres, as defined by Getty AAT \
        with ID 300010358 (material) and 300055649 (volume)."
    )
    material_density = models.FloatField(
        blank=True, null=True,
        verbose_name="Material Density (g/cm3)",
        help_text="Material density of object in grams per cubic centimetre, as \
        defined by Getty AAT with ID 300010358 (material) and 300056237 (density)."
    )
    outer_volume = models.FloatField(
        blank=True, null=True,
        verbose_name="Outer Volume (cm3)",
        help_text="Outer volume of object in cubic centimetres, as defined by Getty AAT \
        with ID 300055649 (volume)."
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

    def get_thumbnail(self):
        img_list = self.fetch_binaries()
        if img_list:
            return "{}?format=iiif&PARAM=/full/,120/0/default.jpg".format(img_list[0].acdh_id)
        else:
            None


@reversion.register()
class ThreeD(models.Model):
    """provides metadata about the production of 3D-Models"""

    digital_container = models.ForeignKey(
        DigitalContainer, blank=True, null=True,
        verbose_name="Vase Object (ID Inv.Nr.)", help_text="The 3d model's source",
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


@reversion.register()
class Photo(models.Model):
    """provides metadata about the production of Photo"""

    digital_container = models.ForeignKey(
        DigitalContainer, blank=True, null=True,
        verbose_name="Vase Object (ID Inv.Nr.)", help_text="The photo's source",
        related_name="has_photo", on_delete=models.SET_NULL
    )
    start_date = models.DateField(
        blank=True, null=True,
        verbose_name="Post-processing: date",
        help_text="YYYY-MM-DD"
    )
    creator = models.ManyToManyField(
        Person, blank=True, related_name="creted_photo_of",
        verbose_name="Post-processing: author"
    )
    software = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Post-processing: software",
        help_text="Post-processing: software",
        related_name="software_of_photo", on_delete=models.SET_NULL
    )
    post_processing_method = models.CharField(
        max_length=300, blank=True,
        verbose_name="Post-processing: method"
    )

    class Meta:
        ordering = ['digital_container']

    def __str__(self):
        if self.digital_container:
            return "{} [photo]".format(self.digital_container)
        else:
            return "{} [photo]".format(self.id)

    @classmethod
    def get_listview_url(self):
        return reverse('dobjects:browse_photos')

    @classmethod
    def get_createview_url(self):
        return reverse('dobjects:photo_create')

    def get_absolute_url(self):
        return reverse('dobjects:photo_detail', kwargs={'pk': self.id})

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


@reversion.register()
class Illustration(models.Model):
    """provides metadata about the production of an Illustration"""

    digital_container = models.ForeignKey(
        DigitalContainer, blank=True, null=True,
        verbose_name="Vase Object (ID Inv.Nr.)", help_text="The photo's source",
        related_name="has_illustration", on_delete=models.SET_NULL
    )
    start_date = models.DateField(
        blank=True, null=True,
        verbose_name="Illustration: date",
        help_text="YYYY-MM-DD"
    )
    creator = models.ManyToManyField(
        Person, blank=True, related_name="created_illustration_of",
        verbose_name="Illustration: author"
    )
    software = models.ManyToManyField(
        SkosConcept, blank=True,
        verbose_name="Illustration: software",
        help_text="Illustration: software",
        related_name="software_of_illustration"
    )
    post_processing_method = models.CharField(
        max_length=300, blank=True,
        verbose_name="Illustration: method"
    )

    class Meta:
        ordering = ['digital_container']

    def __str__(self):
        if self.digital_container:
            return "{} [illustration]".format(self.digital_container)
        else:
            return "{} [illustration]".format(self.id)

    @classmethod
    def get_listview_url(self):
        return reverse('dobjects:browse_illustrations')

    @classmethod
    def get_createview_url(self):
        return reverse('dobjects:illustration_create')

    def get_absolute_url(self):
        return reverse('dobjects:illustration_detail', kwargs={'pk': self.id})

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
