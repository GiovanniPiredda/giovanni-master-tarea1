from operations import sourceData

def displayMenu():
    print("[0] Exit the program")
    print("[1] Refresh source data")
    print("[2] Synthetic global report")
    print("[3] Country details")

displayMenu()
option = int(input("What do you want to do: "))

while option != 0:

    #Refresh source data
    if option == 1:
        print()
        print("Starting downloading data...")
        sourceData.updateData()
        print()
        print("Data downloaded successfuly.")

    #Synthetic global report
    elif option == 2:
        print("Not implemented yet. Coming soon :)")

    #Country details
    elif option == 3:
        print("Not implemented yet. Coming soon :)")

    #Countries comparison
    elif option == 4:
        print("Not implemented yet. Coming soon :)")

    #Invalid option message
    else:
        print("Please choose a valid option.")

    print()
    displayMenu()
    option = int(input("What do you want to do: "))

print("Thanks for using the program.\nGood bye! :D")