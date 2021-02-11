import requests
import rdflib
from rdflib import Graph, RDF
from django.conf import settings


def create_query_sting(param_dict):
    params = "&".join([f"{key}={value}" for key, value in param_dict.items()])
    return params


def get_ttl(param_dict):
    params = create_query_sting(param_dict)
    r = requests.get(f"{settings.ARCHE_SEARCH}?{params}")
    ttl = r.text
    g = rdflib.Graph().parse(data=ttl, format='ttl')
    return g

def get_results(param_dict):
    g = get_ttl(param_dict)
    subj = set([str(url) for url in g.subjects(
            RDF.type,
            rdflib.URIRef('https://vocabs.acdh.oeaw.ac.at/schema#Resource')
        )])
    return list(subj)


def results_to_list(result, value_field):
    return []
