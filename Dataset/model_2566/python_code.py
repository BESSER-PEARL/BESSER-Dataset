from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dsl_State:

    def __init__(self, name: str, dsl_State7: set["dsl_Transition"] = None, dsl_State13: "dsl_Transition" = None, dsl_State: "dsl_StateMachine" = None, dsl_State5: "dsl_StateMachine" = None):
        self.name = name
        self.dsl_State7 = dsl_State7 if dsl_State7 is not None else set()
        self.dsl_State13 = dsl_State13
        self.dsl_State = dsl_State
        self.dsl_State5 = dsl_State5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_State5(self):
        return self.__dsl_State5

    @dsl_State5.setter
    def dsl_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State5", None)
        self.__dsl_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_StateMachine4"):
                opp_val = getattr(old_value, "dsl_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_StateMachine4"):
                opp_val = getattr(value, "dsl_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "dsl_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_State13(self):
        return self.__dsl_State13

    @dsl_State13.setter
    def dsl_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State13", None)
        self.__dsl_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Transition12"):
                opp_val = getattr(old_value, "dsl_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Transition12"):
                opp_val = getattr(value, "dsl_Transition12", None)
                setattr(value, "dsl_Transition12", self)

    @property
    def dsl_State(self):
        return self.__dsl_State

    @dsl_State.setter
    def dsl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State", None)
        self.__dsl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_StateMachine2"):
                opp_val = getattr(old_value, "dsl_StateMachine2", None)
                if opp_val == self:
                    setattr(old_value, "dsl_StateMachine2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_StateMachine2"):
                opp_val = getattr(value, "dsl_StateMachine2", None)
                setattr(value, "dsl_StateMachine2", self)

    @property
    def dsl_State7(self):
        return self.__dsl_State7

    @dsl_State7.setter
    def dsl_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State7", None)
        self.__dsl_State7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Transition"):
                    opp_val = getattr(item, "dsl_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Transition"):
                    opp_val = getattr(item, "dsl_Transition", None)
                    
                    setattr(item, "dsl_Transition", self)
                    

class dsl_Transition:

    pass
class dsl_Event:

    def __init__(self, name: str, dsl_Event: "dsl_StateMachine" = None, dsl_Event10: "dsl_Transition" = None):
        self.name = name
        self.dsl_Event = dsl_Event
        self.dsl_Event10 = dsl_Event10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Event(self):
        return self.__dsl_Event

    @dsl_Event.setter
    def dsl_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Event__dsl_Event", None)
        self.__dsl_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_StateMachine"):
                opp_val = getattr(old_value, "dsl_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_StateMachine"):
                opp_val = getattr(value, "dsl_StateMachine", None)
                if opp_val is None:
                    setattr(value, "dsl_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Event10(self):
        return self.__dsl_Event10

    @dsl_Event10.setter
    def dsl_Event10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Event__dsl_Event10", None)
        self.__dsl_Event10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Transition9"):
                opp_val = getattr(old_value, "dsl_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Transition9"):
                opp_val = getattr(value, "dsl_Transition9", None)
                setattr(value, "dsl_Transition9", self)

class dsl_StateMachine:

    pass