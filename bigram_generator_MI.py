_author__ = 'zelalem'

import glob
from nltk.util import ngrams
import pathlib as path
import pandas as pd


ddf = pd.read_csv('/home/zelalem/Documents/NW-bi-gram-MI.csv')
ddf = ddf.set_index('Unnamed: 0')
mi_threshold = -1
# fileList = ('/home/zelalem/Downloads/hersheys_archives/SN_test/*.txt')
fileList = ('/home/zelalem/Downloads/hersheys_archives/newsweek_phrase/*.txt')
dirs = glob.glob(fileList)
for files in dirs:
    print '===============***********************==================='
    tFile = open(files)
    text = tFile.readlines()
    tFile.close()

    file_txt = open("/home/zelalem/Downloads/hersheys_archives/newsweek_bigram/" + path.PurePath(files).parts[6], "w")
    # file_txt_2 = open("/home/zelalem/Downloads/hersheys_archives/SN_bigrams_not_written/" + path.PurePath(files).parts[6], "w")

    for i in text:
        x = i.split()

        if len(x) == 2:
            bi_grams = (str(x[0]+' '+x[1]))
            file_txt.write(bi_grams)
            file_txt.write('\n')

        else:
            if len(x) > 3:
                six_grams = ngrams(x, 2)
                for grams in six_grams:

                    try:

                        words = (grams[0]+' '+grams[1])
                        MI = ddf.loc[words+' ', 'Mutual_Info']

                        if MI >= mi_threshold:
                            file_txt.write(words)
                            file_txt.write('\n')

                    except:
                        print '========================================='
                        print '||     Word not Found in the CSV       ||'
                        print '========================================='

    file_txt.close()
print '==================='
print '||     Done       ||'
print '==================='