from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_Transition:

    def __init__(self, name: str, trigger: str, action: str, Transition5: "model_State" = None, Transition7: "model_State" = None, Transition: "model_FSM" = None, incoming: "model_State" = None, outgoing: "model_State" = None, ownedTransitions: "model_FSM" = None):
        self.name = name
        self.trigger = trigger
        self.action = action
        self.Transition5 = Transition5
        self.Transition7 = Transition7
        self.Transition = Transition
        self.incoming = incoming
        self.outgoing = outgoing
        self.ownedTransitions = ownedTransitions
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

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
            if hasattr(old_value, "fsm2"):
                opp_val = getattr(old_value, "fsm2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm2"):
                opp_val = getattr(value, "fsm2", None)
                if opp_val is None:
                    setattr(value, "fsm2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "State10"):
                opp_val = getattr(old_value, "State10", None)
                if opp_val == self:
                    setattr(old_value, "State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State10"):
                opp_val = getattr(value, "State10", None)
                setattr(value, "State10", self)

    @property
    def Transition7(self):
        return self.__Transition7

    @Transition7.setter
    def Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__Transition7", None)
        self.__Transition7 = value
        
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
    def ownedTransitions(self):
        return self.__ownedTransitions

    @ownedTransitions.setter
    def ownedTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__ownedTransitions", None)
        self.__ownedTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM14"):
                opp_val = getattr(old_value, "FSM14", None)
                if opp_val == self:
                    setattr(old_value, "FSM14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM14"):
                opp_val = getattr(value, "FSM14", None)
                setattr(value, "FSM14", self)

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
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State12"):
                opp_val = getattr(old_value, "State12", None)
                if opp_val == self:
                    setattr(old_value, "State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State12"):
                opp_val = getattr(value, "State12", None)
                setattr(value, "State12", self)

class model_State:

    def __init__(self, name: str, tgt: set["model_Transition"] = None, src: set["model_Transition"] = None, ownedStates: "model_FSM" = None, State: "model_FSM" = None, model_State: "model_FSM" = None, State10: "model_Transition" = None, State12: "model_Transition" = None):
        self.name = name
        self.tgt = tgt if tgt is not None else set()
        self.src = src if src is not None else set()
        self.ownedStates = ownedStates
        self.State = State
        self.model_State = model_State
        self.State10 = State10
        self.State12 = State12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State10(self):
        return self.__State10

    @State10.setter
    def State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__State10", None)
        self.__State10 = value
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm"):
                opp_val = getattr(old_value, "fsm", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm"):
                opp_val = getattr(value, "fsm", None)
                if opp_val is None:
                    setattr(value, "fsm", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State12(self):
        return self.__State12

    @State12.setter
    def State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__State12", None)
        self.__State12 = value
        
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
        old_value = getattr(self, f"_model_State__tgt", None)
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
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__src", None)
        self.__src = value if value is not None else set()
        
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
    def ownedStates(self):
        return self.__ownedStates

    @ownedStates.setter
    def ownedStates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__ownedStates", None)
        self.__ownedStates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM"):
                opp_val = getattr(old_value, "FSM", None)
                if opp_val == self:
                    setattr(old_value, "FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM"):
                opp_val = getattr(value, "FSM", None)
                setattr(value, "FSM", self)

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
                if opp_val == self:
                    setattr(old_value, "model_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FSM"):
                opp_val = getattr(value, "model_FSM", None)
                setattr(value, "model_FSM", self)

class model_FSM:

    def __init__(self, name: str, FSM: "model_State" = None, fsm: set["model_State"] = None, fsm2: set["model_Transition"] = None, model_FSM: "model_State" = None, FSM14: "model_Transition" = None):
        self.name = name
        self.FSM = FSM
        self.fsm = fsm if fsm is not None else set()
        self.fsm2 = fsm2 if fsm2 is not None else set()
        self.model_FSM = model_FSM
        self.FSM14 = FSM14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm2(self):
        return self.__fsm2

    @fsm2.setter
    def fsm2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__fsm2", None)
        self.__fsm2 = value if value is not None else set()
        
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
    def fsm(self):
        return self.__fsm

    @fsm.setter
    def fsm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__fsm", None)
        self.__fsm = value if value is not None else set()
        
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
    def model_FSM(self):
        return self.__model_FSM

    @model_FSM.setter
    def model_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__model_FSM", None)
        self.__model_FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_State"):
                opp_val = getattr(old_value, "model_State", None)
                if opp_val == self:
                    setattr(old_value, "model_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_State"):
                opp_val = getattr(value, "model_State", None)
                setattr(value, "model_State", self)

    @property
    def FSM(self):
        return self.__FSM

    @FSM.setter
    def FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__FSM", None)
        self.__FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedStates"):
                opp_val = getattr(old_value, "ownedStates", None)
                if opp_val == self:
                    setattr(old_value, "ownedStates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedStates"):
                opp_val = getattr(value, "ownedStates", None)
                setattr(value, "ownedStates", self)

    @property
    def FSM14(self):
        return self.__FSM14

    @FSM14.setter
    def FSM14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__FSM14", None)
        self.__FSM14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedTransitions"):
                opp_val = getattr(old_value, "ownedTransitions", None)
                if opp_val == self:
                    setattr(old_value, "ownedTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedTransitions"):
                opp_val = getattr(value, "ownedTransitions", None)
                setattr(value, "ownedTransitions", self)
