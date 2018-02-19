__author__ = 'zelalem'

import glob
import os


file_path = ('/home/zelalem/Desktop/reddit/*.txt')
dirs = glob.glob(file_path)

for files in dirs:
    reddit_file = open(files)
    reddit_file = reddit_file.readlines()

    for i in range(len(reddit_file)):
        print(i,'@@@@@@@@',reddit_file[i])
        print(reddit_file[i].split(' ----++++---- '))

    # print reddit_file
    # reddit_file = reddit_file.split('\n')
    # print reddit_file
    # temp = ''
    #
    #
    # for i in reddit_file:
    #     reddit_line =  i.split(' ----++++---- ')
    #
    #
    #     if len(reddit_line) == 2:
    #
    #         if temp != '':
    #
    #
    #             reddit_date = str((reddit_line[1]).split()[0])
    #             reddit_text = str(reddit_line[0])
    #
    #             print temp + ' '+reddit_text + '******************' + reddit_date
    #             temp = ''
    #
    #             file_txt = '/home/zelalem/Desktop/reddit_out/'+reddit_date
    #

    #
    #    #        if os.path.exists(file_txt):
    #                 with open(file_txt, "a") as my_file:
    #                     my_file.write('\n'+reddit_text)
    #
    #             else:
    #                 with open(file_txt, "w") as my_file:
    #                     my_file.write('\n'+reddit_text)
    #
    #         else:
    #             reddit_date = str((reddit_line[1]).split()[0])
    #             reddit_text = str(reddit_line[0])
    #             print reddit_text+'******************' +reddit_date
    #
    #             file_txt = '/home/zelalem/Desktop/reddit_out/'+reddit_date
    #
    #             if os.path.exists(file_txt):
    #                 with open(file_txt, "a") as my_file:
    #                     my_file.write('\n'+reddit_text)
    #             else:
    #                 with open(file_txt, "w") as my_file:
    #                     my_file.write('\n'+reddit_text)
    #
    #
    #
    #
    #     if len(reddit_line) == 1:
    #             temp = temp+ ' ' +reddit_line[0]
    #
    #
    #
# file_txt = open("/home/zelalem/Downloads/hersheys_archives/newsweek_phrase/" + path.PurePath(files).parts[6], "w")