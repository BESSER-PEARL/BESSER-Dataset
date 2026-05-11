from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class factorydeclorder_D:

    pass
class factorydeclorder_B:

    def __init__(self, fb: str):
        self.fb = fb
        
        pass
    @property
    def fb(self):
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
class factorydeclorder_A(B, D):

    def __init__(self, fa: int):
        self.fa = fa
        
        pass
    @property
    def fa(self):
        return self.__fa

    @fa.setter
    def fa(self, fa: int):
        self.__fa = fa


class factorydeclorder_C(B, A):

    def __init__(self, fc: bool):
        self.fc = fc
        
        pass
    @property
    def fc(self):
        return self.__fc

    @fc.setter
    def fc(self, fc: bool):
        self.__fc = fc

