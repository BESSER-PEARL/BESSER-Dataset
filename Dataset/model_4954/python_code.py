from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TypeScript(Enum):
    PreinstScript = "PreinstScript"
    PostinstScript = "PostinstScript"
    PrermScript = "PrermScript"
    PostrmScript = "PostrmScript"


############################################
# Definition of Classes
############################################

class positionmm_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class positionmm_Counter(NamedElement):

    def __init__(self, position: int, script: str):
        self.position = position
        self.script = script
        
    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def script(self) -> str:
        return self.__script

    @script.setter
    def script(self, script: str):
        self.__script = script
