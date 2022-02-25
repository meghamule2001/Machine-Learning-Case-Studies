
class AgeInvalid(Exception):
    def __init__(self,data):
        self.data = data

# 20 21 7 8 9 10 11
def main():
    try:
        age = int(input("Enter your age for PAN card : "))
        if age < 18:
            raise AgeInvalid("Your age is less than 18")

    except AgeInvalid as obj:
        print(obj)

    else:
        print("You will ger the PAN card within 7 working days")


if __name__=="__main__":
    main()