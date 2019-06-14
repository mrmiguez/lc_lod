"""
INCLUDED ONLY FOR DEVELOPMENT PURPOSES
Will be deleted
"""

import json
import urllib.parse
from collections import namedtuple

import requests

subject = namedtuple('subject', 'text URI auth authURI parts')


def tgm(term):
    """"""
    term_request = requests.get(
        'http://id.loc.gov/vocabulary/graphicMaterials/label/{0}'.format(urllib.parse.quote(term)),
        timeout=5)
    if term_request.status_code == 200:
        auth = 'lctgm'
        authURI = 'http://id.loc.gov/vocabulary/graphicMaterials'
        data = requests.get('{0}.madsrdf.json'.format(term_request.url.rstrip('.html')))
        ld = json.loads(data.text)
        for item in ld:
            if 'http://www.loc.gov/mads/rdf/v1#authoritativeLabel' in item.keys():
                return subject(item['http://www.loc.gov/mads/rdf/v1#authoritativeLabel'][0]['@value'],
                               item['@id'],
                               auth, authURI, None)
            elif 'http://www.loc.gov/mads/rdf/v1#useInstead' in item.keys():
                use_instead = item['http://www.loc.gov/mads/rdf/v1#useInstead'][0]['@id']
                data = requests.get('{0}.madsrdf.json'.format(use_instead.rstrip('.html')))
                ld = json.loads(data.text)
                for item in ld:
                    if 'http://www.loc.gov/mads/rdf/v1#authoritativeLabel' in item.keys():
                        return subject(item['http://www.loc.gov/mads/rdf/v1#authoritativeLabel'][0]['@value'],
                                       item['@id'],
                                       auth, authURI, None)
    else:
        return None


def lcsh(term):
    """"""
    term = term.replace(u"\u2014", '--').replace(u"\u2013", '--')
    term_request = requests.get(
        'http://id.loc.gov/authorities/subjects/label/{0}'.format(urllib.parse.quote(term)),
        timeout=5)
    if term_request.status_code == 200:
        auth = 'lcsh'
        authURI = 'http://id.loc.gov/authorities/subjects/label/{0}'
        data = requests.get('{0}.madsrdf.json'.format(term_request.url.rstrip('.html')))
        ld = json.loads(data.text)
        for item in ld:
            if 'http://www.loc.gov/mads/rdf/v1#authoritativeLabel' in item.keys():
                return subject(item['http://www.loc.gov/mads/rdf/v1#authoritativeLabel'][0]['@value'],
                               item['@id'],
                               auth, authURI, None)
            elif 'http://www.loc.gov/mads/rdf/v1#useInstead' in item.keys():
                use_instead = item['http://www.loc.gov/mads/rdf/v1#useInstead'][0]['@id']
                data = requests.get('{0}.madsrdf.json'.format(use_instead.rstrip('.html')))
                ld = json.loads(data.text)
                for item in ld:
                    if 'http://www.loc.gov/mads/rdf/v1#authoritativeLabel' in item.keys():
                        return subject(item['http://www.loc.gov/mads/rdf/v1#authoritativeLabel'][0]['@value'],
                                       item['@id'],
                                       auth, authURI, None)
    else:
        return None


def lookup():
    """"""
