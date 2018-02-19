__author__ = 'zelalem'
import nltk
from nltk.tag.stanford import StanfordPOSTagger
path_to_tagger = '/home/zelalem/Downloads/stanford-postagger-2014-08-27/models/english-bidirectional-distsim.tagger'
stanford_postagger_jar = '/home/zelalem/Downloads/stanford-postagger-2014-08-27/stanford-postagger.jar'
st = StanfordPOSTagger(path_to_tagger, stanford_postagger_jar)
toks = 'For some time, psychologist Carl Thoresen and his co-workers at Stanford University have noticed that patients recovering from heart attacks who fit the competitive, hostile, achivement-oriented pattern of "Type A" behavior are unable to remember ever having not fit into a hard-driving mold.'
toks = toks.split()
postoks = st.tag(toks)
print postoks