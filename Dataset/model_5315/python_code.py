from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class N:

    pass
class refinher2_Y(N):

    pass
class refinher2_H(N):

    pass
class M:

    pass
class A:

    pass
class refinher2_DG:

    pass
class E:

    pass
class refinher2_CE(E, A):

    pass
class refinher2_DR(E):

    pass
class CE:

    pass
class refinher2_DC(CE):

    pass
class refinher2_DL(CE):

    pass
class refinher2_DNamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class refinher2_M:

    pass
class DNamedElement:

    pass
class refinher2_AB(DNamedElement):

    pass
class refinher2_BB(DNamedElement):

    pass
class refinher2_A(DNamedElement):

    pass
class refinher2_N(M, DNamedElement, A):

    pass
class refinher2_E(DNamedElement):

    pass