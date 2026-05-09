from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Variable:

    pass
class fsm_NumberVariable(Variable):

    def __init__(self, initialValue: int, value: bool, fsm_NumberVariable: "fsm_NumberGuard" = None, fsm_NumberVariable24: "fsm_Action" = None):
        self.initialValue = initialValue
        self.value = value
        self.fsm_NumberVariable = fsm_NumberVariable
        self.fsm_NumberVariable24 = fsm_NumberVariable24
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: int):
        self.__initialValue = initialValue


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

    @property
    def fsm_NumberVariable24(self):
        return self.__fsm_NumberVariable24

    @fsm_NumberVariable24.setter
    def fsm_NumberVariable24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_NumberVariable__fsm_NumberVariable24", None)
        self.__fsm_NumberVariable24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Action23"):
                opp_val = getattr(old_value, "fsm_Action23", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Action23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Action23"):
                opp_val = getattr(value, "fsm_Action23", None)
                setattr(value, "fsm_Action23", self)

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

    def __init__(self, fsm_Action23: "fsm_NumberVariable" = None, fsm_Action: "fsm_Transition" = None):
        self.fsm_Action23 = fsm_Action23
        self.fsm_Action = fsm_Action
        
        pass
    @property
    def fsm_Action23(self):
        return self.__fsm_Action23

    @fsm_Action23.setter
    def fsm_Action23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Action__fsm_Action23", None)
        self.__fsm_Action23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_NumberVariable24"):
                opp_val = getattr(old_value, "fsm_NumberVariable24", None)
                if opp_val == self:
                    setattr(old_value, "fsm_NumberVariable24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_NumberVariable24"):
                opp_val = getattr(value, "fsm_NumberVariable24", None)
                setattr(value, "fsm_NumberVariable24", self)

    @property
    def fsm_Action(self):
        return self.__fsm_Action

    @fsm_Action.setter
    def fsm_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Action__fsm_Action", None)
        self.__fsm_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition20"):
                opp_val = getattr(old_value, "fsm_Transition20", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition20"):
                opp_val = getattr(value, "fsm_Transition20", None)
                setattr(value, "fsm_Transition20", self)

    def execute(self):
        # TODO: Implement execute method
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
            if hasattr(old_value, "fsm_Transition18"):
                opp_val = getattr(old_value, "fsm_Transition18", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition18"):
                opp_val = getattr(value, "fsm_Transition18", None)
                setattr(value, "fsm_Transition18", self)

    def holds(self):
        # TODO: Implement holds method
        pass

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


    def execute(self):
        # TODO: Implement execute method
        pass

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


    def execute(self):
        # TODO: Implement execute method
        pass

class fsm_AssignValueAction(Action):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


    def execute(self):
        # TODO: Implement execute method
        pass

class NumberGuard:

    pass
class fsm_LessThanNumberGuard(NumberGuard):

    def __init__(self):
        
        pass
    def holds(self):
        # TODO: Implement holds method
        pass

class fsm_GreaterThanNumberGuard(NumberGuard):

    def __init__(self):
        
        pass
    def holds(self):
        # TODO: Implement holds method
        pass

class fsm_EqualNumberGuard(NumberGuard):

    def __init__(self):
        
        pass
    def holds(self):
        # TODO: Implement holds method
        pass

class Guard:

    pass
class fsm_NumberGuard(Guard):

    def __init__(self, value: bool, fsm_NumberGuard: "fsm_NumberVariable" = None):
        self.value = value
        self.fsm_NumberGuard = fsm_NumberGuard
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
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

    def holds(self):
        # TODO: Implement holds method
        pass

class NamedElement:

    pass
class fsm_State(NamedElement):

    pass
class fsm_StateMachine(NamedElement):

    def __init__(self, owningFSM: set["fsm_State"] = None, fsm_StateMachine: "fsm_State" = None, fsm_StateMachine3: set["fsm_Transition"] = None, fsm_StateMachine5: set["fsm_Variable"] = None, fsm_StateMachine7: "fsm_State" = None, StateMachine: "fsm_State" = None):
        self.owningFSM = owningFSM if owningFSM is not None else set()
        self.fsm_StateMachine = fsm_StateMachine
        self.fsm_StateMachine3 = fsm_StateMachine3 if fsm_StateMachine3 is not None else set()
        self.fsm_StateMachine5 = fsm_StateMachine5 if fsm_StateMachine5 is not None else set()
        self.fsm_StateMachine7 = fsm_StateMachine7
        self.StateMachine = StateMachine
        
        pass
    @property
    def owningFSM(self):
        return self.__owningFSM

    @owningFSM.setter
    def owningFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__owningFSM", None)
        self.__owningFSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def fsm_StateMachine3(self):
        return self.__fsm_StateMachine3

    @fsm_StateMachine3.setter
    def fsm_StateMachine3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine3", None)
        self.__fsm_StateMachine3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    setattr(item, "fsm_Transition", self)
                    

    @property
    def fsm_StateMachine7(self):
        return self.__fsm_StateMachine7

    @fsm_StateMachine7.setter
    def fsm_StateMachine7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine7", None)
        self.__fsm_StateMachine7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State8"):
                opp_val = getattr(old_value, "fsm_State8", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State8"):
                opp_val = getattr(value, "fsm_State8", None)
                setattr(value, "fsm_State8", self)

    @property
    def fsm_StateMachine(self):
        return self.__fsm_StateMachine

    @fsm_StateMachine.setter
    def fsm_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine", None)
        self.__fsm_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State"):
                opp_val = getattr(old_value, "fsm_State", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State"):
                opp_val = getattr(value, "fsm_State", None)
                setattr(value, "fsm_State", self)

    @property
    def fsm_StateMachine5(self):
        return self.__fsm_StateMachine5

    @fsm_StateMachine5.setter
    def fsm_StateMachine5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine5", None)
        self.__fsm_StateMachine5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Variable"):
                    opp_val = getattr(item, "fsm_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Variable"):
                    opp_val = getattr(item, "fsm_Variable", None)
                    
                    setattr(item, "fsm_Variable", self)
                    

    @property
    def StateMachine(self):
        return self.__StateMachine

    @StateMachine.setter
    def StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__StateMachine", None)
        self.__StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedStates"):
                opp_val = getattr(old_value, "ownedStates", None)
                if opp_val == self:
                    setattr(old_value, "ownedStates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedStates"):
                opp_val = getattr(value, "ownedStates", None)
                setattr(value, "ownedStates", self)

    def assignInitialValues(self, fsm_arguments):
        # TODO: Implement assignInitialValues method
        pass

    def step(self):
        # TODO: Implement step method
        pass

    def main(self):
        # TODO: Implement main method
        pass

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

class fsm_Transition(NamedElement):

    def __init__(self, fsm_Transition: "fsm_StateMachine" = None, Transition: "fsm_State" = None, Transition12: "fsm_State" = None, outgoingTransitions: "fsm_State" = None, incomingTransitions: "fsm_State" = None, fsm_Transition18: "fsm_Guard" = None, fsm_Transition20: "fsm_Action" = None):
        self.fsm_Transition = fsm_Transition
        self.Transition = Transition
        self.Transition12 = Transition12
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.fsm_Transition18 = fsm_Transition18
        self.fsm_Transition20 = fsm_Transition20
        
        pass
    @property
    def fsm_Transition20(self):
        return self.__fsm_Transition20

    @fsm_Transition20.setter
    def fsm_Transition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition20", None)
        self.__fsm_Transition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Action"):
                opp_val = getattr(old_value, "fsm_Action", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Action"):
                opp_val = getattr(value, "fsm_Action", None)
                setattr(value, "fsm_Action", self)

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State14"):
                opp_val = getattr(old_value, "State14", None)
                if opp_val == self:
                    setattr(old_value, "State14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State14"):
                opp_val = getattr(value, "State14", None)
                setattr(value, "State14", self)

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State16"):
                opp_val = getattr(old_value, "State16", None)
                if opp_val == self:
                    setattr(old_value, "State16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State16"):
                opp_val = getattr(value, "State16", None)
                setattr(value, "State16", self)

    @property
    def fsm_Transition18(self):
        return self.__fsm_Transition18

    @fsm_Transition18.setter
    def fsm_Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition18", None)
        self.__fsm_Transition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Guard"):
                opp_val = getattr(old_value, "fsm_Guard", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Guard"):
                opp_val = getattr(value, "fsm_Guard", None)
                setattr(value, "fsm_Guard", self)

    @property
    def fsm_Transition(self):
        return self.__fsm_Transition

    @fsm_Transition.setter
    def fsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition", None)
        self.__fsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_StateMachine3"):
                opp_val = getattr(old_value, "fsm_StateMachine3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_StateMachine3"):
                opp_val = getattr(value, "fsm_StateMachine3", None)
                if opp_val is None:
                    setattr(value, "fsm_StateMachine3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition12(self):
        return self.__Transition12

    @Transition12.setter
    def Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition12", None)
        self.__Transition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def fire(self):
        # TODO: Implement fire method
        pass
