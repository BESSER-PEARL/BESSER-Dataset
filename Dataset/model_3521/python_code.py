from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class factorydeclorder_D:

    pass
class factorydeclorder_B:

    def __init__(self, fb: str):
        self.fb = fb
        
    @property
    def fb(self) -> str:
        return self.__fb

    @fb.setter
    def fb(self, fb: str):
        self.__fb = fb

class D:

    pass
class A:

    pass
class B:

    pass
class factorydeclorder_A(D, B):

    def __init__(self, fa: int):
        self.fa = fa
        
    @property
    def fa(self) -> int:
        return self.__fa

    @fa.setter
    def fa(self, fa: int):
        self.__fa = fa

class factorydeclorder_C(A, B):

    def __init__(self, fc: bool):
        self.fc = fc
        
    @property
    def fc(self) -> bool:
        return self.__fc

    @fc.setter
    def fc(self, fc: bool):
        self.__fc = fc
