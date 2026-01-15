from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sm6_Transition:

    def __init__(self, event: str, outgoing: "sm6_State" = None, sm6_Transition: "sm6_StateMachine" = None, Transition: "sm6_State" = None, Transition7: "sm6_State" = None, incoming: "sm6_State" = None):
        self.event = event
        self.outgoing = outgoing
        self.sm6_Transition = sm6_Transition
        self.Transition = Transition
        self.Transition7 = Transition7
        self.incoming = incoming
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def sm6_Transition(self):
        return self.__sm6_Transition

    @sm6_Transition.setter
    def sm6_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm6_Transition__sm6_Transition", None)
        self.__sm6_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm6_StateMachine3"):
                opp_val = getattr(old_value, "sm6_StateMachine3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm6_StateMachine3"):
                opp_val = getattr(value, "sm6_StateMachine3", None)
                if opp_val is None:
                    setattr(value, "sm6_StateMachine3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm6_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State9"):
                opp_val = getattr(old_value, "State9", None)
                if opp_val == self:
                    setattr(old_value, "State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State9"):
                opp_val = getattr(value, "State9", None)
                setattr(value, "State9", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm6_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "src"):
                opp_val = getattr(old_value, "src", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "src"):
                opp_val = getattr(value, "src", None)
                if opp_val is None:
                    setattr(value, "src", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition7(self):
        return self.__Transition7

    @Transition7.setter
    def Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm6_Transition__Transition7", None)
        self.__Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgt"):
                opp_val = getattr(old_value, "tgt", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgt"):
                opp_val = getattr(value, "tgt", None)
                if opp_val is None:
                    setattr(value, "tgt", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm6_Transition__incoming", None)
        self.__incoming = value
        
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

class sm6_State:

    def __init__(self, name: str, isFinal: str, State9: "sm6_Transition" = None, sm6_State: "sm6_StateMachine" = None, State: "sm6_StateMachine" = None, states: "sm6_StateMachine" = None, src: set["sm6_Transition"] = None, tgt: set["sm6_Transition"] = None, State11: "sm6_Transition" = None):
        self.name = name
        self.isFinal = isFinal
        self.State9 = State9
        self.sm6_State = sm6_State
        self.State = State
        self.states = states
        self.src = src if src is not None else set()
        self.tgt = tgt if tgt is not None else set()
        self.State11 = State11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isFinal(self) -> str:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: str):
        self.__isFinal = isFinal

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm6_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm"):
                opp_val = getattr(old_value, "sm", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm"):
                opp_val = getattr(value, "sm", None)
                if opp_val is None:
                    setattr(value, "sm", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State11(self):
        return self.__State11

    @State11.setter
    def State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm6_State__State11", None)
        self.__State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def State9(self):
        return self.__State9

    @State9.setter
    def State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm6_State__State9", None)
        self.__State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def tgt(self):
        return self.__tgt

    @tgt.setter
    def tgt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm6_State__tgt", None)
        self.__tgt = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition7"):
                    opp_val = getattr(item, "Transition7", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition7"):
                    opp_val = getattr(item, "Transition7", None)
                    
                    setattr(item, "Transition7", self)
                    

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm6_State__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine"):
                opp_val = getattr(old_value, "StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine"):
                opp_val = getattr(value, "StateMachine", None)
                setattr(value, "StateMachine", self)

    @property
    def sm6_State(self):
        return self.__sm6_State

    @sm6_State.setter
    def sm6_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm6_State__sm6_State", None)
        self.__sm6_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm6_StateMachine"):
                opp_val = getattr(old_value, "sm6_StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "sm6_StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm6_StateMachine"):
                opp_val = getattr(value, "sm6_StateMachine", None)
                setattr(value, "sm6_StateMachine", self)

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm6_State__src", None)
        self.__src = value if value is not None else set()
        
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
                    

class sm6_StateMachine:

    pass