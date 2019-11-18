from django.conf import settings
from SPARQLWrapper import SPARQLWrapper, JSON

try:
    ARCHE_BG = settings.ARCHE_BG
except AttributeError:
    print("setting.ARCHE_BG not set, use arche-curation-bg as fallback")
    ARCHE_BG = "https://arche-curation.acdh-dev.oeaw.ac.at/blazegraph/sparql"


query_all_binaries = """
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX acdh: <https://vocabs.acdh.oeaw.ac.at/schema#>

Select ?uri ?binaries ?title
where {{
  ?s acdh:hasIdentifier ?uri .
  FILTER STRSTARTS(str(?uri), "{}")
  ?binaries acdh:hasIdentifier ?uri .
  ?binaries rdf:type <http://fedora.info/definitions/v4/repository#Binary> .
  ?binaries acdh:hasTitle ?title .
  }}
"""

query_tifs = """
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX acdh: <https://vocabs.acdh.oeaw.ac.at/schema#>

Select ?uri ?binaries ?title
where {{
  ?s acdh:hasIdentifier ?uri .
  FILTER STRSTARTS(str(?uri), "{}")
  FILTER STRENDS(str(?uri), ".tif")
  ?binaries acdh:hasIdentifier ?uri .
  ?binaries rdf:type <http://fedora.info/definitions/v4/repository#Binary> .
  ?binaries acdh:hasTitle ?title .
}}
"""


def get_results(query, endpoint=ARCHE_BG):
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    try:
        result = sparql.query().convert()
    except Exception as e:
        print("get_results")
        print(e)
        result = []
    return result


def results_to_list(result, value_field):
    try:
        return [x[value_field]['value'] for x in result['results']['bindings']]
    except Exception as e:
        print(e)
        print("results_to_list")
        return []
