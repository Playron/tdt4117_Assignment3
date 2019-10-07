import random
import codecs
import gensim
import nltk
import copy

file = "/Users/perhaagensen/PycharmProjects/tdt4117Oving3/pg3300.txt"
file2 = "/Users/perhaagensen/PycharmProjects/tdt4117Oving3/pg3300_2.txt"

random.seed(123)

#Task 1.1
#This function returns the opened file. File is set to read only
def openFile(file):
    return codecs.open(file, "r", "utf-8")

#Task 1.2
#This function splits up the text file in to paragraphs, and adds the, to an array.
def paragraph(file):
    fil = openFile(file)
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
def wordRemover(word):
    paragrafListe = []
    for p in paragraph(file):
        if word.casefold() not in p.casefold():
            paragrafListe.append(p)
    return paragrafListe

def tokenize(paragraf):
    for i, p in enumerate(paragraf):
        paragraf[i] = p.split(" ")
    return paragraf




paragraph(file)

wordRemover("Gutenberg")

print(tokenize(wordRemover("Gutenberg")))






