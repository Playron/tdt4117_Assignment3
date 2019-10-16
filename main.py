from helpers import *
import gensim
import string


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

stopwords = 'a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your'

stopwordlist = stopwords.split(',')

dict = gensim.corpora.Dictionary(liste)

ids = stopword_id(dict, stopwordlist)

dict.filter_tokens(ids)

def convert_bow(paragraf):
    bow = []
    for p in paragraf:
        bow.append(dict.doc2bow(p))
    return bow

bow = convert_bow(liste)


# Task 3.1, 3.2, 3.3
# the TF-IDF model based on BoW
tfidf_model = gensim.models.TfidfModel(bow)

# the BoW on the following format for each word: (index, weight)
tfidf_corpus = tfidf_model[bow]

# matrix similarity of the corpus
matrix_sim = gensim.similarities.MatrixSimilarity(tfidf_corpus)

# Task 3.4
# this will group documents and words, based on their tf-idf-weight, together into topics (serializing)
lsi_model = gensim.models.LsiModel(tfidf_corpus, id2word=dict, num_topics=100)
lsi_corpus = lsi_model[bow]
lsi_matrix = gensim.similarities.MatrixSimilarity(lsi_corpus)

# Task 3.5
# printing the first three topics
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














