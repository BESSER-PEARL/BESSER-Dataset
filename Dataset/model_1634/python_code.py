from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractTransition:

    pass
class ptn_Transition(AbstractTransition):

    def __init__(self, weight: int):
        self.weight = weight
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

class ptn_AbstractNode(ABC):

    def __init__(self, name: str, tMin: int, tMax: int, ptn_AbstractNode: "ptn_Place" = None):
        self.name = name
        self.tMin = tMin
        self.tMax = tMax
        self.ptn_AbstractNode = ptn_AbstractNode
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def ptn_AbstractNode(self):
        return self.__ptn_AbstractNode

    @ptn_AbstractNode.setter
    def ptn_AbstractNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptn_AbstractNode__ptn_AbstractNode", None)
        self.__ptn_AbstractNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptn_Place3"):
                opp_val = getattr(old_value, "ptn_Place3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptn_Place3"):
                opp_val = getattr(value, "ptn_Place3", None)
                if opp_val is None:
                    setattr(value, "ptn_Place3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ptn_Token:

    pass
class AbstractNode:

    pass
class ptn_AbstractTransition(AbstractNode):

    def __init__(self, guard: str, ptn_AbstractTransition: "ptn_Place" = None, ptn_AbstractTransition9: set["ptn_Place"] = None):
        self.guard = guard
        self.ptn_AbstractTransition = ptn_AbstractTransition
        self.ptn_AbstractTransition9 = ptn_AbstractTransition9 if ptn_AbstractTransition9 is not None else set()
        
    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def ptn_AbstractTransition9(self):
        return self.__ptn_AbstractTransition9

    @ptn_AbstractTransition9.setter
    def ptn_AbstractTransition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptn_AbstractTransition__ptn_AbstractTransition9", None)
        self.__ptn_AbstractTransition9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ptn_Place10"):
                    opp_val = getattr(item, "ptn_Place10", None)
                    
                    if opp_val == self:
                        setattr(item, "ptn_Place10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ptn_Place10"):
                    opp_val = getattr(item, "ptn_Place10", None)
                    
                    setattr(item, "ptn_Place10", self)
                    

    @property
    def ptn_AbstractTransition(self):
        return self.__ptn_AbstractTransition

    @ptn_AbstractTransition.setter
    def ptn_AbstractTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptn_AbstractTransition__ptn_AbstractTransition", None)
        self.__ptn_AbstractTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptn_Place5"):
                opp_val = getattr(old_value, "ptn_Place5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptn_Place5"):
                opp_val = getattr(value, "ptn_Place5", None)
                if opp_val is None:
                    setattr(value, "ptn_Place5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ptn_Place(AbstractNode):

    pass