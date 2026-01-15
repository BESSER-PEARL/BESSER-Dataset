from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_Transition:

    def __init__(self, name: str, incoming: "model_State" = None, outgoing: "model_State" = None, model_Transition: "model_FSM" = None, Transition: "model_State" = None, Transition5: "model_State" = None):
        self.name = name
        self.incoming = incoming
        self.outgoing = outgoing
        self.model_Transition = model_Transition
        self.Transition = Transition
        self.Transition5 = Transition5
        
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
        old_value = getattr(self, f"_model_Transition__Transition", None)
        self.__Transition = value
        
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
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__Transition5", None)
        self.__Transition5 = value
        
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

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__outgoing", None)
        self.__outgoing = value
        
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__incoming", None)
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
    def model_Transition(self):
        return self.__model_Transition

    @model_Transition.setter
    def model_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__model_Transition", None)
        self.__model_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FSM2"):
                opp_val = getattr(old_value, "model_FSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FSM2"):
                opp_val = getattr(value, "model_FSM2", None)
                if opp_val is None:
                    setattr(value, "model_FSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_State:

    def __init__(self, name: str, State: "model_Transition" = None, State8: "model_Transition" = None, model_State: "model_FSM" = None, to: set["model_Transition"] = None, from: set["model_Transition"] = None):
        self.name = name
        self.State = State
        self.State8 = State8
        self.model_State = model_State
        self.to = to if to is not None else set()
        self.from = from if from is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State8(self):
        return self.__State8

    @State8.setter
    def State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__State8", None)
        self.__State8 = value
        
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
    def model_State(self):
        return self.__model_State

    @model_State.setter
    def model_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__model_State", None)
        self.__model_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FSM"):
                opp_val = getattr(old_value, "model_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FSM"):
                opp_val = getattr(value, "model_FSM", None)
                if opp_val is None:
                    setattr(value, "model_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__from", None)
        self.__from = value if value is not None else set()
        
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
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__to", None)
        self.__to = value if value is not None else set()
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__State", None)
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

class model_FSM:

    def __init__(self, name: str, model_FSM: set["model_State"] = None, model_FSM2: set["model_Transition"] = None):
        self.name = name
        self.model_FSM = model_FSM if model_FSM is not None else set()
        self.model_FSM2 = model_FSM2 if model_FSM2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_FSM(self):
        return self.__model_FSM

    @model_FSM.setter
    def model_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__model_FSM", None)
        self.__model_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_State"):
                    opp_val = getattr(item, "model_State", None)
                    
                    if opp_val == self:
                        setattr(item, "model_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_State"):
                    opp_val = getattr(item, "model_State", None)
                    
                    setattr(item, "model_State", self)
                    

    @property
    def model_FSM2(self):
        return self.__model_FSM2

    @model_FSM2.setter
    def model_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__model_FSM2", None)
        self.__model_FSM2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Transition"):
                    opp_val = getattr(item, "model_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Transition"):
                    opp_val = getattr(item, "model_Transition", None)
                    
                    setattr(item, "model_Transition", self)
                    
