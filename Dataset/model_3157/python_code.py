from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AccessExpression:

    pass
class model_SelectExpression(AccessExpression):

    pass
class model_RecordAccessExpression(AccessExpression):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class ArgumentedElement:

    pass
class model_ArrayAccessExpression(ArgumentedElement, AccessExpression):

    pass
class model_FunctionAccessExpression(ArgumentedElement, AccessExpression):

    pass
class ComparisonExpression:

    pass
class model_GreaterExpression(ComparisonExpression):

    pass
class model_LessEqualExpression(ComparisonExpression):

    pass
class model_LessExpression(ComparisonExpression):

    pass
class model_GreaterEqualExpression(ComparisonExpression):

    pass
class EquivalenceExpression:

    pass
class model_InequalityExpression(EquivalenceExpression):

    pass
class model_EqualityExpression(EquivalenceExpression):

    pass
class PredicateExpression:

    pass
class QuantifierExpression:

    pass
class model_ExistsExpression(QuantifierExpression):

    pass
class model_ForallExpression(QuantifierExpression):

    pass
class BinaryExpression:

    pass
class model_ComparisonExpression(BinaryExpression, PredicateExpression):

    pass
class model_EquivalenceExpression(BinaryExpression, PredicateExpression):

    pass
class model_FieldAssignment:

    def __init__(self, reference: str, model_FieldAssignment: "model_RecordLiteralExpression" = None, model_FieldAssignment49: "model_Expression" = None):
        self.reference = reference
        self.model_FieldAssignment = model_FieldAssignment
        self.model_FieldAssignment49 = model_FieldAssignment49
        
    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def model_FieldAssignment(self):
        return self.__model_FieldAssignment

    @model_FieldAssignment.setter
    def model_FieldAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FieldAssignment__model_FieldAssignment", None)
        self.__model_FieldAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_RecordLiteralExpression"):
                opp_val = getattr(old_value, "model_RecordLiteralExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_RecordLiteralExpression"):
                opp_val = getattr(value, "model_RecordLiteralExpression", None)
                if opp_val is None:
                    setattr(value, "model_RecordLiteralExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_FieldAssignment49(self):
        return self.__model_FieldAssignment49

    @model_FieldAssignment49.setter
    def model_FieldAssignment49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FieldAssignment__model_FieldAssignment49", None)
        self.__model_FieldAssignment49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Expression50"):
                opp_val = getattr(old_value, "model_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "model_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Expression50"):
                opp_val = getattr(value, "model_Expression50", None)
                setattr(value, "model_Expression50", self)

class MultiaryExpression:

    pass
class EnumerableExpression:

    pass
class BooleanLiteralExpression:

    pass
class model_FalseExpression(BooleanLiteralExpression):

    pass
class model_TrueExpression(BooleanLiteralExpression):

    pass
class BooleanExpression:

    pass
class model_OrExpression(MultiaryExpression, BooleanExpression):

    pass
class model_AndExpression(MultiaryExpression, BooleanExpression):

    pass
class model_ImplyExpression(BinaryExpression, BooleanExpression):

    pass
class model_XorExpression(MultiaryExpression, BooleanExpression):

    pass
class ArithmeticLiteralExpression:

    pass
class model_RationalLiteralExpression(ArithmeticLiteralExpression):

    def __init__(self, numerator: str, denominator: str):
        self.numerator = numerator
        self.denominator = denominator
        
    @property
    def denominator(self) -> str:
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator: str):
        self.__denominator = denominator

    @property
    def numerator(self) -> str:
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator: str):
        self.__numerator = numerator

class model_DecimalLiteralExpression(ArithmeticLiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class model_IntegerLiteralExpression(ArithmeticLiteralExpression):

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
class model_AddExpression(MultiaryExpression, ArithmeticExpression):

    pass
class model_DivideExpression(BinaryExpression, ArithmeticExpression):

    pass
class model_DivExpression(BinaryExpression, ArithmeticExpression):

    pass
class model_SubtractExpression(BinaryExpression, ArithmeticExpression):

    pass
class model_MultiplyExpression(MultiaryExpression, ArithmeticExpression):

    pass
class model_ModExpression(BinaryExpression, ArithmeticExpression):

    pass
class LiteralExpression:

    pass
class model_RecordLiteralExpression(LiteralExpression):

    pass
class model_IntegerRangeLiteralExpression(EnumerableExpression, LiteralExpression, BinaryExpression):

    def __init__(self, rightInclusive: bool, leftInclusive: bool):
        self.rightInclusive = rightInclusive
        self.leftInclusive = leftInclusive
        
    @property
    def rightInclusive(self) -> bool:
        return self.__rightInclusive

    @rightInclusive.setter
    def rightInclusive(self, rightInclusive: bool):
        self.__rightInclusive = rightInclusive

    @property
    def leftInclusive(self) -> bool:
        return self.__leftInclusive

    @leftInclusive.setter
    def leftInclusive(self, leftInclusive: bool):
        self.__leftInclusive = leftInclusive

class model_ArrayLiteralExpression(MultiaryExpression, LiteralExpression, EnumerableExpression):

    pass
class UnaryExpression:

    pass
class model_UnaryPlusExpression(UnaryExpression, ArithmeticExpression):

    pass
class model_UnaryMinusExpression(UnaryExpression, ArithmeticExpression):

    pass
class model_NotExpression(UnaryExpression, BooleanExpression):

    pass
class ElseExpression:

    pass
class model_DefaultExpression(ElseExpression):

    pass
class NullaryExpression:

    pass
class model_EnumerationLiteralExpression(NullaryExpression, LiteralExpression):

    pass
class model_ReferenceExpression(NullaryExpression):

    pass
class model_BooleanLiteralExpression(NullaryExpression, LiteralExpression, BooleanExpression):

    pass
class model_ArithmeticLiteralExpression(NullaryExpression, LiteralExpression, ArithmeticExpression):

    pass
class model_OpaqueExpression(NullaryExpression):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class LogicExpression:

    pass
class model_PredicateExpression(LogicExpression):

    pass
class model_ElseExpression(NullaryExpression, LogicExpression):

    pass
class model_BooleanExpression(LogicExpression):

    pass
class Expression:

    pass
class model_UnaryExpression(Expression):

    pass
class model_EnumerableExpression(Expression):

    pass
class model_BinaryExpression(Expression):

    pass
class model_LiteralExpression(Expression):

    pass
class model_ArithmeticExpression(Expression):

    pass
class model_IfThenElseExpression(Expression):

    pass
class model_AccessExpression(Expression):

    pass
class model_LogicExpression(Expression):

    pass
class model_MultiaryExpression(Expression):

    pass
class model_NullaryExpression(Expression):

    pass
class ConstraintDefinition:

    pass
class model_ConstraintDefinition(ABC):

    pass
class EnumerableTypeDefinition:

    pass
class model_ArrayTypeDefinition(EnumerableTypeDefinition):

    pass
class model_IntegerRangeTypeDefinition(EnumerableTypeDefinition):

    pass
class model_EnumerationTypeDefinition(EnumerableTypeDefinition):

    pass
class CompositeTypeDefinition:

    pass
class model_RecordTypeDefinition(CompositeTypeDefinition):

    pass
class model_FunctionTypeDefinition(CompositeTypeDefinition):

    pass
class model_EnumerableTypeDefinition(CompositeTypeDefinition):

    pass
class NumericalTypeDefinition:

    pass
class model_DecimalTypeDefinition(NumericalTypeDefinition):

    pass
class model_RationalTypeDefinition(NumericalTypeDefinition):

    pass
class model_SubrangeTypeDefinition(CompositeTypeDefinition, NumericalTypeDefinition):

    pass
class model_IntegerTypeDefinition(NumericalTypeDefinition):

    pass
class TypeDefinition:

    pass
class model_BooleanTypeDefinition(TypeDefinition):

    pass
class model_CompositeTypeDefinition(TypeDefinition):

    pass
class model_VoidTypeDefinition(TypeDefinition):

    pass
class model_NumericalTypeDefinition(TypeDefinition):

    pass
class Type:

    pass
class model_TypeDefinition(Type):

    pass
class model_TypeReference(Type):

    pass
class FunctionDeclaration:

    pass
class model_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class InitializableElement:

    pass
class model_LambdaDeclaration(InitializableElement, FunctionDeclaration):

    pass
class ValueDeclaration:

    pass
class model_FieldDeclaration(ValueDeclaration):

    pass
class model_VariableDeclaration(InitializableElement, ValueDeclaration):

    pass
class Declaration:

    pass
class model_ValueDeclaration(Declaration):

    pass
class model_Type:

    pass
class model_BasicConstraintDefinition(ConstraintDefinition):

    pass
class model_ConstantDeclaration(InitializableElement, ValueDeclaration):

    pass
class model_TypeDeclaration(Declaration):

    pass
class ParametricElement:

    pass
class model_FunctionDeclaration(ParametricElement, Declaration):

    pass
class model_QuantifierExpression(UnaryExpression, LogicExpression, ParametricElement):

    pass
class NamedElement:

    pass
class model_EnumerationLiteralDefinition(NamedElement):

    pass
class model_Declaration(NamedElement):

    pass
class model_InitializableElement(NamedElement):

    pass
class model_ExpressionPackage(NamedElement, ParametricElement):

    pass
class model_Expression(ABC):

    pass
class model_ArgumentedElement:

    pass
class model_ParameterDeclaration(ValueDeclaration):

    pass
class model_ParametricElement(ABC):

    pass
class model_Comment:

    def __init__(self, comment: str, model_Comment: "model_CommentableElement" = None):
        self.comment = comment
        self.model_Comment = model_Comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def model_Comment(self):
        return self.__model_Comment

    @model_Comment.setter
    def model_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Comment__model_Comment", None)
        self.__model_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CommentableElement"):
                opp_val = getattr(old_value, "model_CommentableElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CommentableElement"):
                opp_val = getattr(value, "model_CommentableElement", None)
                if opp_val is None:
                    setattr(value, "model_CommentableElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_CommentableElement:

    pass