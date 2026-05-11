from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Example_A:

    def __init__(self, a: str):
        self.a = a
        
        pass
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a


    def getAs(self) :
        # TODO: Implement getAs method
        pass

class B:

    pass
class Example_Bb(B):

    pass
class Example_Ba(B):

    def __init__(self, ba: str):
        self.ba = ba
        
        pass
    @property
    def ba(self):
        return self.__ba

    @ba.setter
    def ba(self, ba: str):
        self.__ba = ba


class Example_B:

    def __init__(self, b: str):
        self.b = b
        
        pass
    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b


    def getBs(self) :
        # TODO: Implement getBs method
        pass
