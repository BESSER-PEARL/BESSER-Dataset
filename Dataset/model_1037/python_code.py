from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class State:

    pass
class tfsm_FinalState(State):

    pass
class BinaryClockConstraint:

    pass
class tfsm_OrClockConstraint(BinaryClockConstraint):

    pass
class tfsm_AndClockConstraint(BinaryClockConstraint):

    pass
class tfsm_ClockConstraintOperation(ABC):

    pass
class tfsm_InitialState(State):

    pass
class tfsm_Transition:

    def __init__(self, event: str, Transition17: "tfsm_State" = None, tfsm_Transition19: set["tfsm_ClockReset"] = None, tfsm_Transition21: "tfsm_ClockConstraintOperation" = None, outgoingtransitions: "tfsm_State" = None, incommingtransitions: "tfsm_State" = None, tfsm_Transition: "tfsm_FSM" = None, Transition: "tfsm_State" = None):
        self.event = event
        self.Transition17 = Transition17
        self.tfsm_Transition19 = tfsm_Transition19 if tfsm_Transition19 is not None else set()
        self.tfsm_Transition21 = tfsm_Transition21
        self.outgoingtransitions = outgoingtransitions
        self.incommingtransitions = incommingtransitions
        self.tfsm_Transition = tfsm_Transition
        self.Transition = Transition
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def Transition17(self):
        return self.__Transition17

    @Transition17.setter
    def Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__Transition17", None)
        self.__Transition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to"):
                opp_val = getattr(old_value, "to", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to"):
                opp_val = getattr(value, "to", None)
                if opp_val is None:
                    setattr(value, "to", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_Transition21(self):
        return self.__tfsm_Transition21

    @tfsm_Transition21.setter
    def tfsm_Transition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition21", None)
        self.__tfsm_Transition21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_ClockConstraintOperation22"):
                opp_val = getattr(old_value, "tfsm_ClockConstraintOperation22", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_ClockConstraintOperation22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_ClockConstraintOperation22"):
                opp_val = getattr(value, "tfsm_ClockConstraintOperation22", None)
                setattr(value, "tfsm_ClockConstraintOperation22", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                if opp_val is None:
                    setattr(value, "from", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingtransitions(self):
        return self.__outgoingtransitions

    @outgoingtransitions.setter
    def outgoingtransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__outgoingtransitions", None)
        self.__outgoingtransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    @property
    def tfsm_Transition(self):
        return self.__tfsm_Transition

    @tfsm_Transition.setter
    def tfsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition", None)
        self.__tfsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_FSM4"):
                opp_val = getattr(old_value, "tfsm_FSM4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSM4"):
                opp_val = getattr(value, "tfsm_FSM4", None)
                if opp_val is None:
                    setattr(value, "tfsm_FSM4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_Transition19(self):
        return self.__tfsm_Transition19

    @tfsm_Transition19.setter
    def tfsm_Transition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition19", None)
        self.__tfsm_Transition19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_ClockReset"):
                    opp_val = getattr(item, "tfsm_ClockReset", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_ClockReset", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_ClockReset"):
                    opp_val = getattr(item, "tfsm_ClockReset", None)
                    
                    setattr(item, "tfsm_ClockReset", self)
                    

    @property
    def incommingtransitions(self):
        return self.__incommingtransitions

    @incommingtransitions.setter
    def incommingtransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__incommingtransitions", None)
        self.__incommingtransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State25"):
                opp_val = getattr(old_value, "State25", None)
                if opp_val == self:
                    setattr(old_value, "State25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State25"):
                opp_val = getattr(value, "State25", None)
                setattr(value, "State25", self)

class tfsm_State:

    def __init__(self, name: str, to: set["tfsm_Transition"] = None, State: "tfsm_Transition" = None, State25: "tfsm_Transition" = None, tfsm_State: "tfsm_FSM" = None, tfsm_State9: "tfsm_FSM" = None, tfsm_State11: "tfsm_ClockConstraintOperation" = None, tfsm_State13: "tfsm_FSM" = None, from: set["tfsm_Transition"] = None):
        self.name = name
        self.to = to if to is not None else set()
        self.State = State
        self.State25 = State25
        self.tfsm_State = tfsm_State
        self.tfsm_State9 = tfsm_State9
        self.tfsm_State11 = tfsm_State11
        self.tfsm_State13 = tfsm_State13
        self.from = from if from is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tfsm_State13(self):
        return self.__tfsm_State13

    @tfsm_State13.setter
    def tfsm_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__tfsm_State13", None)
        self.__tfsm_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_FSM14"):
                opp_val = getattr(old_value, "tfsm_FSM14", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_FSM14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSM14"):
                opp_val = getattr(value, "tfsm_FSM14", None)
                setattr(value, "tfsm_FSM14", self)

    @property
    def State25(self):
        return self.__State25

    @State25.setter
    def State25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__State25", None)
        self.__State25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incommingtransitions"):
                opp_val = getattr(old_value, "incommingtransitions", None)
                if opp_val == self:
                    setattr(old_value, "incommingtransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incommingtransitions"):
                opp_val = getattr(value, "incommingtransitions", None)
                setattr(value, "incommingtransitions", self)

    @property
    def tfsm_State(self):
        return self.__tfsm_State

    @tfsm_State.setter
    def tfsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__tfsm_State", None)
        self.__tfsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_FSM2"):
                opp_val = getattr(old_value, "tfsm_FSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSM2"):
                opp_val = getattr(value, "tfsm_FSM2", None)
                if opp_val is None:
                    setattr(value, "tfsm_FSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_State11(self):
        return self.__tfsm_State11

    @tfsm_State11.setter
    def tfsm_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__tfsm_State11", None)
        self.__tfsm_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_ClockConstraintOperation"):
                opp_val = getattr(old_value, "tfsm_ClockConstraintOperation", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_ClockConstraintOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_ClockConstraintOperation"):
                opp_val = getattr(value, "tfsm_ClockConstraintOperation", None)
                setattr(value, "tfsm_ClockConstraintOperation", self)

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition17"):
                    opp_val = getattr(item, "Transition17", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition17"):
                    opp_val = getattr(item, "Transition17", None)
                    
                    setattr(item, "Transition17", self)
                    

    @property
    def tfsm_State9(self):
        return self.__tfsm_State9

    @tfsm_State9.setter
    def tfsm_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__tfsm_State9", None)
        self.__tfsm_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_FSM8"):
                opp_val = getattr(old_value, "tfsm_FSM8", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_FSM8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSM8"):
                opp_val = getattr(value, "tfsm_FSM8", None)
                setattr(value, "tfsm_FSM8", self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__from", None)
        self.__from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingtransitions"):
                opp_val = getattr(old_value, "outgoingtransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingtransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingtransitions"):
                opp_val = getattr(value, "outgoingtransitions", None)
                setattr(value, "outgoingtransitions", self)

class ClockConstraint:

    pass
class tfsm_LowerEqualClockConstraint(ClockConstraint):

    pass
class tfsm_UpperClockConstraint(ClockConstraint):

    pass
class tfsm_UpperEqualClockConstraint(ClockConstraint):

    pass
class tfsm_LowerClockConstraint(ClockConstraint):

    pass
class tfsm_Clock:

    def __init__(self, name: str, tick: int, tfsm_Clock27: "tfsm_ClockConstraint" = None, tfsm_Clock30: "tfsm_ClockReset" = None, tfsm_Clock: "tfsm_FSM" = None):
        self.name = name
        self.tick = tick
        self.tfsm_Clock27 = tfsm_Clock27
        self.tfsm_Clock30 = tfsm_Clock30
        self.tfsm_Clock = tfsm_Clock
        
    @property
    def tick(self) -> int:
        return self.__tick

    @tick.setter
    def tick(self, tick: int):
        self.__tick = tick

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tfsm_Clock27(self):
        return self.__tfsm_Clock27

    @tfsm_Clock27.setter
    def tfsm_Clock27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Clock__tfsm_Clock27", None)
        self.__tfsm_Clock27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_ClockConstraint"):
                opp_val = getattr(old_value, "tfsm_ClockConstraint", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_ClockConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_ClockConstraint"):
                opp_val = getattr(value, "tfsm_ClockConstraint", None)
                setattr(value, "tfsm_ClockConstraint", self)

    @property
    def tfsm_Clock30(self):
        return self.__tfsm_Clock30

    @tfsm_Clock30.setter
    def tfsm_Clock30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Clock__tfsm_Clock30", None)
        self.__tfsm_Clock30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_ClockReset29"):
                opp_val = getattr(old_value, "tfsm_ClockReset29", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_ClockReset29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_ClockReset29"):
                opp_val = getattr(value, "tfsm_ClockReset29", None)
                setattr(value, "tfsm_ClockReset29", self)

    @property
    def tfsm_Clock(self):
        return self.__tfsm_Clock

    @tfsm_Clock.setter
    def tfsm_Clock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Clock__tfsm_Clock", None)
        self.__tfsm_Clock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_FSM"):
                opp_val = getattr(old_value, "tfsm_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSM"):
                opp_val = getattr(value, "tfsm_FSM", None)
                if opp_val is None:
                    setattr(value, "tfsm_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClockConstraintOperation:

    pass
class tfsm_BinaryClockConstraint(ClockConstraintOperation):

    pass
class tfsm_ClockConstraint(ClockConstraintOperation):

    def __init__(self, threshold: int, tfsm_ClockConstraint: "tfsm_Clock" = None):
        self.threshold = threshold
        self.tfsm_ClockConstraint = tfsm_ClockConstraint
        
    @property
    def threshold(self) -> int:
        return self.__threshold

    @threshold.setter
    def threshold(self, threshold: int):
        self.__threshold = threshold

    @property
    def tfsm_ClockConstraint(self):
        return self.__tfsm_ClockConstraint

    @tfsm_ClockConstraint.setter
    def tfsm_ClockConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_ClockConstraint__tfsm_ClockConstraint", None)
        self.__tfsm_ClockConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_Clock27"):
                opp_val = getattr(old_value, "tfsm_Clock27", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_Clock27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_Clock27"):
                opp_val = getattr(value, "tfsm_Clock27", None)
                setattr(value, "tfsm_Clock27", self)

class tfsm_ClockReset:

    pass
class tfsm_FSM:

    def __init__(self, name: str, tfsm_FSM: set["tfsm_Clock"] = None, tfsm_FSM2: set["tfsm_State"] = None, tfsm_FSM4: set["tfsm_Transition"] = None, tfsm_FSM6: "tfsm_InitialState" = None, tfsm_FSM8: "tfsm_State" = None, tfsm_FSM14: "tfsm_State" = None):
        self.name = name
        self.tfsm_FSM = tfsm_FSM if tfsm_FSM is not None else set()
        self.tfsm_FSM2 = tfsm_FSM2 if tfsm_FSM2 is not None else set()
        self.tfsm_FSM4 = tfsm_FSM4 if tfsm_FSM4 is not None else set()
        self.tfsm_FSM6 = tfsm_FSM6
        self.tfsm_FSM8 = tfsm_FSM8
        self.tfsm_FSM14 = tfsm_FSM14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tfsm_FSM2(self):
        return self.__tfsm_FSM2

    @tfsm_FSM2.setter
    def tfsm_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSM__tfsm_FSM2", None)
        self.__tfsm_FSM2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_State"):
                    opp_val = getattr(item, "tfsm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_State"):
                    opp_val = getattr(item, "tfsm_State", None)
                    
                    setattr(item, "tfsm_State", self)
                    

    @property
    def tfsm_FSM6(self):
        return self.__tfsm_FSM6

    @tfsm_FSM6.setter
    def tfsm_FSM6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSM__tfsm_FSM6", None)
        self.__tfsm_FSM6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_InitialState"):
                opp_val = getattr(old_value, "tfsm_InitialState", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_InitialState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_InitialState"):
                opp_val = getattr(value, "tfsm_InitialState", None)
                setattr(value, "tfsm_InitialState", self)

    @property
    def tfsm_FSM4(self):
        return self.__tfsm_FSM4

    @tfsm_FSM4.setter
    def tfsm_FSM4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSM__tfsm_FSM4", None)
        self.__tfsm_FSM4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_Transition"):
                    opp_val = getattr(item, "tfsm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_Transition"):
                    opp_val = getattr(item, "tfsm_Transition", None)
                    
                    setattr(item, "tfsm_Transition", self)
                    

    @property
    def tfsm_FSM14(self):
        return self.__tfsm_FSM14

    @tfsm_FSM14.setter
    def tfsm_FSM14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSM__tfsm_FSM14", None)
        self.__tfsm_FSM14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_State13"):
                opp_val = getattr(old_value, "tfsm_State13", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_State13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_State13"):
                opp_val = getattr(value, "tfsm_State13", None)
                setattr(value, "tfsm_State13", self)

    @property
    def tfsm_FSM(self):
        return self.__tfsm_FSM

    @tfsm_FSM.setter
    def tfsm_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSM__tfsm_FSM", None)
        self.__tfsm_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_Clock"):
                    opp_val = getattr(item, "tfsm_Clock", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_Clock", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_Clock"):
                    opp_val = getattr(item, "tfsm_Clock", None)
                    
                    setattr(item, "tfsm_Clock", self)
                    

    @property
    def tfsm_FSM8(self):
        return self.__tfsm_FSM8

    @tfsm_FSM8.setter
    def tfsm_FSM8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSM__tfsm_FSM8", None)
        self.__tfsm_FSM8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_State9"):
                opp_val = getattr(old_value, "tfsm_State9", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_State9"):
                opp_val = getattr(value, "tfsm_State9", None)
                setattr(value, "tfsm_State9", self)
