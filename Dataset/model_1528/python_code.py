from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class minifsm_FinalState(State):

    pass
class minifsm_Transition:

    def __init__(self, event: str, in: "minifsm_State" = None, minifsm_Transition: "minifsm_Machine" = None, Transition: "minifsm_State" = None, Transition5: "minifsm_State" = None, out: "minifsm_State" = None):
        self.event = event
        self.in = in
        self.minifsm_Transition = minifsm_Transition
        self.Transition = Transition
        self.Transition5 = Transition5
        self.out = out
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def out(self):
        return self.__out

    @out.setter
    def out(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__out", None)
        self.__out = value
        
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
    def minifsm_Transition(self):
        return self.__minifsm_Transition

    @minifsm_Transition.setter
    def minifsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__minifsm_Transition", None)
        self.__minifsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minifsm_Machine2"):
                opp_val = getattr(old_value, "minifsm_Machine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minifsm_Machine2"):
                opp_val = getattr(value, "minifsm_Machine2", None)
                if opp_val is None:
                    setattr(value, "minifsm_Machine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def in(self):
        return self.__in

    @in.setter
    def in(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__in", None)
        self.__in = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State8"):
                opp_val = getattr(old_value, "State8", None)
                if opp_val == self:
                    setattr(old_value, "State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State8"):
                opp_val = getattr(value, "State8", None)
                setattr(value, "State8", self)

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
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__Transition5", None)
        self.__Transition5 = value
        
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

class minifsm_State:

    def __init__(self, name: str, State8: "minifsm_Transition" = None, minifsm_State: "minifsm_Machine" = None, src: set["minifsm_Transition"] = None, tgt: set["minifsm_Transition"] = None, State: "minifsm_Transition" = None):
        self.name = name
        self.State8 = State8
        self.minifsm_State = minifsm_State
        self.src = src if src is not None else set()
        self.tgt = tgt if tgt is not None else set()
        self.State = State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__src", None)
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
    def tgt(self):
        return self.__tgt

    @tgt.setter
    def tgt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__tgt", None)
        self.__tgt = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    setattr(item, "Transition5", self)
                    

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
            if hasattr(old_value, "out"):
                opp_val = getattr(old_value, "out", None)
                if opp_val == self:
                    setattr(old_value, "out", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out"):
                opp_val = getattr(value, "out", None)
                setattr(value, "out", self)

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
            if hasattr(old_value, "minifsm_Machine"):
                opp_val = getattr(old_value, "minifsm_Machine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minifsm_Machine"):
                opp_val = getattr(value, "minifsm_Machine", None)
                if opp_val is None:
                    setattr(value, "minifsm_Machine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State8(self):
        return self.__State8

    @State8.setter
    def State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__State8", None)
        self.__State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in"):
                opp_val = getattr(old_value, "in", None)
                if opp_val == self:
                    setattr(old_value, "in", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in"):
                opp_val = getattr(value, "in", None)
                setattr(value, "in", self)

class minifsm_Machine:

    pass