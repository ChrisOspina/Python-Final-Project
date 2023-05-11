import pandas as pd # For data manipulation and analysis
import matplotlib.pyplot as plt # Plotting library for Python programming language and it's numerical mathematics extension NumPy
import seaborn as sns   # Provides a high level interface for drawing attractive and informative statistical graphics
from sklearn.preprocessing import LabelEncoder as lr

class EDA:
    def __init__(self, dataset_path,train):
        self.dataset_path = dataset_path
        self.train = train
    
    def plot_histogram(self):
        '''This method plots histogram'''
        try:
            sns.histplot(data=self.df, x="sepal_length_cm", hue="species", kde=True)
            plt.show()
        except AttributeError:
            print("Dataset not loaded. Please load the dataset first.")

    def plot_distplot(self):
            '''This method plots distplot'''
            sns.distplot(self.train["Purchase"],color='r')
            plt.title("Purchase Distribution")
            plt.show()

    def plot_boxplot(self):
          '''This method plots distplot'''
          sns.boxplot(self.train["Purchase"])
          plt.title("Boxplot of Purchase")
          plt.show()

    def maritial_status(self):
         '''This method produces a countplot using maritial status as a defining column '''
         sns.countplot(self.dataset_path['Marital_Status'])
         plt.show()
         self.train.groupby("Marital_Status").mean()["Purchase"]
         plt.title("Marital_Status and Purchase Analysis")
         plt.show()

    def occupation(self):
         '''This method produces countplot using occupation as a defining column'''
         plt.figure(figsize=(18,5))
         sns.countplot(self.train['Occupation'])
         plt.show()
         occup = pd.DataFrame(self.train.groupby("Occupation").mean()["Purchase"])
         occup
         occup.plot(kind='bar',figsize=(15,5))
         plt.title("Occupation and Purchase Analysis")
         plt.show()

    def city_category(self):
         '''This method does the same thing as the two methods above but for city category
         and we are making a bar graph'''
         sns.countplot(self.train['City_Category'])
         plt.show()
         self.train.groupby("City_Category").mean()["Purchase"].plot(kind='bar')
         plt.title("City Category and Purchase Analysis")
         plt.show()

    def Stay_In_Current_City_Years(self):
         '''This method creates a bargraph denoting how long a customer has lived in his/her current
         city'''
         sns.countplot(self.train['Stay_In_Current_City_Years'])
         plt.show()
         self.train.groupby("Stay_In_Current_City_Years").mean()["Purchase"].plot(kind='bar')
         plt.title("Stay_In_Current_City_Years and Purchase Analysis")
         plt.show()
    
    def Age(self):
         '''This method produces a bar graph displaying mean distribution of various age
         groups 18+'''
         sns.countplot(self.train['Age'])
         plt.title('Distribution of Age')
         plt.xlabel('Different Categories of Age')
         plt.show()
         self.train.groupby("Age").sum()["Purchase"].plot(kind='bar')
         plt.title("Age and Purchase Analysis")
         plt.show()
    
    def product_category(self, categorynum):
        '''We have three product categories and instead of
    repeating the same code for each, we have created just one method to create
    a bar graph. the category num parameter will allow this method to identify the 
    product category'''

        if categorynum > 0 and categorynum < 4:
            category = 'Product_Category' + str(categorynum)

            plt.figure(figsize=(18, 5))
            sns.countplot(self.train[category])
            plt.show()

            # For a purchase mean analysis
            self.train.groupby('category').mean()['Purchase'].plot(kind='bar', figsize=(18, 5))
            plt.title(category + "and Purchase Mean Analysis")
            plt.show()

            # For a purchase sum analysis
            self.train.groupby('category').sum()['Purchase'].plot(kind='bar', figsize=(18, 5))
            plt.title(category + "and Purchase Sum Analysis")
            plt.show()
        else:
            print("Error: There are only three product categories")

         
    def heatmap(self):
         '''produces the heat map based on statistical correlation'''
         sns.heatmap(self.train.corr(),annot=True)
         plt.show()
