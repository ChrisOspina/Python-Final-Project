import pandas as pd # For data manipulation and analysis
import matplotlib.pyplot as plt # Plotting library for Python programming language and it's numerical mathematics extension NumPy
from sklearn.preprocessing import LabelEncoder as lr
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as lR
from sklearn.metrics import mean_absolute_error,mean_squared_error, r2_score
from math import sqrt


class regressor:
  '''This class holds our methods and necessary variables for the
  Scklit-Learning model we are going to use linear regression'''
   #Creating Instances of these Libraries
def __init__(self,train,X_train, X_test, y_train, y_test):
        self.train = train
        self.X_train = X_train
        self.X_test = X_test
        self.y_train= y_train
        self.y_test = y_test

def encode_variables(self):
    self.train['Gender'] = lr.fit_transform(self.train['Gender'])
    self.train['Age'] = lr.fit_transform(self.train['Age'])
    self.train['City_Category'] = lr.fit_transform(self.train['City_Category'])

    self.train.head()

    self.train['Product_Category_2'] =self.train['Product_Category_2'].fillna(0).astype('int64')
    self.train['Product_Category_3'] =self.train['Product_Category_3'].fillna(0).astype('int64')

    self.info()

def drop_columns(self):
     '''This method drops irrelevant columns'''
     self.train = self.train.drop(["User_ID","Product_ID"],axis=1)

def linearregression(self):
     '''This method trains the dataset with the linear regression model'''
     lR.fit(self.X_train,self.y_train)
     lR.intercept_
     lR.coef_
     y_pred = lr.predict(self.X_test)
     print(mean_absolute_error(self.y_test, y_pred))
     print(mean_squared_error(self.y_test, y_pred))
     print(r2_score(self.y_test, y_pred))

     print("RMSE of Linear Regression Model is ",sqrt(mean_squared_error(self.y_test, y_pred)))

     






