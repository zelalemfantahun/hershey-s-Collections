__author__ = 'zelalem'

import glob


file_path = ('/home/zelalem/Desktop/reddit/*.txt')
dirs = glob.glob(file_path)

for files in dirs:
    reddit_file = open(files)
    reddit_file = reddit_file.read()
    reddit_file = reddit_file.split('\n')

    for i in reddit_file:
        reddit_line =  i.split(' ----++++---- ')

        if len(reddit_line) == 2:
            reddit_date = str((reddit_line[1]).split()[0])
            reddit_text = str(reddit_line [0])
            print reddit_text+'*****************'+reddit_date

