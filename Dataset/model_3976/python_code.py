from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class IDBase:

    pass
class dtmc_Label(IDBase):

    def __init__(self, name: str, Label: "dtmc_State" = None, labels: "dtmc_State" = None):
        self.name = name
        self.Label = Label
        self.labels = labels
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Label(self):
        return self.__Label

    @Label.setter
    def Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Label__Label", None)
        self.__Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state"):
                opp_val = getattr(old_value, "state", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state"):
                opp_val = getattr(value, "state", None)
                if opp_val is None:
                    setattr(value, "state", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def labels(self):
        return self.__labels

    @labels.setter
    def labels(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Label__labels", None)
        self.__labels = value
        
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

class dtmc_Transition(IDBase):

    def __init__(self, prob: float, outgoing: "dtmc_State" = None, incoming: "dtmc_State" = None, Transition: "dtmc_State" = None, Transition6: "dtmc_State" = None):
        self.prob = prob
        self.outgoing = outgoing
        self.incoming = incoming
        self.Transition = Transition
        self.Transition6 = Transition6
        
    @property
    def prob(self) -> float:
        return self.__prob

    @prob.setter
    def prob(self, prob: float):
        self.__prob = prob

    @property
    def Transition6(self):
        return self.__Transition6

    @Transition6.setter
    def Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Transition__Transition6", None)
        self.__Transition6 = value
        
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Transition__Transition", None)
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Transition__incoming", None)
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
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Transition__outgoing", None)
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

class dtmc_State(IDBase):

    def __init__(self, name: str, state: set["dtmc_Label"] = None, State: "dtmc_Transition" = None, State10: "dtmc_Transition" = None, State12: "dtmc_Label" = None, dtmc_State: "dtmc_DTMC" = None, dtmc_State3: "dtmc_DTMC" = None, to: set["dtmc_Transition"] = None, from: set["dtmc_Transition"] = None):
        self.name = name
        self.state = state if state is not None else set()
        self.State = State
        self.State10 = State10
        self.State12 = State12
        self.dtmc_State = dtmc_State
        self.dtmc_State3 = dtmc_State3
        self.to = to if to is not None else set()
        self.from = from if from is not None else set()
        
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
        old_value = getattr(self, f"_dtmc_State__State10", None)
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
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_State__to", None)
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
    def State12(self):
        return self.__State12

    @State12.setter
    def State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_State__State12", None)
        self.__State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "labels"):
                opp_val = getattr(old_value, "labels", None)
                if opp_val == self:
                    setattr(old_value, "labels", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "labels"):
                opp_val = getattr(value, "labels", None)
                setattr(value, "labels", self)

    @property
    def dtmc_State3(self):
        return self.__dtmc_State3

    @dtmc_State3.setter
    def dtmc_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_State__dtmc_State3", None)
        self.__dtmc_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dtmc_DTMC2"):
                opp_val = getattr(old_value, "dtmc_DTMC2", None)
                if opp_val == self:
                    setattr(old_value, "dtmc_DTMC2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dtmc_DTMC2"):
                opp_val = getattr(value, "dtmc_DTMC2", None)
                setattr(value, "dtmc_DTMC2", self)

    @property
    def dtmc_State(self):
        return self.__dtmc_State

    @dtmc_State.setter
    def dtmc_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_State__dtmc_State", None)
        self.__dtmc_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dtmc_DTMC"):
                opp_val = getattr(old_value, "dtmc_DTMC", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dtmc_DTMC"):
                opp_val = getattr(value, "dtmc_DTMC", None)
                if opp_val is None:
                    setattr(value, "dtmc_DTMC", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_State__State", None)
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
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_State__state", None)
        self.__state = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Label"):
                    opp_val = getattr(item, "Label", None)
                    
                    if opp_val == self:
                        setattr(item, "Label", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Label"):
                    opp_val = getattr(item, "Label", None)
                    
                    setattr(item, "Label", self)
                    

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_State__from", None)
        self.__from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition6"):
                    opp_val = getattr(item, "Transition6", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition6"):
                    opp_val = getattr(item, "Transition6", None)
                    
                    setattr(item, "Transition6", self)
                    

class dtmc_DTMC(IDBase):

    def __init__(self, name: str, dtmc_DTMC: set["dtmc_State"] = None, dtmc_DTMC2: "dtmc_State" = None):
        self.name = name
        self.dtmc_DTMC = dtmc_DTMC if dtmc_DTMC is not None else set()
        self.dtmc_DTMC2 = dtmc_DTMC2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dtmc_DTMC(self):
        return self.__dtmc_DTMC

    @dtmc_DTMC.setter
    def dtmc_DTMC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_DTMC__dtmc_DTMC", None)
        self.__dtmc_DTMC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dtmc_State"):
                    opp_val = getattr(item, "dtmc_State", None)
                    
                    if opp_val == self:
                        setattr(item, "dtmc_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dtmc_State"):
                    opp_val = getattr(item, "dtmc_State", None)
                    
                    setattr(item, "dtmc_State", self)
                    

    @property
    def dtmc_DTMC2(self):
        return self.__dtmc_DTMC2

    @dtmc_DTMC2.setter
    def dtmc_DTMC2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_DTMC__dtmc_DTMC2", None)
        self.__dtmc_DTMC2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dtmc_State3"):
                opp_val = getattr(old_value, "dtmc_State3", None)
                if opp_val == self:
                    setattr(old_value, "dtmc_State3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dtmc_State3"):
                opp_val = getattr(value, "dtmc_State3", None)
                setattr(value, "dtmc_State3", self)
