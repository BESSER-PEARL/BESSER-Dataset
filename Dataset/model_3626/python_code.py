from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudostateKind(Enum):
    junction = "junction"
    inital = "inital"
    join = "join"
    fork = "fork"


############################################
# Definition of Classes
############################################

class minuml1_BooleanExpression:

    def __init__(self, language: str, body: str, minuml1_BooleanExpression: "minuml1_Guard" = None):
        self.language = language
        self.body = body
        self.minuml1_BooleanExpression = minuml1_BooleanExpression
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

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
            if hasattr(old_value, "minuml1_Guard17"):
                opp_val = getattr(old_value, "minuml1_Guard17", None)
                if opp_val == self:
                    setattr(old_value, "minuml1_Guard17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minuml1_Guard17"):
                opp_val = getattr(value, "minuml1_Guard17", None)
                setattr(value, "minuml1_Guard17", self)

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

class State:

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

class minuml1_FinalState(State):

    pass
class minuml1_ObjectFlowState(State):

    pass
class minuml1_CompositeState(State):

    pass
class minuml1_State(StateVertex):

    pass
class StateMachine:

    pass
class minuml1_Activity(StateMachine):

    pass
class ModelElement:

    pass
class minuml1_Transition(ModelElement):

    pass
class minuml1_Guard(ModelElement):

    pass
class minuml1_StateVertex(ModelElement):

    pass
class minuml1_StateMachine(ModelElement):

    pass
class minuml1_Partition(ModelElement):

    pass
class minuml1_ModelElement:

    def __init__(self, name: str, contents: "minuml1_Partition" = None, ModelElement: "minuml1_Partition" = None, minuml1_ModelElement: "minuml1_ObjectFlowState" = None):
        self.name = name
        self.contents = contents
        self.ModelElement = ModelElement
        self.minuml1_ModelElement = minuml1_ModelElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ModelElement(self):
        return self.__ModelElement

    @ModelElement.setter
    def ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minuml1_ModelElement__ModelElement", None)
        self.__ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partition"):
                opp_val = getattr(old_value, "partition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partition"):
                opp_val = getattr(value, "partition", None)
                if opp_val is None:
                    setattr(value, "partition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minuml1_ModelElement__contents", None)
        self.__contents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Partition"):
                opp_val = getattr(old_value, "Partition", None)
                if opp_val == self:
                    setattr(old_value, "Partition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Partition"):
                opp_val = getattr(value, "Partition", None)
                setattr(value, "Partition", self)

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
            if hasattr(old_value, "minuml1_ObjectFlowState"):
                opp_val = getattr(old_value, "minuml1_ObjectFlowState", None)
                if opp_val == self:
                    setattr(old_value, "minuml1_ObjectFlowState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minuml1_ObjectFlowState"):
                opp_val = getattr(value, "minuml1_ObjectFlowState", None)
                setattr(value, "minuml1_ObjectFlowState", self)
