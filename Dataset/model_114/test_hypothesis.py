import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ShiftOperator,
    c_sharp_operators_RightShift,
    c_sharp_operators_LeftShift,
    UnaryModificationOperator,
    c_sharp_operators_PlusPlus,
    c_sharp_operators_MinusMinus,
    UnaryOperator,
    c_sharp_operators_Negate,
    c_sharp_operators_Complement,
    MultiplicativeOperator,
    c_sharp_operators_Remainder,
    c_sharp_operators_Multiplication,
    c_sharp_operators_Division,
    operators_UnaryOperator,
    operators_AdditiveOperator,
    c_sharp_operators_Subtraction,
    c_sharp_operators_Addition,
    RelationOperator,
    c_sharp_operators_GreaterThanOrEqual,
    c_sharp_operators_LessThan,
    c_sharp_operators_LessThanOrEqual,
    c_sharp_operators_GreaterThan,
    EqualityOperator,
    c_sharp_operators_NotEqual,
    c_sharp_operators_Equal,
    c_sharp_operators_ConditionalOr,
    c_sharp_operators_ConditionalAnd,
    c_sharp_operators_InclusiveOr,
    c_sharp_operators_ExclusiveOr,
    c_sharp_operators_And,
    c_sharp_operators_UnsignedRightShift,
    Operator,
    c_sharp_operators_UnaryModificationOperator,
    c_sharp_operators_RelationOperator,
    c_sharp_operators_MultiplicativeOperator,
    c_sharp_operators_EqualityOperator,
    c_sharp_operators_UnaryOperator,
    c_sharp_operators_AssignmentOperator,
    c_sharp_operators_ShiftOperator,
    c_sharp_operators_AdditiveOperator,
    c_sharp_operators_Operator,
    c_sharp_keywords_Event,
    c_sharp_keywords_Return,
    c_sharp_keywords_Default,
    c_sharp_keywords_Case,
    c_sharp_keywords_Params,
    c_sharp_keywords_Ref,
    c_sharp_keywords_Out,
    c_sharp_modifiers_Modifier,
    ReferenceType,
    c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType,
    Literal,
    c_sharp_literals_StringLiteral,
    c_sharp_literals_RealLiteral,
    c_sharp_literals_CharacterLiteral,
    c_sharp_literals_NullLiteral,
    c_sharp_literals_DecimalIntegerLiteral,
    c_sharp_literals_This,
    c_sharp_literals_HexadecimalIntegerLiteral,
    c_sharp_literals_BooleanLiteral,
    InclusiveOrExpression,
    c_sharp_expressions_ConditionalAndExpression,
    InclusiveOr,
    ExclusiveOrExpression,
    c_sharp_expressions_InclusiveOrExpression,
    ExclusiveOr,
    AndExpression,
    c_sharp_expressions_ExclusiveOrExpression,
    And,
    EqualityExpression,
    c_sharp_expressions_AndExpression,
    NotEqual,
    Equal,
    types_Type,
    types_NonArrayType,
    c_sharp_types_SimpleType,
    c_sharp_types_PointerType,
    c_sharp_types_ReferenceType,
    c_sharp_types_NonArrayType,
    c_sharp_types_Type,
    ConditionalOr,
    ConditionalAndExpression,
    c_sharp_expressions_ConditionalOrExpression,
    ConditionalAnd,
    MultiplicativeExpression,
    c_sharp_expressions_AdditiveExpression,
    Remainder,
    Division,
    c_sharp_expressions_MultiplicativeExpression,
    c_sharp_expressions_AddressOfExpression,
    c_sharp_expressions_CastExpression,
    RelationalExpression,
    c_sharp_expressions_EqualityExpression,
    GreaterThanOrEqual,
    GreaterThan,
    LessThanOrEqual,
    LessThan,
    ShiftExpression,
    c_sharp_expressions_RelationalExpression,
    AdditiveExpression,
    LeftShift,
    RightShift,
    c_sharp_expressions_ShiftExpression,
    AssignmentOperator,
    c_sharp_operators_AssignmentUnsignedRightShift,
    c_sharp_operators_AssignmentAnd,
    c_sharp_operators_AssignmentExclusiveOr,
    c_sharp_operators_AssignmentLeftShift,
    c_sharp_operators_AssignmentPlus,
    c_sharp_operators_AssignmentDivision,
    c_sharp_operators_AssignmentOr,
    c_sharp_operators_Assignment,
    c_sharp_operators_AssignmentRightShift,
    c_sharp_operators_AssignmentMultiplication,
    c_sharp_operators_AssignmentMinus,
    c_sharp_operators_AssignmentModulo,
    expressions_Expression,
    ConditionalOrExpression,
    AddressOfExpression,
    CastExpression,
    PreDecrementExpression,
    ArrayInitializer,
    PrimaryNoArrayCreationExpression,
    c_sharp_literals_Literal,
    c_sharp_expressions_TypeOfExpression,
    c_sharp_expressions_SizeOfExpression,
    c_sharp_expressions_UncheckedExpression,
    c_sharp_expressions_DelegateCreationExpression,
    c_sharp_expressions_CheckedExpression,
    c_sharp_expressions_BaseAccess,
    PreIncrementExpression,
    UnaryExpression,
    Multiplication,
    Complement,
    Negate,
    Subtraction,
    Addition,
    MemberAccess,
    c_sharp_expressions_UnaryExpression,
    c_sharp_expressions_ParenthesizedExpression,
    c_sharp_expressions_Argument,
    c_sharp_expressions_ExpressionList,
    classes_VariableInitializer,
    c_sharp_expressions_StatementExpression,
    ArgumentList,
    expressions_StatementExpression,
    c_sharp_expressions_AssignmentExpression,
    expressions_PrimaryExtendedExpressionType,
    c_sharp_expressions_PostIncrementExpression,
    c_sharp_expressions_PostDecrementExpression,
    c_sharp_expressions_InvocationExpression,
    SimpleType,
    c_sharp_types_Byte,
    c_sharp_types_UInt,
    c_sharp_types_Float,
    c_sharp_types_Short,
    c_sharp_types_Object,
    c_sharp_types_Void,
    c_sharp_types_Bool,
    c_sharp_types_Decimal,
    c_sharp_types_SByte,
    c_sharp_types_Double,
    c_sharp_types_Char,
    c_sharp_types_UShort,
    c_sharp_types_Long,
    c_sharp_types_String,
    c_sharp_types_Int,
    c_sharp_types_ULong,
    PrimaryExtendedExpressionType,
    c_sharp_expressions_PointerMemberAccess,
    c_sharp_expressions_ElementAccess,
    c_sharp_expressions_MemberAccess,
    c_sharp_expressions_PrimaryExtendedExpressionType,
    PrimaryExpression,
    c_sharp_expressions_ArrayCreationExpression,
    c_sharp_expressions_PrimaryNoArrayCreationExpression,
    c_sharp_expressions_PrimaryExpression,
    Argument,
    c_sharp_expressions_ArgumentList,
    FixedPointerDeclarator,
    PointerType,
    ResourceAcquisition,
    c_sharp_statements_ResourceAcquisition,
    c_sharp_statements_LocalConstantDeclaration,
    statements_ResourceAcquisition,
    c_sharp_expressions_Expression,
    statements_ForInitializer,
    c_sharp_statements_VariableDeclaration,
    c_sharp_statements_FixedPointerDeclarator,
    JumpStatement,
    c_sharp_statements_ReturnStatement,
    c_sharp_statements_ContinueStatement,
    c_sharp_statements_GotoStatement,
    c_sharp_statements_BreakStatement,
    c_sharp_statements_ForInitializer,
    c_sharp_statements_FinallyClause,
    c_sharp_statements_GeneralCatchClause,
    c_sharp_statements_SpecificCatchClause,
    FinallyClause,
    GeneralCatchClause,
    SpecificCatchClause,
    c_sharp_statements_ThrowStatement,
    Default,
    c_sharp_statements_SwitchLabel,
    SwitchLabel,
    c_sharp_statements_SwitchSection,
    SwitchSection,
    SelectionStatement,
    c_sharp_statements_SwitchStatement,
    c_sharp_statements_IfStatement,
    StatementExpression,
    c_sharp_expressions_PreDecrementExpression,
    c_sharp_expressions_PreIncrementExpression,
    StatementExpressionList,
    ForInitializer,
    c_sharp_expressions_StatementExpressionList,
    IterationStatement,
    c_sharp_statements_ForeachStatement,
    c_sharp_statements_DoStatement,
    c_sharp_statements_ForStatement,
    c_sharp_statements_WhileStatement,
    Case,
    NamedArgumentList,
    ExpressionList,
    c_sharp_attributes_AttributeArguments,
    AttributeArguments,
    c_sharp_attributes_Attribute,
    Return,
    Event,
    c_sharp_attributes_AttributeTarget,
    AttributeTarget,
    c_sharp_attributes_Attributes,
    c_sharp_attributes_GlobalAttributeTarget,
    Unsafe,
    EmbeddedStatement,
    c_sharp_statements_CheckedStatement,
    c_sharp_statements_LockStatement,
    c_sharp_statements_UncheckedStatement,
    c_sharp_statements_SelectionStatement,
    c_sharp_statements_UsingStatement,
    c_sharp_statements_EmptyStatement,
    c_sharp_statements_IterationStatement,
    c_sharp_statements_ExpressionStatement,
    c_sharp_statements_JumpStatement,
    c_sharp_statements_TryStatement,
    c_sharp_statements_FixedStatement,
    c_sharp_statements_SimpleEmbeddedStatement,
    LocalConstantDeclaration,
    VariableDeclaration,
    statements_Statement,
    c_sharp_statements_Statement,
    c_sharp_attributes_NamedArgument,
    NamedArgument,
    c_sharp_attributes_NamedArgumentList,
    ConstantDeclarator,
    c_sharp_classes_VariableInitializer,
    Statement,
    c_sharp_statements_DeclarationStatement,
    c_sharp_statements_EmbeddedStatement,
    c_sharp_classes_Block,
    ArrayType,
    Attribute,
    GlobalAttributeTarget,
    c_sharp_attributes_GlobalAttributes,
    c_sharp_arrays_RankSpecifier,
    RankSpecifier,
    NonArrayType,
    Expression,
    c_sharp_expressions_ConditionalExpression,
    VariableInitializer,
    c_sharp_arrays_ArrayInitializer,
    c_sharp_arrays_StackallocInitializer,
    VariableDeclarator,
    FormalParameterList,
    Type,
    c_sharp_arrays_ArrayType,
    c_sharp_classes_ClassMemberDeclaration,
    ClassOrInterfaceOrDelegateOrEnumType,
    c_sharp_classes_ClassBase,
    ClassMemberDeclaration,
    c_sharp_classes_ConstantDeclaration,
    c_sharp_classes_FieldDeclaration,
    Params,
    c_sharp_classes_ParameterArray,
    Out,
    Ref,
    c_sharp_classes_FixedParameter,
    ParameterArray,
    FixedParameter,
    c_sharp_classes_FormalParameterList,
    Block,
    NamespaceMemberDeclaration,
    GlobalAttributes,
    UsingDirective,
    c_sharp_namespaces_CompilationUnit,
    expressions_PrimaryNoArrayCreationExpression,
    c_sharp_expressions_ObjectCreationExpression,
    common_NamedElement,
    c_sharp_statements_LabeledStatement,
    c_sharp_common_Identifier,
    Identifier,
    c_sharp_common_NamespaceOrTypeName,
    c_sharp_common_NamedElement,
    ClassBase,
    Modifier,
    c_sharp_modifiers_Extern,
    c_sharp_modifiers_ReadOnly,
    c_sharp_modifiers_New,
    c_sharp_modifiers_Partial,
    c_sharp_modifiers_Volatile,
    c_sharp_modifiers_Sealed,
    c_sharp_modifiers_Private,
    c_sharp_modifiers_Public,
    c_sharp_modifiers_Abstract,
    c_sharp_modifiers_Virtual,
    c_sharp_modifiers_OverrideModifier,
    c_sharp_modifiers_Static,
    c_sharp_modifiers_Protected,
    c_sharp_modifiers_Internal,
    c_sharp_modifiers_Unsafe,
    Attributes,
    namespaces_TypeDeclaration,
    c_sharp_classes_Class,
    classes_ClassMemberDeclaration,
    c_sharp_classes_Method,
    namespaces_NamespaceMemberDeclaration,
    c_sharp_namespaces_TypeDeclaration,
    c_sharp_namespaces_NamespaceBody,
    NamespaceBody,
    c_sharp_namespaces_Namespace,
    c_sharp_namespaces_NamespaceMemberDeclaration,
    NamespaceOrTypeName,
    NamedElement,
    c_sharp_statements_VariableDeclarator,
    c_sharp_statements_ConstantDeclarator,
    c_sharp_namespaces_UsingDirective,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_shiftoperator_is_not_abstract():
    assert not inspect.isabstract(ShiftOperator)


def test_shiftoperator_constructor_exists():
    assert callable(ShiftOperator.__init__)


def test_shiftoperator_constructor_args():
    sig = inspect.signature(ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_rightshift_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_RightShift)


def test_c_sharp_operators_rightshift_constructor_exists():
    assert callable(c_sharp_operators_RightShift.__init__)


def test_c_sharp_operators_rightshift_constructor_args():
    sig = inspect.signature(c_sharp_operators_RightShift.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_leftshift_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_LeftShift)


def test_c_sharp_operators_leftshift_constructor_exists():
    assert callable(c_sharp_operators_LeftShift.__init__)


def test_c_sharp_operators_leftshift_constructor_args():
    sig = inspect.signature(c_sharp_operators_LeftShift.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationOperator)


def test_unarymodificationoperator_constructor_exists():
    assert callable(UnaryModificationOperator.__init__)


def test_unarymodificationoperator_constructor_args():
    sig = inspect.signature(UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_plusplus_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_PlusPlus)


def test_c_sharp_operators_plusplus_constructor_exists():
    assert callable(c_sharp_operators_PlusPlus.__init__)


def test_c_sharp_operators_plusplus_constructor_args():
    sig = inspect.signature(c_sharp_operators_PlusPlus.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_minusminus_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_MinusMinus)


def test_c_sharp_operators_minusminus_constructor_exists():
    assert callable(c_sharp_operators_MinusMinus.__init__)


def test_c_sharp_operators_minusminus_constructor_args():
    sig = inspect.signature(c_sharp_operators_MinusMinus.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_negate_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Negate)


def test_c_sharp_operators_negate_constructor_exists():
    assert callable(c_sharp_operators_Negate.__init__)


def test_c_sharp_operators_negate_constructor_args():
    sig = inspect.signature(c_sharp_operators_Negate.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_complement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Complement)


def test_c_sharp_operators_complement_constructor_exists():
    assert callable(c_sharp_operators_Complement.__init__)


def test_c_sharp_operators_complement_constructor_args():
    sig = inspect.signature(c_sharp_operators_Complement.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeOperator)


def test_multiplicativeoperator_constructor_exists():
    assert callable(MultiplicativeOperator.__init__)


def test_multiplicativeoperator_constructor_args():
    sig = inspect.signature(MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_remainder_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Remainder)


def test_c_sharp_operators_remainder_constructor_exists():
    assert callable(c_sharp_operators_Remainder.__init__)


def test_c_sharp_operators_remainder_constructor_args():
    sig = inspect.signature(c_sharp_operators_Remainder.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_multiplication_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Multiplication)


def test_c_sharp_operators_multiplication_constructor_exists():
    assert callable(c_sharp_operators_Multiplication.__init__)


def test_c_sharp_operators_multiplication_constructor_args():
    sig = inspect.signature(c_sharp_operators_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_division_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Division)


def test_c_sharp_operators_division_constructor_exists():
    assert callable(c_sharp_operators_Division.__init__)


def test_c_sharp_operators_division_constructor_args():
    sig = inspect.signature(c_sharp_operators_Division.__init__)
    params = list(sig.parameters.keys())



def test_operators_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(operators_UnaryOperator)


def test_operators_unaryoperator_constructor_exists():
    assert callable(operators_UnaryOperator.__init__)


def test_operators_unaryoperator_constructor_args():
    sig = inspect.signature(operators_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_additiveoperator_is_not_abstract():
    assert not inspect.isabstract(operators_AdditiveOperator)


def test_operators_additiveoperator_constructor_exists():
    assert callable(operators_AdditiveOperator.__init__)


def test_operators_additiveoperator_constructor_args():
    sig = inspect.signature(operators_AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_subtraction_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Subtraction)


def test_c_sharp_operators_subtraction_constructor_exists():
    assert callable(c_sharp_operators_Subtraction.__init__)


def test_c_sharp_operators_subtraction_constructor_args():
    sig = inspect.signature(c_sharp_operators_Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_addition_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Addition)


def test_c_sharp_operators_addition_constructor_exists():
    assert callable(c_sharp_operators_Addition.__init__)


def test_c_sharp_operators_addition_constructor_args():
    sig = inspect.signature(c_sharp_operators_Addition.__init__)
    params = list(sig.parameters.keys())



def test_relationoperator_is_not_abstract():
    assert not inspect.isabstract(RelationOperator)


def test_relationoperator_constructor_exists():
    assert callable(RelationOperator.__init__)


def test_relationoperator_constructor_args():
    sig = inspect.signature(RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_GreaterThanOrEqual)


def test_c_sharp_operators_greaterthanorequal_constructor_exists():
    assert callable(c_sharp_operators_GreaterThanOrEqual.__init__)


def test_c_sharp_operators_greaterthanorequal_constructor_args():
    sig = inspect.signature(c_sharp_operators_GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_lessthan_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_LessThan)


def test_c_sharp_operators_lessthan_constructor_exists():
    assert callable(c_sharp_operators_LessThan.__init__)


def test_c_sharp_operators_lessthan_constructor_args():
    sig = inspect.signature(c_sharp_operators_LessThan.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_LessThanOrEqual)


def test_c_sharp_operators_lessthanorequal_constructor_exists():
    assert callable(c_sharp_operators_LessThanOrEqual.__init__)


def test_c_sharp_operators_lessthanorequal_constructor_args():
    sig = inspect.signature(c_sharp_operators_LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_greaterthan_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_GreaterThan)


def test_c_sharp_operators_greaterthan_constructor_exists():
    assert callable(c_sharp_operators_GreaterThan.__init__)


def test_c_sharp_operators_greaterthan_constructor_args():
    sig = inspect.signature(c_sharp_operators_GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_equalityoperator_is_not_abstract():
    assert not inspect.isabstract(EqualityOperator)


def test_equalityoperator_constructor_exists():
    assert callable(EqualityOperator.__init__)


def test_equalityoperator_constructor_args():
    sig = inspect.signature(EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_notequal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_NotEqual)


def test_c_sharp_operators_notequal_constructor_exists():
    assert callable(c_sharp_operators_NotEqual.__init__)


def test_c_sharp_operators_notequal_constructor_args():
    sig = inspect.signature(c_sharp_operators_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_equal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Equal)


def test_c_sharp_operators_equal_constructor_exists():
    assert callable(c_sharp_operators_Equal.__init__)


def test_c_sharp_operators_equal_constructor_args():
    sig = inspect.signature(c_sharp_operators_Equal.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_conditionalor_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_ConditionalOr)


def test_c_sharp_operators_conditionalor_constructor_exists():
    assert callable(c_sharp_operators_ConditionalOr.__init__)


def test_c_sharp_operators_conditionalor_constructor_args():
    sig = inspect.signature(c_sharp_operators_ConditionalOr.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_conditionaland_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_ConditionalAnd)


def test_c_sharp_operators_conditionaland_constructor_exists():
    assert callable(c_sharp_operators_ConditionalAnd.__init__)


def test_c_sharp_operators_conditionaland_constructor_args():
    sig = inspect.signature(c_sharp_operators_ConditionalAnd.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_inclusiveor_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_InclusiveOr)


def test_c_sharp_operators_inclusiveor_constructor_exists():
    assert callable(c_sharp_operators_InclusiveOr.__init__)


def test_c_sharp_operators_inclusiveor_constructor_args():
    sig = inspect.signature(c_sharp_operators_InclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_exclusiveor_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_ExclusiveOr)


def test_c_sharp_operators_exclusiveor_constructor_exists():
    assert callable(c_sharp_operators_ExclusiveOr.__init__)


def test_c_sharp_operators_exclusiveor_constructor_args():
    sig = inspect.signature(c_sharp_operators_ExclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_and_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_And)


def test_c_sharp_operators_and_constructor_exists():
    assert callable(c_sharp_operators_And.__init__)


def test_c_sharp_operators_and_constructor_args():
    sig = inspect.signature(c_sharp_operators_And.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_unsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_UnsignedRightShift)


def test_c_sharp_operators_unsignedrightshift_constructor_exists():
    assert callable(c_sharp_operators_UnsignedRightShift.__init__)


def test_c_sharp_operators_unsignedrightshift_constructor_args():
    sig = inspect.signature(c_sharp_operators_UnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_UnaryModificationOperator)


def test_c_sharp_operators_unarymodificationoperator_constructor_exists():
    assert callable(c_sharp_operators_UnaryModificationOperator.__init__)


def test_c_sharp_operators_unarymodificationoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_relationoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_RelationOperator)


def test_c_sharp_operators_relationoperator_constructor_exists():
    assert callable(c_sharp_operators_RelationOperator.__init__)


def test_c_sharp_operators_relationoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_MultiplicativeOperator)


def test_c_sharp_operators_multiplicativeoperator_constructor_exists():
    assert callable(c_sharp_operators_MultiplicativeOperator.__init__)


def test_c_sharp_operators_multiplicativeoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_equalityoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_EqualityOperator)


def test_c_sharp_operators_equalityoperator_constructor_exists():
    assert callable(c_sharp_operators_EqualityOperator.__init__)


def test_c_sharp_operators_equalityoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_UnaryOperator)


def test_c_sharp_operators_unaryoperator_constructor_exists():
    assert callable(c_sharp_operators_UnaryOperator.__init__)


def test_c_sharp_operators_unaryoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentOperator)


def test_c_sharp_operators_assignmentoperator_constructor_exists():
    assert callable(c_sharp_operators_AssignmentOperator.__init__)


def test_c_sharp_operators_assignmentoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_shiftoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_ShiftOperator)


def test_c_sharp_operators_shiftoperator_constructor_exists():
    assert callable(c_sharp_operators_ShiftOperator.__init__)


def test_c_sharp_operators_shiftoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_additiveoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AdditiveOperator)


def test_c_sharp_operators_additiveoperator_constructor_exists():
    assert callable(c_sharp_operators_AdditiveOperator.__init__)


def test_c_sharp_operators_additiveoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_operator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Operator)


def test_c_sharp_operators_operator_constructor_exists():
    assert callable(c_sharp_operators_Operator.__init__)


def test_c_sharp_operators_operator_constructor_args():
    sig = inspect.signature(c_sharp_operators_Operator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_keywords_event_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Event)


def test_c_sharp_keywords_event_constructor_exists():
    assert callable(c_sharp_keywords_Event.__init__)


def test_c_sharp_keywords_event_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Event.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_keywords_return_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Return)


def test_c_sharp_keywords_return_constructor_exists():
    assert callable(c_sharp_keywords_Return.__init__)


def test_c_sharp_keywords_return_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Return.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_keywords_default_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Default)


def test_c_sharp_keywords_default_constructor_exists():
    assert callable(c_sharp_keywords_Default.__init__)


def test_c_sharp_keywords_default_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Default.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_keywords_case_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Case)


def test_c_sharp_keywords_case_constructor_exists():
    assert callable(c_sharp_keywords_Case.__init__)


def test_c_sharp_keywords_case_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Case.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_keywords_params_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Params)


def test_c_sharp_keywords_params_constructor_exists():
    assert callable(c_sharp_keywords_Params.__init__)


def test_c_sharp_keywords_params_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Params.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_keywords_ref_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Ref)


def test_c_sharp_keywords_ref_constructor_exists():
    assert callable(c_sharp_keywords_Ref.__init__)


def test_c_sharp_keywords_ref_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Ref.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_keywords_out_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Out)


def test_c_sharp_keywords_out_constructor_exists():
    assert callable(c_sharp_keywords_Out.__init__)


def test_c_sharp_keywords_out_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Out.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_modifier_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Modifier)


def test_c_sharp_modifiers_modifier_constructor_exists():
    assert callable(c_sharp_modifiers_Modifier.__init__)


def test_c_sharp_modifiers_modifier_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Modifier.__init__)
    params = list(sig.parameters.keys())



def test_referencetype_is_not_abstract():
    assert not inspect.isabstract(ReferenceType)


def test_referencetype_constructor_exists():
    assert callable(ReferenceType.__init__)


def test_referencetype_constructor_args():
    sig = inspect.signature(ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_classorinterfaceordelegateorenumtype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType)


def test_c_sharp_types_classorinterfaceordelegateorenumtype_constructor_exists():
    assert callable(c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType.__init__)


def test_c_sharp_types_classorinterfaceordelegateorenumtype_constructor_args():
    sig = inspect.signature(c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_literals_stringliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_StringLiteral)


def test_c_sharp_literals_stringliteral_constructor_exists():
    assert callable(c_sharp_literals_StringLiteral.__init__)


def test_c_sharp_literals_stringliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_sharp_literals_stringliteral_has_value():
    assert hasattr(c_sharp_literals_StringLiteral, "value")
    descriptor = None
    for klass in c_sharp_literals_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c_sharp_literals_realliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_RealLiteral)


def test_c_sharp_literals_realliteral_constructor_exists():
    assert callable(c_sharp_literals_RealLiteral.__init__)


def test_c_sharp_literals_realliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_sharp_literals_realliteral_has_value():
    assert hasattr(c_sharp_literals_RealLiteral, "value")
    descriptor = None
    for klass in c_sharp_literals_RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c_sharp_literals_characterliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_CharacterLiteral)


def test_c_sharp_literals_characterliteral_constructor_exists():
    assert callable(c_sharp_literals_CharacterLiteral.__init__)


def test_c_sharp_literals_characterliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_sharp_literals_characterliteral_has_value():
    assert hasattr(c_sharp_literals_CharacterLiteral, "value")
    descriptor = None
    for klass in c_sharp_literals_CharacterLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c_sharp_literals_nullliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_NullLiteral)


def test_c_sharp_literals_nullliteral_constructor_exists():
    assert callable(c_sharp_literals_NullLiteral.__init__)


def test_c_sharp_literals_nullliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_literals_decimalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_DecimalIntegerLiteral)


def test_c_sharp_literals_decimalintegerliteral_constructor_exists():
    assert callable(c_sharp_literals_DecimalIntegerLiteral.__init__)


def test_c_sharp_literals_decimalintegerliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_DecimalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_sharp_literals_decimalintegerliteral_has_value():
    assert hasattr(c_sharp_literals_DecimalIntegerLiteral, "value")
    descriptor = None
    for klass in c_sharp_literals_DecimalIntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c_sharp_literals_this_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_This)


def test_c_sharp_literals_this_constructor_exists():
    assert callable(c_sharp_literals_This.__init__)


def test_c_sharp_literals_this_constructor_args():
    sig = inspect.signature(c_sharp_literals_This.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_literals_hexadecimalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_HexadecimalIntegerLiteral)


def test_c_sharp_literals_hexadecimalintegerliteral_constructor_exists():
    assert callable(c_sharp_literals_HexadecimalIntegerLiteral.__init__)


def test_c_sharp_literals_hexadecimalintegerliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_HexadecimalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_sharp_literals_hexadecimalintegerliteral_has_value():
    assert hasattr(c_sharp_literals_HexadecimalIntegerLiteral, "value")
    descriptor = None
    for klass in c_sharp_literals_HexadecimalIntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c_sharp_literals_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_BooleanLiteral)


def test_c_sharp_literals_booleanliteral_constructor_exists():
    assert callable(c_sharp_literals_BooleanLiteral.__init__)


def test_c_sharp_literals_booleanliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_sharp_literals_booleanliteral_has_value():
    assert hasattr(c_sharp_literals_BooleanLiteral, "value")
    descriptor = None
    for klass in c_sharp_literals_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(InclusiveOrExpression)


def test_inclusiveorexpression_constructor_exists():
    assert callable(InclusiveOrExpression.__init__)


def test_inclusiveorexpression_constructor_args():
    sig = inspect.signature(InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ConditionalAndExpression)


def test_c_sharp_expressions_conditionalandexpression_constructor_exists():
    assert callable(c_sharp_expressions_ConditionalAndExpression.__init__)


def test_c_sharp_expressions_conditionalandexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_inclusiveor_is_not_abstract():
    assert not inspect.isabstract(InclusiveOr)


def test_inclusiveor_constructor_exists():
    assert callable(InclusiveOr.__init__)


def test_inclusiveor_constructor_args():
    sig = inspect.signature(InclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(ExclusiveOrExpression)


def test_exclusiveorexpression_constructor_exists():
    assert callable(ExclusiveOrExpression.__init__)


def test_exclusiveorexpression_constructor_args():
    sig = inspect.signature(ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_InclusiveOrExpression)


def test_c_sharp_expressions_inclusiveorexpression_constructor_exists():
    assert callable(c_sharp_expressions_InclusiveOrExpression.__init__)


def test_c_sharp_expressions_inclusiveorexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_exclusiveor_is_not_abstract():
    assert not inspect.isabstract(ExclusiveOr)


def test_exclusiveor_constructor_exists():
    assert callable(ExclusiveOr.__init__)


def test_exclusiveor_constructor_args():
    sig = inspect.signature(ExclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_andexpression_is_not_abstract():
    assert not inspect.isabstract(AndExpression)


def test_andexpression_constructor_exists():
    assert callable(AndExpression.__init__)


def test_andexpression_constructor_args():
    sig = inspect.signature(AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ExclusiveOrExpression)


def test_c_sharp_expressions_exclusiveorexpression_constructor_exists():
    assert callable(c_sharp_expressions_ExclusiveOrExpression.__init__)


def test_c_sharp_expressions_exclusiveorexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_and_is_not_abstract():
    assert not inspect.isabstract(And)


def test_and_constructor_exists():
    assert callable(And.__init__)


def test_and_constructor_args():
    sig = inspect.signature(And.__init__)
    params = list(sig.parameters.keys())



def test_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(EqualityExpression)


def test_equalityexpression_constructor_exists():
    assert callable(EqualityExpression.__init__)


def test_equalityexpression_constructor_args():
    sig = inspect.signature(EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_andexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_AndExpression)


def test_c_sharp_expressions_andexpression_constructor_exists():
    assert callable(c_sharp_expressions_AndExpression.__init__)


def test_c_sharp_expressions_andexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_notequal_is_not_abstract():
    assert not inspect.isabstract(NotEqual)


def test_notequal_constructor_exists():
    assert callable(NotEqual.__init__)


def test_notequal_constructor_args():
    sig = inspect.signature(NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_equal_is_not_abstract():
    assert not inspect.isabstract(Equal)


def test_equal_constructor_exists():
    assert callable(Equal.__init__)


def test_equal_constructor_args():
    sig = inspect.signature(Equal.__init__)
    params = list(sig.parameters.keys())



def test_types_type_is_not_abstract():
    assert not inspect.isabstract(types_Type)


def test_types_type_constructor_exists():
    assert callable(types_Type.__init__)


def test_types_type_constructor_args():
    sig = inspect.signature(types_Type.__init__)
    params = list(sig.parameters.keys())



def test_types_nonarraytype_is_not_abstract():
    assert not inspect.isabstract(types_NonArrayType)


def test_types_nonarraytype_constructor_exists():
    assert callable(types_NonArrayType.__init__)


def test_types_nonarraytype_constructor_args():
    sig = inspect.signature(types_NonArrayType.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_simpletype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_SimpleType)


def test_c_sharp_types_simpletype_constructor_exists():
    assert callable(c_sharp_types_SimpleType.__init__)


def test_c_sharp_types_simpletype_constructor_args():
    sig = inspect.signature(c_sharp_types_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_pointertype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_PointerType)


def test_c_sharp_types_pointertype_constructor_exists():
    assert callable(c_sharp_types_PointerType.__init__)


def test_c_sharp_types_pointertype_constructor_args():
    sig = inspect.signature(c_sharp_types_PointerType.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_referencetype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_ReferenceType)


def test_c_sharp_types_referencetype_constructor_exists():
    assert callable(c_sharp_types_ReferenceType.__init__)


def test_c_sharp_types_referencetype_constructor_args():
    sig = inspect.signature(c_sharp_types_ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_nonarraytype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_NonArrayType)


def test_c_sharp_types_nonarraytype_constructor_exists():
    assert callable(c_sharp_types_NonArrayType.__init__)


def test_c_sharp_types_nonarraytype_constructor_args():
    sig = inspect.signature(c_sharp_types_NonArrayType.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_type_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Type)


def test_c_sharp_types_type_constructor_exists():
    assert callable(c_sharp_types_Type.__init__)


def test_c_sharp_types_type_constructor_args():
    sig = inspect.signature(c_sharp_types_Type.__init__)
    params = list(sig.parameters.keys())



def test_conditionalor_is_not_abstract():
    assert not inspect.isabstract(ConditionalOr)


def test_conditionalor_constructor_exists():
    assert callable(ConditionalOr.__init__)


def test_conditionalor_constructor_args():
    sig = inspect.signature(ConditionalOr.__init__)
    params = list(sig.parameters.keys())



def test_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(ConditionalAndExpression)


def test_conditionalandexpression_constructor_exists():
    assert callable(ConditionalAndExpression.__init__)


def test_conditionalandexpression_constructor_args():
    sig = inspect.signature(ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ConditionalOrExpression)


def test_c_sharp_expressions_conditionalorexpression_constructor_exists():
    assert callable(c_sharp_expressions_ConditionalOrExpression.__init__)


def test_c_sharp_expressions_conditionalorexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionaland_is_not_abstract():
    assert not inspect.isabstract(ConditionalAnd)


def test_conditionaland_constructor_exists():
    assert callable(ConditionalAnd.__init__)


def test_conditionaland_constructor_args():
    sig = inspect.signature(ConditionalAnd.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeExpression)


def test_multiplicativeexpression_constructor_exists():
    assert callable(MultiplicativeExpression.__init__)


def test_multiplicativeexpression_constructor_args():
    sig = inspect.signature(MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_AdditiveExpression)


def test_c_sharp_expressions_additiveexpression_constructor_exists():
    assert callable(c_sharp_expressions_AdditiveExpression.__init__)


def test_c_sharp_expressions_additiveexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_remainder_is_not_abstract():
    assert not inspect.isabstract(Remainder)


def test_remainder_constructor_exists():
    assert callable(Remainder.__init__)


def test_remainder_constructor_args():
    sig = inspect.signature(Remainder.__init__)
    params = list(sig.parameters.keys())



def test_division_is_not_abstract():
    assert not inspect.isabstract(Division)


def test_division_constructor_exists():
    assert callable(Division.__init__)


def test_division_constructor_args():
    sig = inspect.signature(Division.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_MultiplicativeExpression)


def test_c_sharp_expressions_multiplicativeexpression_constructor_exists():
    assert callable(c_sharp_expressions_MultiplicativeExpression.__init__)


def test_c_sharp_expressions_multiplicativeexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_addressofexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_AddressOfExpression)


def test_c_sharp_expressions_addressofexpression_constructor_exists():
    assert callable(c_sharp_expressions_AddressOfExpression.__init__)


def test_c_sharp_expressions_addressofexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_AddressOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_castexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_CastExpression)


def test_c_sharp_expressions_castexpression_constructor_exists():
    assert callable(c_sharp_expressions_CastExpression.__init__)


def test_c_sharp_expressions_castexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(RelationalExpression)


def test_relationalexpression_constructor_exists():
    assert callable(RelationalExpression.__init__)


def test_relationalexpression_constructor_args():
    sig = inspect.signature(RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_EqualityExpression)


def test_c_sharp_expressions_equalityexpression_constructor_exists():
    assert callable(c_sharp_expressions_EqualityExpression.__init__)


def test_c_sharp_expressions_equalityexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(GreaterThanOrEqual)


def test_greaterthanorequal_constructor_exists():
    assert callable(GreaterThanOrEqual.__init__)


def test_greaterthanorequal_constructor_args():
    sig = inspect.signature(GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_greaterthan_is_not_abstract():
    assert not inspect.isabstract(GreaterThan)


def test_greaterthan_constructor_exists():
    assert callable(GreaterThan.__init__)


def test_greaterthan_constructor_args():
    sig = inspect.signature(GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(LessThanOrEqual)


def test_lessthanorequal_constructor_exists():
    assert callable(LessThanOrEqual.__init__)


def test_lessthanorequal_constructor_args():
    sig = inspect.signature(LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_lessthan_is_not_abstract():
    assert not inspect.isabstract(LessThan)


def test_lessthan_constructor_exists():
    assert callable(LessThan.__init__)


def test_lessthan_constructor_args():
    sig = inspect.signature(LessThan.__init__)
    params = list(sig.parameters.keys())



def test_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(ShiftExpression)


def test_shiftexpression_constructor_exists():
    assert callable(ShiftExpression.__init__)


def test_shiftexpression_constructor_args():
    sig = inspect.signature(ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_RelationalExpression)


def test_c_sharp_expressions_relationalexpression_constructor_exists():
    assert callable(c_sharp_expressions_RelationalExpression.__init__)


def test_c_sharp_expressions_relationalexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(AdditiveExpression)


def test_additiveexpression_constructor_exists():
    assert callable(AdditiveExpression.__init__)


def test_additiveexpression_constructor_args():
    sig = inspect.signature(AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_leftshift_is_not_abstract():
    assert not inspect.isabstract(LeftShift)


def test_leftshift_constructor_exists():
    assert callable(LeftShift.__init__)


def test_leftshift_constructor_args():
    sig = inspect.signature(LeftShift.__init__)
    params = list(sig.parameters.keys())



def test_rightshift_is_not_abstract():
    assert not inspect.isabstract(RightShift)


def test_rightshift_constructor_exists():
    assert callable(RightShift.__init__)


def test_rightshift_constructor_args():
    sig = inspect.signature(RightShift.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ShiftExpression)


def test_c_sharp_expressions_shiftexpression_constructor_exists():
    assert callable(c_sharp_expressions_ShiftExpression.__init__)


def test_c_sharp_expressions_shiftexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(AssignmentOperator)


def test_assignmentoperator_constructor_exists():
    assert callable(AssignmentOperator.__init__)


def test_assignmentoperator_constructor_args():
    sig = inspect.signature(AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_assignmentunsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentUnsignedRightShift)


def test_c_sharp_operators_assignmentunsignedrightshift_constructor_exists():
    assert callable(c_sharp_operators_AssignmentUnsignedRightShift.__init__)


def test_c_sharp_operators_assignmentunsignedrightshift_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentUnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_assignmentand_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentAnd)


def test_c_sharp_operators_assignmentand_constructor_exists():
    assert callable(c_sharp_operators_AssignmentAnd.__init__)


def test_c_sharp_operators_assignmentand_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentAnd.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_assignmentexclusiveor_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentExclusiveOr)


def test_c_sharp_operators_assignmentexclusiveor_constructor_exists():
    assert callable(c_sharp_operators_AssignmentExclusiveOr.__init__)


def test_c_sharp_operators_assignmentexclusiveor_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentExclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_assignmentleftshift_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentLeftShift)


def test_c_sharp_operators_assignmentleftshift_constructor_exists():
    assert callable(c_sharp_operators_AssignmentLeftShift.__init__)


def test_c_sharp_operators_assignmentleftshift_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_assignmentplus_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentPlus)


def test_c_sharp_operators_assignmentplus_constructor_exists():
    assert callable(c_sharp_operators_AssignmentPlus.__init__)


def test_c_sharp_operators_assignmentplus_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentPlus.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_assignmentdivision_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentDivision)


def test_c_sharp_operators_assignmentdivision_constructor_exists():
    assert callable(c_sharp_operators_AssignmentDivision.__init__)


def test_c_sharp_operators_assignmentdivision_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentDivision.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_assignmentor_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentOr)


def test_c_sharp_operators_assignmentor_constructor_exists():
    assert callable(c_sharp_operators_AssignmentOr.__init__)


def test_c_sharp_operators_assignmentor_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentOr.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_assignment_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Assignment)


def test_c_sharp_operators_assignment_constructor_exists():
    assert callable(c_sharp_operators_Assignment.__init__)


def test_c_sharp_operators_assignment_constructor_args():
    sig = inspect.signature(c_sharp_operators_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_assignmentrightshift_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentRightShift)


def test_c_sharp_operators_assignmentrightshift_constructor_exists():
    assert callable(c_sharp_operators_AssignmentRightShift.__init__)


def test_c_sharp_operators_assignmentrightshift_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentRightShift.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_assignmentmultiplication_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentMultiplication)


def test_c_sharp_operators_assignmentmultiplication_constructor_exists():
    assert callable(c_sharp_operators_AssignmentMultiplication.__init__)


def test_c_sharp_operators_assignmentmultiplication_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentMultiplication.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_assignmentminus_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentMinus)


def test_c_sharp_operators_assignmentminus_constructor_exists():
    assert callable(c_sharp_operators_AssignmentMinus.__init__)


def test_c_sharp_operators_assignmentminus_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentMinus.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_operators_assignmentmodulo_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentModulo)


def test_c_sharp_operators_assignmentmodulo_constructor_exists():
    assert callable(c_sharp_operators_AssignmentModulo.__init__)


def test_c_sharp_operators_assignmentmodulo_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentModulo.__init__)
    params = list(sig.parameters.keys())



def test_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(expressions_Expression)


def test_expressions_expression_constructor_exists():
    assert callable(expressions_Expression.__init__)


def test_expressions_expression_constructor_args():
    sig = inspect.signature(expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(ConditionalOrExpression)


def test_conditionalorexpression_constructor_exists():
    assert callable(ConditionalOrExpression.__init__)


def test_conditionalorexpression_constructor_args():
    sig = inspect.signature(ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_addressofexpression_is_not_abstract():
    assert not inspect.isabstract(AddressOfExpression)


def test_addressofexpression_constructor_exists():
    assert callable(AddressOfExpression.__init__)


def test_addressofexpression_constructor_args():
    sig = inspect.signature(AddressOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_castexpression_is_not_abstract():
    assert not inspect.isabstract(CastExpression)


def test_castexpression_constructor_exists():
    assert callable(CastExpression.__init__)


def test_castexpression_constructor_args():
    sig = inspect.signature(CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_predecrementexpression_is_not_abstract():
    assert not inspect.isabstract(PreDecrementExpression)


def test_predecrementexpression_constructor_exists():
    assert callable(PreDecrementExpression.__init__)


def test_predecrementexpression_constructor_args():
    sig = inspect.signature(PreDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(ArrayInitializer)


def test_arrayinitializer_constructor_exists():
    assert callable(ArrayInitializer.__init__)


def test_arrayinitializer_constructor_args():
    sig = inspect.signature(ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_primarynoarraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryNoArrayCreationExpression)


def test_primarynoarraycreationexpression_constructor_exists():
    assert callable(PrimaryNoArrayCreationExpression.__init__)


def test_primarynoarraycreationexpression_constructor_args():
    sig = inspect.signature(PrimaryNoArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_literals_literal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_Literal)


def test_c_sharp_literals_literal_constructor_exists():
    assert callable(c_sharp_literals_Literal.__init__)


def test_c_sharp_literals_literal_constructor_args():
    sig = inspect.signature(c_sharp_literals_Literal.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_typeofexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_TypeOfExpression)


def test_c_sharp_expressions_typeofexpression_constructor_exists():
    assert callable(c_sharp_expressions_TypeOfExpression.__init__)


def test_c_sharp_expressions_typeofexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_TypeOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_sizeofexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_SizeOfExpression)


def test_c_sharp_expressions_sizeofexpression_constructor_exists():
    assert callable(c_sharp_expressions_SizeOfExpression.__init__)


def test_c_sharp_expressions_sizeofexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_SizeOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_uncheckedexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_UncheckedExpression)


def test_c_sharp_expressions_uncheckedexpression_constructor_exists():
    assert callable(c_sharp_expressions_UncheckedExpression.__init__)


def test_c_sharp_expressions_uncheckedexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_UncheckedExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_delegatecreationexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_DelegateCreationExpression)


def test_c_sharp_expressions_delegatecreationexpression_constructor_exists():
    assert callable(c_sharp_expressions_DelegateCreationExpression.__init__)


def test_c_sharp_expressions_delegatecreationexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_DelegateCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_checkedexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_CheckedExpression)


def test_c_sharp_expressions_checkedexpression_constructor_exists():
    assert callable(c_sharp_expressions_CheckedExpression.__init__)


def test_c_sharp_expressions_checkedexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_CheckedExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_baseaccess_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_BaseAccess)


def test_c_sharp_expressions_baseaccess_constructor_exists():
    assert callable(c_sharp_expressions_BaseAccess.__init__)


def test_c_sharp_expressions_baseaccess_constructor_args():
    sig = inspect.signature(c_sharp_expressions_BaseAccess.__init__)
    params = list(sig.parameters.keys())



def test_preincrementexpression_is_not_abstract():
    assert not inspect.isabstract(PreIncrementExpression)


def test_preincrementexpression_constructor_exists():
    assert callable(PreIncrementExpression.__init__)


def test_preincrementexpression_constructor_args():
    sig = inspect.signature(PreIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_multiplication_is_not_abstract():
    assert not inspect.isabstract(Multiplication)


def test_multiplication_constructor_exists():
    assert callable(Multiplication.__init__)


def test_multiplication_constructor_args():
    sig = inspect.signature(Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_complement_is_not_abstract():
    assert not inspect.isabstract(Complement)


def test_complement_constructor_exists():
    assert callable(Complement.__init__)


def test_complement_constructor_args():
    sig = inspect.signature(Complement.__init__)
    params = list(sig.parameters.keys())



def test_negate_is_not_abstract():
    assert not inspect.isabstract(Negate)


def test_negate_constructor_exists():
    assert callable(Negate.__init__)


def test_negate_constructor_args():
    sig = inspect.signature(Negate.__init__)
    params = list(sig.parameters.keys())



def test_subtraction_is_not_abstract():
    assert not inspect.isabstract(Subtraction)


def test_subtraction_constructor_exists():
    assert callable(Subtraction.__init__)


def test_subtraction_constructor_args():
    sig = inspect.signature(Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_addition_is_not_abstract():
    assert not inspect.isabstract(Addition)


def test_addition_constructor_exists():
    assert callable(Addition.__init__)


def test_addition_constructor_args():
    sig = inspect.signature(Addition.__init__)
    params = list(sig.parameters.keys())



def test_memberaccess_is_not_abstract():
    assert not inspect.isabstract(MemberAccess)


def test_memberaccess_constructor_exists():
    assert callable(MemberAccess.__init__)


def test_memberaccess_constructor_args():
    sig = inspect.signature(MemberAccess.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_UnaryExpression)


def test_c_sharp_expressions_unaryexpression_constructor_exists():
    assert callable(c_sharp_expressions_UnaryExpression.__init__)


def test_c_sharp_expressions_unaryexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ParenthesizedExpression)


def test_c_sharp_expressions_parenthesizedexpression_constructor_exists():
    assert callable(c_sharp_expressions_ParenthesizedExpression.__init__)


def test_c_sharp_expressions_parenthesizedexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_argument_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_Argument)


def test_c_sharp_expressions_argument_constructor_exists():
    assert callable(c_sharp_expressions_Argument.__init__)


def test_c_sharp_expressions_argument_constructor_args():
    sig = inspect.signature(c_sharp_expressions_Argument.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_expressionlist_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ExpressionList)


def test_c_sharp_expressions_expressionlist_constructor_exists():
    assert callable(c_sharp_expressions_ExpressionList.__init__)


def test_c_sharp_expressions_expressionlist_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_classes_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(classes_VariableInitializer)


def test_classes_variableinitializer_constructor_exists():
    assert callable(classes_VariableInitializer.__init__)


def test_classes_variableinitializer_constructor_args():
    sig = inspect.signature(classes_VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_statementexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_StatementExpression)


def test_c_sharp_expressions_statementexpression_constructor_exists():
    assert callable(c_sharp_expressions_StatementExpression.__init__)


def test_c_sharp_expressions_statementexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_argumentlist_is_not_abstract():
    assert not inspect.isabstract(ArgumentList)


def test_argumentlist_constructor_exists():
    assert callable(ArgumentList.__init__)


def test_argumentlist_constructor_args():
    sig = inspect.signature(ArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_expressions_statementexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_StatementExpression)


def test_expressions_statementexpression_constructor_exists():
    assert callable(expressions_StatementExpression.__init__)


def test_expressions_statementexpression_constructor_args():
    sig = inspect.signature(expressions_StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_AssignmentExpression)


def test_c_sharp_expressions_assignmentexpression_constructor_exists():
    assert callable(c_sharp_expressions_AssignmentExpression.__init__)


def test_c_sharp_expressions_assignmentexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_primaryextendedexpressiontype_is_not_abstract():
    assert not inspect.isabstract(expressions_PrimaryExtendedExpressionType)


def test_expressions_primaryextendedexpressiontype_constructor_exists():
    assert callable(expressions_PrimaryExtendedExpressionType.__init__)


def test_expressions_primaryextendedexpressiontype_constructor_args():
    sig = inspect.signature(expressions_PrimaryExtendedExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_postincrementexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PostIncrementExpression)


def test_c_sharp_expressions_postincrementexpression_constructor_exists():
    assert callable(c_sharp_expressions_PostIncrementExpression.__init__)


def test_c_sharp_expressions_postincrementexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PostIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_postdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PostDecrementExpression)


def test_c_sharp_expressions_postdecrementexpression_constructor_exists():
    assert callable(c_sharp_expressions_PostDecrementExpression.__init__)


def test_c_sharp_expressions_postdecrementexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PostDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_invocationexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_InvocationExpression)


def test_c_sharp_expressions_invocationexpression_constructor_exists():
    assert callable(c_sharp_expressions_InvocationExpression.__init__)


def test_c_sharp_expressions_invocationexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_InvocationExpression.__init__)
    params = list(sig.parameters.keys())



def test_simpletype_is_not_abstract():
    assert not inspect.isabstract(SimpleType)


def test_simpletype_constructor_exists():
    assert callable(SimpleType.__init__)


def test_simpletype_constructor_args():
    sig = inspect.signature(SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_byte_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Byte)


def test_c_sharp_types_byte_constructor_exists():
    assert callable(c_sharp_types_Byte.__init__)


def test_c_sharp_types_byte_constructor_args():
    sig = inspect.signature(c_sharp_types_Byte.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_uint_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_UInt)


def test_c_sharp_types_uint_constructor_exists():
    assert callable(c_sharp_types_UInt.__init__)


def test_c_sharp_types_uint_constructor_args():
    sig = inspect.signature(c_sharp_types_UInt.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_float_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Float)


def test_c_sharp_types_float_constructor_exists():
    assert callable(c_sharp_types_Float.__init__)


def test_c_sharp_types_float_constructor_args():
    sig = inspect.signature(c_sharp_types_Float.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_short_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Short)


def test_c_sharp_types_short_constructor_exists():
    assert callable(c_sharp_types_Short.__init__)


def test_c_sharp_types_short_constructor_args():
    sig = inspect.signature(c_sharp_types_Short.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_object_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Object)


def test_c_sharp_types_object_constructor_exists():
    assert callable(c_sharp_types_Object.__init__)


def test_c_sharp_types_object_constructor_args():
    sig = inspect.signature(c_sharp_types_Object.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_void_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Void)


def test_c_sharp_types_void_constructor_exists():
    assert callable(c_sharp_types_Void.__init__)


def test_c_sharp_types_void_constructor_args():
    sig = inspect.signature(c_sharp_types_Void.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_bool_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Bool)


def test_c_sharp_types_bool_constructor_exists():
    assert callable(c_sharp_types_Bool.__init__)


def test_c_sharp_types_bool_constructor_args():
    sig = inspect.signature(c_sharp_types_Bool.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_decimal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Decimal)


def test_c_sharp_types_decimal_constructor_exists():
    assert callable(c_sharp_types_Decimal.__init__)


def test_c_sharp_types_decimal_constructor_args():
    sig = inspect.signature(c_sharp_types_Decimal.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_sbyte_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_SByte)


def test_c_sharp_types_sbyte_constructor_exists():
    assert callable(c_sharp_types_SByte.__init__)


def test_c_sharp_types_sbyte_constructor_args():
    sig = inspect.signature(c_sharp_types_SByte.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_double_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Double)


def test_c_sharp_types_double_constructor_exists():
    assert callable(c_sharp_types_Double.__init__)


def test_c_sharp_types_double_constructor_args():
    sig = inspect.signature(c_sharp_types_Double.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_char_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Char)


def test_c_sharp_types_char_constructor_exists():
    assert callable(c_sharp_types_Char.__init__)


def test_c_sharp_types_char_constructor_args():
    sig = inspect.signature(c_sharp_types_Char.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_ushort_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_UShort)


def test_c_sharp_types_ushort_constructor_exists():
    assert callable(c_sharp_types_UShort.__init__)


def test_c_sharp_types_ushort_constructor_args():
    sig = inspect.signature(c_sharp_types_UShort.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_long_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Long)


def test_c_sharp_types_long_constructor_exists():
    assert callable(c_sharp_types_Long.__init__)


def test_c_sharp_types_long_constructor_args():
    sig = inspect.signature(c_sharp_types_Long.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_string_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_String)


def test_c_sharp_types_string_constructor_exists():
    assert callable(c_sharp_types_String.__init__)


def test_c_sharp_types_string_constructor_args():
    sig = inspect.signature(c_sharp_types_String.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_int_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Int)


def test_c_sharp_types_int_constructor_exists():
    assert callable(c_sharp_types_Int.__init__)


def test_c_sharp_types_int_constructor_args():
    sig = inspect.signature(c_sharp_types_Int.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_types_ulong_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_ULong)


def test_c_sharp_types_ulong_constructor_exists():
    assert callable(c_sharp_types_ULong.__init__)


def test_c_sharp_types_ulong_constructor_args():
    sig = inspect.signature(c_sharp_types_ULong.__init__)
    params = list(sig.parameters.keys())



def test_primaryextendedexpressiontype_is_not_abstract():
    assert not inspect.isabstract(PrimaryExtendedExpressionType)


def test_primaryextendedexpressiontype_constructor_exists():
    assert callable(PrimaryExtendedExpressionType.__init__)


def test_primaryextendedexpressiontype_constructor_args():
    sig = inspect.signature(PrimaryExtendedExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_pointermemberaccess_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PointerMemberAccess)


def test_c_sharp_expressions_pointermemberaccess_constructor_exists():
    assert callable(c_sharp_expressions_PointerMemberAccess.__init__)


def test_c_sharp_expressions_pointermemberaccess_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PointerMemberAccess.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_elementaccess_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ElementAccess)


def test_c_sharp_expressions_elementaccess_constructor_exists():
    assert callable(c_sharp_expressions_ElementAccess.__init__)


def test_c_sharp_expressions_elementaccess_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_memberaccess_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_MemberAccess)


def test_c_sharp_expressions_memberaccess_constructor_exists():
    assert callable(c_sharp_expressions_MemberAccess.__init__)


def test_c_sharp_expressions_memberaccess_constructor_args():
    sig = inspect.signature(c_sharp_expressions_MemberAccess.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_primaryextendedexpressiontype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PrimaryExtendedExpressionType)


def test_c_sharp_expressions_primaryextendedexpressiontype_constructor_exists():
    assert callable(c_sharp_expressions_PrimaryExtendedExpressionType.__init__)


def test_c_sharp_expressions_primaryextendedexpressiontype_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PrimaryExtendedExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_arraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ArrayCreationExpression)


def test_c_sharp_expressions_arraycreationexpression_constructor_exists():
    assert callable(c_sharp_expressions_ArrayCreationExpression.__init__)


def test_c_sharp_expressions_arraycreationexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_primarynoarraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PrimaryNoArrayCreationExpression)


def test_c_sharp_expressions_primarynoarraycreationexpression_constructor_exists():
    assert callable(c_sharp_expressions_PrimaryNoArrayCreationExpression.__init__)


def test_c_sharp_expressions_primarynoarraycreationexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PrimaryNoArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PrimaryExpression)


def test_c_sharp_expressions_primaryexpression_constructor_exists():
    assert callable(c_sharp_expressions_PrimaryExpression.__init__)


def test_c_sharp_expressions_primaryexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_argument_is_not_abstract():
    assert not inspect.isabstract(Argument)


def test_argument_constructor_exists():
    assert callable(Argument.__init__)


def test_argument_constructor_args():
    sig = inspect.signature(Argument.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_argumentlist_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ArgumentList)


def test_c_sharp_expressions_argumentlist_constructor_exists():
    assert callable(c_sharp_expressions_ArgumentList.__init__)


def test_c_sharp_expressions_argumentlist_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_fixedpointerdeclarator_is_not_abstract():
    assert not inspect.isabstract(FixedPointerDeclarator)


def test_fixedpointerdeclarator_constructor_exists():
    assert callable(FixedPointerDeclarator.__init__)


def test_fixedpointerdeclarator_constructor_args():
    sig = inspect.signature(FixedPointerDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_pointertype_is_not_abstract():
    assert not inspect.isabstract(PointerType)


def test_pointertype_constructor_exists():
    assert callable(PointerType.__init__)


def test_pointertype_constructor_args():
    sig = inspect.signature(PointerType.__init__)
    params = list(sig.parameters.keys())



def test_resourceacquisition_is_not_abstract():
    assert not inspect.isabstract(ResourceAcquisition)


def test_resourceacquisition_constructor_exists():
    assert callable(ResourceAcquisition.__init__)


def test_resourceacquisition_constructor_args():
    sig = inspect.signature(ResourceAcquisition.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_resourceacquisition_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ResourceAcquisition)


def test_c_sharp_statements_resourceacquisition_constructor_exists():
    assert callable(c_sharp_statements_ResourceAcquisition.__init__)


def test_c_sharp_statements_resourceacquisition_constructor_args():
    sig = inspect.signature(c_sharp_statements_ResourceAcquisition.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_localconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_LocalConstantDeclaration)


def test_c_sharp_statements_localconstantdeclaration_constructor_exists():
    assert callable(c_sharp_statements_LocalConstantDeclaration.__init__)


def test_c_sharp_statements_localconstantdeclaration_constructor_args():
    sig = inspect.signature(c_sharp_statements_LocalConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_statements_resourceacquisition_is_not_abstract():
    assert not inspect.isabstract(statements_ResourceAcquisition)


def test_statements_resourceacquisition_constructor_exists():
    assert callable(statements_ResourceAcquisition.__init__)


def test_statements_resourceacquisition_constructor_args():
    sig = inspect.signature(statements_ResourceAcquisition.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_Expression)


def test_c_sharp_expressions_expression_constructor_exists():
    assert callable(c_sharp_expressions_Expression.__init__)


def test_c_sharp_expressions_expression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_statements_forinitializer_is_not_abstract():
    assert not inspect.isabstract(statements_ForInitializer)


def test_statements_forinitializer_constructor_exists():
    assert callable(statements_ForInitializer.__init__)


def test_statements_forinitializer_constructor_args():
    sig = inspect.signature(statements_ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_VariableDeclaration)


def test_c_sharp_statements_variabledeclaration_constructor_exists():
    assert callable(c_sharp_statements_VariableDeclaration.__init__)


def test_c_sharp_statements_variabledeclaration_constructor_args():
    sig = inspect.signature(c_sharp_statements_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_fixedpointerdeclarator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_FixedPointerDeclarator)


def test_c_sharp_statements_fixedpointerdeclarator_constructor_exists():
    assert callable(c_sharp_statements_FixedPointerDeclarator.__init__)


def test_c_sharp_statements_fixedpointerdeclarator_constructor_args():
    sig = inspect.signature(c_sharp_statements_FixedPointerDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(JumpStatement)


def test_jumpstatement_constructor_exists():
    assert callable(JumpStatement.__init__)


def test_jumpstatement_constructor_args():
    sig = inspect.signature(JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_returnstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ReturnStatement)


def test_c_sharp_statements_returnstatement_constructor_exists():
    assert callable(c_sharp_statements_ReturnStatement.__init__)


def test_c_sharp_statements_returnstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_continuestatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ContinueStatement)


def test_c_sharp_statements_continuestatement_constructor_exists():
    assert callable(c_sharp_statements_ContinueStatement.__init__)


def test_c_sharp_statements_continuestatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_gotostatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_GotoStatement)


def test_c_sharp_statements_gotostatement_constructor_exists():
    assert callable(c_sharp_statements_GotoStatement.__init__)


def test_c_sharp_statements_gotostatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_GotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_breakstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_BreakStatement)


def test_c_sharp_statements_breakstatement_constructor_exists():
    assert callable(c_sharp_statements_BreakStatement.__init__)


def test_c_sharp_statements_breakstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_forinitializer_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ForInitializer)


def test_c_sharp_statements_forinitializer_constructor_exists():
    assert callable(c_sharp_statements_ForInitializer.__init__)


def test_c_sharp_statements_forinitializer_constructor_args():
    sig = inspect.signature(c_sharp_statements_ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_finallyclause_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_FinallyClause)


def test_c_sharp_statements_finallyclause_constructor_exists():
    assert callable(c_sharp_statements_FinallyClause.__init__)


def test_c_sharp_statements_finallyclause_constructor_args():
    sig = inspect.signature(c_sharp_statements_FinallyClause.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_generalcatchclause_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_GeneralCatchClause)


def test_c_sharp_statements_generalcatchclause_constructor_exists():
    assert callable(c_sharp_statements_GeneralCatchClause.__init__)


def test_c_sharp_statements_generalcatchclause_constructor_args():
    sig = inspect.signature(c_sharp_statements_GeneralCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_specificcatchclause_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_SpecificCatchClause)


def test_c_sharp_statements_specificcatchclause_constructor_exists():
    assert callable(c_sharp_statements_SpecificCatchClause.__init__)


def test_c_sharp_statements_specificcatchclause_constructor_args():
    sig = inspect.signature(c_sharp_statements_SpecificCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_finallyclause_is_not_abstract():
    assert not inspect.isabstract(FinallyClause)


def test_finallyclause_constructor_exists():
    assert callable(FinallyClause.__init__)


def test_finallyclause_constructor_args():
    sig = inspect.signature(FinallyClause.__init__)
    params = list(sig.parameters.keys())



def test_generalcatchclause_is_not_abstract():
    assert not inspect.isabstract(GeneralCatchClause)


def test_generalcatchclause_constructor_exists():
    assert callable(GeneralCatchClause.__init__)


def test_generalcatchclause_constructor_args():
    sig = inspect.signature(GeneralCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_specificcatchclause_is_not_abstract():
    assert not inspect.isabstract(SpecificCatchClause)


def test_specificcatchclause_constructor_exists():
    assert callable(SpecificCatchClause.__init__)


def test_specificcatchclause_constructor_args():
    sig = inspect.signature(SpecificCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_throwstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ThrowStatement)


def test_c_sharp_statements_throwstatement_constructor_exists():
    assert callable(c_sharp_statements_ThrowStatement.__init__)


def test_c_sharp_statements_throwstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_default_is_not_abstract():
    assert not inspect.isabstract(Default)


def test_default_constructor_exists():
    assert callable(Default.__init__)


def test_default_constructor_args():
    sig = inspect.signature(Default.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_switchlabel_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_SwitchLabel)


def test_c_sharp_statements_switchlabel_constructor_exists():
    assert callable(c_sharp_statements_SwitchLabel.__init__)


def test_c_sharp_statements_switchlabel_constructor_args():
    sig = inspect.signature(c_sharp_statements_SwitchLabel.__init__)
    params = list(sig.parameters.keys())



def test_switchlabel_is_not_abstract():
    assert not inspect.isabstract(SwitchLabel)


def test_switchlabel_constructor_exists():
    assert callable(SwitchLabel.__init__)


def test_switchlabel_constructor_args():
    sig = inspect.signature(SwitchLabel.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_switchsection_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_SwitchSection)


def test_c_sharp_statements_switchsection_constructor_exists():
    assert callable(c_sharp_statements_SwitchSection.__init__)


def test_c_sharp_statements_switchsection_constructor_args():
    sig = inspect.signature(c_sharp_statements_SwitchSection.__init__)
    params = list(sig.parameters.keys())



def test_switchsection_is_not_abstract():
    assert not inspect.isabstract(SwitchSection)


def test_switchsection_constructor_exists():
    assert callable(SwitchSection.__init__)


def test_switchsection_constructor_args():
    sig = inspect.signature(SwitchSection.__init__)
    params = list(sig.parameters.keys())



def test_selectionstatement_is_not_abstract():
    assert not inspect.isabstract(SelectionStatement)


def test_selectionstatement_constructor_exists():
    assert callable(SelectionStatement.__init__)


def test_selectionstatement_constructor_args():
    sig = inspect.signature(SelectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_switchstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_SwitchStatement)


def test_c_sharp_statements_switchstatement_constructor_exists():
    assert callable(c_sharp_statements_SwitchStatement.__init__)


def test_c_sharp_statements_switchstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_ifstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_IfStatement)


def test_c_sharp_statements_ifstatement_constructor_exists():
    assert callable(c_sharp_statements_IfStatement.__init__)


def test_c_sharp_statements_ifstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_statementexpression_is_not_abstract():
    assert not inspect.isabstract(StatementExpression)


def test_statementexpression_constructor_exists():
    assert callable(StatementExpression.__init__)


def test_statementexpression_constructor_args():
    sig = inspect.signature(StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_predecrementexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PreDecrementExpression)


def test_c_sharp_expressions_predecrementexpression_constructor_exists():
    assert callable(c_sharp_expressions_PreDecrementExpression.__init__)


def test_c_sharp_expressions_predecrementexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PreDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_preincrementexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PreIncrementExpression)


def test_c_sharp_expressions_preincrementexpression_constructor_exists():
    assert callable(c_sharp_expressions_PreIncrementExpression.__init__)


def test_c_sharp_expressions_preincrementexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PreIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_statementexpressionlist_is_not_abstract():
    assert not inspect.isabstract(StatementExpressionList)


def test_statementexpressionlist_constructor_exists():
    assert callable(StatementExpressionList.__init__)


def test_statementexpressionlist_constructor_args():
    sig = inspect.signature(StatementExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_forinitializer_is_not_abstract():
    assert not inspect.isabstract(ForInitializer)


def test_forinitializer_constructor_exists():
    assert callable(ForInitializer.__init__)


def test_forinitializer_constructor_args():
    sig = inspect.signature(ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_statementexpressionlist_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_StatementExpressionList)


def test_c_sharp_expressions_statementexpressionlist_constructor_exists():
    assert callable(c_sharp_expressions_StatementExpressionList.__init__)


def test_c_sharp_expressions_statementexpressionlist_constructor_args():
    sig = inspect.signature(c_sharp_expressions_StatementExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_iterationstatement_is_not_abstract():
    assert not inspect.isabstract(IterationStatement)


def test_iterationstatement_constructor_exists():
    assert callable(IterationStatement.__init__)


def test_iterationstatement_constructor_args():
    sig = inspect.signature(IterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_foreachstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ForeachStatement)


def test_c_sharp_statements_foreachstatement_constructor_exists():
    assert callable(c_sharp_statements_ForeachStatement.__init__)


def test_c_sharp_statements_foreachstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_ForeachStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_dostatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_DoStatement)


def test_c_sharp_statements_dostatement_constructor_exists():
    assert callable(c_sharp_statements_DoStatement.__init__)


def test_c_sharp_statements_dostatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_forstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ForStatement)


def test_c_sharp_statements_forstatement_constructor_exists():
    assert callable(c_sharp_statements_ForStatement.__init__)


def test_c_sharp_statements_forstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_whilestatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_WhileStatement)


def test_c_sharp_statements_whilestatement_constructor_exists():
    assert callable(c_sharp_statements_WhileStatement.__init__)


def test_c_sharp_statements_whilestatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_case_is_not_abstract():
    assert not inspect.isabstract(Case)


def test_case_constructor_exists():
    assert callable(Case.__init__)


def test_case_constructor_args():
    sig = inspect.signature(Case.__init__)
    params = list(sig.parameters.keys())



def test_namedargumentlist_is_not_abstract():
    assert not inspect.isabstract(NamedArgumentList)


def test_namedargumentlist_constructor_exists():
    assert callable(NamedArgumentList.__init__)


def test_namedargumentlist_constructor_args():
    sig = inspect.signature(NamedArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_expressionlist_is_not_abstract():
    assert not inspect.isabstract(ExpressionList)


def test_expressionlist_constructor_exists():
    assert callable(ExpressionList.__init__)


def test_expressionlist_constructor_args():
    sig = inspect.signature(ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_attributes_attributearguments_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_AttributeArguments)


def test_c_sharp_attributes_attributearguments_constructor_exists():
    assert callable(c_sharp_attributes_AttributeArguments.__init__)


def test_c_sharp_attributes_attributearguments_constructor_args():
    sig = inspect.signature(c_sharp_attributes_AttributeArguments.__init__)
    params = list(sig.parameters.keys())



def test_attributearguments_is_not_abstract():
    assert not inspect.isabstract(AttributeArguments)


def test_attributearguments_constructor_exists():
    assert callable(AttributeArguments.__init__)


def test_attributearguments_constructor_args():
    sig = inspect.signature(AttributeArguments.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_attributes_attribute_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_Attribute)


def test_c_sharp_attributes_attribute_constructor_exists():
    assert callable(c_sharp_attributes_Attribute.__init__)


def test_c_sharp_attributes_attribute_constructor_args():
    sig = inspect.signature(c_sharp_attributes_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_return_is_not_abstract():
    assert not inspect.isabstract(Return)


def test_return_constructor_exists():
    assert callable(Return.__init__)


def test_return_constructor_args():
    sig = inspect.signature(Return.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_attributes_attributetarget_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_AttributeTarget)


def test_c_sharp_attributes_attributetarget_constructor_exists():
    assert callable(c_sharp_attributes_AttributeTarget.__init__)


def test_c_sharp_attributes_attributetarget_constructor_args():
    sig = inspect.signature(c_sharp_attributes_AttributeTarget.__init__)
    params = list(sig.parameters.keys())



def test_attributetarget_is_not_abstract():
    assert not inspect.isabstract(AttributeTarget)


def test_attributetarget_constructor_exists():
    assert callable(AttributeTarget.__init__)


def test_attributetarget_constructor_args():
    sig = inspect.signature(AttributeTarget.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_attributes_attributes_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_Attributes)


def test_c_sharp_attributes_attributes_constructor_exists():
    assert callable(c_sharp_attributes_Attributes.__init__)


def test_c_sharp_attributes_attributes_constructor_args():
    sig = inspect.signature(c_sharp_attributes_Attributes.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_attributes_globalattributetarget_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_GlobalAttributeTarget)


def test_c_sharp_attributes_globalattributetarget_constructor_exists():
    assert callable(c_sharp_attributes_GlobalAttributeTarget.__init__)


def test_c_sharp_attributes_globalattributetarget_constructor_args():
    sig = inspect.signature(c_sharp_attributes_GlobalAttributeTarget.__init__)
    params = list(sig.parameters.keys())



def test_unsafe_is_not_abstract():
    assert not inspect.isabstract(Unsafe)


def test_unsafe_constructor_exists():
    assert callable(Unsafe.__init__)


def test_unsafe_constructor_args():
    sig = inspect.signature(Unsafe.__init__)
    params = list(sig.parameters.keys())



def test_embeddedstatement_is_not_abstract():
    assert not inspect.isabstract(EmbeddedStatement)


def test_embeddedstatement_constructor_exists():
    assert callable(EmbeddedStatement.__init__)


def test_embeddedstatement_constructor_args():
    sig = inspect.signature(EmbeddedStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_checkedstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_CheckedStatement)


def test_c_sharp_statements_checkedstatement_constructor_exists():
    assert callable(c_sharp_statements_CheckedStatement.__init__)


def test_c_sharp_statements_checkedstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_CheckedStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_lockstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_LockStatement)


def test_c_sharp_statements_lockstatement_constructor_exists():
    assert callable(c_sharp_statements_LockStatement.__init__)


def test_c_sharp_statements_lockstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_LockStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_uncheckedstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_UncheckedStatement)


def test_c_sharp_statements_uncheckedstatement_constructor_exists():
    assert callable(c_sharp_statements_UncheckedStatement.__init__)


def test_c_sharp_statements_uncheckedstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_UncheckedStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_selectionstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_SelectionStatement)


def test_c_sharp_statements_selectionstatement_constructor_exists():
    assert callable(c_sharp_statements_SelectionStatement.__init__)


def test_c_sharp_statements_selectionstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_SelectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_usingstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_UsingStatement)


def test_c_sharp_statements_usingstatement_constructor_exists():
    assert callable(c_sharp_statements_UsingStatement.__init__)


def test_c_sharp_statements_usingstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_UsingStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_emptystatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_EmptyStatement)


def test_c_sharp_statements_emptystatement_constructor_exists():
    assert callable(c_sharp_statements_EmptyStatement.__init__)


def test_c_sharp_statements_emptystatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_iterationstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_IterationStatement)


def test_c_sharp_statements_iterationstatement_constructor_exists():
    assert callable(c_sharp_statements_IterationStatement.__init__)


def test_c_sharp_statements_iterationstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_IterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ExpressionStatement)


def test_c_sharp_statements_expressionstatement_constructor_exists():
    assert callable(c_sharp_statements_ExpressionStatement.__init__)


def test_c_sharp_statements_expressionstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_JumpStatement)


def test_c_sharp_statements_jumpstatement_constructor_exists():
    assert callable(c_sharp_statements_JumpStatement.__init__)


def test_c_sharp_statements_jumpstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_trystatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_TryStatement)


def test_c_sharp_statements_trystatement_constructor_exists():
    assert callable(c_sharp_statements_TryStatement.__init__)


def test_c_sharp_statements_trystatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_fixedstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_FixedStatement)


def test_c_sharp_statements_fixedstatement_constructor_exists():
    assert callable(c_sharp_statements_FixedStatement.__init__)


def test_c_sharp_statements_fixedstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_FixedStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_simpleembeddedstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_SimpleEmbeddedStatement)


def test_c_sharp_statements_simpleembeddedstatement_constructor_exists():
    assert callable(c_sharp_statements_SimpleEmbeddedStatement.__init__)


def test_c_sharp_statements_simpleembeddedstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_SimpleEmbeddedStatement.__init__)
    params = list(sig.parameters.keys())



def test_localconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(LocalConstantDeclaration)


def test_localconstantdeclaration_constructor_exists():
    assert callable(LocalConstantDeclaration.__init__)


def test_localconstantdeclaration_constructor_args():
    sig = inspect.signature(LocalConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_statements_statement_is_not_abstract():
    assert not inspect.isabstract(statements_Statement)


def test_statements_statement_constructor_exists():
    assert callable(statements_Statement.__init__)


def test_statements_statement_constructor_args():
    sig = inspect.signature(statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_statement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_Statement)


def test_c_sharp_statements_statement_constructor_exists():
    assert callable(c_sharp_statements_Statement.__init__)


def test_c_sharp_statements_statement_constructor_args():
    sig = inspect.signature(c_sharp_statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_attributes_namedargument_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_NamedArgument)


def test_c_sharp_attributes_namedargument_constructor_exists():
    assert callable(c_sharp_attributes_NamedArgument.__init__)


def test_c_sharp_attributes_namedargument_constructor_args():
    sig = inspect.signature(c_sharp_attributes_NamedArgument.__init__)
    params = list(sig.parameters.keys())



def test_namedargument_is_not_abstract():
    assert not inspect.isabstract(NamedArgument)


def test_namedargument_constructor_exists():
    assert callable(NamedArgument.__init__)


def test_namedargument_constructor_args():
    sig = inspect.signature(NamedArgument.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_attributes_namedargumentlist_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_NamedArgumentList)


def test_c_sharp_attributes_namedargumentlist_constructor_exists():
    assert callable(c_sharp_attributes_NamedArgumentList.__init__)


def test_c_sharp_attributes_namedargumentlist_constructor_args():
    sig = inspect.signature(c_sharp_attributes_NamedArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_constantdeclarator_is_not_abstract():
    assert not inspect.isabstract(ConstantDeclarator)


def test_constantdeclarator_constructor_exists():
    assert callable(ConstantDeclarator.__init__)


def test_constantdeclarator_constructor_args():
    sig = inspect.signature(ConstantDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_classes_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_VariableInitializer)


def test_c_sharp_classes_variableinitializer_constructor_exists():
    assert callable(c_sharp_classes_VariableInitializer.__init__)


def test_c_sharp_classes_variableinitializer_constructor_args():
    sig = inspect.signature(c_sharp_classes_VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_declarationstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_DeclarationStatement)


def test_c_sharp_statements_declarationstatement_constructor_exists():
    assert callable(c_sharp_statements_DeclarationStatement.__init__)


def test_c_sharp_statements_declarationstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_DeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_embeddedstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_EmbeddedStatement)


def test_c_sharp_statements_embeddedstatement_constructor_exists():
    assert callable(c_sharp_statements_EmbeddedStatement.__init__)


def test_c_sharp_statements_embeddedstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_EmbeddedStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_classes_block_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_Block)


def test_c_sharp_classes_block_constructor_exists():
    assert callable(c_sharp_classes_Block.__init__)


def test_c_sharp_classes_block_constructor_args():
    sig = inspect.signature(c_sharp_classes_Block.__init__)
    params = list(sig.parameters.keys())



def test_arraytype_is_not_abstract():
    assert not inspect.isabstract(ArrayType)


def test_arraytype_constructor_exists():
    assert callable(ArrayType.__init__)


def test_arraytype_constructor_args():
    sig = inspect.signature(ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_globalattributetarget_is_not_abstract():
    assert not inspect.isabstract(GlobalAttributeTarget)


def test_globalattributetarget_constructor_exists():
    assert callable(GlobalAttributeTarget.__init__)


def test_globalattributetarget_constructor_args():
    sig = inspect.signature(GlobalAttributeTarget.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_attributes_globalattributes_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_GlobalAttributes)


def test_c_sharp_attributes_globalattributes_constructor_exists():
    assert callable(c_sharp_attributes_GlobalAttributes.__init__)


def test_c_sharp_attributes_globalattributes_constructor_args():
    sig = inspect.signature(c_sharp_attributes_GlobalAttributes.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_arrays_rankspecifier_is_not_abstract():
    assert not inspect.isabstract(c_sharp_arrays_RankSpecifier)


def test_c_sharp_arrays_rankspecifier_constructor_exists():
    assert callable(c_sharp_arrays_RankSpecifier.__init__)


def test_c_sharp_arrays_rankspecifier_constructor_args():
    sig = inspect.signature(c_sharp_arrays_RankSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_rankspecifier_is_not_abstract():
    assert not inspect.isabstract(RankSpecifier)


def test_rankspecifier_constructor_exists():
    assert callable(RankSpecifier.__init__)


def test_rankspecifier_constructor_args():
    sig = inspect.signature(RankSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_nonarraytype_is_not_abstract():
    assert not inspect.isabstract(NonArrayType)


def test_nonarraytype_constructor_exists():
    assert callable(NonArrayType.__init__)


def test_nonarraytype_constructor_args():
    sig = inspect.signature(NonArrayType.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ConditionalExpression)


def test_c_sharp_expressions_conditionalexpression_constructor_exists():
    assert callable(c_sharp_expressions_ConditionalExpression.__init__)


def test_c_sharp_expressions_conditionalexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(VariableInitializer)


def test_variableinitializer_constructor_exists():
    assert callable(VariableInitializer.__init__)


def test_variableinitializer_constructor_args():
    sig = inspect.signature(VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_arrays_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(c_sharp_arrays_ArrayInitializer)


def test_c_sharp_arrays_arrayinitializer_constructor_exists():
    assert callable(c_sharp_arrays_ArrayInitializer.__init__)


def test_c_sharp_arrays_arrayinitializer_constructor_args():
    sig = inspect.signature(c_sharp_arrays_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_arrays_stackallocinitializer_is_not_abstract():
    assert not inspect.isabstract(c_sharp_arrays_StackallocInitializer)


def test_c_sharp_arrays_stackallocinitializer_constructor_exists():
    assert callable(c_sharp_arrays_StackallocInitializer.__init__)


def test_c_sharp_arrays_stackallocinitializer_constructor_args():
    sig = inspect.signature(c_sharp_arrays_StackallocInitializer.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarator_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarator)


def test_variabledeclarator_constructor_exists():
    assert callable(VariableDeclarator.__init__)


def test_variabledeclarator_constructor_args():
    sig = inspect.signature(VariableDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_formalparameterlist_is_not_abstract():
    assert not inspect.isabstract(FormalParameterList)


def test_formalparameterlist_constructor_exists():
    assert callable(FormalParameterList.__init__)


def test_formalparameterlist_constructor_args():
    sig = inspect.signature(FormalParameterList.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_arrays_arraytype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_arrays_ArrayType)


def test_c_sharp_arrays_arraytype_constructor_exists():
    assert callable(c_sharp_arrays_ArrayType.__init__)


def test_c_sharp_arrays_arraytype_constructor_args():
    sig = inspect.signature(c_sharp_arrays_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_classes_classmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_ClassMemberDeclaration)


def test_c_sharp_classes_classmemberdeclaration_constructor_exists():
    assert callable(c_sharp_classes_ClassMemberDeclaration.__init__)


def test_c_sharp_classes_classmemberdeclaration_constructor_args():
    sig = inspect.signature(c_sharp_classes_ClassMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_classorinterfaceordelegateorenumtype_is_not_abstract():
    assert not inspect.isabstract(ClassOrInterfaceOrDelegateOrEnumType)


def test_classorinterfaceordelegateorenumtype_constructor_exists():
    assert callable(ClassOrInterfaceOrDelegateOrEnumType.__init__)


def test_classorinterfaceordelegateorenumtype_constructor_args():
    sig = inspect.signature(ClassOrInterfaceOrDelegateOrEnumType.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_classes_classbase_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_ClassBase)


def test_c_sharp_classes_classbase_constructor_exists():
    assert callable(c_sharp_classes_ClassBase.__init__)


def test_c_sharp_classes_classbase_constructor_args():
    sig = inspect.signature(c_sharp_classes_ClassBase.__init__)
    params = list(sig.parameters.keys())



def test_classmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(ClassMemberDeclaration)


def test_classmemberdeclaration_constructor_exists():
    assert callable(ClassMemberDeclaration.__init__)


def test_classmemberdeclaration_constructor_args():
    sig = inspect.signature(ClassMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_classes_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_ConstantDeclaration)


def test_c_sharp_classes_constantdeclaration_constructor_exists():
    assert callable(c_sharp_classes_ConstantDeclaration.__init__)


def test_c_sharp_classes_constantdeclaration_constructor_args():
    sig = inspect.signature(c_sharp_classes_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_classes_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_FieldDeclaration)


def test_c_sharp_classes_fielddeclaration_constructor_exists():
    assert callable(c_sharp_classes_FieldDeclaration.__init__)


def test_c_sharp_classes_fielddeclaration_constructor_args():
    sig = inspect.signature(c_sharp_classes_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_params_is_not_abstract():
    assert not inspect.isabstract(Params)


def test_params_constructor_exists():
    assert callable(Params.__init__)


def test_params_constructor_args():
    sig = inspect.signature(Params.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_classes_parameterarray_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_ParameterArray)


def test_c_sharp_classes_parameterarray_constructor_exists():
    assert callable(c_sharp_classes_ParameterArray.__init__)


def test_c_sharp_classes_parameterarray_constructor_args():
    sig = inspect.signature(c_sharp_classes_ParameterArray.__init__)
    params = list(sig.parameters.keys())



def test_out_is_not_abstract():
    assert not inspect.isabstract(Out)


def test_out_constructor_exists():
    assert callable(Out.__init__)


def test_out_constructor_args():
    sig = inspect.signature(Out.__init__)
    params = list(sig.parameters.keys())



def test_ref_is_not_abstract():
    assert not inspect.isabstract(Ref)


def test_ref_constructor_exists():
    assert callable(Ref.__init__)


def test_ref_constructor_args():
    sig = inspect.signature(Ref.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_classes_fixedparameter_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_FixedParameter)


def test_c_sharp_classes_fixedparameter_constructor_exists():
    assert callable(c_sharp_classes_FixedParameter.__init__)


def test_c_sharp_classes_fixedparameter_constructor_args():
    sig = inspect.signature(c_sharp_classes_FixedParameter.__init__)
    params = list(sig.parameters.keys())



def test_parameterarray_is_not_abstract():
    assert not inspect.isabstract(ParameterArray)


def test_parameterarray_constructor_exists():
    assert callable(ParameterArray.__init__)


def test_parameterarray_constructor_args():
    sig = inspect.signature(ParameterArray.__init__)
    params = list(sig.parameters.keys())



def test_fixedparameter_is_not_abstract():
    assert not inspect.isabstract(FixedParameter)


def test_fixedparameter_constructor_exists():
    assert callable(FixedParameter.__init__)


def test_fixedparameter_constructor_args():
    sig = inspect.signature(FixedParameter.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_classes_formalparameterlist_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_FormalParameterList)


def test_c_sharp_classes_formalparameterlist_constructor_exists():
    assert callable(c_sharp_classes_FormalParameterList.__init__)


def test_c_sharp_classes_formalparameterlist_constructor_args():
    sig = inspect.signature(c_sharp_classes_FormalParameterList.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_namespacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(NamespaceMemberDeclaration)


def test_namespacememberdeclaration_constructor_exists():
    assert callable(NamespaceMemberDeclaration.__init__)


def test_namespacememberdeclaration_constructor_args():
    sig = inspect.signature(NamespaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_globalattributes_is_not_abstract():
    assert not inspect.isabstract(GlobalAttributes)


def test_globalattributes_constructor_exists():
    assert callable(GlobalAttributes.__init__)


def test_globalattributes_constructor_args():
    sig = inspect.signature(GlobalAttributes.__init__)
    params = list(sig.parameters.keys())



def test_usingdirective_is_not_abstract():
    assert not inspect.isabstract(UsingDirective)


def test_usingdirective_constructor_exists():
    assert callable(UsingDirective.__init__)


def test_usingdirective_constructor_args():
    sig = inspect.signature(UsingDirective.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_namespaces_compilationunit_is_not_abstract():
    assert not inspect.isabstract(c_sharp_namespaces_CompilationUnit)


def test_c_sharp_namespaces_compilationunit_constructor_exists():
    assert callable(c_sharp_namespaces_CompilationUnit.__init__)


def test_c_sharp_namespaces_compilationunit_constructor_args():
    sig = inspect.signature(c_sharp_namespaces_CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_expressions_primarynoarraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_PrimaryNoArrayCreationExpression)


def test_expressions_primarynoarraycreationexpression_constructor_exists():
    assert callable(expressions_PrimaryNoArrayCreationExpression.__init__)


def test_expressions_primarynoarraycreationexpression_constructor_args():
    sig = inspect.signature(expressions_PrimaryNoArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_expressions_objectcreationexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ObjectCreationExpression)


def test_c_sharp_expressions_objectcreationexpression_constructor_exists():
    assert callable(c_sharp_expressions_ObjectCreationExpression.__init__)


def test_c_sharp_expressions_objectcreationexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ObjectCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_common_namedelement_is_not_abstract():
    assert not inspect.isabstract(common_NamedElement)


def test_common_namedelement_constructor_exists():
    assert callable(common_NamedElement.__init__)


def test_common_namedelement_constructor_args():
    sig = inspect.signature(common_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_LabeledStatement)


def test_c_sharp_statements_labeledstatement_constructor_exists():
    assert callable(c_sharp_statements_LabeledStatement.__init__)


def test_c_sharp_statements_labeledstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_common_identifier_is_not_abstract():
    assert not inspect.isabstract(c_sharp_common_Identifier)


def test_c_sharp_common_identifier_constructor_exists():
    assert callable(c_sharp_common_Identifier.__init__)


def test_c_sharp_common_identifier_constructor_args():
    sig = inspect.signature(c_sharp_common_Identifier.__init__)
    params = list(sig.parameters.keys())



def test_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_common_namespaceortypename_is_not_abstract():
    assert not inspect.isabstract(c_sharp_common_NamespaceOrTypeName)


def test_c_sharp_common_namespaceortypename_constructor_exists():
    assert callable(c_sharp_common_NamespaceOrTypeName.__init__)


def test_c_sharp_common_namespaceortypename_constructor_args():
    sig = inspect.signature(c_sharp_common_NamespaceOrTypeName.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_common_namedelement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_common_NamedElement)


def test_c_sharp_common_namedelement_constructor_exists():
    assert callable(c_sharp_common_NamedElement.__init__)


def test_c_sharp_common_namedelement_constructor_args():
    sig = inspect.signature(c_sharp_common_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_c_sharp_common_namedelement_has_name():
    assert hasattr(c_sharp_common_NamedElement, "name")
    descriptor = None
    for klass in c_sharp_common_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classbase_is_not_abstract():
    assert not inspect.isabstract(ClassBase)


def test_classbase_constructor_exists():
    assert callable(ClassBase.__init__)


def test_classbase_constructor_args():
    sig = inspect.signature(ClassBase.__init__)
    params = list(sig.parameters.keys())



def test_modifier_is_not_abstract():
    assert not inspect.isabstract(Modifier)


def test_modifier_constructor_exists():
    assert callable(Modifier.__init__)


def test_modifier_constructor_args():
    sig = inspect.signature(Modifier.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_extern_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Extern)


def test_c_sharp_modifiers_extern_constructor_exists():
    assert callable(c_sharp_modifiers_Extern.__init__)


def test_c_sharp_modifiers_extern_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Extern.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_readonly_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_ReadOnly)


def test_c_sharp_modifiers_readonly_constructor_exists():
    assert callable(c_sharp_modifiers_ReadOnly.__init__)


def test_c_sharp_modifiers_readonly_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_ReadOnly.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_new_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_New)


def test_c_sharp_modifiers_new_constructor_exists():
    assert callable(c_sharp_modifiers_New.__init__)


def test_c_sharp_modifiers_new_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_New.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_partial_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Partial)


def test_c_sharp_modifiers_partial_constructor_exists():
    assert callable(c_sharp_modifiers_Partial.__init__)


def test_c_sharp_modifiers_partial_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Partial.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_volatile_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Volatile)


def test_c_sharp_modifiers_volatile_constructor_exists():
    assert callable(c_sharp_modifiers_Volatile.__init__)


def test_c_sharp_modifiers_volatile_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Volatile.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_sealed_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Sealed)


def test_c_sharp_modifiers_sealed_constructor_exists():
    assert callable(c_sharp_modifiers_Sealed.__init__)


def test_c_sharp_modifiers_sealed_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Sealed.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_private_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Private)


def test_c_sharp_modifiers_private_constructor_exists():
    assert callable(c_sharp_modifiers_Private.__init__)


def test_c_sharp_modifiers_private_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Private.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_public_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Public)


def test_c_sharp_modifiers_public_constructor_exists():
    assert callable(c_sharp_modifiers_Public.__init__)


def test_c_sharp_modifiers_public_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Public.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_abstract_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Abstract)


def test_c_sharp_modifiers_abstract_constructor_exists():
    assert callable(c_sharp_modifiers_Abstract.__init__)


def test_c_sharp_modifiers_abstract_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Abstract.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_virtual_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Virtual)


def test_c_sharp_modifiers_virtual_constructor_exists():
    assert callable(c_sharp_modifiers_Virtual.__init__)


def test_c_sharp_modifiers_virtual_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Virtual.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_overridemodifier_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_OverrideModifier)


def test_c_sharp_modifiers_overridemodifier_constructor_exists():
    assert callable(c_sharp_modifiers_OverrideModifier.__init__)


def test_c_sharp_modifiers_overridemodifier_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_OverrideModifier.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_static_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Static)


def test_c_sharp_modifiers_static_constructor_exists():
    assert callable(c_sharp_modifiers_Static.__init__)


def test_c_sharp_modifiers_static_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Static.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_protected_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Protected)


def test_c_sharp_modifiers_protected_constructor_exists():
    assert callable(c_sharp_modifiers_Protected.__init__)


def test_c_sharp_modifiers_protected_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Protected.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_internal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Internal)


def test_c_sharp_modifiers_internal_constructor_exists():
    assert callable(c_sharp_modifiers_Internal.__init__)


def test_c_sharp_modifiers_internal_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Internal.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_modifiers_unsafe_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Unsafe)


def test_c_sharp_modifiers_unsafe_constructor_exists():
    assert callable(c_sharp_modifiers_Unsafe.__init__)


def test_c_sharp_modifiers_unsafe_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Unsafe.__init__)
    params = list(sig.parameters.keys())



def test_attributes_is_not_abstract():
    assert not inspect.isabstract(Attributes)


def test_attributes_constructor_exists():
    assert callable(Attributes.__init__)


def test_attributes_constructor_args():
    sig = inspect.signature(Attributes.__init__)
    params = list(sig.parameters.keys())



def test_namespaces_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(namespaces_TypeDeclaration)


def test_namespaces_typedeclaration_constructor_exists():
    assert callable(namespaces_TypeDeclaration.__init__)


def test_namespaces_typedeclaration_constructor_args():
    sig = inspect.signature(namespaces_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_classes_class_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_Class)


def test_c_sharp_classes_class_constructor_exists():
    assert callable(c_sharp_classes_Class.__init__)


def test_c_sharp_classes_class_constructor_args():
    sig = inspect.signature(c_sharp_classes_Class.__init__)
    params = list(sig.parameters.keys())



def test_classes_classmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(classes_ClassMemberDeclaration)


def test_classes_classmemberdeclaration_constructor_exists():
    assert callable(classes_ClassMemberDeclaration.__init__)


def test_classes_classmemberdeclaration_constructor_args():
    sig = inspect.signature(classes_ClassMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_classes_method_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_Method)


def test_c_sharp_classes_method_constructor_exists():
    assert callable(c_sharp_classes_Method.__init__)


def test_c_sharp_classes_method_constructor_args():
    sig = inspect.signature(c_sharp_classes_Method.__init__)
    params = list(sig.parameters.keys())



def test_namespaces_namespacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(namespaces_NamespaceMemberDeclaration)


def test_namespaces_namespacememberdeclaration_constructor_exists():
    assert callable(namespaces_NamespaceMemberDeclaration.__init__)


def test_namespaces_namespacememberdeclaration_constructor_args():
    sig = inspect.signature(namespaces_NamespaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_namespaces_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_namespaces_TypeDeclaration)


def test_c_sharp_namespaces_typedeclaration_constructor_exists():
    assert callable(c_sharp_namespaces_TypeDeclaration.__init__)


def test_c_sharp_namespaces_typedeclaration_constructor_args():
    sig = inspect.signature(c_sharp_namespaces_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_namespaces_namespacebody_is_not_abstract():
    assert not inspect.isabstract(c_sharp_namespaces_NamespaceBody)


def test_c_sharp_namespaces_namespacebody_constructor_exists():
    assert callable(c_sharp_namespaces_NamespaceBody.__init__)


def test_c_sharp_namespaces_namespacebody_constructor_args():
    sig = inspect.signature(c_sharp_namespaces_NamespaceBody.__init__)
    params = list(sig.parameters.keys())



def test_namespacebody_is_not_abstract():
    assert not inspect.isabstract(NamespaceBody)


def test_namespacebody_constructor_exists():
    assert callable(NamespaceBody.__init__)


def test_namespacebody_constructor_args():
    sig = inspect.signature(NamespaceBody.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_namespaces_namespace_is_not_abstract():
    assert not inspect.isabstract(c_sharp_namespaces_Namespace)


def test_c_sharp_namespaces_namespace_constructor_exists():
    assert callable(c_sharp_namespaces_Namespace.__init__)


def test_c_sharp_namespaces_namespace_constructor_args():
    sig = inspect.signature(c_sharp_namespaces_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_namespaces_namespacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_namespaces_NamespaceMemberDeclaration)


def test_c_sharp_namespaces_namespacememberdeclaration_constructor_exists():
    assert callable(c_sharp_namespaces_NamespaceMemberDeclaration.__init__)


def test_c_sharp_namespaces_namespacememberdeclaration_constructor_args():
    sig = inspect.signature(c_sharp_namespaces_NamespaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_namespaceortypename_is_not_abstract():
    assert not inspect.isabstract(NamespaceOrTypeName)


def test_namespaceortypename_constructor_exists():
    assert callable(NamespaceOrTypeName.__init__)


def test_namespaceortypename_constructor_args():
    sig = inspect.signature(NamespaceOrTypeName.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_variabledeclarator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_VariableDeclarator)


def test_c_sharp_statements_variabledeclarator_constructor_exists():
    assert callable(c_sharp_statements_VariableDeclarator.__init__)


def test_c_sharp_statements_variabledeclarator_constructor_args():
    sig = inspect.signature(c_sharp_statements_VariableDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_statements_constantdeclarator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ConstantDeclarator)


def test_c_sharp_statements_constantdeclarator_constructor_exists():
    assert callable(c_sharp_statements_ConstantDeclarator.__init__)


def test_c_sharp_statements_constantdeclarator_constructor_args():
    sig = inspect.signature(c_sharp_statements_ConstantDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_c_sharp_namespaces_usingdirective_is_not_abstract():
    assert not inspect.isabstract(c_sharp_namespaces_UsingDirective)


def test_c_sharp_namespaces_usingdirective_constructor_exists():
    assert callable(c_sharp_namespaces_UsingDirective.__init__)


def test_c_sharp_namespaces_usingdirective_constructor_args():
    sig = inspect.signature(c_sharp_namespaces_UsingDirective.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
ShiftOperator_strategy = st.builds(
    ShiftOperator,
)
c_sharp_operators_RightShift_strategy = st.builds(
    c_sharp_operators_RightShift,
)
c_sharp_operators_LeftShift_strategy = st.builds(
    c_sharp_operators_LeftShift,
)
UnaryModificationOperator_strategy = st.builds(
    UnaryModificationOperator,
)
c_sharp_operators_PlusPlus_strategy = st.builds(
    c_sharp_operators_PlusPlus,
)
c_sharp_operators_MinusMinus_strategy = st.builds(
    c_sharp_operators_MinusMinus,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
c_sharp_operators_Negate_strategy = st.builds(
    c_sharp_operators_Negate,
)
c_sharp_operators_Complement_strategy = st.builds(
    c_sharp_operators_Complement,
)
MultiplicativeOperator_strategy = st.builds(
    MultiplicativeOperator,
)
c_sharp_operators_Remainder_strategy = st.builds(
    c_sharp_operators_Remainder,
)
c_sharp_operators_Multiplication_strategy = st.builds(
    c_sharp_operators_Multiplication,
)
c_sharp_operators_Division_strategy = st.builds(
    c_sharp_operators_Division,
)
operators_UnaryOperator_strategy = st.builds(
    operators_UnaryOperator,
)
operators_AdditiveOperator_strategy = st.builds(
    operators_AdditiveOperator,
)
c_sharp_operators_Subtraction_strategy = st.builds(
    c_sharp_operators_Subtraction,
)
c_sharp_operators_Addition_strategy = st.builds(
    c_sharp_operators_Addition,
)
RelationOperator_strategy = st.builds(
    RelationOperator,
)
c_sharp_operators_GreaterThanOrEqual_strategy = st.builds(
    c_sharp_operators_GreaterThanOrEqual,
)
c_sharp_operators_LessThan_strategy = st.builds(
    c_sharp_operators_LessThan,
)
c_sharp_operators_LessThanOrEqual_strategy = st.builds(
    c_sharp_operators_LessThanOrEqual,
)
c_sharp_operators_GreaterThan_strategy = st.builds(
    c_sharp_operators_GreaterThan,
)
EqualityOperator_strategy = st.builds(
    EqualityOperator,
)
c_sharp_operators_NotEqual_strategy = st.builds(
    c_sharp_operators_NotEqual,
)
c_sharp_operators_Equal_strategy = st.builds(
    c_sharp_operators_Equal,
)
c_sharp_operators_ConditionalOr_strategy = st.builds(
    c_sharp_operators_ConditionalOr,
)
c_sharp_operators_ConditionalAnd_strategy = st.builds(
    c_sharp_operators_ConditionalAnd,
)
c_sharp_operators_InclusiveOr_strategy = st.builds(
    c_sharp_operators_InclusiveOr,
)
c_sharp_operators_ExclusiveOr_strategy = st.builds(
    c_sharp_operators_ExclusiveOr,
)
c_sharp_operators_And_strategy = st.builds(
    c_sharp_operators_And,
)
c_sharp_operators_UnsignedRightShift_strategy = st.builds(
    c_sharp_operators_UnsignedRightShift,
)
Operator_strategy = st.builds(
    Operator,
)
c_sharp_operators_UnaryModificationOperator_strategy = st.builds(
    c_sharp_operators_UnaryModificationOperator,
)
c_sharp_operators_RelationOperator_strategy = st.builds(
    c_sharp_operators_RelationOperator,
)
c_sharp_operators_MultiplicativeOperator_strategy = st.builds(
    c_sharp_operators_MultiplicativeOperator,
)
c_sharp_operators_EqualityOperator_strategy = st.builds(
    c_sharp_operators_EqualityOperator,
)
c_sharp_operators_UnaryOperator_strategy = st.builds(
    c_sharp_operators_UnaryOperator,
)
c_sharp_operators_AssignmentOperator_strategy = st.builds(
    c_sharp_operators_AssignmentOperator,
)
c_sharp_operators_ShiftOperator_strategy = st.builds(
    c_sharp_operators_ShiftOperator,
)
c_sharp_operators_AdditiveOperator_strategy = st.builds(
    c_sharp_operators_AdditiveOperator,
)
c_sharp_operators_Operator_strategy = st.builds(
    c_sharp_operators_Operator,
)
c_sharp_keywords_Event_strategy = st.builds(
    c_sharp_keywords_Event,
)
c_sharp_keywords_Return_strategy = st.builds(
    c_sharp_keywords_Return,
)
c_sharp_keywords_Default_strategy = st.builds(
    c_sharp_keywords_Default,
)
c_sharp_keywords_Case_strategy = st.builds(
    c_sharp_keywords_Case,
)
c_sharp_keywords_Params_strategy = st.builds(
    c_sharp_keywords_Params,
)
c_sharp_keywords_Ref_strategy = st.builds(
    c_sharp_keywords_Ref,
)
c_sharp_keywords_Out_strategy = st.builds(
    c_sharp_keywords_Out,
)
c_sharp_modifiers_Modifier_strategy = st.builds(
    c_sharp_modifiers_Modifier,
)
ReferenceType_strategy = st.builds(
    ReferenceType,
)
c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType_strategy = st.builds(
    c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType,
)
Literal_strategy = st.builds(
    Literal,
)
c_sharp_literals_StringLiteral_strategy = st.builds(
    c_sharp_literals_StringLiteral,
    value=
        safe_text
)
c_sharp_literals_RealLiteral_strategy = st.builds(
    c_sharp_literals_RealLiteral,
    value=
        safe_text
)
c_sharp_literals_CharacterLiteral_strategy = st.builds(
    c_sharp_literals_CharacterLiteral,
    value=
        safe_text
)
c_sharp_literals_NullLiteral_strategy = st.builds(
    c_sharp_literals_NullLiteral,
)
c_sharp_literals_DecimalIntegerLiteral_strategy = st.builds(
    c_sharp_literals_DecimalIntegerLiteral,
    value=
        safe_text
)
c_sharp_literals_This_strategy = st.builds(
    c_sharp_literals_This,
)
c_sharp_literals_HexadecimalIntegerLiteral_strategy = st.builds(
    c_sharp_literals_HexadecimalIntegerLiteral,
    value=
        safe_text
)
c_sharp_literals_BooleanLiteral_strategy = st.builds(
    c_sharp_literals_BooleanLiteral,
    value=
        st.booleans()
)
InclusiveOrExpression_strategy = st.builds(
    InclusiveOrExpression,
)
c_sharp_expressions_ConditionalAndExpression_strategy = st.builds(
    c_sharp_expressions_ConditionalAndExpression,
)
InclusiveOr_strategy = st.builds(
    InclusiveOr,
)
ExclusiveOrExpression_strategy = st.builds(
    ExclusiveOrExpression,
)
c_sharp_expressions_InclusiveOrExpression_strategy = st.builds(
    c_sharp_expressions_InclusiveOrExpression,
)
ExclusiveOr_strategy = st.builds(
    ExclusiveOr,
)
AndExpression_strategy = st.builds(
    AndExpression,
)
c_sharp_expressions_ExclusiveOrExpression_strategy = st.builds(
    c_sharp_expressions_ExclusiveOrExpression,
)
And_strategy = st.builds(
    And,
)
EqualityExpression_strategy = st.builds(
    EqualityExpression,
)
c_sharp_expressions_AndExpression_strategy = st.builds(
    c_sharp_expressions_AndExpression,
)
NotEqual_strategy = st.builds(
    NotEqual,
)
Equal_strategy = st.builds(
    Equal,
)
types_Type_strategy = st.builds(
    types_Type,
)
types_NonArrayType_strategy = st.builds(
    types_NonArrayType,
)
c_sharp_types_SimpleType_strategy = st.builds(
    c_sharp_types_SimpleType,
)
c_sharp_types_PointerType_strategy = st.builds(
    c_sharp_types_PointerType,
)
c_sharp_types_ReferenceType_strategy = st.builds(
    c_sharp_types_ReferenceType,
)
c_sharp_types_NonArrayType_strategy = st.builds(
    c_sharp_types_NonArrayType,
)
c_sharp_types_Type_strategy = st.builds(
    c_sharp_types_Type,
)
ConditionalOr_strategy = st.builds(
    ConditionalOr,
)
ConditionalAndExpression_strategy = st.builds(
    ConditionalAndExpression,
)
c_sharp_expressions_ConditionalOrExpression_strategy = st.builds(
    c_sharp_expressions_ConditionalOrExpression,
)
ConditionalAnd_strategy = st.builds(
    ConditionalAnd,
)
MultiplicativeExpression_strategy = st.builds(
    MultiplicativeExpression,
)
c_sharp_expressions_AdditiveExpression_strategy = st.builds(
    c_sharp_expressions_AdditiveExpression,
)
Remainder_strategy = st.builds(
    Remainder,
)
Division_strategy = st.builds(
    Division,
)
c_sharp_expressions_MultiplicativeExpression_strategy = st.builds(
    c_sharp_expressions_MultiplicativeExpression,
)
c_sharp_expressions_AddressOfExpression_strategy = st.builds(
    c_sharp_expressions_AddressOfExpression,
)
c_sharp_expressions_CastExpression_strategy = st.builds(
    c_sharp_expressions_CastExpression,
)
RelationalExpression_strategy = st.builds(
    RelationalExpression,
)
c_sharp_expressions_EqualityExpression_strategy = st.builds(
    c_sharp_expressions_EqualityExpression,
)
GreaterThanOrEqual_strategy = st.builds(
    GreaterThanOrEqual,
)
GreaterThan_strategy = st.builds(
    GreaterThan,
)
LessThanOrEqual_strategy = st.builds(
    LessThanOrEqual,
)
LessThan_strategy = st.builds(
    LessThan,
)
ShiftExpression_strategy = st.builds(
    ShiftExpression,
)
c_sharp_expressions_RelationalExpression_strategy = st.builds(
    c_sharp_expressions_RelationalExpression,
)
AdditiveExpression_strategy = st.builds(
    AdditiveExpression,
)
LeftShift_strategy = st.builds(
    LeftShift,
)
RightShift_strategy = st.builds(
    RightShift,
)
c_sharp_expressions_ShiftExpression_strategy = st.builds(
    c_sharp_expressions_ShiftExpression,
)
AssignmentOperator_strategy = st.builds(
    AssignmentOperator,
)
c_sharp_operators_AssignmentUnsignedRightShift_strategy = st.builds(
    c_sharp_operators_AssignmentUnsignedRightShift,
)
c_sharp_operators_AssignmentAnd_strategy = st.builds(
    c_sharp_operators_AssignmentAnd,
)
c_sharp_operators_AssignmentExclusiveOr_strategy = st.builds(
    c_sharp_operators_AssignmentExclusiveOr,
)
c_sharp_operators_AssignmentLeftShift_strategy = st.builds(
    c_sharp_operators_AssignmentLeftShift,
)
c_sharp_operators_AssignmentPlus_strategy = st.builds(
    c_sharp_operators_AssignmentPlus,
)
c_sharp_operators_AssignmentDivision_strategy = st.builds(
    c_sharp_operators_AssignmentDivision,
)
c_sharp_operators_AssignmentOr_strategy = st.builds(
    c_sharp_operators_AssignmentOr,
)
c_sharp_operators_Assignment_strategy = st.builds(
    c_sharp_operators_Assignment,
)
c_sharp_operators_AssignmentRightShift_strategy = st.builds(
    c_sharp_operators_AssignmentRightShift,
)
c_sharp_operators_AssignmentMultiplication_strategy = st.builds(
    c_sharp_operators_AssignmentMultiplication,
)
c_sharp_operators_AssignmentMinus_strategy = st.builds(
    c_sharp_operators_AssignmentMinus,
)
c_sharp_operators_AssignmentModulo_strategy = st.builds(
    c_sharp_operators_AssignmentModulo,
)
expressions_Expression_strategy = st.builds(
    expressions_Expression,
)
ConditionalOrExpression_strategy = st.builds(
    ConditionalOrExpression,
)
AddressOfExpression_strategy = st.builds(
    AddressOfExpression,
)
CastExpression_strategy = st.builds(
    CastExpression,
)
PreDecrementExpression_strategy = st.builds(
    PreDecrementExpression,
)
ArrayInitializer_strategy = st.builds(
    ArrayInitializer,
)
PrimaryNoArrayCreationExpression_strategy = st.builds(
    PrimaryNoArrayCreationExpression,
)
c_sharp_literals_Literal_strategy = st.builds(
    c_sharp_literals_Literal,
)
c_sharp_expressions_TypeOfExpression_strategy = st.builds(
    c_sharp_expressions_TypeOfExpression,
)
c_sharp_expressions_SizeOfExpression_strategy = st.builds(
    c_sharp_expressions_SizeOfExpression,
)
c_sharp_expressions_UncheckedExpression_strategy = st.builds(
    c_sharp_expressions_UncheckedExpression,
)
c_sharp_expressions_DelegateCreationExpression_strategy = st.builds(
    c_sharp_expressions_DelegateCreationExpression,
)
c_sharp_expressions_CheckedExpression_strategy = st.builds(
    c_sharp_expressions_CheckedExpression,
)
c_sharp_expressions_BaseAccess_strategy = st.builds(
    c_sharp_expressions_BaseAccess,
)
PreIncrementExpression_strategy = st.builds(
    PreIncrementExpression,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
Multiplication_strategy = st.builds(
    Multiplication,
)
Complement_strategy = st.builds(
    Complement,
)
Negate_strategy = st.builds(
    Negate,
)
Subtraction_strategy = st.builds(
    Subtraction,
)
Addition_strategy = st.builds(
    Addition,
)
MemberAccess_strategy = st.builds(
    MemberAccess,
)
c_sharp_expressions_UnaryExpression_strategy = st.builds(
    c_sharp_expressions_UnaryExpression,
)
c_sharp_expressions_ParenthesizedExpression_strategy = st.builds(
    c_sharp_expressions_ParenthesizedExpression,
)
c_sharp_expressions_Argument_strategy = st.builds(
    c_sharp_expressions_Argument,
)
c_sharp_expressions_ExpressionList_strategy = st.builds(
    c_sharp_expressions_ExpressionList,
)
classes_VariableInitializer_strategy = st.builds(
    classes_VariableInitializer,
)
c_sharp_expressions_StatementExpression_strategy = st.builds(
    c_sharp_expressions_StatementExpression,
)
ArgumentList_strategy = st.builds(
    ArgumentList,
)
expressions_StatementExpression_strategy = st.builds(
    expressions_StatementExpression,
)
c_sharp_expressions_AssignmentExpression_strategy = st.builds(
    c_sharp_expressions_AssignmentExpression,
)
expressions_PrimaryExtendedExpressionType_strategy = st.builds(
    expressions_PrimaryExtendedExpressionType,
)
c_sharp_expressions_PostIncrementExpression_strategy = st.builds(
    c_sharp_expressions_PostIncrementExpression,
)
c_sharp_expressions_PostDecrementExpression_strategy = st.builds(
    c_sharp_expressions_PostDecrementExpression,
)
c_sharp_expressions_InvocationExpression_strategy = st.builds(
    c_sharp_expressions_InvocationExpression,
)
SimpleType_strategy = st.builds(
    SimpleType,
)
c_sharp_types_Byte_strategy = st.builds(
    c_sharp_types_Byte,
)
c_sharp_types_UInt_strategy = st.builds(
    c_sharp_types_UInt,
)
c_sharp_types_Float_strategy = st.builds(
    c_sharp_types_Float,
)
c_sharp_types_Short_strategy = st.builds(
    c_sharp_types_Short,
)
c_sharp_types_Object_strategy = st.builds(
    c_sharp_types_Object,
)
c_sharp_types_Void_strategy = st.builds(
    c_sharp_types_Void,
)
c_sharp_types_Bool_strategy = st.builds(
    c_sharp_types_Bool,
)
c_sharp_types_Decimal_strategy = st.builds(
    c_sharp_types_Decimal,
)
c_sharp_types_SByte_strategy = st.builds(
    c_sharp_types_SByte,
)
c_sharp_types_Double_strategy = st.builds(
    c_sharp_types_Double,
)
c_sharp_types_Char_strategy = st.builds(
    c_sharp_types_Char,
)
c_sharp_types_UShort_strategy = st.builds(
    c_sharp_types_UShort,
)
c_sharp_types_Long_strategy = st.builds(
    c_sharp_types_Long,
)
c_sharp_types_String_strategy = st.builds(
    c_sharp_types_String,
)
c_sharp_types_Int_strategy = st.builds(
    c_sharp_types_Int,
)
c_sharp_types_ULong_strategy = st.builds(
    c_sharp_types_ULong,
)
PrimaryExtendedExpressionType_strategy = st.builds(
    PrimaryExtendedExpressionType,
)
c_sharp_expressions_PointerMemberAccess_strategy = st.builds(
    c_sharp_expressions_PointerMemberAccess,
)
c_sharp_expressions_ElementAccess_strategy = st.builds(
    c_sharp_expressions_ElementAccess,
)
c_sharp_expressions_MemberAccess_strategy = st.builds(
    c_sharp_expressions_MemberAccess,
)
c_sharp_expressions_PrimaryExtendedExpressionType_strategy = st.builds(
    c_sharp_expressions_PrimaryExtendedExpressionType,
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
c_sharp_expressions_ArrayCreationExpression_strategy = st.builds(
    c_sharp_expressions_ArrayCreationExpression,
)
c_sharp_expressions_PrimaryNoArrayCreationExpression_strategy = st.builds(
    c_sharp_expressions_PrimaryNoArrayCreationExpression,
)
c_sharp_expressions_PrimaryExpression_strategy = st.builds(
    c_sharp_expressions_PrimaryExpression,
)
Argument_strategy = st.builds(
    Argument,
)
c_sharp_expressions_ArgumentList_strategy = st.builds(
    c_sharp_expressions_ArgumentList,
)
FixedPointerDeclarator_strategy = st.builds(
    FixedPointerDeclarator,
)
PointerType_strategy = st.builds(
    PointerType,
)
ResourceAcquisition_strategy = st.builds(
    ResourceAcquisition,
)
c_sharp_statements_ResourceAcquisition_strategy = st.builds(
    c_sharp_statements_ResourceAcquisition,
)
c_sharp_statements_LocalConstantDeclaration_strategy = st.builds(
    c_sharp_statements_LocalConstantDeclaration,
)
statements_ResourceAcquisition_strategy = st.builds(
    statements_ResourceAcquisition,
)
c_sharp_expressions_Expression_strategy = st.builds(
    c_sharp_expressions_Expression,
)
statements_ForInitializer_strategy = st.builds(
    statements_ForInitializer,
)
c_sharp_statements_VariableDeclaration_strategy = st.builds(
    c_sharp_statements_VariableDeclaration,
)
c_sharp_statements_FixedPointerDeclarator_strategy = st.builds(
    c_sharp_statements_FixedPointerDeclarator,
)
JumpStatement_strategy = st.builds(
    JumpStatement,
)
c_sharp_statements_ReturnStatement_strategy = st.builds(
    c_sharp_statements_ReturnStatement,
)
c_sharp_statements_ContinueStatement_strategy = st.builds(
    c_sharp_statements_ContinueStatement,
)
c_sharp_statements_GotoStatement_strategy = st.builds(
    c_sharp_statements_GotoStatement,
)
c_sharp_statements_BreakStatement_strategy = st.builds(
    c_sharp_statements_BreakStatement,
)
c_sharp_statements_ForInitializer_strategy = st.builds(
    c_sharp_statements_ForInitializer,
)
c_sharp_statements_FinallyClause_strategy = st.builds(
    c_sharp_statements_FinallyClause,
)
c_sharp_statements_GeneralCatchClause_strategy = st.builds(
    c_sharp_statements_GeneralCatchClause,
)
c_sharp_statements_SpecificCatchClause_strategy = st.builds(
    c_sharp_statements_SpecificCatchClause,
)
FinallyClause_strategy = st.builds(
    FinallyClause,
)
GeneralCatchClause_strategy = st.builds(
    GeneralCatchClause,
)
SpecificCatchClause_strategy = st.builds(
    SpecificCatchClause,
)
c_sharp_statements_ThrowStatement_strategy = st.builds(
    c_sharp_statements_ThrowStatement,
)
Default_strategy = st.builds(
    Default,
)
c_sharp_statements_SwitchLabel_strategy = st.builds(
    c_sharp_statements_SwitchLabel,
)
SwitchLabel_strategy = st.builds(
    SwitchLabel,
)
c_sharp_statements_SwitchSection_strategy = st.builds(
    c_sharp_statements_SwitchSection,
)
SwitchSection_strategy = st.builds(
    SwitchSection,
)
SelectionStatement_strategy = st.builds(
    SelectionStatement,
)
c_sharp_statements_SwitchStatement_strategy = st.builds(
    c_sharp_statements_SwitchStatement,
)
c_sharp_statements_IfStatement_strategy = st.builds(
    c_sharp_statements_IfStatement,
)
StatementExpression_strategy = st.builds(
    StatementExpression,
)
c_sharp_expressions_PreDecrementExpression_strategy = st.builds(
    c_sharp_expressions_PreDecrementExpression,
)
c_sharp_expressions_PreIncrementExpression_strategy = st.builds(
    c_sharp_expressions_PreIncrementExpression,
)
StatementExpressionList_strategy = st.builds(
    StatementExpressionList,
)
ForInitializer_strategy = st.builds(
    ForInitializer,
)
c_sharp_expressions_StatementExpressionList_strategy = st.builds(
    c_sharp_expressions_StatementExpressionList,
)
IterationStatement_strategy = st.builds(
    IterationStatement,
)
c_sharp_statements_ForeachStatement_strategy = st.builds(
    c_sharp_statements_ForeachStatement,
)
c_sharp_statements_DoStatement_strategy = st.builds(
    c_sharp_statements_DoStatement,
)
c_sharp_statements_ForStatement_strategy = st.builds(
    c_sharp_statements_ForStatement,
)
c_sharp_statements_WhileStatement_strategy = st.builds(
    c_sharp_statements_WhileStatement,
)
Case_strategy = st.builds(
    Case,
)
NamedArgumentList_strategy = st.builds(
    NamedArgumentList,
)
ExpressionList_strategy = st.builds(
    ExpressionList,
)
c_sharp_attributes_AttributeArguments_strategy = st.builds(
    c_sharp_attributes_AttributeArguments,
)
AttributeArguments_strategy = st.builds(
    AttributeArguments,
)
c_sharp_attributes_Attribute_strategy = st.builds(
    c_sharp_attributes_Attribute,
)
Return_strategy = st.builds(
    Return,
)
Event_strategy = st.builds(
    Event,
)
c_sharp_attributes_AttributeTarget_strategy = st.builds(
    c_sharp_attributes_AttributeTarget,
)
AttributeTarget_strategy = st.builds(
    AttributeTarget,
)
c_sharp_attributes_Attributes_strategy = st.builds(
    c_sharp_attributes_Attributes,
)
c_sharp_attributes_GlobalAttributeTarget_strategy = st.builds(
    c_sharp_attributes_GlobalAttributeTarget,
)
Unsafe_strategy = st.builds(
    Unsafe,
)
EmbeddedStatement_strategy = st.builds(
    EmbeddedStatement,
)
c_sharp_statements_CheckedStatement_strategy = st.builds(
    c_sharp_statements_CheckedStatement,
)
c_sharp_statements_LockStatement_strategy = st.builds(
    c_sharp_statements_LockStatement,
)
c_sharp_statements_UncheckedStatement_strategy = st.builds(
    c_sharp_statements_UncheckedStatement,
)
c_sharp_statements_SelectionStatement_strategy = st.builds(
    c_sharp_statements_SelectionStatement,
)
c_sharp_statements_UsingStatement_strategy = st.builds(
    c_sharp_statements_UsingStatement,
)
c_sharp_statements_EmptyStatement_strategy = st.builds(
    c_sharp_statements_EmptyStatement,
)
c_sharp_statements_IterationStatement_strategy = st.builds(
    c_sharp_statements_IterationStatement,
)
c_sharp_statements_ExpressionStatement_strategy = st.builds(
    c_sharp_statements_ExpressionStatement,
)
c_sharp_statements_JumpStatement_strategy = st.builds(
    c_sharp_statements_JumpStatement,
)
c_sharp_statements_TryStatement_strategy = st.builds(
    c_sharp_statements_TryStatement,
)
c_sharp_statements_FixedStatement_strategy = st.builds(
    c_sharp_statements_FixedStatement,
)
c_sharp_statements_SimpleEmbeddedStatement_strategy = st.builds(
    c_sharp_statements_SimpleEmbeddedStatement,
)
LocalConstantDeclaration_strategy = st.builds(
    LocalConstantDeclaration,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
statements_Statement_strategy = st.builds(
    statements_Statement,
)
c_sharp_statements_Statement_strategy = st.builds(
    c_sharp_statements_Statement,
)
c_sharp_attributes_NamedArgument_strategy = st.builds(
    c_sharp_attributes_NamedArgument,
)
NamedArgument_strategy = st.builds(
    NamedArgument,
)
c_sharp_attributes_NamedArgumentList_strategy = st.builds(
    c_sharp_attributes_NamedArgumentList,
)
ConstantDeclarator_strategy = st.builds(
    ConstantDeclarator,
)
c_sharp_classes_VariableInitializer_strategy = st.builds(
    c_sharp_classes_VariableInitializer,
)
Statement_strategy = st.builds(
    Statement,
)
c_sharp_statements_DeclarationStatement_strategy = st.builds(
    c_sharp_statements_DeclarationStatement,
)
c_sharp_statements_EmbeddedStatement_strategy = st.builds(
    c_sharp_statements_EmbeddedStatement,
)
c_sharp_classes_Block_strategy = st.builds(
    c_sharp_classes_Block,
)
ArrayType_strategy = st.builds(
    ArrayType,
)
Attribute_strategy = st.builds(
    Attribute,
)
GlobalAttributeTarget_strategy = st.builds(
    GlobalAttributeTarget,
)
c_sharp_attributes_GlobalAttributes_strategy = st.builds(
    c_sharp_attributes_GlobalAttributes,
)
c_sharp_arrays_RankSpecifier_strategy = st.builds(
    c_sharp_arrays_RankSpecifier,
)
RankSpecifier_strategy = st.builds(
    RankSpecifier,
)
NonArrayType_strategy = st.builds(
    NonArrayType,
)
Expression_strategy = st.builds(
    Expression,
)
c_sharp_expressions_ConditionalExpression_strategy = st.builds(
    c_sharp_expressions_ConditionalExpression,
)
VariableInitializer_strategy = st.builds(
    VariableInitializer,
)
c_sharp_arrays_ArrayInitializer_strategy = st.builds(
    c_sharp_arrays_ArrayInitializer,
)
c_sharp_arrays_StackallocInitializer_strategy = st.builds(
    c_sharp_arrays_StackallocInitializer,
)
VariableDeclarator_strategy = st.builds(
    VariableDeclarator,
)
FormalParameterList_strategy = st.builds(
    FormalParameterList,
)
Type_strategy = st.builds(
    Type,
)
c_sharp_arrays_ArrayType_strategy = st.builds(
    c_sharp_arrays_ArrayType,
)
c_sharp_classes_ClassMemberDeclaration_strategy = st.builds(
    c_sharp_classes_ClassMemberDeclaration,
)
ClassOrInterfaceOrDelegateOrEnumType_strategy = st.builds(
    ClassOrInterfaceOrDelegateOrEnumType,
)
c_sharp_classes_ClassBase_strategy = st.builds(
    c_sharp_classes_ClassBase,
)
ClassMemberDeclaration_strategy = st.builds(
    ClassMemberDeclaration,
)
c_sharp_classes_ConstantDeclaration_strategy = st.builds(
    c_sharp_classes_ConstantDeclaration,
)
c_sharp_classes_FieldDeclaration_strategy = st.builds(
    c_sharp_classes_FieldDeclaration,
)
Params_strategy = st.builds(
    Params,
)
c_sharp_classes_ParameterArray_strategy = st.builds(
    c_sharp_classes_ParameterArray,
)
Out_strategy = st.builds(
    Out,
)
Ref_strategy = st.builds(
    Ref,
)
c_sharp_classes_FixedParameter_strategy = st.builds(
    c_sharp_classes_FixedParameter,
)
ParameterArray_strategy = st.builds(
    ParameterArray,
)
FixedParameter_strategy = st.builds(
    FixedParameter,
)
c_sharp_classes_FormalParameterList_strategy = st.builds(
    c_sharp_classes_FormalParameterList,
)
Block_strategy = st.builds(
    Block,
)
NamespaceMemberDeclaration_strategy = st.builds(
    NamespaceMemberDeclaration,
)
GlobalAttributes_strategy = st.builds(
    GlobalAttributes,
)
UsingDirective_strategy = st.builds(
    UsingDirective,
)
c_sharp_namespaces_CompilationUnit_strategy = st.builds(
    c_sharp_namespaces_CompilationUnit,
)
expressions_PrimaryNoArrayCreationExpression_strategy = st.builds(
    expressions_PrimaryNoArrayCreationExpression,
)
c_sharp_expressions_ObjectCreationExpression_strategy = st.builds(
    c_sharp_expressions_ObjectCreationExpression,
)
common_NamedElement_strategy = st.builds(
    common_NamedElement,
)
c_sharp_statements_LabeledStatement_strategy = st.builds(
    c_sharp_statements_LabeledStatement,
)
c_sharp_common_Identifier_strategy = st.builds(
    c_sharp_common_Identifier,
)
Identifier_strategy = st.builds(
    Identifier,
)
c_sharp_common_NamespaceOrTypeName_strategy = st.builds(
    c_sharp_common_NamespaceOrTypeName,
)
c_sharp_common_NamedElement_strategy = st.builds(
    c_sharp_common_NamedElement,
    name=
        safe_text
)
ClassBase_strategy = st.builds(
    ClassBase,
)
Modifier_strategy = st.builds(
    Modifier,
)
c_sharp_modifiers_Extern_strategy = st.builds(
    c_sharp_modifiers_Extern,
)
c_sharp_modifiers_ReadOnly_strategy = st.builds(
    c_sharp_modifiers_ReadOnly,
)
c_sharp_modifiers_New_strategy = st.builds(
    c_sharp_modifiers_New,
)
c_sharp_modifiers_Partial_strategy = st.builds(
    c_sharp_modifiers_Partial,
)
c_sharp_modifiers_Volatile_strategy = st.builds(
    c_sharp_modifiers_Volatile,
)
c_sharp_modifiers_Sealed_strategy = st.builds(
    c_sharp_modifiers_Sealed,
)
c_sharp_modifiers_Private_strategy = st.builds(
    c_sharp_modifiers_Private,
)
c_sharp_modifiers_Public_strategy = st.builds(
    c_sharp_modifiers_Public,
)
c_sharp_modifiers_Abstract_strategy = st.builds(
    c_sharp_modifiers_Abstract,
)
c_sharp_modifiers_Virtual_strategy = st.builds(
    c_sharp_modifiers_Virtual,
)
c_sharp_modifiers_OverrideModifier_strategy = st.builds(
    c_sharp_modifiers_OverrideModifier,
)
c_sharp_modifiers_Static_strategy = st.builds(
    c_sharp_modifiers_Static,
)
c_sharp_modifiers_Protected_strategy = st.builds(
    c_sharp_modifiers_Protected,
)
c_sharp_modifiers_Internal_strategy = st.builds(
    c_sharp_modifiers_Internal,
)
c_sharp_modifiers_Unsafe_strategy = st.builds(
    c_sharp_modifiers_Unsafe,
)
Attributes_strategy = st.builds(
    Attributes,
)
namespaces_TypeDeclaration_strategy = st.builds(
    namespaces_TypeDeclaration,
)
c_sharp_classes_Class_strategy = st.builds(
    c_sharp_classes_Class,
)
classes_ClassMemberDeclaration_strategy = st.builds(
    classes_ClassMemberDeclaration,
)
c_sharp_classes_Method_strategy = st.builds(
    c_sharp_classes_Method,
)
namespaces_NamespaceMemberDeclaration_strategy = st.builds(
    namespaces_NamespaceMemberDeclaration,
)
c_sharp_namespaces_TypeDeclaration_strategy = st.builds(
    c_sharp_namespaces_TypeDeclaration,
)
c_sharp_namespaces_NamespaceBody_strategy = st.builds(
    c_sharp_namespaces_NamespaceBody,
)
NamespaceBody_strategy = st.builds(
    NamespaceBody,
)
c_sharp_namespaces_Namespace_strategy = st.builds(
    c_sharp_namespaces_Namespace,
)
c_sharp_namespaces_NamespaceMemberDeclaration_strategy = st.builds(
    c_sharp_namespaces_NamespaceMemberDeclaration,
)
NamespaceOrTypeName_strategy = st.builds(
    NamespaceOrTypeName,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
c_sharp_statements_VariableDeclarator_strategy = st.builds(
    c_sharp_statements_VariableDeclarator,
)
c_sharp_statements_ConstantDeclarator_strategy = st.builds(
    c_sharp_statements_ConstantDeclarator,
)
c_sharp_namespaces_UsingDirective_strategy = st.builds(
    c_sharp_namespaces_UsingDirective,
)

@given(instance=ShiftOperator_strategy)
@settings(max_examples=50)
def test_shiftoperator_instantiation(instance):
    assert isinstance(instance, ShiftOperator)

@given(instance=c_sharp_operators_RightShift_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_rightshift_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_RightShift)

@given(instance=c_sharp_operators_LeftShift_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_leftshift_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_LeftShift)

@given(instance=UnaryModificationOperator_strategy)
@settings(max_examples=50)
def test_unarymodificationoperator_instantiation(instance):
    assert isinstance(instance, UnaryModificationOperator)

@given(instance=c_sharp_operators_PlusPlus_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_plusplus_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_PlusPlus)

@given(instance=c_sharp_operators_MinusMinus_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_minusminus_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_MinusMinus)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=c_sharp_operators_Negate_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_negate_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Negate)

@given(instance=c_sharp_operators_Complement_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_complement_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Complement)

@given(instance=MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, MultiplicativeOperator)

@given(instance=c_sharp_operators_Remainder_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_remainder_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Remainder)

@given(instance=c_sharp_operators_Multiplication_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_multiplication_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Multiplication)

@given(instance=c_sharp_operators_Division_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_division_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Division)

@given(instance=operators_UnaryOperator_strategy)
@settings(max_examples=50)
def test_operators_unaryoperator_instantiation(instance):
    assert isinstance(instance, operators_UnaryOperator)

@given(instance=operators_AdditiveOperator_strategy)
@settings(max_examples=50)
def test_operators_additiveoperator_instantiation(instance):
    assert isinstance(instance, operators_AdditiveOperator)

@given(instance=c_sharp_operators_Subtraction_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_subtraction_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Subtraction)

@given(instance=c_sharp_operators_Addition_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_addition_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Addition)

@given(instance=RelationOperator_strategy)
@settings(max_examples=50)
def test_relationoperator_instantiation(instance):
    assert isinstance(instance, RelationOperator)

@given(instance=c_sharp_operators_GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_greaterthanorequal_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_GreaterThanOrEqual)

@given(instance=c_sharp_operators_LessThan_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_lessthan_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_LessThan)

@given(instance=c_sharp_operators_LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_lessthanorequal_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_LessThanOrEqual)

@given(instance=c_sharp_operators_GreaterThan_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_greaterthan_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_GreaterThan)

@given(instance=EqualityOperator_strategy)
@settings(max_examples=50)
def test_equalityoperator_instantiation(instance):
    assert isinstance(instance, EqualityOperator)

@given(instance=c_sharp_operators_NotEqual_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_notequal_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_NotEqual)

@given(instance=c_sharp_operators_Equal_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_equal_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Equal)

@given(instance=c_sharp_operators_ConditionalOr_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_conditionalor_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_ConditionalOr)

@given(instance=c_sharp_operators_ConditionalAnd_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_conditionaland_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_ConditionalAnd)

@given(instance=c_sharp_operators_InclusiveOr_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_inclusiveor_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_InclusiveOr)

@given(instance=c_sharp_operators_ExclusiveOr_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_exclusiveor_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_ExclusiveOr)

@given(instance=c_sharp_operators_And_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_and_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_And)

@given(instance=c_sharp_operators_UnsignedRightShift_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_unsignedrightshift_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_UnsignedRightShift)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=c_sharp_operators_UnaryModificationOperator_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_unarymodificationoperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_UnaryModificationOperator)

@given(instance=c_sharp_operators_RelationOperator_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_relationoperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_RelationOperator)

@given(instance=c_sharp_operators_MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_MultiplicativeOperator)

@given(instance=c_sharp_operators_EqualityOperator_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_equalityoperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_EqualityOperator)

@given(instance=c_sharp_operators_UnaryOperator_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_unaryoperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_UnaryOperator)

@given(instance=c_sharp_operators_AssignmentOperator_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_assignmentoperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentOperator)

@given(instance=c_sharp_operators_ShiftOperator_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_shiftoperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_ShiftOperator)

@given(instance=c_sharp_operators_AdditiveOperator_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_additiveoperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AdditiveOperator)

@given(instance=c_sharp_operators_Operator_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_operator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Operator)

@given(instance=c_sharp_keywords_Event_strategy)
@settings(max_examples=50)
def test_c_sharp_keywords_event_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Event)

@given(instance=c_sharp_keywords_Return_strategy)
@settings(max_examples=50)
def test_c_sharp_keywords_return_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Return)

@given(instance=c_sharp_keywords_Default_strategy)
@settings(max_examples=50)
def test_c_sharp_keywords_default_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Default)

@given(instance=c_sharp_keywords_Case_strategy)
@settings(max_examples=50)
def test_c_sharp_keywords_case_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Case)

@given(instance=c_sharp_keywords_Params_strategy)
@settings(max_examples=50)
def test_c_sharp_keywords_params_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Params)

@given(instance=c_sharp_keywords_Ref_strategy)
@settings(max_examples=50)
def test_c_sharp_keywords_ref_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Ref)

@given(instance=c_sharp_keywords_Out_strategy)
@settings(max_examples=50)
def test_c_sharp_keywords_out_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Out)

@given(instance=c_sharp_modifiers_Modifier_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_modifier_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Modifier)

@given(instance=ReferenceType_strategy)
@settings(max_examples=50)
def test_referencetype_instantiation(instance):
    assert isinstance(instance, ReferenceType)

@given(instance=c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType_strategy)
@settings(max_examples=50)
def test_c_sharp_types_classorinterfaceordelegateorenumtype_instantiation(instance):
    assert isinstance(instance, c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=c_sharp_literals_StringLiteral_strategy)
@settings(max_examples=50)
def test_c_sharp_literals_stringliteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_StringLiteral)



@given(instance=c_sharp_literals_StringLiteral_strategy)
def test_c_sharp_literals_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=c_sharp_literals_RealLiteral_strategy)
@settings(max_examples=50)
def test_c_sharp_literals_realliteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_RealLiteral)



@given(instance=c_sharp_literals_RealLiteral_strategy)
def test_c_sharp_literals_realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=c_sharp_literals_CharacterLiteral_strategy)
@settings(max_examples=50)
def test_c_sharp_literals_characterliteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_CharacterLiteral)



@given(instance=c_sharp_literals_CharacterLiteral_strategy)
def test_c_sharp_literals_characterliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=c_sharp_literals_NullLiteral_strategy)
@settings(max_examples=50)
def test_c_sharp_literals_nullliteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_NullLiteral)

@given(instance=c_sharp_literals_DecimalIntegerLiteral_strategy)
@settings(max_examples=50)
def test_c_sharp_literals_decimalintegerliteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_DecimalIntegerLiteral)



@given(instance=c_sharp_literals_DecimalIntegerLiteral_strategy)
def test_c_sharp_literals_decimalintegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=c_sharp_literals_This_strategy)
@settings(max_examples=50)
def test_c_sharp_literals_this_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_This)

@given(instance=c_sharp_literals_HexadecimalIntegerLiteral_strategy)
@settings(max_examples=50)
def test_c_sharp_literals_hexadecimalintegerliteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_HexadecimalIntegerLiteral)



@given(instance=c_sharp_literals_HexadecimalIntegerLiteral_strategy)
def test_c_sharp_literals_hexadecimalintegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=c_sharp_literals_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_c_sharp_literals_booleanliteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_BooleanLiteral)



@given(instance=c_sharp_literals_BooleanLiteral_strategy)
def test_c_sharp_literals_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, InclusiveOrExpression)

@given(instance=c_sharp_expressions_ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ConditionalAndExpression)

@given(instance=InclusiveOr_strategy)
@settings(max_examples=50)
def test_inclusiveor_instantiation(instance):
    assert isinstance(instance, InclusiveOr)

@given(instance=ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, ExclusiveOrExpression)

@given(instance=c_sharp_expressions_InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_InclusiveOrExpression)

@given(instance=ExclusiveOr_strategy)
@settings(max_examples=50)
def test_exclusiveor_instantiation(instance):
    assert isinstance(instance, ExclusiveOr)

@given(instance=AndExpression_strategy)
@settings(max_examples=50)
def test_andexpression_instantiation(instance):
    assert isinstance(instance, AndExpression)

@given(instance=c_sharp_expressions_ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ExclusiveOrExpression)

@given(instance=And_strategy)
@settings(max_examples=50)
def test_and_instantiation(instance):
    assert isinstance(instance, And)

@given(instance=EqualityExpression_strategy)
@settings(max_examples=50)
def test_equalityexpression_instantiation(instance):
    assert isinstance(instance, EqualityExpression)

@given(instance=c_sharp_expressions_AndExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_andexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_AndExpression)

@given(instance=NotEqual_strategy)
@settings(max_examples=50)
def test_notequal_instantiation(instance):
    assert isinstance(instance, NotEqual)

@given(instance=Equal_strategy)
@settings(max_examples=50)
def test_equal_instantiation(instance):
    assert isinstance(instance, Equal)

@given(instance=types_Type_strategy)
@settings(max_examples=50)
def test_types_type_instantiation(instance):
    assert isinstance(instance, types_Type)

@given(instance=types_NonArrayType_strategy)
@settings(max_examples=50)
def test_types_nonarraytype_instantiation(instance):
    assert isinstance(instance, types_NonArrayType)

@given(instance=c_sharp_types_SimpleType_strategy)
@settings(max_examples=50)
def test_c_sharp_types_simpletype_instantiation(instance):
    assert isinstance(instance, c_sharp_types_SimpleType)

@given(instance=c_sharp_types_PointerType_strategy)
@settings(max_examples=50)
def test_c_sharp_types_pointertype_instantiation(instance):
    assert isinstance(instance, c_sharp_types_PointerType)

@given(instance=c_sharp_types_ReferenceType_strategy)
@settings(max_examples=50)
def test_c_sharp_types_referencetype_instantiation(instance):
    assert isinstance(instance, c_sharp_types_ReferenceType)

@given(instance=c_sharp_types_NonArrayType_strategy)
@settings(max_examples=50)
def test_c_sharp_types_nonarraytype_instantiation(instance):
    assert isinstance(instance, c_sharp_types_NonArrayType)

@given(instance=c_sharp_types_Type_strategy)
@settings(max_examples=50)
def test_c_sharp_types_type_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Type)

@given(instance=ConditionalOr_strategy)
@settings(max_examples=50)
def test_conditionalor_instantiation(instance):
    assert isinstance(instance, ConditionalOr)

@given(instance=ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, ConditionalAndExpression)

@given(instance=c_sharp_expressions_ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ConditionalOrExpression)

@given(instance=ConditionalAnd_strategy)
@settings(max_examples=50)
def test_conditionaland_instantiation(instance):
    assert isinstance(instance, ConditionalAnd)

@given(instance=MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, MultiplicativeExpression)

@given(instance=c_sharp_expressions_AdditiveExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_additiveexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_AdditiveExpression)

@given(instance=Remainder_strategy)
@settings(max_examples=50)
def test_remainder_instantiation(instance):
    assert isinstance(instance, Remainder)

@given(instance=Division_strategy)
@settings(max_examples=50)
def test_division_instantiation(instance):
    assert isinstance(instance, Division)

@given(instance=c_sharp_expressions_MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_MultiplicativeExpression)

@given(instance=c_sharp_expressions_AddressOfExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_addressofexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_AddressOfExpression)

@given(instance=c_sharp_expressions_CastExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_castexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_CastExpression)

@given(instance=RelationalExpression_strategy)
@settings(max_examples=50)
def test_relationalexpression_instantiation(instance):
    assert isinstance(instance, RelationalExpression)

@given(instance=c_sharp_expressions_EqualityExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_equalityexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_EqualityExpression)

@given(instance=GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_greaterthanorequal_instantiation(instance):
    assert isinstance(instance, GreaterThanOrEqual)

@given(instance=GreaterThan_strategy)
@settings(max_examples=50)
def test_greaterthan_instantiation(instance):
    assert isinstance(instance, GreaterThan)

@given(instance=LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_lessthanorequal_instantiation(instance):
    assert isinstance(instance, LessThanOrEqual)

@given(instance=LessThan_strategy)
@settings(max_examples=50)
def test_lessthan_instantiation(instance):
    assert isinstance(instance, LessThan)

@given(instance=ShiftExpression_strategy)
@settings(max_examples=50)
def test_shiftexpression_instantiation(instance):
    assert isinstance(instance, ShiftExpression)

@given(instance=c_sharp_expressions_RelationalExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_relationalexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_RelationalExpression)

@given(instance=AdditiveExpression_strategy)
@settings(max_examples=50)
def test_additiveexpression_instantiation(instance):
    assert isinstance(instance, AdditiveExpression)

@given(instance=LeftShift_strategy)
@settings(max_examples=50)
def test_leftshift_instantiation(instance):
    assert isinstance(instance, LeftShift)

@given(instance=RightShift_strategy)
@settings(max_examples=50)
def test_rightshift_instantiation(instance):
    assert isinstance(instance, RightShift)

@given(instance=c_sharp_expressions_ShiftExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_shiftexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ShiftExpression)

@given(instance=AssignmentOperator_strategy)
@settings(max_examples=50)
def test_assignmentoperator_instantiation(instance):
    assert isinstance(instance, AssignmentOperator)

@given(instance=c_sharp_operators_AssignmentUnsignedRightShift_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_assignmentunsignedrightshift_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentUnsignedRightShift)

@given(instance=c_sharp_operators_AssignmentAnd_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_assignmentand_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentAnd)

@given(instance=c_sharp_operators_AssignmentExclusiveOr_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_assignmentexclusiveor_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentExclusiveOr)

@given(instance=c_sharp_operators_AssignmentLeftShift_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_assignmentleftshift_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentLeftShift)

@given(instance=c_sharp_operators_AssignmentPlus_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_assignmentplus_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentPlus)

@given(instance=c_sharp_operators_AssignmentDivision_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_assignmentdivision_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentDivision)

@given(instance=c_sharp_operators_AssignmentOr_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_assignmentor_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentOr)

@given(instance=c_sharp_operators_Assignment_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_assignment_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Assignment)

@given(instance=c_sharp_operators_AssignmentRightShift_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_assignmentrightshift_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentRightShift)

@given(instance=c_sharp_operators_AssignmentMultiplication_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_assignmentmultiplication_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentMultiplication)

@given(instance=c_sharp_operators_AssignmentMinus_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_assignmentminus_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentMinus)

@given(instance=c_sharp_operators_AssignmentModulo_strategy)
@settings(max_examples=50)
def test_c_sharp_operators_assignmentmodulo_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentModulo)

@given(instance=expressions_Expression_strategy)
@settings(max_examples=50)
def test_expressions_expression_instantiation(instance):
    assert isinstance(instance, expressions_Expression)

@given(instance=ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, ConditionalOrExpression)

@given(instance=AddressOfExpression_strategy)
@settings(max_examples=50)
def test_addressofexpression_instantiation(instance):
    assert isinstance(instance, AddressOfExpression)

@given(instance=CastExpression_strategy)
@settings(max_examples=50)
def test_castexpression_instantiation(instance):
    assert isinstance(instance, CastExpression)

@given(instance=PreDecrementExpression_strategy)
@settings(max_examples=50)
def test_predecrementexpression_instantiation(instance):
    assert isinstance(instance, PreDecrementExpression)

@given(instance=ArrayInitializer_strategy)
@settings(max_examples=50)
def test_arrayinitializer_instantiation(instance):
    assert isinstance(instance, ArrayInitializer)

@given(instance=PrimaryNoArrayCreationExpression_strategy)
@settings(max_examples=50)
def test_primarynoarraycreationexpression_instantiation(instance):
    assert isinstance(instance, PrimaryNoArrayCreationExpression)

@given(instance=c_sharp_literals_Literal_strategy)
@settings(max_examples=50)
def test_c_sharp_literals_literal_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_Literal)

@given(instance=c_sharp_expressions_TypeOfExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_typeofexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_TypeOfExpression)

@given(instance=c_sharp_expressions_SizeOfExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_sizeofexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_SizeOfExpression)

@given(instance=c_sharp_expressions_UncheckedExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_uncheckedexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_UncheckedExpression)

@given(instance=c_sharp_expressions_DelegateCreationExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_delegatecreationexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_DelegateCreationExpression)

@given(instance=c_sharp_expressions_CheckedExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_checkedexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_CheckedExpression)

@given(instance=c_sharp_expressions_BaseAccess_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_baseaccess_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_BaseAccess)

@given(instance=PreIncrementExpression_strategy)
@settings(max_examples=50)
def test_preincrementexpression_instantiation(instance):
    assert isinstance(instance, PreIncrementExpression)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=Multiplication_strategy)
@settings(max_examples=50)
def test_multiplication_instantiation(instance):
    assert isinstance(instance, Multiplication)

@given(instance=Complement_strategy)
@settings(max_examples=50)
def test_complement_instantiation(instance):
    assert isinstance(instance, Complement)

@given(instance=Negate_strategy)
@settings(max_examples=50)
def test_negate_instantiation(instance):
    assert isinstance(instance, Negate)

@given(instance=Subtraction_strategy)
@settings(max_examples=50)
def test_subtraction_instantiation(instance):
    assert isinstance(instance, Subtraction)

@given(instance=Addition_strategy)
@settings(max_examples=50)
def test_addition_instantiation(instance):
    assert isinstance(instance, Addition)

@given(instance=MemberAccess_strategy)
@settings(max_examples=50)
def test_memberaccess_instantiation(instance):
    assert isinstance(instance, MemberAccess)

@given(instance=c_sharp_expressions_UnaryExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_unaryexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_UnaryExpression)

@given(instance=c_sharp_expressions_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ParenthesizedExpression)

@given(instance=c_sharp_expressions_Argument_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_argument_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_Argument)

@given(instance=c_sharp_expressions_ExpressionList_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_expressionlist_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ExpressionList)

@given(instance=classes_VariableInitializer_strategy)
@settings(max_examples=50)
def test_classes_variableinitializer_instantiation(instance):
    assert isinstance(instance, classes_VariableInitializer)

@given(instance=c_sharp_expressions_StatementExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_statementexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_StatementExpression)

@given(instance=ArgumentList_strategy)
@settings(max_examples=50)
def test_argumentlist_instantiation(instance):
    assert isinstance(instance, ArgumentList)

@given(instance=expressions_StatementExpression_strategy)
@settings(max_examples=50)
def test_expressions_statementexpression_instantiation(instance):
    assert isinstance(instance, expressions_StatementExpression)

@given(instance=c_sharp_expressions_AssignmentExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_assignmentexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_AssignmentExpression)

@given(instance=expressions_PrimaryExtendedExpressionType_strategy)
@settings(max_examples=50)
def test_expressions_primaryextendedexpressiontype_instantiation(instance):
    assert isinstance(instance, expressions_PrimaryExtendedExpressionType)

@given(instance=c_sharp_expressions_PostIncrementExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_postincrementexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PostIncrementExpression)

@given(instance=c_sharp_expressions_PostDecrementExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_postdecrementexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PostDecrementExpression)

@given(instance=c_sharp_expressions_InvocationExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_invocationexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_InvocationExpression)

@given(instance=SimpleType_strategy)
@settings(max_examples=50)
def test_simpletype_instantiation(instance):
    assert isinstance(instance, SimpleType)

@given(instance=c_sharp_types_Byte_strategy)
@settings(max_examples=50)
def test_c_sharp_types_byte_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Byte)

@given(instance=c_sharp_types_UInt_strategy)
@settings(max_examples=50)
def test_c_sharp_types_uint_instantiation(instance):
    assert isinstance(instance, c_sharp_types_UInt)

@given(instance=c_sharp_types_Float_strategy)
@settings(max_examples=50)
def test_c_sharp_types_float_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Float)

@given(instance=c_sharp_types_Short_strategy)
@settings(max_examples=50)
def test_c_sharp_types_short_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Short)

@given(instance=c_sharp_types_Object_strategy)
@settings(max_examples=50)
def test_c_sharp_types_object_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Object)

@given(instance=c_sharp_types_Void_strategy)
@settings(max_examples=50)
def test_c_sharp_types_void_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Void)

@given(instance=c_sharp_types_Bool_strategy)
@settings(max_examples=50)
def test_c_sharp_types_bool_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Bool)

@given(instance=c_sharp_types_Decimal_strategy)
@settings(max_examples=50)
def test_c_sharp_types_decimal_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Decimal)

@given(instance=c_sharp_types_SByte_strategy)
@settings(max_examples=50)
def test_c_sharp_types_sbyte_instantiation(instance):
    assert isinstance(instance, c_sharp_types_SByte)

@given(instance=c_sharp_types_Double_strategy)
@settings(max_examples=50)
def test_c_sharp_types_double_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Double)

@given(instance=c_sharp_types_Char_strategy)
@settings(max_examples=50)
def test_c_sharp_types_char_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Char)

@given(instance=c_sharp_types_UShort_strategy)
@settings(max_examples=50)
def test_c_sharp_types_ushort_instantiation(instance):
    assert isinstance(instance, c_sharp_types_UShort)

@given(instance=c_sharp_types_Long_strategy)
@settings(max_examples=50)
def test_c_sharp_types_long_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Long)

@given(instance=c_sharp_types_String_strategy)
@settings(max_examples=50)
def test_c_sharp_types_string_instantiation(instance):
    assert isinstance(instance, c_sharp_types_String)

@given(instance=c_sharp_types_Int_strategy)
@settings(max_examples=50)
def test_c_sharp_types_int_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Int)

@given(instance=c_sharp_types_ULong_strategy)
@settings(max_examples=50)
def test_c_sharp_types_ulong_instantiation(instance):
    assert isinstance(instance, c_sharp_types_ULong)

@given(instance=PrimaryExtendedExpressionType_strategy)
@settings(max_examples=50)
def test_primaryextendedexpressiontype_instantiation(instance):
    assert isinstance(instance, PrimaryExtendedExpressionType)

@given(instance=c_sharp_expressions_PointerMemberAccess_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_pointermemberaccess_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PointerMemberAccess)

@given(instance=c_sharp_expressions_ElementAccess_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_elementaccess_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ElementAccess)

@given(instance=c_sharp_expressions_MemberAccess_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_memberaccess_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_MemberAccess)

@given(instance=c_sharp_expressions_PrimaryExtendedExpressionType_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_primaryextendedexpressiontype_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PrimaryExtendedExpressionType)

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=c_sharp_expressions_ArrayCreationExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_arraycreationexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ArrayCreationExpression)

@given(instance=c_sharp_expressions_PrimaryNoArrayCreationExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_primarynoarraycreationexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PrimaryNoArrayCreationExpression)

@given(instance=c_sharp_expressions_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_primaryexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PrimaryExpression)

@given(instance=Argument_strategy)
@settings(max_examples=50)
def test_argument_instantiation(instance):
    assert isinstance(instance, Argument)

@given(instance=c_sharp_expressions_ArgumentList_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_argumentlist_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ArgumentList)

@given(instance=FixedPointerDeclarator_strategy)
@settings(max_examples=50)
def test_fixedpointerdeclarator_instantiation(instance):
    assert isinstance(instance, FixedPointerDeclarator)

@given(instance=PointerType_strategy)
@settings(max_examples=50)
def test_pointertype_instantiation(instance):
    assert isinstance(instance, PointerType)

@given(instance=ResourceAcquisition_strategy)
@settings(max_examples=50)
def test_resourceacquisition_instantiation(instance):
    assert isinstance(instance, ResourceAcquisition)

@given(instance=c_sharp_statements_ResourceAcquisition_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_resourceacquisition_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ResourceAcquisition)

@given(instance=c_sharp_statements_LocalConstantDeclaration_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_localconstantdeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_LocalConstantDeclaration)

@given(instance=statements_ResourceAcquisition_strategy)
@settings(max_examples=50)
def test_statements_resourceacquisition_instantiation(instance):
    assert isinstance(instance, statements_ResourceAcquisition)

@given(instance=c_sharp_expressions_Expression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_expression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_Expression)

@given(instance=statements_ForInitializer_strategy)
@settings(max_examples=50)
def test_statements_forinitializer_instantiation(instance):
    assert isinstance(instance, statements_ForInitializer)

@given(instance=c_sharp_statements_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_variabledeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_VariableDeclaration)

@given(instance=c_sharp_statements_FixedPointerDeclarator_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_fixedpointerdeclarator_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_FixedPointerDeclarator)

@given(instance=JumpStatement_strategy)
@settings(max_examples=50)
def test_jumpstatement_instantiation(instance):
    assert isinstance(instance, JumpStatement)

@given(instance=c_sharp_statements_ReturnStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_returnstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ReturnStatement)

@given(instance=c_sharp_statements_ContinueStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_continuestatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ContinueStatement)

@given(instance=c_sharp_statements_GotoStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_gotostatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_GotoStatement)

@given(instance=c_sharp_statements_BreakStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_breakstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_BreakStatement)

@given(instance=c_sharp_statements_ForInitializer_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_forinitializer_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ForInitializer)

@given(instance=c_sharp_statements_FinallyClause_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_finallyclause_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_FinallyClause)

@given(instance=c_sharp_statements_GeneralCatchClause_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_generalcatchclause_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_GeneralCatchClause)

@given(instance=c_sharp_statements_SpecificCatchClause_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_specificcatchclause_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_SpecificCatchClause)

@given(instance=FinallyClause_strategy)
@settings(max_examples=50)
def test_finallyclause_instantiation(instance):
    assert isinstance(instance, FinallyClause)

@given(instance=GeneralCatchClause_strategy)
@settings(max_examples=50)
def test_generalcatchclause_instantiation(instance):
    assert isinstance(instance, GeneralCatchClause)

@given(instance=SpecificCatchClause_strategy)
@settings(max_examples=50)
def test_specificcatchclause_instantiation(instance):
    assert isinstance(instance, SpecificCatchClause)

@given(instance=c_sharp_statements_ThrowStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_throwstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ThrowStatement)

@given(instance=Default_strategy)
@settings(max_examples=50)
def test_default_instantiation(instance):
    assert isinstance(instance, Default)

@given(instance=c_sharp_statements_SwitchLabel_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_switchlabel_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_SwitchLabel)

@given(instance=SwitchLabel_strategy)
@settings(max_examples=50)
def test_switchlabel_instantiation(instance):
    assert isinstance(instance, SwitchLabel)

@given(instance=c_sharp_statements_SwitchSection_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_switchsection_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_SwitchSection)

@given(instance=SwitchSection_strategy)
@settings(max_examples=50)
def test_switchsection_instantiation(instance):
    assert isinstance(instance, SwitchSection)

@given(instance=SelectionStatement_strategy)
@settings(max_examples=50)
def test_selectionstatement_instantiation(instance):
    assert isinstance(instance, SelectionStatement)

@given(instance=c_sharp_statements_SwitchStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_switchstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_SwitchStatement)

@given(instance=c_sharp_statements_IfStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_ifstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_IfStatement)

@given(instance=StatementExpression_strategy)
@settings(max_examples=50)
def test_statementexpression_instantiation(instance):
    assert isinstance(instance, StatementExpression)

@given(instance=c_sharp_expressions_PreDecrementExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_predecrementexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PreDecrementExpression)

@given(instance=c_sharp_expressions_PreIncrementExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_preincrementexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PreIncrementExpression)

@given(instance=StatementExpressionList_strategy)
@settings(max_examples=50)
def test_statementexpressionlist_instantiation(instance):
    assert isinstance(instance, StatementExpressionList)

@given(instance=ForInitializer_strategy)
@settings(max_examples=50)
def test_forinitializer_instantiation(instance):
    assert isinstance(instance, ForInitializer)

@given(instance=c_sharp_expressions_StatementExpressionList_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_statementexpressionlist_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_StatementExpressionList)

@given(instance=IterationStatement_strategy)
@settings(max_examples=50)
def test_iterationstatement_instantiation(instance):
    assert isinstance(instance, IterationStatement)

@given(instance=c_sharp_statements_ForeachStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_foreachstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ForeachStatement)

@given(instance=c_sharp_statements_DoStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_dostatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_DoStatement)

@given(instance=c_sharp_statements_ForStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_forstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ForStatement)

@given(instance=c_sharp_statements_WhileStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_whilestatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_WhileStatement)

@given(instance=Case_strategy)
@settings(max_examples=50)
def test_case_instantiation(instance):
    assert isinstance(instance, Case)

@given(instance=NamedArgumentList_strategy)
@settings(max_examples=50)
def test_namedargumentlist_instantiation(instance):
    assert isinstance(instance, NamedArgumentList)

@given(instance=ExpressionList_strategy)
@settings(max_examples=50)
def test_expressionlist_instantiation(instance):
    assert isinstance(instance, ExpressionList)

@given(instance=c_sharp_attributes_AttributeArguments_strategy)
@settings(max_examples=50)
def test_c_sharp_attributes_attributearguments_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_AttributeArguments)

@given(instance=AttributeArguments_strategy)
@settings(max_examples=50)
def test_attributearguments_instantiation(instance):
    assert isinstance(instance, AttributeArguments)

@given(instance=c_sharp_attributes_Attribute_strategy)
@settings(max_examples=50)
def test_c_sharp_attributes_attribute_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_Attribute)

@given(instance=Return_strategy)
@settings(max_examples=50)
def test_return_instantiation(instance):
    assert isinstance(instance, Return)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=c_sharp_attributes_AttributeTarget_strategy)
@settings(max_examples=50)
def test_c_sharp_attributes_attributetarget_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_AttributeTarget)

@given(instance=AttributeTarget_strategy)
@settings(max_examples=50)
def test_attributetarget_instantiation(instance):
    assert isinstance(instance, AttributeTarget)

@given(instance=c_sharp_attributes_Attributes_strategy)
@settings(max_examples=50)
def test_c_sharp_attributes_attributes_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_Attributes)

@given(instance=c_sharp_attributes_GlobalAttributeTarget_strategy)
@settings(max_examples=50)
def test_c_sharp_attributes_globalattributetarget_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_GlobalAttributeTarget)

@given(instance=Unsafe_strategy)
@settings(max_examples=50)
def test_unsafe_instantiation(instance):
    assert isinstance(instance, Unsafe)

@given(instance=EmbeddedStatement_strategy)
@settings(max_examples=50)
def test_embeddedstatement_instantiation(instance):
    assert isinstance(instance, EmbeddedStatement)

@given(instance=c_sharp_statements_CheckedStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_checkedstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_CheckedStatement)

@given(instance=c_sharp_statements_LockStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_lockstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_LockStatement)

@given(instance=c_sharp_statements_UncheckedStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_uncheckedstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_UncheckedStatement)

@given(instance=c_sharp_statements_SelectionStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_selectionstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_SelectionStatement)

@given(instance=c_sharp_statements_UsingStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_usingstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_UsingStatement)

@given(instance=c_sharp_statements_EmptyStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_emptystatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_EmptyStatement)

@given(instance=c_sharp_statements_IterationStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_iterationstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_IterationStatement)

@given(instance=c_sharp_statements_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_expressionstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ExpressionStatement)

@given(instance=c_sharp_statements_JumpStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_jumpstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_JumpStatement)

@given(instance=c_sharp_statements_TryStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_trystatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_TryStatement)

@given(instance=c_sharp_statements_FixedStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_fixedstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_FixedStatement)

@given(instance=c_sharp_statements_SimpleEmbeddedStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_simpleembeddedstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_SimpleEmbeddedStatement)

@given(instance=LocalConstantDeclaration_strategy)
@settings(max_examples=50)
def test_localconstantdeclaration_instantiation(instance):
    assert isinstance(instance, LocalConstantDeclaration)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=statements_Statement_strategy)
@settings(max_examples=50)
def test_statements_statement_instantiation(instance):
    assert isinstance(instance, statements_Statement)

@given(instance=c_sharp_statements_Statement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_statement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_Statement)

@given(instance=c_sharp_attributes_NamedArgument_strategy)
@settings(max_examples=50)
def test_c_sharp_attributes_namedargument_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_NamedArgument)

@given(instance=NamedArgument_strategy)
@settings(max_examples=50)
def test_namedargument_instantiation(instance):
    assert isinstance(instance, NamedArgument)

@given(instance=c_sharp_attributes_NamedArgumentList_strategy)
@settings(max_examples=50)
def test_c_sharp_attributes_namedargumentlist_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_NamedArgumentList)

@given(instance=ConstantDeclarator_strategy)
@settings(max_examples=50)
def test_constantdeclarator_instantiation(instance):
    assert isinstance(instance, ConstantDeclarator)

@given(instance=c_sharp_classes_VariableInitializer_strategy)
@settings(max_examples=50)
def test_c_sharp_classes_variableinitializer_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_VariableInitializer)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=c_sharp_statements_DeclarationStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_declarationstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_DeclarationStatement)

@given(instance=c_sharp_statements_EmbeddedStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_embeddedstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_EmbeddedStatement)

@given(instance=c_sharp_classes_Block_strategy)
@settings(max_examples=50)
def test_c_sharp_classes_block_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_Block)

@given(instance=ArrayType_strategy)
@settings(max_examples=50)
def test_arraytype_instantiation(instance):
    assert isinstance(instance, ArrayType)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=GlobalAttributeTarget_strategy)
@settings(max_examples=50)
def test_globalattributetarget_instantiation(instance):
    assert isinstance(instance, GlobalAttributeTarget)

@given(instance=c_sharp_attributes_GlobalAttributes_strategy)
@settings(max_examples=50)
def test_c_sharp_attributes_globalattributes_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_GlobalAttributes)

@given(instance=c_sharp_arrays_RankSpecifier_strategy)
@settings(max_examples=50)
def test_c_sharp_arrays_rankspecifier_instantiation(instance):
    assert isinstance(instance, c_sharp_arrays_RankSpecifier)

@given(instance=RankSpecifier_strategy)
@settings(max_examples=50)
def test_rankspecifier_instantiation(instance):
    assert isinstance(instance, RankSpecifier)

@given(instance=NonArrayType_strategy)
@settings(max_examples=50)
def test_nonarraytype_instantiation(instance):
    assert isinstance(instance, NonArrayType)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=c_sharp_expressions_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_conditionalexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ConditionalExpression)

@given(instance=VariableInitializer_strategy)
@settings(max_examples=50)
def test_variableinitializer_instantiation(instance):
    assert isinstance(instance, VariableInitializer)

@given(instance=c_sharp_arrays_ArrayInitializer_strategy)
@settings(max_examples=50)
def test_c_sharp_arrays_arrayinitializer_instantiation(instance):
    assert isinstance(instance, c_sharp_arrays_ArrayInitializer)

@given(instance=c_sharp_arrays_StackallocInitializer_strategy)
@settings(max_examples=50)
def test_c_sharp_arrays_stackallocinitializer_instantiation(instance):
    assert isinstance(instance, c_sharp_arrays_StackallocInitializer)

@given(instance=VariableDeclarator_strategy)
@settings(max_examples=50)
def test_variabledeclarator_instantiation(instance):
    assert isinstance(instance, VariableDeclarator)

@given(instance=FormalParameterList_strategy)
@settings(max_examples=50)
def test_formalparameterlist_instantiation(instance):
    assert isinstance(instance, FormalParameterList)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=c_sharp_arrays_ArrayType_strategy)
@settings(max_examples=50)
def test_c_sharp_arrays_arraytype_instantiation(instance):
    assert isinstance(instance, c_sharp_arrays_ArrayType)

@given(instance=c_sharp_classes_ClassMemberDeclaration_strategy)
@settings(max_examples=50)
def test_c_sharp_classes_classmemberdeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_ClassMemberDeclaration)

@given(instance=ClassOrInterfaceOrDelegateOrEnumType_strategy)
@settings(max_examples=50)
def test_classorinterfaceordelegateorenumtype_instantiation(instance):
    assert isinstance(instance, ClassOrInterfaceOrDelegateOrEnumType)

@given(instance=c_sharp_classes_ClassBase_strategy)
@settings(max_examples=50)
def test_c_sharp_classes_classbase_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_ClassBase)

@given(instance=ClassMemberDeclaration_strategy)
@settings(max_examples=50)
def test_classmemberdeclaration_instantiation(instance):
    assert isinstance(instance, ClassMemberDeclaration)

@given(instance=c_sharp_classes_ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_c_sharp_classes_constantdeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_ConstantDeclaration)

@given(instance=c_sharp_classes_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_c_sharp_classes_fielddeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_FieldDeclaration)

@given(instance=Params_strategy)
@settings(max_examples=50)
def test_params_instantiation(instance):
    assert isinstance(instance, Params)

@given(instance=c_sharp_classes_ParameterArray_strategy)
@settings(max_examples=50)
def test_c_sharp_classes_parameterarray_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_ParameterArray)

@given(instance=Out_strategy)
@settings(max_examples=50)
def test_out_instantiation(instance):
    assert isinstance(instance, Out)

@given(instance=Ref_strategy)
@settings(max_examples=50)
def test_ref_instantiation(instance):
    assert isinstance(instance, Ref)

@given(instance=c_sharp_classes_FixedParameter_strategy)
@settings(max_examples=50)
def test_c_sharp_classes_fixedparameter_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_FixedParameter)

@given(instance=ParameterArray_strategy)
@settings(max_examples=50)
def test_parameterarray_instantiation(instance):
    assert isinstance(instance, ParameterArray)

@given(instance=FixedParameter_strategy)
@settings(max_examples=50)
def test_fixedparameter_instantiation(instance):
    assert isinstance(instance, FixedParameter)

@given(instance=c_sharp_classes_FormalParameterList_strategy)
@settings(max_examples=50)
def test_c_sharp_classes_formalparameterlist_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_FormalParameterList)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=NamespaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_namespacememberdeclaration_instantiation(instance):
    assert isinstance(instance, NamespaceMemberDeclaration)

@given(instance=GlobalAttributes_strategy)
@settings(max_examples=50)
def test_globalattributes_instantiation(instance):
    assert isinstance(instance, GlobalAttributes)

@given(instance=UsingDirective_strategy)
@settings(max_examples=50)
def test_usingdirective_instantiation(instance):
    assert isinstance(instance, UsingDirective)

@given(instance=c_sharp_namespaces_CompilationUnit_strategy)
@settings(max_examples=50)
def test_c_sharp_namespaces_compilationunit_instantiation(instance):
    assert isinstance(instance, c_sharp_namespaces_CompilationUnit)

@given(instance=expressions_PrimaryNoArrayCreationExpression_strategy)
@settings(max_examples=50)
def test_expressions_primarynoarraycreationexpression_instantiation(instance):
    assert isinstance(instance, expressions_PrimaryNoArrayCreationExpression)

@given(instance=c_sharp_expressions_ObjectCreationExpression_strategy)
@settings(max_examples=50)
def test_c_sharp_expressions_objectcreationexpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ObjectCreationExpression)

@given(instance=common_NamedElement_strategy)
@settings(max_examples=50)
def test_common_namedelement_instantiation(instance):
    assert isinstance(instance, common_NamedElement)

@given(instance=c_sharp_statements_LabeledStatement_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_labeledstatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_LabeledStatement)

@given(instance=c_sharp_common_Identifier_strategy)
@settings(max_examples=50)
def test_c_sharp_common_identifier_instantiation(instance):
    assert isinstance(instance, c_sharp_common_Identifier)

@given(instance=Identifier_strategy)
@settings(max_examples=50)
def test_identifier_instantiation(instance):
    assert isinstance(instance, Identifier)

@given(instance=c_sharp_common_NamespaceOrTypeName_strategy)
@settings(max_examples=50)
def test_c_sharp_common_namespaceortypename_instantiation(instance):
    assert isinstance(instance, c_sharp_common_NamespaceOrTypeName)

@given(instance=c_sharp_common_NamedElement_strategy)
@settings(max_examples=50)
def test_c_sharp_common_namedelement_instantiation(instance):
    assert isinstance(instance, c_sharp_common_NamedElement)



@given(instance=c_sharp_common_NamedElement_strategy)
def test_c_sharp_common_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassBase_strategy)
@settings(max_examples=50)
def test_classbase_instantiation(instance):
    assert isinstance(instance, ClassBase)

@given(instance=Modifier_strategy)
@settings(max_examples=50)
def test_modifier_instantiation(instance):
    assert isinstance(instance, Modifier)

@given(instance=c_sharp_modifiers_Extern_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_extern_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Extern)

@given(instance=c_sharp_modifiers_ReadOnly_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_readonly_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_ReadOnly)

@given(instance=c_sharp_modifiers_New_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_new_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_New)

@given(instance=c_sharp_modifiers_Partial_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_partial_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Partial)

@given(instance=c_sharp_modifiers_Volatile_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_volatile_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Volatile)

@given(instance=c_sharp_modifiers_Sealed_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_sealed_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Sealed)

@given(instance=c_sharp_modifiers_Private_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_private_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Private)

@given(instance=c_sharp_modifiers_Public_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_public_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Public)

@given(instance=c_sharp_modifiers_Abstract_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_abstract_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Abstract)

@given(instance=c_sharp_modifiers_Virtual_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_virtual_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Virtual)

@given(instance=c_sharp_modifiers_OverrideModifier_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_overridemodifier_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_OverrideModifier)

@given(instance=c_sharp_modifiers_Static_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_static_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Static)

@given(instance=c_sharp_modifiers_Protected_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_protected_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Protected)

@given(instance=c_sharp_modifiers_Internal_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_internal_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Internal)

@given(instance=c_sharp_modifiers_Unsafe_strategy)
@settings(max_examples=50)
def test_c_sharp_modifiers_unsafe_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Unsafe)

@given(instance=Attributes_strategy)
@settings(max_examples=50)
def test_attributes_instantiation(instance):
    assert isinstance(instance, Attributes)

@given(instance=namespaces_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_namespaces_typedeclaration_instantiation(instance):
    assert isinstance(instance, namespaces_TypeDeclaration)

@given(instance=c_sharp_classes_Class_strategy)
@settings(max_examples=50)
def test_c_sharp_classes_class_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_Class)

@given(instance=classes_ClassMemberDeclaration_strategy)
@settings(max_examples=50)
def test_classes_classmemberdeclaration_instantiation(instance):
    assert isinstance(instance, classes_ClassMemberDeclaration)

@given(instance=c_sharp_classes_Method_strategy)
@settings(max_examples=50)
def test_c_sharp_classes_method_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_Method)

@given(instance=namespaces_NamespaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_namespaces_namespacememberdeclaration_instantiation(instance):
    assert isinstance(instance, namespaces_NamespaceMemberDeclaration)

@given(instance=c_sharp_namespaces_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_c_sharp_namespaces_typedeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_namespaces_TypeDeclaration)

@given(instance=c_sharp_namespaces_NamespaceBody_strategy)
@settings(max_examples=50)
def test_c_sharp_namespaces_namespacebody_instantiation(instance):
    assert isinstance(instance, c_sharp_namespaces_NamespaceBody)

@given(instance=NamespaceBody_strategy)
@settings(max_examples=50)
def test_namespacebody_instantiation(instance):
    assert isinstance(instance, NamespaceBody)

@given(instance=c_sharp_namespaces_Namespace_strategy)
@settings(max_examples=50)
def test_c_sharp_namespaces_namespace_instantiation(instance):
    assert isinstance(instance, c_sharp_namespaces_Namespace)

@given(instance=c_sharp_namespaces_NamespaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_c_sharp_namespaces_namespacememberdeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_namespaces_NamespaceMemberDeclaration)

@given(instance=NamespaceOrTypeName_strategy)
@settings(max_examples=50)
def test_namespaceortypename_instantiation(instance):
    assert isinstance(instance, NamespaceOrTypeName)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=c_sharp_statements_VariableDeclarator_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_variabledeclarator_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_VariableDeclarator)

@given(instance=c_sharp_statements_ConstantDeclarator_strategy)
@settings(max_examples=50)
def test_c_sharp_statements_constantdeclarator_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ConstantDeclarator)

@given(instance=c_sharp_namespaces_UsingDirective_strategy)
@settings(max_examples=50)
def test_c_sharp_namespaces_usingdirective_instantiation(instance):
    assert isinstance(instance, c_sharp_namespaces_UsingDirective)
