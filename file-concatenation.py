__author__ = 'zelalem'

import os
import glob

def filefind():
    file_concat=''

    path = '/home/zelalem/Downloads/hersheys_archives/PS_Merge/'
    merge = '/home/zelalem/Downloads/hersheys_archives/PS_year_mnth/'
    dirs = os.listdir(path)


    for dir in dirs:
        try:
            # print(dir)

            path2=path+dir+'/'
            dirs2=os.listdir(path2)
            #
            for file in dirs2:
                path3=path2+file
                # print(path3)

                for files in glob.glob(path3):
                     try:
                        url = open(files)
                        filename=url.read()
                        file_concat=file_concat+filename
                     except:
                        print path3
                        continue
            #
            writer1=open(merge+dir+'.txt','w')
            writer1.write(file_concat)
            writer1.close()
            file_concat=''
        except:
            print path3
            continue


filefind()
