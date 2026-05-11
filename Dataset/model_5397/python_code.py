from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class B_B:

    def __init__(self, name: str, description1: str, description2: str):
        self.name = name
        self.description1 = description1
        self.description2 = description2
        
        pass
    @property
    def description1(self):
        return self.__description1

    @description1.setter
    def description1(self, description1: str):
        self.__description1 = description1


    @property
    def description2(self):
        return self.__description2

    @description2.setter
    def description2(self, description2: str):
        self.__description2 = description2


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

