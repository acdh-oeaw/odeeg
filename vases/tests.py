from django.conf import settings
from django.test import TestCase

from vases.models import Object
from vases.arche_utils import create_query_sting

QUERY_DICT = {
    "key": "value",
    "key1": "123"
}


class ArcheTest(TestCase):

    def setUp(self):
        self.item = Object.objects.all()[33]

    def test_001_get_tiffs(self):
        query_str = create_query_sting(QUERY_DICT)
        self.assertIsInstance(query_str, 'str')

