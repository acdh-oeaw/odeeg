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
from . models import Period, DigitalContainer


class DigitalContainerDetailView(DetailView):
    model = DigitalContainer
    template_name = 'dobjects/digitalcontainer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DigitalContainerDetailView, self).get_context_data(**kwargs)
        context['history'] = Version.objects.get_for_object(self.object)
        context['imgs'] = self.object.fetch_binaries()
        context['illustrations'] = self.object.fetch_binaries(bin_type='illustrations')
        context['threeds'] = self.object.fetch_binaries(bin_type='3D-data/3Dscan_lowRes-data')
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
