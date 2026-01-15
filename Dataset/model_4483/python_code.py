from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ConditionKind(Enum):
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    GREATER_THAN = "GREATER_THAN"
    LESSER_THAN = "LESSER_THAN"


############################################
# Definition of Classes
############################################

class behaviour_Condition:

    def __init__(self, operation: str, key: str, value: str, behaviour_Condition27: "behaviour_While" = None, behaviour_Condition: "behaviour_Choice" = None, behaviour_Condition16: "behaviour_FieldObject" = None):
        self.operation = operation
        self.key = key
        self.value = value
        self.behaviour_Condition27 = behaviour_Condition27
        self.behaviour_Condition = behaviour_Condition
        self.behaviour_Condition16 = behaviour_Condition16
        
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
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def behaviour_Condition(self):
        return self.__behaviour_Condition

    @behaviour_Condition.setter
    def behaviour_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Condition__behaviour_Condition", None)
        self.__behaviour_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Choice"):
                opp_val = getattr(old_value, "behaviour_Choice", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Choice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Choice"):
                opp_val = getattr(value, "behaviour_Choice", None)
                setattr(value, "behaviour_Choice", self)

    @property
    def behaviour_Condition27(self):
        return self.__behaviour_Condition27

    @behaviour_Condition27.setter
    def behaviour_Condition27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Condition__behaviour_Condition27", None)
        self.__behaviour_Condition27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_While26"):
                opp_val = getattr(old_value, "behaviour_While26", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_While26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_While26"):
                opp_val = getattr(value, "behaviour_While26", None)
                setattr(value, "behaviour_While26", self)

    @property
    def behaviour_Condition16(self):
        return self.__behaviour_Condition16

    @behaviour_Condition16.setter
    def behaviour_Condition16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Condition__behaviour_Condition16", None)
        self.__behaviour_Condition16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_FieldObject17"):
                opp_val = getattr(old_value, "behaviour_FieldObject17", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_FieldObject17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_FieldObject17"):
                opp_val = getattr(value, "behaviour_FieldObject17", None)
                setattr(value, "behaviour_FieldObject17", self)

class behaviour_Action:

    pass
class behaviour_FieldObject:

    pass
class Instruction:

    pass
class behaviour_Choice(Instruction):

    pass
class behaviour_PerformAction(Instruction):

    pass
class behaviour_SendMessage(Instruction):

    def __init__(self, messageType: str):
        self.messageType = messageType
        
    @property
    def messageType(self) -> str:
        return self.__messageType

    @messageType.setter
    def messageType(self, messageType: str):
        self.__messageType = messageType

class behaviour_WaitForMessage(Instruction):

    def __init__(self, type: str, timeout: float, behaviour_WaitForMessage21: set["behaviour_Instruction"] = None, behaviour_WaitForMessage: set["behaviour_Instruction"] = None):
        self.type = type
        self.timeout = timeout
        self.behaviour_WaitForMessage21 = behaviour_WaitForMessage21 if behaviour_WaitForMessage21 is not None else set()
        self.behaviour_WaitForMessage = behaviour_WaitForMessage if behaviour_WaitForMessage is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def timeout(self) -> float:
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: float):
        self.__timeout = timeout

    @property
    def behaviour_WaitForMessage(self):
        return self.__behaviour_WaitForMessage

    @behaviour_WaitForMessage.setter
    def behaviour_WaitForMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_WaitForMessage__behaviour_WaitForMessage", None)
        self.__behaviour_WaitForMessage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Instruction19"):
                    opp_val = getattr(item, "behaviour_Instruction19", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Instruction19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Instruction19"):
                    opp_val = getattr(item, "behaviour_Instruction19", None)
                    
                    setattr(item, "behaviour_Instruction19", self)
                    

    @property
    def behaviour_WaitForMessage21(self):
        return self.__behaviour_WaitForMessage21

    @behaviour_WaitForMessage21.setter
    def behaviour_WaitForMessage21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_WaitForMessage__behaviour_WaitForMessage21", None)
        self.__behaviour_WaitForMessage21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Instruction22"):
                    opp_val = getattr(item, "behaviour_Instruction22", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Instruction22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Instruction22"):
                    opp_val = getattr(item, "behaviour_Instruction22", None)
                    
                    setattr(item, "behaviour_Instruction22", self)
                    

class behaviour_Pause(Instruction):

    def __init__(self, duration: float):
        self.duration = duration
        
    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, duration: float):
        self.__duration = duration

class behaviour_PlaceObject(Instruction):

    pass
class behaviour_MoveTo(Instruction):

    pass
class behaviour_MovableObject:

    pass
class behaviour_Lift(Instruction):

    pass
class behaviour_Instruct(Instruction):

    pass
class behaviour_While(Instruction):

    pass
class behaviour_Drone:

    pass
class behaviour_Instruction(ABC):

    pass
class NamedElement:

    pass
class behaviour_DroneBehaviour(NamedElement):

    def __init__(self, canBeInterrupted: bool, behaviour_DroneBehaviour: set["behaviour_Instruction"] = None, behaviour_DroneBehaviour2: set["behaviour_Drone"] = None):
        self.canBeInterrupted = canBeInterrupted
        self.behaviour_DroneBehaviour = behaviour_DroneBehaviour if behaviour_DroneBehaviour is not None else set()
        self.behaviour_DroneBehaviour2 = behaviour_DroneBehaviour2 if behaviour_DroneBehaviour2 is not None else set()
        
    @property
    def canBeInterrupted(self) -> bool:
        return self.__canBeInterrupted

    @canBeInterrupted.setter
    def canBeInterrupted(self, canBeInterrupted: bool):
        self.__canBeInterrupted = canBeInterrupted

    @property
    def behaviour_DroneBehaviour2(self):
        return self.__behaviour_DroneBehaviour2

    @behaviour_DroneBehaviour2.setter
    def behaviour_DroneBehaviour2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DroneBehaviour__behaviour_DroneBehaviour2", None)
        self.__behaviour_DroneBehaviour2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Drone"):
                    opp_val = getattr(item, "behaviour_Drone", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Drone", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Drone"):
                    opp_val = getattr(item, "behaviour_Drone", None)
                    
                    setattr(item, "behaviour_Drone", self)
                    

    @property
    def behaviour_DroneBehaviour(self):
        return self.__behaviour_DroneBehaviour

    @behaviour_DroneBehaviour.setter
    def behaviour_DroneBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DroneBehaviour__behaviour_DroneBehaviour", None)
        self.__behaviour_DroneBehaviour = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Instruction"):
                    opp_val = getattr(item, "behaviour_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Instruction"):
                    opp_val = getattr(item, "behaviour_Instruction", None)
                    
                    setattr(item, "behaviour_Instruction", self)
                    

class behaviour_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
