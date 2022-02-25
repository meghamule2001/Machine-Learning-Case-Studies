

def main():
    Employee = {11:{"Name":"Megha","Age":30},21:{"Name": "Anjali","Age":22},51:{"Name":"Namo","Age":23}}

    print("Employee information is : ")
    for eid,einformation in Employee.items():
        print("Employee ID is : ",eid)
        for key in einformation:
            print(key,einformation[key])

if __name__ == "__main__":
    main()