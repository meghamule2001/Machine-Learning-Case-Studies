
from sklearn import tree
# Rough 1
# Smooth 0
# Tennis 1
# Cricket 2

def MarvellousML(weight,surface):
    # Step 1 & 2
    Features = [[35, 1], [47, 1], [90, 0],
                [48, 1], [90, 0], [35, 1],
                [92, 0], [35, 1], [35, 1],
                [35, 1], [96, 0], [43, 1],
                [110, 0], [35, 1], [95, 0]]

    Labele = [1, 1, 2,
              1, 2, 1,
              2, 1, 1,
              1, 2, 1,
              2, 1, 2]

    # Step 3
    dobj = tree.DecisionTreeClassifier()

    # Step 4
    dobj.fit(Features, Labele)

    # Step 5
    result = dobj.predict([[weight,surface]])  # result = dobj.predict([[91,0],[85,0],[40,1]])
                                               # result -> [2,2,1]
    if result == 1:
       print("Your object looks like Tennis ball")
    else:
        print("Your object looks like Cricket ball")


def main():
   print("___________Supervised Machine Learning___________")
   print("Enter weight of object : ")
   weight = int(input())
   print("Enter surface type of object : ")
   surface = input()

   if surface.lower() == "rough":       # Rough  ROUGH  rough  RoUgH -> all gets converted into rough
                                        # by using lower() method
       surface = 1
   elif surface.lower() == "smooth":
       surface = 0
   else:
       print("Invalid input")
       return

   MarvellousML(weight,surface)

if __name__=="__main__":
    main()
