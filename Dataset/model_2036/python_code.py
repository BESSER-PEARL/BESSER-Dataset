from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class stm_Parameter:

    def __init__(self, name: str, type: str, stm_Parameter: "stm_Guard" = None):
        self.name = name
        self.type = type
        self.stm_Parameter = stm_Parameter
        
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
    def stm_Parameter(self):
        return self.__stm_Parameter

    @stm_Parameter.setter
    def stm_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Parameter__stm_Parameter", None)
        self.__stm_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_Guard50"):
                opp_val = getattr(old_value, "stm_Guard50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_Guard50"):
                opp_val = getattr(value, "stm_Guard50", None)
                if opp_val is None:
                    setattr(value, "stm_Guard50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class stm_GuardCall:

    def __init__(self, parameters: str, stm_GuardCall42: "stm_SelfEvent" = None, stm_GuardCall: "stm_Transition" = None, stm_GuardCall47: "stm_Guard" = None):
        self.parameters = parameters
        self.stm_GuardCall42 = stm_GuardCall42
        self.stm_GuardCall = stm_GuardCall
        self.stm_GuardCall47 = stm_GuardCall47
        
    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def stm_GuardCall47(self):
        return self.__stm_GuardCall47

    @stm_GuardCall47.setter
    def stm_GuardCall47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_GuardCall__stm_GuardCall47", None)
        self.__stm_GuardCall47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_Guard48"):
                opp_val = getattr(old_value, "stm_Guard48", None)
                if opp_val == self:
                    setattr(old_value, "stm_Guard48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_Guard48"):
                opp_val = getattr(value, "stm_Guard48", None)
                setattr(value, "stm_Guard48", self)

    @property
    def stm_GuardCall42(self):
        return self.__stm_GuardCall42

    @stm_GuardCall42.setter
    def stm_GuardCall42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_GuardCall__stm_GuardCall42", None)
        self.__stm_GuardCall42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_SelfEvent41"):
                opp_val = getattr(old_value, "stm_SelfEvent41", None)
                if opp_val == self:
                    setattr(old_value, "stm_SelfEvent41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_SelfEvent41"):
                opp_val = getattr(value, "stm_SelfEvent41", None)
                setattr(value, "stm_SelfEvent41", self)

    @property
    def stm_GuardCall(self):
        return self.__stm_GuardCall

    @stm_GuardCall.setter
    def stm_GuardCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_GuardCall__stm_GuardCall", None)
        self.__stm_GuardCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_Transition30"):
                opp_val = getattr(old_value, "stm_Transition30", None)
                if opp_val == self:
                    setattr(old_value, "stm_Transition30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_Transition30"):
                opp_val = getattr(value, "stm_Transition30", None)
                setattr(value, "stm_Transition30", self)

class stm_Transition:

    pass
class stm_State:

    def __init__(self, name: str, stm_State11: "stm_Command" = None, stm_State14: "stm_Command" = None, stm_State18: "stm_State" = None, stm_State16: set["stm_State"] = None, stm_State: "stm_Statemachine" = None, stm_State8: set["stm_Command"] = None, stm_State20: set["stm_SelfEvent"] = None, stm_State22: set["stm_Transition"] = None, stm_State24: set["stm_Command"] = None, stm_State33: "stm_Transition" = None):
        self.name = name
        self.stm_State11 = stm_State11
        self.stm_State14 = stm_State14
        self.stm_State18 = stm_State18
        self.stm_State16 = stm_State16 if stm_State16 is not None else set()
        self.stm_State = stm_State
        self.stm_State8 = stm_State8 if stm_State8 is not None else set()
        self.stm_State20 = stm_State20 if stm_State20 is not None else set()
        self.stm_State22 = stm_State22 if stm_State22 is not None else set()
        self.stm_State24 = stm_State24 if stm_State24 is not None else set()
        self.stm_State33 = stm_State33
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stm_State11(self):
        return self.__stm_State11

    @stm_State11.setter
    def stm_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_State__stm_State11", None)
        self.__stm_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_Command12"):
                opp_val = getattr(old_value, "stm_Command12", None)
                if opp_val == self:
                    setattr(old_value, "stm_Command12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_Command12"):
                opp_val = getattr(value, "stm_Command12", None)
                setattr(value, "stm_Command12", self)

    @property
    def stm_State33(self):
        return self.__stm_State33

    @stm_State33.setter
    def stm_State33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_State__stm_State33", None)
        self.__stm_State33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_Transition32"):
                opp_val = getattr(old_value, "stm_Transition32", None)
                if opp_val == self:
                    setattr(old_value, "stm_Transition32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_Transition32"):
                opp_val = getattr(value, "stm_Transition32", None)
                setattr(value, "stm_Transition32", self)

    @property
    def stm_State20(self):
        return self.__stm_State20

    @stm_State20.setter
    def stm_State20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_State__stm_State20", None)
        self.__stm_State20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stm_SelfEvent"):
                    opp_val = getattr(item, "stm_SelfEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "stm_SelfEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stm_SelfEvent"):
                    opp_val = getattr(item, "stm_SelfEvent", None)
                    
                    setattr(item, "stm_SelfEvent", self)
                    

    @property
    def stm_State24(self):
        return self.__stm_State24

    @stm_State24.setter
    def stm_State24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_State__stm_State24", None)
        self.__stm_State24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stm_Command25"):
                    opp_val = getattr(item, "stm_Command25", None)
                    
                    if opp_val == self:
                        setattr(item, "stm_Command25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stm_Command25"):
                    opp_val = getattr(item, "stm_Command25", None)
                    
                    setattr(item, "stm_Command25", self)
                    

    @property
    def stm_State22(self):
        return self.__stm_State22

    @stm_State22.setter
    def stm_State22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_State__stm_State22", None)
        self.__stm_State22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stm_Transition"):
                    opp_val = getattr(item, "stm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "stm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stm_Transition"):
                    opp_val = getattr(item, "stm_Transition", None)
                    
                    setattr(item, "stm_Transition", self)
                    

    @property
    def stm_State16(self):
        return self.__stm_State16

    @stm_State16.setter
    def stm_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_State__stm_State16", None)
        self.__stm_State16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stm_State18"):
                    opp_val = getattr(item, "stm_State18", None)
                    
                    if opp_val == self:
                        setattr(item, "stm_State18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stm_State18"):
                    opp_val = getattr(item, "stm_State18", None)
                    
                    setattr(item, "stm_State18", self)
                    

    @property
    def stm_State(self):
        return self.__stm_State

    @stm_State.setter
    def stm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_State__stm_State", None)
        self.__stm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_Statemachine6"):
                opp_val = getattr(old_value, "stm_Statemachine6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_Statemachine6"):
                opp_val = getattr(value, "stm_Statemachine6", None)
                if opp_val is None:
                    setattr(value, "stm_Statemachine6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stm_State8(self):
        return self.__stm_State8

    @stm_State8.setter
    def stm_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_State__stm_State8", None)
        self.__stm_State8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stm_Command9"):
                    opp_val = getattr(item, "stm_Command9", None)
                    
                    if opp_val == self:
                        setattr(item, "stm_Command9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stm_Command9"):
                    opp_val = getattr(item, "stm_Command9", None)
                    
                    setattr(item, "stm_Command9", self)
                    

    @property
    def stm_State14(self):
        return self.__stm_State14

    @stm_State14.setter
    def stm_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_State__stm_State14", None)
        self.__stm_State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_Command15"):
                opp_val = getattr(old_value, "stm_Command15", None)
                if opp_val == self:
                    setattr(old_value, "stm_Command15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_Command15"):
                opp_val = getattr(value, "stm_Command15", None)
                setattr(value, "stm_Command15", self)

    @property
    def stm_State18(self):
        return self.__stm_State18

    @stm_State18.setter
    def stm_State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_State__stm_State18", None)
        self.__stm_State18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_State16"):
                opp_val = getattr(old_value, "stm_State16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_State16"):
                opp_val = getattr(value, "stm_State16", None)
                if opp_val is None:
                    setattr(value, "stm_State16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class stm_Guard:

    def __init__(self, name: str, stm_Guard: "stm_Statemachine" = None, stm_Guard48: "stm_GuardCall" = None, stm_Guard50: set["stm_Parameter"] = None):
        self.name = name
        self.stm_Guard = stm_Guard
        self.stm_Guard48 = stm_Guard48
        self.stm_Guard50 = stm_Guard50 if stm_Guard50 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stm_Guard(self):
        return self.__stm_Guard

    @stm_Guard.setter
    def stm_Guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Guard__stm_Guard", None)
        self.__stm_Guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_Statemachine4"):
                opp_val = getattr(old_value, "stm_Statemachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_Statemachine4"):
                opp_val = getattr(value, "stm_Statemachine4", None)
                if opp_val is None:
                    setattr(value, "stm_Statemachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stm_Guard48(self):
        return self.__stm_Guard48

    @stm_Guard48.setter
    def stm_Guard48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Guard__stm_Guard48", None)
        self.__stm_Guard48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_GuardCall47"):
                opp_val = getattr(old_value, "stm_GuardCall47", None)
                if opp_val == self:
                    setattr(old_value, "stm_GuardCall47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_GuardCall47"):
                opp_val = getattr(value, "stm_GuardCall47", None)
                setattr(value, "stm_GuardCall47", self)

    @property
    def stm_Guard50(self):
        return self.__stm_Guard50

    @stm_Guard50.setter
    def stm_Guard50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Guard__stm_Guard50", None)
        self.__stm_Guard50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stm_Parameter"):
                    opp_val = getattr(item, "stm_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "stm_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stm_Parameter"):
                    opp_val = getattr(item, "stm_Parameter", None)
                    
                    setattr(item, "stm_Parameter", self)
                    

class stm_Command:

    def __init__(self, name: str, stm_Command15: "stm_State" = None, stm_Command: "stm_Statemachine" = None, stm_Command9: "stm_State" = None, stm_Command12: "stm_State" = None, stm_Command45: "stm_SelfEvent" = None, stm_Command25: "stm_State" = None, stm_Command36: "stm_Transition" = None):
        self.name = name
        self.stm_Command15 = stm_Command15
        self.stm_Command = stm_Command
        self.stm_Command9 = stm_Command9
        self.stm_Command12 = stm_Command12
        self.stm_Command45 = stm_Command45
        self.stm_Command25 = stm_Command25
        self.stm_Command36 = stm_Command36
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stm_Command25(self):
        return self.__stm_Command25

    @stm_Command25.setter
    def stm_Command25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Command__stm_Command25", None)
        self.__stm_Command25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_State24"):
                opp_val = getattr(old_value, "stm_State24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_State24"):
                opp_val = getattr(value, "stm_State24", None)
                if opp_val is None:
                    setattr(value, "stm_State24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stm_Command45(self):
        return self.__stm_Command45

    @stm_Command45.setter
    def stm_Command45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Command__stm_Command45", None)
        self.__stm_Command45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_SelfEvent44"):
                opp_val = getattr(old_value, "stm_SelfEvent44", None)
                if opp_val == self:
                    setattr(old_value, "stm_SelfEvent44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_SelfEvent44"):
                opp_val = getattr(value, "stm_SelfEvent44", None)
                setattr(value, "stm_SelfEvent44", self)

    @property
    def stm_Command9(self):
        return self.__stm_Command9

    @stm_Command9.setter
    def stm_Command9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Command__stm_Command9", None)
        self.__stm_Command9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_State8"):
                opp_val = getattr(old_value, "stm_State8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_State8"):
                opp_val = getattr(value, "stm_State8", None)
                if opp_val is None:
                    setattr(value, "stm_State8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stm_Command(self):
        return self.__stm_Command

    @stm_Command.setter
    def stm_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Command__stm_Command", None)
        self.__stm_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_Statemachine2"):
                opp_val = getattr(old_value, "stm_Statemachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_Statemachine2"):
                opp_val = getattr(value, "stm_Statemachine2", None)
                if opp_val is None:
                    setattr(value, "stm_Statemachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stm_Command36(self):
        return self.__stm_Command36

    @stm_Command36.setter
    def stm_Command36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Command__stm_Command36", None)
        self.__stm_Command36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_Transition35"):
                opp_val = getattr(old_value, "stm_Transition35", None)
                if opp_val == self:
                    setattr(old_value, "stm_Transition35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_Transition35"):
                opp_val = getattr(value, "stm_Transition35", None)
                setattr(value, "stm_Transition35", self)

    @property
    def stm_Command12(self):
        return self.__stm_Command12

    @stm_Command12.setter
    def stm_Command12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Command__stm_Command12", None)
        self.__stm_Command12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_State11"):
                opp_val = getattr(old_value, "stm_State11", None)
                if opp_val == self:
                    setattr(old_value, "stm_State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_State11"):
                opp_val = getattr(value, "stm_State11", None)
                setattr(value, "stm_State11", self)

    @property
    def stm_Command15(self):
        return self.__stm_Command15

    @stm_Command15.setter
    def stm_Command15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Command__stm_Command15", None)
        self.__stm_Command15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_State14"):
                opp_val = getattr(old_value, "stm_State14", None)
                if opp_val == self:
                    setattr(old_value, "stm_State14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_State14"):
                opp_val = getattr(value, "stm_State14", None)
                setattr(value, "stm_State14", self)

class stm_SelfEvent:

    pass
class stm_Event:

    def __init__(self, name: str, stm_Event: "stm_Statemachine" = None, stm_Event39: "stm_SelfEvent" = None, stm_Event28: "stm_Transition" = None):
        self.name = name
        self.stm_Event = stm_Event
        self.stm_Event39 = stm_Event39
        self.stm_Event28 = stm_Event28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stm_Event39(self):
        return self.__stm_Event39

    @stm_Event39.setter
    def stm_Event39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Event__stm_Event39", None)
        self.__stm_Event39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_SelfEvent38"):
                opp_val = getattr(old_value, "stm_SelfEvent38", None)
                if opp_val == self:
                    setattr(old_value, "stm_SelfEvent38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_SelfEvent38"):
                opp_val = getattr(value, "stm_SelfEvent38", None)
                setattr(value, "stm_SelfEvent38", self)

    @property
    def stm_Event28(self):
        return self.__stm_Event28

    @stm_Event28.setter
    def stm_Event28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Event__stm_Event28", None)
        self.__stm_Event28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_Transition27"):
                opp_val = getattr(old_value, "stm_Transition27", None)
                if opp_val == self:
                    setattr(old_value, "stm_Transition27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_Transition27"):
                opp_val = getattr(value, "stm_Transition27", None)
                setattr(value, "stm_Transition27", self)

    @property
    def stm_Event(self):
        return self.__stm_Event

    @stm_Event.setter
    def stm_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stm_Event__stm_Event", None)
        self.__stm_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stm_Statemachine"):
                opp_val = getattr(old_value, "stm_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stm_Statemachine"):
                opp_val = getattr(value, "stm_Statemachine", None)
                if opp_val is None:
                    setattr(value, "stm_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class stm_Statemachine:

    pass