from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class statemachine_State:

    def __init__(self, name: str, statemachine_State9: set["statemachine_Command"] = None, statemachine_State12: set["statemachine_Transition"] = None, statemachine_State: "statemachine_Statemachine" = None, statemachine_State18: "statemachine_Transition" = None):
        self.name = name
        self.statemachine_State9 = statemachine_State9 if statemachine_State9 is not None else set()
        self.statemachine_State12 = statemachine_State12 if statemachine_State12 is not None else set()
        self.statemachine_State = statemachine_State
        self.statemachine_State18 = statemachine_State18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_State18(self):
        return self.__statemachine_State18

    @statemachine_State18.setter
    def statemachine_State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State18", None)
        self.__statemachine_State18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition17"):
                opp_val = getattr(old_value, "statemachine_Transition17", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition17"):
                opp_val = getattr(value, "statemachine_Transition17", None)
                setattr(value, "statemachine_Transition17", self)

    @property
    def statemachine_State9(self):
        return self.__statemachine_State9

    @statemachine_State9.setter
    def statemachine_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State9", None)
        self.__statemachine_State9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Command10"):
                    opp_val = getattr(item, "statemachine_Command10", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Command10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Command10"):
                    opp_val = getattr(item, "statemachine_Command10", None)
                    
                    setattr(item, "statemachine_Command10", self)
                    

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
            if hasattr(old_value, "statemachine_Statemachine7"):
                opp_val = getattr(old_value, "statemachine_Statemachine7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine7"):
                opp_val = getattr(value, "statemachine_Statemachine7", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State12(self):
        return self.__statemachine_State12

    @statemachine_State12.setter
    def statemachine_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State12", None)
        self.__statemachine_State12 = value if value is not None else set()
        
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
                    

class statemachine_Command:

    def __init__(self, code: str, name: str, statemachine_Command10: "statemachine_State" = None, statemachine_Command: "statemachine_Statemachine" = None):
        self.code = code
        self.name = name
        self.statemachine_Command10 = statemachine_Command10
        self.statemachine_Command = statemachine_Command
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "statemachine_Statemachine5"):
                opp_val = getattr(old_value, "statemachine_Statemachine5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine5"):
                opp_val = getattr(value, "statemachine_Statemachine5", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_Command10(self):
        return self.__statemachine_Command10

    @statemachine_Command10.setter
    def statemachine_Command10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Command__statemachine_Command10", None)
        self.__statemachine_Command10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State9"):
                opp_val = getattr(old_value, "statemachine_State9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State9"):
                opp_val = getattr(value, "statemachine_State9", None)
                if opp_val is None:
                    setattr(value, "statemachine_State9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_Event:

    def __init__(self, name: str, code: str, statemachine_Event: "statemachine_Statemachine" = None, statemachine_Event3: "statemachine_Statemachine" = None, statemachine_Event15: "statemachine_Transition" = None):
        self.name = name
        self.code = code
        self.statemachine_Event = statemachine_Event
        self.statemachine_Event3 = statemachine_Event3
        self.statemachine_Event15 = statemachine_Event15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

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
    def statemachine_Event15(self):
        return self.__statemachine_Event15

    @statemachine_Event15.setter
    def statemachine_Event15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Event__statemachine_Event15", None)
        self.__statemachine_Event15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition14"):
                opp_val = getattr(old_value, "statemachine_Transition14", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition14"):
                opp_val = getattr(value, "statemachine_Transition14", None)
                setattr(value, "statemachine_Transition14", self)

    @property
    def statemachine_Event3(self):
        return self.__statemachine_Event3

    @statemachine_Event3.setter
    def statemachine_Event3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Event__statemachine_Event3", None)
        self.__statemachine_Event3 = value
        
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

class statemachine_Transition:

    pass
class statemachine_Statemachine:

    pass