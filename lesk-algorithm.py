import nltk
import glob
import pathlib as path
import os

from nltk.tag.stanford import StanfordPOSTagger
path_to_tagger = '/home/zelalem/Downloads/stanford-postagger-2014-08-27/models/english-bidirectional-distsim.tagger'
stanford_postagger_jar = '/home/zelalem/Downloads/stanford-postagger-2014-08-27/stanford-postagger.jar'
st = StanfordPOSTagger(path_to_tagger, stanford_postagger_jar)

fileList = ('/home/zelalem/Downloads/hersheys_archives/popular-science-extracted/')
dirs = os.listdir(fileList)
try:
    for files in dirs:
        try:
            files=fileList+files
            # print(files)
            tFile = open(files)
            text = tFile.read()
            tFile.close()
            # files_split = files.split('/')
            # print files_split[5]

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

            file_txt = open("/home/zelalem/Downloads/hersheys_archives/popular-science-phrase/" + path.PurePath(files).parts[6], "w")

            for term in terms:

                # print(term.__len__())
                if (term.__len__())==1 or term.__len__()==0:
                    continue
                else:
                    # print(term)
                    for word in term:
                        file_txt.write(word )
                        file_txt.write(' ')

                        # print word,

                    # print(splitted)
                    file_txt.write('\n')

            file_txt.close()
        except:
            print 'error'+files
            continue

    # tFile.close()
except ValueError:
    print 'error'+files