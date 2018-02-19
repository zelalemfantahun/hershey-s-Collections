# -*- coding: utf-8 -*-    # Very important line for UTF8 Encoding ..
import json
import os
import datetime

'''
Code Usage Manual
This code is written to extract useful information from Reddit Json File.
It is intended to only extract comment and its date of creation and write them in a line for
each comments in a reddit file f and for each files in reddit archive iteratively.
the next major move here is to write a code that
- splits each line of text
- For the first time
  - create a file with the date
  - Continue writing the first split to the new file(line by line) until you get new date.
  - when you get a new date close the previous file and create a new file with the new date as a name.
  - follow the above steps ....
- After executing this code you should have a file like 2007-10-01, 2007-10-02, .....,2015-05-30.


'''


path = '/home/zelalem/Desktop/reddit_json_files/'  # this is source path
store_at='/home/zelalem/Desktop/reddit_json_out/' # this is the path tow write extracted information.
dirs = os.listdir(path)
temp_date = ''

for file in dirs:
    try:
        print('file in process: ' + file) # used just to keep track of the code execution.
        ''' reading file  '''

        with open(path+file) as json_file:

            data = json_file.readlines()

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
                if 'body' in json_i:

                    final_txt=json_i['body'] # used to get body/content of the comment
                    checker=final_txt.encode('utf8')
                    if str(checker).__contains__('[deleted]'): # by passing deleted comments
                        continue
                    else:
                        time= json_i['created_utc']
                        converted_time= datetime.datetime.utcfromtimestamp(long(time))#  adjusting date formatting
                        temp_date = converted_time
                        reddit_date= str(converted_time).split()[0]

                        file_txt = store_at+reddit_date

                        if os.path.exists(file_txt):
                            with open(file_txt, "a") as my_file:
                                my_file.write(final_txt.encode('utf8')+'\n')

                        else:
                            with open(file_txt, "w") as my_file:
                                my_file.write(final_txt.encode('utf8')+'\n')


            else:
                if 'body' in json_i: # if the json file- line has body/comment

                    final_txt=json_i['body']
                    checker=final_txt.encode('utf8') # there was sm issue related to the coding mechanism in python(Asc) so this code is used to encode to utf8 format
                    if str(checker).__contains__('[deleted]'):
                        continue
                    else:

                        converted_time= temp_date
                        reddit_date = str(converted_time).split()[0]

                        file_txt = store_at+reddit_date

                        if os.path.exists(file_txt):
                            with open(file_txt, "a") as my_file:
                                my_file.write(final_txt.encode('utf8')+'\n')

                        else:
                            with open(file_txt, "w") as my_file:
                                my_file.write(final_txt.encode('utf8')+'\n')


        print(file + '  done') # confirming successful file exe
    except ArithmeticError:
        print(file + ' not done')
        continue



