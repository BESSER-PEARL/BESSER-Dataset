from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class statemachine_FinalState(State):

    pass
class statemachine_MyFSM:

    def __init__(self, name: str, statemachine_MyFSM: set["statemachine_State"] = None, statemachine_MyFSM2: set["statemachine_Transition"] = None, statemachine_MyFSM4: "statemachine_InitialState" = None):
        self.name = name
        self.statemachine_MyFSM = statemachine_MyFSM if statemachine_MyFSM is not None else set()
        self.statemachine_MyFSM2 = statemachine_MyFSM2 if statemachine_MyFSM2 is not None else set()
        self.statemachine_MyFSM4 = statemachine_MyFSM4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_MyFSM(self):
        return self.__statemachine_MyFSM

    @statemachine_MyFSM.setter
    def statemachine_MyFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_MyFSM__statemachine_MyFSM", None)
        self.__statemachine_MyFSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_State"):
                    opp_val = getattr(item, "statemachine_State", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_State"):
                    opp_val = getattr(item, "statemachine_State", None)
                    
                    setattr(item, "statemachine_State", self)
                    

    @property
    def statemachine_MyFSM4(self):
        return self.__statemachine_MyFSM4

    @statemachine_MyFSM4.setter
    def statemachine_MyFSM4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_MyFSM__statemachine_MyFSM4", None)
        self.__statemachine_MyFSM4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_InitialState"):
                opp_val = getattr(old_value, "statemachine_InitialState", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_InitialState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_InitialState"):
                opp_val = getattr(value, "statemachine_InitialState", None)
                setattr(value, "statemachine_InitialState", self)

    @property
    def statemachine_MyFSM2(self):
        return self.__statemachine_MyFSM2

    @statemachine_MyFSM2.setter
    def statemachine_MyFSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_MyFSM__statemachine_MyFSM2", None)
        self.__statemachine_MyFSM2 = value if value is not None else set()
        
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
                    

class statemachine_InitialState(State):

    pass
class statemachine_Transition:

    def __init__(self, name: str, statemachine_Transition: "statemachine_MyFSM" = None, statemachine_Transition6: "statemachine_State" = None, statemachine_Transition9: "statemachine_State" = None):
        self.name = name
        self.statemachine_Transition = statemachine_Transition
        self.statemachine_Transition6 = statemachine_Transition6
        self.statemachine_Transition9 = statemachine_Transition9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_Transition9(self):
        return self.__statemachine_Transition9

    @statemachine_Transition9.setter
    def statemachine_Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition9", None)
        self.__statemachine_Transition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State10"):
                opp_val = getattr(old_value, "statemachine_State10", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State10"):
                opp_val = getattr(value, "statemachine_State10", None)
                setattr(value, "statemachine_State10", self)

    @property
    def statemachine_Transition6(self):
        return self.__statemachine_Transition6

    @statemachine_Transition6.setter
    def statemachine_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition6", None)
        self.__statemachine_Transition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State7"):
                opp_val = getattr(old_value, "statemachine_State7", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State7"):
                opp_val = getattr(value, "statemachine_State7", None)
                setattr(value, "statemachine_State7", self)

    @property
    def statemachine_Transition(self):
        return self.__statemachine_Transition

    @statemachine_Transition.setter
    def statemachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition", None)
        self.__statemachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_MyFSM2"):
                opp_val = getattr(old_value, "statemachine_MyFSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_MyFSM2"):
                opp_val = getattr(value, "statemachine_MyFSM2", None)
                if opp_val is None:
                    setattr(value, "statemachine_MyFSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_State:

    def __init__(self, name: str, statemachine_State: "statemachine_MyFSM" = None, statemachine_State7: "statemachine_Transition" = None, statemachine_State10: "statemachine_Transition" = None):
        self.name = name
        self.statemachine_State = statemachine_State
        self.statemachine_State7 = statemachine_State7
        self.statemachine_State10 = statemachine_State10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_State7(self):
        return self.__statemachine_State7

    @statemachine_State7.setter
    def statemachine_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State7", None)
        self.__statemachine_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition6"):
                opp_val = getattr(old_value, "statemachine_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition6"):
                opp_val = getattr(value, "statemachine_Transition6", None)
                setattr(value, "statemachine_Transition6", self)

    @property
    def statemachine_State10(self):
        return self.__statemachine_State10

    @statemachine_State10.setter
    def statemachine_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State10", None)
        self.__statemachine_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition9"):
                opp_val = getattr(old_value, "statemachine_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition9"):
                opp_val = getattr(value, "statemachine_Transition9", None)
                setattr(value, "statemachine_Transition9", self)

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
            if hasattr(old_value, "statemachine_MyFSM"):
                opp_val = getattr(old_value, "statemachine_MyFSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_MyFSM"):
                opp_val = getattr(value, "statemachine_MyFSM", None)
                if opp_val is None:
                    setattr(value, "statemachine_MyFSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
