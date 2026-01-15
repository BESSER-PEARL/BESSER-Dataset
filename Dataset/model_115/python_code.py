from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ShiftOperator:

    pass
class c_sharp_operators_UnsignedRightShift(ShiftOperator):

    pass
class c_sharp_operators_RightShift(ShiftOperator):

    pass
class c_sharp_operators_LeftShift(ShiftOperator):

    pass
class UnaryModificationOperator:

    pass
class c_sharp_operators_PlusPlus(UnaryModificationOperator):

    pass
class c_sharp_operators_MinusMinus(UnaryModificationOperator):

    pass
class UnaryOperator:

    pass
class c_sharp_operators_And(UnaryOperator):

    pass
class c_sharp_operators_ConditionalOr(UnaryOperator):

    pass
class c_sharp_operators_Negate(UnaryOperator):

    pass
class c_sharp_operators_ConditionalAnd(UnaryOperator):

    pass
class c_sharp_operators_InclusiveOr(UnaryOperator):

    pass
class c_sharp_operators_ExclusiveOr(UnaryOperator):

    pass
class c_sharp_operators_Complement(UnaryOperator):

    pass
class Operator:

    pass
class c_sharp_operators_AssignmentOperator(Operator):

    pass
class c_sharp_operators_EqualityOperator(Operator):

    pass
class c_sharp_operators_RelationOperator(Operator):

    pass
class c_sharp_operators_MultiplicativeOperator(Operator):

    pass
class c_sharp_operators_UnaryOperator(Operator):

    pass
class c_sharp_operators_ShiftOperator(Operator):

    pass
class c_sharp_operators_UnaryModificationOperator(Operator):

    pass
class c_sharp_operators_AdditiveOperator(Operator):

    pass
class c_sharp_operators_Operator(ABC):

    pass
class c_sharp_keywords_Event:

    pass
class c_sharp_keywords_Return:

    pass
class c_sharp_keywords_Default:

    pass
class c_sharp_keywords_Case:

    pass
class c_sharp_keywords_Params:

    pass
class c_sharp_keywords_Ref:

    pass
class c_sharp_keywords_Out:

    pass
class MultiplicativeOperator:

    pass
class c_sharp_operators_Multiplication(MultiplicativeOperator):

    pass
class c_sharp_operators_Remainder(MultiplicativeOperator):

    pass
class c_sharp_operators_Division(MultiplicativeOperator):

    pass
class operators_UnaryOperator:

    pass
class operators_AdditiveOperator:

    pass
class c_sharp_operators_Subtraction(operators_UnaryOperator, operators_AdditiveOperator):

    pass
class c_sharp_operators_Addition(operators_UnaryOperator, operators_AdditiveOperator):

    pass
class RelationOperator:

    pass
class c_sharp_operators_LessThan(RelationOperator):

    pass
class c_sharp_operators_GreaterThanOrEqual(RelationOperator):

    pass
class c_sharp_operators_LessThanOrEqual(RelationOperator):

    pass
class c_sharp_operators_GreaterThan(RelationOperator):

    pass
class EqualityOperator:

    pass
class c_sharp_operators_NotEqual(EqualityOperator):

    pass
class c_sharp_operators_Equal(EqualityOperator):

    pass
class Literal:

    pass
class c_sharp_literals_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class c_sharp_literals_BooleanLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class c_sharp_modifiers_Modifier(ABC):

    pass
class c_sharp_literals_CharacterLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class c_sharp_literals_This(Literal):

    pass
class c_sharp_literals_NullLiteral(Literal):

    pass
class c_sharp_literals_RealLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class c_sharp_literals_HexadecimalIntegerLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class c_sharp_literals_DecimalIntegerLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class types_Type:

    pass
class types_NonArrayType:

    pass
class c_sharp_types_SimpleType(types_NonArrayType, types_Type):

    pass
class c_sharp_types_ReferenceType(types_NonArrayType, types_Type):

    pass
class c_sharp_types_NonArrayType(ABC):

    pass
class c_sharp_types_PointerType(types_NonArrayType, types_Type):

    pass
class ReferenceType:

    pass
class c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType(ReferenceType):

    pass
class InclusiveOrExpression:

    pass
class c_sharp_expressions_ConditionalAndExpression:

    pass
class InclusiveOr:

    pass
class ExclusiveOrExpression:

    pass
class c_sharp_expressions_InclusiveOrExpression:

    pass
class ExclusiveOr:

    pass
class AndExpression:

    pass
class c_sharp_expressions_ExclusiveOrExpression:

    pass
class And:

    pass
class EqualityExpression:

    pass
class c_sharp_expressions_AndExpression:

    pass
class NotEqual:

    pass
class c_sharp_types_Type(ABC):

    pass
class ConditionalOr:

    pass
class ConditionalAndExpression:

    pass
class c_sharp_expressions_ConditionalOrExpression:

    pass
class ConditionalAnd:

    pass
class GreaterThanOrEqual:

    pass
class GreaterThan:

    pass
class LessThanOrEqual:

    pass
class LessThan:

    pass
class ShiftExpression:

    pass
class c_sharp_expressions_RelationalExpression:

    pass
class Equal:

    pass
class RelationalExpression:

    pass
class c_sharp_expressions_EqualityExpression:

    pass
class RightShift:

    pass
class c_sharp_expressions_ShiftExpression:

    pass
class MultiplicativeExpression:

    pass
class c_sharp_expressions_AdditiveExpression:

    pass
class AdditiveExpression:

    pass
class c_sharp_expressions_AddressOfExpression:

    pass
class LeftShift:

    pass
class c_sharp_expressions_CastExpression:

    pass
class Remainder:

    pass
class Division:

    pass
class c_sharp_expressions_MultiplicativeExpression:

    pass
class AssignmentOperator:

    pass
class c_sharp_operators_AssignmentLeftShift(AssignmentOperator):

    pass
class c_sharp_operators_AssignmentMinus(AssignmentOperator):

    pass
class c_sharp_operators_AssignmentDivision(AssignmentOperator):

    pass
class c_sharp_operators_AssignmentAnd(AssignmentOperator):

    pass
class c_sharp_operators_AssignmentExclusiveOr(AssignmentOperator):

    pass
class c_sharp_operators_Assignment(AssignmentOperator):

    pass
class c_sharp_operators_AssignmentModulo(AssignmentOperator):

    pass
class c_sharp_operators_AssignmentRightShift(AssignmentOperator):

    pass
class c_sharp_operators_AssignmentPlus(AssignmentOperator):

    pass
class c_sharp_operators_AssignmentMultiplication(AssignmentOperator):

    pass
class c_sharp_operators_AssignmentOr(AssignmentOperator):

    pass
class c_sharp_operators_AssignmentUnsignedRightShift(AssignmentOperator):

    pass
class expressions_Expression:

    pass
class PreDecrementExpression:

    pass
class PreIncrementExpression:

    pass
class UnaryExpression:

    pass
class Multiplication:

    pass
class Complement:

    pass
class Negate:

    pass
class Subtraction:

    pass
class Addition:

    pass
class ConditionalOrExpression:

    pass
class AddressOfExpression:

    pass
class CastExpression:

    pass
class MemberAccess:

    pass
class c_sharp_expressions_UnaryExpression:

    pass
class ArrayInitializer:

    pass
class SimpleType:

    pass
class c_sharp_types_SByte(SimpleType):

    pass
class c_sharp_types_Object(SimpleType):

    pass
class c_sharp_types_Bool(SimpleType):

    pass
class c_sharp_types_Void(SimpleType):

    pass
class c_sharp_types_Double(SimpleType):

    pass
class c_sharp_types_ULong(SimpleType):

    pass
class c_sharp_types_Short(SimpleType):

    pass
class c_sharp_types_Long(SimpleType):

    pass
class c_sharp_types_Byte(SimpleType):

    pass
class c_sharp_types_Int(SimpleType):

    pass
class c_sharp_types_String(SimpleType):

    pass
class c_sharp_types_Float(SimpleType):

    pass
class c_sharp_types_Char(SimpleType):

    pass
class c_sharp_types_UShort(SimpleType):

    pass
class c_sharp_types_UInt(SimpleType):

    pass
class c_sharp_types_Decimal(SimpleType):

    pass
class PrimaryExtendedExpressionType:

    pass
class c_sharp_expressions_ElementAccess(PrimaryExtendedExpressionType):

    pass
class c_sharp_expressions_MemberAccess(PrimaryExtendedExpressionType):

    pass
class c_sharp_expressions_PrimaryExtendedExpressionType(ABC):

    pass
class PrimaryExpression:

    pass
class c_sharp_expressions_ArrayCreationExpression(PrimaryExpression):

    pass
class c_sharp_expressions_PrimaryNoArrayCreationExpression(PrimaryExpression):

    pass
class c_sharp_expressions_PrimaryExpression(ABC):

    pass
class Argument:

    pass
class c_sharp_expressions_ArgumentList:

    pass
class PrimaryNoArrayCreationExpression:

    pass
class c_sharp_literals_Literal(PrimaryNoArrayCreationExpression):

    pass
class c_sharp_expressions_UncheckedExpression(PrimaryNoArrayCreationExpression):

    pass
class c_sharp_expressions_CheckedExpression(PrimaryNoArrayCreationExpression):

    pass
class c_sharp_expressions_DelegateCreationExpression(PrimaryNoArrayCreationExpression):

    pass
class c_sharp_expressions_SizeOfExpression(PrimaryNoArrayCreationExpression):

    pass
class c_sharp_expressions_TypeOfExpression(PrimaryNoArrayCreationExpression):

    pass
class c_sharp_expressions_ParenthesizedExpression(PrimaryNoArrayCreationExpression):

    pass
class c_sharp_expressions_BaseAccess(PrimaryNoArrayCreationExpression):

    pass
class c_sharp_expressions_PointerMemberAccess(PrimaryExtendedExpressionType):

    pass
class ArgumentList:

    pass
class expressions_StatementExpression:

    pass
class c_sharp_expressions_AssignmentExpression(expressions_Expression, expressions_StatementExpression):

    pass
class expressions_PrimaryExtendedExpressionType:

    pass
class c_sharp_expressions_PostIncrementExpression(expressions_PrimaryExtendedExpressionType, expressions_StatementExpression):

    pass
class c_sharp_expressions_PostDecrementExpression(expressions_PrimaryExtendedExpressionType, expressions_StatementExpression):

    pass
class c_sharp_expressions_InvocationExpression(expressions_PrimaryExtendedExpressionType, expressions_StatementExpression):

    pass
class c_sharp_statements_LocalConstantDeclaration:

    pass
class statements_ResourceAcquisition:

    pass
class statements_ForInitializer:

    pass
class c_sharp_statements_VariableDeclaration(statements_ResourceAcquisition, statements_ForInitializer):

    pass
class c_sharp_expressions_Argument:

    pass
class c_sharp_expressions_ExpressionList:

    pass
class classes_VariableInitializer:

    pass
class c_sharp_expressions_Expression(classes_VariableInitializer, statements_ResourceAcquisition):

    pass
class c_sharp_expressions_StatementExpression(ABC):

    pass
class ResourceAcquisition:

    pass
class c_sharp_statements_ResourceAcquisition(ABC):

    pass
class c_sharp_statements_FixedPointerDeclarator:

    pass
class FixedPointerDeclarator:

    pass
class PointerType:

    pass
class c_sharp_statements_SpecificCatchClause:

    pass
class FinallyClause:

    pass
class GeneralCatchClause:

    pass
class SpecificCatchClause:

    pass
class c_sharp_statements_FinallyClause:

    pass
class c_sharp_statements_GeneralCatchClause:

    pass
class StatementExpressionList:

    pass
class ForInitializer:

    pass
class c_sharp_expressions_StatementExpressionList(ForInitializer):

    pass
class JumpStatement:

    pass
class c_sharp_statements_GotoStatement(JumpStatement):

    pass
class c_sharp_statements_ThrowStatement(JumpStatement):

    pass
class c_sharp_statements_ReturnStatement(JumpStatement):

    pass
class c_sharp_statements_ContinueStatement(JumpStatement):

    pass
class c_sharp_statements_BreakStatement(JumpStatement):

    pass
class c_sharp_statements_ForInitializer(ABC):

    pass
class Default:

    pass
class c_sharp_statements_SwitchLabel:

    pass
class SwitchLabel:

    pass
class c_sharp_statements_SwitchSection:

    pass
class SwitchSection:

    pass
class SelectionStatement:

    pass
class c_sharp_statements_SwitchStatement(SelectionStatement):

    pass
class c_sharp_statements_IfStatement(SelectionStatement):

    pass
class StatementExpression:

    pass
class c_sharp_expressions_PreDecrementExpression(StatementExpression):

    pass
class c_sharp_expressions_PreIncrementExpression(StatementExpression):

    pass
class IterationStatement:

    pass
class c_sharp_statements_ForStatement(IterationStatement):

    pass
class c_sharp_statements_DoStatement(IterationStatement):

    pass
class c_sharp_statements_ForeachStatement(IterationStatement):

    pass
class c_sharp_statements_WhileStatement(IterationStatement):

    pass
class statements_Statement:

    pass
class Case:

    pass
class c_sharp_statements_Statement(ABC):

    pass
class c_sharp_attributes_NamedArgument:

    pass
class NamedArgument:

    pass
class c_sharp_attributes_NamedArgumentList:

    pass
class NamedArgumentList:

    pass
class ExpressionList:

    pass
class c_sharp_attributes_AttributeArguments:

    pass
class AttributeArguments:

    pass
class c_sharp_attributes_Attribute:

    pass
class Unsafe:

    pass
class EmbeddedStatement:

    pass
class c_sharp_statements_IterationStatement(EmbeddedStatement):

    pass
class c_sharp_statements_FixedStatement(EmbeddedStatement):

    pass
class c_sharp_statements_TryStatement(EmbeddedStatement):

    pass
class c_sharp_statements_EmptyStatement(EmbeddedStatement):

    pass
class c_sharp_statements_JumpStatement(EmbeddedStatement):

    pass
class c_sharp_statements_UncheckedStatement(EmbeddedStatement):

    pass
class c_sharp_statements_CheckedStatement(EmbeddedStatement):

    pass
class c_sharp_statements_UsingStatement(EmbeddedStatement):

    pass
class c_sharp_statements_SelectionStatement(EmbeddedStatement):

    pass
class c_sharp_statements_ExpressionStatement(EmbeddedStatement):

    pass
class c_sharp_statements_LockStatement(EmbeddedStatement):

    pass
class c_sharp_statements_SimpleEmbeddedStatement(EmbeddedStatement):

    pass
class LocalConstantDeclaration:

    pass
class VariableDeclaration:

    pass
class c_sharp_arrays_RankSpecifier:

    pass
class RankSpecifier:

    pass
class NonArrayType:

    pass
class Expression:

    pass
class c_sharp_expressions_ConditionalExpression(Expression):

    pass
class VariableInitializer:

    pass
class c_sharp_arrays_ArrayInitializer(VariableInitializer):

    pass
class c_sharp_arrays_StackallocInitializer(VariableInitializer):

    pass
class VariableDeclarator:

    pass
class Return:

    pass
class Event:

    pass
class c_sharp_attributes_AttributeTarget:

    pass
class AttributeTarget:

    pass
class c_sharp_attributes_Attributes:

    pass
class c_sharp_attributes_GlobalAttributeTarget:

    pass
class Attribute:

    pass
class GlobalAttributeTarget:

    pass
class c_sharp_attributes_GlobalAttributes:

    pass
class ArrayType:

    pass
class Params:

    pass
class c_sharp_classes_ParameterArray:

    pass
class Out:

    pass
class Ref:

    pass
class c_sharp_classes_FixedParameter:

    pass
class ParameterArray:

    pass
class FixedParameter:

    pass
class c_sharp_classes_FormalParameterList:

    pass
class Block:

    pass
class FormalParameterList:

    pass
class ConstantDeclarator:

    pass
class c_sharp_classes_ClassMemberDeclaration(ABC):

    pass
class c_sharp_classes_VariableInitializer(ABC):

    pass
class Statement:

    pass
class c_sharp_statements_EmbeddedStatement(Statement):

    pass
class c_sharp_statements_DeclarationStatement(Statement):

    pass
class c_sharp_classes_Block:

    pass
class ClassOrInterfaceOrDelegateOrEnumType:

    pass
class c_sharp_classes_ClassBase:

    pass
class ClassMemberDeclaration:

    pass
class c_sharp_classes_FieldDeclaration(ClassMemberDeclaration):

    pass
class c_sharp_classes_ConstantDeclaration(ClassMemberDeclaration):

    pass
class ClassBase:

    pass
class Modifier:

    pass
class c_sharp_modifiers_Partial(Modifier):

    pass
class c_sharp_modifiers_Static(Modifier):

    pass
class c_sharp_modifiers_Volatile(Modifier):

    pass
class c_sharp_modifiers_Internal(Modifier):

    pass
class c_sharp_modifiers_Private(Modifier):

    pass
class c_sharp_modifiers_Sealed(Modifier):

    pass
class c_sharp_modifiers_OverrideModifier(Modifier):

    pass
class c_sharp_modifiers_Virtual(Modifier):

    pass
class c_sharp_modifiers_Public(Modifier):

    pass
class c_sharp_modifiers_ReadOnly(Modifier):

    pass
class c_sharp_modifiers_Protected(Modifier):

    pass
class c_sharp_modifiers_Abstract(Modifier):

    pass
class c_sharp_modifiers_Unsafe(Modifier):

    pass
class c_sharp_modifiers_Extern(Modifier):

    pass
class c_sharp_modifiers_New(Modifier):

    pass
class Attributes:

    pass
class Type:

    pass
class c_sharp_arrays_ArrayType(Type):

    pass
class NamespaceBody:

    pass
class c_sharp_namespaces_NamespaceMemberDeclaration(ABC):

    pass
class NamespaceOrTypeName:

    pass
class NamedElement:

    pass
class c_sharp_statements_ConstantDeclarator(NamedElement):

    pass
class c_sharp_statements_VariableDeclarator(NamedElement):

    pass
class c_sharp_namespaces_UsingDirective(NamedElement):

    pass
class NamespaceMemberDeclaration:

    pass
class c_sharp_namespaces_Namespace(NamespaceMemberDeclaration):

    pass
class GlobalAttributes:

    pass
class UsingDirective:

    pass
class namespaces_TypeDeclaration:

    pass
class c_sharp_namespaces_CompilationUnit:

    pass
class classes_ClassMemberDeclaration:

    pass
class namespaces_NamespaceMemberDeclaration:

    pass
class c_sharp_namespaces_TypeDeclaration(classes_ClassMemberDeclaration, namespaces_NamespaceMemberDeclaration):

    pass
class c_sharp_namespaces_NamespaceBody:

    pass
class c_sharp_common_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class expressions_PrimaryNoArrayCreationExpression:

    pass
class c_sharp_expressions_ObjectCreationExpression(expressions_PrimaryNoArrayCreationExpression, expressions_StatementExpression):

    pass
class common_NamedElement:

    pass
class c_sharp_statements_LabeledStatement(statements_Statement, common_NamedElement):

    pass
class c_sharp_classes_Method(classes_ClassMemberDeclaration, common_NamedElement):

    pass
class c_sharp_classes_Class(namespaces_TypeDeclaration, common_NamedElement):

    pass
class c_sharp_common_Identifier(common_NamedElement, expressions_PrimaryNoArrayCreationExpression):

    pass
class Identifier:

    pass
class c_sharp_common_NamespaceOrTypeName:

    pass