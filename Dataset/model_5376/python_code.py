from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class hExamle_4_RHS_X:

    def __init__(self, att1: str):
        self.att1 = att1
        
        pass
    @property
    def att1(self):
        return self.__att1

    @att1.setter
    def att1(self, att1: str):
        self.__att1 = att1

