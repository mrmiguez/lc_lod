import unittest

from lc_lod import *

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


class LinkedDataNameTests(unittest.TestCase):
    def setUp(self):
        self.lcnaf_name = ld_object.LinkedDataName("Florida State University")
        self.viaf_name = ld_object.LinkedDataName("Florida International University", services=[VIAFQuery])

    def test_name_term(self):
        self.assertEqual("Florida State University", self.lcnaf_name.term)
        self.assertEqual("Florida International University", self.viaf_name.term)

    def test_name_uri(self):
        self.assertEqual("http://id.loc.gov/authorities/names/n80126238", self.lcnaf_name.uri)
        self.assertEqual("http://viaf.org/viaf/134215376", self.viaf_name.uri)

    def test_name_vocab(self):
        self.assertEqual("naf", self.lcnaf_name.vocab)
        self.assertEqual("viaf", self.viaf_name.vocab)


# class LinkedDataGenreTests(unittest.TestCase):
#     def setUp(self):
#         self.gmgpc_term = ld_object.LinkedDataGenre("")
#         self.lcgft_term = ld_object.LinkedDataGenre("")
#         self.marcgt_term = ld_object.LinkedDataGenre("")
#
#     def test_genre_term(self):
#         self.assertEqual("", self.gmgpc_term.term)
#
#     def test_genre_uri(self):
#         self.assertEqual("", self.gmgpc_term.uri)
#
#     def test_genre_vocab(self):
#         self.assertEqual("gmgpc", self.gmgpc_term.vocab)