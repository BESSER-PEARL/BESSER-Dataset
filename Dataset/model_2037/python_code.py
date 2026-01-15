from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class etatma_State:

    def __init__(self, name: str, etatma_State: "etatma_StateMachine" = None, State: "etatma_Transition" = None, State5: "etatma_Transition" = None, from: "etatma_Transition" = None, to: "etatma_Transition" = None):
        self.name = name
        self.etatma_State = etatma_State
        self.State = State
        self.State5 = State5
        self.from = from
        self.to = to
        
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
        old_value = getattr(self, f"_etatma_State__State", None)
        self.__State = value
        
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
    def State5(self):
        return self.__State5

    @State5.setter
    def State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etatma_State__State5", None)
        self.__State5 = value
        
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
        old_value = getattr(self, f"_etatma_State__to", None)
        self.__to = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition8"):
                opp_val = getattr(old_value, "Transition8", None)
                if opp_val == self:
                    setattr(old_value, "Transition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition8"):
                opp_val = getattr(value, "Transition8", None)
                setattr(value, "Transition8", self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etatma_State__from", None)
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

    @property
    def etatma_State(self):
        return self.__etatma_State

    @etatma_State.setter
    def etatma_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etatma_State__etatma_State", None)
        self.__etatma_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etatma_StateMachine2"):
                opp_val = getattr(old_value, "etatma_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etatma_StateMachine2"):
                opp_val = getattr(value, "etatma_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "etatma_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class etatma_Transition:

    def __init__(self, name: str, etatma_Transition: "etatma_StateMachine" = None, outgoing: "etatma_State" = None, incoming: "etatma_State" = None, Transition: "etatma_State" = None, Transition8: "etatma_State" = None):
        self.name = name
        self.etatma_Transition = etatma_Transition
        self.outgoing = outgoing
        self.incoming = incoming
        self.Transition = Transition
        self.Transition8 = Transition8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etatma_Transition__Transition", None)
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etatma_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State5"):
                opp_val = getattr(old_value, "State5", None)
                if opp_val == self:
                    setattr(old_value, "State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State5"):
                opp_val = getattr(value, "State5", None)
                setattr(value, "State5", self)

    @property
    def Transition8(self):
        return self.__Transition8

    @Transition8.setter
    def Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etatma_Transition__Transition8", None)
        self.__Transition8 = value
        
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
    def etatma_Transition(self):
        return self.__etatma_Transition

    @etatma_Transition.setter
    def etatma_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etatma_Transition__etatma_Transition", None)
        self.__etatma_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etatma_StateMachine"):
                opp_val = getattr(old_value, "etatma_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etatma_StateMachine"):
                opp_val = getattr(value, "etatma_StateMachine", None)
                if opp_val is None:
                    setattr(value, "etatma_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etatma_Transition__outgoing", None)
        self.__outgoing = value
        
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

class etatma_StateMachine:

    def __init__(self, name: str, etatma_StateMachine: set["etatma_Transition"] = None, etatma_StateMachine2: set["etatma_State"] = None):
        self.name = name
        self.etatma_StateMachine = etatma_StateMachine if etatma_StateMachine is not None else set()
        self.etatma_StateMachine2 = etatma_StateMachine2 if etatma_StateMachine2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def etatma_StateMachine2(self):
        return self.__etatma_StateMachine2

    @etatma_StateMachine2.setter
    def etatma_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etatma_StateMachine__etatma_StateMachine2", None)
        self.__etatma_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etatma_State"):
                    opp_val = getattr(item, "etatma_State", None)
                    
                    if opp_val == self:
                        setattr(item, "etatma_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etatma_State"):
                    opp_val = getattr(item, "etatma_State", None)
                    
                    setattr(item, "etatma_State", self)
                    

    @property
    def etatma_StateMachine(self):
        return self.__etatma_StateMachine

    @etatma_StateMachine.setter
    def etatma_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etatma_StateMachine__etatma_StateMachine", None)
        self.__etatma_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etatma_Transition"):
                    opp_val = getattr(item, "etatma_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "etatma_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etatma_Transition"):
                    opp_val = getattr(item, "etatma_Transition", None)
                    
                    setattr(item, "etatma_Transition", self)
                    
