from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class StateType(Enum):
    Default = "Default"
    Start = "Start"
    Success = "Success"
    Failure = "Failure"


############################################
# Definition of Classes
############################################

class markov_Entity:

    def __init__(self, Name: str):
        self.Name = Name
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

class markov_Label:

    def __init__(self, key: str, value: str, markov_Label: "markov_State" = None):
        self.key = key
        self.value = value
        self.markov_Label = markov_Label
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def markov_Label(self):
        return self.__markov_Label

    @markov_Label.setter
    def markov_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_markov_Label__markov_Label", None)
        self.__markov_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "markov_State"):
                opp_val = getattr(old_value, "markov_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "markov_State"):
                opp_val = getattr(value, "markov_State", None)
                if opp_val is None:
                    setattr(value, "markov_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Entity:

    pass
class markov_Transition(Entity):

    def __init__(self, probability: float, markov_Transition: "markov_State" = None, markov_Transition4: "markov_State" = None, markov_Transition10: "markov_MarkovChain" = None):
        self.probability = probability
        self.markov_Transition = markov_Transition
        self.markov_Transition4 = markov_Transition4
        self.markov_Transition10 = markov_Transition10
        
    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

    @property
    def markov_Transition4(self):
        return self.__markov_Transition4

    @markov_Transition4.setter
    def markov_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_markov_Transition__markov_Transition4", None)
        self.__markov_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "markov_State5"):
                opp_val = getattr(old_value, "markov_State5", None)
                if opp_val == self:
                    setattr(old_value, "markov_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "markov_State5"):
                opp_val = getattr(value, "markov_State5", None)
                setattr(value, "markov_State5", self)

    @property
    def markov_Transition10(self):
        return self.__markov_Transition10

    @markov_Transition10.setter
    def markov_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_markov_Transition__markov_Transition10", None)
        self.__markov_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "markov_MarkovChain9"):
                opp_val = getattr(old_value, "markov_MarkovChain9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "markov_MarkovChain9"):
                opp_val = getattr(value, "markov_MarkovChain9", None)
                if opp_val is None:
                    setattr(value, "markov_MarkovChain9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def markov_Transition(self):
        return self.__markov_Transition

    @markov_Transition.setter
    def markov_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_markov_Transition__markov_Transition", None)
        self.__markov_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "markov_State2"):
                opp_val = getattr(old_value, "markov_State2", None)
                if opp_val == self:
                    setattr(old_value, "markov_State2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "markov_State2"):
                opp_val = getattr(value, "markov_State2", None)
                setattr(value, "markov_State2", self)

class markov_MarkovChain(Entity):

    pass
class markov_State(Entity):

    def __init__(self, type: str, traces: str, markov_State: set["markov_Label"] = None, markov_State2: "markov_Transition" = None, markov_State5: "markov_Transition" = None, markov_State7: "markov_MarkovChain" = None):
        self.type = type
        self.traces = traces
        self.markov_State = markov_State if markov_State is not None else set()
        self.markov_State2 = markov_State2
        self.markov_State5 = markov_State5
        self.markov_State7 = markov_State7
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def traces(self) -> str:
        return self.__traces

    @traces.setter
    def traces(self, traces: str):
        self.__traces = traces

    @property
    def markov_State2(self):
        return self.__markov_State2

    @markov_State2.setter
    def markov_State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_markov_State__markov_State2", None)
        self.__markov_State2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "markov_Transition"):
                opp_val = getattr(old_value, "markov_Transition", None)
                if opp_val == self:
                    setattr(old_value, "markov_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "markov_Transition"):
                opp_val = getattr(value, "markov_Transition", None)
                setattr(value, "markov_Transition", self)

    @property
    def markov_State(self):
        return self.__markov_State

    @markov_State.setter
    def markov_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_markov_State__markov_State", None)
        self.__markov_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "markov_Label"):
                    opp_val = getattr(item, "markov_Label", None)
                    
                    if opp_val == self:
                        setattr(item, "markov_Label", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "markov_Label"):
                    opp_val = getattr(item, "markov_Label", None)
                    
                    setattr(item, "markov_Label", self)
                    

    @property
    def markov_State7(self):
        return self.__markov_State7

    @markov_State7.setter
    def markov_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_markov_State__markov_State7", None)
        self.__markov_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "markov_MarkovChain"):
                opp_val = getattr(old_value, "markov_MarkovChain", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "markov_MarkovChain"):
                opp_val = getattr(value, "markov_MarkovChain", None)
                if opp_val is None:
                    setattr(value, "markov_MarkovChain", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def markov_State5(self):
        return self.__markov_State5

    @markov_State5.setter
    def markov_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_markov_State__markov_State5", None)
        self.__markov_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "markov_Transition4"):
                opp_val = getattr(old_value, "markov_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "markov_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "markov_Transition4"):
                opp_val = getattr(value, "markov_Transition4", None)
                setattr(value, "markov_Transition4", self)
