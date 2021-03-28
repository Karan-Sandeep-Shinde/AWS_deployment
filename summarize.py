# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:34:33 2021

@author: Karan Shinde
"""
import numpy as np
from preProcessor import PreprocessText

class SummarizeArticle:
    
    def __init__(self):
        processObj = PreprocessText()
        self.sentArray = processObj.preprocess()
    
    def groupSentence(self,sentArray):
        
        firstSent = sentArray[0]
        restSents = sentArray[1:]
        return firstSent,restSents
    
    def sortSentences(self,restSents):
        sentLengths = [len(sent) for sent in restSents]
        sortedIdxs = np.argsort(sentLengths)
        sortedSentences = []
        for idx in sortedIdxs:
            sortedSentences.append(restSents[len(restSents)-idx-1])
        return sortedSentences
    
    def combineSentences(self,firstSent,sortedSentences):
        
        combinedSentences = [firstSent] + sortedSentences[:5]
        summary = ' '.join(combinedSentences)
        return summary
    
    def summarize(self):
        
        firstSent,restSents = self.groupSentence(self.sentArray)
        sortedSentences = self.sortSentences(restSents)
        summary = self.combineSentences(firstSent,sortedSentences)
        return summary
    
summaryObj = SummarizeArticle()
summary = summaryObj.summarize()
print("The summary of article is\n\n{}".format(summary))
    
    
            