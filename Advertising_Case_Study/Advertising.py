
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def MeanData(arr):
    size = len(arr)
    sum = 0
    for i in range(size):
         sum = sum + arr[i]

    return (sum / size)

def Advertising(path):
    dataset = pd.read_csv(path)
    print("Size of dataset is : ",dataset.shape)

    TV = dataset.TV
    radio = dataset.radio
    newspaper = dataset.newspaper

    S = TV+radio+newspaper
    X = dataset(S)
    Y = dataset["sales"]

    print("Length of Independent variable : ",len(X))
    print("Length of Dependent variable : ",len(Y))

    X_Mean = MeanData(X)
    Y_Mean = MeanData(Y)

    print("Mean of X intercept : ",X_Mean)
    print("Mean of Y intercept : ",Y_Mean)

    # find slope
    numerator = 0
    denomenator = 0

    for i in range(X):
        numerator = numerator + ((X[i] - X_Mean) * (Y[i] - Y_Mean))
        denomenator = denomenator + (Y[i] - Y_Mean)

    m = (numerator / denomenator)
    print("Value of slope is : ",m)
    # find c = y - mx
    c = Y_Mean - (m*X_Mean)
    print("Value of Y intercept is ")

    X_Start = np.min(X) - 200
    X_End = np.min(X) + 200

    x = np.linspace(X_Start,X_End)
    y = m*x + c

    plt.plot(x,y,color = 'r', lebel = 'Line of Regression')
    plt.plot(x,y,color = 'b',label = 'Data Plot')

    plt.xlabel("Advertising mediums")
    plt.ylabel("Sales")

    plt.legend()
    plt.show()

    numerator = 0
    denomenator = 0

    for i in range(X):
        numerator = numerator + (((m*X[i] + c) - Y_Mean) ** 2)
        denomenator = denomenator + (Y[i] - Y_Mean)

    RSquare = numerator / denomenator
    print("Value of R square is : ",RSquare)

def main():
    print("Enter the csv file path : ")
    path = input()

    Advertising(path)

if __name__=="__main__":
    main()
