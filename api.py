# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import flask
from flask import request
import json
from flask import jsonify, Flask, render_template
from flask_socketio import SocketIO
import plac
import numpy
import re


from KeyWordExtraction import *
#from keywordcluster import *
app = flask.Flask(__name__)
app.config["DEBUG"] = False

model_path = './ner/final-model.pt'
stopWordList = 'nerStopword.txt'
x = extracrKeyWord(model_path, stopWordList)
@app.route('/', methods=['GET'])
def home():
	ner1=[]
	return ner1
@app.route('/extract', methods=['POST']) 
def extract():
	#data = request.stream.read()
	data = request.get_json()
	ner={'KeyWord':x.extracNer_text(data['Art'])}
	return jsonify(ner)
##-------------------------------------------------------------------

@app.route('/dictionary_ner', methods=['POST'])
def dictionary():
    data3 = request.get_json()
    text=data3['Art']
    keyword=[]
    with open('keyword2.txt', encoding="utf8", errors='ignore') as f:
        for line in f:
            keyword.append(line.strip('\n'))
    f.close()
    name=[]
    job=[]
    for i in keyword:
        i=i.split(',')
        name.append(i[0])
        job.append(i[1])
    stopwords = dict.fromkeys(name,True)
    
    fillter = x.extracNer_text(text)
    for i in stopwords:
        if i in text:
        #if search_exact_word._in_string(i, text):
            fillter.append(i.strip())
    fillter.sort(key=len)
    for i in range(len(fillter)-1):
        for j in range(i+1,len(fillter)):
            if fillter[i] in fillter[j]:
                fillter[i]=''
    fillter=[i for i in fillter if i !='']
   
    clean_fillter=[]
    for i in fillter:
        tmp=[]
        tmp.append(i)
        try:
            tmp.append(job[name.index(i+' ')])
        except:
            tmp.append('Ner')
        clean_fillter.append(tmp)
        
    outPut = {'KeyWord:': clean_fillter}
    return jsonify(outPut)

@app.route('/person', methods=['POST'])
def person():
    data3 = request.get_json()
    text=data3['Art']
    keyword=[]
    with open('keyword2.txt', encoding="utf8", errors='ignore') as f:
        for line in f:
            keyword.append(line.strip('\n'))
    f.close()
    name=[]
    job=[]
    for i in keyword:
        i=i.split(',')
        name.append(i[0])
        job.append(i[1])
    stopwords = dict.fromkeys(name,True)
    fillter=[]
    for i in stopwords:
        if i in text:
        #if search_exact_word._in_string(i, text):
            fillter.append(i)
    fillter.sort(key=len)
    for i in range(len(fillter)-1):
        for j in range(i+1,len(fillter)):
            if fillter[i] in fillter[j]:
                fillter[i]=''
    fillter=[i for i in fillter if i !='']
   
    clean_fillter=[]
    for i in fillter:
        tmp=[]
        tmp.append(i)
        tmp.append(job[name.index(i)])
        clean_fillter.append(tmp)
    outPut = {'KeyWord:': clean_fillter}
    return jsonify(outPut)
#app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'
#socketio = SocketIO(app)
#if __name__ == '__main__':
#socketio.run(app)
app.run(host='0.0.0.0', port=63500)
