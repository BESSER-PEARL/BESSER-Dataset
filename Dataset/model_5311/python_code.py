from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TypeB_BDoubleElement:

    def __init__(self, doubleValue: float):
        self.doubleValue = doubleValue
        
        pass
    @property
    def doubleValue(self):
        return self.__doubleValue

    @doubleValue.setter
    def doubleValue(self, doubleValue: float):
        self.__doubleValue = doubleValue


class TypeB_BStringElement:

    def __init__(self, stringValue: str):
        self.stringValue = stringValue
        
        pass
    @property
    def stringValue(self):
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue

