from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class B:

    pass
class Example_Bb(B):

    pass
class Example_Ba(B):

    def __init__(self, ba: str):
        self.ba = ba
        
    @property
    def ba(self) -> str:
        return self.__ba

    @ba.setter
    def ba(self, ba: str):
        self.__ba = ba

class Example_B:

    def __init__(self, b: str):
        self.b = b
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    def getBs(self) -> str:
        # TODO: Implement getBs method
        pass

class Example_A:

    def __init__(self, a: str):
        self.a = a
        
    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    def getAs(self) -> str:
        # TODO: Implement getAs method
        pass
