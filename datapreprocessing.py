class datapreprocessing:
  def __init__(self,train):
    self.train = train
  def perform_eda(self,dset):
    '''This method performs all our data preprocessing 
    in one shot'''
    #the shape function
    print(self.train.shape)
    #checking for null values
    print(self.train.isnull().sum())
    #describe the data
    print(self.train.describe())
    #find unique values
    print(self.train['sentiment'].unique())
 #info function
    def info(self):
      '''This method outputs the information
      of the dataset'''
      return self.dset.info()
