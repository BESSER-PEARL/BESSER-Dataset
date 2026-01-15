from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ExtensionDefinitionKind(Enum):
    Association = "Association"
    Generalization = "Generalization"
    MultiGeneralization = "MultiGeneralization"
    Fusion = "Fusion"


############################################
# Definition of Classes
############################################

class facademapping_EObject:

    pass
class facademapping_Mapping:

    pass
class facademapping_FacadeMappping:

    pass
class Mapping:

    pass
class facademapping_StereotypedMapping(Mapping):

    def __init__(self, kind: str, facademapping_StereotypedMapping: set["facademapping_EObject"] = None):
        self.kind = kind
        self.facademapping_StereotypedMapping = facademapping_StereotypedMapping if facademapping_StereotypedMapping is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def facademapping_StereotypedMapping(self):
        return self.__facademapping_StereotypedMapping

    @facademapping_StereotypedMapping.setter
    def facademapping_StereotypedMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_facademapping_StereotypedMapping__facademapping_StereotypedMapping", None)
        self.__facademapping_StereotypedMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "facademapping_EObject5"):
                    opp_val = getattr(item, "facademapping_EObject5", None)
                    
                    if opp_val == self:
                        setattr(item, "facademapping_EObject5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "facademapping_EObject5"):
                    opp_val = getattr(item, "facademapping_EObject5", None)
                    
                    setattr(item, "facademapping_EObject5", self)
                    
