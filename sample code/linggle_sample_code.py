from linggle_api_new import Linggle
linggle = Linggle()

def ngram(query):
	ngrams = linggle[query]
	print (ngrams)

following_words={}
words=['happy', 'exciting', 'entertaining', 'elated']

for word in words:
	following_words[word]=[]
	phrases=linggle[word+' n.']
	for phrase in phrases[:10]:
		following_words[word].append(phrase[0].replace(word+' ',''))
print(following_words)