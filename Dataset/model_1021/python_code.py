from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class dsl_InitialState(State):

    pass
class dsl_Transition:

    def __init__(self, name: str, trigger: str, dsl_Transition: "dsl_FSM" = None, dsl_Transition6: "dsl_State" = None, dsl_Transition9: "dsl_State" = None):
        self.name = name
        self.trigger = trigger
        self.dsl_Transition = dsl_Transition
        self.dsl_Transition6 = dsl_Transition6
        self.dsl_Transition9 = dsl_Transition9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def dsl_Transition(self):
        return self.__dsl_Transition

    @dsl_Transition.setter
    def dsl_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Transition__dsl_Transition", None)
        self.__dsl_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_FSM2"):
                opp_val = getattr(old_value, "dsl_FSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_FSM2"):
                opp_val = getattr(value, "dsl_FSM2", None)
                if opp_val is None:
                    setattr(value, "dsl_FSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Transition6(self):
        return self.__dsl_Transition6

    @dsl_Transition6.setter
    def dsl_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Transition__dsl_Transition6", None)
        self.__dsl_Transition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_State7"):
                opp_val = getattr(old_value, "dsl_State7", None)
                if opp_val == self:
                    setattr(old_value, "dsl_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_State7"):
                opp_val = getattr(value, "dsl_State7", None)
                setattr(value, "dsl_State7", self)

    @property
    def dsl_Transition9(self):
        return self.__dsl_Transition9

    @dsl_Transition9.setter
    def dsl_Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Transition__dsl_Transition9", None)
        self.__dsl_Transition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_State10"):
                opp_val = getattr(old_value, "dsl_State10", None)
                if opp_val == self:
                    setattr(old_value, "dsl_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_State10"):
                opp_val = getattr(value, "dsl_State10", None)
                setattr(value, "dsl_State10", self)

class dsl_State:

    def __init__(self, name: str, isFinal: bool, dsl_State: "dsl_FSM" = None, dsl_State7: "dsl_Transition" = None, dsl_State10: "dsl_Transition" = None):
        self.name = name
        self.isFinal = isFinal
        self.dsl_State = dsl_State
        self.dsl_State7 = dsl_State7
        self.dsl_State10 = dsl_State10
        
    @property
    def isFinal(self) -> bool:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "dsl_FSM"):
                opp_val = getattr(old_value, "dsl_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_FSM"):
                opp_val = getattr(value, "dsl_FSM", None)
                if opp_val is None:
                    setattr(value, "dsl_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_State7(self):
        return self.__dsl_State7

    @dsl_State7.setter
    def dsl_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State7", None)
        self.__dsl_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Transition6"):
                opp_val = getattr(old_value, "dsl_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Transition6"):
                opp_val = getattr(value, "dsl_Transition6", None)
                setattr(value, "dsl_Transition6", self)

    @property
    def dsl_State10(self):
        return self.__dsl_State10

    @dsl_State10.setter
    def dsl_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State10", None)
        self.__dsl_State10 = value
        
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

class dsl_FSM:

    def __init__(self, name: str, dsl_FSM: set["dsl_State"] = None, dsl_FSM2: set["dsl_Transition"] = None, dsl_FSM4: "dsl_InitialState" = None):
        self.name = name
        self.dsl_FSM = dsl_FSM if dsl_FSM is not None else set()
        self.dsl_FSM2 = dsl_FSM2 if dsl_FSM2 is not None else set()
        self.dsl_FSM4 = dsl_FSM4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_FSM2(self):
        return self.__dsl_FSM2

    @dsl_FSM2.setter
    def dsl_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_FSM__dsl_FSM2", None)
        self.__dsl_FSM2 = value if value is not None else set()
        
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
                    

    @property
    def dsl_FSM(self):
        return self.__dsl_FSM

    @dsl_FSM.setter
    def dsl_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_FSM__dsl_FSM", None)
        self.__dsl_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_State"):
                    opp_val = getattr(item, "dsl_State", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_State"):
                    opp_val = getattr(item, "dsl_State", None)
                    
                    setattr(item, "dsl_State", self)
                    

    @property
    def dsl_FSM4(self):
        return self.__dsl_FSM4

    @dsl_FSM4.setter
    def dsl_FSM4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_FSM__dsl_FSM4", None)
        self.__dsl_FSM4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_InitialState"):
                opp_val = getattr(old_value, "dsl_InitialState", None)
                if opp_val == self:
                    setattr(old_value, "dsl_InitialState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_InitialState"):
                opp_val = getattr(value, "dsl_InitialState", None)
                setattr(value, "dsl_InitialState", self)
