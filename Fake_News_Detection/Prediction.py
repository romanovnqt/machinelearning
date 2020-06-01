# -*- coding: utf-8 -*-
"""
Created on Mon May 18

@author: Ngo Quang Tri
"""

import pickle
import TextfileTerminal

sentence = input("Please input the sentence you want to verify: ")
print("Your sentence: " + str(sentence))

#retrieving the best model for prediction call
load_model = pickle.load(open("DataFile/final_model.sav", 'rb'))

triple = TextfileTerminal.extracttriple(sentence)

print("Standardized sentence: " + triple)

classifing_threadhold = 0.5
# classifing_threadhold = 0.59
prob = load_model.predict_proba([triple])
if prob[0][1] < classifing_threadhold:
    prediction = "false"
else:
    prediction = "true"
# print("Prob: ",prob[0][1])
print("Your sentence is",prediction)