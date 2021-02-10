from django.conf import settings
import unittest
from vases.models import Object
from vases.arche_utils import create_query_sting, get_results

QUERY_DICT = {
    "key": "value",
    "key1": "123"
}

ACTUAL_SEARCH_PARAMS = {
    "property[0]": "https://vocabs.acdh.oeaw.ac.at/schema%23hasRawBinarySize",
    "operator[1]": "~",
    "property[1]": "https://vocabs.acdh.oeaw.ac.at/schema%23hasIdentifier",
    "value[1]": "^https://id.acdh.oeaw.ac.at/ODeeg/Collections/AT-Vienna-KHM/KHM-ANSA-IV1001",
    "property[2]": "https://vocabs.acdh.oeaw.ac.at/schema%23hasFormat",
    "value[2]": "image/tiff"
}


class ArcheTest(unittest.TestCase):

    def setUp(self):
        self.item = Object.objects.all()[33]

    def test_001_query_string(self):
        query_str = create_query_sting(QUERY_DICT)
        self.assertIsInstance(query_str, str)
        self.assertEqual(
            query_str,
            "key=value&key1=123",
            f"should be 'key=value&key1=123'"
        )
    
    def test_002_get_arche_md(self):
        result = get_results(ACTUAL_SEARCH_PARAMS)
        self.assertIsInstance(result, list)
        self.assertTrue(settings.ARCHE_BASE in result[1])