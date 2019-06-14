from lc_lod import *


ldo = LinkedDataObject("Buildings")
print(ldo)
sub = LinkedDataSubject("Buildings")
sub.search()
print(sub)
sub = LinkedDataSubject("Potato").search()
try:
    print(sub.term, sub.uri, sub.vocab)
except AttributeError:
    pass
# genre = LinkedDataGenre("Books")
# print(genre)
# name = LinkedDataName("Homer")
# print(name)
