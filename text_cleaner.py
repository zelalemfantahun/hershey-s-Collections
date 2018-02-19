__author__ = 'zelalem'

import glob
import re
import pathlib as path
# fileList = glob.glob('/home/zelalem/Downloads/hersheys_archives/PS_error/*.txt') # input file read
fileList = glob.glob('/home/zelalem/Desktop/PS-extracted/*.txt') # input file read

for files in fileList:

     tFile = open(files)
     text = tFile.read().lower()
     text = re.sub('[^a-zA-Z0-9-_*.]', ' ', text)
     # text = re.sub(r"http\S+", "", text)
     text1 = text.replace("\n","")
     text = text1.split('.')
     x = '[illustration omitted]'
     file_txt = open("/home/zelalem/Desktop/ps_corrected_test/"+path.PurePath(files).parts[5], "w")
     for i in text:
         if i.__contains__(x) or i.__contains__('PHOTO :') or i.__contains__('(www') or i.__contains__('com)'):
             pass
         else:
             file_txt.write(i)
             file_txt.write('\n')


     file_txt.close()



tFile.close()
