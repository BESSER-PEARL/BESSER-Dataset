from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class fsm_Final(State):

    pass
class fsm_Initial(State):

    pass
class fsm_FSM:

    def __init__(self, fsm_FSM: set["fsm_State"] = None, fsm: set["fsm_Transition"] = None, FSM: "fsm_Transition" = None):
        self.fsm_FSM = fsm_FSM if fsm_FSM is not None else set()
        self.fsm = fsm if fsm is not None else set()
        self.FSM = FSM
        
    @property
    def FSM(self):
        return self.__FSM

    @FSM.setter
    def FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__FSM", None)
        self.__FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitions"):
                opp_val = getattr(old_value, "transitions", None)
                if opp_val == self:
                    setattr(old_value, "transitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitions"):
                opp_val = getattr(value, "transitions", None)
                setattr(value, "transitions", self)

    @property
    def fsm(self):
        return self.__fsm

    @fsm.setter
    def fsm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm", None)
        self.__fsm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def fsm_FSM(self):
        return self.__fsm_FSM

    @fsm_FSM.setter
    def fsm_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM", None)
        self.__fsm_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_State"):
                    opp_val = getattr(item, "fsm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_State"):
                    opp_val = getattr(item, "fsm_State", None)
                    
                    setattr(item, "fsm_State", self)
                    

    def execute(self, events: str):
        # TODO: Implement execute method
        pass

class fsm_Transition:

    def __init__(self, event: str, Transition: "fsm_FSM" = None, fsm_Transition: "fsm_State" = None, fsm_Transition5: "fsm_State" = None, transitions: "fsm_FSM" = None):
        self.event = event
        self.Transition = Transition
        self.fsm_Transition = fsm_Transition
        self.fsm_Transition5 = fsm_Transition5
        self.transitions = transitions
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def fsm_Transition(self):
        return self.__fsm_Transition

    @fsm_Transition.setter
    def fsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition", None)
        self.__fsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State3"):
                opp_val = getattr(old_value, "fsm_State3", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State3"):
                opp_val = getattr(value, "fsm_State3", None)
                setattr(value, "fsm_State3", self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM"):
                opp_val = getattr(old_value, "FSM", None)
                if opp_val == self:
                    setattr(old_value, "FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM"):
                opp_val = getattr(value, "FSM", None)
                setattr(value, "FSM", self)

    @property
    def fsm_Transition5(self):
        return self.__fsm_Transition5

    @fsm_Transition5.setter
    def fsm_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition5", None)
        self.__fsm_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State6"):
                opp_val = getattr(old_value, "fsm_State6", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State6"):
                opp_val = getattr(value, "fsm_State6", None)
                setattr(value, "fsm_State6", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm"):
                opp_val = getattr(old_value, "fsm", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm"):
                opp_val = getattr(value, "fsm", None)
                if opp_val is None:
                    setattr(value, "fsm", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isActivated(self) -> bool:
        # TODO: Implement isActivated method
        pass

class fsm_State:

    def __init__(self, name: str, fsm_State: "fsm_FSM" = None, fsm_State3: "fsm_Transition" = None, fsm_State6: "fsm_Transition" = None):
        self.name = name
        self.fsm_State = fsm_State
        self.fsm_State3 = fsm_State3
        self.fsm_State6 = fsm_State6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_State(self):
        return self.__fsm_State

    @fsm_State.setter
    def fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State", None)
        self.__fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM"):
                opp_val = getattr(old_value, "fsm_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM"):
                opp_val = getattr(value, "fsm_FSM", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_State3(self):
        return self.__fsm_State3

    @fsm_State3.setter
    def fsm_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State3", None)
        self.__fsm_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition"):
                opp_val = getattr(old_value, "fsm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition"):
                opp_val = getattr(value, "fsm_Transition", None)
                setattr(value, "fsm_Transition", self)

    @property
    def fsm_State6(self):
        return self.__fsm_State6

    @fsm_State6.setter
    def fsm_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State6", None)
        self.__fsm_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition5"):
                opp_val = getattr(old_value, "fsm_Transition5", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition5"):
                opp_val = getattr(value, "fsm_Transition5", None)
                setattr(value, "fsm_Transition5", self)

    def execute(self):
        # TODO: Implement execute method
        pass
