# -*- coding: utf-8 -*-
'''
Created on Sep 27, 2017

@author: Zac
'''
import sgmllib
from fileinput import filename

class Preprocess(sgmllib.SGMLParser):

    def __init__(self, verbose = 0):
        ''' Initialize an object, passing ’verbose’ to the superclass '''
        sgmllib.SGMLParser.__init__(self, verbose)
        
        '''indicate whether we pass the title'''
        self.in_title = 0
        
        ''' Flag indicating whether or not we’re parsing the dateline'''
        self.in_dateline = 0

        '''Flag indicating whether or not we’re parsing the body'''
        self.in_body = 0
        
        self.in_text = 0
        
        '''Title of the document'''
        self.title = ''
        
        '''docID'''
        self.doc_id = 0
        
        '''date line for the document'''
        self.dateline = ''
        
        '''body of document'''
        self.body = '' 
        
        '''text of doc'''
        self.text = ''
        
    def parse(self, string):
        self.feed(string)
        self.close()
        
   
    '''print out data in TEXT '''
    def handle_data(self, data):
        if self.in_body:
            self.body = self.body + data
        elif self.in_title:
            self.title = self.title + data
        elif self.in_dateline:
            self.dateline = self.dateline + data
        elif self.in_text :
            self.body = self.body + data

    '''handle reuters tag'''
    def start_reuters(self, attributes):
        '''bracket each document as a new file'''
        for name, value in attributes:
            if name == 'newid':
                self.doc_id = value 
                
    '''write out the contents to a file and reset all variables'''
    def end_reuters(self):
        from textwrap import fill 
        import re
        
        '''print out contents. For body of the text, merge into 70 character lines using python's fill utility'''
        filename = 'text/'+str(self.doc_id)+ '.txt'
        doc_file = open(filename, 'w')
        doc_file.write(self.title + '\n')
        '''strip out multiple spaces in the body'''
        self.body = re.sub(r'\s+', r' ', self.body)
        doc_file.write(fill(self.body)+'\n')
        doc_file.close()
        
        '''reset variables'''
        self.in_title = 0
        self.in_dateline = 0
        self.in_body = 0
        self.doc_id = 0
        self.in_text = 0
        self.title = ''
        self.body = ''
        self.dateline = ''
    
    '''handle title tags '''
    def start_title(self, attributes):
        self.in_title = 1
    
    def end_title(self):
        self.in_title = 0
    
    ''' handle dateline tags '''
    def start_dateline(self, attributes):
        self.in_dateline = 1
        
    def end_dateline(self):
        self.in_dateline = 0
    
    '''handle body tags '''
    def start_body(self, attributes):
        self.in_body = 1
    
    def end_body(self):
        self.in_body = 0
        
    def start_text(self, attributes):
        self.in_text = 1
     
    def end_text(self):
        self.in_text = 0
     
import sys
import os
import os.path

# if __name__ == '__main__':
#      
#     '''create a text directory if one does not exist'''
#     if not os.path.isdir('text1'):
#         os.makedirs('text1')
#      
#     for i in range(0,22):
#         if i < 10:
#             filename = 'C:/Users/sh_hen/Desktop/Info/Info/file/reut2-00%i.sgm'%(i)
#         else:
#             filename = 'C:/Users/sh_hen/Desktop/Info/Info/file/reut2-0%i.sgm'%(i)
#          
#         f = open(filename, 'r', errors = 'ignore')
#         s = f.read()
#          
#         '''parse the file and output the results'''
#         parser = Preprocess() 
#         parser.parse(s)
     
     
    
   
        
        
        
        