from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test_Person:

    def __init__(self, age: int):
        self.age = age
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    def isAgeValid(self, map: str, diag: str) -> bool:
        # TODO: Implement isAgeValid method
        pass
