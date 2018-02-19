__author__ = 'zelalem'

__author__ = 'zelalem'

# this block of code first reads a files directory

import re
import glob
import nltk
from nltk.corpus import stopwords
import pathlib as path
from stemming.porter2 import stem
import string




fileList = glob.glob('/home/zelalem/Desktop/*.txt')

pos_dict = {'JJ': 'a', 'JJR': 'a',
        'JJS': 'a', 'NN':'n',
        'NNS': 'n', 'NNP': 'n',
        'NNPS': 'n', 'PRP': 'n',
        'PRP$': 'n', 'RB': 'r',
        'RBR': 'r', 'RBS': 'r',
        'VB': 'v', 'VBD': 'v',
        'VBG': 'v', 'VBN': 'v',
        'VBZ': 'v', }


# porter = nltk.PorterStemmer()
# porter = nltk.PorterStemmer()
wnl = nltk.WordNetLemmatizer()
stop = stopwords.words('english')
# Pun_pattern = re.compile(r'([^A-Za-z0-9])')
z = []
wnl_tokens = []


def is_float(x):

    try:
        float(x)
        return True
    except:
        return False

def return_cleaned(t1):
    returned_token = []

    for i in t1:
        print(i)
        if (len(i)<=2):
            print('-------',i)
            pass
        elif (i[:2] == '//'):
            print('*******',i)
            # t1.remove(i)
            pass
        elif (is_float(i)):
            print('///////',i)
            # t1.remove(i)
            pass
        else:
            pass

            returned_token.append(i)

    print('!!!!!!!!!!!!!!!!!!!!!')
    print returned_token
    return returned_token





print('------pre-process started-------')
for files in fileList:
    tFile = open(files)
    line = tFile.read().lower()
    tokens = nltk.word_tokenize(line)

    print('Tokens being printed')
    print(tokens)
    tokens = return_cleaned(tokens)
    # tokens = Pun_pattern.sub("", str(tokens))
    tokenstemp = []
    for t1 in tokens:
        for tt1 in t1:
            if(not string.punctuation.__contains__(tt1)):
                if(t1 != "'s"):
                    tokenstemp.append(t1)
                break

    tokens = tokenstemp




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
        wnl_tokens.append(wnl.lemmatize(filtered_words[i],z[i]))

    por_tokens = [stem(t) for t in wnl_tokens]

    file_txt = open("/home/zelalem/Desktop/preprocessed.txt", "w")
    # print '***********', path.PurePath(files).parts[6]
    for i in por_tokens:
        file_txt.write(i)
        file_txt.write('\n')
    file_txt.close()
print('------pre-process finished--------')





