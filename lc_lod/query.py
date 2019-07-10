from .ld_object import *
import requests
import urllib


class LinkedDataQuery(requests.Request):
    """"""

    def __init__(self):
        super(LinkedDataQuery, self).__init__()

    @staticmethod
    def lc_search(term, url):
        term = term.replace(u"\u2014", '--').replace(u"\u2013", '--')
        try:
            search = requests.get(url + urllib.parse.quote(term), timeout=15)
            if search.status_code == 200:
                request = requests.get(f'{search.url.rstrip(".html")}.madsrdf.json').json()
                for item in request:
                    if 'http://www.loc.gov/mads/rdf/v1#authoritativeLabel' in item.keys() and "http://www.loc.gov/mads/rdf/v1#Authority" in item["@type"]:
                        return item['http://www.loc.gov/mads/rdf/v1#authoritativeLabel'][0]['@value'], item['@id'], request
                    elif 'http://www.loc.gov/mads/rdf/v1#useInstead' in item.keys():
                        use_instead = item['http://www.loc.gov/mads/rdf/v1#useInstead'][0]['@id']
                        r = requests.get(f'{use_instead.rstrip(".html")}.madsrdf.json').json()
                        for i in r:
                            if 'http://www.loc.gov/mads/rdf/v1#authoritativeLabel' in i.keys():
                                return i['http://www.loc.gov/mads/rdf/v1#authoritativeLabel'][0]['@value'], i['@id'], r
            else:
                return None
        except requests.exceptions.ReadTimeout:
            raise LCTimeOut("Linked data service has timed out after 15 seconds.")


class TGMQuery(LinkedDataQuery):
    """"""

    def __init__(self):
        LinkedDataQuery.__init__(self)

    def query(self, term):
        search = self.lc_search(term, 'http://id.loc.gov/vocabulary/graphicMaterials/label/')
        if search:
            return search + ("lctgm", )
        else:
            return None


class LCSHQuery(LinkedDataQuery):
    """"""

    def __init__(self):
        LinkedDataQuery.__init__(self)

    def query(self, term):
        search = self.lc_search(term, 'http://id.loc.gov/authorities/subjects/label/')
        if search:
            return search + ("lcsh", )
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
        search = self.lc_search(term, 'http://id.loc.gov/authorities/names/label/')
        if search:
            return search + ("naf", )
        else:
            return None


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


class GMGPCQuery(LinkedDataQuery):

    def __init__(self):
        LinkedDataQuery.__init__(self)

    def query(self, term):
        search = self.lc_search(term, 'http://id.loc.gov/vocabulary/graphicMaterials/label/')
        if search:
            return search + ("gmgpc", )  # todo: add some extra logic to check if it can be used as a genre
        else:
            return None


class LCGFTQuery(LinkedDataQuery):

    def __init__(self):
        LinkedDataQuery.__init__(self)

    def query(self, term):
        search = self.lc_search(term, 'id.loc.gov/authorities/genreForms/label/')
        if search:
            return search + ("lgft", )
        else:
            return None


class MARCGTQuery(LinkedDataQuery):

    def __init__(self):
        LinkedDataQuery.__init__(self)

    def query(self, term):
        search = self.lc_search(term, 'http://id.loc.gov/vocabulary/marcgt/label/')  # ??
        if search:
            return search + ("marcgt", )
        else:
            return None
