from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class Persons_Female(Person):

    pass
class Persons_Male(Person):

    pass
class Persons_Person(ABC):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

