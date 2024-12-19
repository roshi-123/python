class User:
    def __init__(self):
        self.__name = None
        self.__password = None
        self.__status = "waiting"
        self.__amount = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount