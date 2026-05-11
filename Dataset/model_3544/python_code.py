from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class NewEClass3:

    pass
class NewEClass2:

    pass
class multipleinheritence_NewEClass1(NewEClass2, NewEClass3):

    def __init__(self, f1: int):
        self.f1 = f1
        
        pass
    @property
    def f1(self):
        return self.__f1

    @f1.setter
    def f1(self, f1: int):
        self.__f1 = f1


class multipleinheritence_NewEClass5:

    def __init__(self, f5: int):
        self.f5 = f5
        
        pass
    @property
    def f5(self):
        return self.__f5

    @f5.setter
    def f5(self, f5: int):
        self.__f5 = f5


class multipleinheritence_NewEClass4:

    def __init__(self, f4: int):
        self.f4 = f4
        
        pass
    @property
    def f4(self):
        return self.__f4

    @f4.setter
    def f4(self, f4: int):
        self.__f4 = f4


class NewEClass5:

    pass
class NewEClass4:

    pass
class multipleinheritence_NewEClass3(NewEClass5, NewEClass4):

    def __init__(self, f3: int):
        self.f3 = f3
        
        pass
    @property
    def f3(self):
        return self.__f3

    @f3.setter
    def f3(self, f3: int):
        self.__f3 = f3


class multipleinheritence_NewEClass2:

    def __init__(self, f2: int):
        self.f2 = f2
        
        pass
    @property
    def f2(self):
        return self.__f2

    @f2.setter
    def f2(self, f2: int):
        self.__f2 = f2

