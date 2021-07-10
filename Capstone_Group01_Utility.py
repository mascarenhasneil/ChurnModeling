"""
Final Capstone Project. Group 1
ALY6140 80956 Analytics Systems Technology SEC 04 Spring 2021 CPS

Title: Customer Churn Modeling.

Copyright (c) 2021
Licensed
Written by Neil Mascarenhas
Date: 10 May 2021
"""


from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import AdaBoostClassifier



def Test():   # Not required but a good practice to check if this file is accessible 
    print("Capstone Test Successful")


def EstimatedSalary_FE(bcd):
    bcd.loc[bcd['EstimatedSalary'] <= 40007, 'EstimatedSalary'] = 0
    bcd.loc[(bcd['EstimatedSalary'] > 40007) & (bcd['EstimatedSalary'] <= 80003), 'EstimatedSalary'] = 1
    bcd.loc[(bcd['EstimatedSalary'] > 80003) & (bcd['EstimatedSalary'] <= 120000), 'EstimatedSalary'] = 2
    bcd.loc[(bcd['EstimatedSalary'] > 120000) & (bcd['EstimatedSalary'] <= 159996), 'EstimatedSalary'] = 3
    bcd.loc[bcd['EstimatedSalary'] > 159996, 'EstimatedSalary'] = 4

    return bcd

def Balance_FE(bcd):
    bcd.loc[bcd['Balance'] <= 0, 'Balance'] = 0
    bcd.loc[(bcd['Balance'] > 0) & (bcd['Balance'] <= 251), 'Balance'] = 1
    bcd.loc[(bcd['Balance'] > 251) & (bcd['Balance'] <= 50179), 'Balance'] = 2
    bcd.loc[(bcd['Balance'] > 50179) & (bcd['Balance'] <= 100359), 'Balance'] = 3
    bcd.loc[(bcd['Balance'] > 100359) & (bcd['Balance'] <= 150538), 'Balance'] = 4
    bcd.loc[(bcd['Balance'] > 150538) & (bcd['Balance'] <= 200718), 'Balance'] = 5
    bcd.loc[(bcd['Balance'] > 200718) & (bcd['Balance'] <= 250000), 'Balance'] = 6
    return bcd

def CreditScore_FE(bcd):
    bcd.loc[bcd['CreditScore'] <= 450, 'CreditScore'] = 0
    bcd.loc[(bcd['CreditScore'] > 450) & (bcd['CreditScore'] <= 550), 'CreditScore'] = 1
    bcd.loc[(bcd['CreditScore'] > 550) & (bcd['CreditScore'] <= 650), 'CreditScore'] = 2
    bcd.loc[(bcd['CreditScore'] > 650) & (bcd['CreditScore'] <= 750), 'CreditScore'] = 3
    bcd.loc[(bcd['CreditScore'] > 750) & (bcd['CreditScore'] <= 850), 'CreditScore'] = 4
    bcd.loc[(bcd['CreditScore'] > 850), 'CreditScore'] = 5
    return bcd



def GetModels():
    models = []
    models.append(['XGBClassifier',XGBClassifier(learning_rate=0.1,
                                             objective='binary:logistic',
                                             random_state=0,eval_metric='mlogloss')])
    models.append(['Logistic Regression',LogisticRegression(random_state=0)])
    models.append(['SVM',SVC(random_state=0)])
    models.append(['KNeigbors',KNeighborsClassifier()])
    models.append(['DecisionTree',DecisionTreeClassifier(random_state=0)])
    models.append(['RandomForest',RandomForestClassifier(random_state=0)])
    models.append(['AdaBoostClassifier',AdaBoostClassifier()])
    return models


def Get_Grid_Models():
    grid_models = [(XGBClassifier(), [{'learning_rate': [0.01, 0.05, 0.1], 'eval_metric': ['logloss','error']}]),
               (KNeighborsClassifier(),[{'n_neighbors':[5,7,8,10], 'metric': ['euclidean', 'manhattan', 'chebyshev', 'minkowski']}]), 
               (DecisionTreeClassifier(),[{'criterion':['gini','entropy'],'random_state':[0]}]), 
               (RandomForestClassifier(),[{'n_estimators':[100,150,200],'criterion':['gini','entropy'],'random_state':[0]}]),]
    return grid_models

def Get_classifier():
    classifier = XGBClassifier(base_score=None, booster=None, colsample_bylevel=None,colsample_bynode=None, colsample_bytree=None, gamma=None,
              gpu_id=None, importance_type='gain', interaction_constraints=None,
              learning_rate=None, max_delta_step=None, max_depth=None,
              min_child_weight=None,monotone_constraints=None,
              n_estimators=100, n_jobs=None, num_parallel_tree=None,
              random_state=None, reg_alpha=None, reg_lambda=None,
              scale_pos_weight=None, subsample=None, tree_method=None,
              validate_parameters=None, verbosity=None)
    return classifier


