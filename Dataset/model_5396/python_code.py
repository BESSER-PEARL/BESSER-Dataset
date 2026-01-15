from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class B_B:

    def __init__(self, description1: str, description2: str, name: str):
        self.description1 = description1
        self.description2 = description2
        self.name = name
        
    @property
    def description1(self) -> str:
        return self.__description1

    @description1.setter
    def description1(self, description1: str):
        self.__description1 = description1

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description2(self) -> str:
        return self.__description2

    @description2.setter
    def description2(self, description2: str):
        self.__description2 = description2
