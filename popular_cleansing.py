__author__ = 'zelalem'
# -*- coding: utf-8 -*-

import re
import glob
import nltk
from nltk.corpus import stopwords
import pathlib as path
from stemming.porter2 import stem
from nltk.tokenize import RegexpTokenizer
import porter_dictionary

port_dict = porter_dictionary.porter_dictionary()
file_dict = ('/home/zelalem/Downloads/hersheys_archives/dict/ps_2010_15_dictionary')

nltk_tokenizer = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
wnl = nltk.WordNetLemmatizer()
stop = stopwords.words('english')

fileList = glob.glob('/home/zelalem/Downloads/hersheys_archives/PS_2010_15/*.txt')

pos_dict = {'JJ': 'a', 'JJR': 'a',
            'JJS': 'a', 'NN': 'n',
            'NNS': 'n', 'NNP': 'n',
            'NNPS': 'n', 'PRP': 'n',
            'PRP$': 'n', 'RB': 'r',
            'RBR': 'r', 'RBS': 'r',
            'VB': 'v', 'VBD': 'v',
            'VBG': 'v', 'VBN': 'v',
            'VBZ': 'v', }

print('------pre-process started-------')

for files in fileList:
    tFile = open(files)
    line = tFile.read().lower().decode('utf-8')
    digit_free = re.sub(r"$\d+\W+|\b\d+\b|\W+\d+$", "", line)
    url_less_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', digit_free)
    tokens = nltk_tokenizer.tokenize(url_less_string)
    filtered_words = [w for w in tokens if not w in stopwords.words('english')]



    POS_Tokens = nltk.pos_tag(filtered_words)
    z = []
    for x in POS_Tokens:
        try:
            z.append(pos_dict[x[1]])
        except:
            z.append('n')

    wnl_tokens = []
    for i in range(len(filtered_words)):
        wnl_tokens.append(wnl.lemmatize(filtered_words[i], z[i]))
    por_tokens = [stem(t) for t in wnl_tokens]

    file_txt = open("/home/zelalem/Downloads/hersheys_archives/ps_2010_15_pre/"+path.PurePath(files).parts[6], "w")

    for i in por_tokens:
        if len(i)==1:
            pass
        else:
            file_txt.write(i.encode('utf-8'))
            file_txt.write('\n')
    file_txt.close()

    temp_term1 = ''
    term1 = ''

    for stmd in range(len(filtered_words)):
        term1 = por_tokens[stmd]
        temp_term1 = filtered_words[stmd]

        port_dict.add_element(stemmed=term1, nonstemmed=temp_term1)

port_dict.write_dict_to_file(file_dict)










