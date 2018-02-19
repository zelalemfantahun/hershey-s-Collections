import pandas as pd
import glob

PATH = '/home/zelalem/Downloads/PS_year_mnth/'
PATH2 = '/home/zelalem/Downloads/'

# PATH = '/home/zelalem/Documents/TF1/'
# PATH2 = '/home/zelalem/Documents/'

TF = 'PS_year_month'


class csv_creator:

    def __init__(self):

        self.columns = []
        self.index = []

        self.fileList = glob.glob(PATH+'*.txt')

        pass



    def read_file_names(self):


        for file1 in self.fileList:
            self.columns.append(file1.split('/')[5][:-4])



    def read_words(self):

        lines2 = []
        temp = ''

        for file1 in self.fileList:
            tFile = open(file1)
            lines = tFile.readlines()

            # This code removes space at in word at beginning of a file

            # print('*************',file1)

            if(lines[0].__contains__(' ')):
                lines[0] = lines[0][1:]


            for slines in lines:
                # print(slines)
                temp = slines.splitlines()[0]

                # temp

                self.index.append(temp)

            tFile.close()

        print('Size with duplication =',len(self.index))

        # print(self.index)

        for l in self.index:
            # print('before appending----------',l)
            if(not self.is_float(l)):
                lines2.append(l)
                # print('after appending************',l)


        self.index = lines2

        self.index = set(self.index)



        print('Size without duplication =', len(self.index))


        self.columns = sorted(self.columns, key=lambda d: map(int, d.split('-')))
        self.index = sorted(self.index)

        # print('zzzzzzzzzzzzzzzzzz')
        # print(self.index)

        self.df1 = pd.DataFrame(index=self.index, columns=self.columns)
        self.df1 = self.df1.fillna(0)
        # self.df1.to_csv(PATH2+'TF.csv')


    def count_words(self):

        counter = 0
        index_value = ''
        drop_list = []

        for file1 in self.fileList:

            lines3 = []
            tFile = open(file1)
            lines = tFile.readlines()


            # This code removes space at in word at beginning of a file
            if(lines[0].__contains__(' ')):
                lines[0] = lines[0][1:]
            for slines in lines:
                # print('$$$$$$$$$$$$$$$$$$',slines)
                # print(slines.splitlines()[0])
                lines3.append(slines.splitlines()[0])
            lines = lines3

            for l in lines:
                str2 = file1.split('/')[5][:-4]
                if(not self.is_float(l)):
                    self.df1.loc[l,str2] = self.df1.loc[l,str2] + 1
                    counter = counter + 1
                    # print(counter)


            tFile.close()

        print('------------------------CSV created------------------------')





        self.df1.to_csv(PATH2+TF+'.csv')
        self.df1.to_html(PATH2+TF+'.html')

    def is_float(self,x):

        try:
            float(x)
            return True
        except:
            return False


if __name__ == '__main__':

    a = csv_creator()
    a.read_file_names()
    a.read_words()
    a.count_words()




