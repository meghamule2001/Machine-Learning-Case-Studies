
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def mnist():
    data = pd.read_csv('mnist.csv')

    df_x = data.iloc[:,1:]  # Labels
    df_y = data.iloc[:,0]   # Pixels

    x_train, x_test, y_train, y_test = train_test_split(df_x,df_y, test_size = 0.2, random_state = 4)

    # descision tree
    dt = DecisionTreeClassifier()
    dt.fit(x_train,y_train)

    print("Testing accuracy using decision tree classifier : ",dt.score(x_test,y_test)*100)
    print("Training accuracy using descision tree classifier : ",dt.score(x_train,y_train)*100)

def main():
    mnist()

if __name__ == "__main__":
    main()
