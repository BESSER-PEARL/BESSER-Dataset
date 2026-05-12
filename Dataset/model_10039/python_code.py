from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class t3_Tree:

    def __init__(self, balanced: bool):
        self.balanced = balanced
        
        pass
    @property
    def balanced(self):
        return self.__balanced

    @balanced.setter
    def balanced(self, balanced: bool):
        self.__balanced = balanced

