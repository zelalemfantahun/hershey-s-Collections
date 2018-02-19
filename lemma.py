__author__ = 'zelalem'
import nltk
lemmatizer = nltk.WordNetLemmatizer()
word = 'The fishermen even went further for fishing.'
# word = word.split()
word = lemmatizer.lemmatize(word)
print word
