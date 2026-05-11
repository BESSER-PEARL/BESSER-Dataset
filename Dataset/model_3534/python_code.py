from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testaccessors_EAcc:

    def __init__(self, b: bool, i: int, bs: bool, is_: int):
        self.b = b
        self.i = i
        self.bs = bs
        self.is_ = is_
        
        pass
    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: bool):
        self.__b = b


    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, i: int):
        self.__i = i


    @property
    def bs(self):
        return self.__bs

    @bs.setter
    def bs(self, bs: bool):
        self.__bs = bs


    @property
    def is_(self):
        return self.__is_

    @is_.setter
    def is_(self, is_: int):
        self.__is_ = is_

