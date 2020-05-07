# import's
#
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from nltk.collocations import *
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from operator import itemgetter
from nltk import FreqDist
WNL = nltk.WordNetLemmatizer()

# Leer el texto
#
f = open('C:\\Users\\guille\\Google Drive\\NLTK\\DEF\\ficheros_in\\Etica\\et_en.txt', encoding="utf8")
raw = f.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
words = [w.lower() for w in tokens]

# STOP WORDS (etica)
#
def prepareStopWords():
 stopwordsList = []
 stopwordsList = stopwords.words('english')
 stopwordsList.append('dont')
 stopwordsList.append('didnt')
 stopwordsList.append('doesnt')
 stopwordsList.append('cant')
 stopwordsList.append('couldnt')
 stopwordsList.append('couldve')
 stopwordsList.append('im')
 stopwordsList.append('ive')
 stopwordsList.append('isnt')
 stopwordsList.append('theres')
 stopwordsList.append('wasnt')
 stopwordsList.append('wouldnt')
 stopwordsList.append('a')
 stopwordsList.append('also')
 stopwordsList.append('prop')
 stopwordsList.append('Prop')
 stopwordsList.append('Prop_vii')
 stopwordsList.append('Prop_xvi')
 stopwordsList.append('i')
 stopwordsList.append('ii')
 stopwordsList.append('iii')
 stopwordsList.append('I')
 stopwordsList.append('II')
 stopwordsList.append('III')
 stopwordsList.append('PROP')
 stopwordsList.append('.')
 stopwordsList.append(',')
 stopwordsList.append('Proof')
 stopwordsList.append('Proof.—')
 stopwordsList.append('.—')
 stopwordsList.append('prop')
 stopwordsList.append('DEFINITIONS')
 stopwordsList.append('AXIOMS')
 stopwordsList.append('PROPOSITION')
 stopwordsList.append('far')
				   
 return stopwordsList

stopwords = prepareStopWords()

# FreqDist
#		
fdist = FreqDist(text)
fdist_no_punc_no_stopwords = nltk.FreqDist(dict((word, freq) for word, freq in fdist.items() if word not in stopwords and word.isalpha()))

# diagrama_1
#
fdist_no_punc_no_stopwords.plot(20, cumulative=True, title="20 most common tokens (no stopwords or punctuation)")


# diagrama_2
#
fdist_no_punc_no_stopwords.plot(20, cumulative=False, title="20 most common tokens (no stopwords or punctuation)")


# diagrama_2_2
#
x, y = zip(*fdist_no_punc_no_stopwords.most_common(n=20))
plt.bar(range(len(x)), y)
plt.xticks(range(len(x)), x)
plt.show()


# WordCLoud
wc = WordCloud().generate(' '.join(words))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.title('WC de Etica_Spinoza')
plt.show()



fd = fdist_no_punc_no_stopwords;


# las mas comunes
fd.most_common(50)

# diagramas_dispersion
text.dispersion_plot(["God","mind","knowledge"])
text.dispersion_plot(["power","reason","nature"])
# text.concordance("god")


# bigramas
# from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
 words)
finder.nbest(bigram_measures.pmi, 10)
finder.apply_freq_filter(3)
finder.nbest(bigram_measures.pmi, 10)

# lo que aqui cambia es el cambio de filtro


# WC para los bigramas mas frecuentes
stopWords = stopwords
text_content = [''.join(re.split("[ .,;:!?‘’``''@#$%^_&*()<>{}~\n\t\\\-]", word)) for word in text]

text_content = [word for word in text_content if word not in stopWords]
text_content = [s for s in text_content if len(s) != 0]
text_content = [WNL.lemmatize(t) for t in text_content]
finder = BigramCollocationFinder.from_words(text_content)
bigram_measures = BigramAssocMeasures()
scored = finder.score_ngrams(bigram_measures.raw_freq)
scoredList = sorted(scored, key=itemgetter(1), reverse=True)
word_dict = {}
listLen = len(scoredList)

for i in range(listLen):
 word_dict['_'.join(scoredList[i][0])] = scoredList[i][1]

WC_height = 500
WC_width = 1000
WC_max_words = 100
wordCloud = WordCloud(max_words=WC_max_words, height=WC_height, width=WC_width)
wordCloud.generate_from_frequencies(word_dict)
plt.title('Most frequently occurring bigrams connected with an underscore_')
plt.imshow(wordCloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# with open('Bigrams_frequent_words.csv', 'w') as f:
#  [f.write('{0},{1}\n'.format(key, value)) for key, value in word_dict.items()]
#  f.close()


# WC de los bigramas menos frecuentes, salvar fichero
scoredList = sorted(scored, key=itemgetter(1))
scoredListLen = len(scoredList)-1
maxLenCnt = 0
MINSCORE = 0.000265

indx = 0
while (indx < scoredListLen) and (scoredList[indx][1] < MINSCORE):
 indx += 1

word_dict2 = {}
while (indx < scoredListLen) and (maxLenCnt < WC_max_words):
 word_dict2['_'.join(scoredList[indx][0])] = scoredList[indx][1]
 indx +=  1
 maxLenCnt += 1

if len(word_dict2) > 0:
 wordCloud.generate_from_frequencies(word_dict2)
 plt.title('Least frequently occurring bigrams connected with an underscore_')
 plt.imshow(wordCloud, interpolation='bilinear')
 plt.axis("off")
 plt.show()
 # wordCloud.to_file("WordCloud_Bigrams_Infrequent_words.png")
else:
 print("\nThere were no words to display in the word cloud.")


 
 
 
# CORPUS
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\Users\guille\Google Drive\NLTK\DEF\ficheros_in\Etica\entera_separada'

newcorpus = PlaintextCorpusReader(corpus_root, '.*')
tokens = nltk.word_tokenize(newcorpus.raw())
words = newcorpus.words()
words = [word.lower() for word in words]


cfd = nltk.ConditionalFreqDist(
 (target, fileid[:])
 for fileid in newcorpus.fileids()
 for w in newcorpus.words(fileid)
 for target in ['mind', 'god']
 if w.lower().startswith(target))
cfd.plot()

cfd = nltk.ConditionalFreqDist(
 (target, fileid[:])
 for fileid in newcorpus.fileids()
 for w in newcorpus.words(fileid)
 for target in ['reason', 'cause']
 if w.lower().startswith(target))
cfd.plot()


cfd = nltk.ConditionalFreqDist(
 (target, fileid[:])
 for fileid in newcorpus.fileids()
 for w in newcorpus.words(fileid)
 for target in ['emotions', 'love','body']
 if w.lower().startswith(target))
cfd.plot()


# modals = 'can, could, may, might, must, will'.split(', ')
# cfd = nltk.ConditionalFreqDist(
#  (target, fileid[:])
#  for fileid in newcorpus.fileids()
#  for w in newcorpus.words(fileid)
#  for target in modals
#  if w.lower().startswith(target))
# cfd.plot()



