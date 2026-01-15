from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BooleanOperator(Enum):
    Equal = "Equal"
    Unequal = "Unequal"
class StringOperator(Enum):
    Equal = "Equal"
    Unequal = "Unequal"
class NumberOperator(Enum):
    Equal = "Equal"
    Unequal = "Unequal"
class DataType(Enum):
    Number = "Number"
    Boolean = "Boolean"
    String = "String"


############################################
# Definition of Classes
############################################

class automata_Action:

    pass
class Guard:

    pass
class automata_NumberGuard(Guard):

    def __init__(self, operator: str, value: str):
        self.operator = operator
        self.value = value
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class automata_StringGuard(Guard):

    def __init__(self, value: str, operator: str):
        self.value = value
        self.operator = operator
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class automata_BooleanGuard(Guard):

    def __init__(self, value: bool, operator: str):
        self.value = value
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class automata_Guard:

    pass
class automata_Variable:

    def __init__(self, name: str, type: str, automata_Variable: "automata_Automaton" = None, automata_Variable15: "automata_Guard" = None, automata_Variable17: "automata_Action" = None):
        self.name = name
        self.type = type
        self.automata_Variable = automata_Variable
        self.automata_Variable15 = automata_Variable15
        self.automata_Variable17 = automata_Variable17
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def automata_Variable17(self):
        return self.__automata_Variable17

    @automata_Variable17.setter
    def automata_Variable17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_Variable__automata_Variable17", None)
        self.__automata_Variable17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Action"):
                opp_val = getattr(old_value, "automata_Action", None)
                if opp_val == self:
                    setattr(old_value, "automata_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Action"):
                opp_val = getattr(value, "automata_Action", None)
                setattr(value, "automata_Action", self)

    @property
    def automata_Variable(self):
        return self.__automata_Variable

    @automata_Variable.setter
    def automata_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_Variable__automata_Variable", None)
        self.__automata_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Automaton4"):
                opp_val = getattr(old_value, "automata_Automaton4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Automaton4"):
                opp_val = getattr(value, "automata_Automaton4", None)
                if opp_val is None:
                    setattr(value, "automata_Automaton4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def automata_Variable15(self):
        return self.__automata_Variable15

    @automata_Variable15.setter
    def automata_Variable15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_Variable__automata_Variable15", None)
        self.__automata_Variable15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Guard14"):
                opp_val = getattr(old_value, "automata_Guard14", None)
                if opp_val == self:
                    setattr(old_value, "automata_Guard14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Guard14"):
                opp_val = getattr(value, "automata_Guard14", None)
                setattr(value, "automata_Guard14", self)

class automata_Transition:

    pass
class automata_State:

    def __init__(self, name: str, initial: bool, automata_State: "automata_Automaton" = None, automata_State7: "automata_Transition" = None, automata_State10: "automata_Transition" = None):
        self.name = name
        self.initial = initial
        self.automata_State = automata_State
        self.automata_State7 = automata_State7
        self.automata_State10 = automata_State10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def initial(self) -> bool:
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial

    @property
    def automata_State(self):
        return self.__automata_State

    @automata_State.setter
    def automata_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_State__automata_State", None)
        self.__automata_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Automaton"):
                opp_val = getattr(old_value, "automata_Automaton", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Automaton"):
                opp_val = getattr(value, "automata_Automaton", None)
                if opp_val is None:
                    setattr(value, "automata_Automaton", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def automata_State7(self):
        return self.__automata_State7

    @automata_State7.setter
    def automata_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_State__automata_State7", None)
        self.__automata_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Transition6"):
                opp_val = getattr(old_value, "automata_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "automata_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Transition6"):
                opp_val = getattr(value, "automata_Transition6", None)
                setattr(value, "automata_Transition6", self)

    @property
    def automata_State10(self):
        return self.__automata_State10

    @automata_State10.setter
    def automata_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_State__automata_State10", None)
        self.__automata_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Transition9"):
                opp_val = getattr(old_value, "automata_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "automata_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Transition9"):
                opp_val = getattr(value, "automata_Transition9", None)
                setattr(value, "automata_Transition9", self)

class automata_Automaton:

    pass