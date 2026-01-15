from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ParametrizedElement:

    pass
class AccessExpression:

    pass
class TTMCConstraint_TupleAccessExpression(AccessExpression):

    def __init__(self, index: str):
        self.index = index
        
    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

class TTMCConstraint_ArrayAccessExpression(ParametrizedElement, AccessExpression):

    pass
class TTMCConstraint_FunctionAccessExpression(ParametrizedElement, AccessExpression):

    pass
class ComparisionExpression:

    pass
class TTMCConstraint_GreaterEqualExpression(ComparisionExpression):

    pass
class TTMCConstraint_LessEqualExpression(ComparisionExpression):

    pass
class TTMCConstraint_LessExpression(ComparisionExpression):

    pass
class TTMCConstraint_GreaterExpression(ComparisionExpression):

    pass
class EquivalenceExpression:

    pass
class TTMCConstraint_InequalityExpression(EquivalenceExpression):

    pass
class TTMCConstraint_EqualityExpression(EquivalenceExpression):

    pass
class TTMCConstraint_RecordAccessExpression(AccessExpression):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class PredicateExpression:

    pass
class TemporalStateExpression:

    pass
class QuantifierExpression:

    pass
class TTMCConstraint_ExistsExpression(QuantifierExpression):

    pass
class TTMCConstraint_ForallExpression(QuantifierExpression):

    pass
class TemporalPathExpression:

    pass
class MultiaryExpression:

    pass
class BinaryExpression:

    pass
class TTMCConstraint_EquivalenceExpression(BinaryExpression, PredicateExpression):

    pass
class TTMCConstraint_UntilExpression(BinaryExpression, TemporalPathExpression):

    pass
class TTMCConstraint_ComparisionExpression(BinaryExpression, PredicateExpression):

    pass
class TTMCConstraint_ReleaseExpression(BinaryExpression, TemporalPathExpression):

    pass
class TTMCConstraint_FieldAssignment:

    def __init__(self, reference: str, TTMCConstraint_FieldAssignment: "TTMCConstraint_RecordLiteralExpression" = None, TTMCConstraint_FieldAssignment58: "TTMCConstraint_Expression" = None):
        self.reference = reference
        self.TTMCConstraint_FieldAssignment = TTMCConstraint_FieldAssignment
        self.TTMCConstraint_FieldAssignment58 = TTMCConstraint_FieldAssignment58
        
    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def TTMCConstraint_FieldAssignment(self):
        return self.__TTMCConstraint_FieldAssignment

    @TTMCConstraint_FieldAssignment.setter
    def TTMCConstraint_FieldAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TTMCConstraint_FieldAssignment__TTMCConstraint_FieldAssignment", None)
        self.__TTMCConstraint_FieldAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TTMCConstraint_RecordLiteralExpression"):
                opp_val = getattr(old_value, "TTMCConstraint_RecordLiteralExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TTMCConstraint_RecordLiteralExpression"):
                opp_val = getattr(value, "TTMCConstraint_RecordLiteralExpression", None)
                if opp_val is None:
                    setattr(value, "TTMCConstraint_RecordLiteralExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TTMCConstraint_FieldAssignment58(self):
        return self.__TTMCConstraint_FieldAssignment58

    @TTMCConstraint_FieldAssignment58.setter
    def TTMCConstraint_FieldAssignment58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TTMCConstraint_FieldAssignment__TTMCConstraint_FieldAssignment58", None)
        self.__TTMCConstraint_FieldAssignment58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TTMCConstraint_Expression59"):
                opp_val = getattr(old_value, "TTMCConstraint_Expression59", None)
                if opp_val == self:
                    setattr(old_value, "TTMCConstraint_Expression59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TTMCConstraint_Expression59"):
                opp_val = getattr(value, "TTMCConstraint_Expression59", None)
                setattr(value, "TTMCConstraint_Expression59", self)

class BooleanLiteralExpression:

    pass
class TTMCConstraint_FalseExpression(BooleanLiteralExpression):

    pass
class TTMCConstraint_TrueExpression(BooleanLiteralExpression):

    pass
class BooleanExpression:

    pass
class TTMCConstraint_ImplyExpression(BinaryExpression, BooleanExpression):

    pass
class TTMCConstraint_EqualExpression(BinaryExpression, BooleanExpression):

    pass
class TTMCConstraint_AndExpression(MultiaryExpression, BooleanExpression):

    pass
class TTMCConstraint_OrExpression(MultiaryExpression, BooleanExpression):

    pass
class ArithmeticLiteralExpression:

    pass
class TTMCConstraint_DecimalLiteralExpression(ArithmeticLiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class TTMCConstraint_RationalLiteralExpression(ArithmeticLiteralExpression):

    def __init__(self, numerator: str, denominator: str):
        self.numerator = numerator
        self.denominator = denominator
        
    @property
    def numerator(self) -> str:
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator: str):
        self.__numerator = numerator

    @property
    def denominator(self) -> str:
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator: str):
        self.__denominator = denominator

class TTMCConstraint_IntegerLiteralExpression(ArithmeticLiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ArithmeticExpression:

    pass
class TTMCConstraint_DivExpression(BinaryExpression, ArithmeticExpression):

    pass
class TTMCConstraint_AddExpression(MultiaryExpression, ArithmeticExpression):

    pass
class TTMCConstraint_ModExpression(BinaryExpression, ArithmeticExpression):

    pass
class TTMCConstraint_DivideExpression(BinaryExpression, ArithmeticExpression):

    pass
class TTMCConstraint_MultiplyExpression(MultiaryExpression, ArithmeticExpression):

    pass
class TTMCConstraint_SubtractExpression(BinaryExpression, ArithmeticExpression):

    pass
class LiteralExpression:

    pass
class TTMCConstraint_TupleLiteralExpression(LiteralExpression):

    pass
class TTMCConstraint_RecordLiteralExpression(LiteralExpression):

    pass
class NullaryExpression:

    pass
class TTMCConstraint_EnumerationLiteralExpression(LiteralExpression, NullaryExpression):

    pass
class TTMCConstraint_BooleanLiteralExpression(LiteralExpression, NullaryExpression, BooleanExpression):

    pass
class TTMCConstraint_ReferenceExpression(NullaryExpression):

    pass
class TTMCConstraint_ArithmeticLiteralExpression(LiteralExpression, NullaryExpression, ArithmeticExpression):

    pass
class TemporalExpression:

    pass
class TTMCConstraint_TemporalStateExpression(TemporalExpression):

    pass
class TTMCConstraint_TemporalPathExpression(TemporalExpression):

    pass
class UnaryExpression:

    pass
class TTMCConstraint_PrimedExpression(UnaryExpression):

    pass
class TTMCConstraint_TemporalForallExpression(UnaryExpression, TemporalStateExpression):

    pass
class TTMCConstraint_NotExpression(UnaryExpression, BooleanExpression):

    pass
class TTMCConstraint_NextExpression(UnaryExpression, TemporalPathExpression):

    pass
class TTMCConstraint_UnaryMinusExpression(UnaryExpression, ArithmeticExpression):

    pass
class TTMCConstraint_FinallyExpression(UnaryExpression, TemporalPathExpression):

    pass
class TTMCConstraint_InExpression(UnaryExpression, PredicateExpression):

    pass
class TTMCConstraint_UnaryPlusExpression(UnaryExpression, ArithmeticExpression):

    pass
class TTMCConstraint_GloballyExpression(UnaryExpression, TemporalPathExpression):

    pass
class TTMCConstraint_TemporalExistsExpression(UnaryExpression, TemporalStateExpression):

    pass
class Expression:

    pass
class TTMCConstraint_PredicateExpression(Expression):

    pass
class TTMCConstraint_TemporalExpression(Expression):

    pass
class TTMCConstraint_LetExpression(Expression):

    pass
class TTMCConstraint_LiteralExpression(Expression):

    pass
class TTMCConstraint_UnaryExpression(Expression):

    pass
class TTMCConstraint_AccessExpression(Expression):

    pass
class TTMCConstraint_ArithmeticExpression(Expression):

    pass
class TTMCConstraint_BinaryExpression(Expression):

    pass
class TTMCConstraint_IfThenElseExpression(Expression):

    pass
class TTMCConstraint_MultiaryExpression(Expression):

    pass
class TTMCConstraint_NullaryExpression(Expression):

    pass
class ConstraintDefinition:

    pass
class TTMCConstraint_ConstraintDefinition(ABC):

    pass
class TTMCConstraint_BooleanExpression(Expression):

    pass
class BasicTypeDefinition:

    pass
class TTMCConstraint_RealTypeDefinition(BasicTypeDefinition):

    pass
class TTMCConstraint_NaturalTypeDefinition(BasicTypeDefinition):

    pass
class TTMCConstraint_BooleanTypeDefinition(BasicTypeDefinition):

    pass
class TTMCConstraint_IntegerTypeDefinition(BasicTypeDefinition):

    pass
class TypeDefinition:

    pass
class TTMCConstraint_ArrayTypeDefinition(TypeDefinition):

    pass
class TTMCConstraint_EnumerationTypeDefinition(TypeDefinition):

    pass
class TTMCConstraint_RecordTypeDefinition(TypeDefinition):

    pass
class TTMCConstraint_TupleTypeDefinition(TypeDefinition):

    pass
class TTMCConstraint_FunctionTypeDefinition(TypeDefinition):

    pass
class TTMCConstraint_SubrangeTypeDefinition(TypeDefinition):

    pass
class TTMCConstraint_BasicTypeDefinition(TypeDefinition):

    pass
class Type:

    pass
class TTMCConstraint_TypeDefinition(Type):

    pass
class TTMCConstraint_TypeReference(Type):

    pass
class DefinableDeclaration:

    pass
class TTMCConstraint_LetDeclaration(DefinableDeclaration):

    pass
class Declaration:

    pass
class TTMCConstraint_FieldDeclaration(Declaration):

    pass
class TTMCConstraint_DefinableDeclaration(Declaration):

    pass
class TTMCConstraint_Type:

    pass
class TTMCConstraint_BasicConstraintDefinition(ConstraintDefinition):

    pass
class TTMCConstraint_ConstantDeclaration(DefinableDeclaration):

    pass
class ParametricElement:

    pass
class TTMCConstraint_QuantifierExpression(UnaryExpression, ParametricElement):

    pass
class TTMCConstraint_ArrayLiteralExpression(UnaryExpression, LiteralExpression, ParametricElement):

    pass
class TTMCConstraint_SubTypeDefinition(TypeDefinition, ParametricElement):

    pass
class TTMCConstraint_FunctionLiteralExpression(UnaryExpression, LiteralExpression, ParametricElement):

    pass
class TTMCConstraint_FunctionDeclaration(DefinableDeclaration, ParametricElement):

    pass
class NamedElement:

    pass
class TTMCConstraint_TypeDeclaration(NamedElement):

    pass
class TTMCConstraint_EnumerationLiteralDefinition(NamedElement):

    pass
class TTMCConstraint_Declaration(NamedElement):

    pass
class TTMCConstraint_ConstraintSpecification(NamedElement, ParametricElement):

    pass
class TTMCConstraint_Expression(ABC):

    pass
class TTMCConstraint_ParametrizedElement:

    pass
class TTMCConstraint_ParameterDeclaration(Declaration):

    pass
class TTMCConstraint_ParametricElement(ABC):

    pass
class TTMCConstraint_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
