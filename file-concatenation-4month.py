
import os
import glob

def categorize2():
    path = '/home/zelalem/Documents/newsweek-cleaned/'
    finalpath='/home/zelalem/Documents/newsweek-merge-4months/'

    dirs = os.listdir(path)
    file_concat=''
    list1 = []
    ctr=0
    prev_month=[]
    prev_year=[]
    month_count=1
    loc_month=[]
    dict={}
    dict_year={}
    for file in dirs:
        print file
        filepath = path+file
        # print filepath
        tmp=''
        file2 = file.split('-')
        # print file2
        # file2acc = file2[2]
        year=file2[0]
        month=int(file2[1])
        print(year)

        #
        # if (month >=1 and month <=4):
        #     file2acc=year+'-'+'1'
        # elif (month >=5 and month <=8):
        #     file2acc=year+'-'+'2'
        # elif (month >=9 and  month <= 12):
        #     file2acc=year+'-'+'3'
        #
        # if file2acc in list1:
        #     if not os.path.isfile(finalpath+file2acc+'/'+file):
        #         os.rename(path+file, finalpath+file2acc+'/'+file)
        #     else:
        # # #
        #         os.remove(finalpath+'/'+file)
        # # #
        # else:
        #     if not os.path.exists(finalpath+file2acc):
        #         os.mkdir(finalpath+file2acc)
        #         os.rename(path+file, finalpath+file2acc+'/'+file)
        #         list1.append(file2acc)
        #     else:
        #         if not os.path.isfile(finalpath+file2acc+'/'+file):
        #             os.rename(path+file,finalpath+file2acc+'/'+file)
        #         else:
        #             os.remove(finalpath+'/'+file)

categorize2()


