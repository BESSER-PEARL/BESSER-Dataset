from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class automation_Automation(NamedElement):

    pass
class automation_Output(NamedElement):

    pass
class automation_Input(NamedElement):

    pass
class automation_Transition(NamedElement):

    pass
class automation_State(NamedElement):

    pass
class automation_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

