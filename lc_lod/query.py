from .ld_object import *
import requests
import urllib


class LinkedDataQuery(requests.Request):
    """"""

    def __init__(self):
        super(LinkedDataQuery, self).__init__()


class TGMQuery(LinkedDataQuery):
    """"""

    def __init__(self):
        LinkedDataQuery.__init__(self)

    def query(self, term):
        # return f'uri:tgm-{term}', 'tgm'
        # try:
        #     request = requests.get(
        #         'http://id.loc.gov/vocabulary/graphicMaterials/label/{0}.json'.format(urllib.parse.quote(term)),
        #         timeout=5).json()
        #     return request[0]["@id"], request[0]["http://www.loc.gov/mads/rdf/v1#authoritativeLabel"][0]["@value"]
        # except
        search = requests.get(
            'http://id.loc.gov/vocabulary/graphicMaterials/label/{0}'.format(urllib.parse.quote(term)),
            timeout=5)
        if search.status_code == 200:
            request = requests.get(f'{search.url.rstrip(".html")}.madsrdf.json').json()
            return request[0]["http://www.loc.gov/mads/rdf/v1#authoritativeLabel"][0]["@value"], request[0]["@id"], "lctgm"
        else:
            return None

class LCSHQuery(LinkedDataQuery):
    """"""

    def __init__(self):
        LinkedDataQuery.__init__(self)

    def query(self, term):
        return term, f'uri:lcsh-{term}', 'lcsh'


class FASTQuery(LinkedDataQuery):
    """"""

    def __init__(self):
        LinkedDataQuery.__init__(self)

    def query(self, term):
        return term, f'uri:fast-{term}', 'fast'
