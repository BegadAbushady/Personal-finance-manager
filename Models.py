class Users:


    def __init__(self, username, password,initial_balance=0):
        self.__username = username
        self.__password = password
        self.balance = initial_balance
        self.transactions_history = {}
        self.budgets = {}
        
        

class Bank:

     user = ""
     def __init__(self):
         self.name = "Personal Finance Bank"
         self.users = {str, Users}

     def createaccount(username, password, initial_balance=0):
         if username not in Bank.users:
            Bank.users[username] = Users(username, password, initial_balance)
         else:
            print("Username already exists and used")

     def login(username, password):
         if username in Bank.users and Bank.users[username].__password == password:
            print("Login successful")
            Bank.user = username
         else:
            print("your username or password might be wrong")

     def logout():
         Bank.user = ""



