import random
import string
import codecs
import gensim
from nltk.stem.porter import PorterStemmer
from nltk.probability import FreqDist

file = "/Users/perhaagensen/PycharmProjects/tdt4117Oving3/pg3300.txt"

stemmer = PorterStemmer()
freqDist = FreqDist()
random.seed(123)

#Task 1.1
#This function returns the opened file. File is set to read only.
#Have to find an another way to modify the file's content.


def open_file(file):
    return codecs.open(file, "r", "utf-8")

#Task 1.2
#The method paragrapgh(), splits up the given books up to paragraphs. This functions
#checks if a line is full of spaces, and adds everything before these lines into
#paragrapgs


def paragraph(file):
    fil = open_file(file)
    paragrafer = []
    paragraf = ""
    for line in fil.readlines():
        paragraf += line
        if line.isspace():
            if line != "":
                paragrafer.append(paragraf)
            paragraf = ""
            continue
    return paragrafer

#Task 1.3
#This function takes in a word, and returns an updated list  where the word
#is filtered out.


def word_remover(word):
    paragrafListe = []
    for p in paragraph(file):
        if word.casefold() not in p.casefold():
            paragrafListe.append(p)
    return paragrafListe


#Task 1.4


def tokener(paragraf):
    for i, avsnitt in enumerate(paragraf):
        paragraf[i] = avsnitt.split(" ")
    return paragraf


#Task 1.5


def lower_case(paragraf):
    paragrafer = []
    for avsnitt in paragraf:
        ord_lower = []
        for ord in avsnitt:
            ord_lower.append(ord.lower())
        paragrafer.append(ord_lower)
    return paragrafer


punc = list(string.punctuation)
punc.append('\r\n')
def remove_punc(paragraf):
    paras = []
    #goes through each word in the paragraph and removes whitespace, etc.
    for p in paragraf:
        words = []
        for word in p:
            temp = replace_multiple(word, punc, ' ')
            templist = temp.split(' ')
            for i in templist:
                if i == '':
                    continue
                else:
                    words.append(i)
        paras.append(words)
    return paras

def replace_multiple(word, toBeRemoved, res):
    for elem in toBeRemoved:
        if elem in word:
            word = word.replace(elem, res)
    return word


#Task 1.6


def stem(paragraphs):
    stemmed_paragraphs = []
    #for each paragraph, stem each word in the paragraph
    for p in paragraphs:
        stemmed_words = []
        for word in p:
            stemmed_words.append(stemmer.stem(word))
        stemmed_paragraphs.append(stemmed_words)
    return stemmed_paragraphs


#Task 1.7


def word_frequency(paragraphs, word):
    for p in paragraphs:
        for w in p:
            if w == word:
                freqDist[w] += 1
    return freqDist


#Task 2



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













