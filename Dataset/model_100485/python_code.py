from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EOperator(Enum):
    Add = "Add"
    Subtract = "Subtract"
    Multiply = "Multiply"
    Divide = "Divide"
    LowerThan = "LowerThan"
    GreaterThan = "GreaterThan"
    LowerEqual = "LowerEqual"
    GreaterEqual = "GreaterEqual"
    Equal = "Equal"
    NotEqual = "NotEqual"
    Not = "Not"
    Negate = "Negate"
    Or = "Or"
    And = "And"
class EType(Enum):
    TBool = "TBool"
    TInt = "TInt"


############################################
# Definition of Classes
############################################

class State:

    pass
class model_state_StateAutomaton:

    pass
class StateAutomaton:

    pass
class Var:

    pass
class model_state_Action:

    pass
class Action:

    pass
class model_state_TransitionSegmentSpecification:

    pass
class TransitionSegmentSpecification:

    pass
class TransitionSegment:

    pass
class IExpressionTerm:

    pass
class model_expression_BoolConst(IExpressionTerm):

    def __init__(self, value: bool, IExpressionTerm26: "model_state_DataStateVariable" = None, IExpressionTerm22: "model_state_TransitionSegmentSpecification" = None, IExpressionTerm8: "model_component_Port" = None, IExpressionTerm30: "model_state_Action" = None, IExpressionTerm: "model_expression_Operation" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class model_expression_Var(IExpressionTerm):

    def __init__(self, identifier: str, IExpressionTerm26: "model_state_DataStateVariable" = None, IExpressionTerm22: "model_state_TransitionSegmentSpecification" = None, IExpressionTerm8: "model_component_Port" = None, IExpressionTerm30: "model_state_Action" = None, IExpressionTerm: "model_expression_Operation" = None):
        self.identifier = identifier
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


class model_expression_IExpressionTerm(ABC):

    pass
class model_INamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Port:

    pass
class model_component_InputPort(Port):

    pass
class model_component_OutputPort(Port):

    pass
class INamedElement:

    pass
class model_state_TransitionSegment(INamedElement):

    pass
class model_state_DataStateVariable(INamedElement):

    def __init__(self, type: str, model_state_DataStateVariable: "IExpressionTerm" = None):
        self.type = type
        self.model_state_DataStateVariable = model_state_DataStateVariable
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def model_state_DataStateVariable(self):
        return self.__model_state_DataStateVariable

    @model_state_DataStateVariable.setter
    def model_state_DataStateVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_state_DataStateVariable__model_state_DataStateVariable", None)
        self.__model_state_DataStateVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IExpressionTerm26"):
                opp_val = getattr(old_value, "IExpressionTerm26", None)
                if opp_val == self:
                    setattr(old_value, "IExpressionTerm26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IExpressionTerm26"):
                opp_val = getattr(value, "IExpressionTerm26", None)
                setattr(value, "IExpressionTerm26", self)

class model_component_Port(INamedElement):

    def __init__(self, type: str, model_component_Port: "IExpressionTerm" = None):
        self.type = type
        self.model_component_Port = model_component_Port
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def model_component_Port(self):
        return self.__model_component_Port

    @model_component_Port.setter
    def model_component_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_component_Port__model_component_Port", None)
        self.__model_component_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IExpressionTerm8"):
                opp_val = getattr(old_value, "IExpressionTerm8", None)
                if opp_val == self:
                    setattr(old_value, "IExpressionTerm8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IExpressionTerm8"):
                opp_val = getattr(value, "IExpressionTerm8", None)
                setattr(value, "IExpressionTerm8", self)

class model_state_State(INamedElement):

    def __init__(self, isInitial: bool, model_state_State: set["TransitionSegmentSpecification"] = None):
        self.isInitial = isInitial
        self.model_state_State = model_state_State if model_state_State is not None else set()
        
        pass
    @property
    def isInitial(self):
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial


    @property
    def model_state_State(self):
        return self.__model_state_State

    @model_state_State.setter
    def model_state_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_state_State__model_state_State", None)
        self.__model_state_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransitionSegmentSpecification"):
                    opp_val = getattr(item, "TransitionSegmentSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "TransitionSegmentSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransitionSegmentSpecification"):
                    opp_val = getattr(item, "TransitionSegmentSpecification", None)
                    
                    setattr(item, "TransitionSegmentSpecification", self)
                    

class model_component_Component(INamedElement):

    pass
class model_expression_Operation(IExpressionTerm):

    def __init__(self, operator: str, model_expression_Operation: set["IExpressionTerm"] = None, IExpressionTerm26: "model_state_DataStateVariable" = None, IExpressionTerm22: "model_state_TransitionSegmentSpecification" = None, IExpressionTerm8: "model_component_Port" = None, IExpressionTerm30: "model_state_Action" = None, IExpressionTerm: "model_expression_Operation" = None):
        self.operator = operator
        self.model_expression_Operation = model_expression_Operation if model_expression_Operation is not None else set()
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def model_expression_Operation(self):
        return self.__model_expression_Operation

    @model_expression_Operation.setter
    def model_expression_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_expression_Operation__model_expression_Operation", None)
        self.__model_expression_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IExpressionTerm"):
                    opp_val = getattr(item, "IExpressionTerm", None)
                    
                    if opp_val == self:
                        setattr(item, "IExpressionTerm", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IExpressionTerm"):
                    opp_val = getattr(item, "IExpressionTerm", None)
                    
                    setattr(item, "IExpressionTerm", self)
                    

class model_expression_IntConst(IExpressionTerm):

    def __init__(self, value: int, IExpressionTerm26: "model_state_DataStateVariable" = None, IExpressionTerm22: "model_state_TransitionSegmentSpecification" = None, IExpressionTerm8: "model_component_Port" = None, IExpressionTerm30: "model_state_Action" = None, IExpressionTerm: "model_expression_Operation" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

