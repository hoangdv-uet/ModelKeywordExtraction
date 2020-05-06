from flair.models import SequenceTagger
from flair.data import Sentence
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re
import string


def unique(list1):

	unique_list = [] 
	for x in list1: 
		if x not in unique_list: 
			unique_list.append(x)
	for i in unique_list:
		if len(i.split()) == 1:
			for j in unique_list:
				if i in j.split() and len(j.split()) > 1:
					unique_list.remove(i) 
					break 
	return unique_list

class extracrKeyWord:
	
	def __init__(self,model_path,WordList):
		self.model = SequenceTagger.load(model_path)
		keyword=[]
		self.name=[]
		self.entity=[]

		with open(WordList, 'r', encoding='utf-8', errors='ignore') as f:
			for line in f:
				keyword.append(line.strip('\n'))

		for i in keyword:
			i=i.split(',')
			self.name.append(i[0])
			self.entity.append(i[1])

		self.stopwords = dict.fromkeys(self.name,True)

	def extracNer_text(self, text):
		text = re.sub(r'[,\.\()]', ' va ', text)
		text = text.translate(str.maketrans('','',string.punctuation))
					
		sentence = Sentence(str(text))	
		self.model.predict(sentence)

		ner=[]
		for i in sentence.get_spans('ner'):
			ner.append(str(i).split('"')[1])
			ner = unique(ner)

		fillter = ner
		for i in self.stopwords:
			if i in text:
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
				tmp.append(self.entity[self.name.index(i+' ')])
			except:
				tmp.append('Ner')
			clean_fillter.append(tmp)
		return clean_fillter


model_path = './Ner_model/final-model.pt'
WordList = './keyword2.txt'
x = extracrKeyWord(model_path,WordList)
print(x.extracNer_text('...'))