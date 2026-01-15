from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StateType(Enum):
    SIMPLE = "SIMPLE"
    INITIAL = "INITIAL"
    FINAL = "FINAL"
class ActionMode(Enum):
    ENTRY = "ENTRY"
    EXIT = "EXIT"


############################################
# Definition of Classes
############################################

class cstat1_EClass0:

    pass
class cstat1_AbstractState(ABC):

    def __init__(self, type: str, id: str, cstat1_AbstractState13: set["cstat1_Action"] = None, cstat1_AbstractState: "cstat1_Transition" = None, cstat1_AbstractState8: "cstat1_Transition" = None, cstat1_AbstractState10: set["cstat1_Transition"] = None):
        self.type = type
        self.id = id
        self.cstat1_AbstractState13 = cstat1_AbstractState13 if cstat1_AbstractState13 is not None else set()
        self.cstat1_AbstractState = cstat1_AbstractState
        self.cstat1_AbstractState8 = cstat1_AbstractState8
        self.cstat1_AbstractState10 = cstat1_AbstractState10 if cstat1_AbstractState10 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def cstat1_AbstractState10(self):
        return self.__cstat1_AbstractState10

    @cstat1_AbstractState10.setter
    def cstat1_AbstractState10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cstat1_AbstractState__cstat1_AbstractState10", None)
        self.__cstat1_AbstractState10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cstat1_Transition11"):
                    opp_val = getattr(item, "cstat1_Transition11", None)
                    
                    if opp_val == self:
                        setattr(item, "cstat1_Transition11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cstat1_Transition11"):
                    opp_val = getattr(item, "cstat1_Transition11", None)
                    
                    setattr(item, "cstat1_Transition11", self)
                    

    @property
    def cstat1_AbstractState(self):
        return self.__cstat1_AbstractState

    @cstat1_AbstractState.setter
    def cstat1_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cstat1_AbstractState__cstat1_AbstractState", None)
        self.__cstat1_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cstat1_Transition"):
                opp_val = getattr(old_value, "cstat1_Transition", None)
                if opp_val == self:
                    setattr(old_value, "cstat1_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cstat1_Transition"):
                opp_val = getattr(value, "cstat1_Transition", None)
                setattr(value, "cstat1_Transition", self)

    @property
    def cstat1_AbstractState13(self):
        return self.__cstat1_AbstractState13

    @cstat1_AbstractState13.setter
    def cstat1_AbstractState13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cstat1_AbstractState__cstat1_AbstractState13", None)
        self.__cstat1_AbstractState13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cstat1_Action"):
                    opp_val = getattr(item, "cstat1_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "cstat1_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cstat1_Action"):
                    opp_val = getattr(item, "cstat1_Action", None)
                    
                    setattr(item, "cstat1_Action", self)
                    

    @property
    def cstat1_AbstractState8(self):
        return self.__cstat1_AbstractState8

    @cstat1_AbstractState8.setter
    def cstat1_AbstractState8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cstat1_AbstractState__cstat1_AbstractState8", None)
        self.__cstat1_AbstractState8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cstat1_Transition7"):
                opp_val = getattr(old_value, "cstat1_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "cstat1_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cstat1_Transition7"):
                opp_val = getattr(value, "cstat1_Transition7", None)
                setattr(value, "cstat1_Transition7", self)

class cstat1_Transition:

    def __init__(self, guard: str, event: str, cstat1_Transition: "cstat1_AbstractState" = None, cstat1_Transition7: "cstat1_AbstractState" = None, cstat1_Transition11: "cstat1_AbstractState" = None):
        self.guard = guard
        self.event = event
        self.cstat1_Transition = cstat1_Transition
        self.cstat1_Transition7 = cstat1_Transition7
        self.cstat1_Transition11 = cstat1_Transition11
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def cstat1_Transition(self):
        return self.__cstat1_Transition

    @cstat1_Transition.setter
    def cstat1_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cstat1_Transition__cstat1_Transition", None)
        self.__cstat1_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cstat1_AbstractState"):
                opp_val = getattr(old_value, "cstat1_AbstractState", None)
                if opp_val == self:
                    setattr(old_value, "cstat1_AbstractState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cstat1_AbstractState"):
                opp_val = getattr(value, "cstat1_AbstractState", None)
                setattr(value, "cstat1_AbstractState", self)

    @property
    def cstat1_Transition7(self):
        return self.__cstat1_Transition7

    @cstat1_Transition7.setter
    def cstat1_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cstat1_Transition__cstat1_Transition7", None)
        self.__cstat1_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cstat1_AbstractState8"):
                opp_val = getattr(old_value, "cstat1_AbstractState8", None)
                if opp_val == self:
                    setattr(old_value, "cstat1_AbstractState8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cstat1_AbstractState8"):
                opp_val = getattr(value, "cstat1_AbstractState8", None)
                setattr(value, "cstat1_AbstractState8", self)

    @property
    def cstat1_Transition11(self):
        return self.__cstat1_Transition11

    @cstat1_Transition11.setter
    def cstat1_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cstat1_Transition__cstat1_Transition11", None)
        self.__cstat1_Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cstat1_AbstractState10"):
                opp_val = getattr(old_value, "cstat1_AbstractState10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cstat1_AbstractState10"):
                opp_val = getattr(value, "cstat1_AbstractState10", None)
                if opp_val is None:
                    setattr(value, "cstat1_AbstractState10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cstat1_Action:

    def __init__(self, expression: str, mode: str, cstat1_Action: "cstat1_AbstractState" = None):
        self.expression = expression
        self.mode = mode
        self.cstat1_Action = cstat1_Action
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def cstat1_Action(self):
        return self.__cstat1_Action

    @cstat1_Action.setter
    def cstat1_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cstat1_Action__cstat1_Action", None)
        self.__cstat1_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cstat1_AbstractState13"):
                opp_val = getattr(old_value, "cstat1_AbstractState13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cstat1_AbstractState13"):
                opp_val = getattr(value, "cstat1_AbstractState13", None)
                if opp_val is None:
                    setattr(value, "cstat1_AbstractState13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cstat1_StateChart:

    pass
class AbstractState:

    pass
class cstat1_State(AbstractState):

    pass
class cstat1_SubState2(AbstractState):

    pass
class cstat1_SubState1(AbstractState):

    pass