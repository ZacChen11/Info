'''
Created on Sep 30, 2017

@author: Zac
'''
import sys
import _pickle as cPickle
import os

class SPIMI():
    '''memory size is 0.5 MB '''
    MemorySize = 0.5
    
    def __init__(self):
        self.current_used_memory_size = 0
        self.num = 0
        self.c = 0
      
        
        
    def generate_dic(self):
        
        current_dict = {}
        doc_length = []
#         c2 = 0
        ''' parse the documents'''
        for j in range(1,21579):
            filename_txt = 'tokenization\\%d.txt'%j
            f = open(filename_txt, 'r')
            ''' strip document into token list'''
            data = f.read().split()
            token_stream = data
            m_length = len(token_stream)
            doc_length.append([j,m_length])
            i = 0
            print ('read doc %d'%j)
            
            
            
            while(i < len(token_stream)):
                
                while (SPIMI.MemorySize* 1024*1024 - self.current_used_memory_size) >0 and i < len(token_stream) :
                
                
                    self.current_used_memory_size = 0
                    
                    if not token_stream[i] in current_dict:
                        current_dict[token_stream[i]] = []
#                         c1 = c1 + 1
                    
#                     print ('current dic size is %d'%(sys.getsizeof(current_dict)))
#                     print ('current dic size of mb is %f'%(sys.getsizeof(current_dict)/1024.0/1024.0))
# #     
                    
                    'check if the current term is already in the same doc in order to compute the term frequency'
                    'current posting list is empty'
                    if  current_dict[token_stream[i]] == []:
                        current_dict[token_stream[i]].append([j,1])
                        self.c = self.c + 1
                    elif current_dict[token_stream[i]][-1][0] == j:
                        current_dict[token_stream[i]][-1][1]+=1
                        self.c = self.c + 1
                    else:
                        current_dict[token_stream[i]].append([j,1])
                        self.c = self.c + 1
                        
                    self.current_used_memory_size = sys.getsizeof(current_dict)
                    i = i + 1
            
            
                ''' memory is over '''
                if SPIMI.MemorySize* 1024*1024 - self.current_used_memory_size <= 0:
                    self.num = self.num + 1
                    print (' memory done') 
                    print (current_dict)
                    '''sort '''
                    key_list = sorted(current_dict.keys());
                    print('new dic %d'%(self.num))
                    print(key_list)
                
                
                    '''write dictionary into disk'''
                    filename = 'dic\\dic%d.txt'%(self.num)  
                    f = open(filename, "wb")
                    cPickle.dump(current_dict, f)
                    f.close()
                    '''write key list into disk'''
                    filename = 'dic\\keylist%d.txt'%(self.num)  
                    f = open(filename, "wb")
                    cPickle.dump(key_list, f)
                    f.close()
                    
                    self.current_used_memory_size = 0
                    current_dict = {}
                
                elif j == 21578:
                    self.num = self.num + 1
                    print (' last one ') 
                    print (current_dict)
                    '''sort '''
                    key_list = sorted(current_dict.keys());
                    print('new dic %d'%(self.num))
                    print(key_list)
                
                
                    '''write dictionary into disk'''
                    filename = 'dic\\dic%d.txt'%(self.num)  
                    f = open(filename, "wb")
                    cPickle.dump(current_dict, f)
                    f.close()
                    '''write key list into disk'''
                    filename = 'dic\\keylist%d.txt'%(self.num)  
                    f = open(filename, "wb")
                    cPickle.dump(key_list, f)
                    f.close()
                    break
        
        '''write doc length into disk'''
        filename = 'dic\\doc.txt'
        f = open(filename, "wb")
        cPickle.dump(doc_length, f)
        f.close()
        print ('out of loop')
#         print('c1 : %d'%c1)
#         print('c2 : %d'%c2)
        

    def merge_dic(self):
        
        list_merge = []
        dic_merge = []
        print('num is %d'%self.num)
        '''compare and merge dictionaries'''
        for m in range(1,self.num+1):
            
            if m == 1:
                print('enter list1, dic1')
                f1 = open('dic\\keylist1.txt', 'rb')
                f2 = open('dic\\dic1.txt', 'rb')
                k1 = cPickle.load(f1)
                d1 = cPickle.load(f2)
                list_merge = k1
                dic_merge = d1
                f1.close()
                f2.close()
#                 print('list:%d  dic:%d'%(len(list_merge), len(dic_merge)))
#                 print(list_merge)
#                 print(dic_merge)
                  
            
            else:
                print('enter list%d dic%d'%(m,m))
                f1 = open('dic\\keylist%d.txt'%m, 'rb')
                f2 = open('dic\\dic%d.txt'%m, 'rb')
                k1 = cPickle.load(f1)
                d1 = cPickle.load(f2)
                f1.close()
                f2.close()
                k2 = list_merge
                d2 = dic_merge
                n1 = len(k1)
                n2 = len(k2)
                list_merge = []
                dic_merge = {}
                i = 0
                j = 0
    
                while i < n1 and j < n2:
                    if k1[i] < k2[j]:
                        list_merge.append(k1[i])
                        dic_merge[k1[i]] = d1[k1[i]]
                        i+=1
                    elif k1[i] > k2[j]:
                        list_merge.append(k2[j])
                        dic_merge[k2[j]] = d2[k2[j]]
                        j+=1
                    else:
                        list_merge.append(k1[i])
                        dic_merge[k1[i]] = d2[k2[j]]+d1[k1[i]]
                        i+=1
                        j+=1
            
                if i >= n1:
                    for k in range(j, n2):
                        list_merge.append(k2[k])
                        dic_merge[k2[k]] = d2[k2[k]]
                if j >= n2:
                    for k in range(i, n1):
                        list_merge.append(k1[k])
                        dic_merge[k1[k]] = d1[k1[k]]
                        
#                 print('i:%d  j:%d  n1:%d  n2:%d  k:%d'%(i,j,n1,n2,k))    
#                 print(list_merge)
#                 print(dic_merge)
            
        print('merge all')
#         print('list:%d'%(len(list_merge)))
#         print(list_merge)
#         print(dic_merge)
        
        
        '''write the dictionary into a disk''' 
        filename = 'dic\\dictionary.txt' 
        f = open(filename, "wb")
        cPickle.dump(dic_merge, f)
        f.close()
        '''write key list into disk'''
        filename = 'dic\\keys.txt'  
        f = open(filename, "wb")
        cPickle.dump(list_merge, f)
        f.close()

        
        
        
        
        
      
          
if __name__ == '__main__':
    '''create another text directory'''
    if not os.path.isdir('dic'):
        os.makedirs('dic')
               
    spimi = SPIMI()
    spimi.generate_dic()
    spimi.merge_dic()
    print(spimi.c)
 
    
        