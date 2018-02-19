__author__ = 'zelalem'

import fastcluster
import matplotlib.pyplot as plt
from scipy import spatial
data  = [[0.1,0.1,0.1,0.5],
        [0.1,0.1,0.1,0.56],
        [0.1,0.1,0.1,0.23],
        [0.2,0.2,0.2,0.58],
        [0.2,0.2,0.2,0.45],
        [0.2,0.2,0.2,0.78],
        [0.3,0.3,0.3,0.89],
        [0.3,0.3,0.3,0.88],
        [0.3,0.3,0.3,0.01],]


distance = spatial.distance.pdist(data)
print distance
# list of methods linkage, single, complete, average, weighted, centroid, median, ward

linkage = fastcluster.linkage(distance,method="median")
clusternum = 3
clustdict = {i:[i] for i in xrange(len(linkage)+1)}
for i in xrange(len(linkage)-clusternum+1):
    clust1= int(linkage[i][0])
    clust2= int(linkage[i][1])
    clustdict[max(clustdict)+1] = clustdict[clust1] + clustdict[clust2]
    del clustdict[clust1], clustdict[clust2]
print clustdict

