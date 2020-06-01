# -*- coding: utf-8 -*-
"""
Created on Mon May 18th

@author: Ngo Quang Tri
"""

import pickle

import DataPrep

print("Load Model File")
load_model = pickle.load(open("DataFile/final_model.sav", 'rb'))

#below dataset were used for testing and validation purposes
# print(DataPrep.test_news.shape)
# print(DataPrep.test_news.all)

total_prediction = 2000

classifing_threadhold = 0.5

def testData(classifing_threadhold):

    statement = ""
    right_label = ""
    true_prediction = 0

    for i in range(0,total_prediction):
        statement = DataPrep.test_news.iloc[i]['Statement']
        right_label = DataPrep.test_news.iloc[i]['Label']

        prob = load_model.predict_proba([statement])
        if prob[0][1] < classifing_threadhold:
            prediction = False
        else:
            prediction = True

        if(prediction == right_label):
            # print(i)
            # print(statement)
            # print(right_label)
            # print(prediction_label)
            true_prediction = true_prediction + 1

    # print("Result")
    # print("Total: ", total_prediction)
    # print("Accurate: ", true_prediction)
    # print("Accurate Rate : ", ((true_prediction/total_prediction)*100))
    print("Result: True: ",true_prediction," Total: ",total_prediction," Rate: ", ((true_prediction / total_prediction) * 100), " %")
    # for train_ind, test_ind in k_fold.split(DataPrep.train_news):

for i in range (1,99):
    classifing_threadhold = i/100
    print("Thread_hold",classifing_threadhold)
    testData(classifing_threadhold)