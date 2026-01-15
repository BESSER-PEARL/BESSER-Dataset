from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class minifsm_FinalState(State):

    pass
class minifsm_Transition:

    def __init__(self, event: str, Transition: "minifsm_FSM" = None, minifsm_Transition: "minifsm_State" = None, minifsm_Transition8: "minifsm_State" = None, transitions: "minifsm_FSM" = None):
        self.event = event
        self.Transition = Transition
        self.minifsm_Transition = minifsm_Transition
        self.minifsm_Transition8 = minifsm_Transition8
        self.transitions = transitions
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

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
    def minifsm_Transition8(self):
        return self.__minifsm_Transition8

    @minifsm_Transition8.setter
    def minifsm_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__minifsm_Transition8", None)
        self.__minifsm_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minifsm_State9"):
                opp_val = getattr(old_value, "minifsm_State9", None)
                if opp_val == self:
                    setattr(old_value, "minifsm_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minifsm_State9"):
                opp_val = getattr(value, "minifsm_State9", None)
                setattr(value, "minifsm_State9", self)

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
            if hasattr(old_value, "fsm2"):
                opp_val = getattr(old_value, "fsm2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm2"):
                opp_val = getattr(value, "fsm2", None)
                if opp_val is None:
                    setattr(value, "fsm2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "FSM11"):
                opp_val = getattr(old_value, "FSM11", None)
                if opp_val == self:
                    setattr(old_value, "FSM11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM11"):
                opp_val = getattr(value, "FSM11", None)
                setattr(value, "FSM11", self)

class minifsm_State:

    def __init__(self, name: str, State: "minifsm_FSM" = None, minifsm_State: "minifsm_FSM" = None, states: "minifsm_FSM" = None, minifsm_State6: "minifsm_Transition" = None, minifsm_State9: "minifsm_Transition" = None):
        self.name = name
        self.State = State
        self.minifsm_State = minifsm_State
        self.states = states
        self.minifsm_State6 = minifsm_State6
        self.minifsm_State9 = minifsm_State9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__State", None)
        self.__State = value
        
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
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__states", None)
        self.__states = value
        
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
    def minifsm_State6(self):
        return self.__minifsm_State6

    @minifsm_State6.setter
    def minifsm_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__minifsm_State6", None)
        self.__minifsm_State6 = value
        
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
                if opp_val == self:
                    setattr(old_value, "minifsm_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minifsm_FSM"):
                opp_val = getattr(value, "minifsm_FSM", None)
                setattr(value, "minifsm_FSM", self)

    @property
    def minifsm_State9(self):
        return self.__minifsm_State9

    @minifsm_State9.setter
    def minifsm_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__minifsm_State9", None)
        self.__minifsm_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minifsm_Transition8"):
                opp_val = getattr(old_value, "minifsm_Transition8", None)
                if opp_val == self:
                    setattr(old_value, "minifsm_Transition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minifsm_Transition8"):
                opp_val = getattr(value, "minifsm_Transition8", None)
                setattr(value, "minifsm_Transition8", self)

class minifsm_FSM:

    pass