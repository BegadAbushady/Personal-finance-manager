import Models as classes
from Models import Users, self
my_bank = self()



#checking function to check if the input is a number and if it's more than 0
#used for checking many inputs in the project
def checkingnumbers(number):
    while True:
        try:
            number = float(number)
        except ValueError:
            print("That's not a number... Please try again by entering an adequate number.")
            number = input()
            continue
        if number < 0:
            print("It cannot be negative... Please try again by entering an adequate number.")
            number = input()
            continue
        return number
        
choice = 0





while True:

    print("==============================")
    print("   PERSONAL FINANCE MANAGER   ")
    print("==============================\n\n")

    print("Please select an option:")
    print("1. Login")
    print("2. Register")
    print("3. Exit\n")

    choice = input("Please enter your choice:  ")

    
    match choice:
    
        case "1":
            while True:
                print("Login selected\n")
                username = input("Enter username:")
                password = input("Enter password:")
                found = my_bank.login(username, password)
                if found == True:
                    break
                else:
                    while input("Do you wanna try again? (y/n)") not in ['n','y']:
                        print("wrong input")
                        continue
                    if input() == 'n':
                        break
                    else:
                        continue


            
        case "2":
            print("Register selected")
            print("Enter username:")
            username = input()
            print("Enter password:")
            password = input()
            print("Do you wanna put in initial balance? (y/n)")
            response = input()
            initial_balance = 0
            if response == "y":
                initial_blanace = print("Enter initial balance:")
                initial_balance = checkingnumbers(initial_balance)
            my_bank.createaccount(username, password, initial_balance)
        case "3":
            print("Exit selected")
            break
        case _:
            print("Invalid choice")







print("1. View balance")
print("2. Add income")
print("3. Add expense")
print("4. View transactions")
print("5. View spending by category")
print("6. Set budget")
print("7. View budget status")
print("8. Financial summery")
print("9. Exit")

choice2 = input()


match choice2:
    case "1":
        print("View balance selected")
    case "2":
        print("Add income selected")
    case "3":
        print("Add expense selected")
    case "4":
        print("View transactions selected")
    case "5":
        print("View spending by category selected")
    case "6":
        print("Set budget selected")
    case "7":
        print("View budget status selected")
    case "8":
        print("Financial summary selected")
    case "9":
        print("Goodbye!")
    case _:
        print("Invalid choice")
