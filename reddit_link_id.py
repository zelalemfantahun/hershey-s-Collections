__author__ = 'zelalem'

import json
import os
import datetime


path = '/home/zelalem/Desktop/reddit_json_files/json_link_id/'  # this is source path
store_at='/home/zelalem/Desktop/reddit_json_out/' # this is the path tow write extracted information.
dirs = os.listdir(path)


for file in dirs:
    try:
        print('file in process: ' + file) # used just to keep track of the code execution.
        ''' reading file  '''

        with open(path+file) as json_file:

            data = json_file.readlines()
            # print data

        # extracts the first date if it is not in the first line of the file
        temp_date = ''
        for j in range(len(data)):
            json_i= json.loads(data[j])
            if 'created_utc' in json_i:
                if(j==0):
                    break
                else:
                    time= json_i['created_utc']
                    temp_date = datetime.datetime.utcfromtimestamp(long(time))
                    break



        ''' Here, retrived txt(data) is loaded as json file '''

        for i in data:



            json_i= json.loads(i)




            if 'created_utc' in json_i: # if the comment has date

                if 'link_id' in json_i and 'body' in json_i:

                    link_id = json_i['link_id']

                    final_txt = json_i['body'] # used to get body/content of the comment
                    checker = final_txt.encode('utf8')
                    if str(checker).__contains__('[deleted]'): # by passing deleted comments
                        continue
                    else:
                        time= json_i['created_utc']
                        converted_time= datetime.datetime.utcfromtimestamp(long(time))#  adjusting date formatting
                        temp_date = converted_time
                        reddit_date= str(converted_time).split()[0]


                        file_txt = open("/home/zelalem/Desktop/reddit_json_out/"+(link_id),"a")
                        file_txt.write(final_txt.encode('utf8')+'\n')


    except ArithmeticError:

        print(file + ' not done')
        continue
