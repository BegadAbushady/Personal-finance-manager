import Models as classes
from Models import Users

choice = 0

print("==============================")
print("   PERSONAL FINANCE MANAGER   ")
print("==============================")

print("Please select an option:")
print("1. Login")
print("2. Register")
print("3. Exit")

while True:
 choice = input()
 match choice:
    case "1":
        print("Login selected")
    case "2":
        print("Register selected")
		
        print("Enter username:")
        username = input()
        print("Enter password:")
        password = input()
        x = Users(username, password)
        print(x.getattribute())
        
    case "3":
        print("Exit selected")
    case _ :
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

choice = input()


match choice:
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
