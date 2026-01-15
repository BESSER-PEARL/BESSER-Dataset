from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class RootInterface:

    pass
class package1_Child3(RootInterface):

    pass
class RootAbstractClass:

    pass
class package1_Child2(RootAbstractClass):

    pass
class RootClass:

    pass
class package1_Child4(RootInterface, RootClass, RootAbstractClass):

    pass
class package1_Child1(RootClass):

    pass
class package1_RootInterface(ABC):

    pass
class package1_RootAbstractClass(ABC):

    pass
class package1_RootClass:

    pass
class package1_subpackage_Child6(RootClass, RootInterface, RootAbstractClass):

    pass
class package1_subpackage_Child5(RootClass):

    pass
class SubChild:

    pass
class package1_SubChild3(RootClass, SubChild):

    pass
class Child4:

    pass
class package1_subpackage_SubChild2(Child4):

    pass
class package1_SubChild(Child4):

    pass