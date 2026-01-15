from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class minifsm_Transition:

    def __init__(self, event: str, transitions: "minifsm_FSM" = None, Transition: "minifsm_FSM" = None, minifsm_Transition: "minifsm_State" = None, minifsm_Transition5: "minifsm_State" = None):
        self.event = event
        self.transitions = transitions
        self.Transition = Transition
        self.minifsm_Transition = minifsm_Transition
        self.minifsm_Transition5 = minifsm_Transition5
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__Transition", None)
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

    @property
    def minifsm_Transition5(self):
        return self.__minifsm_Transition5

    @minifsm_Transition5.setter
    def minifsm_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__minifsm_Transition5", None)
        self.__minifsm_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minifsm_State6"):
                opp_val = getattr(old_value, "minifsm_State6", None)
                if opp_val == self:
                    setattr(old_value, "minifsm_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minifsm_State6"):
                opp_val = getattr(value, "minifsm_State6", None)
                setattr(value, "minifsm_State6", self)

    @property
    def minifsm_Transition(self):
        return self.__minifsm_Transition

    @minifsm_Transition.setter
    def minifsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__minifsm_Transition", None)
        self.__minifsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minifsm_State3"):
                opp_val = getattr(old_value, "minifsm_State3", None)
                if opp_val == self:
                    setattr(old_value, "minifsm_State3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minifsm_State3"):
                opp_val = getattr(value, "minifsm_State3", None)
                setattr(value, "minifsm_State3", self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__transitions", None)
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

    def isActivated(self) -> bool:
        # TODO: Implement isActivated method
        pass

class State:

    pass
class minifsm_Terminal(State):

    pass
class minifsm_Initial(State):

    pass
class minifsm_State:

    def __init__(self, name: str, minifsm_State: "minifsm_FSM" = None, minifsm_State3: "minifsm_Transition" = None, minifsm_State6: "minifsm_Transition" = None):
        self.name = name
        self.minifsm_State = minifsm_State
        self.minifsm_State3 = minifsm_State3
        self.minifsm_State6 = minifsm_State6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minifsm_State6(self):
        return self.__minifsm_State6

    @minifsm_State6.setter
    def minifsm_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__minifsm_State6", None)
        self.__minifsm_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minifsm_Transition5"):
                opp_val = getattr(old_value, "minifsm_Transition5", None)
                if opp_val == self:
                    setattr(old_value, "minifsm_Transition5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minifsm_Transition5"):
                opp_val = getattr(value, "minifsm_Transition5", None)
                setattr(value, "minifsm_Transition5", self)

    @property
    def minifsm_State(self):
        return self.__minifsm_State

    @minifsm_State.setter
    def minifsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__minifsm_State", None)
        self.__minifsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minifsm_FSM"):
                opp_val = getattr(old_value, "minifsm_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minifsm_FSM"):
                opp_val = getattr(value, "minifsm_FSM", None)
                if opp_val is None:
                    setattr(value, "minifsm_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def minifsm_State3(self):
        return self.__minifsm_State3

    @minifsm_State3.setter
    def minifsm_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__minifsm_State3", None)
        self.__minifsm_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minifsm_Transition"):
                opp_val = getattr(old_value, "minifsm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "minifsm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minifsm_Transition"):
                opp_val = getattr(value, "minifsm_Transition", None)
                setattr(value, "minifsm_Transition", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class minifsm_FSM:

    def __init__(self, minifsm_FSM: set["minifsm_State"] = None, FSM: "minifsm_Transition" = None, fsm: set["minifsm_Transition"] = None):
        self.minifsm_FSM = minifsm_FSM if minifsm_FSM is not None else set()
        self.FSM = FSM
        self.fsm = fsm if fsm is not None else set()
        
    @property
    def minifsm_FSM(self):
        return self.__minifsm_FSM

    @minifsm_FSM.setter
    def minifsm_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_FSM__minifsm_FSM", None)
        self.__minifsm_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "minifsm_State"):
                    opp_val = getattr(item, "minifsm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "minifsm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "minifsm_State"):
                    opp_val = getattr(item, "minifsm_State", None)
                    
                    setattr(item, "minifsm_State", self)
                    

    @property
    def FSM(self):
        return self.__FSM

    @FSM.setter
    def FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_FSM__FSM", None)
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
        old_value = getattr(self, f"_minifsm_FSM__fsm", None)
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
                    

    def handle(self, event: str):
        # TODO: Implement handle method
        pass
