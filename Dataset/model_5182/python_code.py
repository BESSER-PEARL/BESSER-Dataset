from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TransitionQVT_Element(ABC):

    def __init__(self, id: int, TransitionQVT_Element3: "TransitionQVT_Element" = None, TransitionQVT_Element1: set["TransitionQVT_Element"] = None, TransitionQVT_Element: "TransitionQVT_Root" = None):
        self.id = id
        self.TransitionQVT_Element3 = TransitionQVT_Element3
        self.TransitionQVT_Element1 = TransitionQVT_Element1 if TransitionQVT_Element1 is not None else set()
        self.TransitionQVT_Element = TransitionQVT_Element
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def TransitionQVT_Element3(self):
        return self.__TransitionQVT_Element3

    @TransitionQVT_Element3.setter
    def TransitionQVT_Element3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TransitionQVT_Element__TransitionQVT_Element3", None)
        self.__TransitionQVT_Element3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TransitionQVT_Element1"):
                opp_val = getattr(old_value, "TransitionQVT_Element1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TransitionQVT_Element1"):
                opp_val = getattr(value, "TransitionQVT_Element1", None)
                if opp_val is None:
                    setattr(value, "TransitionQVT_Element1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TransitionQVT_Element(self):
        return self.__TransitionQVT_Element

    @TransitionQVT_Element.setter
    def TransitionQVT_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TransitionQVT_Element__TransitionQVT_Element", None)
        self.__TransitionQVT_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TransitionQVT_Root"):
                opp_val = getattr(old_value, "TransitionQVT_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TransitionQVT_Root"):
                opp_val = getattr(value, "TransitionQVT_Root", None)
                if opp_val is None:
                    setattr(value, "TransitionQVT_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TransitionQVT_Element1(self):
        return self.__TransitionQVT_Element1

    @TransitionQVT_Element1.setter
    def TransitionQVT_Element1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TransitionQVT_Element__TransitionQVT_Element1", None)
        self.__TransitionQVT_Element1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransitionQVT_Element3"):
                    opp_val = getattr(item, "TransitionQVT_Element3", None)
                    
                    if opp_val == self:
                        setattr(item, "TransitionQVT_Element3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransitionQVT_Element3"):
                    opp_val = getattr(item, "TransitionQVT_Element3", None)
                    
                    setattr(item, "TransitionQVT_Element3", self)
                    

class TransitionQVT_Root:

    pass
class Element:

    pass
class TransitionQVT_C(Element):

    def __init__(self, c: str):
        self.c = c
        
    @property
    def c(self) -> str:
        return self.__c

    @c.setter
    def c(self, c: str):
        self.__c = c

class TransitionQVT_B(Element):

    def __init__(self, boss: str):
        self.boss = boss
        
    @property
    def boss(self) -> str:
        return self.__boss

    @boss.setter
    def boss(self, boss: str):
        self.__boss = boss

class TransitionQVT_A(Element):

    def __init__(self, height: float, reduction: str):
        self.height = height
        self.reduction = reduction
        
    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def reduction(self) -> str:
        return self.__reduction

    @reduction.setter
    def reduction(self, reduction: str):
        self.__reduction = reduction
