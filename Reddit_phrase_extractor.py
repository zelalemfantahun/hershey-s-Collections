
import nltk
import pathlib as path
import os
import porter_dictionary
from nltk.util import ngrams

port_dict = porter_dictionary.porter_dictionary()
file_dict = ('/home/zelalem/Downloads/hersheys_archives/dict/reddit_porter_full_2008_dictionary')
try:
    port_dict.load_dict(file_dict)
except:
    print ("previous Dict not found")

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


done_file = '/home/zelalem/Downloads/hersheys_archives/reddit_done/'
fileList = '/home/zelalem/Downloads/hersheys_archives/reddit_test/'
dirs = os.listdir(fileList)

file_len = 0
file_length = len(dirs)

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

for files in dirs:
    file_rename=fileList+files
    file_move = done_file+files
    file_ori=files
    files=fileList+files
    file_len = file_len + 1
    print  ('Processing file',file_len,'of', file_length)

    tFile = open(files)
    text = tFile.read().decode('utf-8')
    tFile.close()

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

    # postoks = st.tag(toks)
    postoks = nltk.pos_tag(toks)
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


    file_txt = open("/home/zelalem/Downloads/hersheys_archives/reddit_out/" + path.PurePath(files).parts[6], "w")

    for term in terms:
        zterm = ''

        for q1 in term:
            zterm = zterm +' '+ q1
        term = zterm.replace('-',' ').split()
        tagged = nltk.tag.pos_tag(term)
        # print tagged

        z1 = []
        for xxx in tagged:
            try:
                z1.append(pos_dict[xxx[1]])
            except:
                z1.append('n')


        temp_term = []

        for jj in term:
            temp_term.append(jj)

        for k in range(len(term)):
            term[k] = lemmatizer.lemmatize(term[k], z1[k])
            term[k] = stem(term[k])
        if (term.__len__())==1 or term.__len__()==0:
            continue
        else:
            for i in range(len(term)):
                try:

                    word = (str(term))
                    file_txt.write(term[i].encode('utf-8'))
                except:
                    continue
                if i < len(term) -1:
                    file_txt.write(' ')
            file_txt.write('\n')

            if len(term) == 2:
                dict_creator(term,temp_term)
            if len(term) > 2:
                six_grams = list(ngrams(term, 2))
                six_grams_2 = list(ngrams(temp_term,2))
                for i in range(len(six_grams)):
                    # print '****************',six_grams[i],six_grams_2[i]
                    dict_creator(six_grams[i],six_grams_2[i])
    port_dict.write_dict_to_file(file_dict)
    os.rename(file_rename,file_move)

# port_dict.write_dict_to_file(file_dict)
file_txt.close()
#

