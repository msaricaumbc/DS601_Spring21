#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pickle
import re
# import pandas as pd

import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# import boto3
import os


# In[12]:


# import sklearn
# sklearn.__version__


# In[4]:



# def get_model_file(filename):
#     s3 = boto3.resource('s3')
#     with open(filename, 'wb') as data:
#         s3.Bucket("com.msarica.ds").download_fileobj(filename, data)

def load_model_file(filename):
    obj = pickle.load(open(filename, 'rb'))
    return obj


# In[5]:


filename = 'model.pickle'

# if os.path.exists(filename) == False:
#     print('model not found')
#     get_model_file(filename)
#     print('model downloaded from s3')
# else:
#     print('model file found!')


# In[6]:


obj = load_model_file(filename)

model = obj['model']
stopwords = obj['stopwords']
lemmatizer = obj ['lemmatizer']
wordnet_map = obj ['wordnet_map']
vectorizer = obj ['vectorizer']


# In[7]:


#prediction pipeline with text vectorizer and model
def prediction(text_input, STOPWORDS, lemmatizer, wordnet_map, vectorizer, Multinomial_NB):
    
    # Transform words to lower case
    text=text_input.lower()
    # Remove punctuation
    text=re.sub('[^a-zA-Z]', ' ', text)
    # Remove tags
    text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
    # Remove special characters and digits
    text=re.sub("(\\d|\\W)+"," ",text)
    # Remove stop words like : and is a and the
    text=" ".join([word for word in text.split() if word not in STOPWORDS])
    # Find base word for all words in the sentence
    pos_tagged_text=nltk.pos_tag(text.split())
    text=" ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])
    
    # specific
    text = re.sub(r"won\'t", "will not", text); text = re.sub(r"can\'t", "can not", text)
    # general
    text = re.sub(r"n\'t", " not", text); text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text); text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text); text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text); text = re.sub(r"\'m", " am", text)
#     print(text)
    text = np.array(text).reshape(1,)
    vec_text = vectorizer.transform(text)
    output = Multinomial_NB.predict(vec_text)
    
    cols = ['emotion_0','emotion_1','emotion_2','emotion_3','emotion_4',
            'emotion_5','emotion_6','emotion_7','emotion_8']
    output_values = [False if x == 0 else True for x in output[0]]  # np values are replaced with boolean
 
    return { key: value for key, value in zip(cols, output_values)}


# In[11]:


#Source[BBC]: https://www.bbc.com/news/world-asia-56546920
text_input= "Myanmar coup: Dozens killed as army opens fire on protesters during deadliest day.Security forces were out in strength trying to prevent rallies.Local news site Myanmar Now put the death toll at 114, while the United Nations said it was receiving reports of scores killed and hundreds more injured."

#Prediction output
output= prediction(text_input, stopwords, lemmatizer, wordnet_map, vectorizer, model)
output


# In[9]:


def make_prediction(sentence):
    return prediction(sentence, stopwords, lemmatizer, wordnet_map, vectorizer, model)


# In[10]:

from flask import Flask
from flask import jsonify, request
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
CORS(app)

@app.route('/')
def start():
    sentence = request.args.get('sentence')

    if sentence == None: 
        return jsonify({})

    # print(sentence)
    
    result = make_prediction(sentence)
    
    # print(result)
    return jsonify(result)

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=80)



