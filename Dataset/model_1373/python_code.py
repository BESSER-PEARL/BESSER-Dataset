from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class statemachines_Event:

    def __init__(self, name: str, code: str, statemachines_Event5: "statemachines_StateMachine" = None, statemachines_Event13: "statemachines_Transition" = None, statemachines_Event: "statemachines_StateMachine" = None):
        self.name = name
        self.code = code
        self.statemachines_Event5 = statemachines_Event5
        self.statemachines_Event13 = statemachines_Event13
        self.statemachines_Event = statemachines_Event
        
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
    def statemachines_Event(self):
        return self.__statemachines_Event

    @statemachines_Event.setter
    def statemachines_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Event__statemachines_Event", None)
        self.__statemachines_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_StateMachine2"):
                opp_val = getattr(old_value, "statemachines_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_StateMachine2"):
                opp_val = getattr(value, "statemachines_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "statemachines_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachines_Event13(self):
        return self.__statemachines_Event13

    @statemachines_Event13.setter
    def statemachines_Event13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Event__statemachines_Event13", None)
        self.__statemachines_Event13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Transition12"):
                opp_val = getattr(old_value, "statemachines_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Transition12"):
                opp_val = getattr(value, "statemachines_Transition12", None)
                setattr(value, "statemachines_Transition12", self)

    @property
    def statemachines_Event5(self):
        return self.__statemachines_Event5

    @statemachines_Event5.setter
    def statemachines_Event5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Event__statemachines_Event5", None)
        self.__statemachines_Event5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_StateMachine4"):
                opp_val = getattr(old_value, "statemachines_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_StateMachine4"):
                opp_val = getattr(value, "statemachines_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "statemachines_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachines_Transition:

    pass
class statemachines_State:

    def __init__(self, name: str, statemachines_State: "statemachines_StateMachine" = None, statemachines_State7: set["statemachines_Transition"] = None, statemachines_State10: "statemachines_Transition" = None):
        self.name = name
        self.statemachines_State = statemachines_State
        self.statemachines_State7 = statemachines_State7 if statemachines_State7 is not None else set()
        self.statemachines_State10 = statemachines_State10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachines_State(self):
        return self.__statemachines_State

    @statemachines_State.setter
    def statemachines_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State", None)
        self.__statemachines_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_StateMachine"):
                opp_val = getattr(old_value, "statemachines_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_StateMachine"):
                opp_val = getattr(value, "statemachines_StateMachine", None)
                if opp_val is None:
                    setattr(value, "statemachines_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachines_State7(self):
        return self.__statemachines_State7

    @statemachines_State7.setter
    def statemachines_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State7", None)
        self.__statemachines_State7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachines_Transition"):
                    opp_val = getattr(item, "statemachines_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachines_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachines_Transition"):
                    opp_val = getattr(item, "statemachines_Transition", None)
                    
                    setattr(item, "statemachines_Transition", self)
                    

    @property
    def statemachines_State10(self):
        return self.__statemachines_State10

    @statemachines_State10.setter
    def statemachines_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State10", None)
        self.__statemachines_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Transition9"):
                opp_val = getattr(old_value, "statemachines_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Transition9"):
                opp_val = getattr(value, "statemachines_Transition9", None)
                setattr(value, "statemachines_Transition9", self)

class statemachines_StateMachine:

    pass