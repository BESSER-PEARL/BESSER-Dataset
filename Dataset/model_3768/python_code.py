from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_Transition:

    def __init__(self, ls: str, als: str):
        self.ls = ls
        self.als = als
        
        pass
    @property
    def als(self):
        return self.__als

    @als.setter
    def als(self, als: str):
        self.__als = als


    @property
    def ls(self):
        return self.__ls

    @ls.setter
    def ls(self, ls: str):
        self.__ls = ls

