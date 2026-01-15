from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StringOperator(Enum):
    Equal = "Equal"
    Unequal = "Unequal"
class BooleanOperator(Enum):
    Equal = "Equal"
    Unequal = "Unequal"
class NumberOperator(Enum):
    Equal = "Equal"
    Unequal = "Unequal"
    LessThan = "LessThan"
    GreaterThan = "GreaterThan"
    GreaterOrEqualThan = "GreaterOrEqualThan"
    LessOrEqualThan = "LessOrEqualThan"


############################################
# Definition of Classes
############################################

class Action:

    pass
class automata_NumberAction(Action):

    def __init__(self, value: str, automata_NumberAction: "automata_NumberVariable" = None):
        self.value = value
        self.automata_NumberAction = automata_NumberAction
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def automata_NumberAction(self):
        return self.__automata_NumberAction

    @automata_NumberAction.setter
    def automata_NumberAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_NumberAction__automata_NumberAction", None)
        self.__automata_NumberAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_NumberVariable21"):
                opp_val = getattr(old_value, "automata_NumberVariable21", None)
                if opp_val == self:
                    setattr(old_value, "automata_NumberVariable21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_NumberVariable21"):
                opp_val = getattr(value, "automata_NumberVariable21", None)
                setattr(value, "automata_NumberVariable21", self)

class automata_BooleanAction(Action):

    def __init__(self, value: bool, automata_BooleanAction: "automata_BooleanVariable" = None):
        self.value = value
        self.automata_BooleanAction = automata_BooleanAction
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def automata_BooleanAction(self):
        return self.__automata_BooleanAction

    @automata_BooleanAction.setter
    def automata_BooleanAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_BooleanAction__automata_BooleanAction", None)
        self.__automata_BooleanAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_BooleanVariable23"):
                opp_val = getattr(old_value, "automata_BooleanVariable23", None)
                if opp_val == self:
                    setattr(old_value, "automata_BooleanVariable23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_BooleanVariable23"):
                opp_val = getattr(value, "automata_BooleanVariable23", None)
                setattr(value, "automata_BooleanVariable23", self)

class automata_StringAction(Action):

    def __init__(self, value: str, automata_StringAction: "automata_StringVariable" = None):
        self.value = value
        self.automata_StringAction = automata_StringAction
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def automata_StringAction(self):
        return self.__automata_StringAction

    @automata_StringAction.setter
    def automata_StringAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_StringAction__automata_StringAction", None)
        self.__automata_StringAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_StringVariable19"):
                opp_val = getattr(old_value, "automata_StringVariable19", None)
                if opp_val == self:
                    setattr(old_value, "automata_StringVariable19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_StringVariable19"):
                opp_val = getattr(value, "automata_StringVariable19", None)
                setattr(value, "automata_StringVariable19", self)

class Variable:

    pass
class automata_BooleanVariable(Variable):

    def __init__(self, initialValue: bool, automata_BooleanVariable: "automata_BooleanGuard" = None, automata_BooleanVariable23: "automata_BooleanAction" = None):
        self.initialValue = initialValue
        self.automata_BooleanVariable = automata_BooleanVariable
        self.automata_BooleanVariable23 = automata_BooleanVariable23
        
    @property
    def initialValue(self) -> bool:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: bool):
        self.__initialValue = initialValue

    @property
    def automata_BooleanVariable(self):
        return self.__automata_BooleanVariable

    @automata_BooleanVariable.setter
    def automata_BooleanVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_BooleanVariable__automata_BooleanVariable", None)
        self.__automata_BooleanVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_BooleanGuard"):
                opp_val = getattr(old_value, "automata_BooleanGuard", None)
                if opp_val == self:
                    setattr(old_value, "automata_BooleanGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_BooleanGuard"):
                opp_val = getattr(value, "automata_BooleanGuard", None)
                setattr(value, "automata_BooleanGuard", self)

    @property
    def automata_BooleanVariable23(self):
        return self.__automata_BooleanVariable23

    @automata_BooleanVariable23.setter
    def automata_BooleanVariable23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_BooleanVariable__automata_BooleanVariable23", None)
        self.__automata_BooleanVariable23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_BooleanAction"):
                opp_val = getattr(old_value, "automata_BooleanAction", None)
                if opp_val == self:
                    setattr(old_value, "automata_BooleanAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_BooleanAction"):
                opp_val = getattr(value, "automata_BooleanAction", None)
                setattr(value, "automata_BooleanAction", self)

class automata_NumberVariable(Variable):

    def __init__(self, initialValue: str, automata_NumberVariable: "automata_NumberGuard" = None, automata_NumberVariable21: "automata_NumberAction" = None):
        self.initialValue = initialValue
        self.automata_NumberVariable = automata_NumberVariable
        self.automata_NumberVariable21 = automata_NumberVariable21
        
    @property
    def initialValue(self) -> str:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue

    @property
    def automata_NumberVariable21(self):
        return self.__automata_NumberVariable21

    @automata_NumberVariable21.setter
    def automata_NumberVariable21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_NumberVariable__automata_NumberVariable21", None)
        self.__automata_NumberVariable21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_NumberAction"):
                opp_val = getattr(old_value, "automata_NumberAction", None)
                if opp_val == self:
                    setattr(old_value, "automata_NumberAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_NumberAction"):
                opp_val = getattr(value, "automata_NumberAction", None)
                setattr(value, "automata_NumberAction", self)

    @property
    def automata_NumberVariable(self):
        return self.__automata_NumberVariable

    @automata_NumberVariable.setter
    def automata_NumberVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_NumberVariable__automata_NumberVariable", None)
        self.__automata_NumberVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_NumberGuard"):
                opp_val = getattr(old_value, "automata_NumberGuard", None)
                if opp_val == self:
                    setattr(old_value, "automata_NumberGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_NumberGuard"):
                opp_val = getattr(value, "automata_NumberGuard", None)
                setattr(value, "automata_NumberGuard", self)

class automata_StringVariable(Variable):

    def __init__(self, initialValue: str, automata_StringVariable: "automata_StringGuard" = None, automata_StringVariable19: "automata_StringAction" = None):
        self.initialValue = initialValue
        self.automata_StringVariable = automata_StringVariable
        self.automata_StringVariable19 = automata_StringVariable19
        
    @property
    def initialValue(self) -> str:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue

    @property
    def automata_StringVariable19(self):
        return self.__automata_StringVariable19

    @automata_StringVariable19.setter
    def automata_StringVariable19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_StringVariable__automata_StringVariable19", None)
        self.__automata_StringVariable19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_StringAction"):
                opp_val = getattr(old_value, "automata_StringAction", None)
                if opp_val == self:
                    setattr(old_value, "automata_StringAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_StringAction"):
                opp_val = getattr(value, "automata_StringAction", None)
                setattr(value, "automata_StringAction", self)

    @property
    def automata_StringVariable(self):
        return self.__automata_StringVariable

    @automata_StringVariable.setter
    def automata_StringVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_StringVariable__automata_StringVariable", None)
        self.__automata_StringVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_StringGuard"):
                opp_val = getattr(old_value, "automata_StringGuard", None)
                if opp_val == self:
                    setattr(old_value, "automata_StringGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_StringGuard"):
                opp_val = getattr(value, "automata_StringGuard", None)
                setattr(value, "automata_StringGuard", self)

class automata_Action(ABC):

    pass
class automata_Guard(ABC):

    pass
class automata_Variable(ABC):

    def __init__(self, name: str, automata_Variable: "automata_Automaton" = None):
        self.name = name
        self.automata_Variable = automata_Variable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class Guard:

    pass
class automata_StringGuard(Guard):

    def __init__(self, value: str, operator: str, automata_StringGuard: "automata_StringVariable" = None):
        self.value = value
        self.operator = operator
        self.automata_StringGuard = automata_StringGuard
        
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

    @property
    def automata_StringGuard(self):
        return self.__automata_StringGuard

    @automata_StringGuard.setter
    def automata_StringGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_StringGuard__automata_StringGuard", None)
        self.__automata_StringGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_StringVariable"):
                opp_val = getattr(old_value, "automata_StringVariable", None)
                if opp_val == self:
                    setattr(old_value, "automata_StringVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_StringVariable"):
                opp_val = getattr(value, "automata_StringVariable", None)
                setattr(value, "automata_StringVariable", self)

class automata_NumberGuard(Guard):

    def __init__(self, value: str, operator: str, automata_NumberGuard: "automata_NumberVariable" = None):
        self.value = value
        self.operator = operator
        self.automata_NumberGuard = automata_NumberGuard
        
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

    @property
    def automata_NumberGuard(self):
        return self.__automata_NumberGuard

    @automata_NumberGuard.setter
    def automata_NumberGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_NumberGuard__automata_NumberGuard", None)
        self.__automata_NumberGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_NumberVariable"):
                opp_val = getattr(old_value, "automata_NumberVariable", None)
                if opp_val == self:
                    setattr(old_value, "automata_NumberVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_NumberVariable"):
                opp_val = getattr(value, "automata_NumberVariable", None)
                setattr(value, "automata_NumberVariable", self)

class automata_BooleanGuard(Guard):

    def __init__(self, value: bool, operator: str, automata_BooleanGuard: "automata_BooleanVariable" = None):
        self.value = value
        self.operator = operator
        self.automata_BooleanGuard = automata_BooleanGuard
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def automata_BooleanGuard(self):
        return self.__automata_BooleanGuard

    @automata_BooleanGuard.setter
    def automata_BooleanGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_BooleanGuard__automata_BooleanGuard", None)
        self.__automata_BooleanGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_BooleanVariable"):
                opp_val = getattr(old_value, "automata_BooleanVariable", None)
                if opp_val == self:
                    setattr(old_value, "automata_BooleanVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_BooleanVariable"):
                opp_val = getattr(value, "automata_BooleanVariable", None)
                setattr(value, "automata_BooleanVariable", self)

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

class automata_Automaton:

    pass