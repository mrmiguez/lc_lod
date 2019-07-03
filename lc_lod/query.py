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
        search = requests.get(
            'http://id.loc.gov/vocabulary/graphicMaterials/label/{0}'.format(urllib.parse.quote(term)),
            timeout=5)
        if search.status_code == 200:
            request = requests.get(f'{search.url.rstrip(".html")}.madsrdf.json').json()
            for item in request:
                if 'http://www.loc.gov/mads/rdf/v1#authoritativeLabel' in item.keys():
                    return item['http://www.loc.gov/mads/rdf/v1#authoritativeLabel'][0]["@value"], item["@id"], "lctgm", request
                elif 'http://www.loc.gov/mads/rdf/v1#useInstead' in item.keys():
                    use_instead = item['http://www.loc.gov/mads/rdf/v1#useInstead'][0]['@id']
                    r = requests.get(f'{use_instead.rstrip(".html")}.madsrdf.json').json()
                    for i in r:
                        if 'http://www.loc.gov/mads/rdf/v1#authoritativeLabel' in i.keys():
                            return i['http://www.loc.gov/mads/rdf/v1#authoritativeLabel'][0]['@value'], i['@id'], "lctgm", r
        else:
            return None


class LCSHQuery(LinkedDataQuery):
    """"""

    def __init__(self):
        LinkedDataQuery.__init__(self)

    def query(self, term):
        term = term.replace(u"\u2014", '--').replace(u"\u2013", '--')
        search = requests.get(
            'http://id.loc.gov/authorities/subjects/label/{0}'.format(urllib.parse.quote(term)),
            timeout=5)
        if search.status_code == 200:
            request = requests.get(f'{search.url.rstrip(".html")}.madsrdf.json').json()
            for item in request:
                if 'http://www.loc.gov/mads/rdf/v1#authoritativeLabel' in item.keys():
                    return item['http://www.loc.gov/mads/rdf/v1#authoritativeLabel'][0]['@value'], item['@id'], "lcsh", request
                elif 'http://www.loc.gov/mads/rdf/v1#useInstead' in item.keys():
                    use_instead = item['http://www.loc.gov/mads/rdf/v1#useInstead'][0]['@id']
                    r = requests.get(f'{use_instead.rstrip(".html")}.madsrdf.json').json()
                    for i in r:
                        if 'http://www.loc.gov/mads/rdf/v1#authoritativeLabel' in i.keys():
                            return i['http://www.loc.gov/mads/rdf/v1#authoritativeLabel'][0]['@value'], i['@id'], "lcsh", r
        else:
            return None


class FASTQuery(LinkedDataQuery):
    """"""

    def __init__(self):
        LinkedDataQuery.__init__(self)

    def query(self, term):
        """
        Great documentation OCLC! /s
        """
        return NotImplemented


class NAFQuery(LinkedDataQuery):
    """"""

    def __init__(self):
        LinkedDataQuery.__init__(self)

    def query(self, term):
        term = term.replace(u"\u2014", '--').replace(u"\u2013", '--')
        search = requests.get(
            'http://id.loc.gov/authorities/names/label/{0}'.format(urllib.parse.quote(term)),
            timeout=15)
        if search.status_code == 200:
            request = requests.get(f'{search.url.rstrip(".html")}.madsrdf.json').json()
            for item in request:
                if 'http://www.loc.gov/mads/rdf/v1#authoritativeLabel' in item.keys() and "http://www.loc.gov/mads/rdf/v1#Authority" in item["@type"]:
                    return item['http://www.loc.gov/mads/rdf/v1#authoritativeLabel'][0]['@value'], item['@id'], "naf", request
                elif 'http://www.loc.gov/mads/rdf/v1#useInstead' in item.keys():
                    use_instead = item['http://www.loc.gov/mads/rdf/v1#useInstead'][0]['@id']
                    r = requests.get(f'{use_instead.rstrip(".html")}.madsrdf.json').json()
                    for i in r:
                        if 'http://www.loc.gov/mads/rdf/v1#authoritativeLabel' in i.keys():
                            return i['http://www.loc.gov/mads/rdf/v1#authoritativeLabel'][0]['@value'], i['@id'], "naf", r


class VIAFQuery(LinkedDataQuery):

    def __init__(self):
        LinkedDataQuery.__init__(self)

    def query(self):
        return NotImplemented


class WikiDataQuery(LinkedDataQuery):

    def __init__(self):
        LinkedDataQuery.__init__(self)

    def query(self):
        return NotImplemented
