import pandas as pd
from sklearn.preprocessing import LabelEncoder #this call is already imported in the Notebook
from sklearn.preprocessing import StandardScaler as SS
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

class methods:
    '''This class holds our methods and necessary variables'''
    #Adding the necessary attributes
    X = None
    Xr = None
    Y = None
    X_train = None
    Y_train = None

    #Creating Instances of these Libraries
    lr = LinearRegression()
    dtr = DecisionTreeRegressor()
    rfr = RandomForestRegressor()
    gbr = GradientBoostingRegressor()

    def fill_null_values():
        '''This method creates an array consisting of 2 columns namely Product_Category_2,Product_Category_3
         and replacing the null spaces with max vales'''
        
        b = ['Product_Category_2','Product_Category_3']

        for i in b:
            exec("bfriday.%s.fillna(bfriday.%s.value_counts().idxmax(), inplace=True)" %(i,i))

        return
    
    def convert_data_X(self, dataset):
        '''This method encodes the X data (everything but purchases)
        and converts it into numerical form'''
        X = dataset.drop(["Purchase"], axis=1)
        LE = LabelEncoder()
        X= X.apply(LE.fit_transform) #apply encoder into our data

        #Now we will convert the data into numeric data
        X.Gender = pd.to_numeric(X.Gender)
        X.Age = pd.to_numeric(X.Age)
        X.Occupation = pd.to_numeric(X.Occupation)
        X.City_Category = pd.to_numeric(X.City_Category)
        X.Stay_In_Current_City_Years = pd.to_numeric(X.Stay_In_Current_City_Years)
        X.Marital_Status = pd.to_numeric(X.Marital_Status)
        X.Product_Category_1 = pd.to_numeric(X.Product_Category_1)
        X.Product_Category_2 = pd.to_numeric(X.Product_Category_2)
        X.Product_Category_3 = pd.to_numeric(X.Product_Category_3)

        self.X = X

        self.Xs = SS.fit_transform(X)

        return self.Xs
    def convert_data_Y(self, dataset):
        '''This method does the same thing but for our Y variable which holds purchases'''
        self.Y = dataset["Purchase"]
        return self.Y
    
    def train_models(self,dataset):
        X_train = self.X_train
        y_train = self.Y_train
        '''This method trains the models and outputs the result'''
        fit1 = self.lr.fit(X_train,y_train)#Here we fit training data to linear regressor
        fit2 = self.dtr.fit(X_train,y_train)#Here we fit training data to Decision Tree Regressor
        fit3 = self.rfr.fit(X_train,y_train)#Here we fit training data to Random Forest Regressor
        fit4 = self.gbr.fit(X_train,y_train)#Here we fit training data to Gradient Boosting Regressor

        #printing the results
        
        print("Accuracy Score of Linear regression on train set",fit1.score(X_train,y_train)*100)
        print("Accuracy Score of Decision Tree on train set",fit2.score(X_train,y_train)*100)
        print("Accuracy Score of Random Forests on train set",fit3.score(X_train,y_train)*100)
        print("Accuracy Score of Gradient Boosting on train set",fit4.score(X_train,y_train)*100)

        return

        
    
