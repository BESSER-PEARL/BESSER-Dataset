from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class persons_Person:

    def __init__(self, id: str, firstName: str, lastName: str):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        
        pass
    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

