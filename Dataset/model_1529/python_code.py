from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tP1_EM_State:

    def __init__(self, name: str, tP1_EM_State: "tP1_EM_StateMachine" = None, tP1_EM_State5: "tP1_EM_StateMachine" = None, from: "tP1_EM_Transition" = None, State: "tP1_EM_Transition" = None, State11: "tP1_EM_Transition" = None, to: "tP1_EM_Transition" = None):
        self.name = name
        self.tP1_EM_State = tP1_EM_State
        self.tP1_EM_State5 = tP1_EM_State5
        self.from = from
        self.State = State
        self.State11 = State11
        self.to = to
        
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
        old_value = getattr(self, f"_tP1_EM_State__State11", None)
        self.__State11 = value
        
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
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tP1_EM_State__to", None)
        self.__to = value
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tP1_EM_State__State", None)
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
    def tP1_EM_State5(self):
        return self.__tP1_EM_State5

    @tP1_EM_State5.setter
    def tP1_EM_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tP1_EM_State__tP1_EM_State5", None)
        self.__tP1_EM_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tP1_EM_StateMachine4"):
                opp_val = getattr(old_value, "tP1_EM_StateMachine4", None)
                if opp_val == self:
                    setattr(old_value, "tP1_EM_StateMachine4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tP1_EM_StateMachine4"):
                opp_val = getattr(value, "tP1_EM_StateMachine4", None)
                setattr(value, "tP1_EM_StateMachine4", self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tP1_EM_State__from", None)
        self.__from = value
        
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
    def tP1_EM_State(self):
        return self.__tP1_EM_State

    @tP1_EM_State.setter
    def tP1_EM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tP1_EM_State__tP1_EM_State", None)
        self.__tP1_EM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tP1_EM_StateMachine2"):
                opp_val = getattr(old_value, "tP1_EM_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tP1_EM_StateMachine2"):
                opp_val = getattr(value, "tP1_EM_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "tP1_EM_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tP1_EM_Transition:

    def __init__(self, name: str, tP1_EM_Transition: "tP1_EM_StateMachine" = None, Transition: "tP1_EM_State" = None, incoming: "tP1_EM_State" = None, outgoing: "tP1_EM_State" = None, Transition8: "tP1_EM_State" = None):
        self.name = name
        self.tP1_EM_Transition = tP1_EM_Transition
        self.Transition = Transition
        self.incoming = incoming
        self.outgoing = outgoing
        self.Transition8 = Transition8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tP1_EM_Transition__outgoing", None)
        self.__outgoing = value
        
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
    def tP1_EM_Transition(self):
        return self.__tP1_EM_Transition

    @tP1_EM_Transition.setter
    def tP1_EM_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tP1_EM_Transition__tP1_EM_Transition", None)
        self.__tP1_EM_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tP1_EM_StateMachine"):
                opp_val = getattr(old_value, "tP1_EM_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tP1_EM_StateMachine"):
                opp_val = getattr(value, "tP1_EM_StateMachine", None)
                if opp_val is None:
                    setattr(value, "tP1_EM_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tP1_EM_Transition__Transition", None)
        self.__Transition = value
        
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
    def Transition8(self):
        return self.__Transition8

    @Transition8.setter
    def Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tP1_EM_Transition__Transition8", None)
        self.__Transition8 = value
        
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
        old_value = getattr(self, f"_tP1_EM_Transition__incoming", None)
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

class tP1_EM_StateMachine:

    def __init__(self, name: str, tP1_EM_StateMachine2: set["tP1_EM_State"] = None, tP1_EM_StateMachine4: "tP1_EM_State" = None, tP1_EM_StateMachine: set["tP1_EM_Transition"] = None):
        self.name = name
        self.tP1_EM_StateMachine2 = tP1_EM_StateMachine2 if tP1_EM_StateMachine2 is not None else set()
        self.tP1_EM_StateMachine4 = tP1_EM_StateMachine4
        self.tP1_EM_StateMachine = tP1_EM_StateMachine if tP1_EM_StateMachine is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tP1_EM_StateMachine2(self):
        return self.__tP1_EM_StateMachine2

    @tP1_EM_StateMachine2.setter
    def tP1_EM_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tP1_EM_StateMachine__tP1_EM_StateMachine2", None)
        self.__tP1_EM_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tP1_EM_State"):
                    opp_val = getattr(item, "tP1_EM_State", None)
                    
                    if opp_val == self:
                        setattr(item, "tP1_EM_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tP1_EM_State"):
                    opp_val = getattr(item, "tP1_EM_State", None)
                    
                    setattr(item, "tP1_EM_State", self)
                    

    @property
    def tP1_EM_StateMachine(self):
        return self.__tP1_EM_StateMachine

    @tP1_EM_StateMachine.setter
    def tP1_EM_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tP1_EM_StateMachine__tP1_EM_StateMachine", None)
        self.__tP1_EM_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tP1_EM_Transition"):
                    opp_val = getattr(item, "tP1_EM_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "tP1_EM_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tP1_EM_Transition"):
                    opp_val = getattr(item, "tP1_EM_Transition", None)
                    
                    setattr(item, "tP1_EM_Transition", self)
                    

    @property
    def tP1_EM_StateMachine4(self):
        return self.__tP1_EM_StateMachine4

    @tP1_EM_StateMachine4.setter
    def tP1_EM_StateMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tP1_EM_StateMachine__tP1_EM_StateMachine4", None)
        self.__tP1_EM_StateMachine4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tP1_EM_State5"):
                opp_val = getattr(old_value, "tP1_EM_State5", None)
                if opp_val == self:
                    setattr(old_value, "tP1_EM_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tP1_EM_State5"):
                opp_val = getattr(value, "tP1_EM_State5", None)
                setattr(value, "tP1_EM_State5", self)
