__author__ = 'zelalem'
#
import textmining
from math import*
import numpy as np
from scipy.spatial.distance import pdist, euclidean, squareform
# #
doc1 = 'John and Bob are brothers.'
doc2 = 'John went to the store. The store was closed.'
doc3 = 'Bob went to the store too.'

tdm = textmining.TermDocumentMatrix()

tdm.add_doc(doc1)
tdm.add_doc(doc2)
tdm.add_doc(doc3)

tdm.write_csv('/home/zelalem/Downloads//matrix.csv', cutoff=1)


a = list(tdm.rows(cutoff=1))[1:]
x = a[0]
y = a[1]
print a[2]

from sklearn.metrics.pairwise import euclidean_distances
X = [[0, 1], [1, 1]]
print euclidean_distances(X, X)