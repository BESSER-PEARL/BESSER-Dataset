from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class oclstdlib_UniqueCollection(ABC):

    pass
class oclstdlib_Set(ABC):

    pass
class oclstdlib_Sequence(ABC):

    pass
class oclstdlib_OrderedSet(ABC):

    pass
class oclstdlib_OrderedCollection(ABC):

    pass
class OclElement:

    pass
class oclstdlib_OclType(OclElement):

    pass
class OclVoid:

    pass
class oclstdlib_OclInvalid(OclVoid):

    pass
class oclstdlib_OclAny(ABC):

    pass
class oclstdlib_Bag(ABC):

    pass
class OclAny:

    pass
class oclstdlib_OclElement(OclAny):

    pass
class oclstdlib_OclMessage(OclAny):

    pass
class oclstdlib_OclSummable(OclAny):

    pass
class oclstdlib_OclState(OclAny):

    pass
class oclstdlib_OclLambda(OclAny):

    pass
class oclstdlib_OclVoid(OclAny):

    pass
class oclstdlib_OclTuple(OclAny):

    pass
class oclstdlib_OclComparable(OclAny):

    pass
class oclstdlib_Collection(OclAny):

    def __init__(self, lower: str, upper: str):
        self.lower = lower
        self.upper = upper
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower
