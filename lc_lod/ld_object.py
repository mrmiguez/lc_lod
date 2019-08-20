from .query import *
from .exceptions import *


class LinkedDataObject(object):

    def __init__(self, term=None, uri=None, vocab=None, raw=None):
        """"""
        self.term = term
        self.uri = uri
        self.vocab = vocab
        self.raw = raw

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.term}-{self.uri}>'


class LinkedDataSubject(LinkedDataObject):
    """"""

    def __init__(self, term, services=[TGMQuery, LCSHQuery]):
        LinkedDataObject.__init__(self, term)
        while self.raw is None:
            for klass in services:
                obj = klass()
                q = obj.query(self.term)
                if q:
                    self.term, self.uri, self.raw, self.vocab = q
                    break
            else:
                raise LinkedDataObjectException(f'Term--{self.term}--not found.')

    def detail(self):
        """"""


class LinkedDataName(LinkedDataObject):
    """"""

    def __init__(self, term, services=[NAFQuery, VIAFQuery, WikiDataQuery]):
        LinkedDataObject.__init__(self, term)
        while self.raw is None:
            for klass in services:
                obj = klass()
                q = obj.query(self.term)
                if q:
                    self.term, self.uri, self.raw, self.vocab = q
                    break
            else:
                raise LinkedDataObjectException(f'Term--{self.term}--not found.')

    def detail(self):
        """"""


class LinkedDataGenre(LinkedDataObject):
    """"""

    def __init__(self, term, services=[GMGPCQuery, LCGFTQuery, MARCGTQuery]):
        LinkedDataObject.__init__(self, term)
        while self.raw is None:
            for klass in services:
                obj = klass()
                q = obj.query(self.term)
                if q:
                    self.term, self.uri, self.raw, self.vocab = q
                    break
            else:
                raise LinkedDataObjectException(f'Term--{self.term}--not found.')

    def detail(self):
        """"""
