# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:34:33 2021

@author: Karan Shinde
"""
import numpy as np
from preProcessor import PreprocessText
import json
import flask
from flask import Flask , request

SummaryApp = Flask(__name__)

class SummarizeArticle:
    
    def __init__(self,article):
        processObj = PreprocessText()
        self.sentArray = processObj.preprocess(article)
    
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
#
#@SummaryApp.route('/home/summary/default',methods=['GET'])
#def summaryApi():
#    summaryObj = SummarizeArticle()
#    summary = summaryObj.summarize()
#    return summary
##    print("The summary of article is\n\n{}".format(summary))
    
@SummaryApp.route('/home/summary/custom',methods=['POST'])
def summaryApi():
    article = json.loads(request.data.decode())["articleText"]
    summaryObj = SummarizeArticle(article)
    summary = summaryObj.summarize()
    return summary
##    print("The summary of article is\n\n{}".format(summary))
    
SummaryApp.run('127.0.0.1',port=8000)
    
    
            