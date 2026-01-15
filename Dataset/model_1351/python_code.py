from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class FiringElement:

    pass
class statemachine_StateAction(FiringElement):

    pass
class AbstractState:

    pass
class statemachine_FinalState(AbstractState):

    pass
class statemachine_InitialState(AbstractState):

    pass
class statemachine_State(AbstractState):

    pass
class statemachine_FiringElement(ABC):

    def __init__(self, trigger: str, action: str):
        self.trigger = trigger
        self.action = action
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

class statemachine_Transition(FiringElement):

    pass
class statemachine_AbstractState(ABC):

    def __init__(self, name: str, statemachine_AbstractState: "statemachine_StateMachine" = None, source: set["statemachine_Transition"] = None, target: set["statemachine_Transition"] = None, AbstractState: "statemachine_Transition" = None, AbstractState9: "statemachine_Transition" = None):
        self.name = name
        self.statemachine_AbstractState = statemachine_AbstractState
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.AbstractState = AbstractState
        self.AbstractState9 = AbstractState9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def AbstractState9(self):
        return self.__AbstractState9

    @AbstractState9.setter
    def AbstractState9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_AbstractState__AbstractState9", None)
        self.__AbstractState9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitionsAsTarget"):
                opp_val = getattr(old_value, "transitionsAsTarget", None)
                if opp_val == self:
                    setattr(old_value, "transitionsAsTarget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitionsAsTarget"):
                opp_val = getattr(value, "transitionsAsTarget", None)
                setattr(value, "transitionsAsTarget", self)

    @property
    def AbstractState(self):
        return self.__AbstractState

    @AbstractState.setter
    def AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_AbstractState__AbstractState", None)
        self.__AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitionsAsSource"):
                opp_val = getattr(old_value, "transitionsAsSource", None)
                if opp_val == self:
                    setattr(old_value, "transitionsAsSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitionsAsSource"):
                opp_val = getattr(value, "transitionsAsSource", None)
                setattr(value, "transitionsAsSource", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_AbstractState__target", None)
        self.__target = value if value is not None else set()
        
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_AbstractState__source", None)
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
    def statemachine_AbstractState(self):
        return self.__statemachine_AbstractState

    @statemachine_AbstractState.setter
    def statemachine_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_AbstractState__statemachine_AbstractState", None)
        self.__statemachine_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateMachine"):
                opp_val = getattr(old_value, "statemachine_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateMachine"):
                opp_val = getattr(value, "statemachine_StateMachine", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_StateMachine:

    pass