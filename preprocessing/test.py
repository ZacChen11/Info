'''
Created on Oct 15, 2017

@author: Zac
'''

import Tokenization
import QueryRetrieval

class process_Query():
    def __init__(self):
        pass
    
    def process_query(self,s):
      
        tokenization = Tokenization.Tokenization()
  
        s = tokenization.case_folding(s)
#         print('******case folding *****\n%s'%(s))
        s = tokenization.remove_num(s) 
        s = tokenization.remove_punctuation(s)
        s = tokenization.toke_nize(s)
       
        s = tokenization.remove_stopwords(s) 
# #         print ('*******removal stop words*******\n%s'%s)
        s = tokenization.remove_steamming(s)
# #         print ('*******removal steamming *******\n%s'%s)
        print (s)  
        return s

if __name__ == '__main__':
    
    m_query = QueryRetrieval.QueryRetrieval()
    process_query = process_Query() 
   
    'sample queries'
    print("Democrats' welfare and healthcare reform policies")
    s = process_query.process_query("Democrats' welfare and healthcare reform policies")  
    m_query.rank(s, 1.5, 0.75)
    
    print("\nDrug company bankruptcies")
    s = process_query.process_query("Drug company bankruptcies")  
    m_query.rank(s, 1.5, 0.75)
    
    print("\nGeorge Bush")
    s = process_query.process_query("George Bush")  
    m_query.rank(s, 1.5, 0.75)
    
    'version 1 of sample queries'
    print("\nDemocrats' benefits and medical care reform policies")
    s = process_query.process_query("People's benefits and medical care reform policies")  
    m_query.rank(s, 1.5, 0.75)
    
    print("\nMedical company bankruptcies")
    s = process_query.process_query("Medical company bankruptcies")  
    m_query.rank(s, 1.5, 0.75)
    
    print("\nAmerican President George Bush")
    s = process_query.process_query("American President George Bush")  
    m_query.rank(s, 1.5, 0.75)
    
    'version 2 of sample queries'
    print("\nDemocrats' welfare and medical care reform policies")
    s = process_query.process_query("People's benefits and medical care reform policies")  
    m_query.rank(s, 1.5, 0.75)
    
    print("\nDrug corporation bankruptcies")
    s = process_query.process_query("Medical corporation bankruptcies")  
    m_query.rank(s, 1.5, 0.75)
    
    print("\nGeorge Bush President of USA")
    s = process_query.process_query("George Bush President of USA")  
    m_query.rank(s, 1.5, 0.75)
    
    'version 3 of sample queries'
    print("\nDemocratic welfare and healthcare policy reformation")
    s = process_query.process_query("Democratic welfare and healthcare policy reformation")  
    m_query.rank(s, 1.5, 0.75)
    
    print("\nDrug company bankrupt")
    s = process_query.process_query("Drug company bankruptcies")  
    m_query.rank(s, 1.5, 0.75)
    
    print("\nPresident George Bush")
    s = process_query.process_query("President George Bush")  
    m_query.rank(s, 1.5, 0.75)
    
    
    'my queries'
    print("\nShipholding")
    s = process_query.process_query("Shipholding")  
    m_query.rank(s, 1.5, 0.75)
    
    print("\nexpanded theater")
    s = process_query.process_query("expanded theater")  
    m_query.rank(s, 1.5, 0.75)
    
    print("\nNephew Associated Companies SMITH AND NEPHEW")
    s = process_query.process_query("Nephew Associated Companies SMITH AND NEPHEW")  
    m_query.rank(s, 1.5, 0.75)
    
    
    
    
    
    
    
    


    
    
    
    
    
    