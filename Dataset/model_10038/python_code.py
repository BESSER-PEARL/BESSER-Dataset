from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class t2_Son(Person):

    pass
class t2_Dad(Person):

    pass
class t2_Person(ABC):

    def __init__(self, age: int):
        self.age = age
        
        pass
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

