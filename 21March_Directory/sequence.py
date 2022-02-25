
def main():
    arr = (11,21,23.5,"Hello")
    print(type(arr))

    for i in range(len(arr)):
        print(arr[i])

# not allowed in tuple
    # arr[0] = 12

    # print(arr[0])

    brr = (10,20,30,)
    print("Type of brr is: ",type(arr))

    crr = (40)
    print("Type of crr is : ",type(crr))

    drr = (50,)
    print("Type of drr is : ",type(drr))

if __name__=="__main__":
    main()