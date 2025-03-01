from helpers import *
import gensim
import string

#FILE I AM USING
file = "/Users/perhaagensen/PycharmProjects/tdt4117Oving3/pg3300.txt"

stemmer = PorterStemmer()
freqDist = FreqDist()
random.seed(123)

#Task 1 - Create modified list
#In this task i create a variable liste, and keeps modififying this list with
#the functions declered in the helper.py file.

liste = paragraph(file)

paragraf = paragraph(file)

liste = word_remover("Gutenberg")

liste = tokener(liste)

liste = lower_case(liste)

liste = remove_punc(liste)


#last step of modifying original file. Stem functions only keeps the stem of the words.
liste = stem(liste)

#Task 2
#I start to create a string with the stopwords, separated with comma, and then splits all the element by the comma, and adds it
#to the list stopwordlist. Then I use the gensim framework to create a proper dictionary, and then removes the stopwords
#as well as creating a bow, and add a system of word ids, and occurences.

stopwords = 'a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your'

stopwordlist = stopwords.split(',')

dict = gensim.corpora.Dictionary(liste)

ids = stopword_id(dict, stopwordlist)

dict.filter_tokens(ids)


#This method returns the bow described over.
def convert_bow(paragraf):
    bow = []
    for p in paragraf:
        bow.append(dict.doc2bow(p))
    return bow

bow = convert_bow(liste)


# Task 3.1, 3.2, 3.3
# TF-IDF model based on the bow
tfidf_model = gensim.models.TfidfModel(bow)

# the BoW formated on all words like this (index, weight)
tfidf_corpus = tfidf_model[bow]

# matrix similarity of the corpus
matrix_sim = gensim.similarities.MatrixSimilarity(tfidf_corpus)

# Task 3.4
# this will group documents and words, based on their tf-idf-weight, together into topics (serializing)
lsi_model = gensim.models.LsiModel(tfidf_corpus, id2word=dict, num_topics=100)
lsi_corpus = lsi_model[bow]
lsi_matrix = gensim.similarities.MatrixSimilarity(lsi_corpus)

# Task 3.5
# Printing the first three topics
topic1 = lsi_model.show_topic(1)
topic2 = lsi_model.show_topic(2)
topic3 = lsi_model.show_topic(3)
print("\n\nTOPICS: ", "\n")
print(topic1)
print(topic2)
print(topic3, "\n")

print("The three topics are related in the way that they are structured such that\n"
      "each cluster of docs and similar words in the occurence matrix represents the topics."
      "\nEach topic includes the most important words in defining the topic in the output, "
      "\nalong with their contribution to the topic.\n")



#Task 4

#4.1
#preprocessing function does all the same that we did to the txt file in task 1
#just making the query simplier.

def preprocessing(query):
    query = query.split()
    stemmed_query = []
    for word in query:
        stemmed_query.append(stemmer.stem(word.lower().strip(string.punctuation + '\n\r\t')))
    return stemmed_query

def preprocessing_(q):
    list = q.split()
    for i in range(len(list)):
        list[i] = stemmer.stem(list[i].strip(string.punctuation).lower())
    return list

query = preprocessing("What is the function of money?")
query = dict.doc2bow(query)
print(query)

#4.2
tfidf_query = tfidf_model[query]
tfidf_index = gensim.similarities.MatrixSimilarity(tfidf_corpus)

# This function prints out the word with highest score weights based on the query
def print_weights(tfidf_query):
    for weight_tuple in tfidf_query:
        print(dict.get(weight_tuple[0]), ":", weight_tuple[1])


print_weights(tfidf_query)













