from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
# Create your views here.
from browsing.browsing_utils import GenericListView, BaseCreateView, BaseUpdateView
from reversion.models import Version

from . filters import *
from . forms import *
from . models import Period, DigitalContainer, ThreeD, Illustration


class IllustrationListView(GenericListView):
    model = Illustration
    filter_class = IllustrationListFilter
    formhelper_class = IllustrationFilterFormHelper
    init_columns = [
        'id',
        'digital_container'
    ]


class IllustrationDetailView(DetailView):
    model = Illustration
    template_name = 'dobjects/illustration_detail.html'


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
    success_url = reverse_lazy('dobjects:browse_illustrations')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IllustrationDelete, self).dispatch(*args, **kwargs)


class PhotoListView(GenericListView):
    model = Photo
    filter_class = PhotoListFilter
    formhelper_class = PhotoFilterFormHelper
    init_columns = [
        'id',
    ]


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'dobjects/photo_detail.html'


class PhotoCreate(BaseCreateView):

    model = Photo
    form_class = PhotoForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PhotoCreate, self).dispatch(*args, **kwargs)


class PhotoUpdate(BaseUpdateView):

    model = Photo
    form_class = PhotoForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PhotoUpdate, self).dispatch(*args, **kwargs)


class PhotoDelete(DeleteView):
    model = Photo
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('dobjects:browse_photos')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PhotoDelete, self).dispatch(*args, **kwargs)


class ThreeDListView(GenericListView):
    model = ThreeD
    filter_class = ThreeDListFilter
    formhelper_class = ThreeDFilterFormHelper
    init_columns = [
        'id',
    ]


class ThreeDDetailView(DetailView):
    model = ThreeD
    template_name = 'dobjects/threed_detail.html'


class ThreeDCreate(BaseCreateView):

    model = ThreeD
    form_class = ThreeDForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ThreeDCreate, self).dispatch(*args, **kwargs)


class ThreeDUpdate(BaseUpdateView):

    model = ThreeD
    form_class = ThreeDForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ThreeDUpdate, self).dispatch(*args, **kwargs)


class ThreeDDelete(DeleteView):
    model = ThreeD
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('dobjects:browse_threeds')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ThreeDDelete, self).dispatch(*args, **kwargs)


class DigitalContainerDetailView(DetailView):
    model = DigitalContainer
    template_name = 'dobjects/digitalcontainer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DigitalContainerDetailView, self).get_context_data(**kwargs)
        context['history'] = Version.objects.get_for_object(self.object)
        context['imgs'] = self.object.fetch_binaries()
        try:
            context['iiif'] = [
                "{}?format=iiif&PARAM=info.json".format(x.acdh_id) for x in context['imgs']
            ]
        except TypeError:
            context['iiif'] = None
        context['illustrations'] = self.object.fetch_binaries(bin_type='illustrations')
        context['threeds'] = self.object.fetch_binaries(bin_type='3D-data/3Dscan_lowRes-data')
        try:
            context['3d'] = "{}?format=raw".format(context['threeds'][0].acdh_id)
        except (TypeError, IndexError):
            context['3d'] = None
        return context


class DigitalContainerCreate(BaseCreateView):

    model = DigitalContainer
    form_class = DigitalContainerForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DigitalContainerCreate, self).dispatch(*args, **kwargs)


class DigitalContainerUpdate(BaseUpdateView):

    model = DigitalContainer
    form_class = DigitalContainerForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DigitalContainerUpdate, self).dispatch(*args, **kwargs)


class DigitalContainerDelete(DeleteView):
    model = DigitalContainer
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('dobjects:browse_digitalcontainers')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DigitalContainerDelete, self).dispatch(*args, **kwargs)


class DigitalContainerListView(GenericListView):
    model = DigitalContainer
    filter_class = DigitalContainerListFilter
    formhelper_class = DigitalContainerFilterFormHelper
    init_columns = [
        'id',
        'period'
    ]


class PeriodDetailView(DetailView):
    model = Period
    template_name = 'dobjects/period_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PeriodDetailView, self).get_context_data(**kwargs)
        context['history'] = Version.objects.get_for_object(self.object)
        return context


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
    success_url = reverse_lazy('dobjects:browse_periods')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PeriodDelete, self).dispatch(*args, **kwargs)


class PeriodListView(GenericListView):
    model = Period
    filter_class = PeriodListFilter
    formhelper_class = PeriodFilterFormHelper
    init_columns = [
        'id',
        'name',
        'first_name'
    ]
