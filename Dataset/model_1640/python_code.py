from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class kiamacs_EObject:

    pass
class kiamacs_BaseCS(ABC):

    pass
class NodeCS:

    pass
class kiamacs_NumCS(NodeCS):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class kiamacs_PlusCS(NodeCS):

    pass
class BaseCS:

    pass
class kiamacs_NodeCS(BaseCS):

    pass
class kiamacs_TopCS(BaseCS):

    pass