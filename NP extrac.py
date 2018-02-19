__author__ = 'zelalem'

import nltk
import glob
import pathlib as path
import os

from nltk.tag.stanford import StanfordPOSTagger
path_to_tagger = '/home/zelalem/Downloads/stanford-postagger-2014-08-27/models/english-bidirectional-distsim.tagger'
stanford_postagger_jar = '/home/zelalem/Downloads/stanford-postagger-2014-08-27/stanford-postagger.jar'
st = StanfordPOSTagger(path_to_tagger, stanford_postagger_jar)

fileList = ('/home/zelalem/Downloads/hersheys_archives/reddit_test/') # input file read
error_path ='/home/zelalem/Downloads/hersheys_archives/reddit_error/' # a folder Containing files with error
dirs = os.listdir(fileList)
try:
    for files in dirs:
        try:
            file_rename=fileList+ files
            file_ori=files
            files=fileList+files
            # print(files)
            tFile = open(files)
            text = tFile.read().encode('utf-8')
            tFile.close()
            
        # Used when tokenizing words
            sentence_re = r'''(?x)      # set flag to allow verbose regexps
                  ([A-Z])(\.[A-Z])+\.?  # abbreviations, e.g. U.S.A.
                | \w+(-\w+)*            # words with optional internal hyphens
                | \$?\d+(\.\d+)?%?      # currency and percentages, e.g. $12.40, 82%
                | \.\.\.                # ellipsis
                | [][.,;"'?():-_`]      # these are separate tokens
            '''

            lemmatizer = nltk.WordNetLemmatizer()
            stemmer = nltk.stem.porter.PorterStemmer()

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
            # print type(toks)
            # print len(toks)
            # postoks = nltk.tag.pos_tag(toks)
            postoks = st.tag(toks)
            # print postoks

            # print postoks

            tree = chunker.parse(postoks)

            from nltk.corpus import stopwords
            stopwords = stopwords.words('english')


            def leaves(tree):
                """Finds NP (nounphrase) leaf nodes of a chunk tree."""
                for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
                    yield subtree.leaves()

            def normalise(word):
                """Normalises words to lowercase and stems and lemmatizes it."""
                word = word.lower()

                # word = stemmer.stem_word(word)
                word = lemmatizer.lemmatize(word)

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

            # print(path.PurePath(files).parts[5])

            file_txt = open("/home/zelalem/Downloads/hersheys_archives/reddit_out/" + path.PurePath(files).parts[6], "w") # a folder containing output

                          # print(term)
            str_word=''
            for word in terms:
                x=word.__len__()
                if x==0:
                    continue
                else:
                    counter=0;
                    while counter< x:
                        str_word=str_word + ' ' + word[counter]
                        counter+=1
                    file_txt.write(str_word)
                    file_txt.write(' ')
                    file_txt.write('\n')
                    str_word=''

            file_txt.close()
        except ValueError:
            print('error'+'-------------'+files)
            # print(file_rename)
            # print files
            os.rename(file_rename,error_path+file_ori)
            print(error_path+file_ori)
            continue

    # tFile.close()
except ValueError:
    print ('error'+files)