from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class statemachine_Event:

    def __init__(self, value: bool, statemachine_Event: "statemachine_Condition" = None, statemachine_Event15: "statemachine_Signal" = None):
        self.value = value
        self.statemachine_Event = statemachine_Event
        self.statemachine_Event15 = statemachine_Event15
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def statemachine_Event(self):
        return self.__statemachine_Event

    @statemachine_Event.setter
    def statemachine_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Event__statemachine_Event", None)
        self.__statemachine_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Condition13"):
                opp_val = getattr(old_value, "statemachine_Condition13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Condition13"):
                opp_val = getattr(value, "statemachine_Condition13", None)
                if opp_val is None:
                    setattr(value, "statemachine_Condition13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_Event15(self):
        return self.__statemachine_Event15

    @statemachine_Event15.setter
    def statemachine_Event15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Event__statemachine_Event15", None)
        self.__statemachine_Event15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Signal16"):
                opp_val = getattr(old_value, "statemachine_Signal16", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Signal16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Signal16"):
                opp_val = getattr(value, "statemachine_Signal16", None)
                setattr(value, "statemachine_Signal16", self)

class statemachine_Condition:

    pass
class statemachine_Transition:

    pass
class statemachine_Command:

    def __init__(self, newValue: bool, statemachine_Command: "statemachine_State" = None, statemachine_Command18: "statemachine_Signal" = None):
        self.newValue = newValue
        self.statemachine_Command = statemachine_Command
        self.statemachine_Command18 = statemachine_Command18
        
    @property
    def newValue(self) -> bool:
        return self.__newValue

    @newValue.setter
    def newValue(self, newValue: bool):
        self.__newValue = newValue

    @property
    def statemachine_Command18(self):
        return self.__statemachine_Command18

    @statemachine_Command18.setter
    def statemachine_Command18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Command__statemachine_Command18", None)
        self.__statemachine_Command18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Signal19"):
                opp_val = getattr(old_value, "statemachine_Signal19", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Signal19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Signal19"):
                opp_val = getattr(value, "statemachine_Signal19", None)
                setattr(value, "statemachine_Signal19", self)

    @property
    def statemachine_Command(self):
        return self.__statemachine_Command

    @statemachine_Command.setter
    def statemachine_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Command__statemachine_Command", None)
        self.__statemachine_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State4"):
                opp_val = getattr(old_value, "statemachine_State4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State4"):
                opp_val = getattr(value, "statemachine_State4", None)
                if opp_val is None:
                    setattr(value, "statemachine_State4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Signal:

    pass
class statemachine_OutputSignal(Signal):

    pass
class statemachine_State:

    def __init__(self, name: str, statemachine_State: "statemachine_Statemachine" = None, statemachine_State4: set["statemachine_Command"] = None, statemachine_State6: set["statemachine_Transition"] = None, statemachine_State11: "statemachine_Transition" = None):
        self.name = name
        self.statemachine_State = statemachine_State
        self.statemachine_State4 = statemachine_State4 if statemachine_State4 is not None else set()
        self.statemachine_State6 = statemachine_State6 if statemachine_State6 is not None else set()
        self.statemachine_State11 = statemachine_State11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_State11(self):
        return self.__statemachine_State11

    @statemachine_State11.setter
    def statemachine_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State11", None)
        self.__statemachine_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition10"):
                opp_val = getattr(old_value, "statemachine_Transition10", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition10"):
                opp_val = getattr(value, "statemachine_Transition10", None)
                setattr(value, "statemachine_Transition10", self)

    @property
    def statemachine_State6(self):
        return self.__statemachine_State6

    @statemachine_State6.setter
    def statemachine_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State6", None)
        self.__statemachine_State6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Transition"):
                    opp_val = getattr(item, "statemachine_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Transition"):
                    opp_val = getattr(item, "statemachine_Transition", None)
                    
                    setattr(item, "statemachine_Transition", self)
                    

    @property
    def statemachine_State(self):
        return self.__statemachine_State

    @statemachine_State.setter
    def statemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State", None)
        self.__statemachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statemachine2"):
                opp_val = getattr(old_value, "statemachine_Statemachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine2"):
                opp_val = getattr(value, "statemachine_Statemachine2", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State4(self):
        return self.__statemachine_State4

    @statemachine_State4.setter
    def statemachine_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State4", None)
        self.__statemachine_State4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Command"):
                    opp_val = getattr(item, "statemachine_Command", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Command", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Command"):
                    opp_val = getattr(item, "statemachine_Command", None)
                    
                    setattr(item, "statemachine_Command", self)
                    

class statemachine_Signal:

    def __init__(self, name: str, statemachine_Signal: "statemachine_Statemachine" = None, statemachine_Signal16: "statemachine_Event" = None, statemachine_Signal19: "statemachine_Command" = None):
        self.name = name
        self.statemachine_Signal = statemachine_Signal
        self.statemachine_Signal16 = statemachine_Signal16
        self.statemachine_Signal19 = statemachine_Signal19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_Signal16(self):
        return self.__statemachine_Signal16

    @statemachine_Signal16.setter
    def statemachine_Signal16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Signal__statemachine_Signal16", None)
        self.__statemachine_Signal16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Event15"):
                opp_val = getattr(old_value, "statemachine_Event15", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Event15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Event15"):
                opp_val = getattr(value, "statemachine_Event15", None)
                setattr(value, "statemachine_Event15", self)

    @property
    def statemachine_Signal(self):
        return self.__statemachine_Signal

    @statemachine_Signal.setter
    def statemachine_Signal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Signal__statemachine_Signal", None)
        self.__statemachine_Signal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statemachine"):
                opp_val = getattr(old_value, "statemachine_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine"):
                opp_val = getattr(value, "statemachine_Statemachine", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_Signal19(self):
        return self.__statemachine_Signal19

    @statemachine_Signal19.setter
    def statemachine_Signal19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Signal__statemachine_Signal19", None)
        self.__statemachine_Signal19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Command18"):
                opp_val = getattr(old_value, "statemachine_Command18", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Command18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Command18"):
                opp_val = getattr(value, "statemachine_Command18", None)
                setattr(value, "statemachine_Command18", self)

class statemachine_Statemachine:

    pass
class statemachine_InputSignal(Signal):

    pass