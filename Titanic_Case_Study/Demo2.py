
# ===================
# Imports
# ===================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from seaborn import countplot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# ===================
# ML Operation
# ===================
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
    #show()

    print("Visualization according to Gender")
    figure()
    countplot(data = Titanic_Data, x = "Survived", hue = "Sex").set_title("Visualization according to sex")
    #show()
    print(line)

    print("Visualization according to Passenger Class")
    figure()
    countplot(data = Titanic_Data, x = "Survived", hue = "Pclass").set_title("Visualization according to Passenger Class")
    #show()
    print(line)

    print("Survive vs Non-Survive Base on Age")
    figure()
    Titanic_Data["Age"].plot.hist().set_title("Visualization according to age")
    #show()

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
    Pclass = pd.get_dummies(Titanic_Data["Pclass"], drop_first=True)
    print(line)

# Confusion matrix

    # Concat Sex and Pclass field in our dataset

    Titanic_Data = pd.concat([Titanic_Data,Sex,Pclass], axis = 1)
    print("Data after concatination ")
    print(Titanic_Data.head())
    print(line)

    # Removing un-necessary fields

    Titanic_Data.drop(["Sex","sibsp","Parch","Embarked"], axis = 1, inplace = True)
    print(line)
    print(Titanic_Data.head())
    print(line)

    # Divide the dataset into x and y

    x = Titanic_Data.drop("Survived", axis = 1) # inplace use karat nahiye mhanun Survived udat nahi only drop hot
    y = Titanic_Data["Survived"]

    # Split the data for training and testing purpose

    x_train, x_test, y_train, y_test = train_test_split(x , y , test_size = 0.5)

    obj = LogisticRegression(max_iter = 2000)

# Step - 4 : Train the Dataset

    obj.fit(x_train, y_train)

# Step - 5 : Test the Dataset

    output = obj.predict(x_test)

    print("Accuracy of the given dataset is : ")
    print(accuracy_score(y_test, output)*100)

# Confusion matrics

    print("Confusion matrix is ")
    print(confusion_matrix(y_test , output))

# =============
# Entry Point
# =============
def main():
    print("Logostic case study")

    TitanicLogistic()

# ==========
# Starter
# ==========
if __name__=="__main__":
    main()