class User:
    def __init__(self,name,contact) :
        self.__name=name
        self.__contact=contact
    def get_name(self):
        return self.__name
    def get_contact(self):
        return self.__contact
    def __str__(self):
        return f'User:{self.__name},Contact:{self.__contact}'