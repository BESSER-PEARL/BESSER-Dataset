from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudostateKind(Enum):
    initial = "initial"
    join = "join"
    fork = "fork"
    junction = "junction"


############################################
# Definition of Classes
############################################

class minuml1_BooleanExpression:

    def __init__(self, language: str, body: str, minuml1_BooleanExpression: "minuml1_Guard" = None):
        self.language = language
        self.body = body
        self.minuml1_BooleanExpression = minuml1_BooleanExpression
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def minuml1_BooleanExpression(self):
        return self.__minuml1_BooleanExpression

    @minuml1_BooleanExpression.setter
    def minuml1_BooleanExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minuml1_BooleanExpression__minuml1_BooleanExpression", None)
        self.__minuml1_BooleanExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minuml1_Guard18"):
                opp_val = getattr(old_value, "minuml1_Guard18", None)
                if opp_val == self:
                    setattr(old_value, "minuml1_Guard18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minuml1_Guard18"):
                opp_val = getattr(value, "minuml1_Guard18", None)
                setattr(value, "minuml1_Guard18", self)

class State:

    pass
class minuml1_FinalState(State):

    pass
class minuml1_ActionState(State):

    def __init__(self, isDynamic: bool):
        self.isDynamic = isDynamic
        
    @property
    def isDynamic(self) -> bool:
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: bool):
        self.__isDynamic = isDynamic

class minuml1_ObjectFlowState(State):

    pass
class minuml1_CompositeState(State):

    pass
class StateVertex:

    pass
class minuml1_Pseudostate(StateVertex):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class StateMachine:

    pass
class minuml1_ActivityGraph(StateMachine):

    pass
class minuml1_State(StateVertex):

    pass
class ModelElement:

    pass
class minuml1_Partition(ModelElement):

    pass
class minuml1_Transition(ModelElement):

    pass
class minuml1_StateVertex(ModelElement):

    pass
class minuml1_Guard(ModelElement):

    pass
class minuml1_StateMachine(ModelElement):

    pass
class minuml1_ModelElement:

    def __init__(self, name: str, minuml1_ModelElement11: "minuml1_ObjectFlowState" = None, minuml1_ModelElement: "minuml1_Partition" = None):
        self.name = name
        self.minuml1_ModelElement11 = minuml1_ModelElement11
        self.minuml1_ModelElement = minuml1_ModelElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minuml1_ModelElement(self):
        return self.__minuml1_ModelElement

    @minuml1_ModelElement.setter
    def minuml1_ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minuml1_ModelElement__minuml1_ModelElement", None)
        self.__minuml1_ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minuml1_Partition5"):
                opp_val = getattr(old_value, "minuml1_Partition5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minuml1_Partition5"):
                opp_val = getattr(value, "minuml1_Partition5", None)
                if opp_val is None:
                    setattr(value, "minuml1_Partition5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def minuml1_ModelElement11(self):
        return self.__minuml1_ModelElement11

    @minuml1_ModelElement11.setter
    def minuml1_ModelElement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minuml1_ModelElement__minuml1_ModelElement11", None)
        self.__minuml1_ModelElement11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minuml1_ObjectFlowState"):
                opp_val = getattr(old_value, "minuml1_ObjectFlowState", None)
                if opp_val == self:
                    setattr(old_value, "minuml1_ObjectFlowState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minuml1_ObjectFlowState"):
                opp_val = getattr(value, "minuml1_ObjectFlowState", None)
                setattr(value, "minuml1_ObjectFlowState", self)
