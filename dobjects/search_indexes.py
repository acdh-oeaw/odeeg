import datetime
from haystack import indexes
from . models import DigitalContainer


class DigitalContainerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return DigitalContainer
