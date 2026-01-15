from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class eMFProject_Transition:

    pass
class eMFProject_Event:

    def __init__(self, name: str, code: str, eMFProject_Event3: "eMFProject_Statemachine" = None, eMFProject_Event: "eMFProject_Statemachine" = None, eMFProject_Event15: "eMFProject_Transition" = None):
        self.name = name
        self.code = code
        self.eMFProject_Event3 = eMFProject_Event3
        self.eMFProject_Event = eMFProject_Event
        self.eMFProject_Event15 = eMFProject_Event15
        
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
    def eMFProject_Event3(self):
        return self.__eMFProject_Event3

    @eMFProject_Event3.setter
    def eMFProject_Event3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eMFProject_Event__eMFProject_Event3", None)
        self.__eMFProject_Event3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eMFProject_Statemachine2"):
                opp_val = getattr(old_value, "eMFProject_Statemachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eMFProject_Statemachine2"):
                opp_val = getattr(value, "eMFProject_Statemachine2", None)
                if opp_val is None:
                    setattr(value, "eMFProject_Statemachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eMFProject_Event15(self):
        return self.__eMFProject_Event15

    @eMFProject_Event15.setter
    def eMFProject_Event15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eMFProject_Event__eMFProject_Event15", None)
        self.__eMFProject_Event15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eMFProject_Transition14"):
                opp_val = getattr(old_value, "eMFProject_Transition14", None)
                if opp_val == self:
                    setattr(old_value, "eMFProject_Transition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eMFProject_Transition14"):
                opp_val = getattr(value, "eMFProject_Transition14", None)
                setattr(value, "eMFProject_Transition14", self)

    @property
    def eMFProject_Event(self):
        return self.__eMFProject_Event

    @eMFProject_Event.setter
    def eMFProject_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eMFProject_Event__eMFProject_Event", None)
        self.__eMFProject_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eMFProject_Statemachine"):
                opp_val = getattr(old_value, "eMFProject_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eMFProject_Statemachine"):
                opp_val = getattr(value, "eMFProject_Statemachine", None)
                if opp_val is None:
                    setattr(value, "eMFProject_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eMFProject_Statemachine:

    pass
class eMFProject_State:

    def __init__(self, name: str, eMFProject_State: "eMFProject_Statemachine" = None, eMFProject_State18: "eMFProject_Transition" = None, eMFProject_State9: set["eMFProject_Command"] = None, eMFProject_State12: set["eMFProject_Transition"] = None):
        self.name = name
        self.eMFProject_State = eMFProject_State
        self.eMFProject_State18 = eMFProject_State18
        self.eMFProject_State9 = eMFProject_State9 if eMFProject_State9 is not None else set()
        self.eMFProject_State12 = eMFProject_State12 if eMFProject_State12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eMFProject_State18(self):
        return self.__eMFProject_State18

    @eMFProject_State18.setter
    def eMFProject_State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eMFProject_State__eMFProject_State18", None)
        self.__eMFProject_State18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eMFProject_Transition17"):
                opp_val = getattr(old_value, "eMFProject_Transition17", None)
                if opp_val == self:
                    setattr(old_value, "eMFProject_Transition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eMFProject_Transition17"):
                opp_val = getattr(value, "eMFProject_Transition17", None)
                setattr(value, "eMFProject_Transition17", self)

    @property
    def eMFProject_State9(self):
        return self.__eMFProject_State9

    @eMFProject_State9.setter
    def eMFProject_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eMFProject_State__eMFProject_State9", None)
        self.__eMFProject_State9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eMFProject_Command10"):
                    opp_val = getattr(item, "eMFProject_Command10", None)
                    
                    if opp_val == self:
                        setattr(item, "eMFProject_Command10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eMFProject_Command10"):
                    opp_val = getattr(item, "eMFProject_Command10", None)
                    
                    setattr(item, "eMFProject_Command10", self)
                    

    @property
    def eMFProject_State12(self):
        return self.__eMFProject_State12

    @eMFProject_State12.setter
    def eMFProject_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eMFProject_State__eMFProject_State12", None)
        self.__eMFProject_State12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eMFProject_Transition"):
                    opp_val = getattr(item, "eMFProject_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "eMFProject_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eMFProject_Transition"):
                    opp_val = getattr(item, "eMFProject_Transition", None)
                    
                    setattr(item, "eMFProject_Transition", self)
                    

    @property
    def eMFProject_State(self):
        return self.__eMFProject_State

    @eMFProject_State.setter
    def eMFProject_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eMFProject_State__eMFProject_State", None)
        self.__eMFProject_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eMFProject_Statemachine7"):
                opp_val = getattr(old_value, "eMFProject_Statemachine7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eMFProject_Statemachine7"):
                opp_val = getattr(value, "eMFProject_Statemachine7", None)
                if opp_val is None:
                    setattr(value, "eMFProject_Statemachine7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eMFProject_Command:

    def __init__(self, name: str, code: str, eMFProject_Command: "eMFProject_Statemachine" = None, eMFProject_Command10: "eMFProject_State" = None):
        self.name = name
        self.code = code
        self.eMFProject_Command = eMFProject_Command
        self.eMFProject_Command10 = eMFProject_Command10
        
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
    def eMFProject_Command(self):
        return self.__eMFProject_Command

    @eMFProject_Command.setter
    def eMFProject_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eMFProject_Command__eMFProject_Command", None)
        self.__eMFProject_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eMFProject_Statemachine5"):
                opp_val = getattr(old_value, "eMFProject_Statemachine5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eMFProject_Statemachine5"):
                opp_val = getattr(value, "eMFProject_Statemachine5", None)
                if opp_val is None:
                    setattr(value, "eMFProject_Statemachine5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eMFProject_Command10(self):
        return self.__eMFProject_Command10

    @eMFProject_Command10.setter
    def eMFProject_Command10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eMFProject_Command__eMFProject_Command10", None)
        self.__eMFProject_Command10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eMFProject_State9"):
                opp_val = getattr(old_value, "eMFProject_State9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eMFProject_State9"):
                opp_val = getattr(value, "eMFProject_State9", None)
                if opp_val is None:
                    setattr(value, "eMFProject_State9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
