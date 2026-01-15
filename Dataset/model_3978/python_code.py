from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ctmc_State:

    def __init__(self, name: str, exitRate: float, state: set["ctmc_Label"] = None, from: set["ctmc_Transition"] = None, to: set["ctmc_Transition"] = None, State: "ctmc_Transition" = None, State7: "ctmc_Transition" = None, State9: "ctmc_Label" = None, ctmc_State: "ctmc_CTMC" = None):
        self.name = name
        self.exitRate = exitRate
        self.state = state if state is not None else set()
        self.from = from if from is not None else set()
        self.to = to if to is not None else set()
        self.State = State
        self.State7 = State7
        self.State9 = State9
        self.ctmc_State = ctmc_State
        
    @property
    def exitRate(self) -> float:
        return self.__exitRate

    @exitRate.setter
    def exitRate(self, exitRate: float):
        self.__exitRate = exitRate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                if hasattr(item, "Transition4"):
                    opp_val = getattr(item, "Transition4", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition4"):
                    opp_val = getattr(item, "Transition4", None)
                    
                    setattr(item, "Transition4", self)
                    

    @property
    def State9(self):
        return self.__State9

    @State9.setter
    def State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_State__State9", None)
        self.__State9 = value
        
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
    def State7(self):
        return self.__State7

    @State7.setter
    def State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_State__State7", None)
        self.__State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in"):
                opp_val = getattr(old_value, "in", None)
                if opp_val == self:
                    setattr(old_value, "in", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in"):
                opp_val = getattr(value, "in", None)
                setattr(value, "in", self)

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
        old_value = getattr(self, f"_ctmc_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out"):
                opp_val = getattr(old_value, "out", None)
                if opp_val == self:
                    setattr(old_value, "out", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out"):
                opp_val = getattr(value, "out", None)
                setattr(value, "out", self)

class ctmc_CTMC:

    def __init__(self, name: str, ctmc_CTMC: set["ctmc_State"] = None):
        self.name = name
        self.ctmc_CTMC = ctmc_CTMC if ctmc_CTMC is not None else set()
        
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
                    

class ctmc_Transition:

    def __init__(self, name: str, probability: float, duration: float, Transition: "ctmc_State" = None, Transition4: "ctmc_State" = None, out: "ctmc_State" = None, in: "ctmc_State" = None):
        self.name = name
        self.probability = probability
        self.duration = duration
        self.Transition = Transition
        self.Transition4 = Transition4
        self.out = out
        self.in = in
        
    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, duration: float):
        self.__duration = duration

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

    @property
    def Transition4(self):
        return self.__Transition4

    @Transition4.setter
    def Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_Transition__Transition4", None)
        self.__Transition4 = value
        
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
    def out(self):
        return self.__out

    @out.setter
    def out(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_Transition__out", None)
        self.__out = value
        
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
    def in(self):
        return self.__in

    @in.setter
    def in(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctmc_Transition__in", None)
        self.__in = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State7"):
                opp_val = getattr(old_value, "State7", None)
                if opp_val == self:
                    setattr(old_value, "State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State7"):
                opp_val = getattr(value, "State7", None)
                setattr(value, "State7", self)

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

class ctmc_Label:

    def __init__(self, text: str, Label: "ctmc_State" = None, labels: "ctmc_State" = None):
        self.text = text
        self.Label = Label
        self.labels = labels
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

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
            if hasattr(old_value, "State9"):
                opp_val = getattr(old_value, "State9", None)
                if opp_val == self:
                    setattr(old_value, "State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State9"):
                opp_val = getattr(value, "State9", None)
                setattr(value, "State9", self)
