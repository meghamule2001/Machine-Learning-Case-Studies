class Student:
    def __init__(self,str,a,b,c):
        self.name = str
        self.m1 = a
        self.m2 = b
        self.m3 = c

    def __eq__(self,other):
        print("Inside equal method")
        if self.m1 == other.m1 and self.m2 == other.m2 and self.m3 == other.m3:
            return True
        else:
            return False

def main():

    obj1 = Student("Megha",56,89,78)
    obj2 = Student("Chakuli",45,89,90)

    if obj1 == obj2:
        print("Both the students are same")
    else:
        print("Both the students are different")

if __name__=="__main__":
    main()