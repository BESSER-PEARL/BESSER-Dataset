from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class M:

    pass
class A:

    pass
class N:

    pass
class refinher2_Y(N):

    pass
class refinher2_H(N):

    pass
class CE:

    pass
class refinher2_DL(CE):

    pass
class refinher2_DNamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class refinher2_M:

    pass
class DNamedElement:

    pass
class refinher2_A(DNamedElement):

    pass
class refinher2_AB(DNamedElement):

    pass
class refinher2_N(M, A, DNamedElement):

    pass
class refinher2_E(DNamedElement):

    pass
class refinher2_DG:

    pass
class refinher2_DC(CE):

    pass
class E:

    pass
class refinher2_CE(A, E):

    pass
class refinher2_DR(E):

    pass
class refinher2_BB(DNamedElement):

    pass