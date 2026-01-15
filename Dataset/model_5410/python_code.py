from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Dependency:

    pass
class dynamicFaultTree_Sequence(Dependency):

    pass
class Gate:

    pass
class dynamicFaultTree_PAND(Gate):

    pass
class dynamicFaultTree_POR(Gate):

    pass
class dynamicFaultTree_XOR(Gate):

    pass
class dynamicFaultTree_Spare(Gate):

    pass
class dynamicFaultTree_OR(Gate):

    pass
class dynamicFaultTree_AND(Gate):

    pass
class dynamicFaultTree_FunctionalDependency(Dependency):

    pass
class Element:

    pass
class dynamicFaultTree_Event(Element):

    pass
class dynamicFaultTree_Gate(Element):

    pass
class dynamicFaultTree_Element(ABC):

    def __init__(self, name: str, probability: float, sequencePosition: int, elementID: int):
        self.name = name
        self.probability = probability
        self.sequencePosition = sequencePosition
        self.elementID = elementID
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def elementID(self) -> int:
        return self.__elementID

    @elementID.setter
    def elementID(self, elementID: int):
        self.__elementID = elementID

    @property
    def sequencePosition(self) -> int:
        return self.__sequencePosition

    @sequencePosition.setter
    def sequencePosition(self, sequencePosition: int):
        self.__sequencePosition = sequencePosition

    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

class dynamicFaultTree_Dependency(Element):

    pass
class dynamicFaultTree_TopLevelEvent(Element):

    pass
class dynamicFaultTree_DFT:

    def __init__(self, name: str, dynamicFaultTree_DFT: "dynamicFaultTree_TopLevelEvent" = None, dynamicFaultTree_DFT2: set["dynamicFaultTree_Dependency"] = None):
        self.name = name
        self.dynamicFaultTree_DFT = dynamicFaultTree_DFT
        self.dynamicFaultTree_DFT2 = dynamicFaultTree_DFT2 if dynamicFaultTree_DFT2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dynamicFaultTree_DFT2(self):
        return self.__dynamicFaultTree_DFT2

    @dynamicFaultTree_DFT2.setter
    def dynamicFaultTree_DFT2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dynamicFaultTree_DFT__dynamicFaultTree_DFT2", None)
        self.__dynamicFaultTree_DFT2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dynamicFaultTree_Dependency"):
                    opp_val = getattr(item, "dynamicFaultTree_Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "dynamicFaultTree_Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dynamicFaultTree_Dependency"):
                    opp_val = getattr(item, "dynamicFaultTree_Dependency", None)
                    
                    setattr(item, "dynamicFaultTree_Dependency", self)
                    

    @property
    def dynamicFaultTree_DFT(self):
        return self.__dynamicFaultTree_DFT

    @dynamicFaultTree_DFT.setter
    def dynamicFaultTree_DFT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dynamicFaultTree_DFT__dynamicFaultTree_DFT", None)
        self.__dynamicFaultTree_DFT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dynamicFaultTree_TopLevelEvent"):
                opp_val = getattr(old_value, "dynamicFaultTree_TopLevelEvent", None)
                if opp_val == self:
                    setattr(old_value, "dynamicFaultTree_TopLevelEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dynamicFaultTree_TopLevelEvent"):
                opp_val = getattr(value, "dynamicFaultTree_TopLevelEvent", None)
                setattr(value, "dynamicFaultTree_TopLevelEvent", self)
