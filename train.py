from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import joblib



import pandas as pd
import numpy as np

class train:

    clf = None

    def __init__(self, data,  model = 'svm', k_n = 5, kernel = 'rbf'):
        self.model = model
        self.data = data
        self.kn = k_n
        self.kernel = kernel

    

    def split_data(self):
        X = self.data.drop('target', axis = 1)
        y = self.data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 
    
        return X_train, X_test, y_train, y_test
    
    def scale_data(x_train, x_test):
        sc = MinMaxScaler()
        sc.fit(x_train)
        x_tr = sc.fit_transform(x_train)
        x_te = sc.fit_transform(x_test)

        return x_tr, x_te
    

    def train(self, data = None): 
        x_tr, x_te, y_tr, y_te = self.split_data() #split data

        #choose the right model
        if self.model ==  'lr':
            self.clf = LogisticRegression(random_state=0)
    
        elif self.model =='knn':
            self.clf = KNeighborsClassifier(self.kn)

        elif self.model == 'svm':                
            self.clf = SVC(kernel = 'rbf', random_state =  0)
                
        #fit the model
        self.clf.fit(x_tr, y_tr)
        y_predict = self.clf.predict(x_te) #test the model
        tr_score = self.clf.score(x_tr, y_tr) #get train score
        te_score = self.clf.score(x_te, y_te) #get test score
          

        joblib.dump(self.clf, 'model.pkl')
            
        report = classification_report(y_true=y_te, y_pred= y_predict, output_dict = True)
        df_report= pd.DataFrame(report).T.to_html(classes = 'table table-dark table-striped')
            
        return df_report, tr_score, te_score #return neccessary vlaues

        
    
        



