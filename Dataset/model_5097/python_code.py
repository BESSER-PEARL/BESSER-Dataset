from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Component:

    pass
class testport_Base(Component):

    pass
class testport_Required:

    pass
class testport_Component(ABC):

    def __init__(self, name: str, testport_Component: set["testport_Required"] = None):
        self.name = name
        self.testport_Component = testport_Component if testport_Component is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def testport_Component(self):
        return self.__testport_Component

    @testport_Component.setter
    def testport_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testport_Component__testport_Component", None)
        self.__testport_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testport_Required"):
                    opp_val = getattr(item, "testport_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "testport_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testport_Required"):
                    opp_val = getattr(item, "testport_Required", None)
                    
                    setattr(item, "testport_Required", self)
                    
