''' 
Created on Sep 30, 2017

@author: Zac
'''

import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.stem.wordnet import WordNetLemmatizer





class Tokenization():
    
    def toke_nize(self, string):
        
        return nltk.word_tokenize(string)
#         return nltk.wordpunct_tokenize(string)
    
    def case_folding(self, string):
        
        return string.lower()
      
    
    def remove_num(self, string):
        
        return re.sub(r'\d', '', string)
    
    def remove_punctuation(self, string):
        
        return re.sub(r'[^\w\s]','',string)
    
    def remove_stopwords(self, m_list):
        stop_words = set(stopwords.words('english'))
        new_list = []
        for i in m_list:
            if not i in stop_words:
                new_list.append(i)
        return new_list
    
    def remove_steamming(self, m_list):
        new_list = []
        s = PorterStemmer()
        for i in m_list:
            a = s.stem(i)
            new_list.append(a) 
        return new_list
        
    
#     def remove_lemmatization(self, data):
#         new_data = []
#         l = WordNetLemmatizer()
#         for i in data:
#             a = l.lemmatize(i)
#             new_data.append(a)
#         return new_data
    
    def remove_duplicates(self, m_list):
        new_list = []
        for i in m_list:
            if not i in new_list:
                new_list.append(i)
        return new_list
    
    def remove_reuter(self, m_list, a):
        if len(m_list)==0:
#             print ('doc : %d'%(a))
            return m_list
        else:
            del m_list[-1]
            return m_list
    
    def list_to_string(self, m_list):
        new_string = ''
        for i in m_list:
            new_string += i
            new_string += ' '
        return new_string
