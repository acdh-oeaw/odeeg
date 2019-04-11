APP_PY = """
from django.apps import AppConfig
class {{ app_name|title }}Config(AppConfig):
    name = '{{ app_name }}'
"""


ADMIN_PY = """
# generated by SiradReader
from django.contrib import admin
from . models import (
{%- for x in data %}
    {{ x.model_name }}{{ "," if not loop.last }}
{%- endfor %}
)
{%- for x in data %}
admin.site.register({{ x.model_name }})
{%- endfor %}
"""


URLS_PY = """
# generated by SiradReader
from django.conf.urls import url
from . import views
app_name = '{{ app_name }}'
urlpatterns = [
{%- for x in data %}
    url(
        r'^{{ x.model_name|lower }}/$',
        views.{{ x.model_name}}ListView.as_view(),
        name='{{ x.model_name|lower }}_browse'
    ),
    url(
        r'^{{ x.model_name|lower }}/detail/(?P<pk>[0-9]+)$',
        views.{{ x.model_name}}DetailView.as_view(),
        name='{{ x.model_name|lower }}_detail'
    ),
    url(
        r'^{{ x.model_name|lower }}/create/$',
        views.{{ x.model_name}}Create.as_view(),
        name='{{ x.model_name|lower }}_create'
    ),
    url(
        r'^{{ x.model_name|lower }}/edit/(?P<pk>[0-9]+)$',
        views.{{ x.model_name}}Update.as_view(),
        name='{{ x.model_name|lower }}_edit'
    ),
    url(
        r'^{{ x.model_name|lower }}/delete/(?P<pk>[0-9]+)$',
        views.{{ x.model_name}}Delete.as_view(),
        name='{{ x.model_name|lower }}_delete'),
{%- endfor %}
]
"""

FILTERS_PY = """
# generated by SiradReader
import django_filters
from django import forms
from . models import (
{%- for x in data %}
    {{ x.model_name }}{{ "," if not loop.last }}
{%- endfor %}
)
{% for x in data %}
class {{ x.model_name }}ListFilter(django_filters.FilterSet):
    {%- for y in x.fields %}
    {%- if y.model_field_type == 'CharField' %}
    {{y.model_field_name}} = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text={{ x.model_name}}._meta.get_field('{{y.model_field_name}}').help_text,
        label={{ x.model_name}}._meta.get_field('{{y.model_field_name}}').verbose_name
    )
    {%- endif %}
    {%- if y.model_field_type == 'TextField' %}
    {{y.model_field_name}} = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text={{ x.model_name}}._meta.get_field('{{y.model_field_name}}').help_text,
        label={{ x.model_name}}._meta.get_field('{{y.model_field_name}}').verbose_name
    )
    {%- endif %}
    {%- endfor %}
    class Meta:
        model = {{ x.model_name }}
        fields = "__all__"
{% endfor %}
"""

FORMS_PY = """
# generated by SiradReader
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,  Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import Accordion, AccordionGroup
from . models import (
{%- for x in data %}
    {{ x.model_name }}{{ "," if not loop.last }}
{%- endfor %}
)
{% for x in data %}
class {{ x.model_name }}FilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super({{ x.model_name }}FilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    {%- for y in x.fields %}
                    '{{ y.model_field_name }}',
                    {%- endfor %}
                    css_id="more"
                    ),
                )
            )
class {{ x.model_name }}Form(forms.ModelForm):
    class Meta:
        model = {{ x.model_name }}
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super({{ x.model_name }}Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
{% endfor %}
"""


TABLES_PY = """
# generated by SiradReader
import django_tables2 as tables
from django_tables2.utils import A
from . models import (
{%- for x in data %}
    {{ x.model_name }}{{ "," if not loop.last }}
{%- endfor %}
)
{% for x in data %}
class {{ x.model_name }}Table(tables.Table):
    id = tables.LinkColumn(verbose_name='ID')
    class Meta:
        model = {{ x.model_name }}
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}
{% endfor %}
"""

VIEWS_PY = """
# generated by SiradReader
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from . filters import *
from . forms import *
from . tables import *
from . models import (
{%- for x in data %}
    {{ x.model_name }}{{ "," if not loop.last }}
{%- endfor %}
)
from browsing.browsing_utils import GenericListView, BaseCreateView, BaseUpdateView
{% for x in data %}
class {{ x.model_name }}ListView(GenericListView):
    model = {{ x.model_name }}
    filter_class = {{ x.model_name }}ListFilter
    formhelper_class = {{ x.model_name }}FilterFormHelper
    table_class = {{ x.model_name }}Table
    init_columns = [
        'id',
    ]
class {{ x.model_name }}DetailView(DetailView):
    model = {{ x.model_name }}
    template_name = 'browsing/generic_detail.html'
class {{ x.model_name }}Create(BaseCreateView):
    model = {{ x.model_name }}
    form_class = {{ x.model_name }}Form
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super({{ x.model_name }}Create, self).dispatch(*args, **kwargs)
class {{ x.model_name }}Update(BaseUpdateView):
    model = {{ x.model_name }}
    form_class = {{ x.model_name }}Form
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super({{ x.model_name }}Update, self).dispatch(*args, **kwargs)
class {{ x.model_name }}Delete(DeleteView):
    model = {{ x.model_name }}
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('{{ app_name }}:{{ x.model_name|lower }}_browse')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super({{ x.model_name }}Delete, self).dispatch(*args, **kwargs)
{% endfor %}
"""

MODELS_PY = """# generated by appcreator

from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import DateRangeField

from vocabs.models import SkosConcept

from browsing.browsing_utils import model_to_dict

{% for x in data %}
class {{ x.model_name }}(models.Model):
    {% if x.model_helptext %}### {{ x.model_helptext }} ###{% endif %}
    {%- for y in x.model_fields %}
    {%- if y.field_type == 'DateRangeField' %}
    {{ y.field_name }} = {{ y.field_type}}(
    {%- else %}
    {{ y.field_name }} = models.{{ y.field_type}}(
    {%- endif %}
        {%- if y.field_type == 'DecimalField' %}
        max_digits=19,
        decimal_places=10,
        {%- endif %}
        {%- if y.field_type == 'CharField' %}
        {%- if y.choices %}
        choices={{ y.choices }},
        {%- endif %}
        max_length=250,
        blank=True,
        {%- elif y.field_type == 'TextField' %}
        blank=True,
        {%- elif y.field_type == 'ForeignKey' %}
        {%- if y.related_class == 'SkosConcept' %}
        {{ y.related_class }},
        {%- else %}
        "{{ y.related_class }}",
        {%- endif %}
        related_name='{{ y.related_name }}',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        {%- elif y.field_type == 'ManyToManyField' %}
        {%- if y.related_class == 'SkosConcept' %}
        {{ y.related_class }},
        {%- else %}
        "{{ y.related_class }}",
        {%- endif %}
        related_name='{{ y.related_name }}',
        blank=True,
        {%- else %}
        blank=True, null=True,
        {%- endif %}
        verbose_name="{{ y.field_verbose_name }}",
        help_text="{{ y.field_helptext }}",
    )
    {%- endfor %}

    def __str__(self):
        return "{}".format(self.id)

{% endfor %}
"""
