from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test1unique_ConceptA:

    def __init__(self, bs: str):
        self.bs = bs
        
        pass
    @property
    def bs(self):
        return self.__bs

    @bs.setter
    def bs(self, bs: str):
        self.__bs = bs

