'''
Created on Oct 15, 2017

@author: Zac
'''
import _pickle as cPickle
import math

class QueryRetrieval():


    def __init__(self):
        pass
    
    def and_search(self, m_list):
        f = open('dic\\dictionary.txt', 'rb')
        d = cPickle.load(f)
        f.close()
        f = open('dic\\keys.txt', 'rb')
        k = cPickle.load(f)
        f.close()
        n = 0
        '''check if all the words in query is in the dictionary'''
        for item in m_list:
            if item in k:
                n += 1
        '''words are in dictionary'''
        if n == len(m_list):
            ''' single word'''
            if n == 1:
                n_list = []
                for item in d[m_list[0]]:
                    docid = item[0]
                    n_list.append(docid)
#                 print ('posting list is %s'%(d[m_list[0]]))
                print ('posting list is %s'%(n_list))
           
            elif n == 2:
                p1 = d[m_list[0]]
                p2 = d[m_list[1]]
                n1 = len(p1)
                n2 = len(p2)
                i = 0
                j = 0 
                doclist = []  
                
                ' compare the doc id'
                while i < n1 and j < n2:
                    if p1[i][0] < p2[j][0]:
                        i+=1
                    elif p1[i][0] > p2[j][0]:
                        j+=1
                    else:
                        doclist.append(p1[i])
                        i+=1
                        j+=1
                if not doclist:
                    print('no match')
                else:
                    n_list = []
                    for item in doclist:
                        docid = item[0]
                        n_list.append(docid)
#                     print('posting list is %s'%(doclist))
                    print('posting list is %s'%(n_list))
            
            else:
                list_of_posting = []
                for item in m_list:
                 
                    list_of_posting.append(d[item])
               
                '''sort the posting list based on frequency'''
                for ii in range(1, len(list_of_posting)):
                    
                    v = list_of_posting[ii]
                    jj = ii - 1
                   
                    while len(list_of_posting[jj])> len(v):
        
                        list_of_posting[jj+1] = list_of_posting[jj]
                        jj = jj - 1
                        if jj < 0:
                            break
                    list_of_posting[jj+1] = v
               
                
            
                
                doclist = list_of_posting[0]
              
                del list_of_posting[0]
                first = list_of_posting[0]
            
                del list_of_posting[0]
               
                
                while  len(list_of_posting) >= 0 :
                
                    p1 = doclist
                    p2 = first
                    n1 = len(p1)
                    n2 = len(p2)
                    i = 0
                    j = 0 
                    result = [] 
                    while i < n1 and j < n2:
                        if p1[i][0] < p2[j][0]:
                            i+=1
                        elif p1[i][0] > p2[j][0]:
                            j+=1
                        else:
                            result.append(p1[i])
                            i+=1
                            j+=1
                    if len(list_of_posting) > 0:     
                        doclist = result
                        first = list_of_posting[0]
                        del list_of_posting[0]
                    else:
                        break
   
                if not result:
                    print('no match')
                else:
                    n_list = []
                    for item in result:
                        docid = item[0]
                        n_list.append(docid)
#                     print('posting list is %s'%(result))
                    print('posting list is %s'%(n_list))    
        else:
            print('no match')     
            
    def or_search(self, m_list):
        f = open('dic\\dictionary.txt', 'rb')
        d = cPickle.load(f)
        f.close()
        f = open('dic\\keys.txt', 'rb')
        k = cPickle.load(f)
        f.close()
        n = 0  
        '''check if anyone of the words in query is in the dictionary'''
        for item in m_list:
            if item in k:
                n += 1
                
        '''words are in dictionary'''
        if n > 0:
            list_of_posting = []
            for item in m_list:
                if item in k:
                    list_of_posting = list_of_posting + d[item]
                        
            list_of_posting = sorted(list_of_posting)
            new_list = []
            for item in list_of_posting:
                docid = item[0]
                if not docid in new_list:
                    new_list.append(docid)
            print('posting list is: %s'%(new_list))
            print('list length: %d'%(len(new_list)))
            return new_list
        else:
            print('no match')
            return []
    
    def combine_search(self, doc1, doc2):
        p1 = doc1
        p2 = doc2
        n1 = len(p1)
        n2 = len(p2)
        i = 0
        j = 0 
        doclist = []  
        while i < n1 and j < n2:
            if p1[i] < p2[j]:
                i+=1
            elif p1[i] > p2[j]:
                j+=1
            else:
                doclist.append(p1[i])
                i+=1
                j+=1
        if not doclist:
            print('no match')
            return 'no match'
        else:
            print('posting list is %s'%(doclist))
            return doclist
        
    
    def rank(self, m_query, k1, b ):
        
        'return or list'
        m_list = QueryRetrieval.or_search(self,m_query)
        
        f = open('dic\\dictionary.txt', 'rb')
        d = cPickle.load(f)
        f.close()
        f = open('dic\\keys.txt', 'rb')
        k = cPickle.load(f)
        f.close()
        f = open('dic\\doc.txt', 'rb')
        l = cPickle.load(f)
        f.close()
        
        new_list = []
        n = 0
        N = 21578.0
        l_average = 1695867.0/N
#         print('average of a doc is : %s'%l_average)
        
        
        'for each doc in the list'
        for id in m_list:
            m_RSV = 0
            ld = l[id-1][1]
#             print('doc length is %d'%ld)
            '''check if the word in query is in the dictionary'''
            for item in m_query: 
                if item in k:
                    'if the term is in dictionary, get the document frequency'
                    dft = len(d[item])
#                     print('dft is %d'%(dft))
                    m_log = math.log10(N/dft)
                    
                    'the posting list of the term'
                    for doc in d[item]:
                        'if the posting list of the term includes doc id,we get the term frequency '
                        if id == doc[0]:
                            tf = doc[1]
                            m_RSV = m_RSV + m_log * (k1 + 1)* tf/ (k1*((1-b)+b*(ld/l_average))+tf)
                    
            'store the score of each doc in a list'
            new_list.append([id, m_RSV])
        'sort the final doc list based on score'    
        new_list = sorted(new_list, key = lambda z:z[1], reverse = True)
        
        n_list = []
        for item in new_list:
            docid = item[0]
            n_list.append(docid)
#         print('list :%s'%new_list)        
        print('ranked posting list is %s'%n_list)
                    
                   
                   
                   
               
               
               
               
        
            
    
    
    