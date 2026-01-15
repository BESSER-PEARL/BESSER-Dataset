from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class root_Test:

    def __init__(self, att1: int, att2: int, name: str):
        self.att1 = att1
        self.att2 = att2
        self.name = name
        
    @property
    def att1(self) -> int:
        return self.__att1

    @att1.setter
    def att1(self, att1: int):
        self.__att1 = att1

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def att2(self) -> int:
        return self.__att2

    @att2.setter
    def att2(self, att2: int):
        self.__att2 = att2
