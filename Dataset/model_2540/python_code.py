from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Itf2:

    pass
class Interface3:

    pass
class test_Interface3(ABC):

    pass
class test_Itf2(ABC):

    pass
class test_Itf1(ABC):

    pass
class ClassB:

    pass
class Itf1:

    pass
class test_ClassD(Itf1, Itf2, Interface3):

    pass
class test_ClassB(Itf1):

    pass
class test_ClassC(ClassB):

    pass
class test_ClassA:

    pass
class test_Interface4(ABC):

    pass
class test_ClassF:

    pass
class ClassC:

    pass
class test_ClassE(ClassC, Interface3):

    pass