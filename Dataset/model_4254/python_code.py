from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Person:

    pass
class properties_Employee(Person):

    def __init__(self, hasSalary: int, hasAge: int):
        self.hasSalary = hasSalary
        self.hasAge = hasAge
        
    @property
    def hasAge(self) -> int:
        return self.__hasAge

    @hasAge.setter
    def hasAge(self, hasAge: int):
        self.__hasAge = hasAge

    @property
    def hasSalary(self) -> int:
        return self.__hasSalary

    @hasSalary.setter
    def hasSalary(self, hasSalary: int):
        self.__hasSalary = hasSalary

class properties_Address:

    pass
class properties_Person:

    pass