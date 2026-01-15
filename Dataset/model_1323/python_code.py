from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityType(Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


############################################
# Definition of Classes
############################################

class AbstractStateElement:

    pass
class stateMachine_State(AbstractStateElement):

    pass
class stateMachine_AbstractMachineElement(ABC):

    pass
class stateMachine_StateMachine:

    def __init__(self, name: str, stateMachine_StateMachine: set["stateMachine_AbstractMachineElement"] = None):
        self.name = name
        self.stateMachine_StateMachine = stateMachine_StateMachine if stateMachine_StateMachine is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_StateMachine(self):
        return self.__stateMachine_StateMachine

    @stateMachine_StateMachine.setter
    def stateMachine_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine", None)
        self.__stateMachine_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_AbstractMachineElement"):
                    opp_val = getattr(item, "stateMachine_AbstractMachineElement", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_AbstractMachineElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_AbstractMachineElement"):
                    opp_val = getattr(item, "stateMachine_AbstractMachineElement", None)
                    
                    setattr(item, "stateMachine_AbstractMachineElement", self)
                    

class AbstractMachineElement:

    pass
class stateMachine_AbstractStateElement(AbstractMachineElement):

    def __init__(self, name: str, stateMachine_AbstractStateElement: "stateMachine_StateTransition" = None, stateMachine_AbstractStateElement3: "stateMachine_StateTransition" = None):
        self.name = name
        self.stateMachine_AbstractStateElement = stateMachine_AbstractStateElement
        self.stateMachine_AbstractStateElement3 = stateMachine_AbstractStateElement3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_AbstractStateElement3(self):
        return self.__stateMachine_AbstractStateElement3

    @stateMachine_AbstractStateElement3.setter
    def stateMachine_AbstractStateElement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_AbstractStateElement__stateMachine_AbstractStateElement3", None)
        self.__stateMachine_AbstractStateElement3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateTransition2"):
                opp_val = getattr(old_value, "stateMachine_StateTransition2", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_StateTransition2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateTransition2"):
                opp_val = getattr(value, "stateMachine_StateTransition2", None)
                setattr(value, "stateMachine_StateTransition2", self)

    @property
    def stateMachine_AbstractStateElement(self):
        return self.__stateMachine_AbstractStateElement

    @stateMachine_AbstractStateElement.setter
    def stateMachine_AbstractStateElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_AbstractStateElement__stateMachine_AbstractStateElement", None)
        self.__stateMachine_AbstractStateElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateTransition"):
                opp_val = getattr(old_value, "stateMachine_StateTransition", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_StateTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateTransition"):
                opp_val = getattr(value, "stateMachine_StateTransition", None)
                setattr(value, "stateMachine_StateTransition", self)

class stateMachine_StateTransition(AbstractMachineElement):

    def __init__(self, visibility: str, stateMachine_StateTransition: "stateMachine_AbstractStateElement" = None, stateMachine_StateTransition2: "stateMachine_AbstractStateElement" = None):
        self.visibility = visibility
        self.stateMachine_StateTransition = stateMachine_StateTransition
        self.stateMachine_StateTransition2 = stateMachine_StateTransition2
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def stateMachine_StateTransition(self):
        return self.__stateMachine_StateTransition

    @stateMachine_StateTransition.setter
    def stateMachine_StateTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateTransition__stateMachine_StateTransition", None)
        self.__stateMachine_StateTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_AbstractStateElement"):
                opp_val = getattr(old_value, "stateMachine_AbstractStateElement", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_AbstractStateElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_AbstractStateElement"):
                opp_val = getattr(value, "stateMachine_AbstractStateElement", None)
                setattr(value, "stateMachine_AbstractStateElement", self)

    @property
    def stateMachine_StateTransition2(self):
        return self.__stateMachine_StateTransition2

    @stateMachine_StateTransition2.setter
    def stateMachine_StateTransition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateTransition__stateMachine_StateTransition2", None)
        self.__stateMachine_StateTransition2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_AbstractStateElement3"):
                opp_val = getattr(old_value, "stateMachine_AbstractStateElement3", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_AbstractStateElement3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_AbstractStateElement3"):
                opp_val = getattr(value, "stateMachine_AbstractStateElement3", None)
                setattr(value, "stateMachine_AbstractStateElement3", self)
