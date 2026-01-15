from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ExecutionType(Enum):
    unspecified = "unspecified"
    search = "search"
    incremental = "incremental"
class CompareFeature(Enum):
    equality = "equality"
    inequality = "inequality"
class ClosureType(Enum):
    original = "original"
    reflexive_transitive = "reflexive_transitive"
    transitive = "transitive"
class ParameterDirection(Enum):
    inout = "inout"
    in = "in"
    out = "out"


############################################
# Definition of Classes
############################################

class vql_XBooleanLiteral:

    pass
class vql_XNumberLiteral:

    pass
class LiteralValueReference:

    pass
class vql_ListValue(LiteralValueReference):

    def __init__(self, vql_ListValue: set["vql_ValueReference"] = None):
        self.vql_ListValue = vql_ListValue if vql_ListValue is not None else set()
        
    @property
    def vql_ListValue(self):
        return self.__vql_ListValue

    @vql_ListValue.setter
    def vql_ListValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_ListValue__vql_ListValue", None)
        self.__vql_ListValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vql_ValueReference73"):
                    opp_val = getattr(item, "vql_ValueReference73", None)
                    
                    if opp_val == self:
                        setattr(item, "vql_ValueReference73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vql_ValueReference73"):
                    opp_val = getattr(item, "vql_ValueReference73", None)
                    
                    setattr(item, "vql_ValueReference73", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_NumberValue(LiteralValueReference):

    def __init__(self, negative: bool, vql_NumberValue: "vql_XNumberLiteral" = None):
        self.negative = negative
        self.vql_NumberValue = vql_NumberValue
        
    @property
    def negative(self) -> bool:
        return self.__negative

    @negative.setter
    def negative(self, negative: bool):
        self.__negative = negative

    @property
    def vql_NumberValue(self):
        return self.__vql_NumberValue

    @vql_NumberValue.setter
    def vql_NumberValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_NumberValue__vql_NumberValue", None)
        self.__vql_NumberValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_XNumberLiteral"):
                opp_val = getattr(old_value, "vql_XNumberLiteral", None)
                if opp_val == self:
                    setattr(old_value, "vql_XNumberLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_XNumberLiteral"):
                opp_val = getattr(value, "vql_XNumberLiteral", None)
                setattr(value, "vql_XNumberLiteral", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_BoolValue(LiteralValueReference):

    def __init__(self, vql_BoolValue: "vql_XBooleanLiteral" = None):
        self.vql_BoolValue = vql_BoolValue
        
    @property
    def vql_BoolValue(self):
        return self.__vql_BoolValue

    @vql_BoolValue.setter
    def vql_BoolValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_BoolValue__vql_BoolValue", None)
        self.__vql_BoolValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_XBooleanLiteral"):
                opp_val = getattr(old_value, "vql_XBooleanLiteral", None)
                if opp_val == self:
                    setattr(old_value, "vql_XBooleanLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_XBooleanLiteral"):
                opp_val = getattr(value, "vql_XBooleanLiteral", None)
                setattr(value, "vql_XBooleanLiteral", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_StringValue(LiteralValueReference):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_JvmType:

    pass
class ComputationValue:

    pass
class vql_AggregatedValue(ComputationValue):

    def __init__(self, vql_AggregatedValue: "vql_JvmDeclaredType" = None, vql_AggregatedValue79: "vql_CallableRelation" = None, vql_AggregatedValue82: "vql_JvmType" = None):
        self.vql_AggregatedValue = vql_AggregatedValue
        self.vql_AggregatedValue79 = vql_AggregatedValue79
        self.vql_AggregatedValue82 = vql_AggregatedValue82
        
    @property
    def vql_AggregatedValue82(self):
        return self.__vql_AggregatedValue82

    @vql_AggregatedValue82.setter
    def vql_AggregatedValue82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_AggregatedValue__vql_AggregatedValue82", None)
        self.__vql_AggregatedValue82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_JvmType"):
                opp_val = getattr(old_value, "vql_JvmType", None)
                if opp_val == self:
                    setattr(old_value, "vql_JvmType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_JvmType"):
                opp_val = getattr(value, "vql_JvmType", None)
                setattr(value, "vql_JvmType", self)

    @property
    def vql_AggregatedValue79(self):
        return self.__vql_AggregatedValue79

    @vql_AggregatedValue79.setter
    def vql_AggregatedValue79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_AggregatedValue__vql_AggregatedValue79", None)
        self.__vql_AggregatedValue79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_CallableRelation80"):
                opp_val = getattr(old_value, "vql_CallableRelation80", None)
                if opp_val == self:
                    setattr(old_value, "vql_CallableRelation80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_CallableRelation80"):
                opp_val = getattr(value, "vql_CallableRelation80", None)
                setattr(value, "vql_CallableRelation80", self)

    @property
    def vql_AggregatedValue(self):
        return self.__vql_AggregatedValue

    @vql_AggregatedValue.setter
    def vql_AggregatedValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_AggregatedValue__vql_AggregatedValue", None)
        self.__vql_AggregatedValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_JvmDeclaredType77"):
                opp_val = getattr(old_value, "vql_JvmDeclaredType77", None)
                if opp_val == self:
                    setattr(old_value, "vql_JvmDeclaredType77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_JvmDeclaredType77"):
                opp_val = getattr(value, "vql_JvmDeclaredType77", None)
                setattr(value, "vql_JvmDeclaredType77", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_FunctionEvaluationValue(ComputationValue):

    def __init__(self, vql_FunctionEvaluationValue: "vql_XExpression" = None):
        self.vql_FunctionEvaluationValue = vql_FunctionEvaluationValue
        
    @property
    def vql_FunctionEvaluationValue(self):
        return self.__vql_FunctionEvaluationValue

    @vql_FunctionEvaluationValue.setter
    def vql_FunctionEvaluationValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_FunctionEvaluationValue__vql_FunctionEvaluationValue", None)
        self.__vql_FunctionEvaluationValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_XExpression75"):
                opp_val = getattr(old_value, "vql_XExpression75", None)
                if opp_val == self:
                    setattr(old_value, "vql_XExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_XExpression75"):
                opp_val = getattr(value, "vql_XExpression75", None)
                setattr(value, "vql_XExpression75", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_CallableRelation(ABC):

    def __init__(self, transitive: str, vql_CallableRelation: "vql_PatternCompositionConstraint" = None, vql_CallableRelation80: "vql_AggregatedValue" = None):
        self.transitive = transitive
        self.vql_CallableRelation = vql_CallableRelation
        self.vql_CallableRelation80 = vql_CallableRelation80
        
    @property
    def transitive(self) -> str:
        return self.__transitive

    @transitive.setter
    def transitive(self, transitive: str):
        self.__transitive = transitive

    @property
    def vql_CallableRelation(self):
        return self.__vql_CallableRelation

    @vql_CallableRelation.setter
    def vql_CallableRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_CallableRelation__vql_CallableRelation", None)
        self.__vql_CallableRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_PatternCompositionConstraint"):
                opp_val = getattr(old_value, "vql_PatternCompositionConstraint", None)
                if opp_val == self:
                    setattr(old_value, "vql_PatternCompositionConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_PatternCompositionConstraint"):
                opp_val = getattr(value, "vql_PatternCompositionConstraint", None)
                setattr(value, "vql_PatternCompositionConstraint", self)

    @property
    def vql_CallableRelation80(self):
        return self.__vql_CallableRelation80

    @vql_CallableRelation80.setter
    def vql_CallableRelation80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_CallableRelation__vql_CallableRelation80", None)
        self.__vql_CallableRelation80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_AggregatedValue79"):
                opp_val = getattr(old_value, "vql_AggregatedValue79", None)
                if opp_val == self:
                    setattr(old_value, "vql_AggregatedValue79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_AggregatedValue79"):
                opp_val = getattr(value, "vql_AggregatedValue79", None)
                setattr(value, "vql_AggregatedValue79", self)

class vql_JvmDeclaredType:

    pass
class vql_XExpression:

    pass
class CallableRelation:

    pass
class vql_UnaryTypeConstraint(CallableRelation):

    pass
class vql_PatternCall(CallableRelation):

    def __init__(self, vql_PatternCall: "vql_Pattern" = None, vql_PatternCall47: set["vql_ValueReference"] = None):
        self.vql_PatternCall = vql_PatternCall
        self.vql_PatternCall47 = vql_PatternCall47 if vql_PatternCall47 is not None else set()
        
    @property
    def vql_PatternCall(self):
        return self.__vql_PatternCall

    @vql_PatternCall.setter
    def vql_PatternCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PatternCall__vql_PatternCall", None)
        self.__vql_PatternCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_Pattern45"):
                opp_val = getattr(old_value, "vql_Pattern45", None)
                if opp_val == self:
                    setattr(old_value, "vql_Pattern45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_Pattern45"):
                opp_val = getattr(value, "vql_Pattern45", None)
                setattr(value, "vql_Pattern45", self)

    @property
    def vql_PatternCall47(self):
        return self.__vql_PatternCall47

    @vql_PatternCall47.setter
    def vql_PatternCall47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PatternCall__vql_PatternCall47", None)
        self.__vql_PatternCall47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vql_ValueReference48"):
                    opp_val = getattr(item, "vql_ValueReference48", None)
                    
                    if opp_val == self:
                        setattr(item, "vql_ValueReference48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vql_ValueReference48"):
                    opp_val = getattr(item, "vql_ValueReference48", None)
                    
                    setattr(item, "vql_ValueReference48", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_Constraint:

    pass
class Type:

    pass
class vql_RelationType(Type):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_EntityType(Type):

    pass
class Variable:

    pass
class vql_Parameter(Variable):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_LocalVariable(Variable):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_ParameterRef(Variable):

    def __init__(self, vql_ParameterRef: "vql_Variable" = None):
        self.vql_ParameterRef = vql_ParameterRef
        
    @property
    def vql_ParameterRef(self):
        return self.__vql_ParameterRef

    @vql_ParameterRef.setter
    def vql_ParameterRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_ParameterRef__vql_ParameterRef", None)
        self.__vql_ParameterRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_Variable50"):
                opp_val = getattr(old_value, "vql_Variable50", None)
                if opp_val == self:
                    setattr(old_value, "vql_Variable50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_Variable50"):
                opp_val = getattr(value, "vql_Variable50", None)
                setattr(value, "vql_Variable50", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_Type:

    def __init__(self, typename: str, vql_Type: "vql_Variable" = None):
        self.typename = typename
        self.vql_Type = vql_Type
        
    @property
    def typename(self) -> str:
        return self.__typename

    @typename.setter
    def typename(self, typename: str):
        self.__typename = typename

    @property
    def vql_Type(self):
        return self.__vql_Type

    @vql_Type.setter
    def vql_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Type__vql_Type", None)
        self.__vql_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_Variable36"):
                opp_val = getattr(old_value, "vql_Variable36", None)
                if opp_val == self:
                    setattr(old_value, "vql_Variable36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_Variable36"):
                opp_val = getattr(value, "vql_Variable36", None)
                setattr(value, "vql_Variable36", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class Expression:

    pass
class vql_Expression:

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_ValueReference(Expression):

    def __init__(self, vql_ValueReference: "vql_AnnotationParameter" = None, vql_ValueReference48: "vql_PatternCall" = None, vql_ValueReference54: "vql_CompareConstraint" = None, vql_ValueReference57: "vql_CompareConstraint" = None, vql_ValueReference73: "vql_ListValue" = None, vql_ValueReference69: "vql_PathExpressionConstraint" = None):
        self.vql_ValueReference = vql_ValueReference
        self.vql_ValueReference48 = vql_ValueReference48
        self.vql_ValueReference54 = vql_ValueReference54
        self.vql_ValueReference57 = vql_ValueReference57
        self.vql_ValueReference73 = vql_ValueReference73
        self.vql_ValueReference69 = vql_ValueReference69
        
    @property
    def vql_ValueReference(self):
        return self.__vql_ValueReference

    @vql_ValueReference.setter
    def vql_ValueReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_ValueReference__vql_ValueReference", None)
        self.__vql_ValueReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_AnnotationParameter34"):
                opp_val = getattr(old_value, "vql_AnnotationParameter34", None)
                if opp_val == self:
                    setattr(old_value, "vql_AnnotationParameter34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_AnnotationParameter34"):
                opp_val = getattr(value, "vql_AnnotationParameter34", None)
                setattr(value, "vql_AnnotationParameter34", self)

    @property
    def vql_ValueReference54(self):
        return self.__vql_ValueReference54

    @vql_ValueReference54.setter
    def vql_ValueReference54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_ValueReference__vql_ValueReference54", None)
        self.__vql_ValueReference54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_CompareConstraint"):
                opp_val = getattr(old_value, "vql_CompareConstraint", None)
                if opp_val == self:
                    setattr(old_value, "vql_CompareConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_CompareConstraint"):
                opp_val = getattr(value, "vql_CompareConstraint", None)
                setattr(value, "vql_CompareConstraint", self)

    @property
    def vql_ValueReference69(self):
        return self.__vql_ValueReference69

    @vql_ValueReference69.setter
    def vql_ValueReference69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_ValueReference__vql_ValueReference69", None)
        self.__vql_ValueReference69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_PathExpressionConstraint68"):
                opp_val = getattr(old_value, "vql_PathExpressionConstraint68", None)
                if opp_val == self:
                    setattr(old_value, "vql_PathExpressionConstraint68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_PathExpressionConstraint68"):
                opp_val = getattr(value, "vql_PathExpressionConstraint68", None)
                setattr(value, "vql_PathExpressionConstraint68", self)

    @property
    def vql_ValueReference57(self):
        return self.__vql_ValueReference57

    @vql_ValueReference57.setter
    def vql_ValueReference57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_ValueReference__vql_ValueReference57", None)
        self.__vql_ValueReference57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_CompareConstraint56"):
                opp_val = getattr(old_value, "vql_CompareConstraint56", None)
                if opp_val == self:
                    setattr(old_value, "vql_CompareConstraint56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_CompareConstraint56"):
                opp_val = getattr(value, "vql_CompareConstraint56", None)
                setattr(value, "vql_CompareConstraint56", self)

    @property
    def vql_ValueReference48(self):
        return self.__vql_ValueReference48

    @vql_ValueReference48.setter
    def vql_ValueReference48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_ValueReference__vql_ValueReference48", None)
        self.__vql_ValueReference48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_PatternCall47"):
                opp_val = getattr(old_value, "vql_PatternCall47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_PatternCall47"):
                opp_val = getattr(value, "vql_PatternCall47", None)
                if opp_val is None:
                    setattr(value, "vql_PatternCall47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vql_ValueReference73(self):
        return self.__vql_ValueReference73

    @vql_ValueReference73.setter
    def vql_ValueReference73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_ValueReference__vql_ValueReference73", None)
        self.__vql_ValueReference73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_ListValue"):
                opp_val = getattr(old_value, "vql_ListValue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_ListValue"):
                opp_val = getattr(value, "vql_ListValue", None)
                if opp_val is None:
                    setattr(value, "vql_ListValue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_AnnotationParameter:

    def __init__(self, name: str, vql_AnnotationParameter: "vql_Annotation" = None, vql_AnnotationParameter34: "vql_ValueReference" = None):
        self.name = name
        self.vql_AnnotationParameter = vql_AnnotationParameter
        self.vql_AnnotationParameter34 = vql_AnnotationParameter34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vql_AnnotationParameter(self):
        return self.__vql_AnnotationParameter

    @vql_AnnotationParameter.setter
    def vql_AnnotationParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_AnnotationParameter__vql_AnnotationParameter", None)
        self.__vql_AnnotationParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_Annotation32"):
                opp_val = getattr(old_value, "vql_Annotation32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_Annotation32"):
                opp_val = getattr(value, "vql_Annotation32", None)
                if opp_val is None:
                    setattr(value, "vql_Annotation32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vql_AnnotationParameter34(self):
        return self.__vql_AnnotationParameter34

    @vql_AnnotationParameter34.setter
    def vql_AnnotationParameter34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_AnnotationParameter__vql_AnnotationParameter34", None)
        self.__vql_AnnotationParameter34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_ValueReference"):
                opp_val = getattr(old_value, "vql_ValueReference", None)
                if opp_val == self:
                    setattr(old_value, "vql_ValueReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_ValueReference"):
                opp_val = getattr(value, "vql_ValueReference", None)
                setattr(value, "vql_ValueReference", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_PatternBody:

    def __init__(self, name: str, vql_PatternBody: "vql_Pattern" = None, vql_PatternBody40: set["vql_Constraint"] = None, vql_PatternBody42: set["vql_Variable"] = None):
        self.name = name
        self.vql_PatternBody = vql_PatternBody
        self.vql_PatternBody40 = vql_PatternBody40 if vql_PatternBody40 is not None else set()
        self.vql_PatternBody42 = vql_PatternBody42 if vql_PatternBody42 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vql_PatternBody42(self):
        return self.__vql_PatternBody42

    @vql_PatternBody42.setter
    def vql_PatternBody42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PatternBody__vql_PatternBody42", None)
        self.__vql_PatternBody42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vql_Variable43"):
                    opp_val = getattr(item, "vql_Variable43", None)
                    
                    if opp_val == self:
                        setattr(item, "vql_Variable43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vql_Variable43"):
                    opp_val = getattr(item, "vql_Variable43", None)
                    
                    setattr(item, "vql_Variable43", self)
                    

    @property
    def vql_PatternBody40(self):
        return self.__vql_PatternBody40

    @vql_PatternBody40.setter
    def vql_PatternBody40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PatternBody__vql_PatternBody40", None)
        self.__vql_PatternBody40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vql_Constraint"):
                    opp_val = getattr(item, "vql_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "vql_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vql_Constraint"):
                    opp_val = getattr(item, "vql_Constraint", None)
                    
                    setattr(item, "vql_Constraint", self)
                    

    @property
    def vql_PatternBody(self):
        return self.__vql_PatternBody

    @vql_PatternBody.setter
    def vql_PatternBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PatternBody__vql_PatternBody", None)
        self.__vql_PatternBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_Pattern30"):
                opp_val = getattr(old_value, "vql_Pattern30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_Pattern30"):
                opp_val = getattr(value, "vql_Pattern30", None)
                if opp_val is None:
                    setattr(value, "vql_Pattern30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_EStructuralFeature:

    pass
class RelationType:

    pass
class vql_ReferenceType(RelationType):

    def __init__(self, vql_ReferenceType: "vql_EStructuralFeature" = None, vql_ReferenceType60: "vql_PathExpressionConstraint" = None):
        self.vql_ReferenceType = vql_ReferenceType
        self.vql_ReferenceType60 = vql_ReferenceType60
        
    @property
    def vql_ReferenceType(self):
        return self.__vql_ReferenceType

    @vql_ReferenceType.setter
    def vql_ReferenceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_ReferenceType__vql_ReferenceType", None)
        self.__vql_ReferenceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_EStructuralFeature"):
                opp_val = getattr(old_value, "vql_EStructuralFeature", None)
                if opp_val == self:
                    setattr(old_value, "vql_EStructuralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_EStructuralFeature"):
                opp_val = getattr(value, "vql_EStructuralFeature", None)
                setattr(value, "vql_EStructuralFeature", self)

    @property
    def vql_ReferenceType60(self):
        return self.__vql_ReferenceType60

    @vql_ReferenceType60.setter
    def vql_ReferenceType60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_ReferenceType__vql_ReferenceType60", None)
        self.__vql_ReferenceType60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_PathExpressionConstraint"):
                opp_val = getattr(old_value, "vql_PathExpressionConstraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_PathExpressionConstraint"):
                opp_val = getattr(value, "vql_PathExpressionConstraint", None)
                if opp_val is None:
                    setattr(value, "vql_PathExpressionConstraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_EClassifier:

    pass
class EntityType:

    pass
class vql_JavaType(EntityType):

    def __init__(self, vql_JavaType: "vql_JvmDeclaredType" = None):
        self.vql_JavaType = vql_JavaType
        
    @property
    def vql_JavaType(self):
        return self.__vql_JavaType

    @vql_JavaType.setter
    def vql_JavaType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_JavaType__vql_JavaType", None)
        self.__vql_JavaType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_JvmDeclaredType"):
                opp_val = getattr(old_value, "vql_JvmDeclaredType", None)
                if opp_val == self:
                    setattr(old_value, "vql_JvmDeclaredType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_JvmDeclaredType"):
                opp_val = getattr(value, "vql_JvmDeclaredType", None)
                setattr(value, "vql_JvmDeclaredType", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_ClassType(EntityType):

    def __init__(self, vql_ClassType: "vql_PackageImport" = None, vql_ClassType21: "vql_EClassifier" = None, vql_ClassType63: "vql_PathExpressionConstraint" = None):
        self.vql_ClassType = vql_ClassType
        self.vql_ClassType21 = vql_ClassType21
        self.vql_ClassType63 = vql_ClassType63
        
    @property
    def vql_ClassType21(self):
        return self.__vql_ClassType21

    @vql_ClassType21.setter
    def vql_ClassType21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_ClassType__vql_ClassType21", None)
        self.__vql_ClassType21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_EClassifier"):
                opp_val = getattr(old_value, "vql_EClassifier", None)
                if opp_val == self:
                    setattr(old_value, "vql_EClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_EClassifier"):
                opp_val = getattr(value, "vql_EClassifier", None)
                setattr(value, "vql_EClassifier", self)

    @property
    def vql_ClassType(self):
        return self.__vql_ClassType

    @vql_ClassType.setter
    def vql_ClassType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_ClassType__vql_ClassType", None)
        self.__vql_ClassType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_PackageImport19"):
                opp_val = getattr(old_value, "vql_PackageImport19", None)
                if opp_val == self:
                    setattr(old_value, "vql_PackageImport19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_PackageImport19"):
                opp_val = getattr(value, "vql_PackageImport19", None)
                setattr(value, "vql_PackageImport19", self)

    @property
    def vql_ClassType63(self):
        return self.__vql_ClassType63

    @vql_ClassType63.setter
    def vql_ClassType63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_ClassType__vql_ClassType63", None)
        self.__vql_ClassType63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_PathExpressionConstraint62"):
                opp_val = getattr(old_value, "vql_PathExpressionConstraint62", None)
                if opp_val == self:
                    setattr(old_value, "vql_PathExpressionConstraint62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_PathExpressionConstraint62"):
                opp_val = getattr(value, "vql_PathExpressionConstraint62", None)
                setattr(value, "vql_PathExpressionConstraint62", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_PatternModel:

    def __init__(self, packageName: str, vql_PatternModel: "vql_VQLImportSection" = None, vql_PatternModel16: set["vql_Pattern"] = None):
        self.packageName = packageName
        self.vql_PatternModel = vql_PatternModel
        self.vql_PatternModel16 = vql_PatternModel16 if vql_PatternModel16 is not None else set()
        
    @property
    def packageName(self) -> str:
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName

    @property
    def vql_PatternModel(self):
        return self.__vql_PatternModel

    @vql_PatternModel.setter
    def vql_PatternModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PatternModel__vql_PatternModel", None)
        self.__vql_PatternModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_VQLImportSection14"):
                opp_val = getattr(old_value, "vql_VQLImportSection14", None)
                if opp_val == self:
                    setattr(old_value, "vql_VQLImportSection14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_VQLImportSection14"):
                opp_val = getattr(value, "vql_VQLImportSection14", None)
                setattr(value, "vql_VQLImportSection14", self)

    @property
    def vql_PatternModel16(self):
        return self.__vql_PatternModel16

    @vql_PatternModel16.setter
    def vql_PatternModel16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PatternModel__vql_PatternModel16", None)
        self.__vql_PatternModel16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vql_Pattern17"):
                    opp_val = getattr(item, "vql_Pattern17", None)
                    
                    if opp_val == self:
                        setattr(item, "vql_Pattern17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vql_Pattern17"):
                    opp_val = getattr(item, "vql_Pattern17", None)
                    
                    setattr(item, "vql_Pattern17", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_EEnumLiteral:

    pass
class vql_EEnum:

    pass
class ValueReference:

    pass
class vql_ComputationValue(ValueReference):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_VariableReference(ValueReference):

    def __init__(self, aggregator: bool, var: str, vql_VariableReference: "vql_Variable" = None, vql_VariableReference66: "vql_PathExpressionConstraint" = None, vql_VariableReference86: "vql_UnaryTypeConstraint" = None):
        self.aggregator = aggregator
        self.var = var
        self.vql_VariableReference = vql_VariableReference
        self.vql_VariableReference66 = vql_VariableReference66
        self.vql_VariableReference86 = vql_VariableReference86
        
    @property
    def aggregator(self) -> bool:
        return self.__aggregator

    @aggregator.setter
    def aggregator(self, aggregator: bool):
        self.__aggregator = aggregator

    @property
    def var(self) -> str:
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var

    @property
    def vql_VariableReference66(self):
        return self.__vql_VariableReference66

    @vql_VariableReference66.setter
    def vql_VariableReference66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_VariableReference__vql_VariableReference66", None)
        self.__vql_VariableReference66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_PathExpressionConstraint65"):
                opp_val = getattr(old_value, "vql_PathExpressionConstraint65", None)
                if opp_val == self:
                    setattr(old_value, "vql_PathExpressionConstraint65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_PathExpressionConstraint65"):
                opp_val = getattr(value, "vql_PathExpressionConstraint65", None)
                setattr(value, "vql_PathExpressionConstraint65", self)

    @property
    def vql_VariableReference(self):
        return self.__vql_VariableReference

    @vql_VariableReference.setter
    def vql_VariableReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_VariableReference__vql_VariableReference", None)
        self.__vql_VariableReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_Variable38"):
                opp_val = getattr(old_value, "vql_Variable38", None)
                if opp_val == self:
                    setattr(old_value, "vql_Variable38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_Variable38"):
                opp_val = getattr(value, "vql_Variable38", None)
                setattr(value, "vql_Variable38", self)

    @property
    def vql_VariableReference86(self):
        return self.__vql_VariableReference86

    @vql_VariableReference86.setter
    def vql_VariableReference86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_VariableReference__vql_VariableReference86", None)
        self.__vql_VariableReference86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_UnaryTypeConstraint85"):
                opp_val = getattr(old_value, "vql_UnaryTypeConstraint85", None)
                if opp_val == self:
                    setattr(old_value, "vql_UnaryTypeConstraint85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_UnaryTypeConstraint85"):
                opp_val = getattr(value, "vql_UnaryTypeConstraint85", None)
                setattr(value, "vql_UnaryTypeConstraint85", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_LiteralValueReference(ValueReference):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_EnumValue(ValueReference):

    def __init__(self, vql_EnumValue: "vql_EEnum" = None, vql_EnumValue12: "vql_EEnumLiteral" = None):
        self.vql_EnumValue = vql_EnumValue
        self.vql_EnumValue12 = vql_EnumValue12
        
    @property
    def vql_EnumValue(self):
        return self.__vql_EnumValue

    @vql_EnumValue.setter
    def vql_EnumValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_EnumValue__vql_EnumValue", None)
        self.__vql_EnumValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_EEnum"):
                opp_val = getattr(old_value, "vql_EEnum", None)
                if opp_val == self:
                    setattr(old_value, "vql_EEnum", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_EEnum"):
                opp_val = getattr(value, "vql_EEnum", None)
                setattr(value, "vql_EEnum", self)

    @property
    def vql_EnumValue12(self):
        return self.__vql_EnumValue12

    @vql_EnumValue12.setter
    def vql_EnumValue12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_EnumValue__vql_EnumValue12", None)
        self.__vql_EnumValue12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_EEnumLiteral"):
                opp_val = getattr(old_value, "vql_EEnumLiteral", None)
                if opp_val == self:
                    setattr(old_value, "vql_EEnumLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_EEnumLiteral"):
                opp_val = getattr(value, "vql_EEnumLiteral", None)
                setattr(value, "vql_EEnumLiteral", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class UnaryTypeConstraint:

    pass
class Constraint:

    pass
class vql_PatternCompositionConstraint(Constraint):

    def __init__(self, negative: bool, vql_PatternCompositionConstraint: "vql_CallableRelation" = None):
        self.negative = negative
        self.vql_PatternCompositionConstraint = vql_PatternCompositionConstraint
        
    @property
    def negative(self) -> bool:
        return self.__negative

    @negative.setter
    def negative(self, negative: bool):
        self.__negative = negative

    @property
    def vql_PatternCompositionConstraint(self):
        return self.__vql_PatternCompositionConstraint

    @vql_PatternCompositionConstraint.setter
    def vql_PatternCompositionConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PatternCompositionConstraint__vql_PatternCompositionConstraint", None)
        self.__vql_PatternCompositionConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_CallableRelation"):
                opp_val = getattr(old_value, "vql_CallableRelation", None)
                if opp_val == self:
                    setattr(old_value, "vql_CallableRelation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_CallableRelation"):
                opp_val = getattr(value, "vql_CallableRelation", None)
                setattr(value, "vql_CallableRelation", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_TypeCheckConstraint(Constraint, UnaryTypeConstraint):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_CheckConstraint(Constraint):

    def __init__(self, vql_CheckConstraint: "vql_XExpression" = None):
        self.vql_CheckConstraint = vql_CheckConstraint
        
    @property
    def vql_CheckConstraint(self):
        return self.__vql_CheckConstraint

    @vql_CheckConstraint.setter
    def vql_CheckConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_CheckConstraint__vql_CheckConstraint", None)
        self.__vql_CheckConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_XExpression"):
                opp_val = getattr(old_value, "vql_XExpression", None)
                if opp_val == self:
                    setattr(old_value, "vql_XExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_XExpression"):
                opp_val = getattr(value, "vql_XExpression", None)
                setattr(value, "vql_XExpression", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_CompareConstraint(Constraint):

    def __init__(self, feature: str, vql_CompareConstraint: "vql_ValueReference" = None, vql_CompareConstraint56: "vql_ValueReference" = None):
        self.feature = feature
        self.vql_CompareConstraint = vql_CompareConstraint
        self.vql_CompareConstraint56 = vql_CompareConstraint56
        
    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

    @property
    def vql_CompareConstraint56(self):
        return self.__vql_CompareConstraint56

    @vql_CompareConstraint56.setter
    def vql_CompareConstraint56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_CompareConstraint__vql_CompareConstraint56", None)
        self.__vql_CompareConstraint56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_ValueReference57"):
                opp_val = getattr(old_value, "vql_ValueReference57", None)
                if opp_val == self:
                    setattr(old_value, "vql_ValueReference57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_ValueReference57"):
                opp_val = getattr(value, "vql_ValueReference57", None)
                setattr(value, "vql_ValueReference57", self)

    @property
    def vql_CompareConstraint(self):
        return self.__vql_CompareConstraint

    @vql_CompareConstraint.setter
    def vql_CompareConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_CompareConstraint__vql_CompareConstraint", None)
        self.__vql_CompareConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_ValueReference54"):
                opp_val = getattr(old_value, "vql_ValueReference54", None)
                if opp_val == self:
                    setattr(old_value, "vql_ValueReference54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_ValueReference54"):
                opp_val = getattr(value, "vql_ValueReference54", None)
                setattr(value, "vql_ValueReference54", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_PathExpressionConstraint(Constraint, CallableRelation):

    def __init__(self, vql_PathExpressionConstraint: set["vql_ReferenceType"] = None, vql_PathExpressionConstraint62: "vql_ClassType" = None, vql_PathExpressionConstraint65: "vql_VariableReference" = None, vql_PathExpressionConstraint68: "vql_ValueReference" = None):
        self.vql_PathExpressionConstraint = vql_PathExpressionConstraint if vql_PathExpressionConstraint is not None else set()
        self.vql_PathExpressionConstraint62 = vql_PathExpressionConstraint62
        self.vql_PathExpressionConstraint65 = vql_PathExpressionConstraint65
        self.vql_PathExpressionConstraint68 = vql_PathExpressionConstraint68
        
    @property
    def vql_PathExpressionConstraint62(self):
        return self.__vql_PathExpressionConstraint62

    @vql_PathExpressionConstraint62.setter
    def vql_PathExpressionConstraint62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PathExpressionConstraint__vql_PathExpressionConstraint62", None)
        self.__vql_PathExpressionConstraint62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_ClassType63"):
                opp_val = getattr(old_value, "vql_ClassType63", None)
                if opp_val == self:
                    setattr(old_value, "vql_ClassType63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_ClassType63"):
                opp_val = getattr(value, "vql_ClassType63", None)
                setattr(value, "vql_ClassType63", self)

    @property
    def vql_PathExpressionConstraint(self):
        return self.__vql_PathExpressionConstraint

    @vql_PathExpressionConstraint.setter
    def vql_PathExpressionConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PathExpressionConstraint__vql_PathExpressionConstraint", None)
        self.__vql_PathExpressionConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vql_ReferenceType60"):
                    opp_val = getattr(item, "vql_ReferenceType60", None)
                    
                    if opp_val == self:
                        setattr(item, "vql_ReferenceType60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vql_ReferenceType60"):
                    opp_val = getattr(item, "vql_ReferenceType60", None)
                    
                    setattr(item, "vql_ReferenceType60", self)
                    

    @property
    def vql_PathExpressionConstraint65(self):
        return self.__vql_PathExpressionConstraint65

    @vql_PathExpressionConstraint65.setter
    def vql_PathExpressionConstraint65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PathExpressionConstraint__vql_PathExpressionConstraint65", None)
        self.__vql_PathExpressionConstraint65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_VariableReference66"):
                opp_val = getattr(old_value, "vql_VariableReference66", None)
                if opp_val == self:
                    setattr(old_value, "vql_VariableReference66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_VariableReference66"):
                opp_val = getattr(value, "vql_VariableReference66", None)
                setattr(value, "vql_VariableReference66", self)

    @property
    def vql_PathExpressionConstraint68(self):
        return self.__vql_PathExpressionConstraint68

    @vql_PathExpressionConstraint68.setter
    def vql_PathExpressionConstraint68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PathExpressionConstraint__vql_PathExpressionConstraint68", None)
        self.__vql_PathExpressionConstraint68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_ValueReference69"):
                opp_val = getattr(old_value, "vql_ValueReference69", None)
                if opp_val == self:
                    setattr(old_value, "vql_ValueReference69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_ValueReference69"):
                opp_val = getattr(value, "vql_ValueReference69", None)
                setattr(value, "vql_ValueReference69", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_EClassifierConstraint(Constraint, UnaryTypeConstraint):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_Variable(Expression):

    def __init__(self, name: str, vql_Variable: "vql_Pattern" = None, vql_Variable38: "vql_VariableReference" = None, vql_Variable36: "vql_Type" = None, vql_Variable50: "vql_ParameterRef" = None, vql_Variable43: "vql_PatternBody" = None):
        self.name = name
        self.vql_Variable = vql_Variable
        self.vql_Variable38 = vql_Variable38
        self.vql_Variable36 = vql_Variable36
        self.vql_Variable50 = vql_Variable50
        self.vql_Variable43 = vql_Variable43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vql_Variable(self):
        return self.__vql_Variable

    @vql_Variable.setter
    def vql_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Variable__vql_Variable", None)
        self.__vql_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_Pattern28"):
                opp_val = getattr(old_value, "vql_Pattern28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_Pattern28"):
                opp_val = getattr(value, "vql_Pattern28", None)
                if opp_val is None:
                    setattr(value, "vql_Pattern28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vql_Variable36(self):
        return self.__vql_Variable36

    @vql_Variable36.setter
    def vql_Variable36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Variable__vql_Variable36", None)
        self.__vql_Variable36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_Type"):
                opp_val = getattr(old_value, "vql_Type", None)
                if opp_val == self:
                    setattr(old_value, "vql_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_Type"):
                opp_val = getattr(value, "vql_Type", None)
                setattr(value, "vql_Type", self)

    @property
    def vql_Variable43(self):
        return self.__vql_Variable43

    @vql_Variable43.setter
    def vql_Variable43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Variable__vql_Variable43", None)
        self.__vql_Variable43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_PatternBody42"):
                opp_val = getattr(old_value, "vql_PatternBody42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_PatternBody42"):
                opp_val = getattr(value, "vql_PatternBody42", None)
                if opp_val is None:
                    setattr(value, "vql_PatternBody42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vql_Variable50(self):
        return self.__vql_Variable50

    @vql_Variable50.setter
    def vql_Variable50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Variable__vql_Variable50", None)
        self.__vql_Variable50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_ParameterRef"):
                opp_val = getattr(old_value, "vql_ParameterRef", None)
                if opp_val == self:
                    setattr(old_value, "vql_ParameterRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_ParameterRef"):
                opp_val = getattr(value, "vql_ParameterRef", None)
                setattr(value, "vql_ParameterRef", self)

    @property
    def vql_Variable38(self):
        return self.__vql_Variable38

    @vql_Variable38.setter
    def vql_Variable38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Variable__vql_Variable38", None)
        self.__vql_Variable38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_VariableReference"):
                opp_val = getattr(old_value, "vql_VariableReference", None)
                if opp_val == self:
                    setattr(old_value, "vql_VariableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_VariableReference"):
                opp_val = getattr(value, "vql_VariableReference", None)
                setattr(value, "vql_VariableReference", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_Modifiers:

    def __init__(self, private: bool, execution: str, vql_Modifiers: "vql_Pattern" = None):
        self.private = private
        self.execution = execution
        self.vql_Modifiers = vql_Modifiers
        
    @property
    def private(self) -> bool:
        return self.__private

    @private.setter
    def private(self, private: bool):
        self.__private = private

    @property
    def execution(self) -> str:
        return self.__execution

    @execution.setter
    def execution(self, execution: str):
        self.__execution = execution

    @property
    def vql_Modifiers(self):
        return self.__vql_Modifiers

    @vql_Modifiers.setter
    def vql_Modifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Modifiers__vql_Modifiers", None)
        self.__vql_Modifiers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_Pattern26"):
                opp_val = getattr(old_value, "vql_Pattern26", None)
                if opp_val == self:
                    setattr(old_value, "vql_Pattern26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_Pattern26"):
                opp_val = getattr(value, "vql_Pattern26", None)
                setattr(value, "vql_Pattern26", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_Annotation:

    def __init__(self, name: str, vql_Annotation: "vql_Pattern" = None, vql_Annotation32: set["vql_AnnotationParameter"] = None):
        self.name = name
        self.vql_Annotation = vql_Annotation
        self.vql_Annotation32 = vql_Annotation32 if vql_Annotation32 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vql_Annotation(self):
        return self.__vql_Annotation

    @vql_Annotation.setter
    def vql_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Annotation__vql_Annotation", None)
        self.__vql_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_Pattern24"):
                opp_val = getattr(old_value, "vql_Pattern24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_Pattern24"):
                opp_val = getattr(value, "vql_Pattern24", None)
                if opp_val is None:
                    setattr(value, "vql_Pattern24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vql_Annotation32(self):
        return self.__vql_Annotation32

    @vql_Annotation32.setter
    def vql_Annotation32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Annotation__vql_Annotation32", None)
        self.__vql_Annotation32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vql_AnnotationParameter"):
                    opp_val = getattr(item, "vql_AnnotationParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "vql_AnnotationParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vql_AnnotationParameter"):
                    opp_val = getattr(item, "vql_AnnotationParameter", None)
                    
                    setattr(item, "vql_AnnotationParameter", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_PackageImport:

    def __init__(self, alias: str, vql_PackageImport4: "vql_EPackage" = None, vql_PackageImport: "vql_VQLImportSection" = None, vql_PackageImport19: "vql_ClassType" = None):
        self.alias = alias
        self.vql_PackageImport4 = vql_PackageImport4
        self.vql_PackageImport = vql_PackageImport
        self.vql_PackageImport19 = vql_PackageImport19
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def vql_PackageImport19(self):
        return self.__vql_PackageImport19

    @vql_PackageImport19.setter
    def vql_PackageImport19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PackageImport__vql_PackageImport19", None)
        self.__vql_PackageImport19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_ClassType"):
                opp_val = getattr(old_value, "vql_ClassType", None)
                if opp_val == self:
                    setattr(old_value, "vql_ClassType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_ClassType"):
                opp_val = getattr(value, "vql_ClassType", None)
                setattr(value, "vql_ClassType", self)

    @property
    def vql_PackageImport4(self):
        return self.__vql_PackageImport4

    @vql_PackageImport4.setter
    def vql_PackageImport4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PackageImport__vql_PackageImport4", None)
        self.__vql_PackageImport4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_EPackage"):
                opp_val = getattr(old_value, "vql_EPackage", None)
                if opp_val == self:
                    setattr(old_value, "vql_EPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_EPackage"):
                opp_val = getattr(value, "vql_EPackage", None)
                setattr(value, "vql_EPackage", self)

    @property
    def vql_PackageImport(self):
        return self.__vql_PackageImport

    @vql_PackageImport.setter
    def vql_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PackageImport__vql_PackageImport", None)
        self.__vql_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_VQLImportSection"):
                opp_val = getattr(old_value, "vql_VQLImportSection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_VQLImportSection"):
                opp_val = getattr(value, "vql_VQLImportSection", None)
                if opp_val is None:
                    setattr(value, "vql_VQLImportSection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class XImportSection:

    pass
class vql_VQLImportSection(XImportSection):

    def __init__(self, vql_VQLImportSection2: set["vql_PatternImport"] = None, vql_VQLImportSection: set["vql_PackageImport"] = None, vql_VQLImportSection14: "vql_PatternModel" = None):
        self.vql_VQLImportSection2 = vql_VQLImportSection2 if vql_VQLImportSection2 is not None else set()
        self.vql_VQLImportSection = vql_VQLImportSection if vql_VQLImportSection is not None else set()
        self.vql_VQLImportSection14 = vql_VQLImportSection14
        
    @property
    def vql_VQLImportSection(self):
        return self.__vql_VQLImportSection

    @vql_VQLImportSection.setter
    def vql_VQLImportSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_VQLImportSection__vql_VQLImportSection", None)
        self.__vql_VQLImportSection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vql_PackageImport"):
                    opp_val = getattr(item, "vql_PackageImport", None)
                    
                    if opp_val == self:
                        setattr(item, "vql_PackageImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vql_PackageImport"):
                    opp_val = getattr(item, "vql_PackageImport", None)
                    
                    setattr(item, "vql_PackageImport", self)
                    

    @property
    def vql_VQLImportSection14(self):
        return self.__vql_VQLImportSection14

    @vql_VQLImportSection14.setter
    def vql_VQLImportSection14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_VQLImportSection__vql_VQLImportSection14", None)
        self.__vql_VQLImportSection14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_PatternModel"):
                opp_val = getattr(old_value, "vql_PatternModel", None)
                if opp_val == self:
                    setattr(old_value, "vql_PatternModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_PatternModel"):
                opp_val = getattr(value, "vql_PatternModel", None)
                setattr(value, "vql_PatternModel", self)

    @property
    def vql_VQLImportSection2(self):
        return self.__vql_VQLImportSection2

    @vql_VQLImportSection2.setter
    def vql_VQLImportSection2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_VQLImportSection__vql_VQLImportSection2", None)
        self.__vql_VQLImportSection2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vql_PatternImport"):
                    opp_val = getattr(item, "vql_PatternImport", None)
                    
                    if opp_val == self:
                        setattr(item, "vql_PatternImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vql_PatternImport"):
                    opp_val = getattr(item, "vql_PatternImport", None)
                    
                    setattr(item, "vql_PatternImport", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_Pattern:

    def __init__(self, name: str, vql_Pattern: "vql_PatternImport" = None, vql_Pattern24: set["vql_Annotation"] = None, vql_Pattern26: "vql_Modifiers" = None, vql_Pattern28: set["vql_Variable"] = None, vql_Pattern9: "vql_PatternImport" = None, vql_Pattern17: "vql_PatternModel" = None, vql_Pattern30: set["vql_PatternBody"] = None, vql_Pattern45: "vql_PatternCall" = None):
        self.name = name
        self.vql_Pattern = vql_Pattern
        self.vql_Pattern24 = vql_Pattern24 if vql_Pattern24 is not None else set()
        self.vql_Pattern26 = vql_Pattern26
        self.vql_Pattern28 = vql_Pattern28 if vql_Pattern28 is not None else set()
        self.vql_Pattern9 = vql_Pattern9
        self.vql_Pattern17 = vql_Pattern17
        self.vql_Pattern30 = vql_Pattern30 if vql_Pattern30 is not None else set()
        self.vql_Pattern45 = vql_Pattern45
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vql_Pattern28(self):
        return self.__vql_Pattern28

    @vql_Pattern28.setter
    def vql_Pattern28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Pattern__vql_Pattern28", None)
        self.__vql_Pattern28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vql_Variable"):
                    opp_val = getattr(item, "vql_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "vql_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vql_Variable"):
                    opp_val = getattr(item, "vql_Variable", None)
                    
                    setattr(item, "vql_Variable", self)
                    

    @property
    def vql_Pattern(self):
        return self.__vql_Pattern

    @vql_Pattern.setter
    def vql_Pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Pattern__vql_Pattern", None)
        self.__vql_Pattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_PatternImport6"):
                opp_val = getattr(old_value, "vql_PatternImport6", None)
                if opp_val == self:
                    setattr(old_value, "vql_PatternImport6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_PatternImport6"):
                opp_val = getattr(value, "vql_PatternImport6", None)
                setattr(value, "vql_PatternImport6", self)

    @property
    def vql_Pattern26(self):
        return self.__vql_Pattern26

    @vql_Pattern26.setter
    def vql_Pattern26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Pattern__vql_Pattern26", None)
        self.__vql_Pattern26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_Modifiers"):
                opp_val = getattr(old_value, "vql_Modifiers", None)
                if opp_val == self:
                    setattr(old_value, "vql_Modifiers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_Modifiers"):
                opp_val = getattr(value, "vql_Modifiers", None)
                setattr(value, "vql_Modifiers", self)

    @property
    def vql_Pattern17(self):
        return self.__vql_Pattern17

    @vql_Pattern17.setter
    def vql_Pattern17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Pattern__vql_Pattern17", None)
        self.__vql_Pattern17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_PatternModel16"):
                opp_val = getattr(old_value, "vql_PatternModel16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_PatternModel16"):
                opp_val = getattr(value, "vql_PatternModel16", None)
                if opp_val is None:
                    setattr(value, "vql_PatternModel16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vql_Pattern9(self):
        return self.__vql_Pattern9

    @vql_Pattern9.setter
    def vql_Pattern9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Pattern__vql_Pattern9", None)
        self.__vql_Pattern9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_PatternImport8"):
                opp_val = getattr(old_value, "vql_PatternImport8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_PatternImport8"):
                opp_val = getattr(value, "vql_PatternImport8", None)
                if opp_val is None:
                    setattr(value, "vql_PatternImport8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vql_Pattern30(self):
        return self.__vql_Pattern30

    @vql_Pattern30.setter
    def vql_Pattern30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Pattern__vql_Pattern30", None)
        self.__vql_Pattern30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vql_PatternBody"):
                    opp_val = getattr(item, "vql_PatternBody", None)
                    
                    if opp_val == self:
                        setattr(item, "vql_PatternBody", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vql_PatternBody"):
                    opp_val = getattr(item, "vql_PatternBody", None)
                    
                    setattr(item, "vql_PatternBody", self)
                    

    @property
    def vql_Pattern24(self):
        return self.__vql_Pattern24

    @vql_Pattern24.setter
    def vql_Pattern24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Pattern__vql_Pattern24", None)
        self.__vql_Pattern24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vql_Annotation"):
                    opp_val = getattr(item, "vql_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "vql_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vql_Annotation"):
                    opp_val = getattr(item, "vql_Annotation", None)
                    
                    setattr(item, "vql_Annotation", self)
                    

    @property
    def vql_Pattern45(self):
        return self.__vql_Pattern45

    @vql_Pattern45.setter
    def vql_Pattern45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_Pattern__vql_Pattern45", None)
        self.__vql_Pattern45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_PatternCall"):
                opp_val = getattr(old_value, "vql_PatternCall", None)
                if opp_val == self:
                    setattr(old_value, "vql_PatternCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_PatternCall"):
                opp_val = getattr(value, "vql_PatternCall", None)
                setattr(value, "vql_PatternCall", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class vql_EPackage:

    pass
class vql_PatternImport:

    def __init__(self, packageName: str, vql_PatternImport: "vql_VQLImportSection" = None, vql_PatternImport6: "vql_Pattern" = None, vql_PatternImport8: set["vql_Pattern"] = None):
        self.packageName = packageName
        self.vql_PatternImport = vql_PatternImport
        self.vql_PatternImport6 = vql_PatternImport6
        self.vql_PatternImport8 = vql_PatternImport8 if vql_PatternImport8 is not None else set()
        
    @property
    def packageName(self) -> str:
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName

    @property
    def vql_PatternImport6(self):
        return self.__vql_PatternImport6

    @vql_PatternImport6.setter
    def vql_PatternImport6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PatternImport__vql_PatternImport6", None)
        self.__vql_PatternImport6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_Pattern"):
                opp_val = getattr(old_value, "vql_Pattern", None)
                if opp_val == self:
                    setattr(old_value, "vql_Pattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_Pattern"):
                opp_val = getattr(value, "vql_Pattern", None)
                setattr(value, "vql_Pattern", self)

    @property
    def vql_PatternImport8(self):
        return self.__vql_PatternImport8

    @vql_PatternImport8.setter
    def vql_PatternImport8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PatternImport__vql_PatternImport8", None)
        self.__vql_PatternImport8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vql_Pattern9"):
                    opp_val = getattr(item, "vql_Pattern9", None)
                    
                    if opp_val == self:
                        setattr(item, "vql_Pattern9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vql_Pattern9"):
                    opp_val = getattr(item, "vql_Pattern9", None)
                    
                    setattr(item, "vql_Pattern9", self)
                    

    @property
    def vql_PatternImport(self):
        return self.__vql_PatternImport

    @vql_PatternImport.setter
    def vql_PatternImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vql_PatternImport__vql_PatternImport", None)
        self.__vql_PatternImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vql_VQLImportSection2"):
                opp_val = getattr(old_value, "vql_VQLImportSection2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vql_VQLImportSection2"):
                opp_val = getattr(value, "vql_VQLImportSection2", None)
                if opp_val is None:
                    setattr(value, "vql_VQLImportSection2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass
