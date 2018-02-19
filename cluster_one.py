__author__ = 'zelalem'

import fastcluster
import numpy
import scipy.spatial.distance as dist
import csv
import tables

hdf5_path = "/home/zelalem/Downloads/popular_year.hdf5"
a = tables.StringAtom(itemsize=24)
hdf5_file = tables.open_file(hdf5_path, mode='w')
data_storage = hdf5_file.create_earray(hdf5_file.root, 'e_array',a, (0,))

f = open('/home/zelalem/Desktop/PS_year_month.csv','rb')
reader = list(csv.reader(f))
dataMatrix = []

for row in reader[1:]:

    dataMatrix.append(row[1:])

dataMatrix = numpy.array(dataMatrix)
# distanceMatrix = dist.pdist(dataMatrix,'euclidean') # Metric: 'euclidean', 'seuclidean', 'cosine', 'hamming', 'correlation'
data_storage.append(dist.pdist(dataMatrix,'euclidean')) # Metric: 'euclidean', 'seuclidean', 'cosine', 'hamming', 'correlation'
linkage = fastcluster.linkage(data_storage, method='median') # Method 'single','complete','average','weighted','ward','centroid','median'
num_of_cluster = 8
clust_dict = {i: [i] for i in xrange(len(linkage)+1)}


for i in xrange(len(linkage)-num_of_cluster+1):
    clust1= int(linkage[i][0])
    clust2= int(linkage[i][1])
    clust_dict[max(clust_dict)+1] = clust_dict[clust1] + clust_dict[clust2]
    del clust_dict[clust1], clust_dict[clust2]

print clust_dict

clust_dict_list = list(clust_dict)
clust_dict_keys= clust_dict.keys()
print clust_dict_keys
print '===================='
for yy in clust_dict_keys:

    for j in clust_dict[yy]:
        print j, ':', reader[j+1][0]
    print '**************'