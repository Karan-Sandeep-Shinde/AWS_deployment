# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:18:40 2021

@author: Karan Shinde
"""

import flask
from flask import Flask,request

app = Flask(__name__)

@app.route('/home',methods=['GET'])
def printYay():
    return "Yay!! its working!!!"


app.run(host='127.0.0.1',port=8080)

