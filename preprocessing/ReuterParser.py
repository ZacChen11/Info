'''
Created on Sep 30, 2017

@author: Zac
'''
import os
import Tokenization
import Preprocess



if __name__ == '__main__':
      
    '''create a text directory if one does not exist'''
    if not os.path.isdir('text'):
        os.makedirs('text')
      
    for i in range(0,22):
        if i < 10:
            filename = 'file\\reut2-00%i.sgm'%(i)
        else:
            filename = 'file\\reut2-0%i.sgm'%(i)
           
        f = open(filename, 'r', errors = 'ignore')
        s = f.read()
          
        '''parse the file and output the results'''
        parser = Preprocess.Preprocess() 
        parser.parse(s)
      
     
    '''create another text directory'''
    if not os.path.isdir('tokenization'):
        os.makedirs('tokenization')
    
    tokenization = Tokenization.Tokenization()    
    
    for j in range(1,21579):
        filename_txt = 'text\\%d.txt'%(j)  
    
        f = open(filename_txt, 'r')
        s = f.read()

       
        s = tokenization.case_folding(s)
#         print('******case folding *****\n%s'%(s))
        s = tokenization.remove_num(s)    
#         print('******num*****\n%s'%(s))
        s = tokenization.remove_punctuation(s)  
        s = tokenization.toke_nize(s)
# #         print ('*******removal punctuation*******\n%s'%s)
       
        s = tokenization.remove_stopwords(s) 
# #         print ('*******removal stop words*******\n%s'%s)
        s = tokenization.remove_steamming(s)
# #         print ('*******removal steamming *******\n%s'%s)
        s = tokenization.remove_reuter(s, j)
# #         print ('*******removal reuters *******\n%s'%s) 
#         s = tokenization.remove_duplicates(s)
# #         print ('*******remove duplicates********\n%s'%s) 
        new_file = tokenization.list_to_string(s)
# #         print (new_file)
#  
        filename1 = 'tokenization\\%d.txt'%(j)   
        f = open(filename1, 'w')
        f.write(new_file)
#     


#  
     
    
        
    
        