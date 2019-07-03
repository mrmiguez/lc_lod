from .query import *
from .exceptions import *


class LinkedDataObject(object):

    def __init__(self, term=None, uri=None, vocab=None):
        """"""
        self.term = term
        self.uri = uri
        self.vocab = vocab

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.term}-{self.uri}>'


class LinkedDataSubject(LinkedDataObject):
    """"""

    def __init__(self, term):
        LinkedDataObject.__init__(self, term)
        while self.uri is None:
            for klass in TGMQuery, LCSHQuery:
                obj = klass()
                q = obj.query(self.term)
                if q:
                    self.term, self.uri, self.vocab, self.raw = q
                    break
            else:
                raise LinkedDataObjectException(f'Term--{self.term}--not found.')

    def detail(self):
        """"""


class LinkedDataName(LinkedDataObject):
    """"""

    def __init__(self, term):
        LinkedDataObject.__init__(self, term)
        while self.uri is None:
            for klass in NAFQuery, VIAFQuery, WikiDataQuery:
                obj = klass()
                q = obj.query(self.term)
                if q:
                    self.term, self.uri, self.vocab, self.raw = q
                    break
            else:
                raise LinkedDataObjectException(f'Term--{self.term}--not found.')

    def detail(self):
        """"""


class LinkedDataGenre(LinkedDataObject):
    """"""

    def __init__(self, term):
        LinkedDataObject.__init__(self, term)
