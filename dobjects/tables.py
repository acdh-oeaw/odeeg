import django_tables2 as tables
from django_tables2.utils import A

from dobjects.models import DigitalContainer


class DigitalContainerTable(tables.Table):
    id = tables.LinkColumn(verbose_name='ID')
    fabric = tables.ManyToManyColumn()
    painting_style = tables.ManyToManyColumn()
    painting_sub_technique = tables.ManyToManyColumn()
    formating_technique = tables.ManyToManyColumn()

    class Meta:
        model = DigitalContainer
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}
