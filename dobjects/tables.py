import django_tables2 as tables
from django_tables2.utils import A

from dobjects.models import DigitalContainer, Period


class DigitalContainerTable(tables.Table):
    id = tables.LinkColumn(verbose_name='ID')
    id_inv_nr = tables.LinkColumn(verbose_name='Inv. Nr.')
    thumbnail = tables.TemplateColumn(
        template_name="dobjects/templatecolumn/thumbcolumn.html",
        orderable=False
    )
    shape_name = tables.ManyToManyColumn()
    fabric = tables.ManyToManyColumn()
    painting_style = tables.ManyToManyColumn()
    painting_sub_technique = tables.ManyToManyColumn()
    formating_technique = tables.ManyToManyColumn()

    class Meta:
        model = DigitalContainer
        sequence = (
            'id',
            'thumbnail',
            'id_inv_nr',
            'shape_name',
            'period',
            )
        attrs = {"class": "table table-responsive table-hover"}


class PeriodTable(tables.Table):
    id = tables.LinkColumn(verbose_name='ID')
    name = tables.LinkColumn(verbose_name='Period')

    class Meta:
        model = Period
        sequence = (
            'id',
            )
        attrs = {"class": "table table-responsive table-hover"}
