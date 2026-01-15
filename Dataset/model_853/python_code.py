from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Pseudostate:

    pass
class fsm_Join(Pseudostate):

    pass
class fsm_Fork(Pseudostate):

    pass
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
class NamedElement:

    pass
class fsm_Transition(NamedElement):

    def __init__(self, initialTime: int, finalTime: int, time: int, 16: "fsm_State" = None, 19: "fsm_State" = None, fsm_Transition: "fsm_Trigger" = None, 23: "fsm_StateMachine" = None, 4: "fsm_StateMachine" = None, 7: "fsm_State" = None, 10: "fsm_State" = None):
        self.initialTime = initialTime
        self.finalTime = finalTime
        self.time = time
        self.16 = 16
        self.19 = 19
        self.fsm_Transition = fsm_Transition
        self.23 = 23
        self.4 = 4
        self.7 = 7
        self.10 = 10
        
    @property
    def initialTime(self) -> int:
        return self.__initialTime

    @initialTime.setter
    def initialTime(self, initialTime: int):
        self.__initialTime = initialTime

    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def finalTime(self) -> int:
        return self.__finalTime

    @finalTime.setter
    def finalTime(self, finalTime: int):
        self.__finalTime = finalTime

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
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__16", None)
        self.__16 = value
        
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
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__19", None)
        self.__19 = value
        
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
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__10", None)
        self.__10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "9"):
                opp_val = getattr(old_value, "9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "9"):
                opp_val = getattr(value, "9", None)
                if opp_val is None:
                    setattr(value, "9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__7", None)
        self.__7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "6"):
                opp_val = getattr(old_value, "6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "6"):
                opp_val = getattr(value, "6", None)
                if opp_val is None:
                    setattr(value, "6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_State(NamedElement):

    def __init__(self, initialTime: int, finalTime: int, 1: "fsm_StateMachine" = None, 12: "fsm_StateMachine" = None, fsm_State: "fsm_CompositeState" = None, 17: "fsm_Transition" = None, 20: "fsm_Transition" = None, 6: set["fsm_Transition"] = None, 9: set["fsm_Transition"] = None, fsm_State29: "fsm_Region" = None):
        self.initialTime = initialTime
        self.finalTime = finalTime
        self.1 = 1
        self.12 = 12
        self.fsm_State = fsm_State
        self.17 = 17
        self.20 = 20
        self.6 = 6 if 6 is not None else set()
        self.9 = 9 if 9 is not None else set()
        self.fsm_State29 = fsm_State29
        
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
    def 9(self):
        return self.__9

    @9.setter
    def 9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__9", None)
        self.__9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    if opp_val == self:
                        setattr(item, "10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    setattr(item, "10", self)
                    

    @property
    def fsm_State29(self):
        return self.__fsm_State29

    @fsm_State29.setter
    def fsm_State29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State29", None)
        self.__fsm_State29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Region28"):
                opp_val = getattr(old_value, "fsm_Region28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Region28"):
                opp_val = getattr(value, "fsm_Region28", None)
                if opp_val is None:
                    setattr(value, "fsm_Region28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__20", None)
        self.__20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "19"):
                opp_val = getattr(old_value, "19", None)
                if opp_val == self:
                    setattr(old_value, "19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "19"):
                opp_val = getattr(value, "19", None)
                setattr(value, "19", self)

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__17", None)
        self.__17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "16"):
                opp_val = getattr(old_value, "16", None)
                if opp_val == self:
                    setattr(old_value, "16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "16"):
                opp_val = getattr(value, "16", None)
                setattr(value, "16", self)

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__6", None)
        self.__6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    if opp_val == self:
                        setattr(item, "7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    setattr(item, "7", self)
                    

    @property
    def 12(self):
        return self.__12

    @12.setter
    def 12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__12", None)
        self.__12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "13"):
                opp_val = getattr(old_value, "13", None)
                if opp_val == self:
                    setattr(old_value, "13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "13"):
                opp_val = getattr(value, "13", None)
                setattr(value, "13", self)

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

class fsm_StateMachine(NamedElement):

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
