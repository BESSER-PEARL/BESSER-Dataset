from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testaccessors_EAcc:

    def __init__(self, b: bool, i: int, bs: bool, is: int):
        self.b = b
        self.i = i
        self.bs = bs
        self.is = is
        
    @property
    def b(self) -> bool:
        return self.__b

    @b.setter
    def b(self, b: bool):
        self.__b = b

    @property
    def bs(self) -> bool:
        return self.__bs

    @bs.setter
    def bs(self, bs: bool):
        self.__bs = bs

    @property
    def is(self) -> int:
        return self.__is

    @is.setter
    def is(self, is: int):
        self.__is = is

    @property
    def i(self) -> int:
        return self.__i

    @i.setter
    def i(self, i: int):
        self.__i = i
