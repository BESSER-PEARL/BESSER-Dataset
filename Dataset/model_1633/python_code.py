from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractTransition:

    pass
class ptn103_Transition(AbstractTransition):

    pass
class AbstractNode:

    pass
class ptn103_Place(AbstractNode):

    pass
class ptn103_Token:

    pass
class ptn103_AbstractTransition(AbstractNode):

    def __init__(self, guard: str, ptn103_AbstractTransition: "ptn103_Place" = None, ptn103_AbstractTransition9: set["ptn103_Place"] = None):
        self.guard = guard
        self.ptn103_AbstractTransition = ptn103_AbstractTransition
        self.ptn103_AbstractTransition9 = ptn103_AbstractTransition9 if ptn103_AbstractTransition9 is not None else set()
        
    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def ptn103_AbstractTransition(self):
        return self.__ptn103_AbstractTransition

    @ptn103_AbstractTransition.setter
    def ptn103_AbstractTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptn103_AbstractTransition__ptn103_AbstractTransition", None)
        self.__ptn103_AbstractTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptn103_Place5"):
                opp_val = getattr(old_value, "ptn103_Place5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptn103_Place5"):
                opp_val = getattr(value, "ptn103_Place5", None)
                if opp_val is None:
                    setattr(value, "ptn103_Place5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ptn103_AbstractTransition9(self):
        return self.__ptn103_AbstractTransition9

    @ptn103_AbstractTransition9.setter
    def ptn103_AbstractTransition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptn103_AbstractTransition__ptn103_AbstractTransition9", None)
        self.__ptn103_AbstractTransition9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ptn103_Place10"):
                    opp_val = getattr(item, "ptn103_Place10", None)
                    
                    if opp_val == self:
                        setattr(item, "ptn103_Place10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ptn103_Place10"):
                    opp_val = getattr(item, "ptn103_Place10", None)
                    
                    setattr(item, "ptn103_Place10", self)
                    

class ptn103_AbstractNode(ABC):

    def __init__(self, name: str, ptn103_AbstractNode: "ptn103_Place" = None):
        self.name = name
        self.ptn103_AbstractNode = ptn103_AbstractNode
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ptn103_AbstractNode(self):
        return self.__ptn103_AbstractNode

    @ptn103_AbstractNode.setter
    def ptn103_AbstractNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptn103_AbstractNode__ptn103_AbstractNode", None)
        self.__ptn103_AbstractNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptn103_Place3"):
                opp_val = getattr(old_value, "ptn103_Place3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptn103_Place3"):
                opp_val = getattr(value, "ptn103_Place3", None)
                if opp_val is None:
                    setattr(value, "ptn103_Place3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
