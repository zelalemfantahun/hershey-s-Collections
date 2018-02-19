__author__ = 'zelalem'

import pandas as pd
import glob
import porter_dictionary
import tables
import numpy as np


PATH = '/home/zelalem/Downloads/xxxxxx/'
PATH2 = '/home/zelalem/Desktop/'
TF = 'reddit_csv_2008_full_archive'

hdf5_path = "/home/zelalem/Downloads/reddit.hdf5"
a = tables.StringAtom(itemsize=24)
hdf5_file = tables.open_file(hdf5_path, mode='w')
data_storage = hdf5_file.create_earray(hdf5_file.root, 'e_array',a, (0,))

columns = []
index = []
fileList = glob.glob(PATH+'*.txt')



for file1 in fileList:

    columns.append(file1.split('/')[5][:-4])

print('******** Reading Words ******')
lines2 = []
lines3 = []
for file1 in fileList:

    tFile = open(file1)
    lines = tFile.readlines()

    for slines in lines:
        temp = slines.splitlines()[0]
        index.append(temp)
    data_storage.append(np.array(index,dtype='S24'))

tFile.close()

print('Size with duplication =',len(index))

def is_float(x):
    try:
        float(x)
        return True
    except:
        return False

for l in index:
    if(not is_float(l)):
        lines2.append(l)

data_storage = lines2
index = set(data_storage)

print('Size without duplication =', len(index))
columns = sorted(columns, key=lambda d: map(int, d.split('-')))
index = sorted(index)

port_dict = porter_dictionary.porter_dictionary()
port_dict.load_dict('/home/zelalem/Downloads/hersheys_archives/dict/reddit_porter_full_2008_dictionary')

temp_index = []

for ind in index:
    if ind in port_dict.dictionary:
        temp_index.append(ind)
    index = temp_index
df1 = pd.DataFrame(0,index = index, columns = columns)
# df1 = df1.fillna(0)
print '********Counting Words********'

file_counter = 0
total_file = len(fileList)
for file1 in fileList:

    file_counter = file_counter+1
    print ('Processing file',file_counter,'of', total_file)
    xy = file1.split('/')
    print xy[5]
    lines3 = []
    tFile = open(file1)
    lines = tFile.readlines()

    for slines in lines:
        lines3.append(slines.splitlines()[0])
    lines = lines3

    for l in lines:
        str2 = file1.split('/')[5][:-4]
        if(not(l=='' or is_float(l))):
            if ( l in index):
                df1.loc[l,str2] = df1.loc[l,str2] + 1
    tFile.close()

port_dict = porter_dictionary.porter_dictionary()
port_dict.load_dict('/home/zelalem/Downloads/hersheys_archives/dict/reddit_porter_full_2008_dictionary')

index2 = []

for ind in index:
    try:
        index2.append(port_dict.dictionary[ind][0])
    except:
        print 'Error--------------:',ind
df1.index = index2
df1.sort_index(inplace=True)
df1.to_csv(PATH2+TF+'.csv')
print('------------------------CSV created------------------------')
print
hdf5_file.close()