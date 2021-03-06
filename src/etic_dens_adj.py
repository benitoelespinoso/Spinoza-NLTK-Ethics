import nltk
from scipy import stats
from numpy import array
import matplotlib.pyplot as plt
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
corpus_root = r'C:\Users\guille\Google Drive\NLTK\DEF\ficheros_in\Etica\proposiciones'
newcorpus = PlaintextCorpusReader(corpus_root, '.*')
tokens = nltk.word_tokenize(newcorpus.raw())
text = nltk.Text(tokens)


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


from nltk import word_tokenize
from nltk.tag import pos_tag
V = ['VB', 'VBZ', 'VBP', 'VBD', 'VBG']
N = ['NN', 'NNS', 'NNP', 'NNPS']
ADV = ['RB', 'RBR', 'RBS']
ADJ = ['JJ', 'JJR', 'JJS']
wLen = []       # number of words
vLen = []       # number of verbs
advLen = []     # number of adverbs
adjLen = []     # number of adjectives
vLen, nLen, advLen, adjLen, wLen = ([] for i in range(5))
for fileid in newcorpus.fileids():
 tokens = word_tokenize(newcorpus.raw(fileid))
 words = [t for t in tokens if t.isalpha()]
 taggedW = pos_tag(words)
 verbs, nouns, advs, adjs = ([] for i in range(4))
 for (w,tag) in taggedW:
     if tag in V: verbs.append(w)
     elif tag in N: nouns.append(w)
     elif tag in ADV: advs.append(w)
     elif tag in ADJ: adjs.append(w)
 wLen.append(len(words))
 vLen.append(len(verbs))
 nLen.append(len(nouns))
 advLen.append(len(advs))
 adjLen.append(len(adjs))
	

tagLists = [vLen, nLen, adjLen]
labels = ['Verb density', 'Noun density', 'Adj density']
# plt.figure(figsize=(5,5))
plt.figure(figsize=(8,8))

for (line, tag) in enumerate(tagLists):
 tempPair = zip(tag, wLen)
 u = list(tempPair)
 u.sort(key=lambda pair: pair[1])
 density = [t/float(w) for (t,w) in u]
 plt.plot(range(len(wLen)), density, label=labels[line])

plt.ylim([0, 0.35]) # make room for legend at top
plt.xticks(range(len(wLen)), sorted(wLen), rotation='vertical')
plt.xlabel('Words in text')
plt.ylabel('Density')
plt.legend(loc='best', fontsize='small')
plt.grid()
plt.tight_layout()
plt.show()
