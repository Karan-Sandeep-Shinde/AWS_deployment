# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:09:09 2021

@author: Karan Shinde
"""

class ReadArticles:
    
    def __init__(self):
        self.dataPath = r'C:\Users\Karan Shinde\OneDrive\Desktop\aws_new\article1.txt'
        self.stopWordPath = r"C:\Users\Karan Shinde\OneDrive\Desktop\aws_new\stopWords.txt"
    
    def loadArticles(self):
        with open(self.dataPath,'r') as fl:
            text = fl.read()
        return text
    
    def stopWordFromFile(self):
        with open(self.stopWordPath,'r') as fl:
            text = fl.read()
        return text.split("\n")
    
    def loadArticlesFromDb(self):
        pass
    
    def loadArticlesFromApi(self):
        pass
        
#readObj = ReadArticles() 
#articleText = readObj.loadArticles()
#print("The text is \n\n{}".format(articleText))