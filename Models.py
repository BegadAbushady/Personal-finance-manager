class Users:


    def __init__(self, username, password,initial_balance=0):
        self._username = username
        self._password = password
        self.balance = initial_balance
        self.transactions_history = []
        self.budgets = {}
        
        

class self:


     def __init__(self):
         self.name = "Personal Finance Bank"
         self.user = ""
         self.users = dict[str, Users]

     def createaccount(self,username, password, initial_balance=0):
         if username not in self.users:
            self.users[username] = self(username, password, initial_balance)
         else:
            print("Username already exists and used")

     def login(self,username, password):
         if username in self.users and self.users[username]._password == password:
            print("Login successful\n\n")
            self.user = username
            return True
         else:
            print("your username or password might be wrong\n\n")
            return False

            

     def logout(self):
         self.user = ""



