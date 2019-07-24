import datetime
from haystack import indexes

from . models import Object


class ObjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Object
