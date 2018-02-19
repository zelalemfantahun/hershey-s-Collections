import fastcluster
import numpy
import scipy.spatial.distance as dist

inFile = open('/home/zelalem/Downloads/demo/input.data', 'r')
inFile.next().strip().split()[1:]
dataMatrix = []
for line in inFile:
    data = line.strip().split()
    # print data
    dataMatrix.append([float(x) for x in data[1:]])

dataMatrix = numpy.array(dataMatrix)
distanceMatrix = dist.pdist(dataMatrix,'euclidean') # Metric: 'euclidean', 'seuclidean', 'cosine', 'hamming', 'correlation'
linkage = fastcluster.linkage(distanceMatrix, method = 'median') # Method 'single','complete','average','weighted','ward','centroid','median'

num_of_cluster = 20
clust_dict = {i:[i] for i in xrange(len(linkage)+1)}
for i in xrange(len(linkage)-num_of_cluster+1):
    clust1= int(linkage[i][0])
    clust2= int(linkage[i][1])
    clust_dict[max(clust_dict)+1] = clust_dict[clust1] + clust_dict[clust2]
    del clust_dict[clust1], clust_dict[clust2]
print clust_dict
