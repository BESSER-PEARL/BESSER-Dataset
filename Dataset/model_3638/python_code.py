from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class dfa_Symbol:

    def __init__(self, literal: str, description: str, direction: str, dfa_Symbol12: "dfa_Language" = None, dfa_Symbol: "dfa_Transition" = None):
        self.literal = literal
        self.description = description
        self.direction = direction
        self.dfa_Symbol12 = dfa_Symbol12
        self.dfa_Symbol = dfa_Symbol
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def dfa_Symbol12(self):
        return self.__dfa_Symbol12

    @dfa_Symbol12.setter
    def dfa_Symbol12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfa_Symbol__dfa_Symbol12", None)
        self.__dfa_Symbol12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfa_Language11"):
                opp_val = getattr(old_value, "dfa_Language11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfa_Language11"):
                opp_val = getattr(value, "dfa_Language11", None)
                if opp_val is None:
                    setattr(value, "dfa_Language11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dfa_Symbol(self):
        return self.__dfa_Symbol

    @dfa_Symbol.setter
    def dfa_Symbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfa_Symbol__dfa_Symbol", None)
        self.__dfa_Symbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfa_Transition9"):
                opp_val = getattr(old_value, "dfa_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "dfa_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfa_Transition9"):
                opp_val = getattr(value, "dfa_Transition9", None)
                setattr(value, "dfa_Transition9", self)

class dfa_Transition:

    pass
class State:

    pass
class RegularState:

    pass
class dfa_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class dfa_RegularState(State):

    pass
class NamedElement:

    pass
class dfa_Language(NamedElement):

    pass
class dfa_State(NamedElement):

    def __init__(self, description: str, dfa_State: "dfa_Transition" = None):
        self.description = description
        self.dfa_State = dfa_State
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def dfa_State(self):
        return self.__dfa_State

    @dfa_State.setter
    def dfa_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfa_State__dfa_State", None)
        self.__dfa_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfa_Transition"):
                opp_val = getattr(old_value, "dfa_Transition", None)
                if opp_val == self:
                    setattr(old_value, "dfa_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfa_Transition"):
                opp_val = getattr(value, "dfa_Transition", None)
                setattr(value, "dfa_Transition", self)

class dfa_Dfa(NamedElement):

    pass
class dfa_FinalState(State):

    pass
class dfa_InitialState(RegularState):

    pass