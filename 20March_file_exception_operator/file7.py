def main():
    name = input("Enter the file name that you want to create : ")

    fobj = open(name, "r")

    print("Data from file is : ")
    for Data in fobj:
        print(Data, end="")


if __name__ == "__main__":
    main()