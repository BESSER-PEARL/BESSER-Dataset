from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tp1_StateMachine:

    def __init__(self, name: str, tp1_StateMachine: set["tp1_Transition"] = None, tp1_StateMachine2: set["tp1_State"] = None):
        self.name = name
        self.tp1_StateMachine = tp1_StateMachine if tp1_StateMachine is not None else set()
        self.tp1_StateMachine2 = tp1_StateMachine2 if tp1_StateMachine2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tp1_StateMachine2(self):
        return self.__tp1_StateMachine2

    @tp1_StateMachine2.setter
    def tp1_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp1_StateMachine__tp1_StateMachine2", None)
        self.__tp1_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp1_State"):
                    opp_val = getattr(item, "tp1_State", None)
                    
                    if opp_val == self:
                        setattr(item, "tp1_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp1_State"):
                    opp_val = getattr(item, "tp1_State", None)
                    
                    setattr(item, "tp1_State", self)
                    

    @property
    def tp1_StateMachine(self):
        return self.__tp1_StateMachine

    @tp1_StateMachine.setter
    def tp1_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp1_StateMachine__tp1_StateMachine", None)
        self.__tp1_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp1_Transition"):
                    opp_val = getattr(item, "tp1_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "tp1_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp1_Transition"):
                    opp_val = getattr(item, "tp1_Transition", None)
                    
                    setattr(item, "tp1_Transition", self)
                    

    def execute(self):
        # TODO: Implement execute method
        pass

class tp1_State:

    def __init__(self, name: str, tp1_State: "tp1_StateMachine" = None, from: "tp1_Transition" = None, to: "tp1_Transition" = None, State: "tp1_Transition" = None, State8: "tp1_Transition" = None):
        self.name = name
        self.tp1_State = tp1_State
        self.from = from
        self.to = to
        self.State = State
        self.State8 = State8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tp1_State(self):
        return self.__tp1_State

    @tp1_State.setter
    def tp1_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp1_State__tp1_State", None)
        self.__tp1_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp1_StateMachine2"):
                opp_val = getattr(old_value, "tp1_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp1_StateMachine2"):
                opp_val = getattr(value, "tp1_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "tp1_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp1_State__State", None)
        self.__State = value
        
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
    def State8(self):
        return self.__State8

    @State8.setter
    def State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp1_State__State8", None)
        self.__State8 = value
        
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
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp1_State__to", None)
        self.__to = value
        
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
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp1_State__from", None)
        self.__from = value
        
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

class tp1_Transition:

    def __init__(self, name: str, tp1_Transition: "tp1_StateMachine" = None, Transition: "tp1_State" = None, Transition5: "tp1_State" = None, outcoming: "tp1_State" = None, incoming: "tp1_State" = None):
        self.name = name
        self.tp1_Transition = tp1_Transition
        self.Transition = Transition
        self.Transition5 = Transition5
        self.outcoming = outcoming
        self.incoming = incoming
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp1_Transition__incoming", None)
        self.__incoming = value
        
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
    def outcoming(self):
        return self.__outcoming

    @outcoming.setter
    def outcoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp1_Transition__outcoming", None)
        self.__outcoming = value
        
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp1_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if opp_val == self:
                    setattr(old_value, "from", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                setattr(value, "from", self)

    @property
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp1_Transition__Transition5", None)
        self.__Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to"):
                opp_val = getattr(old_value, "to", None)
                if opp_val == self:
                    setattr(old_value, "to", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to"):
                opp_val = getattr(value, "to", None)
                setattr(value, "to", self)

    @property
    def tp1_Transition(self):
        return self.__tp1_Transition

    @tp1_Transition.setter
    def tp1_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp1_Transition__tp1_Transition", None)
        self.__tp1_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp1_StateMachine"):
                opp_val = getattr(old_value, "tp1_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp1_StateMachine"):
                opp_val = getattr(value, "tp1_StateMachine", None)
                if opp_val is None:
                    setattr(value, "tp1_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
