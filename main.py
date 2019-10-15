from helpers import *
import gensim


file = "/Users/perhaagensen/PycharmProjects/tdt4117Oving3/pg3300.txt"

stemmer = PorterStemmer()
freqDist = FreqDist()
random.seed(123)

#Task 1 - Create modified list

liste = paragraph(file)

paragraf = paragraph(file)

liste = word_remover("Gutenberg")

liste = tokener(liste)

liste = lower_case(liste)

liste = remove_punc(liste)

liste = stem(liste)

#Task 2

dict = gensim.corpora.Dictionary(liste)








