from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_Transition:

    def __init__(self, k: int):
        self.k = k
        
    @property
    def k(self) -> int:
        return self.__k

    @k.setter
    def k(self, k: int):
        self.__k = k

    def f1(self):
        # TODO: Implement f1 method
        pass

    def f2(self):
        # TODO: Implement f2 method
        pass
