import gzip
import gensim 
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

data_file='reviews_data.txt.gz'
'''
with gzip.open ('reviews_data.txt.gz', 'rb') as f:
    for i,line in enumerate (f):
        print(line)
        break
'''
def read_input(input_file):
    
    logging.info("reading file {0}...this may take a while".format(input_file))
    
    with gzip.open (input_file, 'rb') as f:
        for i, line in enumerate (f): 

            if (i%10000==0):
                logging.info ("read {0} reviews".format (i))
            yield gensim.utils.simple_preprocess (line) # tokenization, lowercasing

documents = list (read_input (data_file))
logging.info ("Done reading data file")

'''
WORD2VEC algo
Behind the scenes we are actually training a simple neural network with a single hidden layer.
But, we are actually not going to use the neural network after training.
Instead, the goal is to learn the weights of the hidden layer.
These weights are essentially the word vectors that we’re trying to learn.
'''

model = gensim.models.Word2Vec (documents, size=150, window=10, min_count=2, workers=10)
#size: the size of the dense vector
#window: the maximum width of related neighboring words to the left and the right
#min_count: Minimium frequency count of words
#workers: threads behind the scenes
model.train(documents,total_examples=len(documents),epochs=10)

w1 = 'funny'
model.wv.most_similar (positive=w1,topn=6)

w1 = ["bed",'sheet','pillow']
w2 = ['couch']
model.wv.most_similar (positive=w1,negative=w2,topn=10)

model.wv.similarity(w1="dirty",w2="smelly") #cosine similarity

model.wv.doesnt_match(["cat","dog","france"])

model.save('review.model.bin')
model.wv.save_word2vec_format('review.model.txt', binary=False)

from gensim.models import KeyedVectors
model2 = KeyedVectors.load('review.model.bin')