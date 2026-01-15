from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Transition:

    pass
class fsm_TimedTransition(Transition):

    def __init__(self, duration: int):
        self.duration = duration
        
    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

class fsm_Region:

    pass
class Pseudostate:

    pass
class fsm_Join(Pseudostate):

    pass
class fsm_Choice(Pseudostate):

    pass
class fsm_Fork(Pseudostate):

    pass
class fsm_Action:

    def __init__(self, variable: str, value: bool, fsm_Action: "fsm_Transition" = None):
        self.variable = variable
        self.value = value
        self.fsm_Action = fsm_Action
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

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
            if hasattr(old_value, "fsm_Transition29"):
                opp_val = getattr(old_value, "fsm_Transition29", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition29"):
                opp_val = getattr(value, "fsm_Transition29", None)
                setattr(value, "fsm_Transition29", self)

class fsm_Guard:

    def __init__(self, expression: str, fsm_Guard: "fsm_Transition" = None):
        self.expression = expression
        self.fsm_Guard = fsm_Guard
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

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
            if hasattr(old_value, "fsm_Transition27"):
                opp_val = getattr(old_value, "fsm_Transition27", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition27"):
                opp_val = getattr(value, "fsm_Transition27", None)
                setattr(value, "fsm_Transition27", self)

class fsm_Trigger:

    def __init__(self, expression: str, fsm_Trigger: "fsm_Transition" = None):
        self.expression = expression
        self.fsm_Trigger = fsm_Trigger
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def fsm_Trigger(self):
        return self.__fsm_Trigger

    @fsm_Trigger.setter
    def fsm_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger", None)
        self.__fsm_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition"):
                opp_val = getattr(old_value, "fsm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition"):
                opp_val = getattr(value, "fsm_Transition", None)
                setattr(value, "fsm_Transition", self)

class State:

    pass
class fsm_Pseudostate(State):

    pass
class fsm_InitialState(State):

    pass
class fsm_FinalState(State):

    pass
class fsm_CompositeState(State):

    pass
class fsm_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class fsm_Variable:

    def __init__(self, name: str, value: bool, fsm_Variable: "fsm_StateMachine" = None):
        self.name = name
        self.value = value
        self.fsm_Variable = fsm_Variable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

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
            if hasattr(old_value, "fsm_StateMachine"):
                opp_val = getattr(old_value, "fsm_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_StateMachine"):
                opp_val = getattr(value, "fsm_StateMachine", None)
                if opp_val is None:
                    setattr(value, "fsm_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class fsm_Transition(NamedElement):

    def __init__(self, initialTime: int, finalTime: int, 4: "fsm_StateMachine" = None, 8: "fsm_State" = None, 17: "fsm_State" = None, 20: "fsm_State" = None, fsm_Transition: "fsm_Trigger" = None, 24: "fsm_StateMachine" = None, fsm_Transition27: "fsm_Guard" = None, fsm_Transition29: "fsm_Action" = None, 11: "fsm_State" = None):
        self.initialTime = initialTime
        self.finalTime = finalTime
        self.4 = 4
        self.8 = 8
        self.17 = 17
        self.20 = 20
        self.fsm_Transition = fsm_Transition
        self.24 = 24
        self.fsm_Transition27 = fsm_Transition27
        self.fsm_Transition29 = fsm_Transition29
        self.11 = 11
        
    @property
    def initialTime(self) -> int:
        return self.__initialTime

    @initialTime.setter
    def initialTime(self, initialTime: int):
        self.__initialTime = initialTime

    @property
    def finalTime(self) -> int:
        return self.__finalTime

    @finalTime.setter
    def finalTime(self, finalTime: int):
        self.__finalTime = finalTime

    @property
    def 8(self):
        return self.__8

    @8.setter
    def 8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__8", None)
        self.__8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "7"):
                opp_val = getattr(old_value, "7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "7"):
                opp_val = getattr(value, "7", None)
                if opp_val is None:
                    setattr(value, "7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 11(self):
        return self.__11

    @11.setter
    def 11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__11", None)
        self.__11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "10"):
                opp_val = getattr(old_value, "10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "10"):
                opp_val = getattr(value, "10", None)
                if opp_val is None:
                    setattr(value, "10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 24(self):
        return self.__24

    @24.setter
    def 24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__24", None)
        self.__24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "25"):
                opp_val = getattr(old_value, "25", None)
                if opp_val == self:
                    setattr(old_value, "25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "25"):
                opp_val = getattr(value, "25", None)
                setattr(value, "25", self)

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
            if hasattr(old_value, "fsm_Trigger"):
                opp_val = getattr(old_value, "fsm_Trigger", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Trigger"):
                opp_val = getattr(value, "fsm_Trigger", None)
                setattr(value, "fsm_Trigger", self)

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "3"):
                opp_val = getattr(old_value, "3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "3"):
                opp_val = getattr(value, "3", None)
                if opp_val is None:
                    setattr(value, "3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_Transition29(self):
        return self.__fsm_Transition29

    @fsm_Transition29.setter
    def fsm_Transition29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition29", None)
        self.__fsm_Transition29 = value
        
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
    def fsm_Transition27(self):
        return self.__fsm_Transition27

    @fsm_Transition27.setter
    def fsm_Transition27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition27", None)
        self.__fsm_Transition27 = value
        
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
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__17", None)
        self.__17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "18"):
                opp_val = getattr(old_value, "18", None)
                if opp_val == self:
                    setattr(old_value, "18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "18"):
                opp_val = getattr(value, "18", None)
                setattr(value, "18", self)

class fsm_State(NamedElement):

    def __init__(self, initialTime: int, finalTime: int, 1: "fsm_StateMachine" = None, 7: set["fsm_Transition"] = None, fsm_State: "fsm_CompositeState" = None, 18: "fsm_Transition" = None, 21: "fsm_Transition" = None, 10: set["fsm_Transition"] = None, 13: "fsm_StateMachine" = None, fsm_State34: "fsm_Region" = None):
        self.initialTime = initialTime
        self.finalTime = finalTime
        self.1 = 1
        self.7 = 7 if 7 is not None else set()
        self.fsm_State = fsm_State
        self.18 = 18
        self.21 = 21
        self.10 = 10 if 10 is not None else set()
        self.13 = 13
        self.fsm_State34 = fsm_State34
        
    @property
    def initialTime(self) -> int:
        return self.__initialTime

    @initialTime.setter
    def initialTime(self, initialTime: int):
        self.__initialTime = initialTime

    @property
    def finalTime(self) -> int:
        return self.__finalTime

    @finalTime.setter
    def finalTime(self, finalTime: int):
        self.__finalTime = finalTime

    @property
    def fsm_State(self):
        return self.__fsm_State

    @fsm_State.setter
    def fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State", None)
        self.__fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_CompositeState"):
                opp_val = getattr(old_value, "fsm_CompositeState", None)
                if opp_val == self:
                    setattr(old_value, "fsm_CompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_CompositeState"):
                opp_val = getattr(value, "fsm_CompositeState", None)
                setattr(value, "fsm_CompositeState", self)

    @property
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__7", None)
        self.__7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "8"):
                    opp_val = getattr(item, "8", None)
                    
                    if opp_val == self:
                        setattr(item, "8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "8"):
                    opp_val = getattr(item, "8", None)
                    
                    setattr(item, "8", self)
                    

    @property
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__10", None)
        self.__10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "11"):
                    opp_val = getattr(item, "11", None)
                    
                    if opp_val == self:
                        setattr(item, "11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "11"):
                    opp_val = getattr(item, "11", None)
                    
                    setattr(item, "11", self)
                    

    @property
    def 18(self):
        return self.__18

    @18.setter
    def 18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__18", None)
        self.__18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "17"):
                opp_val = getattr(old_value, "17", None)
                if opp_val == self:
                    setattr(old_value, "17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "17"):
                opp_val = getattr(value, "17", None)
                setattr(value, "17", self)

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 21(self):
        return self.__21

    @21.setter
    def 21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__21", None)
        self.__21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "20"):
                opp_val = getattr(old_value, "20", None)
                if opp_val == self:
                    setattr(old_value, "20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "20"):
                opp_val = getattr(value, "20", None)
                setattr(value, "20", self)

    @property
    def fsm_State34(self):
        return self.__fsm_State34

    @fsm_State34.setter
    def fsm_State34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State34", None)
        self.__fsm_State34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Region33"):
                opp_val = getattr(old_value, "fsm_Region33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Region33"):
                opp_val = getattr(value, "fsm_Region33", None)
                if opp_val is None:
                    setattr(value, "fsm_Region33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "14"):
                opp_val = getattr(old_value, "14", None)
                if opp_val == self:
                    setattr(old_value, "14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "14"):
                opp_val = getattr(value, "14", None)
                setattr(value, "14", self)

class fsm_StateMachine(NamedElement):

    pass