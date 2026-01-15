from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TestEnum(Enum):
class SubTestEnum(Enum):


############################################
# Definition of Classes
############################################

class TestPackage_SubPackage_SubTestInterface(ABC):

    pass
class TestPackage_SubPackage_SubTestClass:

    pass
class TestPackage_UberClass(ABC):

    pass
class TestPackage_SuperClass(ABC):

    pass
class UberClass:

    pass
class SuperClass:

    pass
class TestPackage_TestInterface(SuperClass):

    pass
class TestPackage_TestClass(SuperClass, UberClass):

    pass