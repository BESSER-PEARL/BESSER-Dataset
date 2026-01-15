from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class IDBase:

    pass
class ctmc_Label(IDBase):

    def __init__(self, name: str, labels: "ctmc_State" = None, Label: "ctmc_State" = None):
        self.name = name
        self.labels = labels
        self.Label = Label
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def labels(self):
        return self.__labels

    @labels.setter
    def labels(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_Label__labels", None)
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

    @property
    def Label(self):
        return self.__Label

    @Label.setter
    def Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_Label__Label", None)
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

class ctmc_State(IDBase):

    def __init__(self, name: str, exitRate: float, State12: "ctmc_Label" = None, ctmc_State: "ctmc_CTMC" = None, ctmc_State3: "ctmc_CTMC" = None, to: set["ctmc_Transition"] = None, from: set["ctmc_Transition"] = None, state: set["ctmc_Label"] = None, State: "ctmc_Transition" = None, State10: "ctmc_Transition" = None):
        self.name = name
        self.exitRate = exitRate
        self.State12 = State12
        self.ctmc_State = ctmc_State
        self.ctmc_State3 = ctmc_State3
        self.to = to if to is not None else set()
        self.from = from if from is not None else set()
        self.state = state if state is not None else set()
        self.State = State
        self.State10 = State10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def exitRate(self) -> float:
        return self.__exitRate

    @exitRate.setter
    def exitRate(self, exitRate: float):
        self.__exitRate = exitRate

    @property
    def State10(self):
        return self.__State10

    @State10.setter
    def State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_State__State10", None)
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
        old_value = getattr(self, f"_ctmc_State__to", None)
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
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_State__from", None)
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
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_State__State", None)
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
    def ctmc_State3(self):
        return self.__ctmc_State3

    @ctmc_State3.setter
    def ctmc_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_State__ctmc_State3", None)
        self.__ctmc_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ctmc_CTMC2"):
                opp_val = getattr(old_value, "ctmc_CTMC2", None)
                if opp_val == self:
                    setattr(old_value, "ctmc_CTMC2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ctmc_CTMC2"):
                opp_val = getattr(value, "ctmc_CTMC2", None)
                setattr(value, "ctmc_CTMC2", self)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_State__state", None)
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
    def ctmc_State(self):
        return self.__ctmc_State

    @ctmc_State.setter
    def ctmc_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_State__ctmc_State", None)
        self.__ctmc_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ctmc_CTMC"):
                opp_val = getattr(old_value, "ctmc_CTMC", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ctmc_CTMC"):
                opp_val = getattr(value, "ctmc_CTMC", None)
                if opp_val is None:
                    setattr(value, "ctmc_CTMC", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State12(self):
        return self.__State12

    @State12.setter
    def State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_State__State12", None)
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

class ctmc_Transition(IDBase):

    def __init__(self, prob: float, rate: float, Transition: "ctmc_State" = None, Transition6: "ctmc_State" = None, outgoing: "ctmc_State" = None, incoming: "ctmc_State" = None):
        self.prob = prob
        self.rate = rate
        self.Transition = Transition
        self.Transition6 = Transition6
        self.outgoing = outgoing
        self.incoming = incoming
        
    @property
    def prob(self) -> float:
        return self.__prob

    @prob.setter
    def prob(self, prob: float):
        self.__prob = prob

    @property
    def rate(self) -> float:
        return self.__rate

    @rate.setter
    def rate(self, rate: float):
        self.__rate = rate

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_Transition__outgoing", None)
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
        old_value = getattr(self, f"_ctmc_Transition__Transition", None)
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
    def Transition6(self):
        return self.__Transition6

    @Transition6.setter
    def Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_Transition__Transition6", None)
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_Transition__incoming", None)
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

class ctmc_CTMC(IDBase):

    def __init__(self, name: str, ctmc_CTMC: set["ctmc_State"] = None, ctmc_CTMC2: "ctmc_State" = None):
        self.name = name
        self.ctmc_CTMC = ctmc_CTMC if ctmc_CTMC is not None else set()
        self.ctmc_CTMC2 = ctmc_CTMC2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ctmc_CTMC(self):
        return self.__ctmc_CTMC

    @ctmc_CTMC.setter
    def ctmc_CTMC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_CTMC__ctmc_CTMC", None)
        self.__ctmc_CTMC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ctmc_State"):
                    opp_val = getattr(item, "ctmc_State", None)
                    
                    if opp_val == self:
                        setattr(item, "ctmc_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ctmc_State"):
                    opp_val = getattr(item, "ctmc_State", None)
                    
                    setattr(item, "ctmc_State", self)
                    

    @property
    def ctmc_CTMC2(self):
        return self.__ctmc_CTMC2

    @ctmc_CTMC2.setter
    def ctmc_CTMC2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_CTMC__ctmc_CTMC2", None)
        self.__ctmc_CTMC2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ctmc_State3"):
                opp_val = getattr(old_value, "ctmc_State3", None)
                if opp_val == self:
                    setattr(old_value, "ctmc_State3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ctmc_State3"):
                opp_val = getattr(value, "ctmc_State3", None)
                setattr(value, "ctmc_State3", self)
