
__author__ = 'zelalem'

import pandas as pd
import glob
import porter_dictionary
import tables
import numpy as np
from tables import *
import os

PATH = '/home/zelalem/Downloads/reddit_2008_bigram/'
PATH2 = '/home/zelalem/Desktop/'
TF = 'Reddit_csv_2008_full'

hdf5_path = "/home/zelalem/Downloads/reddit.hdf5"
a = tables.StringAtom(itemsize=24)
hdf5_file = tables.open_file(hdf5_path, mode='w')
data_storage = hdf5_file.create_earray(hdf5_file.root, 'e_array',a, (0,))


class csv_creator:

    def __init__(self):

        self.columns = []
        self.index = []
        # self.fileList = os.listdir(PATH)
        self.fileList = glob.glob(PATH+'*.txt')

        pass



    def read_file_names(self):


        for file1 in self.fileList:
            self.columns.append(file1.split('/')[5][:-4])




    def read_words(self):

        print('******** Reading Words ******')
        lines2 = []
        temp = ''

        for file1 in self.fileList:
            tFile = open(file1)
            lines = tFile.readlines()

            for slines in lines:
                # print(slines)
                temp = slines.splitlines()[0]
                if(temp==''):

                    continue

                # # temp
                # else:
                self.index.append(temp)

                #     data_storage.append(np.array(self.index.append(temp),dtype='S24'))
                #     print len(data_storage)
            tFile.close()

        # print self.index
        print('Size with duplication =',len(self.index))

        # print(self.index)

        for l in self.index:
            # print('before appending----------',l)
            if(not self.is_float(l)):
                lines2.append(l)
                # print('after appending************',l)


        self.index = lines2
        self.index = set(self.index)



        print('Size without duplication =', len(self.index))


        self.columns = sorted(self.columns, key=lambda d: map(int, d.split('-')))
        self.index = sorted(self.index)

        # print('zzzzzzzzzzzzzzzzzz')
        # print(self.index)

        port_dict = porter_dictionary.porter_dictionary()
        port_dict.load_dict('/home/zelalem/Downloads/hersheys_archives/dict/reddit_porter_full_2008_dictionary')

        temp_index = []
        for ind in self.index:
            if ind in port_dict.dictionary:
                temp_index.append(ind)

        self.index = temp_index


        self.df1 = pd.DataFrame(index=self.index, columns=self.columns)
        self.df1 = self.df1.fillna(0)
        # self.df1.to_csv(PATH2+'TF.csv')


    def count_words(self):
        print '********Counting Words********'

        counter = 0
        index_value = ''
        drop_list = []

        for file1 in self.fileList:

            lines3 = []
            tFile = open(file1)
            lines = tFile.readlines()


            # This code removes space at in word at beginning of a file
            # if(lines[0].__contains__(' ')):
            #     lines[0] = lines[0][1:]
            for slines in lines:
                # print('$$$$$$$$$$$$$$$$$$',slines)
                # print(slines.splitlines()[0])
                lines3.append(slines.splitlines()[0])
            lines = lines3

            for l in lines:

                str2 = file1.split('/')[5][:-4]
                # print '------------------'+str2

                if(not(l=='' or self.is_float(l))):

                    if ( l in self.index):
                        self.df1.loc[l,str2] = self.df1.loc[l,str2] + 1
                    # counter = counter + 1
                    # print(counter)
            # print self.df1
                # str2 = ''
            tFile.close()


        port_dict = porter_dictionary.porter_dictionary()
        port_dict.load_dict('/home/zelalem/Downloads/hersheys_archives/dict/reddit_porter_full_2008_dictionary')
        # print'@@@@@@@@@@', port_dict.dictionary['at']
        # print self.index
        index2 = []

        for ind in self.index:

            try:
                index2.append(port_dict.dictionary[ind][0])
            except:
                print 'Error--------------:',ind
            #     index2.append(ind)

        self.df1.index = index2
        self.df1.sort_index(inplace=True)
        self.df1.to_csv(PATH2+TF+'.csv')
        print('------------------------CSV created------------------------')


    def is_float(self,x):

        try:
            float(x)
            return True
        except:
            return False

hdf5_file.close()
if __name__ == '__main__':


        a = csv_creator()
        a.read_file_names()
        a.read_words()
        a.count_words()






