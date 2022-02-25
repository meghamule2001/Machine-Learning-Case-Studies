class Student:
    def __init__(self,str,a,b,c):
        self.name = str
        self.m1 = a
        self.m2 = b
        self.m3 = c

    def __eq__(self,other):
        print("Inside equal method")
        return ((self.m1 == other.m1) and (self.m2 == other.m2) and (self.m3 == other.m3))


    def __gt__(self,other):
        print("Inside equal method")
        return ((self.m1 > other.m1) and (self.m2 > other.m2) and (self.m3 > other.m3))

def main():

    obj1 = Student("Megha",56,89,78)
    obj2 = Student("Chakuli",45,89,90)

    if obj1 == obj2:
        print("Both the objects are same")
    else:
        print("Both objects are different")


    if obj1 > obj2:
        print("first object is greater")
    else:
        print("second object is greater")

if __name__=="__main__":
    main()