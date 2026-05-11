from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class hExample_3_RHS_X:

    def __init__(self, att1: str, att2: str):
        self.att1 = att1
        self.att2 = att2
        
        pass
    @property
    def att1(self):
        return self.__att1

    @att1.setter
    def att1(self, att1: str):
        self.__att1 = att1


    @property
    def att2(self):
        return self.__att2

    @att2.setter
    def att2(self, att2: str):
        self.__att2 = att2

