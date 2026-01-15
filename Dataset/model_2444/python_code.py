from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsa_State:

    def __init__(self, name: str, accepting: bool, fsa_State5: "fsa_FSA" = None, fsa_State: "fsa_FSA" = None, fromState: set["fsa_Transition"] = None, toState: set["fsa_Transition"] = None, State: "fsa_Transition" = None, State11: "fsa_Transition" = None):
        self.name = name
        self.accepting = accepting
        self.fsa_State5 = fsa_State5
        self.fsa_State = fsa_State
        self.fromState = fromState if fromState is not None else set()
        self.toState = toState if toState is not None else set()
        self.State = State
        self.State11 = State11
        
    @property
    def accepting(self) -> bool:
        return self.__accepting

    @accepting.setter
    def accepting(self, accepting: bool):
        self.__accepting = accepting

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsa_State5(self):
        return self.__fsa_State5

    @fsa_State5.setter
    def fsa_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_State__fsa_State5", None)
        self.__fsa_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsa_FSA4"):
                opp_val = getattr(old_value, "fsa_FSA4", None)
                if opp_val == self:
                    setattr(old_value, "fsa_FSA4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsa_FSA4"):
                opp_val = getattr(value, "fsa_FSA4", None)
                setattr(value, "fsa_FSA4", self)

    @property
    def State11(self):
        return self.__State11

    @State11.setter
    def State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_State__State11", None)
        self.__State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingTransitions"):
                opp_val = getattr(old_value, "incomingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "incomingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingTransitions"):
                opp_val = getattr(value, "incomingTransitions", None)
                setattr(value, "incomingTransitions", self)

    @property
    def toState(self):
        return self.__toState

    @toState.setter
    def toState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_State__toState", None)
        self.__toState = value if value is not None else set()
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransitions"):
                opp_val = getattr(old_value, "outgoingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransitions"):
                opp_val = getattr(value, "outgoingTransitions", None)
                setattr(value, "outgoingTransitions", self)

    @property
    def fsa_State(self):
        return self.__fsa_State

    @fsa_State.setter
    def fsa_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_State__fsa_State", None)
        self.__fsa_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsa_FSA"):
                opp_val = getattr(old_value, "fsa_FSA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsa_FSA"):
                opp_val = getattr(value, "fsa_FSA", None)
                if opp_val is None:
                    setattr(value, "fsa_FSA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fromState(self):
        return self.__fromState

    @fromState.setter
    def fromState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_State__fromState", None)
        self.__fromState = value if value is not None else set()
        
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
                    

class fsa_FSA:

    pass
class fsa_Transition:

    def __init__(self, event: str, fsa_Transition: "fsa_FSA" = None, Transition: "fsa_State" = None, Transition8: "fsa_State" = None, outgoingTransitions: "fsa_State" = None, incomingTransitions: "fsa_State" = None):
        self.event = event
        self.fsa_Transition = fsa_Transition
        self.Transition = Transition
        self.Transition8 = Transition8
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    @property
    def fsa_Transition(self):
        return self.__fsa_Transition

    @fsa_Transition.setter
    def fsa_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_Transition__fsa_Transition", None)
        self.__fsa_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsa_FSA2"):
                opp_val = getattr(old_value, "fsa_FSA2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsa_FSA2"):
                opp_val = getattr(value, "fsa_FSA2", None)
                if opp_val is None:
                    setattr(value, "fsa_FSA2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State11"):
                opp_val = getattr(old_value, "State11", None)
                if opp_val == self:
                    setattr(old_value, "State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State11"):
                opp_val = getattr(value, "State11", None)
                setattr(value, "State11", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fromState"):
                opp_val = getattr(old_value, "fromState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fromState"):
                opp_val = getattr(value, "fromState", None)
                if opp_val is None:
                    setattr(value, "fromState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition8(self):
        return self.__Transition8

    @Transition8.setter
    def Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_Transition__Transition8", None)
        self.__Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toState"):
                opp_val = getattr(old_value, "toState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toState"):
                opp_val = getattr(value, "toState", None)
                if opp_val is None:
                    setattr(value, "toState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
