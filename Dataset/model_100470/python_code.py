from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ShiftOperator(Enum):
    right = "right"
    left = "left"
class UnaryOperator(Enum):
    positive = "positive"
    negative = "negative"
    complement = "complement"
class TimeEventType(Enum):
    after = "after"
    every = "every"
class AssignmentOperator(Enum):
    assign = "assign"
    multAssign = "multAssign"
    divAssign = "divAssign"
    modAssign = "modAssign"
    addAssign = "addAssign"
    subAssign = "subAssign"
    leftShiftAssign = "leftShiftAssign"
    rightShiftAssign = "rightShiftAssign"
    andAssign = "andAssign"
    xorAssign = "xorAssign"
    orAssign = "orAssign"
class Direction(Enum):
    LOCAL = "LOCAL"
    IN = "IN"
    OUT = "OUT"
class RelationalOperator(Enum):
    smaller = "smaller"
    smallerEqual = "smallerEqual"
    greater = "greater"
    greaterEqual = "greaterEqual"
    equals = "equals"
    notEquals = "notEquals"
class AdditiveOperator(Enum):
    plus = "plus"
    minus = "minus"
class TimeUnit(Enum):
    second = "second"
    millisecond = "millisecond"
    microsecond = "microsecond"
    nanosecond = "nanosecond"
class MultiplicativeOperator(Enum):
    mul = "mul"
    div = "div"
    mod = "mod"


############################################
# Definition of Classes
############################################

class stext_EventSpec:

    pass
class ReactionProperty:

    pass
class stext_ExitPointSpec(ReactionProperty):

    pass
class stext_EntryPointSpec(ReactionProperty):

    pass
class stext_ReactionProperty:

    pass
class stext_StatechartSpecification:

    def __init__(self, namespace: str, stext_StatechartSpecification5: set["stext_StatechartScope"] = None, stext_StatechartSpecification: "stext_StatechartRoot" = None):
        self.namespace = namespace
        self.stext_StatechartSpecification5 = stext_StatechartSpecification5 if stext_StatechartSpecification5 is not None else set()
        self.stext_StatechartSpecification = stext_StatechartSpecification
        
        pass
    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace


    @property
    def stext_StatechartSpecification(self):
        return self.__stext_StatechartSpecification

    @stext_StatechartSpecification.setter
    def stext_StatechartSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_StatechartSpecification__stext_StatechartSpecification", None)
        self.__stext_StatechartSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_StatechartRoot"):
                opp_val = getattr(old_value, "stext_StatechartRoot", None)
                if opp_val == self:
                    setattr(old_value, "stext_StatechartRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_StatechartRoot"):
                opp_val = getattr(value, "stext_StatechartRoot", None)
                setattr(value, "stext_StatechartRoot", self)

    @property
    def stext_StatechartSpecification5(self):
        return self.__stext_StatechartSpecification5

    @stext_StatechartSpecification5.setter
    def stext_StatechartSpecification5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_StatechartSpecification__stext_StatechartSpecification5", None)
        self.__stext_StatechartSpecification5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stext_StatechartScope"):
                    opp_val = getattr(item, "stext_StatechartScope", None)
                    
                    if opp_val == self:
                        setattr(item, "stext_StatechartScope", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stext_StatechartScope"):
                    opp_val = getattr(item, "stext_StatechartScope", None)
                    
                    setattr(item, "stext_StatechartScope", self)
                    

class DefRoot:

    pass
class stext_StateRoot(DefRoot):

    pass
class stext_StatechartRoot(DefRoot):

    pass
class stext_Parameter:

    pass
class Operation:

    pass
class Declaration:

    pass
class stext_Exitpoint(Declaration):

    pass
class stext_Entrypoint(Declaration):

    pass
class stext_OperationDefinition(Declaration, Operation):

    pass
class Property:

    pass
class Variable:

    pass
class stext_VariableDefinition(Variable, Property):

    def __init__(self, readonly: bool, external: bool, stext_VariableDefinition: "stext_Expression" = None):
        self.readonly = readonly
        self.external = external
        self.stext_VariableDefinition = stext_VariableDefinition
        
        pass
    @property
    def external(self):
        return self.__external

    @external.setter
    def external(self, external: bool):
        self.__external = external


    @property
    def readonly(self):
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: bool):
        self.__readonly = readonly


    @property
    def stext_VariableDefinition(self):
        return self.__stext_VariableDefinition

    @stext_VariableDefinition.setter
    def stext_VariableDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_VariableDefinition__stext_VariableDefinition", None)
        self.__stext_VariableDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression17"):
                opp_val = getattr(old_value, "stext_Expression17", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression17"):
                opp_val = getattr(value, "stext_Expression17", None)
                setattr(value, "stext_Expression17", self)

class stext_EventDerivation:

    pass
class Event:

    pass
class stext_EventDefinition(Event):

    def __init__(self, direction: str, stext_EventDefinition: "stext_EventDerivation" = None):
        self.direction = direction
        self.stext_EventDefinition = stext_EventDefinition
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def stext_EventDefinition(self):
        return self.__stext_EventDefinition

    @stext_EventDefinition.setter
    def stext_EventDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_EventDefinition__stext_EventDefinition", None)
        self.__stext_EventDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_EventDerivation"):
                opp_val = getattr(old_value, "stext_EventDerivation", None)
                if opp_val == self:
                    setattr(old_value, "stext_EventDerivation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_EventDerivation"):
                opp_val = getattr(value, "stext_EventDerivation", None)
                setattr(value, "stext_EventDerivation", self)

class NamedElement:

    pass
class StatechartScope:

    pass
class stext_InternalScope(StatechartScope):

    pass
class stext_InterfaceScope(StatechartScope, NamedElement):

    pass
class Scope:

    pass
class stext_Scope:

    pass
class stext_StatechartScope(Scope):

    pass
class stext_TransitionSpecification:

    pass
class stext_TransitionRoot(DefRoot):

    pass
class stext_StateSpecification:

    pass
class stext_DefRoot:

    pass
class stext_Root:

    pass
class stext_State:

    pass
class stext_NamedElement:

    pass
class stext_Feature:

    pass
class Expression:

    pass
class stext_NumericalAddSubtractExpression(Expression):

    def __init__(self, operator: str, stext_NumericalAddSubtractExpression: "stext_Expression" = None, stext_NumericalAddSubtractExpression93: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalAddSubtractExpression = stext_NumericalAddSubtractExpression
        self.stext_NumericalAddSubtractExpression93 = stext_NumericalAddSubtractExpression93
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_NumericalAddSubtractExpression93(self):
        return self.__stext_NumericalAddSubtractExpression93

    @stext_NumericalAddSubtractExpression93.setter
    def stext_NumericalAddSubtractExpression93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalAddSubtractExpression__stext_NumericalAddSubtractExpression93", None)
        self.__stext_NumericalAddSubtractExpression93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression94"):
                opp_val = getattr(old_value, "stext_Expression94", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression94"):
                opp_val = getattr(value, "stext_Expression94", None)
                setattr(value, "stext_Expression94", self)

    @property
    def stext_NumericalAddSubtractExpression(self):
        return self.__stext_NumericalAddSubtractExpression

    @stext_NumericalAddSubtractExpression.setter
    def stext_NumericalAddSubtractExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalAddSubtractExpression__stext_NumericalAddSubtractExpression", None)
        self.__stext_NumericalAddSubtractExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression91"):
                opp_val = getattr(old_value, "stext_Expression91", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression91"):
                opp_val = getattr(value, "stext_Expression91", None)
                setattr(value, "stext_Expression91", self)

class stext_LogicalAndExpression(Expression):

    pass
class stext_BitwiseAndExpression(Expression):

    pass
class stext_BitwiseXorExpression(Expression):

    pass
class stext_BitwiseOrExpression(Expression):

    pass
class stext_TypedElementReferenceExpression(Expression):

    pass
class stext_AssignmentExpression(Expression):

    def __init__(self, operator: str, stext_AssignmentExpression: "stext_Expression" = None, stext_AssignmentExpression43: "stext_Expression" = None):
        self.operator = operator
        self.stext_AssignmentExpression = stext_AssignmentExpression
        self.stext_AssignmentExpression43 = stext_AssignmentExpression43
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_AssignmentExpression43(self):
        return self.__stext_AssignmentExpression43

    @stext_AssignmentExpression43.setter
    def stext_AssignmentExpression43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_AssignmentExpression__stext_AssignmentExpression43", None)
        self.__stext_AssignmentExpression43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression44"):
                opp_val = getattr(old_value, "stext_Expression44", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression44"):
                opp_val = getattr(value, "stext_Expression44", None)
                setattr(value, "stext_Expression44", self)

    @property
    def stext_AssignmentExpression(self):
        return self.__stext_AssignmentExpression

    @stext_AssignmentExpression.setter
    def stext_AssignmentExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_AssignmentExpression__stext_AssignmentExpression", None)
        self.__stext_AssignmentExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression41"):
                opp_val = getattr(old_value, "stext_Expression41", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression41"):
                opp_val = getattr(value, "stext_Expression41", None)
                setattr(value, "stext_Expression41", self)

class stext_NumericalUnaryExpression(Expression):

    def __init__(self, operator: str, stext_NumericalUnaryExpression: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalUnaryExpression = stext_NumericalUnaryExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_NumericalUnaryExpression(self):
        return self.__stext_NumericalUnaryExpression

    @stext_NumericalUnaryExpression.setter
    def stext_NumericalUnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalUnaryExpression__stext_NumericalUnaryExpression", None)
        self.__stext_NumericalUnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression101"):
                opp_val = getattr(old_value, "stext_Expression101", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression101"):
                opp_val = getattr(value, "stext_Expression101", None)
                setattr(value, "stext_Expression101", self)

class stext_LogicalNotExpression(Expression):

    pass
class stext_PrimitiveValueExpression(Expression):

    pass
class stext_EventValueReferenceExpression(Expression):

    pass
class stext_ShiftExpression(Expression):

    def __init__(self, operator: str, stext_ShiftExpression: "stext_Expression" = None, stext_ShiftExpression88: "stext_Expression" = None):
        self.operator = operator
        self.stext_ShiftExpression = stext_ShiftExpression
        self.stext_ShiftExpression88 = stext_ShiftExpression88
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_ShiftExpression(self):
        return self.__stext_ShiftExpression

    @stext_ShiftExpression.setter
    def stext_ShiftExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_ShiftExpression__stext_ShiftExpression", None)
        self.__stext_ShiftExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression86"):
                opp_val = getattr(old_value, "stext_Expression86", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression86"):
                opp_val = getattr(value, "stext_Expression86", None)
                setattr(value, "stext_Expression86", self)

    @property
    def stext_ShiftExpression88(self):
        return self.__stext_ShiftExpression88

    @stext_ShiftExpression88.setter
    def stext_ShiftExpression88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_ShiftExpression__stext_ShiftExpression88", None)
        self.__stext_ShiftExpression88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression89"):
                opp_val = getattr(old_value, "stext_Expression89", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression89"):
                opp_val = getattr(value, "stext_Expression89", None)
                setattr(value, "stext_Expression89", self)

class stext_LogicalOrExpression(Expression):

    pass
class stext_ConditionalExpression(Expression):

    pass
class stext_ActiveStateReferenceExpression(Expression):

    pass
class stext_NumericalMultiplyDivideExpression(Expression):

    def __init__(self, operator: str, stext_NumericalMultiplyDivideExpression: "stext_Expression" = None, stext_NumericalMultiplyDivideExpression98: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalMultiplyDivideExpression = stext_NumericalMultiplyDivideExpression
        self.stext_NumericalMultiplyDivideExpression98 = stext_NumericalMultiplyDivideExpression98
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_NumericalMultiplyDivideExpression98(self):
        return self.__stext_NumericalMultiplyDivideExpression98

    @stext_NumericalMultiplyDivideExpression98.setter
    def stext_NumericalMultiplyDivideExpression98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalMultiplyDivideExpression__stext_NumericalMultiplyDivideExpression98", None)
        self.__stext_NumericalMultiplyDivideExpression98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression99"):
                opp_val = getattr(old_value, "stext_Expression99", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression99"):
                opp_val = getattr(value, "stext_Expression99", None)
                setattr(value, "stext_Expression99", self)

    @property
    def stext_NumericalMultiplyDivideExpression(self):
        return self.__stext_NumericalMultiplyDivideExpression

    @stext_NumericalMultiplyDivideExpression.setter
    def stext_NumericalMultiplyDivideExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalMultiplyDivideExpression__stext_NumericalMultiplyDivideExpression", None)
        self.__stext_NumericalMultiplyDivideExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression96"):
                opp_val = getattr(old_value, "stext_Expression96", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression96"):
                opp_val = getattr(value, "stext_Expression96", None)
                setattr(value, "stext_Expression96", self)

class stext_FeatureCall(Expression):

    def __init__(self, operationCall: bool, stext_FeatureCall: "stext_Expression" = None, stext_FeatureCall106: "stext_Feature" = None, stext_FeatureCall108: set["stext_Expression"] = None):
        self.operationCall = operationCall
        self.stext_FeatureCall = stext_FeatureCall
        self.stext_FeatureCall106 = stext_FeatureCall106
        self.stext_FeatureCall108 = stext_FeatureCall108 if stext_FeatureCall108 is not None else set()
        
        pass
    @property
    def operationCall(self):
        return self.__operationCall

    @operationCall.setter
    def operationCall(self, operationCall: bool):
        self.__operationCall = operationCall


    @property
    def stext_FeatureCall(self):
        return self.__stext_FeatureCall

    @stext_FeatureCall.setter
    def stext_FeatureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_FeatureCall__stext_FeatureCall", None)
        self.__stext_FeatureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression104"):
                opp_val = getattr(old_value, "stext_Expression104", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression104"):
                opp_val = getattr(value, "stext_Expression104", None)
                setattr(value, "stext_Expression104", self)

    @property
    def stext_FeatureCall108(self):
        return self.__stext_FeatureCall108

    @stext_FeatureCall108.setter
    def stext_FeatureCall108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_FeatureCall__stext_FeatureCall108", None)
        self.__stext_FeatureCall108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stext_Expression109"):
                    opp_val = getattr(item, "stext_Expression109", None)
                    
                    if opp_val == self:
                        setattr(item, "stext_Expression109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stext_Expression109"):
                    opp_val = getattr(item, "stext_Expression109", None)
                    
                    setattr(item, "stext_Expression109", self)
                    

    @property
    def stext_FeatureCall106(self):
        return self.__stext_FeatureCall106

    @stext_FeatureCall106.setter
    def stext_FeatureCall106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_FeatureCall__stext_FeatureCall106", None)
        self.__stext_FeatureCall106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Feature"):
                opp_val = getattr(old_value, "stext_Feature", None)
                if opp_val == self:
                    setattr(old_value, "stext_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Feature"):
                opp_val = getattr(value, "stext_Feature", None)
                setattr(value, "stext_Feature", self)

class stext_LogicalRelationExpression(Expression):

    def __init__(self, operator: str, stext_LogicalRelationExpression: "stext_Expression" = None, stext_LogicalRelationExpression83: "stext_Expression" = None):
        self.operator = operator
        self.stext_LogicalRelationExpression = stext_LogicalRelationExpression
        self.stext_LogicalRelationExpression83 = stext_LogicalRelationExpression83
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_LogicalRelationExpression83(self):
        return self.__stext_LogicalRelationExpression83

    @stext_LogicalRelationExpression83.setter
    def stext_LogicalRelationExpression83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_LogicalRelationExpression__stext_LogicalRelationExpression83", None)
        self.__stext_LogicalRelationExpression83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression84"):
                opp_val = getattr(old_value, "stext_Expression84", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression84"):
                opp_val = getattr(value, "stext_Expression84", None)
                setattr(value, "stext_Expression84", self)

    @property
    def stext_LogicalRelationExpression(self):
        return self.__stext_LogicalRelationExpression

    @stext_LogicalRelationExpression.setter
    def stext_LogicalRelationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_LogicalRelationExpression__stext_LogicalRelationExpression", None)
        self.__stext_LogicalRelationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression81"):
                opp_val = getattr(old_value, "stext_Expression81", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression81"):
                opp_val = getattr(value, "stext_Expression81", None)
                setattr(value, "stext_Expression81", self)

class stext_EventRaisingExpression(Expression):

    pass
class Effect:

    pass
class stext_ReactionEffect(Effect):

    pass
class Trigger:

    pass
class stext_ReactionTrigger(Trigger):

    pass
class stext_SimpleScope(Scope):

    pass
class stext_ReactionProperties:

    pass
class Reaction:

    pass
class stext_TransitionReaction(Reaction):

    pass
class stext_LocalReaction(Declaration, Reaction):

    pass
class Literal:

    pass
class stext_IntLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class stext_HexLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class stext_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class stext_RealLiteral(Literal):

    def __init__(self, value: float):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class stext_BoolLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class stext_Literal:

    pass
class Statement:

    pass
class stext_Expression(Statement):

    pass
class BuiltinEventSpec:

    pass
class stext_ExitEvent(BuiltinEventSpec):

    pass
class stext_DefaultEvent(BuiltinEventSpec):

    pass
class stext_OnCycleEvent(BuiltinEventSpec):

    pass
class stext_AlwaysEvent(BuiltinEventSpec):

    pass
class stext_EntryEvent(BuiltinEventSpec):

    pass
class EventSpec:

    pass
class stext_TimeEventSpec(EventSpec):

    def __init__(self, type: str, value: int, unit: str):
        self.type = type
        self.value = value
        self.unit = unit
        
        pass
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class stext_BuiltinEventSpec(EventSpec):

    pass
class stext_RegularEventSpec(EventSpec):

    pass