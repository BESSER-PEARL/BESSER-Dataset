from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test1_ConceptA:

    def __init__(self, bs: str, b: str):
        self.bs = bs
        self.b = b
        
        pass
    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b


    @property
    def bs(self):
        return self.__bs

    @bs.setter
    def bs(self, bs: str):
        self.__bs = bs

