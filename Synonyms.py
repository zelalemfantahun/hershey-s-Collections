__author__ = 'zelalem'

# from pywsd.lesk import simple_lesk
# sent = 'The wind swept up the leaves'
# sent1 = 'Wind the clock up before you go to bed.'
#
#
# ambiguous = 'wind'
# answer = simple_lesk(sent, ambiguous, pos='n')
# answer1 = simple_lesk(sent1, ambiguous, pos='n')
# print answer
# print answer1
# print '************'
# print answer.definition()
# print '============='
# print answer1.definition()
# print '-----------------'
#
#
# from nltk.corpus import wordnet as wn
# for ss in wn.synsets('wind'):
#     print(ss, ss.definition())
from nltk.corpus import wordnet

dog = wordnet.synset('dog.n.01')
print dog.lemma_names()
