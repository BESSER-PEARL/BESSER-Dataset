from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class persons_Person:

    def __init__(self, id: str, firstName: str, lastName: str):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName
