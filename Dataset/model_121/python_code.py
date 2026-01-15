from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibility(Enum):
    PRIVATE = "PRIVATE"
    PACKAGE = "PACKAGE"
    PROTECTED = "PROTECTED"
    PUBLIC = "PUBLIC"
    ANY = "ANY"
class BooleanOperator(Enum):
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    EQUAL_TO = "EQUAL_TO"
    NOT_EQUAL_TO = "NOT_EQUAL_TO"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    ANY = "ANY"
class EquationOperator(Enum):
    PLUS = "PLUS"
class LogicOperator(Enum):
    AND = "AND"
    OR = "OR"
    IF_THEN = "IF_THEN"
class AssignmentOperator(Enum):
    PLUS_ASSIGN = "PLUS_ASSIGN"
    ASSIGN = "ASSIGN"
    ANY = "ANY"
class ArithmeticOperator(Enum):
    ADDITION = "ADDITION"
    SUBTRACTION = "SUBTRACTION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    MODULUS = "MODULUS"
    UNDEFINED = "UNDEFINED"
class Inheritance(Enum):
    ABSTRACT = "ABSTRACT"
    FINAL = "FINAL"
    NONE = "NONE"
    ANY = "ANY"
class CollectionKind(Enum):
    EXACT = "EXACT"
    SEQUENCE = "SEQUENCE"
    ANY = "ANY"
    IMMEDIATE = "IMMEDIATE"
class UnaryAssignmentOperator(Enum):
    DECREMENT = "DECREMENT"
    INCREMENT = "INCREMENT"
    ANY = "ANY"


############################################
# Definition of Classes
############################################

class CcslNumberFunction:

    pass
class ccsl_numberFunctions_GetIndexOf(CcslNumberFunction):

    pass
class ccsl_numberFunctions_CcslIntegerLiteral(CcslNumberFunction):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class statements_Access:

    pass
class numberFunctions_CcslNumberFunction:

    pass
class ccsl_filters_EquationFilter:

    def __init__(self, operator: str, ccsl_filters_EquationFilter: set["numberFunctions_CcslNumberFunction"] = None, ccsl_filters_EquationFilter171: set["numberFunctions_CcslNumberFunction"] = None):
        self.operator = operator
        self.ccsl_filters_EquationFilter = ccsl_filters_EquationFilter if ccsl_filters_EquationFilter is not None else set()
        self.ccsl_filters_EquationFilter171 = ccsl_filters_EquationFilter171 if ccsl_filters_EquationFilter171 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ccsl_filters_EquationFilter171(self):
        return self.__ccsl_filters_EquationFilter171

    @ccsl_filters_EquationFilter171.setter
    def ccsl_filters_EquationFilter171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_filters_EquationFilter__ccsl_filters_EquationFilter171", None)
        self.__ccsl_filters_EquationFilter171 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "numberFunctions_CcslNumberFunction172"):
                    opp_val = getattr(item, "numberFunctions_CcslNumberFunction172", None)
                    
                    if opp_val == self:
                        setattr(item, "numberFunctions_CcslNumberFunction172", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "numberFunctions_CcslNumberFunction172"):
                    opp_val = getattr(item, "numberFunctions_CcslNumberFunction172", None)
                    
                    setattr(item, "numberFunctions_CcslNumberFunction172", self)
                    

    @property
    def ccsl_filters_EquationFilter(self):
        return self.__ccsl_filters_EquationFilter

    @ccsl_filters_EquationFilter.setter
    def ccsl_filters_EquationFilter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_filters_EquationFilter__ccsl_filters_EquationFilter", None)
        self.__ccsl_filters_EquationFilter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "numberFunctions_CcslNumberFunction"):
                    opp_val = getattr(item, "numberFunctions_CcslNumberFunction", None)
                    
                    if opp_val == self:
                        setattr(item, "numberFunctions_CcslNumberFunction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "numberFunctions_CcslNumberFunction"):
                    opp_val = getattr(item, "numberFunctions_CcslNumberFunction", None)
                    
                    setattr(item, "numberFunctions_CcslNumberFunction", self)
                    

class expressions_OperatorExpression:

    pass
class TemplateFilter:

    pass
class ccsl_filters_ImplicityOperandFilter(TemplateFilter):

    pass
class AtomicFilter:

    pass
class ccsl_filters_ChildClosureComplexTypeFilter(AtomicFilter):

    pass
class ccsl_filters_IsStringFilter(AtomicFilter):

    pass
class ccsl_filters_TemplateFilter(AtomicFilter):

    pass
class ccsl_filters_HasSameReferenceFilter(AtomicFilter):

    pass
class ccsl_filters_SuperClassClosureFilter(AtomicFilter):

    def __init__(self, includesSubClass: str, ccsl_filters_SuperClassClosureFilter: "complexType_JClass" = None, ccsl_filters_SuperClassClosureFilter183: "complexType_JClass" = None, ccsl_filters_SuperClassClosureFilter186: "Context" = None):
        self.includesSubClass = includesSubClass
        self.ccsl_filters_SuperClassClosureFilter = ccsl_filters_SuperClassClosureFilter
        self.ccsl_filters_SuperClassClosureFilter183 = ccsl_filters_SuperClassClosureFilter183
        self.ccsl_filters_SuperClassClosureFilter186 = ccsl_filters_SuperClassClosureFilter186
        
    @property
    def includesSubClass(self) -> str:
        return self.__includesSubClass

    @includesSubClass.setter
    def includesSubClass(self, includesSubClass: str):
        self.__includesSubClass = includesSubClass

    @property
    def ccsl_filters_SuperClassClosureFilter186(self):
        return self.__ccsl_filters_SuperClassClosureFilter186

    @ccsl_filters_SuperClassClosureFilter186.setter
    def ccsl_filters_SuperClassClosureFilter186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_filters_SuperClassClosureFilter__ccsl_filters_SuperClassClosureFilter186", None)
        self.__ccsl_filters_SuperClassClosureFilter186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Context187"):
                opp_val = getattr(old_value, "Context187", None)
                if opp_val == self:
                    setattr(old_value, "Context187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Context187"):
                opp_val = getattr(value, "Context187", None)
                setattr(value, "Context187", self)

    @property
    def ccsl_filters_SuperClassClosureFilter(self):
        return self.__ccsl_filters_SuperClassClosureFilter

    @ccsl_filters_SuperClassClosureFilter.setter
    def ccsl_filters_SuperClassClosureFilter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_filters_SuperClassClosureFilter__ccsl_filters_SuperClassClosureFilter", None)
        self.__ccsl_filters_SuperClassClosureFilter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "complexType_JClass181"):
                opp_val = getattr(old_value, "complexType_JClass181", None)
                if opp_val == self:
                    setattr(old_value, "complexType_JClass181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "complexType_JClass181"):
                opp_val = getattr(value, "complexType_JClass181", None)
                setattr(value, "complexType_JClass181", self)

    @property
    def ccsl_filters_SuperClassClosureFilter183(self):
        return self.__ccsl_filters_SuperClassClosureFilter183

    @ccsl_filters_SuperClassClosureFilter183.setter
    def ccsl_filters_SuperClassClosureFilter183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_filters_SuperClassClosureFilter__ccsl_filters_SuperClassClosureFilter183", None)
        self.__ccsl_filters_SuperClassClosureFilter183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "complexType_JClass184"):
                opp_val = getattr(old_value, "complexType_JClass184", None)
                if opp_val == self:
                    setattr(old_value, "complexType_JClass184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "complexType_JClass184"):
                opp_val = getattr(value, "complexType_JClass184", None)
                setattr(value, "complexType_JClass184", self)

class ccsl_filters_SuperMethodClosureFilter(AtomicFilter):

    pass
class ccsl_filters_BlockLastStatementFilter(AtomicFilter):

    pass
class ccsl_filters_ImplicityContainerFilter(AtomicFilter):

    pass
class ccsl_filters_FromClosureFilter(AtomicFilter):

    pass
class ccsl_filters_IsTypeOfFilter(AtomicFilter):

    pass
class ccsl_filters_IsKindOfFilter(AtomicFilter):

    pass
class ccsl_filters_RegexMatch(AtomicFilter):

    def __init__(self, regex: str):
        self.regex = regex
        
    @property
    def regex(self) -> str:
        return self.__regex

    @regex.setter
    def regex(self, regex: str):
        self.__regex = regex

class ccsl_filters_SameNameFilter(AtomicFilter):

    def __init__(self, ignoreCase: str, ccsl_filters_SameNameFilter: set["namedElements_NamedElement"] = None):
        self.ignoreCase = ignoreCase
        self.ccsl_filters_SameNameFilter = ccsl_filters_SameNameFilter if ccsl_filters_SameNameFilter is not None else set()
        
    @property
    def ignoreCase(self) -> str:
        return self.__ignoreCase

    @ignoreCase.setter
    def ignoreCase(self, ignoreCase: str):
        self.__ignoreCase = ignoreCase

    @property
    def ccsl_filters_SameNameFilter(self):
        return self.__ccsl_filters_SameNameFilter

    @ccsl_filters_SameNameFilter.setter
    def ccsl_filters_SameNameFilter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_filters_SameNameFilter__ccsl_filters_SameNameFilter", None)
        self.__ccsl_filters_SameNameFilter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "namedElements_NamedElement"):
                    opp_val = getattr(item, "namedElements_NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "namedElements_NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "namedElements_NamedElement"):
                    opp_val = getattr(item, "namedElements_NamedElement", None)
                    
                    setattr(item, "namedElements_NamedElement", self)
                    

class ccsl_filters_CountFilter(AtomicFilter):

    def __init__(self, min: str, max: str, ccsl_filters_CountFilter: set["Context"] = None, ccsl_filters_CountFilter130: "Element" = None, ccsl_filters_CountFilter133: "Element" = None):
        self.min = min
        self.max = max
        self.ccsl_filters_CountFilter = ccsl_filters_CountFilter if ccsl_filters_CountFilter is not None else set()
        self.ccsl_filters_CountFilter130 = ccsl_filters_CountFilter130
        self.ccsl_filters_CountFilter133 = ccsl_filters_CountFilter133
        
    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def ccsl_filters_CountFilter133(self):
        return self.__ccsl_filters_CountFilter133

    @ccsl_filters_CountFilter133.setter
    def ccsl_filters_CountFilter133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_filters_CountFilter__ccsl_filters_CountFilter133", None)
        self.__ccsl_filters_CountFilter133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element134"):
                opp_val = getattr(old_value, "Element134", None)
                if opp_val == self:
                    setattr(old_value, "Element134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element134"):
                opp_val = getattr(value, "Element134", None)
                setattr(value, "Element134", self)

    @property
    def ccsl_filters_CountFilter130(self):
        return self.__ccsl_filters_CountFilter130

    @ccsl_filters_CountFilter130.setter
    def ccsl_filters_CountFilter130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_filters_CountFilter__ccsl_filters_CountFilter130", None)
        self.__ccsl_filters_CountFilter130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element131"):
                opp_val = getattr(old_value, "Element131", None)
                if opp_val == self:
                    setattr(old_value, "Element131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element131"):
                opp_val = getattr(value, "Element131", None)
                setattr(value, "Element131", self)

    @property
    def ccsl_filters_CountFilter(self):
        return self.__ccsl_filters_CountFilter

    @ccsl_filters_CountFilter.setter
    def ccsl_filters_CountFilter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_filters_CountFilter__ccsl_filters_CountFilter", None)
        self.__ccsl_filters_CountFilter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Context128"):
                    opp_val = getattr(item, "Context128", None)
                    
                    if opp_val == self:
                        setattr(item, "Context128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Context128"):
                    opp_val = getattr(item, "Context128", None)
                    
                    setattr(item, "Context128", self)
                    

class ccsl_filters_PropertyFilter(AtomicFilter):

    pass
class Filter:

    pass
class ccsl_filters_CompositeFilter(Filter):

    def __init__(self, operator: str, ccsl_filters_CompositeFilter: set["filters_Filter"] = None):
        self.operator = operator
        self.ccsl_filters_CompositeFilter = ccsl_filters_CompositeFilter if ccsl_filters_CompositeFilter is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ccsl_filters_CompositeFilter(self):
        return self.__ccsl_filters_CompositeFilter

    @ccsl_filters_CompositeFilter.setter
    def ccsl_filters_CompositeFilter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_filters_CompositeFilter__ccsl_filters_CompositeFilter", None)
        self.__ccsl_filters_CompositeFilter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "filters_Filter120"):
                    opp_val = getattr(item, "filters_Filter120", None)
                    
                    if opp_val == self:
                        setattr(item, "filters_Filter120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "filters_Filter120"):
                    opp_val = getattr(item, "filters_Filter120", None)
                    
                    setattr(item, "filters_Filter120", self)
                    

class ccsl_filters_AtomicFilter(Filter):

    pass
class CcslBooleanFunction:

    pass
class ccsl_filters_Filter(CcslBooleanFunction):

    def __init__(self, negated: str):
        self.negated = negated
        
    @property
    def negated(self) -> str:
        return self.__negated

    @negated.setter
    def negated(self, negated: str):
        self.__negated = negated

class CcslFunction:

    pass
class ccsl_numberFunctions_CcslNumberFunction(CcslFunction):

    pass
class ccsl_booleanFunctions_CcslBooleanFunction(CcslFunction):

    pass
class ccsl_functions_CcslFunction(ABC):

    pass
class ccsl_action_ArithmeticOperatorMap:

    def __init__(self, oldArithmeticOperator: str, newArithmeticOperator: str):
        self.oldArithmeticOperator = oldArithmeticOperator
        self.newArithmeticOperator = newArithmeticOperator
        
    @property
    def newArithmeticOperator(self) -> str:
        return self.__newArithmeticOperator

    @newArithmeticOperator.setter
    def newArithmeticOperator(self, newArithmeticOperator: str):
        self.__newArithmeticOperator = newArithmeticOperator

    @property
    def oldArithmeticOperator(self) -> str:
        return self.__oldArithmeticOperator

    @oldArithmeticOperator.setter
    def oldArithmeticOperator(self, oldArithmeticOperator: str):
        self.__oldArithmeticOperator = oldArithmeticOperator

class action_ArithmeticOperatorMap:

    pass
class ccsl_faultTypeDescription_InjectionStrategy(ABC):

    pass
class DataType:

    pass
class ccsl_datatype_PrimitiveType(DataType):

    pass
class ccsl_faultTypeDescription_InjectionAction(ABC):

    pass
class filters_Filter:

    pass
class ccsl_context_Context:

    pass
class ObjectType:

    pass
class ccsl_datatype_ArrayType(ObjectType):

    def __init__(self, dimensions: str, ccsl_datatype_ArrayType: "datatype_DataType" = None):
        self.dimensions = dimensions
        self.ccsl_datatype_ArrayType = ccsl_datatype_ArrayType
        
    @property
    def dimensions(self) -> str:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: str):
        self.__dimensions = dimensions

    @property
    def ccsl_datatype_ArrayType(self):
        return self.__ccsl_datatype_ArrayType

    @ccsl_datatype_ArrayType.setter
    def ccsl_datatype_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_datatype_ArrayType__ccsl_datatype_ArrayType", None)
        self.__ccsl_datatype_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype_DataType109"):
                opp_val = getattr(old_value, "datatype_DataType109", None)
                if opp_val == self:
                    setattr(old_value, "datatype_DataType109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype_DataType109"):
                opp_val = getattr(value, "datatype_DataType109", None)
                setattr(value, "datatype_DataType109", self)

class ccsl_datatype_ParameterizedType(ObjectType):

    pass
class ccsl_datatype_ObjectType(DataType):

    pass
class PrimitiveType:

    pass
class ccsl_datatype_ShortPrimitiveType(PrimitiveType):

    pass
class ccsl_datatype_VoidType(PrimitiveType):

    pass
class ccsl_datatype_IntPrimitiveType(PrimitiveType):

    pass
class ccsl_datatype_BooleanPrimitiveType(PrimitiveType):

    pass
class ccsl_datatype_StringPrimitiveType(PrimitiveType):

    pass
class annotation_Annotation:

    pass
class complexType_AnnotationType:

    pass
class Invocation:

    pass
class ccsl_invocation_SimpleMethodInvocation(Invocation):

    pass
class ccsl_invocation_ConstructorInvocation(Invocation):

    pass
class SimpleMethodInvocation:

    pass
class ccsl_invocation_SuperMethodInvocation(SimpleMethodInvocation):

    pass
class ccsl_invocation_MethodInvocation(SimpleMethodInvocation):

    pass
class UnaryAssignment:

    pass
class ccsl_assignment_PostfixUnaryAssignment(UnaryAssignment):

    pass
class ccsl_assignment_PrefixUnaryAssignment(UnaryAssignment):

    pass
class AbstractAssignment:

    pass
class ccsl_assignment_UnaryAssignment(AbstractAssignment):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class ccsl_assignment_Assignment(AbstractAssignment):

    def __init__(self, operator: str, ccsl_assignment_Assignment: "statements_Statement" = None):
        self.operator = operator
        self.ccsl_assignment_Assignment = ccsl_assignment_Assignment
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ccsl_assignment_Assignment(self):
        return self.__ccsl_assignment_Assignment

    @ccsl_assignment_Assignment.setter
    def ccsl_assignment_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_assignment_Assignment__ccsl_assignment_Assignment", None)
        self.__ccsl_assignment_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statements_Statement91"):
                opp_val = getattr(old_value, "statements_Statement91", None)
                if opp_val == self:
                    setattr(old_value, "statements_Statement91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statements_Statement91"):
                opp_val = getattr(value, "statements_Statement91", None)
                setattr(value, "statements_Statement91", self)

class statements_Block:

    pass
class tryCatch_CatchClause:

    pass
class Block:

    pass
class ccsl_controlFlow_SwitchCaseBlock(Block):

    def __init__(self, default: str):
        self.default = default
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

class controlFlow_SwitchCaseBlock:

    pass
class ControlFlow:

    pass
class ccsl_controlFlow_IfStatement(ControlFlow):

    pass
class ccsl_controlFlow_LoopStatement(ControlFlow):

    pass
class ccsl_controlFlow_SwitchStatement(ControlFlow):

    pass
class LiteralValue:

    pass
class ccsl_literalValues_NumberLiteral(LiteralValue):

    pass
class ccsl_literalValues_StringLiteral(LiteralValue):

    pass
class ccsl_literalValues_BooleanLiteral(LiteralValue):

    pass
class ccsl_literalValues_CharacterLiteral(LiteralValue):

    pass
class ccsl_literalValues_NullLiteral(LiteralValue):

    pass
class ccsl_statements_ThrowStatement:

    pass
class OperatorExpression:

    pass
class ccsl_expressions_BooleanExpression(OperatorExpression):

    def __init__(self, booleanOperator: str):
        self.booleanOperator = booleanOperator
        
    @property
    def booleanOperator(self) -> str:
        return self.__booleanOperator

    @booleanOperator.setter
    def booleanOperator(self, booleanOperator: str):
        self.__booleanOperator = booleanOperator

class ccsl_expressions_ArithmeticExpression(OperatorExpression):

    def __init__(self, arithmeticOperator: str):
        self.arithmeticOperator = arithmeticOperator
        
    @property
    def arithmeticOperator(self) -> str:
        return self.__arithmeticOperator

    @arithmeticOperator.setter
    def arithmeticOperator(self, arithmeticOperator: str):
        self.__arithmeticOperator = arithmeticOperator

class ccsl_expressions_InfixExpression(OperatorExpression):

    pass
class ccsl_expressions_StringConcatenation(OperatorExpression):

    pass
class Access:

    pass
class ccsl_statements_DataTypeAccess(Access):

    pass
class ccsl_statements_VariableAccess(Access):

    pass
class Statement:

    pass
class ccsl_statements_ReturnStatement(Statement):

    pass
class ccsl_annotation_Annotation(Statement):

    pass
class ccsl_statements_ArrayCreation(Statement):

    pass
class ccsl_expressions_OperatorExpression(Statement):

    pass
class ccsl_import_ImportStatement(Statement):

    pass
class ccsl_assignment_AbstractAssignment(Statement):

    pass
class ccsl_statements_ControlFlow(Statement):

    pass
class ccsl_statements_EmptyStatement(Statement):

    pass
class ccsl_statements_InstanceCreation(Statement):

    def __init__(self, argsKind: str, ccsl_statements_InstanceCreation: "datatype_ObjectType" = None, ccsl_statements_InstanceCreation39: "method_Constructor" = None, ccsl_statements_InstanceCreation42: set["statements_Statement"] = None):
        self.argsKind = argsKind
        self.ccsl_statements_InstanceCreation = ccsl_statements_InstanceCreation
        self.ccsl_statements_InstanceCreation39 = ccsl_statements_InstanceCreation39
        self.ccsl_statements_InstanceCreation42 = ccsl_statements_InstanceCreation42 if ccsl_statements_InstanceCreation42 is not None else set()
        
    @property
    def argsKind(self) -> str:
        return self.__argsKind

    @argsKind.setter
    def argsKind(self, argsKind: str):
        self.__argsKind = argsKind

    @property
    def ccsl_statements_InstanceCreation39(self):
        return self.__ccsl_statements_InstanceCreation39

    @ccsl_statements_InstanceCreation39.setter
    def ccsl_statements_InstanceCreation39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_statements_InstanceCreation__ccsl_statements_InstanceCreation39", None)
        self.__ccsl_statements_InstanceCreation39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "method_Constructor40"):
                opp_val = getattr(old_value, "method_Constructor40", None)
                if opp_val == self:
                    setattr(old_value, "method_Constructor40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "method_Constructor40"):
                opp_val = getattr(value, "method_Constructor40", None)
                setattr(value, "method_Constructor40", self)

    @property
    def ccsl_statements_InstanceCreation42(self):
        return self.__ccsl_statements_InstanceCreation42

    @ccsl_statements_InstanceCreation42.setter
    def ccsl_statements_InstanceCreation42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_statements_InstanceCreation__ccsl_statements_InstanceCreation42", None)
        self.__ccsl_statements_InstanceCreation42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statements_Statement43"):
                    opp_val = getattr(item, "statements_Statement43", None)
                    
                    if opp_val == self:
                        setattr(item, "statements_Statement43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statements_Statement43"):
                    opp_val = getattr(item, "statements_Statement43", None)
                    
                    setattr(item, "statements_Statement43", self)
                    

    @property
    def ccsl_statements_InstanceCreation(self):
        return self.__ccsl_statements_InstanceCreation

    @ccsl_statements_InstanceCreation.setter
    def ccsl_statements_InstanceCreation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_statements_InstanceCreation__ccsl_statements_InstanceCreation", None)
        self.__ccsl_statements_InstanceCreation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype_ObjectType37"):
                opp_val = getattr(old_value, "datatype_ObjectType37", None)
                if opp_val == self:
                    setattr(old_value, "datatype_ObjectType37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype_ObjectType37"):
                opp_val = getattr(value, "datatype_ObjectType37", None)
                setattr(value, "datatype_ObjectType37", self)

class ccsl_statements_VarDeclaration(Statement):

    pass
class ccsl_statements_Block(Statement):

    def __init__(self, statementsKind: str, ccsl_statements_Block: set["statements_Statement"] = None):
        self.statementsKind = statementsKind
        self.ccsl_statements_Block = ccsl_statements_Block if ccsl_statements_Block is not None else set()
        
    @property
    def statementsKind(self) -> str:
        return self.__statementsKind

    @statementsKind.setter
    def statementsKind(self, statementsKind: str):
        self.__statementsKind = statementsKind

    @property
    def ccsl_statements_Block(self):
        return self.__ccsl_statements_Block

    @ccsl_statements_Block.setter
    def ccsl_statements_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_statements_Block__ccsl_statements_Block", None)
        self.__ccsl_statements_Block = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statements_Statement34"):
                    opp_val = getattr(item, "statements_Statement34", None)
                    
                    if opp_val == self:
                        setattr(item, "statements_Statement34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statements_Statement34"):
                    opp_val = getattr(item, "statements_Statement34", None)
                    
                    setattr(item, "statements_Statement34", self)
                    

class ccsl_tryCatch_CatchClause(Statement):

    pass
class ccsl_tryCatch_TryStatement(Statement):

    pass
class ccsl_statements_ContinueStatement(Statement):

    pass
class ccsl_statements_InstanceOf(Statement):

    pass
class ccsl_statements_ThisStatement(Statement):

    pass
class ccsl_invocation_Invocation(Statement):

    def __init__(self, argsKind: str, ccsl_invocation_Invocation: set["statements_Statement"] = None):
        self.argsKind = argsKind
        self.ccsl_invocation_Invocation = ccsl_invocation_Invocation if ccsl_invocation_Invocation is not None else set()
        
    @property
    def argsKind(self) -> str:
        return self.__argsKind

    @argsKind.setter
    def argsKind(self, argsKind: str):
        self.__argsKind = argsKind

    @property
    def ccsl_invocation_Invocation(self):
        return self.__ccsl_invocation_Invocation

    @ccsl_invocation_Invocation.setter
    def ccsl_invocation_Invocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_invocation_Invocation__ccsl_invocation_Invocation", None)
        self.__ccsl_invocation_Invocation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statements_Statement95"):
                    opp_val = getattr(item, "statements_Statement95", None)
                    
                    if opp_val == self:
                        setattr(item, "statements_Statement95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statements_Statement95"):
                    opp_val = getattr(item, "statements_Statement95", None)
                    
                    setattr(item, "statements_Statement95", self)
                    

class ccsl_literalValues_LiteralValue(Statement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ccsl_statements_Access(Statement):

    pass
class ccsl_statements_BreakStatement(Statement):

    pass
class ccsl_expressions_ParenthesizedExpression(Statement):

    pass
class ccsl_statements_SynchronizedBlock(Statement):

    pass
class ccsl_statements_NamedElementAccess(Statement):

    pass
class complexType_JClass:

    pass
class method_Constructor:

    pass
class method_SimpleMethod:

    pass
class variable_ParameterVariable:

    pass
class elements_Element:

    pass
class SimpleMethod:

    pass
class ccsl_method_Constructor(SimpleMethod):

    def __init__(self, avaliableInSourceCode: str):
        self.avaliableInSourceCode = avaliableInSourceCode
        
    @property
    def avaliableInSourceCode(self) -> str:
        return self.__avaliableInSourceCode

    @avaliableInSourceCode.setter
    def avaliableInSourceCode(self, avaliableInSourceCode: str):
        self.__avaliableInSourceCode = avaliableInSourceCode

class DeclaredType:

    pass
class ccsl_complexType_AnnotationType(DeclaredType):

    pass
class method_Method:

    pass
class variable_FieldVariable:

    pass
class import_ImportStatement:

    pass
class complexType_JInterface:

    pass
class variable_Variable:

    pass
class datatype_ObjectType:

    pass
class ComplexType:

    pass
class ccsl_datatype_GenericType(ComplexType):

    pass
class ccsl_complexType_AnonymousClass(ComplexType):

    pass
class complexType_ComplexType:

    pass
class variable_InitializableVariable:

    pass
class statements_Statement:

    pass
class Variable:

    pass
class ccsl_variable_InitializableVariable(Variable):

    pass
class InitializableVariable:

    pass
class ccsl_variable_LocalVariable(InitializableVariable):

    pass
class annotation_AnnotableElement:

    pass
class ccsl_variable_FieldVariable(variable_InitializableVariable, annotation_AnnotableElement):

    def __init__(self, static: str, visibility: str):
        self.static = static
        self.visibility = visibility
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

class ccsl_method_SimpleMethod(annotation_AnnotableElement, elements_Element):

    def __init__(self, visibility: str, paramsKind: str, ccsl_method_SimpleMethod: set["variable_ParameterVariable"] = None):
        self.visibility = visibility
        self.paramsKind = paramsKind
        self.ccsl_method_SimpleMethod = ccsl_method_SimpleMethod if ccsl_method_SimpleMethod is not None else set()
        
    @property
    def paramsKind(self) -> str:
        return self.__paramsKind

    @paramsKind.setter
    def paramsKind(self, paramsKind: str):
        self.__paramsKind = paramsKind

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def ccsl_method_SimpleMethod(self):
        return self.__ccsl_method_SimpleMethod

    @ccsl_method_SimpleMethod.setter
    def ccsl_method_SimpleMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_method_SimpleMethod__ccsl_method_SimpleMethod", None)
        self.__ccsl_method_SimpleMethod = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "variable_ParameterVariable"):
                    opp_val = getattr(item, "variable_ParameterVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "variable_ParameterVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "variable_ParameterVariable"):
                    opp_val = getattr(item, "variable_ParameterVariable", None)
                    
                    setattr(item, "variable_ParameterVariable", self)
                    

class ccsl_variable_ParameterVariable(annotation_AnnotableElement, variable_Variable):

    pass
class datatype_DataType:

    pass
class NamedElement:

    pass
class ccsl_variable_Variable(NamedElement):

    def __init__(self, final: str, ccsl_variable_Variable: "datatype_DataType" = None):
        self.final = final
        self.ccsl_variable_Variable = ccsl_variable_Variable
        
    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def ccsl_variable_Variable(self):
        return self.__ccsl_variable_Variable

    @ccsl_variable_Variable.setter
    def ccsl_variable_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_variable_Variable__ccsl_variable_Variable", None)
        self.__ccsl_variable_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype_DataType"):
                opp_val = getattr(old_value, "datatype_DataType", None)
                if opp_val == self:
                    setattr(old_value, "datatype_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype_DataType"):
                opp_val = getattr(value, "datatype_DataType", None)
                setattr(value, "datatype_DataType", self)

class complexType_DeclaredType:

    pass
class ccsl_complexType_JClass(annotation_AnnotableElement, complexType_DeclaredType, complexType_ComplexType):

    def __init__(self, inheritance: str, ccsl_complexType_JClass: set["method_Constructor"] = None, ccsl_complexType_JClass16: "complexType_JClass" = None, complexType_DeclaredType107: "ccsl_datatype_ParameterizedType", complexType_DeclaredType: "ccsl_namedElements_Package", complexType_DeclaredType22: "ccsl_complexType_DeclaredType", complexType_ComplexType165: "ccsl_filters_ChildClosureComplexTypeFilter", complexType_ComplexType: "ccsl_filters_ChildClosureComplexTypeFilter"):
        self.inheritance = inheritance
        self.ccsl_complexType_JClass = ccsl_complexType_JClass if ccsl_complexType_JClass is not None else set()
        self.ccsl_complexType_JClass16 = ccsl_complexType_JClass16
        
    @property
    def inheritance(self) -> str:
        return self.__inheritance

    @inheritance.setter
    def inheritance(self, inheritance: str):
        self.__inheritance = inheritance

    @property
    def ccsl_complexType_JClass16(self):
        return self.__ccsl_complexType_JClass16

    @ccsl_complexType_JClass16.setter
    def ccsl_complexType_JClass16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_complexType_JClass__ccsl_complexType_JClass16", None)
        self.__ccsl_complexType_JClass16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "complexType_JClass"):
                opp_val = getattr(old_value, "complexType_JClass", None)
                if opp_val == self:
                    setattr(old_value, "complexType_JClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "complexType_JClass"):
                opp_val = getattr(value, "complexType_JClass", None)
                setattr(value, "complexType_JClass", self)

    @property
    def ccsl_complexType_JClass(self):
        return self.__ccsl_complexType_JClass

    @ccsl_complexType_JClass.setter
    def ccsl_complexType_JClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_complexType_JClass__ccsl_complexType_JClass", None)
        self.__ccsl_complexType_JClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "method_Constructor"):
                    opp_val = getattr(item, "method_Constructor", None)
                    
                    if opp_val == self:
                        setattr(item, "method_Constructor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "method_Constructor"):
                    opp_val = getattr(item, "method_Constructor", None)
                    
                    setattr(item, "method_Constructor", self)
                    

class ccsl_complexType_JInterface(annotation_AnnotableElement, complexType_DeclaredType, complexType_ComplexType):

    pass
class import_ImportableElement:

    pass
class namedElements_NamedElement:

    pass
class ccsl_method_Method(method_SimpleMethod, namedElements_NamedElement):

    def __init__(self, abstract: str, final: str, static: str, inheritance: str, ccsl_method_Method: "datatype_DataType" = None, namedElements_NamedElement: "ccsl_filters_SameNameFilter"):
        self.abstract = abstract
        self.final = final
        self.static = static
        self.inheritance = inheritance
        self.ccsl_method_Method = ccsl_method_Method
        
    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def inheritance(self) -> str:
        return self.__inheritance

    @inheritance.setter
    def inheritance(self, inheritance: str):
        self.__inheritance = inheritance

    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract

    @property
    def ccsl_method_Method(self):
        return self.__ccsl_method_Method

    @ccsl_method_Method.setter
    def ccsl_method_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_method_Method__ccsl_method_Method", None)
        self.__ccsl_method_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype_DataType28"):
                opp_val = getattr(old_value, "datatype_DataType28", None)
                if opp_val == self:
                    setattr(old_value, "datatype_DataType28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype_DataType28"):
                opp_val = getattr(value, "datatype_DataType28", None)
                setattr(value, "datatype_DataType28", self)

class ccsl_complexType_DeclaredType(datatype_ObjectType, namedElements_NamedElement, import_ImportableElement):

    def __init__(self, visibility: str, static: str, ccsl_complexType_DeclaredType: set["complexType_JInterface"] = None, ccsl_complexType_DeclaredType19: set["import_ImportStatement"] = None, ccsl_complexType_DeclaredType21: set["complexType_DeclaredType"] = None, namedElements_NamedElement: "ccsl_filters_SameNameFilter", import_ImportableElement: "ccsl_import_ImportStatement", datatype_ObjectType50: "ccsl_statements_ArrayCreation", datatype_ObjectType37: "ccsl_statements_InstanceCreation", datatype_ObjectType: "ccsl_complexType_AnonymousClass", datatype_ObjectType104: "ccsl_datatype_ParameterizedType"):
        self.visibility = visibility
        self.static = static
        self.ccsl_complexType_DeclaredType = ccsl_complexType_DeclaredType if ccsl_complexType_DeclaredType is not None else set()
        self.ccsl_complexType_DeclaredType19 = ccsl_complexType_DeclaredType19 if ccsl_complexType_DeclaredType19 is not None else set()
        self.ccsl_complexType_DeclaredType21 = ccsl_complexType_DeclaredType21 if ccsl_complexType_DeclaredType21 is not None else set()
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def ccsl_complexType_DeclaredType21(self):
        return self.__ccsl_complexType_DeclaredType21

    @ccsl_complexType_DeclaredType21.setter
    def ccsl_complexType_DeclaredType21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_complexType_DeclaredType__ccsl_complexType_DeclaredType21", None)
        self.__ccsl_complexType_DeclaredType21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "complexType_DeclaredType22"):
                    opp_val = getattr(item, "complexType_DeclaredType22", None)
                    
                    if opp_val == self:
                        setattr(item, "complexType_DeclaredType22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "complexType_DeclaredType22"):
                    opp_val = getattr(item, "complexType_DeclaredType22", None)
                    
                    setattr(item, "complexType_DeclaredType22", self)
                    

    @property
    def ccsl_complexType_DeclaredType(self):
        return self.__ccsl_complexType_DeclaredType

    @ccsl_complexType_DeclaredType.setter
    def ccsl_complexType_DeclaredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_complexType_DeclaredType__ccsl_complexType_DeclaredType", None)
        self.__ccsl_complexType_DeclaredType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "complexType_JInterface"):
                    opp_val = getattr(item, "complexType_JInterface", None)
                    
                    if opp_val == self:
                        setattr(item, "complexType_JInterface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "complexType_JInterface"):
                    opp_val = getattr(item, "complexType_JInterface", None)
                    
                    setattr(item, "complexType_JInterface", self)
                    

    @property
    def ccsl_complexType_DeclaredType19(self):
        return self.__ccsl_complexType_DeclaredType19

    @ccsl_complexType_DeclaredType19.setter
    def ccsl_complexType_DeclaredType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_complexType_DeclaredType__ccsl_complexType_DeclaredType19", None)
        self.__ccsl_complexType_DeclaredType19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "import_ImportStatement"):
                    opp_val = getattr(item, "import_ImportStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "import_ImportStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "import_ImportStatement"):
                    opp_val = getattr(item, "import_ImportStatement", None)
                    
                    setattr(item, "import_ImportStatement", self)
                    

class ccsl_namedElements_Package(namedElements_NamedElement, import_ImportableElement):

    pass
class ccsl_elements_Element:

    def __init__(self, uniqueName: str):
        self.uniqueName = uniqueName
        
    @property
    def uniqueName(self) -> str:
        return self.__uniqueName

    @uniqueName.setter
    def uniqueName(self, uniqueName: str):
        self.__uniqueName = uniqueName

class InjectionStrategy:

    pass
class ccsl_strategy_AllStrategy(InjectionStrategy):

    pass
class InjectionAction:

    pass
class ccsl_action_ChangeLiteralValueAction(InjectionAction):

    pass
class ccsl_action_DeleteRandomStatementAction(InjectionAction):

    pass
class ccsl_action_ReplaceVariableAccessAction(InjectionAction):

    pass
class ccsl_action_MoveScopeUpAction(InjectionAction):

    pass
class ccsl_action_DeleteAction(InjectionAction):

    pass
class ccsl_action_DeleteInfixOperatorAction(InjectionAction):

    pass
class ccsl_action_ReplaceArithmeticOperatorAction(InjectionAction):

    pass
class ccsl_Root(ABC):

    pass
class Context:

    pass
class Element:

    pass
class ccsl_complexType_ComplexType(Element):

    pass
class ccsl_namedElements_NamedElement(Element):

    def __init__(self, name: str, avaliableInSourceCode: str, Element140: "ccsl_filters_ImplicityContainerFilter", Element131: "ccsl_filters_CountFilter", Element118: "ccsl_filters_AtomicFilter", Element115: "ccsl_faultTypeDescription_InjectionAction", Element143: "ccsl_filters_ImplicityContainerFilter", Element111: "ccsl_context_Context", Element45: "ccsl_statements_Access", Element122: "ccsl_filters_TemplateFilter", Element197: "ccsl_numberFunctions_GetIndexOf", Element194: "ccsl_numberFunctions_GetIndexOf", Element136: "ccsl_filters_ImplicityOperandFilter", Element134: "ccsl_filters_CountFilter", Element: "ccsl_AtomicRule"):
        self.name = name
        self.avaliableInSourceCode = avaliableInSourceCode
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def avaliableInSourceCode(self) -> str:
        return self.__avaliableInSourceCode

    @avaliableInSourceCode.setter
    def avaliableInSourceCode(self, avaliableInSourceCode: str):
        self.__avaliableInSourceCode = avaliableInSourceCode

class ccsl_datatype_DataType(Element):

    pass
class ccsl_statements_Statement(Element):

    pass
class ccsl_import_ImportableElement(Element):

    pass
class ccsl_annotation_AnnotableElement(Element):

    def __init__(self, annotationsKind: str, ccsl_annotation_AnnotableElement: set["annotation_Annotation"] = None, Element140: "ccsl_filters_ImplicityContainerFilter", Element131: "ccsl_filters_CountFilter", Element118: "ccsl_filters_AtomicFilter", Element115: "ccsl_faultTypeDescription_InjectionAction", Element143: "ccsl_filters_ImplicityContainerFilter", Element111: "ccsl_context_Context", Element45: "ccsl_statements_Access", Element122: "ccsl_filters_TemplateFilter", Element197: "ccsl_numberFunctions_GetIndexOf", Element194: "ccsl_numberFunctions_GetIndexOf", Element136: "ccsl_filters_ImplicityOperandFilter", Element134: "ccsl_filters_CountFilter", Element: "ccsl_AtomicRule"):
        self.annotationsKind = annotationsKind
        self.ccsl_annotation_AnnotableElement = ccsl_annotation_AnnotableElement if ccsl_annotation_AnnotableElement is not None else set()
        
    @property
    def annotationsKind(self) -> str:
        return self.__annotationsKind

    @annotationsKind.setter
    def annotationsKind(self, annotationsKind: str):
        self.__annotationsKind = annotationsKind

    @property
    def ccsl_annotation_AnnotableElement(self):
        return self.__ccsl_annotation_AnnotableElement

    @ccsl_annotation_AnnotableElement.setter
    def ccsl_annotation_AnnotableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_annotation_AnnotableElement__ccsl_annotation_AnnotableElement", None)
        self.__ccsl_annotation_AnnotableElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "annotation_Annotation"):
                    opp_val = getattr(item, "annotation_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "annotation_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "annotation_Annotation"):
                    opp_val = getattr(item, "annotation_Annotation", None)
                    
                    setattr(item, "annotation_Annotation", self)
                    

class Rule:

    pass
class ccsl_AtomicRule(Rule):

    pass
class ccsl_CompositeRule(Rule):

    def __init__(self, operator: str, ccsl_CompositeRule: set["ccsl_Rule"] = None):
        self.operator = operator
        self.ccsl_CompositeRule = ccsl_CompositeRule if ccsl_CompositeRule is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ccsl_CompositeRule(self):
        return self.__ccsl_CompositeRule

    @ccsl_CompositeRule.setter
    def ccsl_CompositeRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_CompositeRule__ccsl_CompositeRule", None)
        self.__ccsl_CompositeRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccsl_Rule"):
                    opp_val = getattr(item, "ccsl_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "ccsl_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccsl_Rule"):
                    opp_val = getattr(item, "ccsl_Rule", None)
                    
                    setattr(item, "ccsl_Rule", self)
                    

class Root:

    pass
class ccsl_FaultTypeDescription(Root):

    def __init__(self, name: str, ccsl_FaultTypeDescription: "ccsl_AtomicRule" = None, ccsl_FaultTypeDescription7: set["InjectionAction"] = None, ccsl_FaultTypeDescription9: "InjectionStrategy" = None):
        self.name = name
        self.ccsl_FaultTypeDescription = ccsl_FaultTypeDescription
        self.ccsl_FaultTypeDescription7 = ccsl_FaultTypeDescription7 if ccsl_FaultTypeDescription7 is not None else set()
        self.ccsl_FaultTypeDescription9 = ccsl_FaultTypeDescription9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ccsl_FaultTypeDescription7(self):
        return self.__ccsl_FaultTypeDescription7

    @ccsl_FaultTypeDescription7.setter
    def ccsl_FaultTypeDescription7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_FaultTypeDescription__ccsl_FaultTypeDescription7", None)
        self.__ccsl_FaultTypeDescription7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InjectionAction"):
                    opp_val = getattr(item, "InjectionAction", None)
                    
                    if opp_val == self:
                        setattr(item, "InjectionAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InjectionAction"):
                    opp_val = getattr(item, "InjectionAction", None)
                    
                    setattr(item, "InjectionAction", self)
                    

    @property
    def ccsl_FaultTypeDescription(self):
        return self.__ccsl_FaultTypeDescription

    @ccsl_FaultTypeDescription.setter
    def ccsl_FaultTypeDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_FaultTypeDescription__ccsl_FaultTypeDescription", None)
        self.__ccsl_FaultTypeDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccsl_AtomicRule5"):
                opp_val = getattr(old_value, "ccsl_AtomicRule5", None)
                if opp_val == self:
                    setattr(old_value, "ccsl_AtomicRule5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccsl_AtomicRule5"):
                opp_val = getattr(value, "ccsl_AtomicRule5", None)
                setattr(value, "ccsl_AtomicRule5", self)

    @property
    def ccsl_FaultTypeDescription9(self):
        return self.__ccsl_FaultTypeDescription9

    @ccsl_FaultTypeDescription9.setter
    def ccsl_FaultTypeDescription9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_FaultTypeDescription__ccsl_FaultTypeDescription9", None)
        self.__ccsl_FaultTypeDescription9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InjectionStrategy"):
                opp_val = getattr(old_value, "InjectionStrategy", None)
                if opp_val == self:
                    setattr(old_value, "InjectionStrategy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InjectionStrategy"):
                opp_val = getattr(value, "InjectionStrategy", None)
                setattr(value, "InjectionStrategy", self)

class ccsl_Rule(Root):

    def __init__(self, negated: str, ccsl_Rule: "ccsl_CompositeRule" = None):
        self.negated = negated
        self.ccsl_Rule = ccsl_Rule
        
    @property
    def negated(self) -> str:
        return self.__negated

    @negated.setter
    def negated(self, negated: str):
        self.__negated = negated

    @property
    def ccsl_Rule(self):
        return self.__ccsl_Rule

    @ccsl_Rule.setter
    def ccsl_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccsl_Rule__ccsl_Rule", None)
        self.__ccsl_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccsl_CompositeRule"):
                opp_val = getattr(old_value, "ccsl_CompositeRule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccsl_CompositeRule"):
                opp_val = getattr(value, "ccsl_CompositeRule", None)
                if opp_val is None:
                    setattr(value, "ccsl_CompositeRule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
