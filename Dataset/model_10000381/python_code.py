from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Trapezoidal:

    def __init__(self, D: float, E: float):
        self.D = D
        self.E = E
        
        pass
    @property
    def E(self):
        return self.__E
    @E.setter
    def E(self, E: float):
        self.__E = E

    @property
    def D(self):
        return self.__D
    @D.setter
    def D(self, D: float):
        self.__D = D



class Triangular:

    def __init__(self, C: float):
        self.C = C
        
        pass
    @property
    def C(self):
        return self.__C
    @C.setter
    def C(self, C: float):
        self.__C = C



class Linear:

    pass


class Left_Shoulder:

    pass


class Membership_Function(ABC):

    def __init__(self, HasUID: float, HasName: str, A: float, B: float):
        self.HasUID = HasUID
        self.HasName = HasName
        self.A = A
        self.B = B
        
        pass
    @property
    def B(self):
        return self.__B
    @B.setter
    def B(self, B: float):
        self.__B = B

    @property
    def HasName(self):
        return self.__HasName
    @HasName.setter
    def HasName(self, HasName: str):
        self.__HasName = HasName

    @property
    def HasUID(self):
        return self.__HasUID
    @HasUID.setter
    def HasUID(self, HasUID: float):
        self.__HasUID = HasUID

    @property
    def A(self):
        return self.__A
    @A.setter
    def A(self, A: float):
        self.__A = A



class Right_Shoulder(ABC):

    pass
