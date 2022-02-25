
# ===================
# Imports
# ===================
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show


# ===================
# ML Operation
# ===================
def TitanicLogistic():
    print("Logistic Regression with Titanic Dataset")

    # STEP 1 - Load Data
    titanic_Data = pd.read_csv("MarvellousTitanicDataset.csv")

    # Data Analysis
    print("First 5 record of Dataset \n")
    print(titanic_Data.head())

    print("Total number of records are : ", len(titanic_Data))
    print("Dataset information: \n ", titanic_Data.info())


# =============
# Entry Point
# =============
def main():
    TitanicLogistic()


# ==========
# Starter
# ==========
if (__name__ == "__main__"):
    main()

# ===================
# Imports
# ===================
import numpy as np
import pandas as pd
import seaborn as sb
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show


# ===================
# ML Operation
# ===================
def TitanicLogistic():
    line = "*" * 50
    print("Logistic Regression with Titanic Dataset", line)

    # STEP 1 - Load Data
    titanic_Data = pd.read_csv("MarvellousTitanicDataset.csv")

    # Data Analysis
    print("First 5 record of Dataset \n")
    print(titanic_Data.head())

    print("Total number of records are : ", len(titanic_Data))
    print("Dataset information \n", line)
    print(titanic_Data.info())

    # STEP 2 - Analyse the data in detail
    print("\nVisualization of survived and non-survived passengers \n", line)
    figure()
    countplot(data=titanic_Data, x="Survived")
    show()


# =============
# Entry Point
# =============
def main():
    TitanicLogistic()


# ==========
# Starter
# ==========
if (__name__ == "__main__"):
    main()

