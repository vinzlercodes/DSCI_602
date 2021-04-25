__authors__ = 'Abdullah + Vinayak'

import pickle
import pandas as pd
import time
from sklearn.metrics import classification_report
from skmultilearn.problem_transform import ClassifierChain
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm

def train_and_pickle(model,name,X_train,y_train):
    """
    :param model:
    :param name:
    :param X_train:
    :param y_train:
    :return:
    """
    model.fit(X_train,y_train)
    y_pred = model.predict(X_train)
    print(classification_report(y_pred,y_train))
    with open('../models/'+name+'.pickle', 'wb') as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    """
    main method to use the splited train data set and send it to train_and_pickle method with ml classifiers
    to be trained and generate  the classification_report and lastly pickle the model
    """
    start = time.time()
    # Load data
    X_train = pd.read_csv(r'../Data/Train_Features.csv',index_col=0)
    y_train = pd.read_csv(r'../Data/Train_Labels.csv',index_col=0)
    # perapare the classifiers with their parameters to be send to train_and_pickle
    classifiers = [{'classifierName':'RandomForest','classifier':RandomForestClassifier(class_weight='balanced')}
        , {'classifierName':'MNB','classifier':MultinomialNB()},{'classifierName':'SVM','classifier':svm.SVC()},
                   {'classifierName':'LR','classifier':LogisticRegression()}]
    #send the classifiers one by one usinf for loop
    for x in classifiers:
        print(x['classifierName'],x['classifier'])
        classifierChain = ClassifierChain(x['classifier'])
        train_and_pickle(classifierChain,x['classifierName'],X_train,y_train)
        print((time.time()-start) , 'sec')