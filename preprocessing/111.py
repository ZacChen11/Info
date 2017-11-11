'''
Created on Nov 5, 2017

@author: Zac
'''
import _pickle as cPickle
import Tokenization
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from _overlapped import NULL
if __name__ == '__main__':
    f = open('dic\\keys.txt', 'rb')
    k = cPickle.load(f)
    f.close()
    print(k)
    f = open('dic\\dictionary.txt', 'rb')
    d = cPickle.load(f)
    f.close()
    
    print(len(d['concess']))
    print(len(d['obstruct']))
    
    a = []
    a = a + [[1,2],[2,1],[3,7],[4,5],[1,9],[2,1]]
    print(a)
    a = sorted(a)
    print(a)
    print(len(a))
    
    filename_txt = 'tokenization\\329.txt'
    f = open(filename_txt, 'r')
    ''' strip document into token list'''
    data = f.read().split()
    token_stream = data
    print(len(token_stream))
    
    f = open('dic\\doc.txt', 'rb')
    k = cPickle.load(f)
    f.close()
    print(k)
    t = 0
    for item in k:
        t = t + item[1]
    print(t)
    
    a = [[291, 2.38], [301, 2.20], [115, 2.11], [1,1.34]]
    b = a.sort()
    a = sorted(a, key = lambda doc: doc[1], reverse = True)
    print(a)
    print(b)
    
    s = "Democrats' welfare , ! . build-in and healthcare reform policies"
    print(nltk.wordpunct_tokenize(s))
    print(nltk.word_tokenize(s))
    c = nltk.wordpunct_tokenize(s)
    new_string = ''
    for i in c:
        new_string += i
        new_string += ' '
    print('***')
    print(new_string)
    print(re.sub(r'[^\w\s]','',new_string))
    print(re.sub(r'[^\w\s]','',new_string).split())
    t = re.sub(r'[^\w\s]','',new_string).split()
    tokenization = Tokenization.Tokenization()
    print(tokenization.remove_stopwords(t))
    
    
    
    
    c = nltk.word_tokenize(s)
    new_string = ''
    for i in c:
        new_string += i
        new_string += ' '
    print('***')
    print(new_string)
   
    print(re.sub(r'[^\w\s]','',new_string))
    print(re.sub(r'[^\w\s]','',new_string).split())
    t = re.sub(r'[^\w\s]','',new_string).split()
    tokenization = Tokenization.Tokenization()
    print(tokenization.remove_stopwords(t))
    
    
    c = re.sub(r'[^\w\s]','',s)
    print('***')
    print(c)
    print(nltk.wordpunct_tokenize(c))
    print(nltk.word_tokenize(c))
    
    
    
    

    
    
    