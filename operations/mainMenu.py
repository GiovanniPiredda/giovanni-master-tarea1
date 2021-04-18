from operations import sourceData

def displayMenu():
    print("[0] Exit the program")
    print("[1] Refresh source data")
    print("[2] Compare two countries")

displayMenu()
option = int(input("What do you want to do: "))

while option != 0:

    if option == 1:
        print()
        print("Starting downloading data...")
        sourceData.updateData()
        print()
        print("Data downloaded successfuly.")

    elif option == 2:
        print("Not implemented yet. Coming soon :)")

    else:
        print("Please choose a valid option.")

    print()
    displayMenu()
    option = int(input("What do you want to do: "))

print("Thanks for using the program.\nGood bye! :D")