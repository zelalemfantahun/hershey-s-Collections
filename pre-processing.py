# __author__ = 'zelalem'
#
# import glob
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
#
# s = set()
# fileList = glob.glob('/home/zelalem/Documents/sample/*.txt')
#
# for files in fileList:
#     tFile = open(files)
#     line = tFile.read().lower()
#     stop = stopwords.words('english')
#     line = nltk.word_tokenize(line)
#     s = s.union(set(line))
#     tFile.close()
#
# s = sorted(s)
# filtered_words = [w for w in s if not w in stopwords.words('english')]
#
# listPun = set(",./;'?&-!")
# for line in filtered_words:
#     listPun = set(",./;'?&-!")
#     filtered_words = ''.join(c for c in line if not c in listPun)
#     #print(filtered_words)
#     #
#     # filtered_words = (wnl.lemmatize(filtered_words))
#     print(filtered_words)
#     wnl = WordNetLemmatizer()
#     lem_words = wnl.lemmatize(filtered_words)
#
#     print lem_words
import nltk
from nltk import sent_tokenize
string = "his name is 'zola'. But also."
x = sent_tokenize(string)
print x