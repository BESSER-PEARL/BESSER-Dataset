from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ptn104_Token:

    pass
class AbstractTransition:

    pass
class ptn104_And(AbstractTransition):

    pass
class ptn104_Or(AbstractTransition):

    pass
class ptn104_AbstractNode(ABC):

    def __init__(self, name: str, ptn104_AbstractNode: "ptn104_Place" = None):
        self.name = name
        self.ptn104_AbstractNode = ptn104_AbstractNode
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ptn104_AbstractNode(self):
        return self.__ptn104_AbstractNode

    @ptn104_AbstractNode.setter
    def ptn104_AbstractNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptn104_AbstractNode__ptn104_AbstractNode", None)
        self.__ptn104_AbstractNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptn104_Place3"):
                opp_val = getattr(old_value, "ptn104_Place3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptn104_Place3"):
                opp_val = getattr(value, "ptn104_Place3", None)
                if opp_val is None:
                    setattr(value, "ptn104_Place3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractNode:

    pass
class ptn104_AbstractTransition(AbstractNode):

    def __init__(self, guard: str, ptn104_AbstractTransition: "ptn104_Place" = None, ptn104_AbstractTransition9: set["ptn104_Place"] = None):
        self.guard = guard
        self.ptn104_AbstractTransition = ptn104_AbstractTransition
        self.ptn104_AbstractTransition9 = ptn104_AbstractTransition9 if ptn104_AbstractTransition9 is not None else set()
        
    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def ptn104_AbstractTransition(self):
        return self.__ptn104_AbstractTransition

    @ptn104_AbstractTransition.setter
    def ptn104_AbstractTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptn104_AbstractTransition__ptn104_AbstractTransition", None)
        self.__ptn104_AbstractTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptn104_Place5"):
                opp_val = getattr(old_value, "ptn104_Place5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptn104_Place5"):
                opp_val = getattr(value, "ptn104_Place5", None)
                if opp_val is None:
                    setattr(value, "ptn104_Place5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ptn104_AbstractTransition9(self):
        return self.__ptn104_AbstractTransition9

    @ptn104_AbstractTransition9.setter
    def ptn104_AbstractTransition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptn104_AbstractTransition__ptn104_AbstractTransition9", None)
        self.__ptn104_AbstractTransition9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ptn104_Place10"):
                    opp_val = getattr(item, "ptn104_Place10", None)
                    
                    if opp_val == self:
                        setattr(item, "ptn104_Place10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ptn104_Place10"):
                    opp_val = getattr(item, "ptn104_Place10", None)
                    
                    setattr(item, "ptn104_Place10", self)
                    

class ptn104_Place(AbstractNode):

    pass