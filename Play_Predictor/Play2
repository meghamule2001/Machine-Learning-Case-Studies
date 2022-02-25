
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def Predictor(path):
    # Step1
    data = pd.read_csv(path)    # Dataframe 2D array
    print("Dataset loaded succesfully with the size",len(data))

    # Prepare data
    Fetures = ["Whether","Temprature"]
    print("Fetures names are : ",Fetures)

    Whether = data.Whether      # Series    1D array
    Temprature = data.Temprature    # Series
    Play = data.Play    # Series

    lobj = preprocessing.LabelEncoder()
    WhetherX = lobj.fit_transform(Whether)
    TempratureX = lobj.fit_transform(Temprature)
    Label = lobj.fit_transform(Play)

    print("Encoded whether is : ")
    print(WhetherX)

    print("Encoded temprature is : ")
    print(TempratureX)

    #
    features = list(zip(WhetherX,TempratureX))
    # Step 3
    obj = KNeighborsClassifier(n_neighbors = 4)
    obj.fit(features,Label)

    # Step 4
    output = obj.predict([[0,2]])

    if output == 1:
        print("You can play")
    else:
        print("Don't play")

def main():
    print("_____Marvellous Play Predictor_____")
    print("Enter the path of the file which contains dataset")
    path = input()

    Predictor(path)

if __name__=="__main__":
    main()
