from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractTransition:

    pass
class ptntim101_Transition(AbstractTransition):

    def __init__(self, weight: int):
        self.weight = weight
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

class ptntim101_AbstractNode(ABC):

    def __init__(self, name: str, tMin: int, tMax: int, ptntim101_AbstractNode: "ptntim101_Place" = None):
        self.name = name
        self.tMin = tMin
        self.tMax = tMax
        self.ptntim101_AbstractNode = ptntim101_AbstractNode
        
    @property
    def tMax(self) -> int:
        return self.__tMax

    @tMax.setter
    def tMax(self, tMax: int):
        self.__tMax = tMax

    @property
    def tMin(self) -> int:
        return self.__tMin

    @tMin.setter
    def tMin(self, tMin: int):
        self.__tMin = tMin

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ptntim101_AbstractNode(self):
        return self.__ptntim101_AbstractNode

    @ptntim101_AbstractNode.setter
    def ptntim101_AbstractNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptntim101_AbstractNode__ptntim101_AbstractNode", None)
        self.__ptntim101_AbstractNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptntim101_Place3"):
                opp_val = getattr(old_value, "ptntim101_Place3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptntim101_Place3"):
                opp_val = getattr(value, "ptntim101_Place3", None)
                if opp_val is None:
                    setattr(value, "ptntim101_Place3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractNode:

    pass
class ptntim101_AbstractTransition(AbstractNode):

    def __init__(self, guard: str, ptntim101_AbstractTransition: "ptntim101_Place" = None, ptntim101_AbstractTransition9: set["ptntim101_Place"] = None):
        self.guard = guard
        self.ptntim101_AbstractTransition = ptntim101_AbstractTransition
        self.ptntim101_AbstractTransition9 = ptntim101_AbstractTransition9 if ptntim101_AbstractTransition9 is not None else set()
        
    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def ptntim101_AbstractTransition9(self):
        return self.__ptntim101_AbstractTransition9

    @ptntim101_AbstractTransition9.setter
    def ptntim101_AbstractTransition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptntim101_AbstractTransition__ptntim101_AbstractTransition9", None)
        self.__ptntim101_AbstractTransition9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ptntim101_Place10"):
                    opp_val = getattr(item, "ptntim101_Place10", None)
                    
                    if opp_val == self:
                        setattr(item, "ptntim101_Place10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ptntim101_Place10"):
                    opp_val = getattr(item, "ptntim101_Place10", None)
                    
                    setattr(item, "ptntim101_Place10", self)
                    

    @property
    def ptntim101_AbstractTransition(self):
        return self.__ptntim101_AbstractTransition

    @ptntim101_AbstractTransition.setter
    def ptntim101_AbstractTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptntim101_AbstractTransition__ptntim101_AbstractTransition", None)
        self.__ptntim101_AbstractTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptntim101_Place5"):
                opp_val = getattr(old_value, "ptntim101_Place5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptntim101_Place5"):
                opp_val = getattr(value, "ptntim101_Place5", None)
                if opp_val is None:
                    setattr(value, "ptntim101_Place5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ptntim101_Place(AbstractNode):

    pass
class ptntim101_Token:

    pass