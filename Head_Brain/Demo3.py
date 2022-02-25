import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def MarvellousHeadBrain(Name):
    dataset = pd.read_csv(Name)
    print("Size of our data set is ", dataset.shape)

    X = dataset["Head Size(cm^3)"].values
    Y = dataset["Brain Weight(grams)"].values
    X = X.reshape((-1,1))

    obj = LinearRegression()
    obj.fit(X,Y)

    output = obj.predict(X)
    #Dataset = pd.read_csv("Test.csv")
    #X_new = dataset["Head Size"].values
    #output = obj.predict(X_new)
    #print("Expected Result is : ",output)
    #rsquare = obj.score(X,Y)

    #print(rsquare)

def main():
    MarvellousHeadBrain("Test.csv")

if __name__=="__main__":
    main()