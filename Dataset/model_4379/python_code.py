from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class euml_Relations(ABC):

    pass
class euml_NamedElement(ABC):

    def __init__(self, name: str, euml_NamedElement: "euml_Relations" = None):
        self.name = name
        self.euml_NamedElement = euml_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def euml_NamedElement(self):
        return self.__euml_NamedElement

    @euml_NamedElement.setter
    def euml_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_euml_NamedElement__euml_NamedElement", None)
        self.__euml_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "euml_Relations"):
                opp_val = getattr(old_value, "euml_Relations", None)
                if opp_val == self:
                    setattr(old_value, "euml_Relations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "euml_Relations"):
                opp_val = getattr(value, "euml_Relations", None)
                setattr(value, "euml_Relations", self)

class Relations:

    pass
class euml_Realization(Relations):

    pass
class euml_Generalization(Relations):

    pass
class euml_Dependecy(Relations):

    pass
class NamedElement:

    pass
class euml_Operation(NamedElement):

    pass
class euml_Class(NamedElement):

    pass
class euml_Attribute(NamedElement):

    pass
class euml_Package(NamedElement):

    pass