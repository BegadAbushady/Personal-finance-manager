class Users:


    users = {}
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        Users.users[self.__username] = self.__password
        balance = 0

