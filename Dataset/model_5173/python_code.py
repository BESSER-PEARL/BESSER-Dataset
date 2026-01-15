from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SuperClass:

    pass
class testmodel_SubInterface3(SuperClass):

    pass
class testmodel_Target:

    pass
class testmodel_Source:

    pass
class B:

    pass
class testmodel_C(B):

    def __init__(self, c: str):
        self.c = c
        
    @property
    def c(self) -> str:
        return self.__c

    @c.setter
    def c(self, c: str):
        self.__c = c

    def bOp(self):
        # TODO: Implement bOp method
        pass

    def aOp(self):
        # TODO: Implement aOp method
        pass

class A:

    pass
class testmodel_B(A):

    def __init__(self, b: str):
        self.b = b
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    def bOp(self):
        # TODO: Implement bOp method
        pass

class testmodel_A:

    def __init__(self, a: str):
        self.a = a
        
    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    def aOp(self):
        # TODO: Implement aOp method
        pass

class SubClass1:

    pass
class SubAbstractClass1:

    pass
class testmodel_SubInterface7(SubAbstractClass1, SubClass1):

    pass
class testmodel_SubAbstractClass7(SubAbstractClass1, SubClass1):

    pass
class testmodel_SubClass7(SubAbstractClass1, SubClass1):

    pass
class SubInterface2:

    pass
class SubInterface1:

    pass
class testmodel_SubClass5(SubAbstractClass1, SubInterface1):

    pass
class testmodel_SubAbstractClass5(SubAbstractClass1, SubInterface1):

    pass
class testmodel_SubClass4(SubInterface2, SubInterface1):

    pass
class testmodel_SubClass6(SubClass1, SubInterface1):

    pass
class testmodel_SubAbstractClass6(SubClass1, SubInterface1):

    pass
class testmodel_SubInterface6(SubClass1, SubInterface1):

    pass
class testmodel_SubInterface5(SubAbstractClass1, SubInterface1):

    pass
class testmodel_SubAbstractClass4(SubInterface2, SubInterface1):

    pass
class testmodel_SubInterface4(SubInterface2, SubInterface1):

    pass
class testmodel_SubClass3(SuperClass):

    pass
class testmodel_SubAbstractClass3(SuperClass):

    pass
class SuperAbstractClass:

    pass
class testmodel_SubClass2(SuperAbstractClass):

    pass
class testmodel_SubAbstractClass2(SuperAbstractClass):

    pass
class testmodel_SubInterface2(SuperAbstractClass):

    pass
class SuperInterface:

    pass
class testmodel_SubAbstractClass1(SuperInterface):

    pass
class testmodel_SubClass1(SuperInterface):

    pass
class testmodel_SubInterface1(SuperInterface):

    pass
class testmodel_SuperClass:

    pass
class testmodel_SuperAbstractClass(ABC):

    pass
class testmodel_SuperInterface(ABC):

    pass