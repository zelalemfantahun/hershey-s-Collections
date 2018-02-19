__author__ = 'zelalem'

import glob
import numpy as np  # a conventional alias
from sklearn.feature_extraction.text import CountVectorizer
filenames = ['/home/zelalem/Downloads/data/austen/Austen_Emma.txt',
             '/home/zelalem/Downloads/data/austen/Austen_Pride.txt',
             '/home/zelalem/Downloads/data/austen/Austen_Sense.txt',
             '/home/zelalem/Downloads/data/austen/CBronte_Jane.txt',
             '/home/zelalem/Downloads/data/austen/CBronte_Professor.txt',
             '/home/zelalem/Downloads/data/austen/CBronte_Villette.txt']

vectorizer = CountVectorizer(input='filename')
dtm = vectorizer.fit_transform(filenames)  # a sparse matrix
vocab = vectorizer.get_feature_names()  # a list
dtm = dtm.toarray()
vocab = np.array(vocab)

filenames[0] == 'home/zelalem/Downloads/data/austen/Austen_Emma.txt'
house_idx = list(vocab).index('house')
dtm[0, house_idx]
print dtm[0, vocab == 'house']



# n, _ = dtm.shape
# dist = np.zeros((n, n))
# for i in range(n):
#     for j in range(n):
#         x, y = dtm[i, :], dtm[j, :]
#         dist[i, j] = np.sqrt(np.sum((x - y)**2))
# from sklearn.metrics.pairwise import euclidean_distances
# dist = euclidean_distances(dtm)
# np.round(dist, 1)
# filenames[1] == '/home/zelalem/Downloads/data/austen/Austen_Pride.txt'
# filenames[3] == '/home/zelalem/Downloads/data/austen/CBronte_Jane.txt'
# dist[1, 3]
# dist[1, 3] > dist[3, 5]
# from sklearn.metrics.pairwise import cosine_similarity
# dist = 1 - cosine_similarity(dtm)
# np.round(dist, 2)
# dist[1, 3]
# dist[1, 3] > dist[3, 5]
# norms = np.sqrt(np.sum(dtm * dtm, axis=1, keepdims=True))
# dtm_normed = dtm / norms
# similarities = np.dot(dtm_normed, dtm_normed.T)
# np.round(similarities, 2)
# similarities[1, 3]
# import os  # for os.path.basename
# import matplotlib.pyplot as plt
# from sklearn.manifold import MDS
# mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
# pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
# xs, ys = pos[:, 0], pos[:, 1]
# names = [os.path.basename(fn).replace('.txt', '') for fn in filenames]
# for x, y, name in zip(xs, ys, names):
#     color = 'orange' if "Austen" in name else 'skyblue'
#     plt.scatter(x, y, c=color)
#     plt.text(x, y, name)
# # plt.show()
# mds = MDS(n_components=3, dissimilarity="precomputed", random_state=1)
# pos = mds.fit_transform(dist)
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2])
# for x, y, z, s in zip(pos[:, 0], pos[:, 1], pos[:, 2], names):
#     ax.text(x, y, z, s)
# # plt.show()
# from scipy.cluster.hierarchy import ward, dendrogram
# linkage_matrix = ward(dist)
# dendrogram(linkage_matrix, labels=names)
# plt.tight_layout()
# plt.show()
#
# labels = c('Austen_Emma', 'Austen_Pride', 'Austen_Sense', 'CBronte_Jane',
#            'CBronte_Professor', 'CBronte_Villette')
# dtm_normed = dtm / rowSums(dtm)
# dist_matrix = dist(dtm_normed)
# tree = hclust(dist_matrix, method="ward")
# plt(tree, labels=labels)