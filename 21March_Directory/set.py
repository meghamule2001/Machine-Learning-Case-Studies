
def main():
    arr = {10,20.5,"Hello",10}

    print(type(arr))

    print(arr)

    print(len(arr))

    for value in arr:
        print(value)

    if "Hello" in arr:
        print("Hello is there")

    arr.add(20)
    print(arr)

    arr.remove(20)
    print(arr)

    arr.discard(20.5)
    print(arr)

    # pop use karu naye because unpredictable result milto

    # arr.remove(120)
    # print(arr)
    # error det : KeyError: 120

    arr.discard(120)
    print(arr)
    # ignore karun pudhe run hot
if __name__=="__main__":
    main()