from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class A:

    pass
class tderived_A2(A):

    pass
class B:

    pass
class tderived_B2(B):

    def __init__(self, anotherName: str):
        self.anotherName = anotherName
        
    @property
    def anotherName(self) -> str:
        return self.__anotherName

    @anotherName.setter
    def anotherName(self, anotherName: str):
        self.__anotherName = anotherName

class tderived_D:

    pass