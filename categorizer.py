__author__ = 'zelalem'

import os


def categorize2():
    path = '/home/zelalem/Downloads/hersheys_archives/PS_Phrase/'
    finalpath='/home/zelalem/Downloads/hersheys_archives/PS_Phrase_month_day/'
    dirs = os.listdir(path)
    file_concat = ''
    list1 = []

    for file in dirs:
        file_path = path+file

        file2 = file.split('-')
        # file2acc=file2[0]+'-'+file2[1]+'-'+file2[2]
        file2acc=file2[0]+'-'+file2[1]
        # file2acc=file2[0]

        if file2acc in list1:
            if not os.path.isfile(finalpath+file2acc+'/'+file):
                os.rename(path+file,finalpath+file2acc+'/'+file)
            else:

                os.remove(finalpath+'/'+file)

        else:
            if not os.path.exists(finalpath+file2acc):
                os.mkdir(finalpath+file2acc)
                os.rename(path+file,finalpath+file2acc+'/'+file)
                list1.append(file2acc)
            else:
                if not os.path.isfile(finalpath+file2acc+'/'+file):
                    os.rename(path+file,finalpath+file2acc+'/'+file)
                else:
                    os.remove(finalpath+'/'+file)


categorize2()

