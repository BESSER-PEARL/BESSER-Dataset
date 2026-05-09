from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Variable:

    pass
class fsm_NumberVariable(Variable):

    def __init__(self, initialValue: int, fsm_NumberVariable: "fsm_NumberGuard" = None, fsm_NumberVariable21: "fsm_Action" = None):
        self.initialValue = initialValue
        self.fsm_NumberVariable = fsm_NumberVariable
        self.fsm_NumberVariable21 = fsm_NumberVariable21
        
        pass
    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: int):
        self.__initialValue = initialValue


    @property
    def fsm_NumberVariable21(self):
        return self.__fsm_NumberVariable21

    @fsm_NumberVariable21.setter
    def fsm_NumberVariable21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_NumberVariable__fsm_NumberVariable21", None)
        self.__fsm_NumberVariable21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Action20"):
                opp_val = getattr(old_value, "fsm_Action20", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Action20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Action20"):
                opp_val = getattr(value, "fsm_Action20", None)
                setattr(value, "fsm_Action20", self)

    @property
    def fsm_NumberVariable(self):
        return self.__fsm_NumberVariable

    @fsm_NumberVariable.setter
    def fsm_NumberVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_NumberVariable__fsm_NumberVariable", None)
        self.__fsm_NumberVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_NumberGuard"):
                opp_val = getattr(old_value, "fsm_NumberGuard", None)
                if opp_val == self:
                    setattr(old_value, "fsm_NumberGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_NumberGuard"):
                opp_val = getattr(value, "fsm_NumberGuard", None)
                setattr(value, "fsm_NumberGuard", self)

class Action:

    pass
class fsm_DecreaseValueAction(Action):

    def __init__(self, stepValue: int):
        self.stepValue = stepValue
        
        pass
    @property
    def stepValue(self):
        return self.__stepValue

    @stepValue.setter
    def stepValue(self, stepValue: int):
        self.__stepValue = stepValue


class fsm_IncreaseValueAction(Action):

    def __init__(self, stepValue: int):
        self.stepValue = stepValue
        
        pass
    @property
    def stepValue(self):
        return self.__stepValue

    @stepValue.setter
    def stepValue(self, stepValue: int):
        self.__stepValue = stepValue


class fsm_AssignValueAction(Action):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class NumberGuard:

    pass
class fsm_GreaterThanNumberGuard(NumberGuard):

    pass
class fsm_LessThanNumberGuard(NumberGuard):

    pass
class fsm_EqualNumberGuard(NumberGuard):

    pass
class Guard:

    pass
class fsm_NumberGuard(Guard):

    def __init__(self, value: int, fsm_NumberGuard: "fsm_NumberVariable" = None):
        self.value = value
        self.fsm_NumberGuard = fsm_NumberGuard
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


    @property
    def fsm_NumberGuard(self):
        return self.__fsm_NumberGuard

    @fsm_NumberGuard.setter
    def fsm_NumberGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_NumberGuard__fsm_NumberGuard", None)
        self.__fsm_NumberGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_NumberVariable"):
                opp_val = getattr(old_value, "fsm_NumberVariable", None)
                if opp_val == self:
                    setattr(old_value, "fsm_NumberVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_NumberVariable"):
                opp_val = getattr(value, "fsm_NumberVariable", None)
                setattr(value, "fsm_NumberVariable", self)

class fsm_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class fsm_Action(ABC):

    pass
class fsm_Guard(ABC):

    def __init__(self, not_: bool, fsm_Guard: "fsm_Transition" = None):
        self.not_ = not_
        self.fsm_Guard = fsm_Guard
        
        pass
    @property
    def not_(self):
        return self.__not_

    @not_.setter
    def not_(self, not_: bool):
        self.__not_ = not_


    @property
    def fsm_Guard(self):
        return self.__fsm_Guard

    @fsm_Guard.setter
    def fsm_Guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Guard__fsm_Guard", None)
        self.__fsm_Guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition15"):
                opp_val = getattr(old_value, "fsm_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition15"):
                opp_val = getattr(value, "fsm_Transition15", None)
                setattr(value, "fsm_Transition15", self)

class fsm_Variable(ABC):

    def __init__(self, name: str, fsm_Variable: "fsm_StateMachine" = None):
        self.name = name
        self.fsm_Variable = fsm_Variable
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def fsm_Variable(self):
        return self.__fsm_Variable

    @fsm_Variable.setter
    def fsm_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Variable__fsm_Variable", None)
        self.__fsm_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_StateMachine5"):
                opp_val = getattr(old_value, "fsm_StateMachine5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_StateMachine5"):
                opp_val = getattr(value, "fsm_StateMachine5", None)
                if opp_val is None:
                    setattr(value, "fsm_StateMachine5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class fsm_State(NamedElement):

    pass
class fsm_Transition(NamedElement):

    pass
class fsm_StateMachine(NamedElement):

    pass