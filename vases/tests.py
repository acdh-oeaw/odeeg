import unittest

from vases.arche_utils import create_query_sting, get_results
from vases.models import Object

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
            "should be 'key=value&key1=123'"
        )
    
    def test_002_get_arche_md(self):
        result = get_results(ACTUAL_SEARCH_PARAMS)
        self.assertIsInstance(result, list)
        self.assertTrue('id.acdh.oeaw.ac.at'in result[1])