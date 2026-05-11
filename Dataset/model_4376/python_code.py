from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test_Person:

    def __init__(self, age: int):
        self.age = age
        
        pass
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age


    def isAgeValid(self, test_diag, test_map) :
        # TODO: Implement isAgeValid method
        pass
