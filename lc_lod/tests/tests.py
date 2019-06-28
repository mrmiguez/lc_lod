import unittest

from lc_lod import ld_object

#sub_list = ['', 'Astrophysics', '', 'Florida State University']


class LinkedDataSubjectTests(unittest.TestCase):
    def setUp(self):
        self.tgm_term = ld_object.LinkedDataSubject("City & town life")
        self.redirect_term = ld_object.LinkedDataSubject("Letters")
        self.lcsh_term = ld_object.LinkedDataSubject("Astrophysics--Periodicals")

    def test_subject_term(self):
        self.assertEqual("City & town life", self.tgm_term.term)
        self.assertEqual("Correspondence", self.redirect_term.term)
        self.assertEqual("Astrophysics--Periodicals", self.lcsh_term.term)

    def test_subject_uri(self):
        self.assertEqual("http://id.loc.gov/vocabulary/graphicMaterials/tgm002106", self.tgm_term.uri)
        self.assertEqual("http://id.loc.gov/vocabulary/graphicMaterials/tgm002590", self.redirect_term.uri)
        self.assertEqual("http://id.loc.gov/authorities/subjects/sh2007101551", self.lcsh_term.uri)

    def test_subject_vocab(self):
        self.assertEqual("lctgm", self.tgm_term.vocab)
        self.assertEqual("lctgm", self.redirect_term.vocab)
        self.assertEqual("lcsh", self.lcsh_term.vocab)
