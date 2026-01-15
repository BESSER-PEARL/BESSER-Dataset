from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class P:

    pass
class k2_Q(P):

    pass
class M:

    pass
class k2_N(M):

    pass
class k2_G(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class G:

    pass
class k2_M(G):

    pass
class k2_I(G):

    pass
class C:

    pass
class k2_B(C):

    pass
class B:

    pass
class N:

    pass
class A:

    pass
class k2_J(A):

    pass
class k2_X:

    pass
class k2_A(B):

    pass
class k2_P(N):

    pass
class k2_C(G):

    pass