from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class B:

    pass
class tderived_B2(B):

    def __init__(self, anotherName: str):
        self.anotherName = anotherName
        
        pass
    @property
    def anotherName(self):
        return self.__anotherName

    @anotherName.setter
    def anotherName(self, anotherName: str):
        self.__anotherName = anotherName


class tderived_D:

    pass
class A:

    pass
class tderived_A2(A):

    pass