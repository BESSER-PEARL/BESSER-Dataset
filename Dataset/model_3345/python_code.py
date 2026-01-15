from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LogicalOperator(Enum):
    OR = "OR"
    NOT = "NOT"
    NONE = "NONE"
    AND = "AND"
class ComparisonOperator(Enum):
    EQ = "EQ"
    LT = "LT"
    GT = "GT"
    LE = "LE"
    GE = "GE"
    AND = "AND"
    OR = "OR"
    NE = "NE"
class LiteralType(Enum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
    REAL = "REAL"
    NULL = "NULL"
class PointCutOperator(Enum):
    EXECUTE = "EXECUTE"
    TARGET = "TARGET"
    CALL = "CALL"
class ImportSemantics(Enum):
    ACCESS = "ACCESS"
    IMPORT = "IMPORT"
class ImportType(Enum):
    LIBRARY = "LIBRARY"
    TRANSFORMATION = "TRANSFORMATION"
class AccessLevel(Enum):
    NONE = "NONE"
    PUBLIC = "PUBLIC"
    PROTECTED = "PROTECTED"
    PRIVATE = "PRIVATE"
class ArithmeticOperator(Enum):
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULT = "MULT"
    DIV = "DIV"
class PointCutCombinationOperator(Enum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"
    NONE = "NONE"
class AssignmentOperator(Enum):
    EQ = "EQ"
    PLUS_EQ = "PLUS_EQ"
class ParameterDirection(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
class AdviceOperator(Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    AROUND = "AROUND"


############################################
# Definition of Classes
############################################

class Trace:

    pass
class MOFScriptModel_M2MTrace(Trace):

    def __init__(self, name: str, id: str, MOFScriptModel_M2MTrace: "MOFScriptModel_Reference" = None, MOFScriptModel_M2MTrace116: "MOFScriptModel_Reference" = None):
        self.name = name
        self.id = id
        self.MOFScriptModel_M2MTrace = MOFScriptModel_M2MTrace
        self.MOFScriptModel_M2MTrace116 = MOFScriptModel_M2MTrace116
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MOFScriptModel_M2MTrace116(self):
        return self.__MOFScriptModel_M2MTrace116

    @MOFScriptModel_M2MTrace116.setter
    def MOFScriptModel_M2MTrace116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_M2MTrace__MOFScriptModel_M2MTrace116", None)
        self.__MOFScriptModel_M2MTrace116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_Reference117"):
                opp_val = getattr(old_value, "MOFScriptModel_Reference117", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_Reference117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_Reference117"):
                opp_val = getattr(value, "MOFScriptModel_Reference117", None)
                setattr(value, "MOFScriptModel_Reference117", self)

    @property
    def MOFScriptModel_M2MTrace(self):
        return self.__MOFScriptModel_M2MTrace

    @MOFScriptModel_M2MTrace.setter
    def MOFScriptModel_M2MTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_M2MTrace__MOFScriptModel_M2MTrace", None)
        self.__MOFScriptModel_M2MTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_Reference"):
                opp_val = getattr(old_value, "MOFScriptModel_Reference", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_Reference"):
                opp_val = getattr(value, "MOFScriptModel_Reference", None)
                setattr(value, "MOFScriptModel_Reference", self)

class MOFScriptModel_PointCutExpression:

    def __init__(self, expressionString: str, operator: str, combinationOperator: str, MOFScriptModel_PointCutExpression: "MOFScriptModel_PointCut" = None, MOFScriptModel_PointCutExpression97: "MOFScriptModel_PointCutExpression" = None, MOFScriptModel_PointCutExpression95: set["MOFScriptModel_PointCutExpression"] = None):
        self.expressionString = expressionString
        self.operator = operator
        self.combinationOperator = combinationOperator
        self.MOFScriptModel_PointCutExpression = MOFScriptModel_PointCutExpression
        self.MOFScriptModel_PointCutExpression97 = MOFScriptModel_PointCutExpression97
        self.MOFScriptModel_PointCutExpression95 = MOFScriptModel_PointCutExpression95 if MOFScriptModel_PointCutExpression95 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def expressionString(self) -> str:
        return self.__expressionString

    @expressionString.setter
    def expressionString(self, expressionString: str):
        self.__expressionString = expressionString

    @property
    def combinationOperator(self) -> str:
        return self.__combinationOperator

    @combinationOperator.setter
    def combinationOperator(self, combinationOperator: str):
        self.__combinationOperator = combinationOperator

    @property
    def MOFScriptModel_PointCutExpression(self):
        return self.__MOFScriptModel_PointCutExpression

    @MOFScriptModel_PointCutExpression.setter
    def MOFScriptModel_PointCutExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_PointCutExpression__MOFScriptModel_PointCutExpression", None)
        self.__MOFScriptModel_PointCutExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_PointCut94"):
                opp_val = getattr(old_value, "MOFScriptModel_PointCut94", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_PointCut94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_PointCut94"):
                opp_val = getattr(value, "MOFScriptModel_PointCut94", None)
                setattr(value, "MOFScriptModel_PointCut94", self)

    @property
    def MOFScriptModel_PointCutExpression97(self):
        return self.__MOFScriptModel_PointCutExpression97

    @MOFScriptModel_PointCutExpression97.setter
    def MOFScriptModel_PointCutExpression97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_PointCutExpression__MOFScriptModel_PointCutExpression97", None)
        self.__MOFScriptModel_PointCutExpression97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_PointCutExpression95"):
                opp_val = getattr(old_value, "MOFScriptModel_PointCutExpression95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_PointCutExpression95"):
                opp_val = getattr(value, "MOFScriptModel_PointCutExpression95", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_PointCutExpression95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MOFScriptModel_PointCutExpression95(self):
        return self.__MOFScriptModel_PointCutExpression95

    @MOFScriptModel_PointCutExpression95.setter
    def MOFScriptModel_PointCutExpression95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_PointCutExpression__MOFScriptModel_PointCutExpression95", None)
        self.__MOFScriptModel_PointCutExpression95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MOFScriptModel_PointCutExpression97"):
                    opp_val = getattr(item, "MOFScriptModel_PointCutExpression97", None)
                    
                    if opp_val == self:
                        setattr(item, "MOFScriptModel_PointCutExpression97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MOFScriptModel_PointCutExpression97"):
                    opp_val = getattr(item, "MOFScriptModel_PointCutExpression97", None)
                    
                    setattr(item, "MOFScriptModel_PointCutExpression97", self)
                    

class MOFScriptTransformation:

    pass
class MOFScriptModel_MOFScriptAspect(MOFScriptTransformation):

    pass
class MOFScriptModel_PointCut:

    def __init__(self, typeMatch: str, name: str, MOFScriptModel_PointCut: "MOFScriptModel_MOFScriptAspect" = None, MOFScriptModel_PointCut94: "MOFScriptModel_PointCutExpression" = None, MOFScriptModel_PointCut92: "MOFScriptModel_Advice" = None):
        self.typeMatch = typeMatch
        self.name = name
        self.MOFScriptModel_PointCut = MOFScriptModel_PointCut
        self.MOFScriptModel_PointCut94 = MOFScriptModel_PointCut94
        self.MOFScriptModel_PointCut92 = MOFScriptModel_PointCut92
        
    @property
    def typeMatch(self) -> str:
        return self.__typeMatch

    @typeMatch.setter
    def typeMatch(self, typeMatch: str):
        self.__typeMatch = typeMatch

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MOFScriptModel_PointCut94(self):
        return self.__MOFScriptModel_PointCut94

    @MOFScriptModel_PointCut94.setter
    def MOFScriptModel_PointCut94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_PointCut__MOFScriptModel_PointCut94", None)
        self.__MOFScriptModel_PointCut94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_PointCutExpression"):
                opp_val = getattr(old_value, "MOFScriptModel_PointCutExpression", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_PointCutExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_PointCutExpression"):
                opp_val = getattr(value, "MOFScriptModel_PointCutExpression", None)
                setattr(value, "MOFScriptModel_PointCutExpression", self)

    @property
    def MOFScriptModel_PointCut(self):
        return self.__MOFScriptModel_PointCut

    @MOFScriptModel_PointCut.setter
    def MOFScriptModel_PointCut(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_PointCut__MOFScriptModel_PointCut", None)
        self.__MOFScriptModel_PointCut = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_MOFScriptAspect89"):
                opp_val = getattr(old_value, "MOFScriptModel_MOFScriptAspect89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_MOFScriptAspect89"):
                opp_val = getattr(value, "MOFScriptModel_MOFScriptAspect89", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_MOFScriptAspect89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MOFScriptModel_PointCut92(self):
        return self.__MOFScriptModel_PointCut92

    @MOFScriptModel_PointCut92.setter
    def MOFScriptModel_PointCut92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_PointCut__MOFScriptModel_PointCut92", None)
        self.__MOFScriptModel_PointCut92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_Advice91"):
                opp_val = getattr(old_value, "MOFScriptModel_Advice91", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_Advice91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_Advice91"):
                opp_val = getattr(value, "MOFScriptModel_Advice91", None)
                setattr(value, "MOFScriptModel_Advice91", self)

class SimpleExpression:

    pass
class MOFScriptModel_Literal(SimpleExpression):

    def __init__(self, type: str, value: str):
        self.type = type
        self.value = value
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class MOFScriptModel_Reference(SimpleExpression):

    def __init__(self, name: str, MOFScriptModel_Reference: "MOFScriptModel_M2MTrace" = None, MOFScriptModel_Reference117: "MOFScriptModel_M2MTrace" = None):
        self.name = name
        self.MOFScriptModel_Reference = MOFScriptModel_Reference
        self.MOFScriptModel_Reference117 = MOFScriptModel_Reference117
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MOFScriptModel_Reference117(self):
        return self.__MOFScriptModel_Reference117

    @MOFScriptModel_Reference117.setter
    def MOFScriptModel_Reference117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_Reference__MOFScriptModel_Reference117", None)
        self.__MOFScriptModel_Reference117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_M2MTrace116"):
                opp_val = getattr(old_value, "MOFScriptModel_M2MTrace116", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_M2MTrace116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_M2MTrace116"):
                opp_val = getattr(value, "MOFScriptModel_M2MTrace116", None)
                setattr(value, "MOFScriptModel_M2MTrace116", self)

    @property
    def MOFScriptModel_Reference(self):
        return self.__MOFScriptModel_Reference

    @MOFScriptModel_Reference.setter
    def MOFScriptModel_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_Reference__MOFScriptModel_Reference", None)
        self.__MOFScriptModel_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_M2MTrace"):
                opp_val = getattr(old_value, "MOFScriptModel_M2MTrace", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_M2MTrace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_M2MTrace"):
                opp_val = getattr(value, "MOFScriptModel_M2MTrace", None)
                setattr(value, "MOFScriptModel_M2MTrace", self)

class MOFScriptModel_FunctionCall(SimpleExpression):

    def __init__(self, name: str, isSuperCall: bool, transformationContext: str, MOFScriptModel_FunctionCall: set["MOFScriptModel_ValueExpression"] = None, MOFScriptModel_FunctionCall54: "MOFScriptModel_TransformationRule" = None, MOFScriptModel_FunctionCall61: "MOFScriptModel_FunctionCallStatement" = None, MOFScriptModel_FunctionCall105: "MOFScriptModel_SelectExpression" = None):
        self.name = name
        self.isSuperCall = isSuperCall
        self.transformationContext = transformationContext
        self.MOFScriptModel_FunctionCall = MOFScriptModel_FunctionCall if MOFScriptModel_FunctionCall is not None else set()
        self.MOFScriptModel_FunctionCall54 = MOFScriptModel_FunctionCall54
        self.MOFScriptModel_FunctionCall61 = MOFScriptModel_FunctionCall61
        self.MOFScriptModel_FunctionCall105 = MOFScriptModel_FunctionCall105
        
    @property
    def isSuperCall(self) -> bool:
        return self.__isSuperCall

    @isSuperCall.setter
    def isSuperCall(self, isSuperCall: bool):
        self.__isSuperCall = isSuperCall

    @property
    def transformationContext(self) -> str:
        return self.__transformationContext

    @transformationContext.setter
    def transformationContext(self, transformationContext: str):
        self.__transformationContext = transformationContext

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MOFScriptModel_FunctionCall105(self):
        return self.__MOFScriptModel_FunctionCall105

    @MOFScriptModel_FunctionCall105.setter
    def MOFScriptModel_FunctionCall105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_FunctionCall__MOFScriptModel_FunctionCall105", None)
        self.__MOFScriptModel_FunctionCall105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_SelectExpression104"):
                opp_val = getattr(old_value, "MOFScriptModel_SelectExpression104", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_SelectExpression104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_SelectExpression104"):
                opp_val = getattr(value, "MOFScriptModel_SelectExpression104", None)
                setattr(value, "MOFScriptModel_SelectExpression104", self)

    @property
    def MOFScriptModel_FunctionCall54(self):
        return self.__MOFScriptModel_FunctionCall54

    @MOFScriptModel_FunctionCall54.setter
    def MOFScriptModel_FunctionCall54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_FunctionCall__MOFScriptModel_FunctionCall54", None)
        self.__MOFScriptModel_FunctionCall54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_TransformationRule55"):
                opp_val = getattr(old_value, "MOFScriptModel_TransformationRule55", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_TransformationRule55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_TransformationRule55"):
                opp_val = getattr(value, "MOFScriptModel_TransformationRule55", None)
                setattr(value, "MOFScriptModel_TransformationRule55", self)

    @property
    def MOFScriptModel_FunctionCall(self):
        return self.__MOFScriptModel_FunctionCall

    @MOFScriptModel_FunctionCall.setter
    def MOFScriptModel_FunctionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_FunctionCall__MOFScriptModel_FunctionCall", None)
        self.__MOFScriptModel_FunctionCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MOFScriptModel_ValueExpression52"):
                    opp_val = getattr(item, "MOFScriptModel_ValueExpression52", None)
                    
                    if opp_val == self:
                        setattr(item, "MOFScriptModel_ValueExpression52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MOFScriptModel_ValueExpression52"):
                    opp_val = getattr(item, "MOFScriptModel_ValueExpression52", None)
                    
                    setattr(item, "MOFScriptModel_ValueExpression52", self)
                    

    @property
    def MOFScriptModel_FunctionCall61(self):
        return self.__MOFScriptModel_FunctionCall61

    @MOFScriptModel_FunctionCall61.setter
    def MOFScriptModel_FunctionCall61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_FunctionCall__MOFScriptModel_FunctionCall61", None)
        self.__MOFScriptModel_FunctionCall61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_FunctionCallStatement"):
                opp_val = getattr(old_value, "MOFScriptModel_FunctionCallStatement", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_FunctionCallStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_FunctionCallStatement"):
                opp_val = getattr(value, "MOFScriptModel_FunctionCallStatement", None)
                setattr(value, "MOFScriptModel_FunctionCallStatement", self)

class ValueExpression:

    pass
class MOFScriptModel_SimpleExpression(ValueExpression):

    pass
class MOFScriptModel_SelectExpression(ValueExpression):

    def __init__(self, variable: str, type: str, MOFScriptModel_SelectExpression: "MOFScriptModel_Expression" = None, MOFScriptModel_SelectExpression101: "MOFScriptModel_SimpleExpression" = None, MOFScriptModel_SelectExpression104: "MOFScriptModel_FunctionCall" = None):
        self.variable = variable
        self.type = type
        self.MOFScriptModel_SelectExpression = MOFScriptModel_SelectExpression
        self.MOFScriptModel_SelectExpression101 = MOFScriptModel_SelectExpression101
        self.MOFScriptModel_SelectExpression104 = MOFScriptModel_SelectExpression104
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def MOFScriptModel_SelectExpression104(self):
        return self.__MOFScriptModel_SelectExpression104

    @MOFScriptModel_SelectExpression104.setter
    def MOFScriptModel_SelectExpression104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_SelectExpression__MOFScriptModel_SelectExpression104", None)
        self.__MOFScriptModel_SelectExpression104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_FunctionCall105"):
                opp_val = getattr(old_value, "MOFScriptModel_FunctionCall105", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_FunctionCall105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_FunctionCall105"):
                opp_val = getattr(value, "MOFScriptModel_FunctionCall105", None)
                setattr(value, "MOFScriptModel_FunctionCall105", self)

    @property
    def MOFScriptModel_SelectExpression101(self):
        return self.__MOFScriptModel_SelectExpression101

    @MOFScriptModel_SelectExpression101.setter
    def MOFScriptModel_SelectExpression101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_SelectExpression__MOFScriptModel_SelectExpression101", None)
        self.__MOFScriptModel_SelectExpression101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_SimpleExpression102"):
                opp_val = getattr(old_value, "MOFScriptModel_SimpleExpression102", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_SimpleExpression102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_SimpleExpression102"):
                opp_val = getattr(value, "MOFScriptModel_SimpleExpression102", None)
                setattr(value, "MOFScriptModel_SimpleExpression102", self)

    @property
    def MOFScriptModel_SelectExpression(self):
        return self.__MOFScriptModel_SelectExpression

    @MOFScriptModel_SelectExpression.setter
    def MOFScriptModel_SelectExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_SelectExpression__MOFScriptModel_SelectExpression", None)
        self.__MOFScriptModel_SelectExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_Expression99"):
                opp_val = getattr(old_value, "MOFScriptModel_Expression99", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_Expression99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_Expression99"):
                opp_val = getattr(value, "MOFScriptModel_Expression99", None)
                setattr(value, "MOFScriptModel_Expression99", self)

class MOFScriptModel_ArithmeticExpression(ValueExpression):

    def __init__(self, operator: str, MOFScriptModel_ArithmeticExpression: "MOFScriptModel_ValueExpression" = None, MOFScriptModel_ArithmeticExpression67: "MOFScriptModel_ValueExpression" = None):
        self.operator = operator
        self.MOFScriptModel_ArithmeticExpression = MOFScriptModel_ArithmeticExpression
        self.MOFScriptModel_ArithmeticExpression67 = MOFScriptModel_ArithmeticExpression67
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def MOFScriptModel_ArithmeticExpression67(self):
        return self.__MOFScriptModel_ArithmeticExpression67

    @MOFScriptModel_ArithmeticExpression67.setter
    def MOFScriptModel_ArithmeticExpression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ArithmeticExpression__MOFScriptModel_ArithmeticExpression67", None)
        self.__MOFScriptModel_ArithmeticExpression67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ValueExpression68"):
                opp_val = getattr(old_value, "MOFScriptModel_ValueExpression68", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ValueExpression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ValueExpression68"):
                opp_val = getattr(value, "MOFScriptModel_ValueExpression68", None)
                setattr(value, "MOFScriptModel_ValueExpression68", self)

    @property
    def MOFScriptModel_ArithmeticExpression(self):
        return self.__MOFScriptModel_ArithmeticExpression

    @MOFScriptModel_ArithmeticExpression.setter
    def MOFScriptModel_ArithmeticExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ArithmeticExpression__MOFScriptModel_ArithmeticExpression", None)
        self.__MOFScriptModel_ArithmeticExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ValueExpression65"):
                opp_val = getattr(old_value, "MOFScriptModel_ValueExpression65", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ValueExpression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ValueExpression65"):
                opp_val = getattr(value, "MOFScriptModel_ValueExpression65", None)
                setattr(value, "MOFScriptModel_ValueExpression65", self)

class MOFScriptStatement:

    pass
class MOFScriptModel_FileStatement(MOFScriptStatement):

    def __init__(self, fileReference: str, use: bool, append: bool, MOFScriptModel_FileStatement: "MOFScriptModel_ValueExpression" = None):
        self.fileReference = fileReference
        self.use = use
        self.append = append
        self.MOFScriptModel_FileStatement = MOFScriptModel_FileStatement
        
    @property
    def fileReference(self) -> str:
        return self.__fileReference

    @fileReference.setter
    def fileReference(self, fileReference: str):
        self.__fileReference = fileReference

    @property
    def use(self) -> bool:
        return self.__use

    @use.setter
    def use(self, use: bool):
        self.__use = use

    @property
    def append(self) -> bool:
        return self.__append

    @append.setter
    def append(self, append: bool):
        self.__append = append

    @property
    def MOFScriptModel_FileStatement(self):
        return self.__MOFScriptModel_FileStatement

    @MOFScriptModel_FileStatement.setter
    def MOFScriptModel_FileStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_FileStatement__MOFScriptModel_FileStatement", None)
        self.__MOFScriptModel_FileStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ValueExpression70"):
                opp_val = getattr(old_value, "MOFScriptModel_ValueExpression70", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ValueExpression70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ValueExpression70"):
                opp_val = getattr(value, "MOFScriptModel_ValueExpression70", None)
                setattr(value, "MOFScriptModel_ValueExpression70", self)

class MOFScriptModel_VariableDeclarationStatement(MOFScriptStatement):

    pass
class MOFScriptModel_FunctionCallStatement(MOFScriptStatement):

    pass
class MOFScriptModel_WhileStatement(MOFScriptStatement):

    pass
class MOFScriptModel_BreakStatement(MOFScriptStatement):

    pass
class MOFScriptModel_Trace(MOFScriptStatement):

    pass
class MOFScriptModel_ReturnStatement(MOFScriptStatement):

    pass
class MOFScriptModel_CreateStatement(MOFScriptStatement):

    def __init__(self, type: str, name: str):
        self.type = type
        self.name = name
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class MOFScriptModel_DebugStatement(MOFScriptStatement):

    def __init__(self, specification: str, vars: str):
        self.specification = specification
        self.vars = vars
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

    @property
    def vars(self) -> str:
        return self.__vars

    @vars.setter
    def vars(self, vars: str):
        self.__vars = vars

class MOFScriptModel_GeneralAssignment(MOFScriptStatement):

    def __init__(self, name: str, operator: str, MOFScriptModel_GeneralAssignment: "MOFScriptModel_Expression" = None):
        self.name = name
        self.operator = operator
        self.MOFScriptModel_GeneralAssignment = MOFScriptModel_GeneralAssignment
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MOFScriptModel_GeneralAssignment(self):
        return self.__MOFScriptModel_GeneralAssignment

    @MOFScriptModel_GeneralAssignment.setter
    def MOFScriptModel_GeneralAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_GeneralAssignment__MOFScriptModel_GeneralAssignment", None)
        self.__MOFScriptModel_GeneralAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_Expression59"):
                opp_val = getattr(old_value, "MOFScriptModel_Expression59", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_Expression59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_Expression59"):
                opp_val = getattr(value, "MOFScriptModel_Expression59", None)
                setattr(value, "MOFScriptModel_Expression59", self)

class MOFScriptModel_ResultAssignment(MOFScriptStatement):

    def __init__(self, resultPart: str, operator: str, MOFScriptModel_ResultAssignment: "MOFScriptModel_Expression" = None):
        self.resultPart = resultPart
        self.operator = operator
        self.MOFScriptModel_ResultAssignment = MOFScriptModel_ResultAssignment
        
    @property
    def resultPart(self) -> str:
        return self.__resultPart

    @resultPart.setter
    def resultPart(self, resultPart: str):
        self.__resultPart = resultPart

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def MOFScriptModel_ResultAssignment(self):
        return self.__MOFScriptModel_ResultAssignment

    @MOFScriptModel_ResultAssignment.setter
    def MOFScriptModel_ResultAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ResultAssignment__MOFScriptModel_ResultAssignment", None)
        self.__MOFScriptModel_ResultAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_Expression57"):
                opp_val = getattr(old_value, "MOFScriptModel_Expression57", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_Expression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_Expression57"):
                opp_val = getattr(value, "MOFScriptModel_Expression57", None)
                setattr(value, "MOFScriptModel_Expression57", self)

class MOFScriptModel_PrintStatement(MOFScriptStatement):

    def __init__(self, context: str, printCommand: str, MOFScriptModel_PrintStatement: "MOFScriptModel_ValueExpression" = None):
        self.context = context
        self.printCommand = printCommand
        self.MOFScriptModel_PrintStatement = MOFScriptModel_PrintStatement
        
    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def printCommand(self) -> str:
        return self.__printCommand

    @printCommand.setter
    def printCommand(self, printCommand: str):
        self.__printCommand = printCommand

    @property
    def MOFScriptModel_PrintStatement(self):
        return self.__MOFScriptModel_PrintStatement

    @MOFScriptModel_PrintStatement.setter
    def MOFScriptModel_PrintStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_PrintStatement__MOFScriptModel_PrintStatement", None)
        self.__MOFScriptModel_PrintStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ValueExpression63"):
                opp_val = getattr(old_value, "MOFScriptModel_ValueExpression63", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ValueExpression63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ValueExpression63"):
                opp_val = getattr(value, "MOFScriptModel_ValueExpression63", None)
                setattr(value, "MOFScriptModel_ValueExpression63", self)

class MOFScriptModel_IfStatement(MOFScriptStatement):

    pass
class MOFScriptModel_IteratorStatement(MOFScriptStatement):

    def __init__(self, type: str, variable: str, MOFScriptModel_IteratorStatement: "MOFScriptModel_Expression" = None, MOFScriptModel_IteratorStatement34: "MOFScriptModel_SimpleExpression" = None, MOFScriptModel_IteratorStatement36: "MOFScriptModel_ValueExpression" = None, MOFScriptModel_IteratorStatement38: "MOFScriptModel_ValueExpression" = None, MOFScriptModel_IteratorStatement41: "MOFScriptModel_ValueExpression" = None):
        self.type = type
        self.variable = variable
        self.MOFScriptModel_IteratorStatement = MOFScriptModel_IteratorStatement
        self.MOFScriptModel_IteratorStatement34 = MOFScriptModel_IteratorStatement34
        self.MOFScriptModel_IteratorStatement36 = MOFScriptModel_IteratorStatement36
        self.MOFScriptModel_IteratorStatement38 = MOFScriptModel_IteratorStatement38
        self.MOFScriptModel_IteratorStatement41 = MOFScriptModel_IteratorStatement41
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def MOFScriptModel_IteratorStatement36(self):
        return self.__MOFScriptModel_IteratorStatement36

    @MOFScriptModel_IteratorStatement36.setter
    def MOFScriptModel_IteratorStatement36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_IteratorStatement__MOFScriptModel_IteratorStatement36", None)
        self.__MOFScriptModel_IteratorStatement36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ValueExpression"):
                opp_val = getattr(old_value, "MOFScriptModel_ValueExpression", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ValueExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ValueExpression"):
                opp_val = getattr(value, "MOFScriptModel_ValueExpression", None)
                setattr(value, "MOFScriptModel_ValueExpression", self)

    @property
    def MOFScriptModel_IteratorStatement38(self):
        return self.__MOFScriptModel_IteratorStatement38

    @MOFScriptModel_IteratorStatement38.setter
    def MOFScriptModel_IteratorStatement38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_IteratorStatement__MOFScriptModel_IteratorStatement38", None)
        self.__MOFScriptModel_IteratorStatement38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ValueExpression39"):
                opp_val = getattr(old_value, "MOFScriptModel_ValueExpression39", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ValueExpression39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ValueExpression39"):
                opp_val = getattr(value, "MOFScriptModel_ValueExpression39", None)
                setattr(value, "MOFScriptModel_ValueExpression39", self)

    @property
    def MOFScriptModel_IteratorStatement41(self):
        return self.__MOFScriptModel_IteratorStatement41

    @MOFScriptModel_IteratorStatement41.setter
    def MOFScriptModel_IteratorStatement41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_IteratorStatement__MOFScriptModel_IteratorStatement41", None)
        self.__MOFScriptModel_IteratorStatement41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ValueExpression42"):
                opp_val = getattr(old_value, "MOFScriptModel_ValueExpression42", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ValueExpression42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ValueExpression42"):
                opp_val = getattr(value, "MOFScriptModel_ValueExpression42", None)
                setattr(value, "MOFScriptModel_ValueExpression42", self)

    @property
    def MOFScriptModel_IteratorStatement34(self):
        return self.__MOFScriptModel_IteratorStatement34

    @MOFScriptModel_IteratorStatement34.setter
    def MOFScriptModel_IteratorStatement34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_IteratorStatement__MOFScriptModel_IteratorStatement34", None)
        self.__MOFScriptModel_IteratorStatement34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_SimpleExpression"):
                opp_val = getattr(old_value, "MOFScriptModel_SimpleExpression", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_SimpleExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_SimpleExpression"):
                opp_val = getattr(value, "MOFScriptModel_SimpleExpression", None)
                setattr(value, "MOFScriptModel_SimpleExpression", self)

    @property
    def MOFScriptModel_IteratorStatement(self):
        return self.__MOFScriptModel_IteratorStatement

    @MOFScriptModel_IteratorStatement.setter
    def MOFScriptModel_IteratorStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_IteratorStatement__MOFScriptModel_IteratorStatement", None)
        self.__MOFScriptModel_IteratorStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_Expression32"):
                opp_val = getattr(old_value, "MOFScriptModel_Expression32", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_Expression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_Expression32"):
                opp_val = getattr(value, "MOFScriptModel_Expression32", None)
                setattr(value, "MOFScriptModel_Expression32", self)

class Expression:

    pass
class MOFScriptModel_LogicalExpression(Expression):

    def __init__(self, operator: str, MOFScriptModel_LogicalExpression: "MOFScriptModel_Expression" = None, MOFScriptModel_LogicalExpression46: "MOFScriptModel_Expression" = None):
        self.operator = operator
        self.MOFScriptModel_LogicalExpression = MOFScriptModel_LogicalExpression
        self.MOFScriptModel_LogicalExpression46 = MOFScriptModel_LogicalExpression46
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def MOFScriptModel_LogicalExpression(self):
        return self.__MOFScriptModel_LogicalExpression

    @MOFScriptModel_LogicalExpression.setter
    def MOFScriptModel_LogicalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_LogicalExpression__MOFScriptModel_LogicalExpression", None)
        self.__MOFScriptModel_LogicalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_Expression44"):
                opp_val = getattr(old_value, "MOFScriptModel_Expression44", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_Expression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_Expression44"):
                opp_val = getattr(value, "MOFScriptModel_Expression44", None)
                setattr(value, "MOFScriptModel_Expression44", self)

    @property
    def MOFScriptModel_LogicalExpression46(self):
        return self.__MOFScriptModel_LogicalExpression46

    @MOFScriptModel_LogicalExpression46.setter
    def MOFScriptModel_LogicalExpression46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_LogicalExpression__MOFScriptModel_LogicalExpression46", None)
        self.__MOFScriptModel_LogicalExpression46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_Expression47"):
                opp_val = getattr(old_value, "MOFScriptModel_Expression47", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_Expression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_Expression47"):
                opp_val = getattr(value, "MOFScriptModel_Expression47", None)
                setattr(value, "MOFScriptModel_Expression47", self)

class MOFScriptModel_CreateExpression(Expression):

    def __init__(self, type: str, MOFScriptModel_CreateExpression: set["MOFScriptModel_CreateExpressionParameter"] = None):
        self.type = type
        self.MOFScriptModel_CreateExpression = MOFScriptModel_CreateExpression if MOFScriptModel_CreateExpression is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def MOFScriptModel_CreateExpression(self):
        return self.__MOFScriptModel_CreateExpression

    @MOFScriptModel_CreateExpression.setter
    def MOFScriptModel_CreateExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_CreateExpression__MOFScriptModel_CreateExpression", None)
        self.__MOFScriptModel_CreateExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MOFScriptModel_CreateExpressionParameter"):
                    opp_val = getattr(item, "MOFScriptModel_CreateExpressionParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "MOFScriptModel_CreateExpressionParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MOFScriptModel_CreateExpressionParameter"):
                    opp_val = getattr(item, "MOFScriptModel_CreateExpressionParameter", None)
                    
                    setattr(item, "MOFScriptModel_CreateExpressionParameter", self)
                    

class MOFScriptModel_ComparisonExpression(Expression):

    def __init__(self, operator: str, MOFScriptModel_ComparisonExpression: "MOFScriptModel_ValueExpression" = None, MOFScriptModel_ComparisonExpression74: "MOFScriptModel_ValueExpression" = None):
        self.operator = operator
        self.MOFScriptModel_ComparisonExpression = MOFScriptModel_ComparisonExpression
        self.MOFScriptModel_ComparisonExpression74 = MOFScriptModel_ComparisonExpression74
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def MOFScriptModel_ComparisonExpression(self):
        return self.__MOFScriptModel_ComparisonExpression

    @MOFScriptModel_ComparisonExpression.setter
    def MOFScriptModel_ComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ComparisonExpression__MOFScriptModel_ComparisonExpression", None)
        self.__MOFScriptModel_ComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ValueExpression72"):
                opp_val = getattr(old_value, "MOFScriptModel_ValueExpression72", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ValueExpression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ValueExpression72"):
                opp_val = getattr(value, "MOFScriptModel_ValueExpression72", None)
                setattr(value, "MOFScriptModel_ValueExpression72", self)

    @property
    def MOFScriptModel_ComparisonExpression74(self):
        return self.__MOFScriptModel_ComparisonExpression74

    @MOFScriptModel_ComparisonExpression74.setter
    def MOFScriptModel_ComparisonExpression74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ComparisonExpression__MOFScriptModel_ComparisonExpression74", None)
        self.__MOFScriptModel_ComparisonExpression74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ValueExpression75"):
                opp_val = getattr(old_value, "MOFScriptModel_ValueExpression75", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ValueExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ValueExpression75"):
                opp_val = getattr(value, "MOFScriptModel_ValueExpression75", None)
                setattr(value, "MOFScriptModel_ValueExpression75", self)

class MOFScriptModel_ValueExpression(Expression):

    def __init__(self, specification: str, MOFScriptModel_ValueExpression52: "MOFScriptModel_FunctionCall" = None, MOFScriptModel_ValueExpression: "MOFScriptModel_IteratorStatement" = None, MOFScriptModel_ValueExpression39: "MOFScriptModel_IteratorStatement" = None, MOFScriptModel_ValueExpression42: "MOFScriptModel_IteratorStatement" = None, MOFScriptModel_ValueExpression65: "MOFScriptModel_ArithmeticExpression" = None, MOFScriptModel_ValueExpression68: "MOFScriptModel_ArithmeticExpression" = None, MOFScriptModel_ValueExpression63: "MOFScriptModel_PrintStatement" = None, MOFScriptModel_ValueExpression72: "MOFScriptModel_ComparisonExpression" = None, MOFScriptModel_ValueExpression75: "MOFScriptModel_ComparisonExpression" = None, MOFScriptModel_ValueExpression70: "MOFScriptModel_FileStatement" = None, MOFScriptModel_ValueExpression109: "MOFScriptModel_CreateExpressionParameter" = None):
        self.specification = specification
        self.MOFScriptModel_ValueExpression52 = MOFScriptModel_ValueExpression52
        self.MOFScriptModel_ValueExpression = MOFScriptModel_ValueExpression
        self.MOFScriptModel_ValueExpression39 = MOFScriptModel_ValueExpression39
        self.MOFScriptModel_ValueExpression42 = MOFScriptModel_ValueExpression42
        self.MOFScriptModel_ValueExpression65 = MOFScriptModel_ValueExpression65
        self.MOFScriptModel_ValueExpression68 = MOFScriptModel_ValueExpression68
        self.MOFScriptModel_ValueExpression63 = MOFScriptModel_ValueExpression63
        self.MOFScriptModel_ValueExpression72 = MOFScriptModel_ValueExpression72
        self.MOFScriptModel_ValueExpression75 = MOFScriptModel_ValueExpression75
        self.MOFScriptModel_ValueExpression70 = MOFScriptModel_ValueExpression70
        self.MOFScriptModel_ValueExpression109 = MOFScriptModel_ValueExpression109
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

    @property
    def MOFScriptModel_ValueExpression65(self):
        return self.__MOFScriptModel_ValueExpression65

    @MOFScriptModel_ValueExpression65.setter
    def MOFScriptModel_ValueExpression65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ValueExpression__MOFScriptModel_ValueExpression65", None)
        self.__MOFScriptModel_ValueExpression65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ArithmeticExpression"):
                opp_val = getattr(old_value, "MOFScriptModel_ArithmeticExpression", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ArithmeticExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ArithmeticExpression"):
                opp_val = getattr(value, "MOFScriptModel_ArithmeticExpression", None)
                setattr(value, "MOFScriptModel_ArithmeticExpression", self)

    @property
    def MOFScriptModel_ValueExpression(self):
        return self.__MOFScriptModel_ValueExpression

    @MOFScriptModel_ValueExpression.setter
    def MOFScriptModel_ValueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ValueExpression__MOFScriptModel_ValueExpression", None)
        self.__MOFScriptModel_ValueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_IteratorStatement36"):
                opp_val = getattr(old_value, "MOFScriptModel_IteratorStatement36", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_IteratorStatement36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_IteratorStatement36"):
                opp_val = getattr(value, "MOFScriptModel_IteratorStatement36", None)
                setattr(value, "MOFScriptModel_IteratorStatement36", self)

    @property
    def MOFScriptModel_ValueExpression39(self):
        return self.__MOFScriptModel_ValueExpression39

    @MOFScriptModel_ValueExpression39.setter
    def MOFScriptModel_ValueExpression39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ValueExpression__MOFScriptModel_ValueExpression39", None)
        self.__MOFScriptModel_ValueExpression39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_IteratorStatement38"):
                opp_val = getattr(old_value, "MOFScriptModel_IteratorStatement38", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_IteratorStatement38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_IteratorStatement38"):
                opp_val = getattr(value, "MOFScriptModel_IteratorStatement38", None)
                setattr(value, "MOFScriptModel_IteratorStatement38", self)

    @property
    def MOFScriptModel_ValueExpression52(self):
        return self.__MOFScriptModel_ValueExpression52

    @MOFScriptModel_ValueExpression52.setter
    def MOFScriptModel_ValueExpression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ValueExpression__MOFScriptModel_ValueExpression52", None)
        self.__MOFScriptModel_ValueExpression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_FunctionCall"):
                opp_val = getattr(old_value, "MOFScriptModel_FunctionCall", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_FunctionCall"):
                opp_val = getattr(value, "MOFScriptModel_FunctionCall", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_FunctionCall", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MOFScriptModel_ValueExpression42(self):
        return self.__MOFScriptModel_ValueExpression42

    @MOFScriptModel_ValueExpression42.setter
    def MOFScriptModel_ValueExpression42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ValueExpression__MOFScriptModel_ValueExpression42", None)
        self.__MOFScriptModel_ValueExpression42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_IteratorStatement41"):
                opp_val = getattr(old_value, "MOFScriptModel_IteratorStatement41", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_IteratorStatement41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_IteratorStatement41"):
                opp_val = getattr(value, "MOFScriptModel_IteratorStatement41", None)
                setattr(value, "MOFScriptModel_IteratorStatement41", self)

    @property
    def MOFScriptModel_ValueExpression63(self):
        return self.__MOFScriptModel_ValueExpression63

    @MOFScriptModel_ValueExpression63.setter
    def MOFScriptModel_ValueExpression63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ValueExpression__MOFScriptModel_ValueExpression63", None)
        self.__MOFScriptModel_ValueExpression63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_PrintStatement"):
                opp_val = getattr(old_value, "MOFScriptModel_PrintStatement", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_PrintStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_PrintStatement"):
                opp_val = getattr(value, "MOFScriptModel_PrintStatement", None)
                setattr(value, "MOFScriptModel_PrintStatement", self)

    @property
    def MOFScriptModel_ValueExpression70(self):
        return self.__MOFScriptModel_ValueExpression70

    @MOFScriptModel_ValueExpression70.setter
    def MOFScriptModel_ValueExpression70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ValueExpression__MOFScriptModel_ValueExpression70", None)
        self.__MOFScriptModel_ValueExpression70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_FileStatement"):
                opp_val = getattr(old_value, "MOFScriptModel_FileStatement", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_FileStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_FileStatement"):
                opp_val = getattr(value, "MOFScriptModel_FileStatement", None)
                setattr(value, "MOFScriptModel_FileStatement", self)

    @property
    def MOFScriptModel_ValueExpression109(self):
        return self.__MOFScriptModel_ValueExpression109

    @MOFScriptModel_ValueExpression109.setter
    def MOFScriptModel_ValueExpression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ValueExpression__MOFScriptModel_ValueExpression109", None)
        self.__MOFScriptModel_ValueExpression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_CreateExpressionParameter108"):
                opp_val = getattr(old_value, "MOFScriptModel_CreateExpressionParameter108", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_CreateExpressionParameter108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_CreateExpressionParameter108"):
                opp_val = getattr(value, "MOFScriptModel_CreateExpressionParameter108", None)
                setattr(value, "MOFScriptModel_CreateExpressionParameter108", self)

    @property
    def MOFScriptModel_ValueExpression75(self):
        return self.__MOFScriptModel_ValueExpression75

    @MOFScriptModel_ValueExpression75.setter
    def MOFScriptModel_ValueExpression75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ValueExpression__MOFScriptModel_ValueExpression75", None)
        self.__MOFScriptModel_ValueExpression75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ComparisonExpression74"):
                opp_val = getattr(old_value, "MOFScriptModel_ComparisonExpression74", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ComparisonExpression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ComparisonExpression74"):
                opp_val = getattr(value, "MOFScriptModel_ComparisonExpression74", None)
                setattr(value, "MOFScriptModel_ComparisonExpression74", self)

    @property
    def MOFScriptModel_ValueExpression68(self):
        return self.__MOFScriptModel_ValueExpression68

    @MOFScriptModel_ValueExpression68.setter
    def MOFScriptModel_ValueExpression68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ValueExpression__MOFScriptModel_ValueExpression68", None)
        self.__MOFScriptModel_ValueExpression68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ArithmeticExpression67"):
                opp_val = getattr(old_value, "MOFScriptModel_ArithmeticExpression67", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ArithmeticExpression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ArithmeticExpression67"):
                opp_val = getattr(value, "MOFScriptModel_ArithmeticExpression67", None)
                setattr(value, "MOFScriptModel_ArithmeticExpression67", self)

    @property
    def MOFScriptModel_ValueExpression72(self):
        return self.__MOFScriptModel_ValueExpression72

    @MOFScriptModel_ValueExpression72.setter
    def MOFScriptModel_ValueExpression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_ValueExpression__MOFScriptModel_ValueExpression72", None)
        self.__MOFScriptModel_ValueExpression72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ComparisonExpression"):
                opp_val = getattr(old_value, "MOFScriptModel_ComparisonExpression", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ComparisonExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ComparisonExpression"):
                opp_val = getattr(value, "MOFScriptModel_ComparisonExpression", None)
                setattr(value, "MOFScriptModel_ComparisonExpression", self)

class MOFScriptObject:

    pass
class MOFScriptModel_CreateExpressionParameter(MOFScriptObject):

    def __init__(self, name: str, MOFScriptModel_CreateExpressionParameter: "MOFScriptModel_CreateExpression" = None, MOFScriptModel_CreateExpressionParameter108: "MOFScriptModel_ValueExpression" = None):
        self.name = name
        self.MOFScriptModel_CreateExpressionParameter = MOFScriptModel_CreateExpressionParameter
        self.MOFScriptModel_CreateExpressionParameter108 = MOFScriptModel_CreateExpressionParameter108
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MOFScriptModel_CreateExpressionParameter108(self):
        return self.__MOFScriptModel_CreateExpressionParameter108

    @MOFScriptModel_CreateExpressionParameter108.setter
    def MOFScriptModel_CreateExpressionParameter108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_CreateExpressionParameter__MOFScriptModel_CreateExpressionParameter108", None)
        self.__MOFScriptModel_CreateExpressionParameter108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_ValueExpression109"):
                opp_val = getattr(old_value, "MOFScriptModel_ValueExpression109", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_ValueExpression109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_ValueExpression109"):
                opp_val = getattr(value, "MOFScriptModel_ValueExpression109", None)
                setattr(value, "MOFScriptModel_ValueExpression109", self)

    @property
    def MOFScriptModel_CreateExpressionParameter(self):
        return self.__MOFScriptModel_CreateExpressionParameter

    @MOFScriptModel_CreateExpressionParameter.setter
    def MOFScriptModel_CreateExpressionParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_CreateExpressionParameter__MOFScriptModel_CreateExpressionParameter", None)
        self.__MOFScriptModel_CreateExpressionParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_CreateExpression"):
                opp_val = getattr(old_value, "MOFScriptModel_CreateExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_CreateExpression"):
                opp_val = getattr(value, "MOFScriptModel_CreateExpression", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_CreateExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MOFScriptModel_MOFScriptSpecification(MOFScriptObject):

    pass
class MOFScriptModel_MOFScriptImport(MOFScriptObject):

    def __init__(self, type: str, uri: str, importSemantics: str, name: str, MOFScriptModel_MOFScriptImport: "MOFScriptModel_MOFScriptSpecification" = None):
        self.type = type
        self.uri = uri
        self.importSemantics = importSemantics
        self.name = name
        self.MOFScriptModel_MOFScriptImport = MOFScriptModel_MOFScriptImport
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def importSemantics(self) -> str:
        return self.__importSemantics

    @importSemantics.setter
    def importSemantics(self, importSemantics: str):
        self.__importSemantics = importSemantics

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def MOFScriptModel_MOFScriptImport(self):
        return self.__MOFScriptModel_MOFScriptImport

    @MOFScriptModel_MOFScriptImport.setter
    def MOFScriptModel_MOFScriptImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptImport__MOFScriptModel_MOFScriptImport", None)
        self.__MOFScriptModel_MOFScriptImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_MOFScriptSpecification84"):
                opp_val = getattr(old_value, "MOFScriptModel_MOFScriptSpecification84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_MOFScriptSpecification84"):
                opp_val = getattr(value, "MOFScriptModel_MOFScriptSpecification84", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_MOFScriptSpecification84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MOFScriptModel_VariableDeclaration(MOFScriptObject):

    def __init__(self, name: str, type: str, constant: bool, MOFScriptModel_VariableDeclaration: "MOFScriptModel_MOFScriptStatementOwner" = None, MOFScriptModel_VariableDeclaration19: "MOFScriptModel_MOFScriptTransformation" = None, MOFScriptModel_VariableDeclaration22: "MOFScriptModel_MOFScriptTransformation" = None, MOFScriptModel_VariableDeclaration15: "MOFScriptModel_Expression" = None, MOFScriptModel_VariableDeclaration113: "MOFScriptModel_VariableDeclarationStatement" = None):
        self.name = name
        self.type = type
        self.constant = constant
        self.MOFScriptModel_VariableDeclaration = MOFScriptModel_VariableDeclaration
        self.MOFScriptModel_VariableDeclaration19 = MOFScriptModel_VariableDeclaration19
        self.MOFScriptModel_VariableDeclaration22 = MOFScriptModel_VariableDeclaration22
        self.MOFScriptModel_VariableDeclaration15 = MOFScriptModel_VariableDeclaration15
        self.MOFScriptModel_VariableDeclaration113 = MOFScriptModel_VariableDeclaration113
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def MOFScriptModel_VariableDeclaration22(self):
        return self.__MOFScriptModel_VariableDeclaration22

    @MOFScriptModel_VariableDeclaration22.setter
    def MOFScriptModel_VariableDeclaration22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_VariableDeclaration__MOFScriptModel_VariableDeclaration22", None)
        self.__MOFScriptModel_VariableDeclaration22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_MOFScriptTransformation21"):
                opp_val = getattr(old_value, "MOFScriptModel_MOFScriptTransformation21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_MOFScriptTransformation21"):
                opp_val = getattr(value, "MOFScriptModel_MOFScriptTransformation21", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_MOFScriptTransformation21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MOFScriptModel_VariableDeclaration(self):
        return self.__MOFScriptModel_VariableDeclaration

    @MOFScriptModel_VariableDeclaration.setter
    def MOFScriptModel_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_VariableDeclaration__MOFScriptModel_VariableDeclaration", None)
        self.__MOFScriptModel_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_MOFScriptStatementOwner"):
                opp_val = getattr(old_value, "MOFScriptModel_MOFScriptStatementOwner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_MOFScriptStatementOwner"):
                opp_val = getattr(value, "MOFScriptModel_MOFScriptStatementOwner", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_MOFScriptStatementOwner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MOFScriptModel_VariableDeclaration15(self):
        return self.__MOFScriptModel_VariableDeclaration15

    @MOFScriptModel_VariableDeclaration15.setter
    def MOFScriptModel_VariableDeclaration15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_VariableDeclaration__MOFScriptModel_VariableDeclaration15", None)
        self.__MOFScriptModel_VariableDeclaration15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_Expression"):
                opp_val = getattr(old_value, "MOFScriptModel_Expression", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_Expression"):
                opp_val = getattr(value, "MOFScriptModel_Expression", None)
                setattr(value, "MOFScriptModel_Expression", self)

    @property
    def MOFScriptModel_VariableDeclaration113(self):
        return self.__MOFScriptModel_VariableDeclaration113

    @MOFScriptModel_VariableDeclaration113.setter
    def MOFScriptModel_VariableDeclaration113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_VariableDeclaration__MOFScriptModel_VariableDeclaration113", None)
        self.__MOFScriptModel_VariableDeclaration113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_VariableDeclarationStatement"):
                opp_val = getattr(old_value, "MOFScriptModel_VariableDeclarationStatement", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_VariableDeclarationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_VariableDeclarationStatement"):
                opp_val = getattr(value, "MOFScriptModel_VariableDeclarationStatement", None)
                setattr(value, "MOFScriptModel_VariableDeclarationStatement", self)

    @property
    def MOFScriptModel_VariableDeclaration19(self):
        return self.__MOFScriptModel_VariableDeclaration19

    @MOFScriptModel_VariableDeclaration19.setter
    def MOFScriptModel_VariableDeclaration19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_VariableDeclaration__MOFScriptModel_VariableDeclaration19", None)
        self.__MOFScriptModel_VariableDeclaration19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_MOFScriptTransformation"):
                opp_val = getattr(old_value, "MOFScriptModel_MOFScriptTransformation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_MOFScriptTransformation"):
                opp_val = getattr(value, "MOFScriptModel_MOFScriptTransformation", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_MOFScriptTransformation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MOFScriptModel_Expression(MOFScriptObject):

    pass
class MOFScriptModel_MOFScriptStatementOwner(MOFScriptObject):

    pass
class MOFScriptModel_MOFScriptParameter(MOFScriptObject):

    def __init__(self, name: str, type: str, direction: str, typePrefix: str, MOFScriptModel_MOFScriptParameter: "MOFScriptModel_TransformationRule" = None, MOFScriptModel_MOFScriptParameter7: "MOFScriptModel_TransformationRule" = None, MOFScriptModel_MOFScriptParameter25: "MOFScriptModel_MOFScriptTransformation" = None):
        self.name = name
        self.type = type
        self.direction = direction
        self.typePrefix = typePrefix
        self.MOFScriptModel_MOFScriptParameter = MOFScriptModel_MOFScriptParameter
        self.MOFScriptModel_MOFScriptParameter7 = MOFScriptModel_MOFScriptParameter7
        self.MOFScriptModel_MOFScriptParameter25 = MOFScriptModel_MOFScriptParameter25
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typePrefix(self) -> str:
        return self.__typePrefix

    @typePrefix.setter
    def typePrefix(self, typePrefix: str):
        self.__typePrefix = typePrefix

    @property
    def MOFScriptModel_MOFScriptParameter7(self):
        return self.__MOFScriptModel_MOFScriptParameter7

    @MOFScriptModel_MOFScriptParameter7.setter
    def MOFScriptModel_MOFScriptParameter7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptParameter__MOFScriptModel_MOFScriptParameter7", None)
        self.__MOFScriptModel_MOFScriptParameter7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_TransformationRule6"):
                opp_val = getattr(old_value, "MOFScriptModel_TransformationRule6", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_TransformationRule6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_TransformationRule6"):
                opp_val = getattr(value, "MOFScriptModel_TransformationRule6", None)
                setattr(value, "MOFScriptModel_TransformationRule6", self)

    @property
    def MOFScriptModel_MOFScriptParameter(self):
        return self.__MOFScriptModel_MOFScriptParameter

    @MOFScriptModel_MOFScriptParameter.setter
    def MOFScriptModel_MOFScriptParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptParameter__MOFScriptModel_MOFScriptParameter", None)
        self.__MOFScriptModel_MOFScriptParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_TransformationRule4"):
                opp_val = getattr(old_value, "MOFScriptModel_TransformationRule4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_TransformationRule4"):
                opp_val = getattr(value, "MOFScriptModel_TransformationRule4", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_TransformationRule4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MOFScriptModel_MOFScriptParameter25(self):
        return self.__MOFScriptModel_MOFScriptParameter25

    @MOFScriptModel_MOFScriptParameter25.setter
    def MOFScriptModel_MOFScriptParameter25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptParameter__MOFScriptModel_MOFScriptParameter25", None)
        self.__MOFScriptModel_MOFScriptParameter25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_MOFScriptTransformation24"):
                opp_val = getattr(old_value, "MOFScriptModel_MOFScriptTransformation24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_MOFScriptTransformation24"):
                opp_val = getattr(value, "MOFScriptModel_MOFScriptTransformation24", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_MOFScriptTransformation24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MOFScriptModel_MOFScriptTransformation(MOFScriptObject):

    def __init__(self, name: str, extendsName: str, MOFScriptTransformation: "MOFScriptModel_TransformationRule" = None, MOFScriptModel_MOFScriptTransformation: set["MOFScriptModel_VariableDeclaration"] = None, MOFScriptModel_MOFScriptTransformation21: set["MOFScriptModel_VariableDeclaration"] = None, MOFScriptModel_MOFScriptTransformation24: set["MOFScriptModel_MOFScriptParameter"] = None, MOFScriptModel_MOFScriptTransformation28: "MOFScriptModel_MOFScriptTransformation" = None, MOFScriptModel_MOFScriptTransformation26: "MOFScriptModel_MOFScriptTransformation" = None, owner30: set["MOFScriptModel_TransformationRule"] = None, MOFScriptModel_MOFScriptTransformation82: "MOFScriptModel_MOFScriptSpecification" = None):
        self.name = name
        self.extendsName = extendsName
        self.MOFScriptTransformation = MOFScriptTransformation
        self.MOFScriptModel_MOFScriptTransformation = MOFScriptModel_MOFScriptTransformation if MOFScriptModel_MOFScriptTransformation is not None else set()
        self.MOFScriptModel_MOFScriptTransformation21 = MOFScriptModel_MOFScriptTransformation21 if MOFScriptModel_MOFScriptTransformation21 is not None else set()
        self.MOFScriptModel_MOFScriptTransformation24 = MOFScriptModel_MOFScriptTransformation24 if MOFScriptModel_MOFScriptTransformation24 is not None else set()
        self.MOFScriptModel_MOFScriptTransformation28 = MOFScriptModel_MOFScriptTransformation28
        self.MOFScriptModel_MOFScriptTransformation26 = MOFScriptModel_MOFScriptTransformation26
        self.owner30 = owner30 if owner30 is not None else set()
        self.MOFScriptModel_MOFScriptTransformation82 = MOFScriptModel_MOFScriptTransformation82
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extendsName(self) -> str:
        return self.__extendsName

    @extendsName.setter
    def extendsName(self, extendsName: str):
        self.__extendsName = extendsName

    @property
    def MOFScriptModel_MOFScriptTransformation24(self):
        return self.__MOFScriptModel_MOFScriptTransformation24

    @MOFScriptModel_MOFScriptTransformation24.setter
    def MOFScriptModel_MOFScriptTransformation24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptTransformation__MOFScriptModel_MOFScriptTransformation24", None)
        self.__MOFScriptModel_MOFScriptTransformation24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MOFScriptModel_MOFScriptParameter25"):
                    opp_val = getattr(item, "MOFScriptModel_MOFScriptParameter25", None)
                    
                    if opp_val == self:
                        setattr(item, "MOFScriptModel_MOFScriptParameter25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MOFScriptModel_MOFScriptParameter25"):
                    opp_val = getattr(item, "MOFScriptModel_MOFScriptParameter25", None)
                    
                    setattr(item, "MOFScriptModel_MOFScriptParameter25", self)
                    

    @property
    def MOFScriptModel_MOFScriptTransformation(self):
        return self.__MOFScriptModel_MOFScriptTransformation

    @MOFScriptModel_MOFScriptTransformation.setter
    def MOFScriptModel_MOFScriptTransformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptTransformation__MOFScriptModel_MOFScriptTransformation", None)
        self.__MOFScriptModel_MOFScriptTransformation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MOFScriptModel_VariableDeclaration19"):
                    opp_val = getattr(item, "MOFScriptModel_VariableDeclaration19", None)
                    
                    if opp_val == self:
                        setattr(item, "MOFScriptModel_VariableDeclaration19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MOFScriptModel_VariableDeclaration19"):
                    opp_val = getattr(item, "MOFScriptModel_VariableDeclaration19", None)
                    
                    setattr(item, "MOFScriptModel_VariableDeclaration19", self)
                    

    @property
    def MOFScriptModel_MOFScriptTransformation26(self):
        return self.__MOFScriptModel_MOFScriptTransformation26

    @MOFScriptModel_MOFScriptTransformation26.setter
    def MOFScriptModel_MOFScriptTransformation26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptTransformation__MOFScriptModel_MOFScriptTransformation26", None)
        self.__MOFScriptModel_MOFScriptTransformation26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_MOFScriptTransformation28"):
                opp_val = getattr(old_value, "MOFScriptModel_MOFScriptTransformation28", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_MOFScriptTransformation28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_MOFScriptTransformation28"):
                opp_val = getattr(value, "MOFScriptModel_MOFScriptTransformation28", None)
                setattr(value, "MOFScriptModel_MOFScriptTransformation28", self)

    @property
    def MOFScriptModel_MOFScriptTransformation82(self):
        return self.__MOFScriptModel_MOFScriptTransformation82

    @MOFScriptModel_MOFScriptTransformation82.setter
    def MOFScriptModel_MOFScriptTransformation82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptTransformation__MOFScriptModel_MOFScriptTransformation82", None)
        self.__MOFScriptModel_MOFScriptTransformation82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_MOFScriptSpecification"):
                opp_val = getattr(old_value, "MOFScriptModel_MOFScriptSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_MOFScriptSpecification"):
                opp_val = getattr(value, "MOFScriptModel_MOFScriptSpecification", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_MOFScriptSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MOFScriptTransformation(self):
        return self.__MOFScriptTransformation

    @MOFScriptTransformation.setter
    def MOFScriptTransformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptTransformation__MOFScriptTransformation", None)
        self.__MOFScriptTransformation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformationrules"):
                opp_val = getattr(old_value, "transformationrules", None)
                if opp_val == self:
                    setattr(old_value, "transformationrules", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformationrules"):
                opp_val = getattr(value, "transformationrules", None)
                setattr(value, "transformationrules", self)

    @property
    def owner30(self):
        return self.__owner30

    @owner30.setter
    def owner30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptTransformation__owner30", None)
        self.__owner30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransformationRule"):
                    opp_val = getattr(item, "TransformationRule", None)
                    
                    if opp_val == self:
                        setattr(item, "TransformationRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransformationRule"):
                    opp_val = getattr(item, "TransformationRule", None)
                    
                    setattr(item, "TransformationRule", self)
                    

    @property
    def MOFScriptModel_MOFScriptTransformation28(self):
        return self.__MOFScriptModel_MOFScriptTransformation28

    @MOFScriptModel_MOFScriptTransformation28.setter
    def MOFScriptModel_MOFScriptTransformation28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptTransformation__MOFScriptModel_MOFScriptTransformation28", None)
        self.__MOFScriptModel_MOFScriptTransformation28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_MOFScriptTransformation26"):
                opp_val = getattr(old_value, "MOFScriptModel_MOFScriptTransformation26", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_MOFScriptTransformation26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_MOFScriptTransformation26"):
                opp_val = getattr(value, "MOFScriptModel_MOFScriptTransformation26", None)
                setattr(value, "MOFScriptModel_MOFScriptTransformation26", self)

    @property
    def MOFScriptModel_MOFScriptTransformation21(self):
        return self.__MOFScriptModel_MOFScriptTransformation21

    @MOFScriptModel_MOFScriptTransformation21.setter
    def MOFScriptModel_MOFScriptTransformation21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptTransformation__MOFScriptModel_MOFScriptTransformation21", None)
        self.__MOFScriptModel_MOFScriptTransformation21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MOFScriptModel_VariableDeclaration22"):
                    opp_val = getattr(item, "MOFScriptModel_VariableDeclaration22", None)
                    
                    if opp_val == self:
                        setattr(item, "MOFScriptModel_VariableDeclaration22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MOFScriptModel_VariableDeclaration22"):
                    opp_val = getattr(item, "MOFScriptModel_VariableDeclaration22", None)
                    
                    setattr(item, "MOFScriptModel_VariableDeclaration22", self)
                    

class MOFScriptModel_MOFScriptComment(MOFScriptObject):

    def __init__(self, commentText: str, singleLine: bool, docStyle: bool, MOFScriptModel_MOFScriptComment: "MOFScriptModel_MOFScriptObject" = None):
        self.commentText = commentText
        self.singleLine = singleLine
        self.docStyle = docStyle
        self.MOFScriptModel_MOFScriptComment = MOFScriptModel_MOFScriptComment
        
    @property
    def commentText(self) -> str:
        return self.__commentText

    @commentText.setter
    def commentText(self, commentText: str):
        self.__commentText = commentText

    @property
    def docStyle(self) -> bool:
        return self.__docStyle

    @docStyle.setter
    def docStyle(self, docStyle: bool):
        self.__docStyle = docStyle

    @property
    def singleLine(self) -> bool:
        return self.__singleLine

    @singleLine.setter
    def singleLine(self, singleLine: bool):
        self.__singleLine = singleLine

    @property
    def MOFScriptModel_MOFScriptComment(self):
        return self.__MOFScriptModel_MOFScriptComment

    @MOFScriptModel_MOFScriptComment.setter
    def MOFScriptModel_MOFScriptComment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptComment__MOFScriptModel_MOFScriptComment", None)
        self.__MOFScriptModel_MOFScriptComment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_MOFScriptObject"):
                opp_val = getattr(old_value, "MOFScriptModel_MOFScriptObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_MOFScriptObject"):
                opp_val = getattr(value, "MOFScriptModel_MOFScriptObject", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_MOFScriptObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MOFScriptModel_MOFScriptObject(ABC):

    def __init__(self, line: int, column: int, MOFScriptModel_MOFScriptObject: set["MOFScriptModel_MOFScriptComment"] = None):
        self.line = line
        self.column = column
        self.MOFScriptModel_MOFScriptObject = MOFScriptModel_MOFScriptObject if MOFScriptModel_MOFScriptObject is not None else set()
        
    @property
    def line(self) -> int:
        return self.__line

    @line.setter
    def line(self, line: int):
        self.__line = line

    @property
    def column(self) -> int:
        return self.__column

    @column.setter
    def column(self, column: int):
        self.__column = column

    @property
    def MOFScriptModel_MOFScriptObject(self):
        return self.__MOFScriptModel_MOFScriptObject

    @MOFScriptModel_MOFScriptObject.setter
    def MOFScriptModel_MOFScriptObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_MOFScriptObject__MOFScriptModel_MOFScriptObject", None)
        self.__MOFScriptModel_MOFScriptObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MOFScriptModel_MOFScriptComment"):
                    opp_val = getattr(item, "MOFScriptModel_MOFScriptComment", None)
                    
                    if opp_val == self:
                        setattr(item, "MOFScriptModel_MOFScriptComment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MOFScriptModel_MOFScriptComment"):
                    opp_val = getattr(item, "MOFScriptModel_MOFScriptComment", None)
                    
                    setattr(item, "MOFScriptModel_MOFScriptComment", self)
                    

class MOFScriptModel_StatementBlock:

    def __init__(self, id: str, reference: str, protected: bool, MOFScriptModel_StatementBlock: "MOFScriptModel_MOFScriptStatementOwner" = None, MOFScriptModel_StatementBlock17: set["MOFScriptModel_MOFScriptStatement"] = None):
        self.id = id
        self.reference = reference
        self.protected = protected
        self.MOFScriptModel_StatementBlock = MOFScriptModel_StatementBlock
        self.MOFScriptModel_StatementBlock17 = MOFScriptModel_StatementBlock17 if MOFScriptModel_StatementBlock17 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def protected(self) -> bool:
        return self.__protected

    @protected.setter
    def protected(self, protected: bool):
        self.__protected = protected

    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def MOFScriptModel_StatementBlock(self):
        return self.__MOFScriptModel_StatementBlock

    @MOFScriptModel_StatementBlock.setter
    def MOFScriptModel_StatementBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_StatementBlock__MOFScriptModel_StatementBlock", None)
        self.__MOFScriptModel_StatementBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_MOFScriptStatementOwner11"):
                opp_val = getattr(old_value, "MOFScriptModel_MOFScriptStatementOwner11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_MOFScriptStatementOwner11"):
                opp_val = getattr(value, "MOFScriptModel_MOFScriptStatementOwner11", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_MOFScriptStatementOwner11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MOFScriptModel_StatementBlock17(self):
        return self.__MOFScriptModel_StatementBlock17

    @MOFScriptModel_StatementBlock17.setter
    def MOFScriptModel_StatementBlock17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_StatementBlock__MOFScriptModel_StatementBlock17", None)
        self.__MOFScriptModel_StatementBlock17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MOFScriptModel_MOFScriptStatement"):
                    opp_val = getattr(item, "MOFScriptModel_MOFScriptStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "MOFScriptModel_MOFScriptStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MOFScriptModel_MOFScriptStatement"):
                    opp_val = getattr(item, "MOFScriptModel_MOFScriptStatement", None)
                    
                    setattr(item, "MOFScriptModel_MOFScriptStatement", self)
                    

class MOFScriptStatementOwner:

    pass
class MOFScriptModel_Advice(MOFScriptStatementOwner):

    def __init__(self, name: str, code: str, operator: str, pointCutRef: str, MOFScriptModel_Advice: "MOFScriptModel_MOFScriptAspect" = None, MOFScriptModel_Advice91: "MOFScriptModel_PointCut" = None):
        self.name = name
        self.code = code
        self.operator = operator
        self.pointCutRef = pointCutRef
        self.MOFScriptModel_Advice = MOFScriptModel_Advice
        self.MOFScriptModel_Advice91 = MOFScriptModel_Advice91
        
    @property
    def pointCutRef(self) -> str:
        return self.__pointCutRef

    @pointCutRef.setter
    def pointCutRef(self, pointCutRef: str):
        self.__pointCutRef = pointCutRef

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def MOFScriptModel_Advice(self):
        return self.__MOFScriptModel_Advice

    @MOFScriptModel_Advice.setter
    def MOFScriptModel_Advice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_Advice__MOFScriptModel_Advice", None)
        self.__MOFScriptModel_Advice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_MOFScriptAspect"):
                opp_val = getattr(old_value, "MOFScriptModel_MOFScriptAspect", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_MOFScriptAspect"):
                opp_val = getattr(value, "MOFScriptModel_MOFScriptAspect", None)
                if opp_val is None:
                    setattr(value, "MOFScriptModel_MOFScriptAspect", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MOFScriptModel_Advice91(self):
        return self.__MOFScriptModel_Advice91

    @MOFScriptModel_Advice91.setter
    def MOFScriptModel_Advice91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_Advice__MOFScriptModel_Advice91", None)
        self.__MOFScriptModel_Advice91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_PointCut92"):
                opp_val = getattr(old_value, "MOFScriptModel_PointCut92", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_PointCut92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_PointCut92"):
                opp_val = getattr(value, "MOFScriptModel_PointCut92", None)
                setattr(value, "MOFScriptModel_PointCut92", self)

class MOFScriptModel_MOFScriptStatement(MOFScriptStatementOwner):

    pass
class MOFScriptModel_TransformationRule(MOFScriptStatementOwner):

    def __init__(self, isEntryPoint: bool, name: str, return: str, isAbstract: bool, accessLevel: str, transformationrules: "MOFScriptModel_MOFScriptTransformation" = None, MOFScriptModel_TransformationRule: "MOFScriptModel_TransformationRule" = None, MOFScriptModel_TransformationRule1: "MOFScriptModel_TransformationRule" = None, MOFScriptModel_TransformationRule4: set["MOFScriptModel_MOFScriptParameter"] = None, MOFScriptModel_TransformationRule6: "MOFScriptModel_MOFScriptParameter" = None, TransformationRule: "MOFScriptModel_MOFScriptTransformation" = None, MOFScriptModel_TransformationRule55: "MOFScriptModel_FunctionCall" = None):
        self.isEntryPoint = isEntryPoint
        self.name = name
        self.return = return
        self.isAbstract = isAbstract
        self.accessLevel = accessLevel
        self.transformationrules = transformationrules
        self.MOFScriptModel_TransformationRule = MOFScriptModel_TransformationRule
        self.MOFScriptModel_TransformationRule1 = MOFScriptModel_TransformationRule1
        self.MOFScriptModel_TransformationRule4 = MOFScriptModel_TransformationRule4 if MOFScriptModel_TransformationRule4 is not None else set()
        self.MOFScriptModel_TransformationRule6 = MOFScriptModel_TransformationRule6
        self.TransformationRule = TransformationRule
        self.MOFScriptModel_TransformationRule55 = MOFScriptModel_TransformationRule55
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isEntryPoint(self) -> bool:
        return self.__isEntryPoint

    @isEntryPoint.setter
    def isEntryPoint(self, isEntryPoint: bool):
        self.__isEntryPoint = isEntryPoint

    @property
    def accessLevel(self) -> str:
        return self.__accessLevel

    @accessLevel.setter
    def accessLevel(self, accessLevel: str):
        self.__accessLevel = accessLevel

    @property
    def return(self) -> str:
        return self.__return

    @return.setter
    def return(self, return: str):
        self.__return = return

    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def MOFScriptModel_TransformationRule4(self):
        return self.__MOFScriptModel_TransformationRule4

    @MOFScriptModel_TransformationRule4.setter
    def MOFScriptModel_TransformationRule4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_TransformationRule__MOFScriptModel_TransformationRule4", None)
        self.__MOFScriptModel_TransformationRule4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MOFScriptModel_MOFScriptParameter"):
                    opp_val = getattr(item, "MOFScriptModel_MOFScriptParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "MOFScriptModel_MOFScriptParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MOFScriptModel_MOFScriptParameter"):
                    opp_val = getattr(item, "MOFScriptModel_MOFScriptParameter", None)
                    
                    setattr(item, "MOFScriptModel_MOFScriptParameter", self)
                    

    @property
    def TransformationRule(self):
        return self.__TransformationRule

    @TransformationRule.setter
    def TransformationRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_TransformationRule__TransformationRule", None)
        self.__TransformationRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner30"):
                opp_val = getattr(old_value, "owner30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner30"):
                opp_val = getattr(value, "owner30", None)
                if opp_val is None:
                    setattr(value, "owner30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MOFScriptModel_TransformationRule55(self):
        return self.__MOFScriptModel_TransformationRule55

    @MOFScriptModel_TransformationRule55.setter
    def MOFScriptModel_TransformationRule55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_TransformationRule__MOFScriptModel_TransformationRule55", None)
        self.__MOFScriptModel_TransformationRule55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_FunctionCall54"):
                opp_val = getattr(old_value, "MOFScriptModel_FunctionCall54", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_FunctionCall54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_FunctionCall54"):
                opp_val = getattr(value, "MOFScriptModel_FunctionCall54", None)
                setattr(value, "MOFScriptModel_FunctionCall54", self)

    @property
    def MOFScriptModel_TransformationRule(self):
        return self.__MOFScriptModel_TransformationRule

    @MOFScriptModel_TransformationRule.setter
    def MOFScriptModel_TransformationRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_TransformationRule__MOFScriptModel_TransformationRule", None)
        self.__MOFScriptModel_TransformationRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_TransformationRule1"):
                opp_val = getattr(old_value, "MOFScriptModel_TransformationRule1", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_TransformationRule1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_TransformationRule1"):
                opp_val = getattr(value, "MOFScriptModel_TransformationRule1", None)
                setattr(value, "MOFScriptModel_TransformationRule1", self)

    @property
    def transformationrules(self):
        return self.__transformationrules

    @transformationrules.setter
    def transformationrules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_TransformationRule__transformationrules", None)
        self.__transformationrules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptTransformation"):
                opp_val = getattr(old_value, "MOFScriptTransformation", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptTransformation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptTransformation"):
                opp_val = getattr(value, "MOFScriptTransformation", None)
                setattr(value, "MOFScriptTransformation", self)

    @property
    def MOFScriptModel_TransformationRule1(self):
        return self.__MOFScriptModel_TransformationRule1

    @MOFScriptModel_TransformationRule1.setter
    def MOFScriptModel_TransformationRule1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_TransformationRule__MOFScriptModel_TransformationRule1", None)
        self.__MOFScriptModel_TransformationRule1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_TransformationRule"):
                opp_val = getattr(old_value, "MOFScriptModel_TransformationRule", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_TransformationRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_TransformationRule"):
                opp_val = getattr(value, "MOFScriptModel_TransformationRule", None)
                setattr(value, "MOFScriptModel_TransformationRule", self)

    @property
    def MOFScriptModel_TransformationRule6(self):
        return self.__MOFScriptModel_TransformationRule6

    @MOFScriptModel_TransformationRule6.setter
    def MOFScriptModel_TransformationRule6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MOFScriptModel_TransformationRule__MOFScriptModel_TransformationRule6", None)
        self.__MOFScriptModel_TransformationRule6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MOFScriptModel_MOFScriptParameter7"):
                opp_val = getattr(old_value, "MOFScriptModel_MOFScriptParameter7", None)
                if opp_val == self:
                    setattr(old_value, "MOFScriptModel_MOFScriptParameter7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MOFScriptModel_MOFScriptParameter7"):
                opp_val = getattr(value, "MOFScriptModel_MOFScriptParameter7", None)
                setattr(value, "MOFScriptModel_MOFScriptParameter7", self)
