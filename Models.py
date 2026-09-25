class Users:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    def getattribute(self):
        print("username " + self.__username)
        print("password " + self.__password)