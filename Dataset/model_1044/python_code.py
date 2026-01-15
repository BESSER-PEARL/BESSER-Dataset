from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sample_FSM:

    def __init__(self, name: str, sample_FSM: set["sample_Transition"] = None, sample_FSM2: set["sample_State"] = None):
        self.name = name
        self.sample_FSM = sample_FSM if sample_FSM is not None else set()
        self.sample_FSM2 = sample_FSM2 if sample_FSM2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sample_FSM2(self):
        return self.__sample_FSM2

    @sample_FSM2.setter
    def sample_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_FSM__sample_FSM2", None)
        self.__sample_FSM2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_State"):
                    opp_val = getattr(item, "sample_State", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_State"):
                    opp_val = getattr(item, "sample_State", None)
                    
                    setattr(item, "sample_State", self)
                    

    @property
    def sample_FSM(self):
        return self.__sample_FSM

    @sample_FSM.setter
    def sample_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_FSM__sample_FSM", None)
        self.__sample_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_Transition"):
                    opp_val = getattr(item, "sample_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_Transition"):
                    opp_val = getattr(item, "sample_Transition", None)
                    
                    setattr(item, "sample_Transition", self)
                    

class State:

    pass
class sample_Finalstate(State):

    pass
class sample_Initstate(State):

    pass
class sample_State:

    def __init__(self, name: str, sample_State: "sample_FSM" = None, sample_State5: "sample_Transition" = None, sample_State8: "sample_Transition" = None):
        self.name = name
        self.sample_State = sample_State
        self.sample_State5 = sample_State5
        self.sample_State8 = sample_State8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sample_State5(self):
        return self.__sample_State5

    @sample_State5.setter
    def sample_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_State__sample_State5", None)
        self.__sample_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Transition4"):
                opp_val = getattr(old_value, "sample_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "sample_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Transition4"):
                opp_val = getattr(value, "sample_Transition4", None)
                setattr(value, "sample_Transition4", self)

    @property
    def sample_State8(self):
        return self.__sample_State8

    @sample_State8.setter
    def sample_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_State__sample_State8", None)
        self.__sample_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Transition7"):
                opp_val = getattr(old_value, "sample_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "sample_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Transition7"):
                opp_val = getattr(value, "sample_Transition7", None)
                setattr(value, "sample_Transition7", self)

    @property
    def sample_State(self):
        return self.__sample_State

    @sample_State.setter
    def sample_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_State__sample_State", None)
        self.__sample_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_FSM2"):
                opp_val = getattr(old_value, "sample_FSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_FSM2"):
                opp_val = getattr(value, "sample_FSM2", None)
                if opp_val is None:
                    setattr(value, "sample_FSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sample_Transition:

    def __init__(self, name: str, trigger: str, sample_Transition: "sample_FSM" = None, sample_Transition4: "sample_State" = None, sample_Transition7: "sample_State" = None):
        self.name = name
        self.trigger = trigger
        self.sample_Transition = sample_Transition
        self.sample_Transition4 = sample_Transition4
        self.sample_Transition7 = sample_Transition7
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sample_Transition(self):
        return self.__sample_Transition

    @sample_Transition.setter
    def sample_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Transition__sample_Transition", None)
        self.__sample_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_FSM"):
                opp_val = getattr(old_value, "sample_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_FSM"):
                opp_val = getattr(value, "sample_FSM", None)
                if opp_val is None:
                    setattr(value, "sample_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sample_Transition7(self):
        return self.__sample_Transition7

    @sample_Transition7.setter
    def sample_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Transition__sample_Transition7", None)
        self.__sample_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_State8"):
                opp_val = getattr(old_value, "sample_State8", None)
                if opp_val == self:
                    setattr(old_value, "sample_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_State8"):
                opp_val = getattr(value, "sample_State8", None)
                setattr(value, "sample_State8", self)

    @property
    def sample_Transition4(self):
        return self.__sample_Transition4

    @sample_Transition4.setter
    def sample_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Transition__sample_Transition4", None)
        self.__sample_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_State5"):
                opp_val = getattr(old_value, "sample_State5", None)
                if opp_val == self:
                    setattr(old_value, "sample_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_State5"):
                opp_val = getattr(value, "sample_State5", None)
                setattr(value, "sample_State5", self)
