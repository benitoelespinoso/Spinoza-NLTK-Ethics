import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
corpus_root = r'C:\Users\guille\Google Drive\NLTK\DEF\ficheros_in\Etica\entera_separada'
from nltk import FreqDist
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



fdist = FreqDist(text)
fdist_no_punc_no_stopwords = nltk.FreqDist(dict((word, freq) for word, freq in fdist.items() if word not in stopwords and word.isalpha()))

# términos sinónimos o similares
print("***************** Similar: God **********************************")
text.similar("God")

print("***************************************************")
print("***************** Similar: nature **********************************")
text.similar("nature")

print("******************contextos comunes para God:mind *********************************")
# conextos comunes
text.common_contexts(["God","mind"])
print("***************************************************")
print("******************contextos comunes para love:ambition *********************************")
text.common_contexts(["love","ambition"])

print("***************************************************")
print("***************** Similar: power **********************************")
text.similar("power")
print("***************************************************")
print("***************** Similar: reason **********************************")
text.similar("reason")
print("***************** Similar: cause **********************************")
print("***************************************************")
text.similar("cause")

# comparativa de las apariciones de diversos términos. Se hace con proposición y con sus 3 primeros similares

# cfd = nltk.ConditionalFreqDist(
#  (target, fileid[:])
#  for fileid in newcorpus.fileids()
#  for w in newcorpus.words(fileid)
#  for target in ['proposición', 'lógica']
#  if w.lower().startswith(target))
# cfd.plot()	
# 
# # idem para lenguaje y mundo. 
# 
# cfd = nltk.ConditionalFreqDist(
#  (target, fileid[:])
#  for fileid in newcorpus.fileids()
#  for w in newcorpus.words(fileid)
#  for target in ['mundo', 'lenguaje']
#  if w.lower().startswith(target))
# cfd.plot()
