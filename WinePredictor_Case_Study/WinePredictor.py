
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def WinePredictor(path):
    Line = "*"*40
    print(Line)
    print("Wine Predictor dataset : ")
    print(Line)
    dataset = pd.read_csv(path)
    print(dataset)
    print(Line)

    print("Features of Dataset : ")
    print(Line)
    #data = ["Alcohol","Malic_acid","Ash","Alcalinity_of_ash","Magnesium",
     #       "Total_phenols","Flavanoids","Nonflavanoid_phenols",
      #      "Proanthocyanins","Color_intensity","Hue","diluted_wines","Proline"]

    Alcohol = dataset.Alcohol
    Malic_acid = dataset.Malic_acid
    Ash = dataset.Ash
    Alcalinity_of_ash = dataset.Alcalinity_of_ash
    Magnesium = dataset.Magnesium
    Total_phenols = dataset.Total_phenols
    Flavanoids = dataset.Flavanoids
    Nonflavanoid_phenols = dataset.Nonflavanoid_phenols
    Proanthocyanins = dataset.Proanthocyanins
    Color_intensity = dataset.Color_intensity
    Hue = dataset.Hue
    diluted_wines = dataset.diluted_wines
    Proline = dataset.Proline

    features = list(zip(Alcohol,Malic_acid,Ash,Alcalinity_of_ash,Magnesium,
            Total_phenols,Flavanoids,Nonflavanoid_phenols,
            Proanthocyanins,Color_intensity,Hue,diluted_wines,Proline))
    print(features)
    print(Line)

    print("Labels of Dataset : ")
    print(Line)
    Class = dataset.Class

    print(Class)

    features_train,features_test,Class_train,Class_test = train_test_split(features,Class,test_size = 0.3)

    obj = KNeighborsClassifier(n_neighbors = 3)

    obj.fit(features_train,Class_train)

    print("Output of ML : ")
    print(Line)
    output = obj.predict(features_test)
    print(output)
    print(Line)

    Accuracy = accuracy_score(output,Class_test)

    return Accuracy

def main():
    print("*"*40)
    print("Enter the csv file path : ")
    path = input()

    iRet = WinePredictor(path)

    print("*"*40)
    print("Accuracy is : ",iRet*100,"%")
    print("*"*40)

if __name__=="__main__":
    main()
