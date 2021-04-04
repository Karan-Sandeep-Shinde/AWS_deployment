# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:45:10 2021

@author: Karan Shinde
"""
import re
from load_data import ReadArticles

class PreprocessText:
    
    def __init__(self):
        self.specialChars = [',',';','#','$','\',\n','\n\n']
        readObj = ReadArticles() 
        self.articleText = readObj.loadArticles()
        self.stopWords = readObj.stopWordFromFile()
    
    
    def sentTokenize(self,text):
        """Tokenize sentences from article.
        
        Input:
            text: string
        Output:
            sentArray: a list of strings
         """
        sentArray = text.split(".")
        return sentArray
     
    def wordTokenize(self,text):
        """Tokenize the words
        """
        return re.split(" |,|;|-",text)
    
    def removeStopWords(self,text):
        """Removal of stop words
        """
        
        wordList = self.wordTokenize(text)
        filteredWordList = [word for word in wordList if word not in self.stopWords]
        sentence = ' '.join(filteredWordList)
        return sentence
    
    def removeSpecialChar(self,text):
        
        sentence = ''.join([char for char in text if char not in self.specialChars])
        return sentence
    
    def convertToLC(self,text):
        
        return text.lower()
    
    def preprocess(self,article):
#        text = self.articleText
        text = article
        sentences = self.sentTokenize(text)
        processedSentList = []
        for sentence in sentences:
            text = self.convertToLC(sentence)
            text = self.removeSpecialChar(text)
            text = self.removeStopWords(text)
            processedSentList.append(text)
        return processedSentList
    
#processObj = PreprocessText()
#processedSentList = processObj.preprocess()
#print("List of process sentences: \n\n{}".format(processedSentList))
        