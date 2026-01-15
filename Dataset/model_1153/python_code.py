from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class gemoc_Transition:

    def __init__(self, name: str, trigger: str, gemoc_Transition: "gemoc_FSM" = None, Transition: "gemoc_State" = None, Transition5: "gemoc_State" = None, incoming: "gemoc_State" = None, outcoming: "gemoc_State" = None):
        self.name = name
        self.trigger = trigger
        self.gemoc_Transition = gemoc_Transition
        self.Transition = Transition
        self.Transition5 = Transition5
        self.incoming = incoming
        self.outcoming = outcoming
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state"):
                opp_val = getattr(old_value, "state", None)
                if opp_val == self:
                    setattr(old_value, "state", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state"):
                opp_val = getattr(value, "state", None)
                setattr(value, "state", self)

    @property
    def gemoc_Transition(self):
        return self.__gemoc_Transition

    @gemoc_Transition.setter
    def gemoc_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_Transition__gemoc_Transition", None)
        self.__gemoc_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gemoc_FSM2"):
                opp_val = getattr(old_value, "gemoc_FSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gemoc_FSM2"):
                opp_val = getattr(value, "gemoc_FSM2", None)
                if opp_val is None:
                    setattr(value, "gemoc_FSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_Transition__Transition5", None)
        self.__Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "src"):
                opp_val = getattr(old_value, "src", None)
                if opp_val == self:
                    setattr(old_value, "src", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "src"):
                opp_val = getattr(value, "src", None)
                setattr(value, "src", self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_Transition__incoming", None)
        self.__incoming = value
        
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
    def outcoming(self):
        return self.__outcoming

    @outcoming.setter
    def outcoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_Transition__outcoming", None)
        self.__outcoming = value
        
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

class gemoc_State:

    def __init__(self, name: str, gemoc_State: "gemoc_FSM" = None, state: "gemoc_Transition" = None, src: "gemoc_Transition" = None, State: "gemoc_Transition" = None, State8: "gemoc_Transition" = None):
        self.name = name
        self.gemoc_State = gemoc_State
        self.state = state
        self.src = src
        self.State = State
        self.State8 = State8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gemoc_State(self):
        return self.__gemoc_State

    @gemoc_State.setter
    def gemoc_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_State__gemoc_State", None)
        self.__gemoc_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gemoc_FSM"):
                opp_val = getattr(old_value, "gemoc_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gemoc_FSM"):
                opp_val = getattr(value, "gemoc_FSM", None)
                if opp_val is None:
                    setattr(value, "gemoc_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_State__State", None)
        self.__State = value
        
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
    def State8(self):
        return self.__State8

    @State8.setter
    def State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_State__State8", None)
        self.__State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outcoming"):
                opp_val = getattr(old_value, "outcoming", None)
                if opp_val == self:
                    setattr(old_value, "outcoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outcoming"):
                opp_val = getattr(value, "outcoming", None)
                setattr(value, "outcoming", self)

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_State__src", None)
        self.__src = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition5"):
                opp_val = getattr(old_value, "Transition5", None)
                if opp_val == self:
                    setattr(old_value, "Transition5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition5"):
                opp_val = getattr(value, "Transition5", None)
                setattr(value, "Transition5", self)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_State__state", None)
        self.__state = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition"):
                opp_val = getattr(old_value, "Transition", None)
                if opp_val == self:
                    setattr(old_value, "Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition"):
                opp_val = getattr(value, "Transition", None)
                setattr(value, "Transition", self)

class gemoc_FSM:

    def __init__(self, name: str, gemoc_FSM: set["gemoc_State"] = None, gemoc_FSM2: set["gemoc_Transition"] = None):
        self.name = name
        self.gemoc_FSM = gemoc_FSM if gemoc_FSM is not None else set()
        self.gemoc_FSM2 = gemoc_FSM2 if gemoc_FSM2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gemoc_FSM2(self):
        return self.__gemoc_FSM2

    @gemoc_FSM2.setter
    def gemoc_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_FSM__gemoc_FSM2", None)
        self.__gemoc_FSM2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gemoc_Transition"):
                    opp_val = getattr(item, "gemoc_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "gemoc_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gemoc_Transition"):
                    opp_val = getattr(item, "gemoc_Transition", None)
                    
                    setattr(item, "gemoc_Transition", self)
                    

    @property
    def gemoc_FSM(self):
        return self.__gemoc_FSM

    @gemoc_FSM.setter
    def gemoc_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_FSM__gemoc_FSM", None)
        self.__gemoc_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gemoc_State"):
                    opp_val = getattr(item, "gemoc_State", None)
                    
                    if opp_val == self:
                        setattr(item, "gemoc_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gemoc_State"):
                    opp_val = getattr(item, "gemoc_State", None)
                    
                    setattr(item, "gemoc_State", self)
                    

    def print(self):
        # TODO: Implement print method
        pass
