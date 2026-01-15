from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TypeB_BDoubleElement:

    def __init__(self, doubleValue: float):
        self.doubleValue = doubleValue
        
    @property
    def doubleValue(self) -> float:
        return self.__doubleValue

    @doubleValue.setter
    def doubleValue(self, doubleValue: float):
        self.__doubleValue = doubleValue

class TypeB_BStringElement:

    def __init__(self, stringValue: str):
        self.stringValue = stringValue
        
    @property
    def stringValue(self) -> str:
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue
