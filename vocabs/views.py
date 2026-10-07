import datetime
import time

from browsing.utils import BaseCreateView, BaseUpdateView, GenericListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from .filters import (
    SkosCollectionListFilter,
    SkosConceptListFilter,
    SkosConceptSchemeListFilter,
    SkosLabelListFilter,
)
from .forms import *
from .models import Metadata, SkosCollection, SkosConcept, SkosConceptScheme, SkosLabel
from .rdf_utils import *
from .tables import *

#####################################################
#   Metadata
#####################################################


class MetadataListView(ListView):
    model = Metadata
    template_name = "vocabs/metadata_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topConcepts"] = SkosConcept.objects.filter(top_concept=True)
        return context


class MetadataDetailView(DetailView):
    model = Metadata
    template_name = "vocabs/metadata_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topConcepts"] = SkosConcept.objects.filter(top_concept=True)
        return context


class MetadataCreate(BaseCreateView):
    model = Metadata
    form_class = MetadataForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class MetadataUpdate(BaseUpdateView):
    model = Metadata
    form_class = MetadataForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class MetadataDelete(DeleteView):
    model = Metadata
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("vocabs:metadata")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


#####################################################
#   SkosCollection
#####################################################


class SkosCollectionListView(GenericListView):
    model = SkosCollection
    table_class = SkosCollectionTable
    filter_class = SkosCollectionListFilter
    formhelper_class = SkosCollectionFormHelper
    init_columns = [
        "id",
        "name",
    ]


class SkosCollectionDetailView(DetailView):
    model = SkosCollection
    template_name = "vocabs/skoscollection_detail.html"


class SkosCollectionCreate(BaseCreateView):
    model = SkosCollection
    form_class = SkosCollectionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SkosCollectionUpdate(BaseUpdateView):
    model = SkosCollection
    form_class = SkosCollectionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SkosCollectionDelete(DeleteView):
    model = SkosCollection
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("vocabs:browse_skoscollections")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


#####################################################
#   Concept
#####################################################


class SkosConceptListView(GenericListView):
    model = SkosConcept
    table_class = SkosConceptTable
    filter_class = SkosConceptListFilter
    formhelper_class = SkosConceptFormHelper
    init_columns = [
        "id",
        "pref_label",
        "broader_concept",
    ]


class SkosConceptDetailView(DetailView):
    model = SkosConcept
    template_name = "vocabs/skosconcept_detail.html"


class SkosConceptCreate(BaseCreateView):
    model = SkosConcept
    form_class = SkosConceptForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SkosConceptUpdate(BaseUpdateView):
    model = SkosConcept
    form_class = SkosConceptForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SkosConceptDelete(DeleteView):
    model = SkosConcept
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("vocabs:browse_vocabs")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


#####################################################
#   ConceptScheme
#####################################################


class SkosConceptSchemeListView(GenericListView):
    model = SkosConceptScheme
    table_class = SkosConceptSchemeTable
    filter_class = SkosConceptSchemeListFilter
    formhelper_class = SkosConceptSchemeFormHelper
    init_columns = [
        "id",
        "dc_title",
    ]


class SkosConceptSchemeDetailView(DetailView):
    model = SkosConceptScheme
    template_name = "vocabs/skosconceptscheme_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["concepts"] = SkosConcept.objects.filter(scheme=self.kwargs.get("pk"))
        return context


class SkosConceptSchemeCreate(BaseCreateView):
    model = SkosConceptScheme
    form_class = SkosConceptSchemeForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SkosConceptSchemeUpdate(BaseUpdateView):
    model = SkosConceptScheme
    form_class = SkosConceptSchemeForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SkosConceptSchemeDelete(DeleteView):
    model = SkosConceptScheme
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("vocabs:browse_schemes")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


###################################################
# SkosLabel
###################################################


class SkosLabelListView(GenericListView):
    model = SkosLabel
    table_class = SkosLabelTable
    filter_class = SkosLabelListFilter
    formhelper_class = SkosLabelFormHelper
    init_columns = [
        "id",
        "name",
    ]



class SkosLabelDetailView(DetailView):
    model = SkosLabel
    template_name = "vocabs/skoslabel_detail.html"


class SkosLabelCreate(BaseCreateView):
    model = SkosLabel
    form_class = SkosLabelForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SkosLabelUpdate(BaseUpdateView):
    model = SkosLabel
    form_class = SkosLabelForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SkosLabelDelete(DeleteView):
    model = SkosLabel
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("vocabs:browse_skoslabels")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


###################################################
# SkosConcepts download as one ConceptScheme
###################################################


class SkosConceptDL(GenericListView):
    model = SkosConcept
    table_class = SkosConceptTable
    filter_class = SkosConceptListFilter
    formhelper_class = SkosConceptFormHelper

    def render_to_response(self, context):
        timestamp = datetime.datetime.fromtimestamp(
            time.time(), tz=datetime.UTC
        ).strftime(
            "%Y-%m-%d-%H-%M-%S"
        )
        response = HttpResponse(content_type="application/xml; charset=utf-8")
        filename = f"download_{timestamp}"
        response["Content-Disposition"] = f'attachment; filename="{filename}.rdf"'
        g = graph_construct_qs(self.get_queryset())
        get_format = self.request.GET.get("format", default="pretty-xml")
        g.serialize(destination=response, format=get_format)
        return response
