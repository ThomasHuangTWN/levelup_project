import spacy
from spacy import displacy

nlp=spacy.load('en_core_web_sm')
doc=nlp('I bought an airplane that costs $1 million dollars.')

for token in doc:
	print(token.text,#the word
	token.lemma_,#the basic form
	token.pos_,#part of speech (morphology)
	token.tag_,#detailed part of speech (morphology)
	token.dep_,#relation between tokens
	token.shape_,#Xx. capitalize...
	token.is_alpha,#alpha character
	token.is_stop)#common words
	
displacy.serve(doc, style='dep')

for ent in doc.ents:
	print(token.text,
	token.start_char,
	token.end_char,
	ent.label)#the type of object (entity)

displacy.serve(doc, style='ent')