from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fowlerdsl_Transition:

    pass
class fowlerdsl_State:

    def __init__(self, name: str, fowlerdsl_State: "fowlerdsl_Statemachine" = None, fowlerdsl_State6: set["fowlerdsl_Command"] = None, fowlerdsl_State9: set["fowlerdsl_Transition"] = None, fowlerdsl_State15: "fowlerdsl_Transition" = None):
        self.name = name
        self.fowlerdsl_State = fowlerdsl_State
        self.fowlerdsl_State6 = fowlerdsl_State6 if fowlerdsl_State6 is not None else set()
        self.fowlerdsl_State9 = fowlerdsl_State9 if fowlerdsl_State9 is not None else set()
        self.fowlerdsl_State15 = fowlerdsl_State15
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def fowlerdsl_State15(self):
        return self.__fowlerdsl_State15

    @fowlerdsl_State15.setter
    def fowlerdsl_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fowlerdsl_State__fowlerdsl_State15", None)
        self.__fowlerdsl_State15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fowlerdsl_Transition14"):
                opp_val = getattr(old_value, "fowlerdsl_Transition14", None)
                if opp_val == self:
                    setattr(old_value, "fowlerdsl_Transition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fowlerdsl_Transition14"):
                opp_val = getattr(value, "fowlerdsl_Transition14", None)
                setattr(value, "fowlerdsl_Transition14", self)

    @property
    def fowlerdsl_State6(self):
        return self.__fowlerdsl_State6

    @fowlerdsl_State6.setter
    def fowlerdsl_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fowlerdsl_State__fowlerdsl_State6", None)
        self.__fowlerdsl_State6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fowlerdsl_Command7"):
                    opp_val = getattr(item, "fowlerdsl_Command7", None)
                    
                    if opp_val == self:
                        setattr(item, "fowlerdsl_Command7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fowlerdsl_Command7"):
                    opp_val = getattr(item, "fowlerdsl_Command7", None)
                    
                    setattr(item, "fowlerdsl_Command7", self)
                    

    @property
    def fowlerdsl_State9(self):
        return self.__fowlerdsl_State9

    @fowlerdsl_State9.setter
    def fowlerdsl_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fowlerdsl_State__fowlerdsl_State9", None)
        self.__fowlerdsl_State9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fowlerdsl_Transition"):
                    opp_val = getattr(item, "fowlerdsl_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fowlerdsl_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fowlerdsl_Transition"):
                    opp_val = getattr(item, "fowlerdsl_Transition", None)
                    
                    setattr(item, "fowlerdsl_Transition", self)
                    

    @property
    def fowlerdsl_State(self):
        return self.__fowlerdsl_State

    @fowlerdsl_State.setter
    def fowlerdsl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fowlerdsl_State__fowlerdsl_State", None)
        self.__fowlerdsl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fowlerdsl_Statemachine4"):
                opp_val = getattr(old_value, "fowlerdsl_Statemachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fowlerdsl_Statemachine4"):
                opp_val = getattr(value, "fowlerdsl_Statemachine4", None)
                if opp_val is None:
                    setattr(value, "fowlerdsl_Statemachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fowlerdsl_Command:

    def __init__(self, name: str, code: str, fowlerdsl_Command: "fowlerdsl_Statemachine" = None, fowlerdsl_Command7: "fowlerdsl_State" = None):
        self.name = name
        self.code = code
        self.fowlerdsl_Command = fowlerdsl_Command
        self.fowlerdsl_Command7 = fowlerdsl_Command7
        
        pass
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def fowlerdsl_Command(self):
        return self.__fowlerdsl_Command

    @fowlerdsl_Command.setter
    def fowlerdsl_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fowlerdsl_Command__fowlerdsl_Command", None)
        self.__fowlerdsl_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fowlerdsl_Statemachine2"):
                opp_val = getattr(old_value, "fowlerdsl_Statemachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fowlerdsl_Statemachine2"):
                opp_val = getattr(value, "fowlerdsl_Statemachine2", None)
                if opp_val is None:
                    setattr(value, "fowlerdsl_Statemachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fowlerdsl_Command7(self):
        return self.__fowlerdsl_Command7

    @fowlerdsl_Command7.setter
    def fowlerdsl_Command7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fowlerdsl_Command__fowlerdsl_Command7", None)
        self.__fowlerdsl_Command7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fowlerdsl_State6"):
                opp_val = getattr(old_value, "fowlerdsl_State6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fowlerdsl_State6"):
                opp_val = getattr(value, "fowlerdsl_State6", None)
                if opp_val is None:
                    setattr(value, "fowlerdsl_State6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fowlerdsl_Event:

    def __init__(self, resetting: bool, name: str, code: str, fowlerdsl_Event: "fowlerdsl_Statemachine" = None, fowlerdsl_Event12: "fowlerdsl_Transition" = None):
        self.resetting = resetting
        self.name = name
        self.code = code
        self.fowlerdsl_Event = fowlerdsl_Event
        self.fowlerdsl_Event12 = fowlerdsl_Event12
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def resetting(self):
        return self.__resetting

    @resetting.setter
    def resetting(self, resetting: bool):
        self.__resetting = resetting


    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


    @property
    def fowlerdsl_Event(self):
        return self.__fowlerdsl_Event

    @fowlerdsl_Event.setter
    def fowlerdsl_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fowlerdsl_Event__fowlerdsl_Event", None)
        self.__fowlerdsl_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fowlerdsl_Statemachine"):
                opp_val = getattr(old_value, "fowlerdsl_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fowlerdsl_Statemachine"):
                opp_val = getattr(value, "fowlerdsl_Statemachine", None)
                if opp_val is None:
                    setattr(value, "fowlerdsl_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fowlerdsl_Event12(self):
        return self.__fowlerdsl_Event12

    @fowlerdsl_Event12.setter
    def fowlerdsl_Event12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fowlerdsl_Event__fowlerdsl_Event12", None)
        self.__fowlerdsl_Event12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fowlerdsl_Transition11"):
                opp_val = getattr(old_value, "fowlerdsl_Transition11", None)
                if opp_val == self:
                    setattr(old_value, "fowlerdsl_Transition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fowlerdsl_Transition11"):
                opp_val = getattr(value, "fowlerdsl_Transition11", None)
                setattr(value, "fowlerdsl_Transition11", self)

class fowlerdsl_Statemachine:

    pass