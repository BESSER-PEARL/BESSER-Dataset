from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test1_ConceptA:

    def __init__(self, bs: str):
        self.bs = bs
        
    @property
    def bs(self) -> str:
        return self.__bs

    @bs.setter
    def bs(self, bs: str):
        self.__bs = bs
