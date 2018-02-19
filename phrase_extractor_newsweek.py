__author__ = 'zelalem'

import nltk
import pathlib as path
import os
import porter_dictionary
from nltk.util import ngrams
import glob
import time



port_dict = porter_dictionary.porter_dictionary()
file_dict = ('/home/zelalem/Downloads/hersheys_archives/dict/newsweek_porter_dictionary')


pos_dict = {'JJ': 'a', 'JJR': 'a',
            'JJS': 'a', 'NN': 'n',
            'NNS': 'n', 'NNP': 'n',
            'NNPS': 'n', 'PRP': 'n',
            'PRP$': 'n', 'RB': 'r',
            'RBR': 'r', 'RBS': 'r',
            'VB': 'v', 'VBD': 'v',
            'VBG': 'v', 'VBN': 'v',
            'VBZ': 'v', }

from nltk.tag.stanford import StanfordPOSTagger
path_to_tagger = '/home/zelalem/Downloads/stanford-postagger-2014-08-27/models/english-bidirectional-distsim.tagger'
stanford_postagger_jar = '/home/zelalem/Downloads/stanford-postagger-2014-08-27/stanford-postagger.jar'
st = StanfordPOSTagger(path_to_tagger, stanford_postagger_jar)

fileList = glob.glob('/home/zelalem/Downloads/hersheys_archives/newsweek_extracted/*.txt') # input file read
# fileList = glob.glob('/home/zelalem/Downloads/hersheys_archives/test2/*.txt')# input file read
error_path ='/home/zelalem/Downloads/hersheys_archives/newsweek_error/' # a folder Containing files with error
# error_path ='/home/zelalem/Downloads/hersheys_archives/snextracted_error_test/' # a folder Containing files with error
done_file = '/home/zelalem/Downloads/hersheys_archives/newsweek_done_phrase/'
# done_file = '/home/zelalem/Downloads/hersheys_archives/SN_done_test/'
# dirs = os.listdir(fileList)

def dict_creator(termz,temp_termz):
    temp_term1 = ''
    term1 = ''

    for ij in range(len(termz)):

        if(ij != 0):
            temp_term1 = temp_term1+' '+temp_termz[ij]
            term1 = term1+' '+termz[ij]

        else:
            temp_term1 = temp_termz[ij]
            term1 = termz[ij]

    port_dict.add_element(stemmed=term1,nonstemmed=temp_term1)


try:
    i1234 = 0
    I1234 = len(fileList)
    for files in fileList:
        # print files
        try:
            file1 = str(files).split('/')[6]
            print '888888888888888888888888',file1
            # print (900000000000000000000000)
            i1234 = i1234 + 1
            print  ('Processing file',i1234,'of', I1234)

            # print(files)
            tFile = open(files)
            text = tFile.read()
            tFile.close()

            # print (911111111111111111111111111)

        # Used when tokenizing words
            sentence_re = r'''(?x)      # set flag to allow verbose regexps
                  ([A-Z])(\.[A-Z])+\.?  # abbreviations, e.g. U.S.A.
                | \w+(-\w+)*            # words with optional internal hyphens
                | \$?\d+(\.\d+)?%?      # currency and percentages, e.g. $12.40, 82%
                | \.\.\.                # ellipsis
                | [][.,;"'?():-_`]      # these are separate tokens
            '''

            lemmatizer = nltk.WordNetLemmatizer()

            from stemming.porter2 import stem


            #Taken from Su Nam Kim Paper...
            grammar = r"""
                NBAR:
                    {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns

                NP:
                    {<NBAR>}
                    {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
            """
            chunker = nltk.RegexpParser(grammar)
            toks = nltk.regexp_tokenize(text, sentence_re)
            # print text
            # print (4545454545454545454545454545454545454)
            # print toks
            postoks = st.tag(toks)
            # print postoks
            tree = chunker.parse(postoks)
            from nltk.corpus import stopwords
            stopwords = stopwords.words('english')
            # print (9222222222222222222222222222)


            def leaves(tree):
                """Finds NP (nounphrase) leaf nodes of a chunk tree."""
                for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
                    yield subtree.leaves()

            def normalise(word):
                """Normalises words to lowercase and stems and lemmatizes it."""

                word = word.lower()
                # print word
                return word

            def acceptable_word(word):
                """Checks conditions for acceptable word: length, stopword."""
                accepted = bool(2 <= len(word) <= 40
                    and word.lower() not in stopwords)
                return accepted


            def get_terms(tree):
                for leaf in leaves(tree):
                    term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
                    yield term
            terms = get_terms(tree)


            file_txt = open("/home/zelalem/Downloads/hersheys_archives/newsweek_phrase/" + path.PurePath(files).parts[6], "w") # a folder containing output

            # print (93333333333333333333333333333, (terms),time.strftime("%c"))
            for term in terms:
                zterm = ''

                for q1 in term:
                    zterm = zterm +' '+ q1

                term = zterm.replace('-',' ').split()
                tagged = nltk.tag.pos_tag(term)
                # tagged = st.tag(term)
                # print tagged


                # print (94444444444444444444444444444444444444,term,time.strftime("%c"))
                z1 = []
                for xxx in tagged:
                    try:
                        z1.append(pos_dict[xxx[1]])
                        # print xxx[1]
                    except:
                        z1.append('n')
                # print (95555555555555555555555555555,time.strftime("%c"))
                temp_term = []

                for jj in term:
                    temp_term.append(jj)

                for k in range(len(term)):
                    term[k] = lemmatizer.lemmatize(term[k], z1[k])
                    term[k] = stem(term[k])
                # print (96666666666666666666666666666,term,time.strftime("%c"))

                if (term.__len__())==1 or term.__len__()==0:
                    continue
                else:
                    # print term
                    for i in range(len(term)):
                        # word = (str(term))
                        word = (str(term))
                        file_txt.write(term[i])
                        if i < len(term) -1:
                            file_txt.write(' ')
                    # file_txt.write(' ')
                    file_txt.write('\n')


                    if len(term) == 2:
                        dict_creator(term,temp_term)

                    if len(term) > 2:
                        six_grams = list(ngrams(term, 2))
                        six_grams_2 = list(ngrams(temp_term,2))
                        for i in range(len(six_grams)):
                            dict_creator(six_grams[i],six_grams_2[i])

            file_txt.close()
            os.rename(files,done_file+file1)
        except:
            print('error88888888888888888888888'+'-------------'+files)
            # print(file_rename)
            # print files
            os.rename(files,error_path+file1)
            # print(error_path+file_ori)
            continue
    port_dict.write_dict_to_file(file_dict)
    # tFile.close()
except:
    print ('error99999999999999999'+files)