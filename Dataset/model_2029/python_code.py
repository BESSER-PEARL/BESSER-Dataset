from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class idm_StateMachine:

    def __init__(self, name: str, idm_StateMachine: set["idm_State"] = None, idm_StateMachine2: set["idm_Transition"] = None):
        self.name = name
        self.idm_StateMachine = idm_StateMachine if idm_StateMachine is not None else set()
        self.idm_StateMachine2 = idm_StateMachine2 if idm_StateMachine2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idm_StateMachine2(self):
        return self.__idm_StateMachine2

    @idm_StateMachine2.setter
    def idm_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idm_StateMachine__idm_StateMachine2", None)
        self.__idm_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idm_Transition"):
                    opp_val = getattr(item, "idm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "idm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idm_Transition"):
                    opp_val = getattr(item, "idm_Transition", None)
                    
                    setattr(item, "idm_Transition", self)
                    

    @property
    def idm_StateMachine(self):
        return self.__idm_StateMachine

    @idm_StateMachine.setter
    def idm_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idm_StateMachine__idm_StateMachine", None)
        self.__idm_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idm_State"):
                    opp_val = getattr(item, "idm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "idm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idm_State"):
                    opp_val = getattr(item, "idm_State", None)
                    
                    setattr(item, "idm_State", self)
                    

class idm_Transition:

    def __init__(self, name: str, idm_Transition: "idm_StateMachine" = None, Transition: "idm_State" = None, Transition5: "idm_State" = None, from: set["idm_State"] = None, to: set["idm_State"] = None):
        self.name = name
        self.idm_Transition = idm_Transition
        self.Transition = Transition
        self.Transition5 = Transition5
        self.from = from if from is not None else set()
        self.to = to if to is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idm_Transition__from", None)
        self.__from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idm_Transition__Transition", None)
        self.__Transition = value
        
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
        old_value = getattr(self, f"_idm_Transition__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State8"):
                    opp_val = getattr(item, "State8", None)
                    
                    if opp_val == self:
                        setattr(item, "State8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State8"):
                    opp_val = getattr(item, "State8", None)
                    
                    setattr(item, "State8", self)
                    

    @property
    def idm_Transition(self):
        return self.__idm_Transition

    @idm_Transition.setter
    def idm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idm_Transition__idm_Transition", None)
        self.__idm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idm_StateMachine2"):
                opp_val = getattr(old_value, "idm_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idm_StateMachine2"):
                opp_val = getattr(value, "idm_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "idm_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idm_Transition__Transition5", None)
        self.__Transition5 = value
        
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

class idm_State:

    def __init__(self, name: str, idm_State: "idm_StateMachine" = None, outgoing: "idm_Transition" = None, incoming: "idm_Transition" = None, State: "idm_Transition" = None, State8: "idm_Transition" = None):
        self.name = name
        self.idm_State = idm_State
        self.outgoing = outgoing
        self.incoming = incoming
        self.State = State
        self.State8 = State8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idm_State(self):
        return self.__idm_State

    @idm_State.setter
    def idm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idm_State__idm_State", None)
        self.__idm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idm_StateMachine"):
                opp_val = getattr(old_value, "idm_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idm_StateMachine"):
                opp_val = getattr(value, "idm_StateMachine", None)
                if opp_val is None:
                    setattr(value, "idm_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idm_State__incoming", None)
        self.__incoming = value
        
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
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idm_State__outgoing", None)
        self.__outgoing = value
        
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
        old_value = getattr(self, f"_idm_State__State", None)
        self.__State = value
        
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
    def State8(self):
        return self.__State8

    @State8.setter
    def State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idm_State__State8", None)
        self.__State8 = value
        
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
