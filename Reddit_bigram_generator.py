_author__ = 'zelalem'

import glob
from nltk.util import ngrams
import pathlib as path
import pandas as pd


ddf = pd.read_csv('/home/zelalem/Downloads/hersheys_archives/reddit-bi-gram-2008-MI.csv')
ddf = ddf.set_index('Unnamed: 0')
mi_threshold_higher = 15.355799493
mi_threshold_lower = -6.9999973893
# fileList = ('/home/zelalem/Downloads/hersheys_archives/SN_test/*.txt')
fileList = ('/home/zelalem/Downloads/hersheys_archives/reddit_out/*.txt')
dirs = glob.glob(fileList)
for files in dirs:
    print '===============***********************==================='
    tFile = open(files)
    text = tFile.readlines()
    tFile.close()

    file_txt = open("/home/zelalem/Downloads/hersheys_archives/reddit_2008_bigram/" + path.PurePath(files).parts[6], "w")
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
                        MI_value = ddf.loc[words+' ', 'Mutual_Info']

                        if MI_value >= mi_threshold_lower and MI_value <= mi_threshold_higher :
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