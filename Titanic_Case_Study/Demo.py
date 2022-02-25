
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from seaborn import countplot
import sklearn

def TitanicLogistic():

    line = "*"*50
    print("Inside Logistic function")

# Step 1 - load data
    Titanic_Data = pd.read_csv("MarvellousTitanicDataset.csv")

    print("First five record of dataset : ")
    print(Titanic_Data.head())

    print("Total number of records are")
    print(len(Titanic_Data))
    #print(Titanic_Data.info())

# Step 2 - Analyse the data

    print("Visulization of survived and non-survived pasengers")
    print(line)

    figure()
    countplot(data = Titanic_Data, x = "Survived").set_title("Survived vs non-Survived")
    show()

    print("Visualization according to Gender")
    figure()
    countplot(data = Titanic_Data, x = "Survived", hue = "Sex").set_title("Visualization according to sex")
    show()
    print(line)

    print("Visualization according to Passenger Class",line)
    figure()
    countplot(data = Titanic_Data, x = "Survived", hue = "Pclass").set_title("Visualization according to Passenger Class")
    show()
    print(line)

    print("Survive vs Non-Survive Base on Age")
    figure()
    Titanic_Data["Age"].plot.hist().set_title("Visualization according to age")
    show()

# Step 3 - Data Cleaning
    Titanic_Data.drop("zero", axis = 1, inplace = True)
    print("Data after Column removal")
    print(Titanic_Data.head())
    #print(Titanic_Data.info)

    # pandas get_dummies works like label encoder data rangling (data modification)

    Sex = pd.get_dummies(Titanic_Data["Sex"])
    print(Sex.head())
    print(line)
    #Titanic_Data.drop("zero", axis = 1, inplace = True)
    Sex = pd.get_dummies(Titanic_Data["Sex"], drop_first = True)
    print("Sex column after updation")
    print(line)
    print(Sex.head())

    Pclass = pd.get_dummies(Titanic_Data["Pclass"])
    print(Pclass.head())

# Confusion matrix

def main():
    print("Logostic case study")

    TitanicLogistic()

if __name__=="__main__":
    main()
