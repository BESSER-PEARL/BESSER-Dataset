from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class statemachine_Statemachine:

    pass
class statemachine_Transition:

    pass
class NamedElement:

    pass
class statemachine_Event(NamedElement):

    def __init__(self, code: str, statemachine_Event3: "statemachine_Statemachine" = None, statemachine_Event15: "statemachine_Transition" = None, statemachine_Event: "statemachine_Statemachine" = None):
        self.code = code
        self.statemachine_Event3 = statemachine_Event3
        self.statemachine_Event15 = statemachine_Event15
        self.statemachine_Event = statemachine_Event
        
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

class statemachine_NamedElement:

    def __init__(self, name: str, displayname: str):
        self.name = name
        self.displayname = displayname
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def displayname(self) -> str:
        return self.__displayname

    @displayname.setter
    def displayname(self, displayname: str):
        self.__displayname = displayname

class statemachine_State(NamedElement):

    pass
class statemachine_Command(NamedElement):

    def __init__(self, code: str, statemachine_Command: "statemachine_Statemachine" = None, statemachine_Command10: "statemachine_State" = None):
        self.code = code
        self.statemachine_Command = statemachine_Command
        self.statemachine_Command10 = statemachine_Command10
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

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
