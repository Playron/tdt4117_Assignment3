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


def stopwords_file_fixer():
    stopwords = open_file("/Users/perhaagensen/Documents/Høst2019/InfoGjen Øvinger/tdt4117Oving3/common-english-words.txt")
    file = stopwords.read()
    stopwordlist = file.split(',')
    return stopwordlist

def stopword_id(dict, stopwordlist):
    ids = []
    for word in stopwordlist:
        try:
            ids.append(dict.token2id[word])
        except:
            pass
    return ids

stopwordlist = stopwords_file_fixer()

print(stopword_id(dict, stopwordlist))

print(dict.token2id['a'])









