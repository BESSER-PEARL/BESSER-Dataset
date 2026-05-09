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

    def __init__(self, name: str, trigger: str, Transition: "model_AbstractState" = None, outgoings: "model_AbstractState" = None, model_Transition: "model_AbstractState" = None):
        self.name = name
        self.trigger = trigger
        self.Transition = Transition
        self.outgoings = outgoings
        self.model_Transition = model_Transition
        
        pass
    @property
    def trigger(self):
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger


    @property
    def name(self):
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
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoings(self):
        return self.__outgoings

    @outgoings.setter
    def outgoings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__outgoings", None)
        self.__outgoings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractState5"):
                opp_val = getattr(old_value, "AbstractState5", None)
                if opp_val == self:
                    setattr(old_value, "AbstractState5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractState5"):
                opp_val = getattr(value, "AbstractState5", None)
                setattr(value, "AbstractState5", self)

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
            if hasattr(old_value, "model_AbstractState7"):
                opp_val = getattr(old_value, "model_AbstractState7", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractState7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractState7"):
                opp_val = getattr(value, "model_AbstractState7", None)
                setattr(value, "model_AbstractState7", self)

class model_FiniteStateMachine(AbstractState):

    pass
class model_AbstractState(ABC):

    def __init__(self, name: str, states: "model_FiniteStateMachine" = None, source: set["model_Transition"] = None, model_AbstractState: "model_FiniteStateMachine" = None, AbstractState: "model_FiniteStateMachine" = None, AbstractState5: "model_Transition" = None, model_AbstractState7: "model_Transition" = None):
        self.name = name
        self.states = states
        self.source = source if source is not None else set()
        self.model_AbstractState = model_AbstractState
        self.AbstractState = AbstractState
        self.AbstractState5 = AbstractState5
        self.model_AbstractState7 = model_AbstractState7
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FiniteStateMachine"):
                opp_val = getattr(old_value, "FiniteStateMachine", None)
                if opp_val == self:
                    setattr(old_value, "FiniteStateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FiniteStateMachine"):
                opp_val = getattr(value, "FiniteStateMachine", None)
                setattr(value, "FiniteStateMachine", self)

    @property
    def AbstractState(self):
        return self.__AbstractState

    @AbstractState.setter
    def AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__AbstractState", None)
        self.__AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__source", None)
        self.__source = value if value is not None else set()
        
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
    def model_AbstractState7(self):
        return self.__model_AbstractState7

    @model_AbstractState7.setter
    def model_AbstractState7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__model_AbstractState7", None)
        self.__model_AbstractState7 = value
        
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
    def AbstractState5(self):
        return self.__AbstractState5

    @AbstractState5.setter
    def AbstractState5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__AbstractState5", None)
        self.__AbstractState5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoings"):
                opp_val = getattr(old_value, "outgoings", None)
                if opp_val == self:
                    setattr(old_value, "outgoings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoings"):
                opp_val = getattr(value, "outgoings", None)
                setattr(value, "outgoings", self)
