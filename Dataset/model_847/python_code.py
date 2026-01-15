from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class fsm_FinalState(State):

    pass
class fsm_InitialState(State):

    pass
class fsm_Transition:

    def __init__(self, event: str, Transition: "fsm_FSM" = None, Transition8: "fsm_State" = None, transitions: "fsm_FSM" = None, outgoingtransitions: "fsm_State" = None, incommingtransitions: "fsm_State" = None, Transition6: "fsm_State" = None):
        self.event = event
        self.Transition = Transition
        self.Transition8 = Transition8
        self.transitions = transitions
        self.outgoingtransitions = outgoingtransitions
        self.incommingtransitions = incommingtransitions
        self.Transition6 = Transition6
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def Transition6(self):
        return self.__Transition6

    @Transition6.setter
    def Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition6", None)
        self.__Transition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                if opp_val is None:
                    setattr(value, "from", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incommingtransitions(self):
        return self.__incommingtransitions

    @incommingtransitions.setter
    def incommingtransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__incommingtransitions", None)
        self.__incommingtransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State14"):
                opp_val = getattr(old_value, "State14", None)
                if opp_val == self:
                    setattr(old_value, "State14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State14"):
                opp_val = getattr(value, "State14", None)
                setattr(value, "State14", self)

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
            if hasattr(old_value, "FSM10"):
                opp_val = getattr(old_value, "FSM10", None)
                if opp_val == self:
                    setattr(old_value, "FSM10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM10"):
                opp_val = getattr(value, "FSM10", None)
                setattr(value, "FSM10", self)

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
    def outgoingtransitions(self):
        return self.__outgoingtransitions

    @outgoingtransitions.setter
    def outgoingtransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__outgoingtransitions", None)
        self.__outgoingtransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State12"):
                opp_val = getattr(old_value, "State12", None)
                if opp_val == self:
                    setattr(old_value, "State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State12"):
                opp_val = getattr(value, "State12", None)
                setattr(value, "State12", self)

    @property
    def Transition8(self):
        return self.__Transition8

    @Transition8.setter
    def Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition8", None)
        self.__Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to"):
                opp_val = getattr(old_value, "to", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to"):
                opp_val = getattr(value, "to", None)
                if opp_val is None:
                    setattr(value, "to", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_State:

    def __init__(self, name: str, State: "fsm_FSM" = None, to: set["fsm_Transition"] = None, State12: "fsm_Transition" = None, State14: "fsm_Transition" = None, states: "fsm_FSM" = None, from: set["fsm_Transition"] = None):
        self.name = name
        self.State = State
        self.to = to if to is not None else set()
        self.State12 = State12
        self.State14 = State14
        self.states = states
        self.from = from if from is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__states", None)
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State", None)
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
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    setattr(item, "Transition8", self)
                    

    @property
    def State14(self):
        return self.__State14

    @State14.setter
    def State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State14", None)
        self.__State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incommingtransitions"):
                opp_val = getattr(old_value, "incommingtransitions", None)
                if opp_val == self:
                    setattr(old_value, "incommingtransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incommingtransitions"):
                opp_val = getattr(value, "incommingtransitions", None)
                setattr(value, "incommingtransitions", self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__from", None)
        self.__from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition6"):
                    opp_val = getattr(item, "Transition6", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition6"):
                    opp_val = getattr(item, "Transition6", None)
                    
                    setattr(item, "Transition6", self)
                    

    @property
    def State12(self):
        return self.__State12

    @State12.setter
    def State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State12", None)
        self.__State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingtransitions"):
                opp_val = getattr(old_value, "outgoingtransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingtransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingtransitions"):
                opp_val = getattr(value, "outgoingtransitions", None)
                setattr(value, "outgoingtransitions", self)

class fsm_FSM:

    def __init__(self, name: str, fsm: set["fsm_State"] = None, fsm2: set["fsm_Transition"] = None, fsm_FSM: "fsm_InitialState" = None, FSM10: "fsm_Transition" = None, FSM: "fsm_State" = None):
        self.name = name
        self.fsm = fsm if fsm is not None else set()
        self.fsm2 = fsm2 if fsm2 is not None else set()
        self.fsm_FSM = fsm_FSM
        self.FSM10 = FSM10
        self.FSM = FSM
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def fsm2(self):
        return self.__fsm2

    @fsm2.setter
    def fsm2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm2", None)
        self.__fsm2 = value if value is not None else set()
        
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
    def FSM10(self):
        return self.__FSM10

    @FSM10.setter
    def FSM10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__FSM10", None)
        self.__FSM10 = value
        
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
    def FSM(self):
        return self.__FSM

    @FSM.setter
    def FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__FSM", None)
        self.__FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states"):
                opp_val = getattr(old_value, "states", None)
                if opp_val == self:
                    setattr(old_value, "states", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states"):
                opp_val = getattr(value, "states", None)
                setattr(value, "states", self)

    @property
    def fsm_FSM(self):
        return self.__fsm_FSM

    @fsm_FSM.setter
    def fsm_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM", None)
        self.__fsm_FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_InitialState"):
                opp_val = getattr(old_value, "fsm_InitialState", None)
                if opp_val == self:
                    setattr(old_value, "fsm_InitialState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_InitialState"):
                opp_val = getattr(value, "fsm_InitialState", None)
                setattr(value, "fsm_InitialState", self)
