import sys
def customerManager():
    while(True):
        print("-------------------------")
        print("1. New Customer")
        print("2. All Customers")
        print("3. Search Customer")
        print("4. Edit Customer")
        print("5. Delete Customer")
        print("0. Exit")
        choice2 = int(input("Enter your choice: "))
        if choice2 == 1:
            print("1. Add New Customer")
        elif choice2 == 2:
            print("2. All Customer")
        elif choice2 == 3:
            print("3. Search Customer")
        elif choice2 == 4:
            print("4. Edit Customer")
        elif choice2 == 5:
            print("5. Delete Customer")
        elif choice2 == 0:
            break
        else:
            print("Out of Range")

while(True):
    print("------------Main Menu------------")
    print("1. Customer")
    print("2.Driver")
    print("3.Trip")
    print("0.Exit")
    choice1 = int(input("Enter your choice: "))
    if choice1 == 1:
        print("1. New Customer")
        customerManager()
    elif choice1 == 2:
        print("2. All Customer")
    elif choice1 == 3:
        print("3. Edit Customer")
    elif choice1 == 0:
        print("Bye")
        sys.exit()
    else:
        print("Out of Range")

