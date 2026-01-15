from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Triangles_AbstractClass(ABC):

    def __init__(self, id: int, name: str, flag: bool):
        self.id = id
        self.name = name
        self.flag = flag
        
    @property
    def flag(self) -> bool:
        return self.__flag

    @flag.setter
    def flag(self, flag: bool):
        self.__flag = flag

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class AbstractClass:

    pass
class Triangles_C_Class(AbstractClass):

    pass
class Triangles_D_Class(AbstractClass):

    pass
class Triangles_B_Class(AbstractClass):

    pass
class Triangles_E_Class(AbstractClass):

    pass
class Triangles_A_Class(AbstractClass):

    pass
class Triangles_Container:

    pass