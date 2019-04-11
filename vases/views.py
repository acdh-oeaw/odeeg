# generated by appcreator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from . filters import *
from . forms import *
from . tables import *
from . models import (
    Certainty,
    CollectionSpec,
    Culture,
    Fabric,
    Hardware,
    Illustration,
    IllustrationPanel,
    ImagingTechnique,
    Institution,
    Material,
    Object,
    PaintingStyle,
    PaintingSubTechnique,
    Period,
    Person,
    Place,
    Shape,
    ShapeComponent,
    ThreedData
)
from browsing.browsing_utils import GenericListView, BaseCreateView, BaseUpdateView


class CertaintyListView(GenericListView):

    model = Certainty
    filter_class = CertaintyListFilter
    formhelper_class = CertaintyFilterFormHelper
    table_class = CertaintyTable
    init_columns = [
        'id',
    ]


class CertaintyDetailView(DetailView):

    model = Certainty
    template_name = 'browsing/generic_detail.html'


class CertaintyCreate(BaseCreateView):

    model = Certainty
    form_class = CertaintyForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CertaintyCreate, self).dispatch(*args, **kwargs)


class CertaintyUpdate(BaseUpdateView):

    model = Certainty
    form_class = CertaintyForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CertaintyUpdate, self).dispatch(*args, **kwargs)

class CertaintyDelete(DeleteView):
    model = Certainty
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:certainty_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CertaintyDelete, self).dispatch(*args, **kwargs)


class CollectionSpecListView(GenericListView):

    model = CollectionSpec
    filter_class = CollectionSpecListFilter
    formhelper_class = CollectionSpecFilterFormHelper
    table_class = CollectionSpecTable
    init_columns = [
        'id',
    ]


class CollectionSpecDetailView(DetailView):

    model = CollectionSpec
    template_name = 'browsing/generic_detail.html'


class CollectionSpecCreate(BaseCreateView):

    model = CollectionSpec
    form_class = CollectionSpecForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CollectionSpecCreate, self).dispatch(*args, **kwargs)


class CollectionSpecUpdate(BaseUpdateView):

    model = CollectionSpec
    form_class = CollectionSpecForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CollectionSpecUpdate, self).dispatch(*args, **kwargs)

class CollectionSpecDelete(DeleteView):
    model = CollectionSpec
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:collectionspec_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CollectionSpecDelete, self).dispatch(*args, **kwargs)


class CultureListView(GenericListView):

    model = Culture
    filter_class = CultureListFilter
    formhelper_class = CultureFilterFormHelper
    table_class = CultureTable
    init_columns = [
        'id',
    ]


class CultureDetailView(DetailView):

    model = Culture
    template_name = 'browsing/generic_detail.html'


class CultureCreate(BaseCreateView):

    model = Culture
    form_class = CultureForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CultureCreate, self).dispatch(*args, **kwargs)


class CultureUpdate(BaseUpdateView):

    model = Culture
    form_class = CultureForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CultureUpdate, self).dispatch(*args, **kwargs)

class CultureDelete(DeleteView):
    model = Culture
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:culture_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CultureDelete, self).dispatch(*args, **kwargs)


class FabricListView(GenericListView):

    model = Fabric
    filter_class = FabricListFilter
    formhelper_class = FabricFilterFormHelper
    table_class = FabricTable
    init_columns = [
        'id',
    ]


class FabricDetailView(DetailView):

    model = Fabric
    template_name = 'browsing/generic_detail.html'


class FabricCreate(BaseCreateView):

    model = Fabric
    form_class = FabricForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FabricCreate, self).dispatch(*args, **kwargs)


class FabricUpdate(BaseUpdateView):

    model = Fabric
    form_class = FabricForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FabricUpdate, self).dispatch(*args, **kwargs)

class FabricDelete(DeleteView):
    model = Fabric
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:fabric_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FabricDelete, self).dispatch(*args, **kwargs)


class HardwareListView(GenericListView):

    model = Hardware
    filter_class = HardwareListFilter
    formhelper_class = HardwareFilterFormHelper
    table_class = HardwareTable
    init_columns = [
        'id',
    ]


class HardwareDetailView(DetailView):

    model = Hardware
    template_name = 'browsing/generic_detail.html'


class HardwareCreate(BaseCreateView):

    model = Hardware
    form_class = HardwareForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HardwareCreate, self).dispatch(*args, **kwargs)


class HardwareUpdate(BaseUpdateView):

    model = Hardware
    form_class = HardwareForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HardwareUpdate, self).dispatch(*args, **kwargs)

class HardwareDelete(DeleteView):
    model = Hardware
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:hardware_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HardwareDelete, self).dispatch(*args, **kwargs)


class IllustrationListView(GenericListView):

    model = Illustration
    filter_class = IllustrationListFilter
    formhelper_class = IllustrationFilterFormHelper
    table_class = IllustrationPanel
    init_columns = [
        'id',
    ]


class IllustrationDetailView(DetailView):

    model = Illustration
    template_name = 'browsing/generic_detail.html'


class IllustrationCreate(BaseCreateView):

    model = Illustration
    form_class = IllustrationForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IllustrationCreate, self).dispatch(*args, **kwargs)


class IllustrationUpdate(BaseUpdateView):

    model = Illustration
    form_class = IllustrationForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IllustrationUpdate, self).dispatch(*args, **kwargs)

class IllustrationDelete(DeleteView):
    model = Illustration
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:illustration_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IllustrationDelete, self).dispatch(*args, **kwargs)


class IllustrationPanelListView(GenericListView):

    model = IllustrationPanel
    filter_class = IllustrationPanelListFilter
    formhelper_class = IllustrationPanelFilterFormHelper
    table_class = IllustrationPanelTable
    init_columns = [
        'id',
    ]


class IllustrationPanelDetailView(DetailView):

    model = IllustrationPanel
    template_name = 'browsing/generic_detail.html'


class IllustrationPanelCreate(BaseCreateView):

    model = IllustrationPanel
    form_class = IllustrationPanelForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IllustrationPanelCreate, self).dispatch(*args, **kwargs)


class IllustrationPanelUpdate(BaseUpdateView):

    model = IllustrationPanel
    form_class = IllustrationPanelForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IllustrationPanelUpdate, self).dispatch(*args, **kwargs)

class IllustrationPanelDelete(DeleteView):
    model = IllustrationPanel
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:illustrationtable_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IllustrationPanelDelete, self).dispatch(*args, **kwargs)


class ImagingTechniqueListView(GenericListView):

    model = ImagingTechnique
    filter_class = ImagingTechniqueListFilter
    formhelper_class = ImagingTechniqueFilterFormHelper
    table_class = ImagingTechniqueTable
    init_columns = [
        'id',
    ]


class ImagingTechniqueDetailView(DetailView):

    model = ImagingTechnique
    template_name = 'browsing/generic_detail.html'


class ImagingTechniqueCreate(BaseCreateView):

    model = ImagingTechnique
    form_class = ImagingTechniqueForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ImagingTechniqueCreate, self).dispatch(*args, **kwargs)


class ImagingTechniqueUpdate(BaseUpdateView):

    model = ImagingTechnique
    form_class = ImagingTechniqueForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ImagingTechniqueUpdate, self).dispatch(*args, **kwargs)

class ImagingTechniqueDelete(DeleteView):
    model = ImagingTechnique
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:imagingtechnique_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ImagingTechniqueDelete, self).dispatch(*args, **kwargs)


class InstitutionListView(GenericListView):

    model = Institution
    filter_class = InstitutionListFilter
    formhelper_class = InstitutionFilterFormHelper
    table_class = InstitutionTable
    init_columns = [
        'id',
    ]


class InstitutionDetailView(DetailView):

    model = Institution
    template_name = 'browsing/generic_detail.html'


class InstitutionCreate(BaseCreateView):

    model = Institution
    form_class = InstitutionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InstitutionCreate, self).dispatch(*args, **kwargs)


class InstitutionUpdate(BaseUpdateView):

    model = Institution
    form_class = InstitutionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InstitutionUpdate, self).dispatch(*args, **kwargs)

class InstitutionDelete(DeleteView):
    model = Institution
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:institution_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InstitutionDelete, self).dispatch(*args, **kwargs)


class MaterialListView(GenericListView):

    model = Material
    filter_class = MaterialListFilter
    formhelper_class = MaterialFilterFormHelper
    table_class = MaterialTable
    init_columns = [
        'id',
    ]


class MaterialDetailView(DetailView):

    model = Material
    template_name = 'browsing/generic_detail.html'


class MaterialCreate(BaseCreateView):

    model = Material
    form_class = MaterialForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MaterialCreate, self).dispatch(*args, **kwargs)


class MaterialUpdate(BaseUpdateView):

    model = Material
    form_class = MaterialForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MaterialUpdate, self).dispatch(*args, **kwargs)

class MaterialDelete(DeleteView):
    model = Material
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:material_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MaterialDelete, self).dispatch(*args, **kwargs)


class ObjectListView(GenericListView):

    model = Object
    filter_class = ObjectListFilter
    formhelper_class = ObjectFilterFormHelper
    table_class = ObjectTable
    init_columns = [
        'id',
    ]


class ObjectDetailView(DetailView):

    model = Object
    template_name = 'browsing/generic_detail.html'


class ObjectCreate(BaseCreateView):

    model = Object
    form_class = ObjectForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ObjectCreate, self).dispatch(*args, **kwargs)


class ObjectUpdate(BaseUpdateView):

    model = Object
    form_class = ObjectForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ObjectUpdate, self).dispatch(*args, **kwargs)

class ObjectDelete(DeleteView):
    model = Object
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:object_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ObjectDelete, self).dispatch(*args, **kwargs)


class PaintingStyleListView(GenericListView):

    model = PaintingStyle
    filter_class = PaintingStyleListFilter
    formhelper_class = PaintingStyleFilterFormHelper
    table_class = PaintingStyleTable
    init_columns = [
        'id',
    ]


class PaintingStyleDetailView(DetailView):

    model = PaintingStyle
    template_name = 'browsing/generic_detail.html'


class PaintingStyleCreate(BaseCreateView):

    model = PaintingStyle
    form_class = PaintingStyleForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaintingStyleCreate, self).dispatch(*args, **kwargs)


class PaintingStyleUpdate(BaseUpdateView):

    model = PaintingStyle
    form_class = PaintingStyleForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaintingStyleUpdate, self).dispatch(*args, **kwargs)

class PaintingStyleDelete(DeleteView):
    model = PaintingStyle
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:paintingstyle_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaintingStyleDelete, self).dispatch(*args, **kwargs)


class PaintingSubTechniqueListView(GenericListView):

    model = PaintingSubTechnique
    filter_class = PaintingSubTechniqueListFilter
    formhelper_class = PaintingSubTechniqueFilterFormHelper
    table_class = PaintingSubTechniqueTable
    init_columns = [
        'id',
    ]


class PaintingSubTechniqueDetailView(DetailView):

    model = PaintingSubTechnique
    template_name = 'browsing/generic_detail.html'


class PaintingSubTechniqueCreate(BaseCreateView):

    model = PaintingSubTechnique
    form_class = PaintingSubTechniqueForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaintingSubTechniqueCreate, self).dispatch(*args, **kwargs)


class PaintingSubTechniqueUpdate(BaseUpdateView):

    model = PaintingSubTechnique
    form_class = PaintingSubTechniqueForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaintingSubTechniqueUpdate, self).dispatch(*args, **kwargs)

class PaintingSubTechniqueDelete(DeleteView):
    model = PaintingSubTechnique
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:paintingsubtechnique_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaintingSubTechniqueDelete, self).dispatch(*args, **kwargs)


class PeriodListView(GenericListView):

    model = Period
    filter_class = PeriodListFilter
    formhelper_class = PeriodFilterFormHelper
    table_class = PeriodTable
    init_columns = [
        'id',
    ]


class PeriodDetailView(DetailView):

    model = Period
    template_name = 'browsing/generic_detail.html'


class PeriodCreate(BaseCreateView):

    model = Period
    form_class = PeriodForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PeriodCreate, self).dispatch(*args, **kwargs)


class PeriodUpdate(BaseUpdateView):

    model = Period
    form_class = PeriodForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PeriodUpdate, self).dispatch(*args, **kwargs)

class PeriodDelete(DeleteView):
    model = Period
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:period_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PeriodDelete, self).dispatch(*args, **kwargs)


class PersonListView(GenericListView):

    model = Person
    filter_class = PersonListFilter
    formhelper_class = PersonFilterFormHelper
    table_class = PersonTable
    init_columns = [
        'id',
    ]


class PersonDetailView(DetailView):

    model = Person
    template_name = 'browsing/generic_detail.html'


class PersonCreate(BaseCreateView):

    model = Person
    form_class = PersonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonCreate, self).dispatch(*args, **kwargs)


class PersonUpdate(BaseUpdateView):

    model = Person
    form_class = PersonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonUpdate, self).dispatch(*args, **kwargs)

class PersonDelete(DeleteView):
    model = Person
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:person_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonDelete, self).dispatch(*args, **kwargs)


class PlaceListView(GenericListView):

    model = Place
    filter_class = PlaceListFilter
    formhelper_class = PlaceFilterFormHelper
    table_class = PlaceTable
    init_columns = [
        'id',
    ]


class PlaceDetailView(DetailView):

    model = Place
    template_name = 'browsing/generic_detail.html'


class PlaceCreate(BaseCreateView):

    model = Place
    form_class = PlaceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceCreate, self).dispatch(*args, **kwargs)


class PlaceUpdate(BaseUpdateView):

    model = Place
    form_class = PlaceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceUpdate, self).dispatch(*args, **kwargs)

class PlaceDelete(DeleteView):
    model = Place
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:place_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceDelete, self).dispatch(*args, **kwargs)


class ShapeListView(GenericListView):

    model = Shape
    filter_class = ShapeListFilter
    formhelper_class = ShapeFilterFormHelper
    table_class = ShapeTable
    init_columns = [
        'id',
    ]


class ShapeDetailView(DetailView):

    model = Shape
    template_name = 'browsing/generic_detail.html'


class ShapeCreate(BaseCreateView):

    model = Shape
    form_class = ShapeForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ShapeCreate, self).dispatch(*args, **kwargs)


class ShapeUpdate(BaseUpdateView):

    model = Shape
    form_class = ShapeForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ShapeUpdate, self).dispatch(*args, **kwargs)

class ShapeDelete(DeleteView):
    model = Shape
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:shape_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ShapeDelete, self).dispatch(*args, **kwargs)


class ShapeComponentListView(GenericListView):

    model = ShapeComponent
    filter_class = ShapeComponentListFilter
    formhelper_class = ShapeComponentFilterFormHelper
    table_class = ShapeComponentTable
    init_columns = [
        'id',
    ]


class ShapeComponentDetailView(DetailView):

    model = ShapeComponent
    template_name = 'browsing/generic_detail.html'


class ShapeComponentCreate(BaseCreateView):

    model = ShapeComponent
    form_class = ShapeComponentForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ShapeComponentCreate, self).dispatch(*args, **kwargs)


class ShapeComponentUpdate(BaseUpdateView):

    model = ShapeComponent
    form_class = ShapeComponentForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ShapeComponentUpdate, self).dispatch(*args, **kwargs)

class ShapeComponentDelete(DeleteView):
    model = ShapeComponent
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:shapecomponent_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ShapeComponentDelete, self).dispatch(*args, **kwargs)


class ThreedDataListView(GenericListView):

    model = ThreedData
    filter_class = ThreedDataListFilter
    formhelper_class = ThreedDataFilterFormHelper
    table_class = ThreedDataTable
    init_columns = [
        'id',
    ]


class ThreedDataDetailView(DetailView):

    model = ThreedData
    template_name = 'browsing/generic_detail.html'


class ThreedDataCreate(BaseCreateView):

    model = ThreedData
    form_class = ThreedDataForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ThreedDataCreate, self).dispatch(*args, **kwargs)


class ThreedDataUpdate(BaseUpdateView):

    model = ThreedData
    form_class = ThreedDataForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ThreedDataUpdate, self).dispatch(*args, **kwargs)

class ThreedDataDelete(DeleteView):
    model = ThreedData
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vases:threeddata_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ThreedDataDelete, self).dispatch(*args, **kwargs)


