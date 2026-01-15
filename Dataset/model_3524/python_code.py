from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enum1(Enum):
    LITERAL0 = "LITERAL0"
    LITERAL1 = "LITERAL1"


############################################
# Definition of Classes
############################################

class testenums_Root:

    def __init__(self, enums: str, enum: str):
        self.enums = enums
        self.enum = enum
        
    @property
    def enum(self) -> str:
        return self.__enum

    @enum.setter
    def enum(self, enum: str):
        self.__enum = enum

    @property
    def enums(self) -> str:
        return self.__enums

    @enums.setter
    def enums(self, enums: str):
        self.__enums = enums
