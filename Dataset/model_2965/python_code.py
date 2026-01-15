from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Attribute_NodeVar:

    def __init__(self, Number: int):
        self.Number = Number
        
    @property
    def Number(self) -> int:
        return self.__Number

    @Number.setter
    def Number(self, Number: int):
        self.__Number = Number

class Attribute_NodeInOut:

    def __init__(self, Number: int):
        self.Number = Number
        
    @property
    def Number(self) -> int:
        return self.__Number

    @Number.setter
    def Number(self, Number: int):
        self.__Number = Number

class Attribute_NodeOut:

    def __init__(self, Number: int):
        self.Number = Number
        
    @property
    def Number(self) -> int:
        return self.__Number

    @Number.setter
    def Number(self, Number: int):
        self.__Number = Number

class Attribute_NodeIn:

    def __init__(self, Number: int):
        self.Number = Number
        
    @property
    def Number(self) -> int:
        return self.__Number

    @Number.setter
    def Number(self, Number: int):
        self.__Number = Number
