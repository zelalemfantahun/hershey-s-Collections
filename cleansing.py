__author__ = 'zelalem'

# this block of code first reads a files directory

import glob
import nltk
from nltk.corpus import stopwords
import pathlib as path
from stemming.porter2 import stem
import string
import porter_dictionary



fileList = glob.glob('/home/zelalem/Downloads/hersheys_archives/test/*.txt')
pos_dict = {'JJ': 'a', 'JJR': 'a',
            'JJS': 'a', 'NN': 'n',
            'NNS': 'n', 'NNP': 'n',
            'NNPS': 'n', 'PRP': 'n',
            'PRP$': 'n', 'RB': 'r',
            'RBR': 'r', 'RBS': 'r',
            'VB': 'v', 'VBD': 'v',
            'VBG': 'v', 'VBN': 'v',
            'VBZ': 'v', }

wnl = nltk.WordNetLemmatizer()
stop = stopwords.words('english')

z = []
wnl_tokens = []


def is_float(x):
    try:
        float(x)
        return True
    except:
        return False


def has_token_punct(token):
    for char in token:
        if (char in string.punctuation):
            return True
            break
        else:
            pass


def find_punct(token):
    ch = []
    for char in token:
        if (char in string.punctuation):
            ch.append(char)

    return ch
    # break


def return_cleaned(t1):
    returned_token = []

    for i in t1:
        # print(i)
        if (len(i) <= 2):
            # print('-------',i)
            pass
        elif (i[:2] == '//'):
            # print('*******',i)
            pass
        elif (is_float(i)):
            pass
        # elif (i.__contains__(',')):
        # pass
        elif (i.__contains__('www.') or i.__contains__('xxx.') or i.__contains__('yyy.') or i.__contains__('.gov') ):
            pass
        elif (str(i).endswith('.com') or str(i).endswith('.html') or str(i).endswith('.php') or str(i).endswith(
                '.aspx') or str(i).endswith('.asp') or str(i).endswith('htm') or str(i).endswith('pdf')):
            pass
        elif (str(i).startswith('http') or str(i).startswith('https') or str(i).startswith('/') ):
            pass
        else:
            returned_token.append(i)

    # print returned_token
    #removes punctuation from a string
    token_list = []
    for token in returned_token:
        if ((has_token_punct(token))):
            chr = find_punct(token)
            new_token=token
            for ch in chr:
                new_token = str(new_token).replace(ch, ''
                                                       '')

            # print new_token
            # checks if after removal of  punctuation the remaining string is number only and its length is <2
            if (is_float(new_token) ):
                pass
            else:
                token_list.append(new_token)
        else:
          token_list.append(token)


    # print  token_list
    return token_list
# print  returned_token
# return returned_token


print('------pre-process started-------')
for files in fileList:
    tFile = open(files)
    line = tFile.read().lower()
    tokens = nltk.word_tokenize(line)
    # print tokens
    tokens = return_cleaned(tokens)
    # print tokens

    # tokens = Pun_pattern.sub("", str(tokens))
    # tokenstemp = []
    # for t1 in tokens:
    # for tt1 in t1:
    #         if(not string.punctuation.__contains__(tt1)):
    #             if(t1 != "'s"):
    #                 tokenstemp.append(t1)
    #             break

    # tokens = tokenstemp
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

    for i in range(len(filtered_words)):
        print (filtered_words[i],por_tokens[i])
    # file_txt = open("/home/zelalem/Downloads/hersheys_archives/popular-preprocessed/"+path.PurePath(files).parts[6], "w")
#     file_txt = open("/" + path.PurePath(files).parts[6], "w")
#     # print '***********', path.PurePath(files).parts[6]
#     for i in por_tokens:
#         file_txt.write(i)
#         file_txt.write('\n')
#     file_txt.close()
# print('***------pre-process finished--------')
#

