from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sm2_StateMachine:

    pass
class sm2_Transition:

    def __init__(self, event: str, sm2_Transition: "sm2_StateMachine" = None, Transition: "sm2_State" = None, incoming: "sm2_State" = None, Transition7: "sm2_State" = None, outgoing: "sm2_State" = None):
        self.event = event
        self.sm2_Transition = sm2_Transition
        self.Transition = Transition
        self.incoming = incoming
        self.Transition7 = Transition7
        self.outgoing = outgoing
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def sm2_Transition(self):
        return self.__sm2_Transition

    @sm2_Transition.setter
    def sm2_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm2_Transition__sm2_Transition", None)
        self.__sm2_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm2_StateMachine3"):
                opp_val = getattr(old_value, "sm2_StateMachine3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm2_StateMachine3"):
                opp_val = getattr(value, "sm2_StateMachine3", None)
                if opp_val is None:
                    setattr(value, "sm2_StateMachine3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm2_Transition__outgoing", None)
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
    def Transition7(self):
        return self.__Transition7

    @Transition7.setter
    def Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm2_Transition__Transition7", None)
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm2_Transition__Transition", None)
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm2_Transition__incoming", None)
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

class sm2_State:

    def __init__(self, name: str, sm2_State: "sm2_StateMachine" = None, State: "sm2_StateMachine" = None, states: "sm2_StateMachine" = None, State11: "sm2_Transition" = None, src: set["sm2_Transition"] = None, tgt: set["sm2_Transition"] = None, State9: "sm2_Transition" = None):
        self.name = name
        self.sm2_State = sm2_State
        self.State = State
        self.states = states
        self.State11 = State11
        self.src = src if src is not None else set()
        self.tgt = tgt if tgt is not None else set()
        self.State9 = State9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State9(self):
        return self.__State9

    @State9.setter
    def State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm2_State__State9", None)
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
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm2_State__states", None)
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
    def tgt(self):
        return self.__tgt

    @tgt.setter
    def tgt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm2_State__tgt", None)
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm2_State__State", None)
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
    def sm2_State(self):
        return self.__sm2_State

    @sm2_State.setter
    def sm2_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm2_State__sm2_State", None)
        self.__sm2_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm2_StateMachine"):
                opp_val = getattr(old_value, "sm2_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm2_StateMachine"):
                opp_val = getattr(value, "sm2_StateMachine", None)
                if opp_val is None:
                    setattr(value, "sm2_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm2_State__src", None)
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
                    

    @property
    def State11(self):
        return self.__State11

    @State11.setter
    def State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm2_State__State11", None)
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
