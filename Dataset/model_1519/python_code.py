from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sm4_Transition:

    def __init__(self, event: str, Transition: "sm4_State" = None, Transition7: "sm4_State" = None, sm4_Transition: "sm4_StateMachine" = None, outgoing: "sm4_State" = None, incoming: "sm4_State" = None):
        self.event = event
        self.Transition = Transition
        self.Transition7 = Transition7
        self.sm4_Transition = sm4_Transition
        self.outgoing = outgoing
        self.incoming = incoming
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def Transition7(self):
        return self.__Transition7

    @Transition7.setter
    def Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm4_Transition__Transition7", None)
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
    def sm4_Transition(self):
        return self.__sm4_Transition

    @sm4_Transition.setter
    def sm4_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm4_Transition__sm4_Transition", None)
        self.__sm4_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm4_StateMachine3"):
                opp_val = getattr(old_value, "sm4_StateMachine3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm4_StateMachine3"):
                opp_val = getattr(value, "sm4_StateMachine3", None)
                if opp_val is None:
                    setattr(value, "sm4_StateMachine3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm4_Transition__incoming", None)
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

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm4_Transition__outgoing", None)
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
        old_value = getattr(self, f"_sm4_Transition__Transition", None)
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

class sm4_State:

    def __init__(self, name: str, sm4_State: "sm4_StateMachine" = None, State: "sm4_StateMachine" = None, src: set["sm4_Transition"] = None, tgt: set["sm4_Transition"] = None, states: "sm4_StateMachine" = None, State9: "sm4_Transition" = None, State11: "sm4_Transition" = None):
        self.name = name
        self.sm4_State = sm4_State
        self.State = State
        self.src = src if src is not None else set()
        self.tgt = tgt if tgt is not None else set()
        self.states = states
        self.State9 = State9
        self.State11 = State11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State11(self):
        return self.__State11

    @State11.setter
    def State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm4_State__State11", None)
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
    def sm4_State(self):
        return self.__sm4_State

    @sm4_State.setter
    def sm4_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm4_State__sm4_State", None)
        self.__sm4_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm4_StateMachine"):
                opp_val = getattr(old_value, "sm4_StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "sm4_StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm4_StateMachine"):
                opp_val = getattr(value, "sm4_StateMachine", None)
                setattr(value, "sm4_StateMachine", self)

    @property
    def State9(self):
        return self.__State9

    @State9.setter
    def State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm4_State__State9", None)
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
        old_value = getattr(self, f"_sm4_State__tgt", None)
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
        old_value = getattr(self, f"_sm4_State__states", None)
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm4_State__State", None)
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
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm4_State__src", None)
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
                    

class State:

    pass
class sm4_StateMachine(State):

    pass