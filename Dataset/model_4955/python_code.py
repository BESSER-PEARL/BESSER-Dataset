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
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class NamedElement:

    pass
class positionmm_Counter(NamedElement):

    def __init__(self, script: str, position: int):
        self.script = script
        self.position = position
        
        pass
    @property
    def script(self):
        return self.__script

    @script.setter
    def script(self, script: str):
        self.__script = script


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

