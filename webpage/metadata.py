from django.utils.safestring import mark_safe
# this files contains basic metadata about the project. This data will be used
# (by default) in the base.html and index.html

PROJECT_METADATA = {
    'title': 'ODEEG',
    'author': 'Publisher: Institute for the Study of Ancient Culture (IKAnt), ÖAW: Claudia Lang-Auinger, Vera Moitinho de Almeida, Stefan Spelitz.\n Technical Implementation & Design: Austrian Centre for Digital Humanities (ACDH), ÖAW: Martina Trognitz, Peter Andorfer and Institute for the Study of Ancient Culture (IKAnt), ÖAW: Vera Moitinho de Almeida.',
    'subtitle_en': 'Online database for research on the development of vessel shapes and capacities',
    'subtitle_de': 'Online-Datenbank zur Erforschung der Entwicklung von Gefäßformen und -maßen',
    'description': mark_safe("""ODEEG is an open-access online database for research on the development of ancient pottery shapes and capacities. ODEEG is specially focused on 3D models, filling capacities, metadata, and long term archiving of the data, while applying LOD and FAIR principles. It is connected to the wider <a href="https://www.oeaw.ac.at/en/ancient/publications/overview/publikationen-monant/corpus-vasorum-antiquorum/">CVA project</a>.</br>
Presently, ODEEG includes fine-wear painted vessels, from ancient Greek territories and Cyprus. Whereas the period encompasses 10th–4th century BCE, approximately from the Geometric period to the Hellenistic period.
"""),
    'github': 'https://github.com/acdh-oeaw/odeeg',
    'purpose_de': 'Ziel von ODEEG ist die Publikation von Forschungsdaten.',
    'purpose_en': 'The purpose of ODEEG is the publication of research data.',
    'version': '0.0.1',
    'matomo_id': '92',
    'matomo_url': '//piwik.apollo.arz.oeaw.ac.at/',
    'social_media': [
    ],
    'app_type': 'database',
    'imprint': '/imprint'
}

# 'social_media': [
#        ('data-feather twitter', 'https://twitter.com/ACDH_OeAW'),
#        ('data-feather youtube', 'https://www.youtube.com/channel/UCgaEMaMbPkULYRI5u6gvG-w'),
