from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractState:

    pass
class model_State(AbstractState):

    pass
class model_Transition:

    def __init__(self, name: str, trigger: str, 10: "model_AbstractState" = None, model_Transition: "model_AbstractState" = None, 4: "model_AbstractState" = None):
        self.name = name
        self.trigger = trigger
        self.10 = 10
        self.model_Transition = model_Transition
        self.4 = 4
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "model_AbstractState13"):
                opp_val = getattr(old_value, "model_AbstractState13", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractState13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractState13"):
                opp_val = getattr(value, "model_AbstractState13", None)
                setattr(value, "model_AbstractState13", self)

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "3"):
                opp_val = getattr(old_value, "3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "3"):
                opp_val = getattr(value, "3", None)
                if opp_val is None:
                    setattr(value, "3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__10", None)
        self.__10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "11"):
                opp_val = getattr(old_value, "11", None)
                if opp_val == self:
                    setattr(old_value, "11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "11"):
                opp_val = getattr(value, "11", None)
                setattr(value, "11", self)

class model_FiniteStateMachine(AbstractState):

    pass
class model_AbstractState(ABC):

    def __init__(self, name: str, : "model_FiniteStateMachine" = None, 8: "model_FiniteStateMachine" = None, 11: "model_Transition" = None, model_AbstractState13: "model_Transition" = None, 3: set["model_Transition"] = None, model_AbstractState: "model_FiniteStateMachine" = None):
        self.name = name
        self. = 
        self.8 = 8
        self.11 = 11
        self.model_AbstractState13 = model_AbstractState13
        self.3 = 3 if 3 is not None else set()
        self.model_AbstractState = model_AbstractState
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__", None)
        self.__ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "1"):
                opp_val = getattr(old_value, "1", None)
                if opp_val == self:
                    setattr(old_value, "1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "1"):
                opp_val = getattr(value, "1", None)
                setattr(value, "1", self)

    @property
    def model_AbstractState(self):
        return self.__model_AbstractState

    @model_AbstractState.setter
    def model_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__model_AbstractState", None)
        self.__model_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FiniteStateMachine"):
                opp_val = getattr(old_value, "model_FiniteStateMachine", None)
                if opp_val == self:
                    setattr(old_value, "model_FiniteStateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FiniteStateMachine"):
                opp_val = getattr(value, "model_FiniteStateMachine", None)
                setattr(value, "model_FiniteStateMachine", self)

    @property
    def model_AbstractState13(self):
        return self.__model_AbstractState13

    @model_AbstractState13.setter
    def model_AbstractState13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__model_AbstractState13", None)
        self.__model_AbstractState13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Transition"):
                opp_val = getattr(old_value, "model_Transition", None)
                if opp_val == self:
                    setattr(old_value, "model_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Transition"):
                opp_val = getattr(value, "model_Transition", None)
                setattr(value, "model_Transition", self)

    @property
    def 8(self):
        return self.__8

    @8.setter
    def 8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__8", None)
        self.__8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "7"):
                opp_val = getattr(old_value, "7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "7"):
                opp_val = getattr(value, "7", None)
                if opp_val is None:
                    setattr(value, "7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 11(self):
        return self.__11

    @11.setter
    def 11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__11", None)
        self.__11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "10"):
                opp_val = getattr(old_value, "10", None)
                if opp_val == self:
                    setattr(old_value, "10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "10"):
                opp_val = getattr(value, "10", None)
                setattr(value, "10", self)

    @property
    def 3(self):
        return self.__3

    @3.setter
    def 3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__3", None)
        self.__3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    if opp_val == self:
                        setattr(item, "4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    setattr(item, "4", self)
                    
