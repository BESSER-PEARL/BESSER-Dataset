from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Variable:

    pass
class fsm_NumberVariable(Variable):

    def __init__(self, value: bool, initialValue: int, fsm_NumberVariable: "fsm_NumberGuard" = None, fsm_NumberVariable32: "fsm_Action" = None):
        self.value = value
        self.initialValue = initialValue
        self.fsm_NumberVariable = fsm_NumberVariable
        self.fsm_NumberVariable32 = fsm_NumberVariable32
        
    @property
    def initialValue(self) -> int:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: int):
        self.__initialValue = initialValue

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fsm_NumberVariable32(self):
        return self.__fsm_NumberVariable32

    @fsm_NumberVariable32.setter
    def fsm_NumberVariable32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_NumberVariable__fsm_NumberVariable32", None)
        self.__fsm_NumberVariable32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Action31"):
                opp_val = getattr(old_value, "fsm_Action31", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Action31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Action31"):
                opp_val = getattr(value, "fsm_Action31", None)
                setattr(value, "fsm_Action31", self)

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
class fsm_IncreaseValueAction(Action):

    def __init__(self, stepValue: int):
        self.stepValue = stepValue
        
    @property
    def stepValue(self) -> int:
        return self.__stepValue

    @stepValue.setter
    def stepValue(self, stepValue: int):
        self.__stepValue = stepValue

    def execute(self):
        # TODO: Implement execute method
        pass

class fsm_DecreaseValueAction(Action):

    def __init__(self, stepValue: int):
        self.stepValue = stepValue
        
    @property
    def stepValue(self) -> int:
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
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    def execute(self):
        # TODO: Implement execute method
        pass

class NumberGuard:

    pass
class fsm_GreaterThanNumberGuard(NumberGuard):

    def __init__(self):
        
    def holds(self):
        # TODO: Implement holds method
        pass

class fsm_LessThanNumberGuard(NumberGuard):

    def __init__(self):
        
    def holds(self):
        # TODO: Implement holds method
        pass

class fsm_EqualNumberGuard(NumberGuard):

    def __init__(self):
        
    def holds(self):
        # TODO: Implement holds method
        pass

class Guard:

    pass
class fsm_NumberGuard(Guard):

    def __init__(self, value: bool, fsm_NumberGuard: "fsm_NumberVariable" = None):
        self.value = value
        self.fsm_NumberGuard = fsm_NumberGuard
        
    @property
    def value(self) -> bool:
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

class fsm_Variable(ABC):

    def __init__(self, name: str, fsm_Variable: "fsm_StateMachine" = None):
        self.name = name
        self.fsm_Variable = fsm_Variable
        
    @property
    def name(self) -> str:
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
            if hasattr(old_value, "fsm_StateMachine6"):
                opp_val = getattr(old_value, "fsm_StateMachine6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_StateMachine6"):
                opp_val = getattr(value, "fsm_StateMachine6", None)
                if opp_val is None:
                    setattr(value, "fsm_StateMachine6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class fsm_Action(ABC):

    def __init__(self, fsm_Action: "fsm_Transition" = None, fsm_Action31: "fsm_NumberVariable" = None):
        self.fsm_Action = fsm_Action
        self.fsm_Action31 = fsm_Action31
        
    @property
    def fsm_Action31(self):
        return self.__fsm_Action31

    @fsm_Action31.setter
    def fsm_Action31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Action__fsm_Action31", None)
        self.__fsm_Action31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_NumberVariable32"):
                opp_val = getattr(old_value, "fsm_NumberVariable32", None)
                if opp_val == self:
                    setattr(old_value, "fsm_NumberVariable32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_NumberVariable32"):
                opp_val = getattr(value, "fsm_NumberVariable32", None)
                setattr(value, "fsm_NumberVariable32", self)

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
            if hasattr(old_value, "fsm_Transition28"):
                opp_val = getattr(old_value, "fsm_Transition28", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition28"):
                opp_val = getattr(value, "fsm_Transition28", None)
                setattr(value, "fsm_Transition28", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class fsm_Guard(ABC):

    def __init__(self, not: bool, fsm_Guard: "fsm_Transition" = None):
        self.not = not
        self.fsm_Guard = fsm_Guard
        
    @property
    def not(self) -> bool:
        return self.__not

    @not.setter
    def not(self, not: bool):
        self.__not = not

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
            if hasattr(old_value, "fsm_Transition26"):
                opp_val = getattr(old_value, "fsm_Transition26", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition26"):
                opp_val = getattr(value, "fsm_Transition26", None)
                setattr(value, "fsm_Transition26", self)

    def holds(self):
        # TODO: Implement holds method
        pass

class NamedElement:

    pass
class fsm_Transition(NamedElement):

    def __init__(self, 15: "fsm_State" = None, 18: "fsm_State" = None, 20: "fsm_State" = None, 23: "fsm_State" = None, fsm_Transition26: "fsm_Guard" = None, fsm_Transition28: "fsm_Action" = None, fsm_Transition: "fsm_StateMachine" = None):
        self.15 = 15
        self.18 = 18
        self.20 = 20
        self.23 = 23
        self.fsm_Transition26 = fsm_Transition26
        self.fsm_Transition28 = fsm_Transition28
        self.fsm_Transition = fsm_Transition
        
    @property
    def fsm_Transition26(self):
        return self.__fsm_Transition26

    @fsm_Transition26.setter
    def fsm_Transition26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition26", None)
        self.__fsm_Transition26 = value
        
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
            if hasattr(old_value, "fsm_StateMachine4"):
                opp_val = getattr(old_value, "fsm_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_StateMachine4"):
                opp_val = getattr(value, "fsm_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "fsm_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 23(self):
        return self.__23

    @23.setter
    def 23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__23", None)
        self.__23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "24"):
                opp_val = getattr(old_value, "24", None)
                if opp_val == self:
                    setattr(old_value, "24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "24"):
                opp_val = getattr(value, "24", None)
                setattr(value, "24", self)

    @property
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__20", None)
        self.__20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "21"):
                opp_val = getattr(old_value, "21", None)
                if opp_val == self:
                    setattr(old_value, "21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "21"):
                opp_val = getattr(value, "21", None)
                setattr(value, "21", self)

    @property
    def fsm_Transition28(self):
        return self.__fsm_Transition28

    @fsm_Transition28.setter
    def fsm_Transition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition28", None)
        self.__fsm_Transition28 = value
        
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
    def 15(self):
        return self.__15

    @15.setter
    def 15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__15", None)
        self.__15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "14"):
                opp_val = getattr(old_value, "14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "14"):
                opp_val = getattr(value, "14", None)
                if opp_val is None:
                    setattr(value, "14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 18(self):
        return self.__18

    @18.setter
    def 18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__18", None)
        self.__18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "17"):
                opp_val = getattr(old_value, "17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "17"):
                opp_val = getattr(value, "17", None)
                if opp_val is None:
                    setattr(value, "17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def fire(self):
        # TODO: Implement fire method
        pass

class fsm_State(NamedElement):

    pass
class fsm_StateMachine(NamedElement):

    def __init__(self, : set["fsm_State"] = None, fsm_StateMachine8: "fsm_State" = None, 12: "fsm_State" = None, fsm_StateMachine: "fsm_State" = None, fsm_StateMachine4: set["fsm_Transition"] = None, fsm_StateMachine6: set["fsm_Variable"] = None):
        self. =  if  is not None else set()
        self.fsm_StateMachine8 = fsm_StateMachine8
        self.12 = 12
        self.fsm_StateMachine = fsm_StateMachine
        self.fsm_StateMachine4 = fsm_StateMachine4 if fsm_StateMachine4 is not None else set()
        self.fsm_StateMachine6 = fsm_StateMachine6 if fsm_StateMachine6 is not None else set()
        
    @property
    def 12(self):
        return self.__12

    @12.setter
    def 12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__12", None)
        self.__12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "11"):
                opp_val = getattr(old_value, "11", None)
                if opp_val == self:
                    setattr(old_value, "11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "11"):
                opp_val = getattr(value, "11", None)
                setattr(value, "11", self)

    @property
    def fsm_StateMachine6(self):
        return self.__fsm_StateMachine6

    @fsm_StateMachine6.setter
    def fsm_StateMachine6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine6", None)
        self.__fsm_StateMachine6 = value if value is not None else set()
        
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
    def fsm_StateMachine4(self):
        return self.__fsm_StateMachine4

    @fsm_StateMachine4.setter
    def fsm_StateMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine4", None)
        self.__fsm_StateMachine4 = value if value is not None else set()
        
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
    def fsm_StateMachine8(self):
        return self.__fsm_StateMachine8

    @fsm_StateMachine8.setter
    def fsm_StateMachine8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine8", None)
        self.__fsm_StateMachine8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State9"):
                opp_val = getattr(old_value, "fsm_State9", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State9"):
                opp_val = getattr(value, "fsm_State9", None)
                setattr(value, "fsm_State9", self)

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
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    if opp_val == self:
                        setattr(item, "1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    setattr(item, "1", self)
                    

    def main(self):
        # TODO: Implement main method
        pass

    def step(self):
        # TODO: Implement step method
        pass

    def assignInitialValues(self, arguments: str):
        # TODO: Implement assignInitialValues method
        pass
