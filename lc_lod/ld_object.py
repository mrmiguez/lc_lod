from .query import *


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

    def search(self):
        """"""
        while self.uri is None:
            for klass in TGMQuery, LCSHQuery, FASTQuery:
                obj = klass()
                print(f'{obj.__class__.__name__} is searching for {self.term}')  # test
                q = obj.query(self.term)
                print(f'{obj.__class__.__name__} has found {q}')  # test
                if q:
                    self.term, self.uri, self.vocab = q
                    break
            else:
                raise ValueError  # todo: class exception


class LinkedDataName(LinkedDataObject):
    """"""

    def __init__(self, term):
        LinkedDataObject.__init__(self, term)


class LinkedDataGenre(LinkedDataObject):
    """"""

    def __init__(self, term):
        LinkedDataObject.__init__(self, term)
