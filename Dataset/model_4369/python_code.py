from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Keys(Enum):
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"
    SPACE = "SPACE"
    ENTER = "ENTER"
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    J = "J"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    U = "U"


############################################
# Definition of Classes
############################################

class Event:

    pass
class klang_ActorEvent(Event):

    pass
class klang_GlobalEvent(Event):

    pass
class klang_TreeNode(ABC):

    pass
class klang_AbstractActor(ABC):

    def __init__(self, name: str, subject: str, subjectType: str, actor: set["klang_EventHandler"] = None, actor9: set["klang_VariableDeclaration"] = None):
        self.name = name
        self.subject = subject
        self.subjectType = subjectType
        self.actor = actor if actor is not None else set()
        self.actor9 = actor9 if actor9 is not None else set()
        
    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def subjectType(self) -> str:
        return self.__subjectType

    @subjectType.setter
    def subjectType(self, subjectType: str):
        self.__subjectType = subjectType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def actor(self):
        return self.__actor

    @actor.setter
    def actor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_klang_AbstractActor__actor", None)
        self.__actor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EventHandler"):
                    opp_val = getattr(item, "EventHandler", None)
                    
                    if opp_val == self:
                        setattr(item, "EventHandler", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EventHandler"):
                    opp_val = getattr(item, "EventHandler", None)
                    
                    setattr(item, "EventHandler", self)
                    

    @property
    def actor9(self):
        return self.__actor9

    @actor9.setter
    def actor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_klang_AbstractActor__actor9", None)
        self.__actor9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableDeclaration"):
                    opp_val = getattr(item, "VariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableDeclaration"):
                    opp_val = getattr(item, "VariableDeclaration", None)
                    
                    setattr(item, "VariableDeclaration", self)
                    

    def getVariableDeclarations(self, variableName: str):
        # TODO: Implement getVariableDeclarations method
        pass

    def isInScope(self, variableName: str) -> bool:
        # TODO: Implement isInScope method
        pass

    def getVariableDeclaration(self, variableName: str) -> str:
        # TODO: Implement getVariableDeclaration method
        pass

    def isInLocalScope(self, variableName: str) -> bool:
        # TODO: Implement isInLocalScope method
        pass

    def isInParentScope(self, variableName: str) -> bool:
        # TODO: Implement isInParentScope method
        pass

class ActorEvent:

    pass
class klang_CollisionEvent(ActorEvent):

    pass
class klang_ClickEvent(ActorEvent):

    pass
class GlobalEvent:

    pass
class klang_MessageReceivedEvent(GlobalEvent):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class klang_KeyPressEvent(GlobalEvent):

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class klang_GameStartEvent(GlobalEvent):

    pass
class klang_SpriteActor:

    pass
class klang_Program:

    pass
class klang_SceneActor:

    pass
class klang_Expression:

    pass
class klang_VariableDeclaration:

    def __init__(self, name: str, klang_VariableDeclaration: "klang_Expression" = None, VariableDeclaration: "klang_AbstractActor" = None):
        self.name = name
        self.klang_VariableDeclaration = klang_VariableDeclaration
        self.VariableDeclaration = VariableDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def klang_VariableDeclaration(self):
        return self.__klang_VariableDeclaration

    @klang_VariableDeclaration.setter
    def klang_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_klang_VariableDeclaration__klang_VariableDeclaration", None)
        self.__klang_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "klang_Expression"):
                opp_val = getattr(old_value, "klang_Expression", None)
                if opp_val == self:
                    setattr(old_value, "klang_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "klang_Expression"):
                opp_val = getattr(value, "klang_Expression", None)
                setattr(value, "klang_Expression", self)

    @property
    def VariableDeclaration(self):
        return self.__VariableDeclaration

    @VariableDeclaration.setter
    def VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_klang_VariableDeclaration__VariableDeclaration", None)
        self.__VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actor9"):
                opp_val = getattr(old_value, "actor9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actor9"):
                opp_val = getattr(value, "actor9", None)
                if opp_val is None:
                    setattr(value, "actor9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class klang_Event(ABC):

    def __init__(self, klang_Event: "klang_EventHandler" = None):
        self.klang_Event = klang_Event
        
    @property
    def klang_Event(self):
        return self.__klang_Event

    @klang_Event.setter
    def klang_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_klang_Event__klang_Event", None)
        self.__klang_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "klang_EventHandler5"):
                opp_val = getattr(old_value, "klang_EventHandler5", None)
                if opp_val == self:
                    setattr(old_value, "klang_EventHandler5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "klang_EventHandler5"):
                opp_val = getattr(value, "klang_EventHandler5", None)
                setattr(value, "klang_EventHandler5", self)

    def matchingEvent(self, other: str) -> bool:
        # TODO: Implement matchingEvent method
        pass

class klang_Statement:

    pass
class klang_EventHandler:

    pass