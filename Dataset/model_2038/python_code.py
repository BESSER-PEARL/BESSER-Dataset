from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sAAP_StateMachine:

    def __init__(self, name: str, sAAP_StateMachine5: set["sAAP_Transition"] = None, sAAP_StateMachine: set["sAAP_State"] = None):
        self.name = name
        self.sAAP_StateMachine5 = sAAP_StateMachine5 if sAAP_StateMachine5 is not None else set()
        self.sAAP_StateMachine = sAAP_StateMachine if sAAP_StateMachine is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sAAP_StateMachine(self):
        return self.__sAAP_StateMachine

    @sAAP_StateMachine.setter
    def sAAP_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sAAP_StateMachine__sAAP_StateMachine", None)
        self.__sAAP_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sAAP_State"):
                    opp_val = getattr(item, "sAAP_State", None)
                    
                    if opp_val == self:
                        setattr(item, "sAAP_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sAAP_State"):
                    opp_val = getattr(item, "sAAP_State", None)
                    
                    setattr(item, "sAAP_State", self)
                    

    @property
    def sAAP_StateMachine5(self):
        return self.__sAAP_StateMachine5

    @sAAP_StateMachine5.setter
    def sAAP_StateMachine5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sAAP_StateMachine__sAAP_StateMachine5", None)
        self.__sAAP_StateMachine5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sAAP_Transition"):
                    opp_val = getattr(item, "sAAP_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "sAAP_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sAAP_Transition"):
                    opp_val = getattr(item, "sAAP_Transition", None)
                    
                    setattr(item, "sAAP_Transition", self)
                    

    def execute(self):
        # TODO: Implement execute method
        pass

class sAAP_Transition:

    def __init__(self, name: str, sAAP_Transition: "sAAP_StateMachine" = None, Transition: "sAAP_State" = None, Transition2: "sAAP_State" = None, outgoing: "sAAP_State" = None, incoming: "sAAP_State" = None):
        self.name = name
        self.sAAP_Transition = sAAP_Transition
        self.Transition = Transition
        self.Transition2 = Transition2
        self.outgoing = outgoing
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
        old_value = getattr(self, f"_sAAP_Transition__incoming", None)
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
    def Transition2(self):
        return self.__Transition2

    @Transition2.setter
    def Transition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sAAP_Transition__Transition2", None)
        self.__Transition2 = value
        
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

    @property
    def sAAP_Transition(self):
        return self.__sAAP_Transition

    @sAAP_Transition.setter
    def sAAP_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sAAP_Transition__sAAP_Transition", None)
        self.__sAAP_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sAAP_StateMachine5"):
                opp_val = getattr(old_value, "sAAP_StateMachine5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sAAP_StateMachine5"):
                opp_val = getattr(value, "sAAP_StateMachine5", None)
                if opp_val is None:
                    setattr(value, "sAAP_StateMachine5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sAAP_Transition__outgoing", None)
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

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sAAP_Transition__Transition", None)
        self.__Transition = value
        
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

class sAAP_State:

    def __init__(self, name: str, default: bool, from: set["sAAP_Transition"] = None, to: set["sAAP_Transition"] = None, sAAP_State: "sAAP_StateMachine" = None, State: "sAAP_Transition" = None, State8: "sAAP_Transition" = None):
        self.name = name
        self.default = default
        self.from = from if from is not None else set()
        self.to = to if to is not None else set()
        self.sAAP_State = sAAP_State
        self.State = State
        self.State8 = State8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def State8(self):
        return self.__State8

    @State8.setter
    def State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sAAP_State__State8", None)
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
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sAAP_State__from", None)
        self.__from = value if value is not None else set()
        
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
    def sAAP_State(self):
        return self.__sAAP_State

    @sAAP_State.setter
    def sAAP_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sAAP_State__sAAP_State", None)
        self.__sAAP_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sAAP_StateMachine"):
                opp_val = getattr(old_value, "sAAP_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sAAP_StateMachine"):
                opp_val = getattr(value, "sAAP_StateMachine", None)
                if opp_val is None:
                    setattr(value, "sAAP_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sAAP_State__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition2"):
                    opp_val = getattr(item, "Transition2", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition2"):
                    opp_val = getattr(item, "Transition2", None)
                    
                    setattr(item, "Transition2", self)
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sAAP_State__State", None)
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
