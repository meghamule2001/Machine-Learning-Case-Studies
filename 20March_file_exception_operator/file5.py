def main():
    name = input("Enter the file name that you want to create : ")

    fobj = open(name, "r")

    print("Single line of file  ")
    print(fobj.readline())


if __name__ == "__main__":
    main()