import pandas as pd
import glob

PATH = '/home/zelalem/Downloads/hersheys_archives/1/'
PATH2 = '/home/zelalem/Downloads/hersheys_archives/2/'
TF = 'TF.csv'

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

        for file1 in self.fileList:
            tFile = open(file1)
            lines = tFile.readlines()

            # This code removes space at in word at beginning of a file

            if(lines[0].__contains__(' ')):
                lines[0] = lines[0][1:]

            for slines in lines:
                self.index.append(slines.splitlines()[0])

            tFile.close()

        print('Size with duplication =',len(self.index))


        for l in self.index:
            if(not l.isdigit()):
                lines2.append(l)

        self.index = lines2

        self.index = set(self.index)

        print('Size without duplication =', len(self.index))

        self.df1 = pd.DataFrame(index=self.index, columns=self.columns)
        self.df1 = self.df1.fillna(0)
        # self.df1.to_csv(PATH2+'TF.csv')


    def count_words(self):

        counter = 0

        for file1 in self.fileList:

            lines3 = []
            tFile = open(file1)
            lines = tFile.readlines()


            # This code removes space at in word at beginning of a file
            if(lines[0].__contains__(' ')):
                lines[0] = lines[0][1:]
            for slines in lines:
                lines3.append(slines.splitlines()[0])
            lines = lines3

            for l in lines:
                str2 = file1.split('/')[5][:-4]
                if(not l.isdigit()):
                    self.df1.loc[l,str2] = self.df1.loc[l,str2] + 1
                    counter = counter + 1
                    print(counter)

            tFile.close()
            self.df1.to_csv(PATH2+TF)


if __name__ == '__main__':

    a = csv_creator()
    a.read_file_names()
    a.read_words()
    a.count_words()



