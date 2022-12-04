import sys

while(True):
    print("---------Main Menu-------------")
    print("1. Insert Driver")
    print("2. Display all Drivers")
    print("3. Search Driver")
    print("4. Edit Driver")
    print("5. Delete Driver")
    print("0. Exit")
    print("-------------------------------")
    choice = int(input("Enter your choice: "))
    print("-------------------------------")

    if choice == 0:
        print("Bye")
        sys.exit()
    elif choice >= 6 or choice < 0:
        print("Out of Range")
    elif choice == 1:
        print("Insert Driver")
        print("New Customer")
    elif choice == 2:
        print("Display Driver")
    elif choice == 3:
        print("Search Driver")
    elif choice == 4:
        print("Edit Driver")
    elif choice == 5:
        print("Delete Driver")