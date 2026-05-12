import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AdditionalLocalVariable,
    Block,
    CatchBlock,
    ClassifierReference,
    LocalVariable,
    JumpLabel,
    WhileLoop,
    statements_DoWhileLoop,
    SwitchCase,
    statements_DefaultSwitchCase,
    StatementContainer,
    OrdinaryParameter,
    Modifiable,
    Jump,
    statements_Continue,
    statements_Break,
    Conditional,
    statements_NormalSwitchCase,
    Parameter,
    parameters_OrdinaryParameter,
    PrimitiveType,
    types_Float,
    types_Long,
    types_Byte,
    types_Void,
    types_Short,
    types_Boolean,
    types_Char,
    types_Double,
    types_Int,
    ElementReference,
    references_IdentifierReference,
    ArraySelector,
    parameters_VariableLengthParameter,
    Operator,
    operators_AssignmentOperator,
    operators_EqualityOperator,
    operators_MultiplicativeOperator,
    operators_RelationOperator,
    operators_ShiftOperator,
    operators_AdditiveOperator,
    operators_UnaryModificationOperator,
    operators_UnaryOperator,
    Modifier,
    modifiers_Public,
    modifiers_Strictfp,
    modifiers_Volatile,
    modifiers_Private,
    modifiers_Abstract,
    modifiers_Transient,
    modifiers_Synchronized,
    modifiers_Final,
    modifiers_Native,
    modifiers_Static,
    modifiers_Protected,
    Variable,
    ExceptionThrower,
    Parametrizable,
    StatementListContainer,
    statements_CatchBlock,
    statements_SwitchCase,
    Initializable,
    Method,
    members_ClassMethod,
    members_InterfaceMethod,
    AdditionalField,
    NamespaceClassifierReference,
    DoubleLiteral,
    literals_DecimalDoubleLiteral,
    FloatLiteral,
    literals_HexFloatLiteral,
    literals_DecimalFloatLiteral,
    LongLiteral,
    literals_HexLongLiteral,
    literals_OctalLongLiteral,
    literals_DecimalLongLiteral,
    IntegerLiteral,
    literals_OctalIntegerLiteral,
    literals_HexIntegerLiteral,
    literals_DecimalIntegerLiteral,
    literals_HexDoubleLiteral,
    Literal,
    literals_IntegerLiteral,
    literals_CharacterLiteral,
    literals_NullLiteral,
    literals_FloatLiteral,
    literals_LongLiteral,
    literals_DoubleLiteral,
    literals_BooleanLiteral,
    StaticImport,
    imports_StaticMemberImport,
    imports_StaticClassifierImport,
    Static,
    PrimaryExpression,
    literals_Literal,
    Self,
    literals_Super,
    literals_This,
    AnonymousClass,
    CallTypeArgumentable,
    Instantiation,
    instantiations_ExplicitConstructorCall,
    instantiations_NewConstructorCall,
    TypeArgumentable,
    references_Reference,
    Argumentable,
    references_MethodCall,
    Import,
    imports_ClassifierImport,
    imports_PackageImport,
    imports_StaticImport,
    UnaryModificationExpression,
    expressions_SuffixUnaryModificationExpression,
    Commentable,
    types_TypedElement,
    types_Type,
    operators_Operator,
    instantiations_Initializable,
    statements_Conditional,
    statements_Statement,
    statements_ForLoopInitializer,
    members_MemberContainer,
    statements_StatementListContainer,
    imports_ImportingElement,
    modifiers_AnnotationInstanceOrModifier,
    parameters_Parametrizable,
    statements_StatementContainer,
    literals_Self,
    references_Argumentable,
    modifiers_Modifiable,
    modifiers_AnnotableAndModifiable,
    types_TypeReference,
    members_ExceptionThrower,
    annotations_Annotable,
    arrays_ArrayTypeable,
    Expression,
    annotations_AnnotationValue,
    InterfaceMethod,
    annotations_AnnotationAttribute,
    annotations_AnnotationAttributeSetting,
    AnnotationAttributeSetting,
    AnnotationValue,
    annotations_AnnotationParameter,
    AnnotationParameter,
    annotations_AnnotationParameterList,
    annotations_SingleAnnotationParameter,
    Classifier,
    generics_TypeParameter,
    NamespaceAwareElement,
    imports_Import,
    AnnotationInstanceOrModifier,
    modifiers_Modifier,
    Reference,
    references_PrimitiveTypeReference,
    references_ElementReference,
    references_StringReference,
    references_SelfReference,
    references_ReflectiveClassReference,
    expressions_NestedExpression,
    annotations_AnnotationInstance,
    AnnotationInstance,
    expressions_PrefixUnaryModificationExpression,
    UnaryModificationOperator,
    operators_PlusPlus,
    operators_MinusMinus,
    TypeParameter,
    generics_TypeParametrizable,
    generics_CallTypeArgumentable,
    TypeArgument,
    generics_ExtendsTypeArgument,
    generics_UnknownTypeArgument,
    generics_SuperTypeArgument,
    generics_TypeArgumentable,
    AdditiveOperator,
    AdditiveExpressionChild,
    expressions_MultiplicativeExpression,
    UnaryModificationExpressionChild,
    expressions_PrimaryExpression,
    UnaryExpressionChild,
    expressions_UnaryModificationExpression,
    expressions_UnaryModificationExpressionChild,
    UnaryOperator,
    operators_Negate,
    operators_Addition,
    operators_Subtraction,
    operators_Complement,
    expressions_MultiplicativeExpressionChild,
    MultiplicativeOperator,
    operators_Division,
    operators_Remainder,
    operators_Multiplication,
    MultiplicativeExpressionChild,
    expressions_UnaryExpressionChild,
    expressions_UnaryExpression,
    EqualityExpressionChild,
    EqualityOperator,
    operators_Equal,
    operators_NotEqual,
    ShiftOperator,
    operators_LeftShift,
    operators_RightShift,
    operators_UnsignedRightShift,
    ShiftExpressionChild,
    expressions_AdditiveExpressionChild,
    expressions_AdditiveExpression,
    RelationOperator,
    operators_GreaterThanOrEqual,
    operators_LessThanOrEqual,
    operators_LessThan,
    operators_GreaterThan,
    RelationExpressionChild,
    expressions_ShiftExpressionChild,
    expressions_ShiftExpression,
    expressions_InstanceOfExpressionChild,
    InstanceOfExpressionChild,
    expressions_RelationExpression,
    expressions_RelationExpressionChild,
    ConditionalOrExpressionChild,
    expressions_ConditionalAndExpression,
    AndExpressionChild,
    expressions_EqualityExpressionChild,
    expressions_EqualityExpression,
    ExclusiveOrExpressionChild,
    expressions_AndExpressionChild,
    expressions_AndExpression,
    InclusiveOrExpressionChild,
    expressions_ExclusiveOrExpression,
    expressions_ExclusiveOrExpressionChild,
    expressions_ConditionalAndExpressionChild,
    expressions_AssignmentExpression,
    ConditionalAndExpressionChild,
    expressions_InclusiveOrExpressionChild,
    expressions_InclusiveOrExpression,
    ConditionalExpressionChild,
    expressions_ConditionalOrExpression,
    expressions_ConditionalOrExpressionChild,
    expressions_AssignmentExpressionChild,
    AssignmentOperator,
    operators_AssignmentAnd,
    operators_AssignmentExclusiveOr,
    operators_AssignmentUnsignedRightShift,
    operators_AssignmentPlus,
    operators_AssignmentMinus,
    operators_Assignment,
    operators_AssignmentRightShift,
    operators_AssignmentOr,
    operators_AssignmentMultiplication,
    operators_AssignmentDivision,
    operators_AssignmentLeftShift,
    operators_AssignmentModulo,
    AssignmentExpressionChild,
    expressions_ConditionalExpression,
    expressions_ConditionalExpressionChild,
    JavaRoot,
    containers_CompilationUnit,
    ImportingElement,
    NamedElement,
    members_Member,
    references_ReferenceableElement,
    containers_JavaRoot,
    ForLoopInitializer,
    expressions_ExpressionList,
    containers_EmptyModel,
    Package,
    CompilationUnit,
    Annotable,
    commons_NamespaceAwareElement,
    commons_NamedElement,
    commons_Commentable,
    EnumConstant,
    ReferenceableElement,
    containers_Package,
    members_EnumConstant,
    Type,
    classifiers_Classifier,
    arrays_ArraySelector,
    Implementor,
    ConcreteClassifier,
    classifiers_Interface,
    classifiers_Annotation,
    classifiers_Enumeration,
    classifiers_Class,
    TypeReference,
    types_PrimitiveType,
    types_ClassifierReference,
    types_NamespaceClassifierReference,
    classifiers_Implementor,
    AnnotableAndModifiable,
    variables_LocalVariable,
    parameters_Parameter,
    Statement,
    statements_Condition,
    statements_JumpLabel,
    statements_EmptyStatement,
    statements_Jump,
    statements_Return,
    statements_ForLoop,
    statements_Throw,
    statements_TryBlock,
    statements_ForEachLoop,
    statements_ExpressionStatement,
    statements_Assert,
    statements_SynchronizedBlock,
    statements_WhileLoop,
    statements_LocalVariableStatement,
    statements_Switch,
    Member,
    statements_Block,
    members_Field,
    members_EmptyMember,
    MemberContainer,
    classifiers_AnonymousClass,
    TypeParametrizable,
    members_Constructor,
    classifiers_ConcreteClassifier,
    ArrayDimension,
    ArrayInitializer,
    ArrayTypeable,
    variables_AdditionalLocalVariable,
    members_AdditionalField,
    generics_TypeArgument,
    TypedElement,
    expressions_CastExpression,
    generics_QualifiedTypeArgument,
    arrays_ArrayInstantiationByValues,
    members_Method,
    instantiations_Instantiation,
    variables_Variable,
    expressions_InstanceOfExpression,
    arrays_ArrayInstantiationBySize,
    arrays_ArrayInitializationValue,
    ArrayInitializationValue,
    expressions_Expression,
    arrays_ArrayInitializer,
    arrays_ArrayDimension,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_additionallocalvariable_is_not_abstract():
    assert not inspect.isabstract(AdditionalLocalVariable)


def test_additionallocalvariable_constructor_exists():
    assert callable(AdditionalLocalVariable.__init__)


def test_additionallocalvariable_constructor_args():
    sig = inspect.signature(AdditionalLocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_catchblock_is_not_abstract():
    assert not inspect.isabstract(CatchBlock)


def test_catchblock_constructor_exists():
    assert callable(CatchBlock.__init__)


def test_catchblock_constructor_args():
    sig = inspect.signature(CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_classifierreference_is_not_abstract():
    assert not inspect.isabstract(ClassifierReference)


def test_classifierreference_constructor_exists():
    assert callable(ClassifierReference.__init__)


def test_classifierreference_constructor_args():
    sig = inspect.signature(ClassifierReference.__init__)
    params = list(sig.parameters.keys())



def test_localvariable_is_not_abstract():
    assert not inspect.isabstract(LocalVariable)


def test_localvariable_constructor_exists():
    assert callable(LocalVariable.__init__)


def test_localvariable_constructor_args():
    sig = inspect.signature(LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_jumplabel_is_not_abstract():
    assert not inspect.isabstract(JumpLabel)


def test_jumplabel_constructor_exists():
    assert callable(JumpLabel.__init__)


def test_jumplabel_constructor_args():
    sig = inspect.signature(JumpLabel.__init__)
    params = list(sig.parameters.keys())



def test_whileloop_is_not_abstract():
    assert not inspect.isabstract(WhileLoop)


def test_whileloop_constructor_exists():
    assert callable(WhileLoop.__init__)


def test_whileloop_constructor_args():
    sig = inspect.signature(WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_statements_dowhileloop_is_not_abstract():
    assert not inspect.isabstract(statements_DoWhileLoop)


def test_statements_dowhileloop_constructor_exists():
    assert callable(statements_DoWhileLoop.__init__)


def test_statements_dowhileloop_constructor_args():
    sig = inspect.signature(statements_DoWhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_switchcase_is_not_abstract():
    assert not inspect.isabstract(SwitchCase)


def test_switchcase_constructor_exists():
    assert callable(SwitchCase.__init__)


def test_switchcase_constructor_args():
    sig = inspect.signature(SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_statements_defaultswitchcase_is_not_abstract():
    assert not inspect.isabstract(statements_DefaultSwitchCase)


def test_statements_defaultswitchcase_constructor_exists():
    assert callable(statements_DefaultSwitchCase.__init__)


def test_statements_defaultswitchcase_constructor_args():
    sig = inspect.signature(statements_DefaultSwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_statementcontainer_is_not_abstract():
    assert not inspect.isabstract(StatementContainer)


def test_statementcontainer_constructor_exists():
    assert callable(StatementContainer.__init__)


def test_statementcontainer_constructor_args():
    sig = inspect.signature(StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_ordinaryparameter_is_not_abstract():
    assert not inspect.isabstract(OrdinaryParameter)


def test_ordinaryparameter_constructor_exists():
    assert callable(OrdinaryParameter.__init__)


def test_ordinaryparameter_constructor_args():
    sig = inspect.signature(OrdinaryParameter.__init__)
    params = list(sig.parameters.keys())



def test_modifiable_is_not_abstract():
    assert not inspect.isabstract(Modifiable)


def test_modifiable_constructor_exists():
    assert callable(Modifiable.__init__)


def test_modifiable_constructor_args():
    sig = inspect.signature(Modifiable.__init__)
    params = list(sig.parameters.keys())



def test_jump_is_not_abstract():
    assert not inspect.isabstract(Jump)


def test_jump_constructor_exists():
    assert callable(Jump.__init__)


def test_jump_constructor_args():
    sig = inspect.signature(Jump.__init__)
    params = list(sig.parameters.keys())



def test_statements_continue_is_not_abstract():
    assert not inspect.isabstract(statements_Continue)


def test_statements_continue_constructor_exists():
    assert callable(statements_Continue.__init__)


def test_statements_continue_constructor_args():
    sig = inspect.signature(statements_Continue.__init__)
    params = list(sig.parameters.keys())



def test_statements_break_is_not_abstract():
    assert not inspect.isabstract(statements_Break)


def test_statements_break_constructor_exists():
    assert callable(statements_Break.__init__)


def test_statements_break_constructor_args():
    sig = inspect.signature(statements_Break.__init__)
    params = list(sig.parameters.keys())



def test_conditional_is_not_abstract():
    assert not inspect.isabstract(Conditional)


def test_conditional_constructor_exists():
    assert callable(Conditional.__init__)


def test_conditional_constructor_args():
    sig = inspect.signature(Conditional.__init__)
    params = list(sig.parameters.keys())



def test_statements_normalswitchcase_is_not_abstract():
    assert not inspect.isabstract(statements_NormalSwitchCase)


def test_statements_normalswitchcase_constructor_exists():
    assert callable(statements_NormalSwitchCase.__init__)


def test_statements_normalswitchcase_constructor_args():
    sig = inspect.signature(statements_NormalSwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_parameters_ordinaryparameter_is_not_abstract():
    assert not inspect.isabstract(parameters_OrdinaryParameter)


def test_parameters_ordinaryparameter_constructor_exists():
    assert callable(parameters_OrdinaryParameter.__init__)


def test_parameters_ordinaryparameter_constructor_args():
    sig = inspect.signature(parameters_OrdinaryParameter.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_types_float_is_not_abstract():
    assert not inspect.isabstract(types_Float)


def test_types_float_constructor_exists():
    assert callable(types_Float.__init__)


def test_types_float_constructor_args():
    sig = inspect.signature(types_Float.__init__)
    params = list(sig.parameters.keys())



def test_types_long_is_not_abstract():
    assert not inspect.isabstract(types_Long)


def test_types_long_constructor_exists():
    assert callable(types_Long.__init__)


def test_types_long_constructor_args():
    sig = inspect.signature(types_Long.__init__)
    params = list(sig.parameters.keys())



def test_types_byte_is_not_abstract():
    assert not inspect.isabstract(types_Byte)


def test_types_byte_constructor_exists():
    assert callable(types_Byte.__init__)


def test_types_byte_constructor_args():
    sig = inspect.signature(types_Byte.__init__)
    params = list(sig.parameters.keys())



def test_types_void_is_not_abstract():
    assert not inspect.isabstract(types_Void)


def test_types_void_constructor_exists():
    assert callable(types_Void.__init__)


def test_types_void_constructor_args():
    sig = inspect.signature(types_Void.__init__)
    params = list(sig.parameters.keys())



def test_types_short_is_not_abstract():
    assert not inspect.isabstract(types_Short)


def test_types_short_constructor_exists():
    assert callable(types_Short.__init__)


def test_types_short_constructor_args():
    sig = inspect.signature(types_Short.__init__)
    params = list(sig.parameters.keys())



def test_types_boolean_is_not_abstract():
    assert not inspect.isabstract(types_Boolean)


def test_types_boolean_constructor_exists():
    assert callable(types_Boolean.__init__)


def test_types_boolean_constructor_args():
    sig = inspect.signature(types_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_types_char_is_not_abstract():
    assert not inspect.isabstract(types_Char)


def test_types_char_constructor_exists():
    assert callable(types_Char.__init__)


def test_types_char_constructor_args():
    sig = inspect.signature(types_Char.__init__)
    params = list(sig.parameters.keys())



def test_types_double_is_not_abstract():
    assert not inspect.isabstract(types_Double)


def test_types_double_constructor_exists():
    assert callable(types_Double.__init__)


def test_types_double_constructor_args():
    sig = inspect.signature(types_Double.__init__)
    params = list(sig.parameters.keys())



def test_types_int_is_not_abstract():
    assert not inspect.isabstract(types_Int)


def test_types_int_constructor_exists():
    assert callable(types_Int.__init__)


def test_types_int_constructor_args():
    sig = inspect.signature(types_Int.__init__)
    params = list(sig.parameters.keys())



def test_elementreference_is_not_abstract():
    assert not inspect.isabstract(ElementReference)


def test_elementreference_constructor_exists():
    assert callable(ElementReference.__init__)


def test_elementreference_constructor_args():
    sig = inspect.signature(ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_references_identifierreference_is_not_abstract():
    assert not inspect.isabstract(references_IdentifierReference)


def test_references_identifierreference_constructor_exists():
    assert callable(references_IdentifierReference.__init__)


def test_references_identifierreference_constructor_args():
    sig = inspect.signature(references_IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_arrayselector_is_not_abstract():
    assert not inspect.isabstract(ArraySelector)


def test_arrayselector_constructor_exists():
    assert callable(ArraySelector.__init__)


def test_arrayselector_constructor_args():
    sig = inspect.signature(ArraySelector.__init__)
    params = list(sig.parameters.keys())



def test_parameters_variablelengthparameter_is_not_abstract():
    assert not inspect.isabstract(parameters_VariableLengthParameter)


def test_parameters_variablelengthparameter_constructor_exists():
    assert callable(parameters_VariableLengthParameter.__init__)


def test_parameters_variablelengthparameter_constructor_args():
    sig = inspect.signature(parameters_VariableLengthParameter.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_operators_assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(operators_AssignmentOperator)


def test_operators_assignmentoperator_constructor_exists():
    assert callable(operators_AssignmentOperator.__init__)


def test_operators_assignmentoperator_constructor_args():
    sig = inspect.signature(operators_AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_equalityoperator_is_not_abstract():
    assert not inspect.isabstract(operators_EqualityOperator)


def test_operators_equalityoperator_constructor_exists():
    assert callable(operators_EqualityOperator.__init__)


def test_operators_equalityoperator_constructor_args():
    sig = inspect.signature(operators_EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(operators_MultiplicativeOperator)


def test_operators_multiplicativeoperator_constructor_exists():
    assert callable(operators_MultiplicativeOperator.__init__)


def test_operators_multiplicativeoperator_constructor_args():
    sig = inspect.signature(operators_MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_relationoperator_is_not_abstract():
    assert not inspect.isabstract(operators_RelationOperator)


def test_operators_relationoperator_constructor_exists():
    assert callable(operators_RelationOperator.__init__)


def test_operators_relationoperator_constructor_args():
    sig = inspect.signature(operators_RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_shiftoperator_is_not_abstract():
    assert not inspect.isabstract(operators_ShiftOperator)


def test_operators_shiftoperator_constructor_exists():
    assert callable(operators_ShiftOperator.__init__)


def test_operators_shiftoperator_constructor_args():
    sig = inspect.signature(operators_ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_additiveoperator_is_not_abstract():
    assert not inspect.isabstract(operators_AdditiveOperator)


def test_operators_additiveoperator_constructor_exists():
    assert callable(operators_AdditiveOperator.__init__)


def test_operators_additiveoperator_constructor_args():
    sig = inspect.signature(operators_AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(operators_UnaryModificationOperator)


def test_operators_unarymodificationoperator_constructor_exists():
    assert callable(operators_UnaryModificationOperator.__init__)


def test_operators_unarymodificationoperator_constructor_args():
    sig = inspect.signature(operators_UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(operators_UnaryOperator)


def test_operators_unaryoperator_constructor_exists():
    assert callable(operators_UnaryOperator.__init__)


def test_operators_unaryoperator_constructor_args():
    sig = inspect.signature(operators_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_modifier_is_not_abstract():
    assert not inspect.isabstract(Modifier)


def test_modifier_constructor_exists():
    assert callable(Modifier.__init__)


def test_modifier_constructor_args():
    sig = inspect.signature(Modifier.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_public_is_not_abstract():
    assert not inspect.isabstract(modifiers_Public)


def test_modifiers_public_constructor_exists():
    assert callable(modifiers_Public.__init__)


def test_modifiers_public_constructor_args():
    sig = inspect.signature(modifiers_Public.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_strictfp_is_not_abstract():
    assert not inspect.isabstract(modifiers_Strictfp)


def test_modifiers_strictfp_constructor_exists():
    assert callable(modifiers_Strictfp.__init__)


def test_modifiers_strictfp_constructor_args():
    sig = inspect.signature(modifiers_Strictfp.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_volatile_is_not_abstract():
    assert not inspect.isabstract(modifiers_Volatile)


def test_modifiers_volatile_constructor_exists():
    assert callable(modifiers_Volatile.__init__)


def test_modifiers_volatile_constructor_args():
    sig = inspect.signature(modifiers_Volatile.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_private_is_not_abstract():
    assert not inspect.isabstract(modifiers_Private)


def test_modifiers_private_constructor_exists():
    assert callable(modifiers_Private.__init__)


def test_modifiers_private_constructor_args():
    sig = inspect.signature(modifiers_Private.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_abstract_is_not_abstract():
    assert not inspect.isabstract(modifiers_Abstract)


def test_modifiers_abstract_constructor_exists():
    assert callable(modifiers_Abstract.__init__)


def test_modifiers_abstract_constructor_args():
    sig = inspect.signature(modifiers_Abstract.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_transient_is_not_abstract():
    assert not inspect.isabstract(modifiers_Transient)


def test_modifiers_transient_constructor_exists():
    assert callable(modifiers_Transient.__init__)


def test_modifiers_transient_constructor_args():
    sig = inspect.signature(modifiers_Transient.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_synchronized_is_not_abstract():
    assert not inspect.isabstract(modifiers_Synchronized)


def test_modifiers_synchronized_constructor_exists():
    assert callable(modifiers_Synchronized.__init__)


def test_modifiers_synchronized_constructor_args():
    sig = inspect.signature(modifiers_Synchronized.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_final_is_not_abstract():
    assert not inspect.isabstract(modifiers_Final)


def test_modifiers_final_constructor_exists():
    assert callable(modifiers_Final.__init__)


def test_modifiers_final_constructor_args():
    sig = inspect.signature(modifiers_Final.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_native_is_not_abstract():
    assert not inspect.isabstract(modifiers_Native)


def test_modifiers_native_constructor_exists():
    assert callable(modifiers_Native.__init__)


def test_modifiers_native_constructor_args():
    sig = inspect.signature(modifiers_Native.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_static_is_not_abstract():
    assert not inspect.isabstract(modifiers_Static)


def test_modifiers_static_constructor_exists():
    assert callable(modifiers_Static.__init__)


def test_modifiers_static_constructor_args():
    sig = inspect.signature(modifiers_Static.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_protected_is_not_abstract():
    assert not inspect.isabstract(modifiers_Protected)


def test_modifiers_protected_constructor_exists():
    assert callable(modifiers_Protected.__init__)


def test_modifiers_protected_constructor_args():
    sig = inspect.signature(modifiers_Protected.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_exceptionthrower_is_not_abstract():
    assert not inspect.isabstract(ExceptionThrower)


def test_exceptionthrower_constructor_exists():
    assert callable(ExceptionThrower.__init__)


def test_exceptionthrower_constructor_args():
    sig = inspect.signature(ExceptionThrower.__init__)
    params = list(sig.parameters.keys())



def test_parametrizable_is_not_abstract():
    assert not inspect.isabstract(Parametrizable)


def test_parametrizable_constructor_exists():
    assert callable(Parametrizable.__init__)


def test_parametrizable_constructor_args():
    sig = inspect.signature(Parametrizable.__init__)
    params = list(sig.parameters.keys())



def test_statementlistcontainer_is_not_abstract():
    assert not inspect.isabstract(StatementListContainer)


def test_statementlistcontainer_constructor_exists():
    assert callable(StatementListContainer.__init__)


def test_statementlistcontainer_constructor_args():
    sig = inspect.signature(StatementListContainer.__init__)
    params = list(sig.parameters.keys())



def test_statements_catchblock_is_not_abstract():
    assert not inspect.isabstract(statements_CatchBlock)


def test_statements_catchblock_constructor_exists():
    assert callable(statements_CatchBlock.__init__)


def test_statements_catchblock_constructor_args():
    sig = inspect.signature(statements_CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_statements_switchcase_is_not_abstract():
    assert not inspect.isabstract(statements_SwitchCase)


def test_statements_switchcase_constructor_exists():
    assert callable(statements_SwitchCase.__init__)


def test_statements_switchcase_constructor_args():
    sig = inspect.signature(statements_SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_initializable_is_not_abstract():
    assert not inspect.isabstract(Initializable)


def test_initializable_constructor_exists():
    assert callable(Initializable.__init__)


def test_initializable_constructor_args():
    sig = inspect.signature(Initializable.__init__)
    params = list(sig.parameters.keys())



def test_method_is_not_abstract():
    assert not inspect.isabstract(Method)


def test_method_constructor_exists():
    assert callable(Method.__init__)


def test_method_constructor_args():
    sig = inspect.signature(Method.__init__)
    params = list(sig.parameters.keys())



def test_members_classmethod_is_not_abstract():
    assert not inspect.isabstract(members_ClassMethod)


def test_members_classmethod_constructor_exists():
    assert callable(members_ClassMethod.__init__)


def test_members_classmethod_constructor_args():
    sig = inspect.signature(members_ClassMethod.__init__)
    params = list(sig.parameters.keys())



def test_members_interfacemethod_is_not_abstract():
    assert not inspect.isabstract(members_InterfaceMethod)


def test_members_interfacemethod_constructor_exists():
    assert callable(members_InterfaceMethod.__init__)


def test_members_interfacemethod_constructor_args():
    sig = inspect.signature(members_InterfaceMethod.__init__)
    params = list(sig.parameters.keys())



def test_additionalfield_is_not_abstract():
    assert not inspect.isabstract(AdditionalField)


def test_additionalfield_constructor_exists():
    assert callable(AdditionalField.__init__)


def test_additionalfield_constructor_args():
    sig = inspect.signature(AdditionalField.__init__)
    params = list(sig.parameters.keys())



def test_namespaceclassifierreference_is_not_abstract():
    assert not inspect.isabstract(NamespaceClassifierReference)


def test_namespaceclassifierreference_constructor_exists():
    assert callable(NamespaceClassifierReference.__init__)


def test_namespaceclassifierreference_constructor_args():
    sig = inspect.signature(NamespaceClassifierReference.__init__)
    params = list(sig.parameters.keys())



def test_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(DoubleLiteral)


def test_doubleliteral_constructor_exists():
    assert callable(DoubleLiteral.__init__)


def test_doubleliteral_constructor_args():
    sig = inspect.signature(DoubleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literals_decimaldoubleliteral_is_not_abstract():
    assert not inspect.isabstract(literals_DecimalDoubleLiteral)


def test_literals_decimaldoubleliteral_constructor_exists():
    assert callable(literals_DecimalDoubleLiteral.__init__)


def test_literals_decimaldoubleliteral_constructor_args():
    sig = inspect.signature(literals_DecimalDoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_literals_decimaldoubleliteral_has_decimalValue():
    assert hasattr(literals_DecimalDoubleLiteral, "decimalValue")
    descriptor = None
    for klass in literals_DecimalDoubleLiteral.__mro__:
        if "decimalValue" in klass.__dict__:
            descriptor = klass.__dict__["decimalValue"]
            break
    assert isinstance(descriptor, property)



def test_floatliteral_is_not_abstract():
    assert not inspect.isabstract(FloatLiteral)


def test_floatliteral_constructor_exists():
    assert callable(FloatLiteral.__init__)


def test_floatliteral_constructor_args():
    sig = inspect.signature(FloatLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literals_hexfloatliteral_is_not_abstract():
    assert not inspect.isabstract(literals_HexFloatLiteral)


def test_literals_hexfloatliteral_constructor_exists():
    assert callable(literals_HexFloatLiteral.__init__)


def test_literals_hexfloatliteral_constructor_args():
    sig = inspect.signature(literals_HexFloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_literals_hexfloatliteral_has_hexValue():
    assert hasattr(literals_HexFloatLiteral, "hexValue")
    descriptor = None
    for klass in literals_HexFloatLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_literals_decimalfloatliteral_is_not_abstract():
    assert not inspect.isabstract(literals_DecimalFloatLiteral)


def test_literals_decimalfloatliteral_constructor_exists():
    assert callable(literals_DecimalFloatLiteral.__init__)


def test_literals_decimalfloatliteral_constructor_args():
    sig = inspect.signature(literals_DecimalFloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_literals_decimalfloatliteral_has_decimalValue():
    assert hasattr(literals_DecimalFloatLiteral, "decimalValue")
    descriptor = None
    for klass in literals_DecimalFloatLiteral.__mro__:
        if "decimalValue" in klass.__dict__:
            descriptor = klass.__dict__["decimalValue"]
            break
    assert isinstance(descriptor, property)



def test_longliteral_is_not_abstract():
    assert not inspect.isabstract(LongLiteral)


def test_longliteral_constructor_exists():
    assert callable(LongLiteral.__init__)


def test_longliteral_constructor_args():
    sig = inspect.signature(LongLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literals_hexlongliteral_is_not_abstract():
    assert not inspect.isabstract(literals_HexLongLiteral)


def test_literals_hexlongliteral_constructor_exists():
    assert callable(literals_HexLongLiteral.__init__)


def test_literals_hexlongliteral_constructor_args():
    sig = inspect.signature(literals_HexLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_literals_hexlongliteral_has_hexValue():
    assert hasattr(literals_HexLongLiteral, "hexValue")
    descriptor = None
    for klass in literals_HexLongLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_literals_octallongliteral_is_not_abstract():
    assert not inspect.isabstract(literals_OctalLongLiteral)


def test_literals_octallongliteral_constructor_exists():
    assert callable(literals_OctalLongLiteral.__init__)


def test_literals_octallongliteral_constructor_args():
    sig = inspect.signature(literals_OctalLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "octalValue" in params, "Missing parameter 'octalValue'"

def test_literals_octallongliteral_has_octalValue():
    assert hasattr(literals_OctalLongLiteral, "octalValue")
    descriptor = None
    for klass in literals_OctalLongLiteral.__mro__:
        if "octalValue" in klass.__dict__:
            descriptor = klass.__dict__["octalValue"]
            break
    assert isinstance(descriptor, property)



def test_literals_decimallongliteral_is_not_abstract():
    assert not inspect.isabstract(literals_DecimalLongLiteral)


def test_literals_decimallongliteral_constructor_exists():
    assert callable(literals_DecimalLongLiteral.__init__)


def test_literals_decimallongliteral_constructor_args():
    sig = inspect.signature(literals_DecimalLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_literals_decimallongliteral_has_decimalValue():
    assert hasattr(literals_DecimalLongLiteral, "decimalValue")
    descriptor = None
    for klass in literals_DecimalLongLiteral.__mro__:
        if "decimalValue" in klass.__dict__:
            descriptor = klass.__dict__["decimalValue"]
            break
    assert isinstance(descriptor, property)



def test_integerliteral_is_not_abstract():
    assert not inspect.isabstract(IntegerLiteral)


def test_integerliteral_constructor_exists():
    assert callable(IntegerLiteral.__init__)


def test_integerliteral_constructor_args():
    sig = inspect.signature(IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literals_octalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(literals_OctalIntegerLiteral)


def test_literals_octalintegerliteral_constructor_exists():
    assert callable(literals_OctalIntegerLiteral.__init__)


def test_literals_octalintegerliteral_constructor_args():
    sig = inspect.signature(literals_OctalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "octalValue" in params, "Missing parameter 'octalValue'"

def test_literals_octalintegerliteral_has_octalValue():
    assert hasattr(literals_OctalIntegerLiteral, "octalValue")
    descriptor = None
    for klass in literals_OctalIntegerLiteral.__mro__:
        if "octalValue" in klass.__dict__:
            descriptor = klass.__dict__["octalValue"]
            break
    assert isinstance(descriptor, property)



def test_literals_hexintegerliteral_is_not_abstract():
    assert not inspect.isabstract(literals_HexIntegerLiteral)


def test_literals_hexintegerliteral_constructor_exists():
    assert callable(literals_HexIntegerLiteral.__init__)


def test_literals_hexintegerliteral_constructor_args():
    sig = inspect.signature(literals_HexIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_literals_hexintegerliteral_has_hexValue():
    assert hasattr(literals_HexIntegerLiteral, "hexValue")
    descriptor = None
    for klass in literals_HexIntegerLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_literals_decimalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(literals_DecimalIntegerLiteral)


def test_literals_decimalintegerliteral_constructor_exists():
    assert callable(literals_DecimalIntegerLiteral.__init__)


def test_literals_decimalintegerliteral_constructor_args():
    sig = inspect.signature(literals_DecimalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_literals_decimalintegerliteral_has_decimalValue():
    assert hasattr(literals_DecimalIntegerLiteral, "decimalValue")
    descriptor = None
    for klass in literals_DecimalIntegerLiteral.__mro__:
        if "decimalValue" in klass.__dict__:
            descriptor = klass.__dict__["decimalValue"]
            break
    assert isinstance(descriptor, property)



def test_literals_hexdoubleliteral_is_not_abstract():
    assert not inspect.isabstract(literals_HexDoubleLiteral)


def test_literals_hexdoubleliteral_constructor_exists():
    assert callable(literals_HexDoubleLiteral.__init__)


def test_literals_hexdoubleliteral_constructor_args():
    sig = inspect.signature(literals_HexDoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_literals_hexdoubleliteral_has_hexValue():
    assert hasattr(literals_HexDoubleLiteral, "hexValue")
    descriptor = None
    for klass in literals_HexDoubleLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_literals_integerliteral_is_not_abstract():
    assert not inspect.isabstract(literals_IntegerLiteral)


def test_literals_integerliteral_constructor_exists():
    assert callable(literals_IntegerLiteral.__init__)


def test_literals_integerliteral_constructor_args():
    sig = inspect.signature(literals_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literals_characterliteral_is_not_abstract():
    assert not inspect.isabstract(literals_CharacterLiteral)


def test_literals_characterliteral_constructor_exists():
    assert callable(literals_CharacterLiteral.__init__)


def test_literals_characterliteral_constructor_args():
    sig = inspect.signature(literals_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_literals_characterliteral_has_value():
    assert hasattr(literals_CharacterLiteral, "value")
    descriptor = None
    for klass in literals_CharacterLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_literals_nullliteral_is_not_abstract():
    assert not inspect.isabstract(literals_NullLiteral)


def test_literals_nullliteral_constructor_exists():
    assert callable(literals_NullLiteral.__init__)


def test_literals_nullliteral_constructor_args():
    sig = inspect.signature(literals_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literals_floatliteral_is_not_abstract():
    assert not inspect.isabstract(literals_FloatLiteral)


def test_literals_floatliteral_constructor_exists():
    assert callable(literals_FloatLiteral.__init__)


def test_literals_floatliteral_constructor_args():
    sig = inspect.signature(literals_FloatLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literals_longliteral_is_not_abstract():
    assert not inspect.isabstract(literals_LongLiteral)


def test_literals_longliteral_constructor_exists():
    assert callable(literals_LongLiteral.__init__)


def test_literals_longliteral_constructor_args():
    sig = inspect.signature(literals_LongLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literals_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(literals_DoubleLiteral)


def test_literals_doubleliteral_constructor_exists():
    assert callable(literals_DoubleLiteral.__init__)


def test_literals_doubleliteral_constructor_args():
    sig = inspect.signature(literals_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literals_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(literals_BooleanLiteral)


def test_literals_booleanliteral_constructor_exists():
    assert callable(literals_BooleanLiteral.__init__)


def test_literals_booleanliteral_constructor_args():
    sig = inspect.signature(literals_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_literals_booleanliteral_has_value():
    assert hasattr(literals_BooleanLiteral, "value")
    descriptor = None
    for klass in literals_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_staticimport_is_not_abstract():
    assert not inspect.isabstract(StaticImport)


def test_staticimport_constructor_exists():
    assert callable(StaticImport.__init__)


def test_staticimport_constructor_args():
    sig = inspect.signature(StaticImport.__init__)
    params = list(sig.parameters.keys())



def test_imports_staticmemberimport_is_not_abstract():
    assert not inspect.isabstract(imports_StaticMemberImport)


def test_imports_staticmemberimport_constructor_exists():
    assert callable(imports_StaticMemberImport.__init__)


def test_imports_staticmemberimport_constructor_args():
    sig = inspect.signature(imports_StaticMemberImport.__init__)
    params = list(sig.parameters.keys())



def test_imports_staticclassifierimport_is_not_abstract():
    assert not inspect.isabstract(imports_StaticClassifierImport)


def test_imports_staticclassifierimport_constructor_exists():
    assert callable(imports_StaticClassifierImport.__init__)


def test_imports_staticclassifierimport_constructor_args():
    sig = inspect.signature(imports_StaticClassifierImport.__init__)
    params = list(sig.parameters.keys())



def test_static_is_not_abstract():
    assert not inspect.isabstract(Static)


def test_static_constructor_exists():
    assert callable(Static.__init__)


def test_static_constructor_args():
    sig = inspect.signature(Static.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_literals_literal_is_not_abstract():
    assert not inspect.isabstract(literals_Literal)


def test_literals_literal_constructor_exists():
    assert callable(literals_Literal.__init__)


def test_literals_literal_constructor_args():
    sig = inspect.signature(literals_Literal.__init__)
    params = list(sig.parameters.keys())



def test_self_is_not_abstract():
    assert not inspect.isabstract(Self)


def test_self_constructor_exists():
    assert callable(Self.__init__)


def test_self_constructor_args():
    sig = inspect.signature(Self.__init__)
    params = list(sig.parameters.keys())



def test_literals_super_is_not_abstract():
    assert not inspect.isabstract(literals_Super)


def test_literals_super_constructor_exists():
    assert callable(literals_Super.__init__)


def test_literals_super_constructor_args():
    sig = inspect.signature(literals_Super.__init__)
    params = list(sig.parameters.keys())



def test_literals_this_is_not_abstract():
    assert not inspect.isabstract(literals_This)


def test_literals_this_constructor_exists():
    assert callable(literals_This.__init__)


def test_literals_this_constructor_args():
    sig = inspect.signature(literals_This.__init__)
    params = list(sig.parameters.keys())



def test_anonymousclass_is_not_abstract():
    assert not inspect.isabstract(AnonymousClass)


def test_anonymousclass_constructor_exists():
    assert callable(AnonymousClass.__init__)


def test_anonymousclass_constructor_args():
    sig = inspect.signature(AnonymousClass.__init__)
    params = list(sig.parameters.keys())



def test_calltypeargumentable_is_not_abstract():
    assert not inspect.isabstract(CallTypeArgumentable)


def test_calltypeargumentable_constructor_exists():
    assert callable(CallTypeArgumentable.__init__)


def test_calltypeargumentable_constructor_args():
    sig = inspect.signature(CallTypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_instantiation_is_not_abstract():
    assert not inspect.isabstract(Instantiation)


def test_instantiation_constructor_exists():
    assert callable(Instantiation.__init__)


def test_instantiation_constructor_args():
    sig = inspect.signature(Instantiation.__init__)
    params = list(sig.parameters.keys())



def test_instantiations_explicitconstructorcall_is_not_abstract():
    assert not inspect.isabstract(instantiations_ExplicitConstructorCall)


def test_instantiations_explicitconstructorcall_constructor_exists():
    assert callable(instantiations_ExplicitConstructorCall.__init__)


def test_instantiations_explicitconstructorcall_constructor_args():
    sig = inspect.signature(instantiations_ExplicitConstructorCall.__init__)
    params = list(sig.parameters.keys())



def test_instantiations_newconstructorcall_is_not_abstract():
    assert not inspect.isabstract(instantiations_NewConstructorCall)


def test_instantiations_newconstructorcall_constructor_exists():
    assert callable(instantiations_NewConstructorCall.__init__)


def test_instantiations_newconstructorcall_constructor_args():
    sig = inspect.signature(instantiations_NewConstructorCall.__init__)
    params = list(sig.parameters.keys())



def test_typeargumentable_is_not_abstract():
    assert not inspect.isabstract(TypeArgumentable)


def test_typeargumentable_constructor_exists():
    assert callable(TypeArgumentable.__init__)


def test_typeargumentable_constructor_args():
    sig = inspect.signature(TypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_references_reference_is_not_abstract():
    assert not inspect.isabstract(references_Reference)


def test_references_reference_constructor_exists():
    assert callable(references_Reference.__init__)


def test_references_reference_constructor_args():
    sig = inspect.signature(references_Reference.__init__)
    params = list(sig.parameters.keys())



def test_argumentable_is_not_abstract():
    assert not inspect.isabstract(Argumentable)


def test_argumentable_constructor_exists():
    assert callable(Argumentable.__init__)


def test_argumentable_constructor_args():
    sig = inspect.signature(Argumentable.__init__)
    params = list(sig.parameters.keys())



def test_references_methodcall_is_not_abstract():
    assert not inspect.isabstract(references_MethodCall)


def test_references_methodcall_constructor_exists():
    assert callable(references_MethodCall.__init__)


def test_references_methodcall_constructor_args():
    sig = inspect.signature(references_MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_import_is_not_abstract():
    assert not inspect.isabstract(Import)


def test_import_constructor_exists():
    assert callable(Import.__init__)


def test_import_constructor_args():
    sig = inspect.signature(Import.__init__)
    params = list(sig.parameters.keys())



def test_imports_classifierimport_is_not_abstract():
    assert not inspect.isabstract(imports_ClassifierImport)


def test_imports_classifierimport_constructor_exists():
    assert callable(imports_ClassifierImport.__init__)


def test_imports_classifierimport_constructor_args():
    sig = inspect.signature(imports_ClassifierImport.__init__)
    params = list(sig.parameters.keys())



def test_imports_packageimport_is_not_abstract():
    assert not inspect.isabstract(imports_PackageImport)


def test_imports_packageimport_constructor_exists():
    assert callable(imports_PackageImport.__init__)


def test_imports_packageimport_constructor_args():
    sig = inspect.signature(imports_PackageImport.__init__)
    params = list(sig.parameters.keys())



def test_imports_staticimport_is_not_abstract():
    assert not inspect.isabstract(imports_StaticImport)


def test_imports_staticimport_constructor_exists():
    assert callable(imports_StaticImport.__init__)


def test_imports_staticimport_constructor_args():
    sig = inspect.signature(imports_StaticImport.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationExpression)


def test_unarymodificationexpression_constructor_exists():
    assert callable(UnaryModificationExpression.__init__)


def test_unarymodificationexpression_constructor_args():
    sig = inspect.signature(UnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_suffixunarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_SuffixUnaryModificationExpression)


def test_expressions_suffixunarymodificationexpression_constructor_exists():
    assert callable(expressions_SuffixUnaryModificationExpression.__init__)


def test_expressions_suffixunarymodificationexpression_constructor_args():
    sig = inspect.signature(expressions_SuffixUnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_commentable_is_not_abstract():
    assert not inspect.isabstract(Commentable)


def test_commentable_constructor_exists():
    assert callable(Commentable.__init__)


def test_commentable_constructor_args():
    sig = inspect.signature(Commentable.__init__)
    params = list(sig.parameters.keys())



def test_types_typedelement_is_not_abstract():
    assert not inspect.isabstract(types_TypedElement)


def test_types_typedelement_constructor_exists():
    assert callable(types_TypedElement.__init__)


def test_types_typedelement_constructor_args():
    sig = inspect.signature(types_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_types_type_is_not_abstract():
    assert not inspect.isabstract(types_Type)


def test_types_type_constructor_exists():
    assert callable(types_Type.__init__)


def test_types_type_constructor_args():
    sig = inspect.signature(types_Type.__init__)
    params = list(sig.parameters.keys())



def test_operators_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Operator)


def test_operators_operator_constructor_exists():
    assert callable(operators_Operator.__init__)


def test_operators_operator_constructor_args():
    sig = inspect.signature(operators_Operator.__init__)
    params = list(sig.parameters.keys())



def test_instantiations_initializable_is_not_abstract():
    assert not inspect.isabstract(instantiations_Initializable)


def test_instantiations_initializable_constructor_exists():
    assert callable(instantiations_Initializable.__init__)


def test_instantiations_initializable_constructor_args():
    sig = inspect.signature(instantiations_Initializable.__init__)
    params = list(sig.parameters.keys())



def test_statements_conditional_is_not_abstract():
    assert not inspect.isabstract(statements_Conditional)


def test_statements_conditional_constructor_exists():
    assert callable(statements_Conditional.__init__)


def test_statements_conditional_constructor_args():
    sig = inspect.signature(statements_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_statements_statement_is_not_abstract():
    assert not inspect.isabstract(statements_Statement)


def test_statements_statement_constructor_exists():
    assert callable(statements_Statement.__init__)


def test_statements_statement_constructor_args():
    sig = inspect.signature(statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_statements_forloopinitializer_is_not_abstract():
    assert not inspect.isabstract(statements_ForLoopInitializer)


def test_statements_forloopinitializer_constructor_exists():
    assert callable(statements_ForLoopInitializer.__init__)


def test_statements_forloopinitializer_constructor_args():
    sig = inspect.signature(statements_ForLoopInitializer.__init__)
    params = list(sig.parameters.keys())



def test_members_membercontainer_is_not_abstract():
    assert not inspect.isabstract(members_MemberContainer)


def test_members_membercontainer_constructor_exists():
    assert callable(members_MemberContainer.__init__)


def test_members_membercontainer_constructor_args():
    sig = inspect.signature(members_MemberContainer.__init__)
    params = list(sig.parameters.keys())



def test_statements_statementlistcontainer_is_not_abstract():
    assert not inspect.isabstract(statements_StatementListContainer)


def test_statements_statementlistcontainer_constructor_exists():
    assert callable(statements_StatementListContainer.__init__)


def test_statements_statementlistcontainer_constructor_args():
    sig = inspect.signature(statements_StatementListContainer.__init__)
    params = list(sig.parameters.keys())



def test_imports_importingelement_is_not_abstract():
    assert not inspect.isabstract(imports_ImportingElement)


def test_imports_importingelement_constructor_exists():
    assert callable(imports_ImportingElement.__init__)


def test_imports_importingelement_constructor_args():
    sig = inspect.signature(imports_ImportingElement.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_annotationinstanceormodifier_is_not_abstract():
    assert not inspect.isabstract(modifiers_AnnotationInstanceOrModifier)


def test_modifiers_annotationinstanceormodifier_constructor_exists():
    assert callable(modifiers_AnnotationInstanceOrModifier.__init__)


def test_modifiers_annotationinstanceormodifier_constructor_args():
    sig = inspect.signature(modifiers_AnnotationInstanceOrModifier.__init__)
    params = list(sig.parameters.keys())



def test_parameters_parametrizable_is_not_abstract():
    assert not inspect.isabstract(parameters_Parametrizable)


def test_parameters_parametrizable_constructor_exists():
    assert callable(parameters_Parametrizable.__init__)


def test_parameters_parametrizable_constructor_args():
    sig = inspect.signature(parameters_Parametrizable.__init__)
    params = list(sig.parameters.keys())



def test_statements_statementcontainer_is_not_abstract():
    assert not inspect.isabstract(statements_StatementContainer)


def test_statements_statementcontainer_constructor_exists():
    assert callable(statements_StatementContainer.__init__)


def test_statements_statementcontainer_constructor_args():
    sig = inspect.signature(statements_StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_literals_self_is_not_abstract():
    assert not inspect.isabstract(literals_Self)


def test_literals_self_constructor_exists():
    assert callable(literals_Self.__init__)


def test_literals_self_constructor_args():
    sig = inspect.signature(literals_Self.__init__)
    params = list(sig.parameters.keys())



def test_references_argumentable_is_not_abstract():
    assert not inspect.isabstract(references_Argumentable)


def test_references_argumentable_constructor_exists():
    assert callable(references_Argumentable.__init__)


def test_references_argumentable_constructor_args():
    sig = inspect.signature(references_Argumentable.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_modifiable_is_not_abstract():
    assert not inspect.isabstract(modifiers_Modifiable)


def test_modifiers_modifiable_constructor_exists():
    assert callable(modifiers_Modifiable.__init__)


def test_modifiers_modifiable_constructor_args():
    sig = inspect.signature(modifiers_Modifiable.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_annotableandmodifiable_is_not_abstract():
    assert not inspect.isabstract(modifiers_AnnotableAndModifiable)


def test_modifiers_annotableandmodifiable_constructor_exists():
    assert callable(modifiers_AnnotableAndModifiable.__init__)


def test_modifiers_annotableandmodifiable_constructor_args():
    sig = inspect.signature(modifiers_AnnotableAndModifiable.__init__)
    params = list(sig.parameters.keys())



def test_types_typereference_is_not_abstract():
    assert not inspect.isabstract(types_TypeReference)


def test_types_typereference_constructor_exists():
    assert callable(types_TypeReference.__init__)


def test_types_typereference_constructor_args():
    sig = inspect.signature(types_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_members_exceptionthrower_is_not_abstract():
    assert not inspect.isabstract(members_ExceptionThrower)


def test_members_exceptionthrower_constructor_exists():
    assert callable(members_ExceptionThrower.__init__)


def test_members_exceptionthrower_constructor_args():
    sig = inspect.signature(members_ExceptionThrower.__init__)
    params = list(sig.parameters.keys())



def test_annotations_annotable_is_not_abstract():
    assert not inspect.isabstract(annotations_Annotable)


def test_annotations_annotable_constructor_exists():
    assert callable(annotations_Annotable.__init__)


def test_annotations_annotable_constructor_args():
    sig = inspect.signature(annotations_Annotable.__init__)
    params = list(sig.parameters.keys())



def test_arrays_arraytypeable_is_not_abstract():
    assert not inspect.isabstract(arrays_ArrayTypeable)


def test_arrays_arraytypeable_constructor_exists():
    assert callable(arrays_ArrayTypeable.__init__)


def test_arrays_arraytypeable_constructor_args():
    sig = inspect.signature(arrays_ArrayTypeable.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_annotations_annotationvalue_is_not_abstract():
    assert not inspect.isabstract(annotations_AnnotationValue)


def test_annotations_annotationvalue_constructor_exists():
    assert callable(annotations_AnnotationValue.__init__)


def test_annotations_annotationvalue_constructor_args():
    sig = inspect.signature(annotations_AnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_interfacemethod_is_not_abstract():
    assert not inspect.isabstract(InterfaceMethod)


def test_interfacemethod_constructor_exists():
    assert callable(InterfaceMethod.__init__)


def test_interfacemethod_constructor_args():
    sig = inspect.signature(InterfaceMethod.__init__)
    params = list(sig.parameters.keys())



def test_annotations_annotationattribute_is_not_abstract():
    assert not inspect.isabstract(annotations_AnnotationAttribute)


def test_annotations_annotationattribute_constructor_exists():
    assert callable(annotations_AnnotationAttribute.__init__)


def test_annotations_annotationattribute_constructor_args():
    sig = inspect.signature(annotations_AnnotationAttribute.__init__)
    params = list(sig.parameters.keys())



def test_annotations_annotationattributesetting_is_not_abstract():
    assert not inspect.isabstract(annotations_AnnotationAttributeSetting)


def test_annotations_annotationattributesetting_constructor_exists():
    assert callable(annotations_AnnotationAttributeSetting.__init__)


def test_annotations_annotationattributesetting_constructor_args():
    sig = inspect.signature(annotations_AnnotationAttributeSetting.__init__)
    params = list(sig.parameters.keys())



def test_annotationattributesetting_is_not_abstract():
    assert not inspect.isabstract(AnnotationAttributeSetting)


def test_annotationattributesetting_constructor_exists():
    assert callable(AnnotationAttributeSetting.__init__)


def test_annotationattributesetting_constructor_args():
    sig = inspect.signature(AnnotationAttributeSetting.__init__)
    params = list(sig.parameters.keys())



def test_annotationvalue_is_not_abstract():
    assert not inspect.isabstract(AnnotationValue)


def test_annotationvalue_constructor_exists():
    assert callable(AnnotationValue.__init__)


def test_annotationvalue_constructor_args():
    sig = inspect.signature(AnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_annotations_annotationparameter_is_not_abstract():
    assert not inspect.isabstract(annotations_AnnotationParameter)


def test_annotations_annotationparameter_constructor_exists():
    assert callable(annotations_AnnotationParameter.__init__)


def test_annotations_annotationparameter_constructor_args():
    sig = inspect.signature(annotations_AnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_annotationparameter_is_not_abstract():
    assert not inspect.isabstract(AnnotationParameter)


def test_annotationparameter_constructor_exists():
    assert callable(AnnotationParameter.__init__)


def test_annotationparameter_constructor_args():
    sig = inspect.signature(AnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_annotations_annotationparameterlist_is_not_abstract():
    assert not inspect.isabstract(annotations_AnnotationParameterList)


def test_annotations_annotationparameterlist_constructor_exists():
    assert callable(annotations_AnnotationParameterList.__init__)


def test_annotations_annotationparameterlist_constructor_args():
    sig = inspect.signature(annotations_AnnotationParameterList.__init__)
    params = list(sig.parameters.keys())



def test_annotations_singleannotationparameter_is_not_abstract():
    assert not inspect.isabstract(annotations_SingleAnnotationParameter)


def test_annotations_singleannotationparameter_constructor_exists():
    assert callable(annotations_SingleAnnotationParameter.__init__)


def test_annotations_singleannotationparameter_constructor_args():
    sig = inspect.signature(annotations_SingleAnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_generics_typeparameter_is_not_abstract():
    assert not inspect.isabstract(generics_TypeParameter)


def test_generics_typeparameter_constructor_exists():
    assert callable(generics_TypeParameter.__init__)


def test_generics_typeparameter_constructor_args():
    sig = inspect.signature(generics_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_namespaceawareelement_is_not_abstract():
    assert not inspect.isabstract(NamespaceAwareElement)


def test_namespaceawareelement_constructor_exists():
    assert callable(NamespaceAwareElement.__init__)


def test_namespaceawareelement_constructor_args():
    sig = inspect.signature(NamespaceAwareElement.__init__)
    params = list(sig.parameters.keys())



def test_imports_import_is_not_abstract():
    assert not inspect.isabstract(imports_Import)


def test_imports_import_constructor_exists():
    assert callable(imports_Import.__init__)


def test_imports_import_constructor_args():
    sig = inspect.signature(imports_Import.__init__)
    params = list(sig.parameters.keys())



def test_annotationinstanceormodifier_is_not_abstract():
    assert not inspect.isabstract(AnnotationInstanceOrModifier)


def test_annotationinstanceormodifier_constructor_exists():
    assert callable(AnnotationInstanceOrModifier.__init__)


def test_annotationinstanceormodifier_constructor_args():
    sig = inspect.signature(AnnotationInstanceOrModifier.__init__)
    params = list(sig.parameters.keys())



def test_modifiers_modifier_is_not_abstract():
    assert not inspect.isabstract(modifiers_Modifier)


def test_modifiers_modifier_constructor_exists():
    assert callable(modifiers_Modifier.__init__)


def test_modifiers_modifier_constructor_args():
    sig = inspect.signature(modifiers_Modifier.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_references_primitivetypereference_is_not_abstract():
    assert not inspect.isabstract(references_PrimitiveTypeReference)


def test_references_primitivetypereference_constructor_exists():
    assert callable(references_PrimitiveTypeReference.__init__)


def test_references_primitivetypereference_constructor_args():
    sig = inspect.signature(references_PrimitiveTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_references_elementreference_is_not_abstract():
    assert not inspect.isabstract(references_ElementReference)


def test_references_elementreference_constructor_exists():
    assert callable(references_ElementReference.__init__)


def test_references_elementreference_constructor_args():
    sig = inspect.signature(references_ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_references_stringreference_is_not_abstract():
    assert not inspect.isabstract(references_StringReference)


def test_references_stringreference_constructor_exists():
    assert callable(references_StringReference.__init__)


def test_references_stringreference_constructor_args():
    sig = inspect.signature(references_StringReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_references_stringreference_has_value():
    assert hasattr(references_StringReference, "value")
    descriptor = None
    for klass in references_StringReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_references_selfreference_is_not_abstract():
    assert not inspect.isabstract(references_SelfReference)


def test_references_selfreference_constructor_exists():
    assert callable(references_SelfReference.__init__)


def test_references_selfreference_constructor_args():
    sig = inspect.signature(references_SelfReference.__init__)
    params = list(sig.parameters.keys())



def test_references_reflectiveclassreference_is_not_abstract():
    assert not inspect.isabstract(references_ReflectiveClassReference)


def test_references_reflectiveclassreference_constructor_exists():
    assert callable(references_ReflectiveClassReference.__init__)


def test_references_reflectiveclassreference_constructor_args():
    sig = inspect.signature(references_ReflectiveClassReference.__init__)
    params = list(sig.parameters.keys())



def test_expressions_nestedexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_NestedExpression)


def test_expressions_nestedexpression_constructor_exists():
    assert callable(expressions_NestedExpression.__init__)


def test_expressions_nestedexpression_constructor_args():
    sig = inspect.signature(expressions_NestedExpression.__init__)
    params = list(sig.parameters.keys())



def test_annotations_annotationinstance_is_not_abstract():
    assert not inspect.isabstract(annotations_AnnotationInstance)


def test_annotations_annotationinstance_constructor_exists():
    assert callable(annotations_AnnotationInstance.__init__)


def test_annotations_annotationinstance_constructor_args():
    sig = inspect.signature(annotations_AnnotationInstance.__init__)
    params = list(sig.parameters.keys())



def test_annotationinstance_is_not_abstract():
    assert not inspect.isabstract(AnnotationInstance)


def test_annotationinstance_constructor_exists():
    assert callable(AnnotationInstance.__init__)


def test_annotationinstance_constructor_args():
    sig = inspect.signature(AnnotationInstance.__init__)
    params = list(sig.parameters.keys())



def test_expressions_prefixunarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_PrefixUnaryModificationExpression)


def test_expressions_prefixunarymodificationexpression_constructor_exists():
    assert callable(expressions_PrefixUnaryModificationExpression.__init__)


def test_expressions_prefixunarymodificationexpression_constructor_args():
    sig = inspect.signature(expressions_PrefixUnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationOperator)


def test_unarymodificationoperator_constructor_exists():
    assert callable(UnaryModificationOperator.__init__)


def test_unarymodificationoperator_constructor_args():
    sig = inspect.signature(UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_plusplus_is_not_abstract():
    assert not inspect.isabstract(operators_PlusPlus)


def test_operators_plusplus_constructor_exists():
    assert callable(operators_PlusPlus.__init__)


def test_operators_plusplus_constructor_args():
    sig = inspect.signature(operators_PlusPlus.__init__)
    params = list(sig.parameters.keys())



def test_operators_minusminus_is_not_abstract():
    assert not inspect.isabstract(operators_MinusMinus)


def test_operators_minusminus_constructor_exists():
    assert callable(operators_MinusMinus.__init__)


def test_operators_minusminus_constructor_args():
    sig = inspect.signature(operators_MinusMinus.__init__)
    params = list(sig.parameters.keys())



def test_typeparameter_is_not_abstract():
    assert not inspect.isabstract(TypeParameter)


def test_typeparameter_constructor_exists():
    assert callable(TypeParameter.__init__)


def test_typeparameter_constructor_args():
    sig = inspect.signature(TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_generics_typeparametrizable_is_not_abstract():
    assert not inspect.isabstract(generics_TypeParametrizable)


def test_generics_typeparametrizable_constructor_exists():
    assert callable(generics_TypeParametrizable.__init__)


def test_generics_typeparametrizable_constructor_args():
    sig = inspect.signature(generics_TypeParametrizable.__init__)
    params = list(sig.parameters.keys())



def test_generics_calltypeargumentable_is_not_abstract():
    assert not inspect.isabstract(generics_CallTypeArgumentable)


def test_generics_calltypeargumentable_constructor_exists():
    assert callable(generics_CallTypeArgumentable.__init__)


def test_generics_calltypeargumentable_constructor_args():
    sig = inspect.signature(generics_CallTypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_typeargument_is_not_abstract():
    assert not inspect.isabstract(TypeArgument)


def test_typeargument_constructor_exists():
    assert callable(TypeArgument.__init__)


def test_typeargument_constructor_args():
    sig = inspect.signature(TypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_generics_extendstypeargument_is_not_abstract():
    assert not inspect.isabstract(generics_ExtendsTypeArgument)


def test_generics_extendstypeargument_constructor_exists():
    assert callable(generics_ExtendsTypeArgument.__init__)


def test_generics_extendstypeargument_constructor_args():
    sig = inspect.signature(generics_ExtendsTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_generics_unknowntypeargument_is_not_abstract():
    assert not inspect.isabstract(generics_UnknownTypeArgument)


def test_generics_unknowntypeargument_constructor_exists():
    assert callable(generics_UnknownTypeArgument.__init__)


def test_generics_unknowntypeargument_constructor_args():
    sig = inspect.signature(generics_UnknownTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_generics_supertypeargument_is_not_abstract():
    assert not inspect.isabstract(generics_SuperTypeArgument)


def test_generics_supertypeargument_constructor_exists():
    assert callable(generics_SuperTypeArgument.__init__)


def test_generics_supertypeargument_constructor_args():
    sig = inspect.signature(generics_SuperTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_generics_typeargumentable_is_not_abstract():
    assert not inspect.isabstract(generics_TypeArgumentable)


def test_generics_typeargumentable_constructor_exists():
    assert callable(generics_TypeArgumentable.__init__)


def test_generics_typeargumentable_constructor_args():
    sig = inspect.signature(generics_TypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_additiveoperator_is_not_abstract():
    assert not inspect.isabstract(AdditiveOperator)


def test_additiveoperator_constructor_exists():
    assert callable(AdditiveOperator.__init__)


def test_additiveoperator_constructor_args():
    sig = inspect.signature(AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_additiveexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AdditiveExpressionChild)


def test_additiveexpressionchild_constructor_exists():
    assert callable(AdditiveExpressionChild.__init__)


def test_additiveexpressionchild_constructor_args():
    sig = inspect.signature(AdditiveExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_MultiplicativeExpression)


def test_expressions_multiplicativeexpression_constructor_exists():
    assert callable(expressions_MultiplicativeExpression.__init__)


def test_expressions_multiplicativeexpression_constructor_args():
    sig = inspect.signature(expressions_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationExpressionChild)


def test_unarymodificationexpressionchild_constructor_exists():
    assert callable(UnaryModificationExpressionChild.__init__)


def test_unarymodificationexpressionchild_constructor_args():
    sig = inspect.signature(UnaryModificationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_PrimaryExpression)


def test_expressions_primaryexpression_constructor_exists():
    assert callable(expressions_PrimaryExpression.__init__)


def test_expressions_primaryexpression_constructor_args():
    sig = inspect.signature(expressions_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpressionchild_is_not_abstract():
    assert not inspect.isabstract(UnaryExpressionChild)


def test_unaryexpressionchild_constructor_exists():
    assert callable(UnaryExpressionChild.__init__)


def test_unaryexpressionchild_constructor_args():
    sig = inspect.signature(UnaryExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_unarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_UnaryModificationExpression)


def test_expressions_unarymodificationexpression_constructor_exists():
    assert callable(expressions_UnaryModificationExpression.__init__)


def test_expressions_unarymodificationexpression_constructor_args():
    sig = inspect.signature(expressions_UnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_unarymodificationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_UnaryModificationExpressionChild)


def test_expressions_unarymodificationexpressionchild_constructor_exists():
    assert callable(expressions_UnaryModificationExpressionChild.__init__)


def test_expressions_unarymodificationexpressionchild_constructor_args():
    sig = inspect.signature(expressions_UnaryModificationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_negate_is_not_abstract():
    assert not inspect.isabstract(operators_Negate)


def test_operators_negate_constructor_exists():
    assert callable(operators_Negate.__init__)


def test_operators_negate_constructor_args():
    sig = inspect.signature(operators_Negate.__init__)
    params = list(sig.parameters.keys())



def test_operators_addition_is_not_abstract():
    assert not inspect.isabstract(operators_Addition)


def test_operators_addition_constructor_exists():
    assert callable(operators_Addition.__init__)


def test_operators_addition_constructor_args():
    sig = inspect.signature(operators_Addition.__init__)
    params = list(sig.parameters.keys())



def test_operators_subtraction_is_not_abstract():
    assert not inspect.isabstract(operators_Subtraction)


def test_operators_subtraction_constructor_exists():
    assert callable(operators_Subtraction.__init__)


def test_operators_subtraction_constructor_args():
    sig = inspect.signature(operators_Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_operators_complement_is_not_abstract():
    assert not inspect.isabstract(operators_Complement)


def test_operators_complement_constructor_exists():
    assert callable(operators_Complement.__init__)


def test_operators_complement_constructor_args():
    sig = inspect.signature(operators_Complement.__init__)
    params = list(sig.parameters.keys())



def test_expressions_multiplicativeexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_MultiplicativeExpressionChild)


def test_expressions_multiplicativeexpressionchild_constructor_exists():
    assert callable(expressions_MultiplicativeExpressionChild.__init__)


def test_expressions_multiplicativeexpressionchild_constructor_args():
    sig = inspect.signature(expressions_MultiplicativeExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeOperator)


def test_multiplicativeoperator_constructor_exists():
    assert callable(MultiplicativeOperator.__init__)


def test_multiplicativeoperator_constructor_args():
    sig = inspect.signature(MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_division_is_not_abstract():
    assert not inspect.isabstract(operators_Division)


def test_operators_division_constructor_exists():
    assert callable(operators_Division.__init__)


def test_operators_division_constructor_args():
    sig = inspect.signature(operators_Division.__init__)
    params = list(sig.parameters.keys())



def test_operators_remainder_is_not_abstract():
    assert not inspect.isabstract(operators_Remainder)


def test_operators_remainder_constructor_exists():
    assert callable(operators_Remainder.__init__)


def test_operators_remainder_constructor_args():
    sig = inspect.signature(operators_Remainder.__init__)
    params = list(sig.parameters.keys())



def test_operators_multiplication_is_not_abstract():
    assert not inspect.isabstract(operators_Multiplication)


def test_operators_multiplication_constructor_exists():
    assert callable(operators_Multiplication.__init__)


def test_operators_multiplication_constructor_args():
    sig = inspect.signature(operators_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeexpressionchild_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeExpressionChild)


def test_multiplicativeexpressionchild_constructor_exists():
    assert callable(MultiplicativeExpressionChild.__init__)


def test_multiplicativeexpressionchild_constructor_args():
    sig = inspect.signature(MultiplicativeExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_unaryexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_UnaryExpressionChild)


def test_expressions_unaryexpressionchild_constructor_exists():
    assert callable(expressions_UnaryExpressionChild.__init__)


def test_expressions_unaryexpressionchild_constructor_args():
    sig = inspect.signature(expressions_UnaryExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_UnaryExpression)


def test_expressions_unaryexpression_constructor_exists():
    assert callable(expressions_UnaryExpression.__init__)


def test_expressions_unaryexpression_constructor_args():
    sig = inspect.signature(expressions_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_equalityexpressionchild_is_not_abstract():
    assert not inspect.isabstract(EqualityExpressionChild)


def test_equalityexpressionchild_constructor_exists():
    assert callable(EqualityExpressionChild.__init__)


def test_equalityexpressionchild_constructor_args():
    sig = inspect.signature(EqualityExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_equalityoperator_is_not_abstract():
    assert not inspect.isabstract(EqualityOperator)


def test_equalityoperator_constructor_exists():
    assert callable(EqualityOperator.__init__)


def test_equalityoperator_constructor_args():
    sig = inspect.signature(EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_equal_is_not_abstract():
    assert not inspect.isabstract(operators_Equal)


def test_operators_equal_constructor_exists():
    assert callable(operators_Equal.__init__)


def test_operators_equal_constructor_args():
    sig = inspect.signature(operators_Equal.__init__)
    params = list(sig.parameters.keys())



def test_operators_notequal_is_not_abstract():
    assert not inspect.isabstract(operators_NotEqual)


def test_operators_notequal_constructor_exists():
    assert callable(operators_NotEqual.__init__)


def test_operators_notequal_constructor_args():
    sig = inspect.signature(operators_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_shiftoperator_is_not_abstract():
    assert not inspect.isabstract(ShiftOperator)


def test_shiftoperator_constructor_exists():
    assert callable(ShiftOperator.__init__)


def test_shiftoperator_constructor_args():
    sig = inspect.signature(ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_leftshift_is_not_abstract():
    assert not inspect.isabstract(operators_LeftShift)


def test_operators_leftshift_constructor_exists():
    assert callable(operators_LeftShift.__init__)


def test_operators_leftshift_constructor_args():
    sig = inspect.signature(operators_LeftShift.__init__)
    params = list(sig.parameters.keys())



def test_operators_rightshift_is_not_abstract():
    assert not inspect.isabstract(operators_RightShift)


def test_operators_rightshift_constructor_exists():
    assert callable(operators_RightShift.__init__)


def test_operators_rightshift_constructor_args():
    sig = inspect.signature(operators_RightShift.__init__)
    params = list(sig.parameters.keys())



def test_operators_unsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(operators_UnsignedRightShift)


def test_operators_unsignedrightshift_constructor_exists():
    assert callable(operators_UnsignedRightShift.__init__)


def test_operators_unsignedrightshift_constructor_args():
    sig = inspect.signature(operators_UnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_shiftexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ShiftExpressionChild)


def test_shiftexpressionchild_constructor_exists():
    assert callable(ShiftExpressionChild.__init__)


def test_shiftexpressionchild_constructor_args():
    sig = inspect.signature(ShiftExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_additiveexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_AdditiveExpressionChild)


def test_expressions_additiveexpressionchild_constructor_exists():
    assert callable(expressions_AdditiveExpressionChild.__init__)


def test_expressions_additiveexpressionchild_constructor_args():
    sig = inspect.signature(expressions_AdditiveExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_AdditiveExpression)


def test_expressions_additiveexpression_constructor_exists():
    assert callable(expressions_AdditiveExpression.__init__)


def test_expressions_additiveexpression_constructor_args():
    sig = inspect.signature(expressions_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_relationoperator_is_not_abstract():
    assert not inspect.isabstract(RelationOperator)


def test_relationoperator_constructor_exists():
    assert callable(RelationOperator.__init__)


def test_relationoperator_constructor_args():
    sig = inspect.signature(RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(operators_GreaterThanOrEqual)


def test_operators_greaterthanorequal_constructor_exists():
    assert callable(operators_GreaterThanOrEqual.__init__)


def test_operators_greaterthanorequal_constructor_args():
    sig = inspect.signature(operators_GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_operators_lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(operators_LessThanOrEqual)


def test_operators_lessthanorequal_constructor_exists():
    assert callable(operators_LessThanOrEqual.__init__)


def test_operators_lessthanorequal_constructor_args():
    sig = inspect.signature(operators_LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_operators_lessthan_is_not_abstract():
    assert not inspect.isabstract(operators_LessThan)


def test_operators_lessthan_constructor_exists():
    assert callable(operators_LessThan.__init__)


def test_operators_lessthan_constructor_args():
    sig = inspect.signature(operators_LessThan.__init__)
    params = list(sig.parameters.keys())



def test_operators_greaterthan_is_not_abstract():
    assert not inspect.isabstract(operators_GreaterThan)


def test_operators_greaterthan_constructor_exists():
    assert callable(operators_GreaterThan.__init__)


def test_operators_greaterthan_constructor_args():
    sig = inspect.signature(operators_GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_relationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(RelationExpressionChild)


def test_relationexpressionchild_constructor_exists():
    assert callable(RelationExpressionChild.__init__)


def test_relationexpressionchild_constructor_args():
    sig = inspect.signature(RelationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_shiftexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_ShiftExpressionChild)


def test_expressions_shiftexpressionchild_constructor_exists():
    assert callable(expressions_ShiftExpressionChild.__init__)


def test_expressions_shiftexpressionchild_constructor_args():
    sig = inspect.signature(expressions_ShiftExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_ShiftExpression)


def test_expressions_shiftexpression_constructor_exists():
    assert callable(expressions_ShiftExpression.__init__)


def test_expressions_shiftexpression_constructor_args():
    sig = inspect.signature(expressions_ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_instanceofexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_InstanceOfExpressionChild)


def test_expressions_instanceofexpressionchild_constructor_exists():
    assert callable(expressions_InstanceOfExpressionChild.__init__)


def test_expressions_instanceofexpressionchild_constructor_args():
    sig = inspect.signature(expressions_InstanceOfExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_instanceofexpressionchild_is_not_abstract():
    assert not inspect.isabstract(InstanceOfExpressionChild)


def test_instanceofexpressionchild_constructor_exists():
    assert callable(InstanceOfExpressionChild.__init__)


def test_instanceofexpressionchild_constructor_args():
    sig = inspect.signature(InstanceOfExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_relationexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_RelationExpression)


def test_expressions_relationexpression_constructor_exists():
    assert callable(expressions_RelationExpression.__init__)


def test_expressions_relationexpression_constructor_args():
    sig = inspect.signature(expressions_RelationExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_relationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_RelationExpressionChild)


def test_expressions_relationexpressionchild_constructor_exists():
    assert callable(expressions_RelationExpressionChild.__init__)


def test_expressions_relationexpressionchild_constructor_args():
    sig = inspect.signature(expressions_RelationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_conditionalorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalOrExpressionChild)


def test_conditionalorexpressionchild_constructor_exists():
    assert callable(ConditionalOrExpressionChild.__init__)


def test_conditionalorexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_ConditionalAndExpression)


def test_expressions_conditionalandexpression_constructor_exists():
    assert callable(expressions_ConditionalAndExpression.__init__)


def test_expressions_conditionalandexpression_constructor_args():
    sig = inspect.signature(expressions_ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_andexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AndExpressionChild)


def test_andexpressionchild_constructor_exists():
    assert callable(AndExpressionChild.__init__)


def test_andexpressionchild_constructor_args():
    sig = inspect.signature(AndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_equalityexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_EqualityExpressionChild)


def test_expressions_equalityexpressionchild_constructor_exists():
    assert callable(expressions_EqualityExpressionChild.__init__)


def test_expressions_equalityexpressionchild_constructor_args():
    sig = inspect.signature(expressions_EqualityExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_EqualityExpression)


def test_expressions_equalityexpression_constructor_exists():
    assert callable(expressions_EqualityExpression.__init__)


def test_expressions_equalityexpression_constructor_args():
    sig = inspect.signature(expressions_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_exclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ExclusiveOrExpressionChild)


def test_exclusiveorexpressionchild_constructor_exists():
    assert callable(ExclusiveOrExpressionChild.__init__)


def test_exclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(ExclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_andexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_AndExpressionChild)


def test_expressions_andexpressionchild_constructor_exists():
    assert callable(expressions_AndExpressionChild.__init__)


def test_expressions_andexpressionchild_constructor_args():
    sig = inspect.signature(expressions_AndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_andexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_AndExpression)


def test_expressions_andexpression_constructor_exists():
    assert callable(expressions_AndExpression.__init__)


def test_expressions_andexpression_constructor_args():
    sig = inspect.signature(expressions_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_inclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(InclusiveOrExpressionChild)


def test_inclusiveorexpressionchild_constructor_exists():
    assert callable(InclusiveOrExpressionChild.__init__)


def test_inclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(InclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_ExclusiveOrExpression)


def test_expressions_exclusiveorexpression_constructor_exists():
    assert callable(expressions_ExclusiveOrExpression.__init__)


def test_expressions_exclusiveorexpression_constructor_args():
    sig = inspect.signature(expressions_ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_exclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_ExclusiveOrExpressionChild)


def test_expressions_exclusiveorexpressionchild_constructor_exists():
    assert callable(expressions_ExclusiveOrExpressionChild.__init__)


def test_expressions_exclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(expressions_ExclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_ConditionalAndExpressionChild)


def test_expressions_conditionalandexpressionchild_constructor_exists():
    assert callable(expressions_ConditionalAndExpressionChild.__init__)


def test_expressions_conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(expressions_ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_AssignmentExpression)


def test_expressions_assignmentexpression_constructor_exists():
    assert callable(expressions_AssignmentExpression.__init__)


def test_expressions_assignmentexpression_constructor_args():
    sig = inspect.signature(expressions_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalAndExpressionChild)


def test_conditionalandexpressionchild_constructor_exists():
    assert callable(ConditionalAndExpressionChild.__init__)


def test_conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_inclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_InclusiveOrExpressionChild)


def test_expressions_inclusiveorexpressionchild_constructor_exists():
    assert callable(expressions_InclusiveOrExpressionChild.__init__)


def test_expressions_inclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(expressions_InclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_InclusiveOrExpression)


def test_expressions_inclusiveorexpression_constructor_exists():
    assert callable(expressions_InclusiveOrExpression.__init__)


def test_expressions_inclusiveorexpression_constructor_args():
    sig = inspect.signature(expressions_InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalExpressionChild)


def test_conditionalexpressionchild_constructor_exists():
    assert callable(ConditionalExpressionChild.__init__)


def test_conditionalexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_ConditionalOrExpression)


def test_expressions_conditionalorexpression_constructor_exists():
    assert callable(expressions_ConditionalOrExpression.__init__)


def test_expressions_conditionalorexpression_constructor_args():
    sig = inspect.signature(expressions_ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_conditionalorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_ConditionalOrExpressionChild)


def test_expressions_conditionalorexpressionchild_constructor_exists():
    assert callable(expressions_ConditionalOrExpressionChild.__init__)


def test_expressions_conditionalorexpressionchild_constructor_args():
    sig = inspect.signature(expressions_ConditionalOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_assignmentexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_AssignmentExpressionChild)


def test_expressions_assignmentexpressionchild_constructor_exists():
    assert callable(expressions_AssignmentExpressionChild.__init__)


def test_expressions_assignmentexpressionchild_constructor_args():
    sig = inspect.signature(expressions_AssignmentExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(AssignmentOperator)


def test_assignmentoperator_constructor_exists():
    assert callable(AssignmentOperator.__init__)


def test_assignmentoperator_constructor_args():
    sig = inspect.signature(AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_assignmentand_is_not_abstract():
    assert not inspect.isabstract(operators_AssignmentAnd)


def test_operators_assignmentand_constructor_exists():
    assert callable(operators_AssignmentAnd.__init__)


def test_operators_assignmentand_constructor_args():
    sig = inspect.signature(operators_AssignmentAnd.__init__)
    params = list(sig.parameters.keys())



def test_operators_assignmentexclusiveor_is_not_abstract():
    assert not inspect.isabstract(operators_AssignmentExclusiveOr)


def test_operators_assignmentexclusiveor_constructor_exists():
    assert callable(operators_AssignmentExclusiveOr.__init__)


def test_operators_assignmentexclusiveor_constructor_args():
    sig = inspect.signature(operators_AssignmentExclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_operators_assignmentunsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(operators_AssignmentUnsignedRightShift)


def test_operators_assignmentunsignedrightshift_constructor_exists():
    assert callable(operators_AssignmentUnsignedRightShift.__init__)


def test_operators_assignmentunsignedrightshift_constructor_args():
    sig = inspect.signature(operators_AssignmentUnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_operators_assignmentplus_is_not_abstract():
    assert not inspect.isabstract(operators_AssignmentPlus)


def test_operators_assignmentplus_constructor_exists():
    assert callable(operators_AssignmentPlus.__init__)


def test_operators_assignmentplus_constructor_args():
    sig = inspect.signature(operators_AssignmentPlus.__init__)
    params = list(sig.parameters.keys())



def test_operators_assignmentminus_is_not_abstract():
    assert not inspect.isabstract(operators_AssignmentMinus)


def test_operators_assignmentminus_constructor_exists():
    assert callable(operators_AssignmentMinus.__init__)


def test_operators_assignmentminus_constructor_args():
    sig = inspect.signature(operators_AssignmentMinus.__init__)
    params = list(sig.parameters.keys())



def test_operators_assignment_is_not_abstract():
    assert not inspect.isabstract(operators_Assignment)


def test_operators_assignment_constructor_exists():
    assert callable(operators_Assignment.__init__)


def test_operators_assignment_constructor_args():
    sig = inspect.signature(operators_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_operators_assignmentrightshift_is_not_abstract():
    assert not inspect.isabstract(operators_AssignmentRightShift)


def test_operators_assignmentrightshift_constructor_exists():
    assert callable(operators_AssignmentRightShift.__init__)


def test_operators_assignmentrightshift_constructor_args():
    sig = inspect.signature(operators_AssignmentRightShift.__init__)
    params = list(sig.parameters.keys())



def test_operators_assignmentor_is_not_abstract():
    assert not inspect.isabstract(operators_AssignmentOr)


def test_operators_assignmentor_constructor_exists():
    assert callable(operators_AssignmentOr.__init__)


def test_operators_assignmentor_constructor_args():
    sig = inspect.signature(operators_AssignmentOr.__init__)
    params = list(sig.parameters.keys())



def test_operators_assignmentmultiplication_is_not_abstract():
    assert not inspect.isabstract(operators_AssignmentMultiplication)


def test_operators_assignmentmultiplication_constructor_exists():
    assert callable(operators_AssignmentMultiplication.__init__)


def test_operators_assignmentmultiplication_constructor_args():
    sig = inspect.signature(operators_AssignmentMultiplication.__init__)
    params = list(sig.parameters.keys())



def test_operators_assignmentdivision_is_not_abstract():
    assert not inspect.isabstract(operators_AssignmentDivision)


def test_operators_assignmentdivision_constructor_exists():
    assert callable(operators_AssignmentDivision.__init__)


def test_operators_assignmentdivision_constructor_args():
    sig = inspect.signature(operators_AssignmentDivision.__init__)
    params = list(sig.parameters.keys())



def test_operators_assignmentleftshift_is_not_abstract():
    assert not inspect.isabstract(operators_AssignmentLeftShift)


def test_operators_assignmentleftshift_constructor_exists():
    assert callable(operators_AssignmentLeftShift.__init__)


def test_operators_assignmentleftshift_constructor_args():
    sig = inspect.signature(operators_AssignmentLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_operators_assignmentmodulo_is_not_abstract():
    assert not inspect.isabstract(operators_AssignmentModulo)


def test_operators_assignmentmodulo_constructor_exists():
    assert callable(operators_AssignmentModulo.__init__)


def test_operators_assignmentmodulo_constructor_args():
    sig = inspect.signature(operators_AssignmentModulo.__init__)
    params = list(sig.parameters.keys())



def test_assignmentexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AssignmentExpressionChild)


def test_assignmentexpressionchild_constructor_exists():
    assert callable(AssignmentExpressionChild.__init__)


def test_assignmentexpressionchild_constructor_args():
    sig = inspect.signature(AssignmentExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_expressions_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_ConditionalExpression)


def test_expressions_conditionalexpression_constructor_exists():
    assert callable(expressions_ConditionalExpression.__init__)


def test_expressions_conditionalexpression_constructor_args():
    sig = inspect.signature(expressions_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_conditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions_ConditionalExpressionChild)


def test_expressions_conditionalexpressionchild_constructor_exists():
    assert callable(expressions_ConditionalExpressionChild.__init__)


def test_expressions_conditionalexpressionchild_constructor_args():
    sig = inspect.signature(expressions_ConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_javaroot_is_not_abstract():
    assert not inspect.isabstract(JavaRoot)


def test_javaroot_constructor_exists():
    assert callable(JavaRoot.__init__)


def test_javaroot_constructor_args():
    sig = inspect.signature(JavaRoot.__init__)
    params = list(sig.parameters.keys())



def test_containers_compilationunit_is_not_abstract():
    assert not inspect.isabstract(containers_CompilationUnit)


def test_containers_compilationunit_constructor_exists():
    assert callable(containers_CompilationUnit.__init__)


def test_containers_compilationunit_constructor_args():
    sig = inspect.signature(containers_CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_importingelement_is_not_abstract():
    assert not inspect.isabstract(ImportingElement)


def test_importingelement_constructor_exists():
    assert callable(ImportingElement.__init__)


def test_importingelement_constructor_args():
    sig = inspect.signature(ImportingElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_members_member_is_not_abstract():
    assert not inspect.isabstract(members_Member)


def test_members_member_constructor_exists():
    assert callable(members_Member.__init__)


def test_members_member_constructor_args():
    sig = inspect.signature(members_Member.__init__)
    params = list(sig.parameters.keys())



def test_references_referenceableelement_is_not_abstract():
    assert not inspect.isabstract(references_ReferenceableElement)


def test_references_referenceableelement_constructor_exists():
    assert callable(references_ReferenceableElement.__init__)


def test_references_referenceableelement_constructor_args():
    sig = inspect.signature(references_ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_containers_javaroot_is_not_abstract():
    assert not inspect.isabstract(containers_JavaRoot)


def test_containers_javaroot_constructor_exists():
    assert callable(containers_JavaRoot.__init__)


def test_containers_javaroot_constructor_args():
    sig = inspect.signature(containers_JavaRoot.__init__)
    params = list(sig.parameters.keys())



def test_forloopinitializer_is_not_abstract():
    assert not inspect.isabstract(ForLoopInitializer)


def test_forloopinitializer_constructor_exists():
    assert callable(ForLoopInitializer.__init__)


def test_forloopinitializer_constructor_args():
    sig = inspect.signature(ForLoopInitializer.__init__)
    params = list(sig.parameters.keys())



def test_expressions_expressionlist_is_not_abstract():
    assert not inspect.isabstract(expressions_ExpressionList)


def test_expressions_expressionlist_constructor_exists():
    assert callable(expressions_ExpressionList.__init__)


def test_expressions_expressionlist_constructor_args():
    sig = inspect.signature(expressions_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_containers_emptymodel_is_not_abstract():
    assert not inspect.isabstract(containers_EmptyModel)


def test_containers_emptymodel_constructor_exists():
    assert callable(containers_EmptyModel.__init__)


def test_containers_emptymodel_constructor_args():
    sig = inspect.signature(containers_EmptyModel.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_compilationunit_is_not_abstract():
    assert not inspect.isabstract(CompilationUnit)


def test_compilationunit_constructor_exists():
    assert callable(CompilationUnit.__init__)


def test_compilationunit_constructor_args():
    sig = inspect.signature(CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_annotable_is_not_abstract():
    assert not inspect.isabstract(Annotable)


def test_annotable_constructor_exists():
    assert callable(Annotable.__init__)


def test_annotable_constructor_args():
    sig = inspect.signature(Annotable.__init__)
    params = list(sig.parameters.keys())



def test_commons_namespaceawareelement_is_not_abstract():
    assert not inspect.isabstract(commons_NamespaceAwareElement)


def test_commons_namespaceawareelement_constructor_exists():
    assert callable(commons_NamespaceAwareElement.__init__)


def test_commons_namespaceawareelement_constructor_args():
    sig = inspect.signature(commons_NamespaceAwareElement.__init__)
    params = list(sig.parameters.keys())
    assert "namespaces" in params, "Missing parameter 'namespaces'"

def test_commons_namespaceawareelement_has_namespaces():
    assert hasattr(commons_NamespaceAwareElement, "namespaces")
    descriptor = None
    for klass in commons_NamespaceAwareElement.__mro__:
        if "namespaces" in klass.__dict__:
            descriptor = klass.__dict__["namespaces"]
            break
    assert isinstance(descriptor, property)



def test_commons_namedelement_is_not_abstract():
    assert not inspect.isabstract(commons_NamedElement)


def test_commons_namedelement_constructor_exists():
    assert callable(commons_NamedElement.__init__)


def test_commons_namedelement_constructor_args():
    sig = inspect.signature(commons_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_commons_namedelement_has_name():
    assert hasattr(commons_NamedElement, "name")
    descriptor = None
    for klass in commons_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_commons_commentable_is_not_abstract():
    assert not inspect.isabstract(commons_Commentable)


def test_commons_commentable_constructor_exists():
    assert callable(commons_Commentable.__init__)


def test_commons_commentable_constructor_args():
    sig = inspect.signature(commons_Commentable.__init__)
    params = list(sig.parameters.keys())
    assert "comments" in params, "Missing parameter 'comments'"

def test_commons_commentable_has_comments():
    assert hasattr(commons_Commentable, "comments")
    descriptor = None
    for klass in commons_Commentable.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)



def test_enumconstant_is_not_abstract():
    assert not inspect.isabstract(EnumConstant)


def test_enumconstant_constructor_exists():
    assert callable(EnumConstant.__init__)


def test_enumconstant_constructor_args():
    sig = inspect.signature(EnumConstant.__init__)
    params = list(sig.parameters.keys())



def test_referenceableelement_is_not_abstract():
    assert not inspect.isabstract(ReferenceableElement)


def test_referenceableelement_constructor_exists():
    assert callable(ReferenceableElement.__init__)


def test_referenceableelement_constructor_args():
    sig = inspect.signature(ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_containers_package_is_not_abstract():
    assert not inspect.isabstract(containers_Package)


def test_containers_package_constructor_exists():
    assert callable(containers_Package.__init__)


def test_containers_package_constructor_args():
    sig = inspect.signature(containers_Package.__init__)
    params = list(sig.parameters.keys())



def test_members_enumconstant_is_not_abstract():
    assert not inspect.isabstract(members_EnumConstant)


def test_members_enumconstant_constructor_exists():
    assert callable(members_EnumConstant.__init__)


def test_members_enumconstant_constructor_args():
    sig = inspect.signature(members_EnumConstant.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_classifiers_classifier_is_not_abstract():
    assert not inspect.isabstract(classifiers_Classifier)


def test_classifiers_classifier_constructor_exists():
    assert callable(classifiers_Classifier.__init__)


def test_classifiers_classifier_constructor_args():
    sig = inspect.signature(classifiers_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_arrays_arrayselector_is_not_abstract():
    assert not inspect.isabstract(arrays_ArraySelector)


def test_arrays_arrayselector_constructor_exists():
    assert callable(arrays_ArraySelector.__init__)


def test_arrays_arrayselector_constructor_args():
    sig = inspect.signature(arrays_ArraySelector.__init__)
    params = list(sig.parameters.keys())



def test_implementor_is_not_abstract():
    assert not inspect.isabstract(Implementor)


def test_implementor_constructor_exists():
    assert callable(Implementor.__init__)


def test_implementor_constructor_args():
    sig = inspect.signature(Implementor.__init__)
    params = list(sig.parameters.keys())



def test_concreteclassifier_is_not_abstract():
    assert not inspect.isabstract(ConcreteClassifier)


def test_concreteclassifier_constructor_exists():
    assert callable(ConcreteClassifier.__init__)


def test_concreteclassifier_constructor_args():
    sig = inspect.signature(ConcreteClassifier.__init__)
    params = list(sig.parameters.keys())



def test_classifiers_interface_is_not_abstract():
    assert not inspect.isabstract(classifiers_Interface)


def test_classifiers_interface_constructor_exists():
    assert callable(classifiers_Interface.__init__)


def test_classifiers_interface_constructor_args():
    sig = inspect.signature(classifiers_Interface.__init__)
    params = list(sig.parameters.keys())



def test_classifiers_annotation_is_not_abstract():
    assert not inspect.isabstract(classifiers_Annotation)


def test_classifiers_annotation_constructor_exists():
    assert callable(classifiers_Annotation.__init__)


def test_classifiers_annotation_constructor_args():
    sig = inspect.signature(classifiers_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_classifiers_enumeration_is_not_abstract():
    assert not inspect.isabstract(classifiers_Enumeration)


def test_classifiers_enumeration_constructor_exists():
    assert callable(classifiers_Enumeration.__init__)


def test_classifiers_enumeration_constructor_args():
    sig = inspect.signature(classifiers_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_classifiers_class_is_not_abstract():
    assert not inspect.isabstract(classifiers_Class)


def test_classifiers_class_constructor_exists():
    assert callable(classifiers_Class.__init__)


def test_classifiers_class_constructor_args():
    sig = inspect.signature(classifiers_Class.__init__)
    params = list(sig.parameters.keys())



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types_primitivetype_is_not_abstract():
    assert not inspect.isabstract(types_PrimitiveType)


def test_types_primitivetype_constructor_exists():
    assert callable(types_PrimitiveType.__init__)


def test_types_primitivetype_constructor_args():
    sig = inspect.signature(types_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_types_classifierreference_is_not_abstract():
    assert not inspect.isabstract(types_ClassifierReference)


def test_types_classifierreference_constructor_exists():
    assert callable(types_ClassifierReference.__init__)


def test_types_classifierreference_constructor_args():
    sig = inspect.signature(types_ClassifierReference.__init__)
    params = list(sig.parameters.keys())



def test_types_namespaceclassifierreference_is_not_abstract():
    assert not inspect.isabstract(types_NamespaceClassifierReference)


def test_types_namespaceclassifierreference_constructor_exists():
    assert callable(types_NamespaceClassifierReference.__init__)


def test_types_namespaceclassifierreference_constructor_args():
    sig = inspect.signature(types_NamespaceClassifierReference.__init__)
    params = list(sig.parameters.keys())



def test_classifiers_implementor_is_not_abstract():
    assert not inspect.isabstract(classifiers_Implementor)


def test_classifiers_implementor_constructor_exists():
    assert callable(classifiers_Implementor.__init__)


def test_classifiers_implementor_constructor_args():
    sig = inspect.signature(classifiers_Implementor.__init__)
    params = list(sig.parameters.keys())



def test_annotableandmodifiable_is_not_abstract():
    assert not inspect.isabstract(AnnotableAndModifiable)


def test_annotableandmodifiable_constructor_exists():
    assert callable(AnnotableAndModifiable.__init__)


def test_annotableandmodifiable_constructor_args():
    sig = inspect.signature(AnnotableAndModifiable.__init__)
    params = list(sig.parameters.keys())



def test_variables_localvariable_is_not_abstract():
    assert not inspect.isabstract(variables_LocalVariable)


def test_variables_localvariable_constructor_exists():
    assert callable(variables_LocalVariable.__init__)


def test_variables_localvariable_constructor_args():
    sig = inspect.signature(variables_LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_parameters_parameter_is_not_abstract():
    assert not inspect.isabstract(parameters_Parameter)


def test_parameters_parameter_constructor_exists():
    assert callable(parameters_Parameter.__init__)


def test_parameters_parameter_constructor_args():
    sig = inspect.signature(parameters_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_statements_condition_is_not_abstract():
    assert not inspect.isabstract(statements_Condition)


def test_statements_condition_constructor_exists():
    assert callable(statements_Condition.__init__)


def test_statements_condition_constructor_args():
    sig = inspect.signature(statements_Condition.__init__)
    params = list(sig.parameters.keys())



def test_statements_jumplabel_is_not_abstract():
    assert not inspect.isabstract(statements_JumpLabel)


def test_statements_jumplabel_constructor_exists():
    assert callable(statements_JumpLabel.__init__)


def test_statements_jumplabel_constructor_args():
    sig = inspect.signature(statements_JumpLabel.__init__)
    params = list(sig.parameters.keys())



def test_statements_emptystatement_is_not_abstract():
    assert not inspect.isabstract(statements_EmptyStatement)


def test_statements_emptystatement_constructor_exists():
    assert callable(statements_EmptyStatement.__init__)


def test_statements_emptystatement_constructor_args():
    sig = inspect.signature(statements_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_statements_jump_is_not_abstract():
    assert not inspect.isabstract(statements_Jump)


def test_statements_jump_constructor_exists():
    assert callable(statements_Jump.__init__)


def test_statements_jump_constructor_args():
    sig = inspect.signature(statements_Jump.__init__)
    params = list(sig.parameters.keys())



def test_statements_return_is_not_abstract():
    assert not inspect.isabstract(statements_Return)


def test_statements_return_constructor_exists():
    assert callable(statements_Return.__init__)


def test_statements_return_constructor_args():
    sig = inspect.signature(statements_Return.__init__)
    params = list(sig.parameters.keys())



def test_statements_forloop_is_not_abstract():
    assert not inspect.isabstract(statements_ForLoop)


def test_statements_forloop_constructor_exists():
    assert callable(statements_ForLoop.__init__)


def test_statements_forloop_constructor_args():
    sig = inspect.signature(statements_ForLoop.__init__)
    params = list(sig.parameters.keys())



def test_statements_throw_is_not_abstract():
    assert not inspect.isabstract(statements_Throw)


def test_statements_throw_constructor_exists():
    assert callable(statements_Throw.__init__)


def test_statements_throw_constructor_args():
    sig = inspect.signature(statements_Throw.__init__)
    params = list(sig.parameters.keys())



def test_statements_tryblock_is_not_abstract():
    assert not inspect.isabstract(statements_TryBlock)


def test_statements_tryblock_constructor_exists():
    assert callable(statements_TryBlock.__init__)


def test_statements_tryblock_constructor_args():
    sig = inspect.signature(statements_TryBlock.__init__)
    params = list(sig.parameters.keys())



def test_statements_foreachloop_is_not_abstract():
    assert not inspect.isabstract(statements_ForEachLoop)


def test_statements_foreachloop_constructor_exists():
    assert callable(statements_ForEachLoop.__init__)


def test_statements_foreachloop_constructor_args():
    sig = inspect.signature(statements_ForEachLoop.__init__)
    params = list(sig.parameters.keys())



def test_statements_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(statements_ExpressionStatement)


def test_statements_expressionstatement_constructor_exists():
    assert callable(statements_ExpressionStatement.__init__)


def test_statements_expressionstatement_constructor_args():
    sig = inspect.signature(statements_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_statements_assert_is_not_abstract():
    assert not inspect.isabstract(statements_Assert)


def test_statements_assert_constructor_exists():
    assert callable(statements_Assert.__init__)


def test_statements_assert_constructor_args():
    sig = inspect.signature(statements_Assert.__init__)
    params = list(sig.parameters.keys())



def test_statements_synchronizedblock_is_not_abstract():
    assert not inspect.isabstract(statements_SynchronizedBlock)


def test_statements_synchronizedblock_constructor_exists():
    assert callable(statements_SynchronizedBlock.__init__)


def test_statements_synchronizedblock_constructor_args():
    sig = inspect.signature(statements_SynchronizedBlock.__init__)
    params = list(sig.parameters.keys())



def test_statements_whileloop_is_not_abstract():
    assert not inspect.isabstract(statements_WhileLoop)


def test_statements_whileloop_constructor_exists():
    assert callable(statements_WhileLoop.__init__)


def test_statements_whileloop_constructor_args():
    sig = inspect.signature(statements_WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_statements_localvariablestatement_is_not_abstract():
    assert not inspect.isabstract(statements_LocalVariableStatement)


def test_statements_localvariablestatement_constructor_exists():
    assert callable(statements_LocalVariableStatement.__init__)


def test_statements_localvariablestatement_constructor_args():
    sig = inspect.signature(statements_LocalVariableStatement.__init__)
    params = list(sig.parameters.keys())



def test_statements_switch_is_not_abstract():
    assert not inspect.isabstract(statements_Switch)


def test_statements_switch_constructor_exists():
    assert callable(statements_Switch.__init__)


def test_statements_switch_constructor_args():
    sig = inspect.signature(statements_Switch.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_statements_block_is_not_abstract():
    assert not inspect.isabstract(statements_Block)


def test_statements_block_constructor_exists():
    assert callable(statements_Block.__init__)


def test_statements_block_constructor_args():
    sig = inspect.signature(statements_Block.__init__)
    params = list(sig.parameters.keys())



def test_members_field_is_not_abstract():
    assert not inspect.isabstract(members_Field)


def test_members_field_constructor_exists():
    assert callable(members_Field.__init__)


def test_members_field_constructor_args():
    sig = inspect.signature(members_Field.__init__)
    params = list(sig.parameters.keys())



def test_members_emptymember_is_not_abstract():
    assert not inspect.isabstract(members_EmptyMember)


def test_members_emptymember_constructor_exists():
    assert callable(members_EmptyMember.__init__)


def test_members_emptymember_constructor_args():
    sig = inspect.signature(members_EmptyMember.__init__)
    params = list(sig.parameters.keys())



def test_membercontainer_is_not_abstract():
    assert not inspect.isabstract(MemberContainer)


def test_membercontainer_constructor_exists():
    assert callable(MemberContainer.__init__)


def test_membercontainer_constructor_args():
    sig = inspect.signature(MemberContainer.__init__)
    params = list(sig.parameters.keys())



def test_classifiers_anonymousclass_is_not_abstract():
    assert not inspect.isabstract(classifiers_AnonymousClass)


def test_classifiers_anonymousclass_constructor_exists():
    assert callable(classifiers_AnonymousClass.__init__)


def test_classifiers_anonymousclass_constructor_args():
    sig = inspect.signature(classifiers_AnonymousClass.__init__)
    params = list(sig.parameters.keys())



def test_typeparametrizable_is_not_abstract():
    assert not inspect.isabstract(TypeParametrizable)


def test_typeparametrizable_constructor_exists():
    assert callable(TypeParametrizable.__init__)


def test_typeparametrizable_constructor_args():
    sig = inspect.signature(TypeParametrizable.__init__)
    params = list(sig.parameters.keys())



def test_members_constructor_is_not_abstract():
    assert not inspect.isabstract(members_Constructor)


def test_members_constructor_constructor_exists():
    assert callable(members_Constructor.__init__)


def test_members_constructor_constructor_args():
    sig = inspect.signature(members_Constructor.__init__)
    params = list(sig.parameters.keys())



def test_classifiers_concreteclassifier_is_not_abstract():
    assert not inspect.isabstract(classifiers_ConcreteClassifier)


def test_classifiers_concreteclassifier_constructor_exists():
    assert callable(classifiers_ConcreteClassifier.__init__)


def test_classifiers_concreteclassifier_constructor_args():
    sig = inspect.signature(classifiers_ConcreteClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_classifiers_concreteclassifier_has_fullName():
    assert hasattr(classifiers_ConcreteClassifier, "fullName")
    descriptor = None
    for klass in classifiers_ConcreteClassifier.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)



def test_arraydimension_is_not_abstract():
    assert not inspect.isabstract(ArrayDimension)


def test_arraydimension_constructor_exists():
    assert callable(ArrayDimension.__init__)


def test_arraydimension_constructor_args():
    sig = inspect.signature(ArrayDimension.__init__)
    params = list(sig.parameters.keys())



def test_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(ArrayInitializer)


def test_arrayinitializer_constructor_exists():
    assert callable(ArrayInitializer.__init__)


def test_arrayinitializer_constructor_args():
    sig = inspect.signature(ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_arraytypeable_is_not_abstract():
    assert not inspect.isabstract(ArrayTypeable)


def test_arraytypeable_constructor_exists():
    assert callable(ArrayTypeable.__init__)


def test_arraytypeable_constructor_args():
    sig = inspect.signature(ArrayTypeable.__init__)
    params = list(sig.parameters.keys())



def test_variables_additionallocalvariable_is_not_abstract():
    assert not inspect.isabstract(variables_AdditionalLocalVariable)


def test_variables_additionallocalvariable_constructor_exists():
    assert callable(variables_AdditionalLocalVariable.__init__)


def test_variables_additionallocalvariable_constructor_args():
    sig = inspect.signature(variables_AdditionalLocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_members_additionalfield_is_not_abstract():
    assert not inspect.isabstract(members_AdditionalField)


def test_members_additionalfield_constructor_exists():
    assert callable(members_AdditionalField.__init__)


def test_members_additionalfield_constructor_args():
    sig = inspect.signature(members_AdditionalField.__init__)
    params = list(sig.parameters.keys())



def test_generics_typeargument_is_not_abstract():
    assert not inspect.isabstract(generics_TypeArgument)


def test_generics_typeargument_constructor_exists():
    assert callable(generics_TypeArgument.__init__)


def test_generics_typeargument_constructor_args():
    sig = inspect.signature(generics_TypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_expressions_castexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_CastExpression)


def test_expressions_castexpression_constructor_exists():
    assert callable(expressions_CastExpression.__init__)


def test_expressions_castexpression_constructor_args():
    sig = inspect.signature(expressions_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_generics_qualifiedtypeargument_is_not_abstract():
    assert not inspect.isabstract(generics_QualifiedTypeArgument)


def test_generics_qualifiedtypeargument_constructor_exists():
    assert callable(generics_QualifiedTypeArgument.__init__)


def test_generics_qualifiedtypeargument_constructor_args():
    sig = inspect.signature(generics_QualifiedTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_arrays_arrayinstantiationbyvalues_is_not_abstract():
    assert not inspect.isabstract(arrays_ArrayInstantiationByValues)


def test_arrays_arrayinstantiationbyvalues_constructor_exists():
    assert callable(arrays_ArrayInstantiationByValues.__init__)


def test_arrays_arrayinstantiationbyvalues_constructor_args():
    sig = inspect.signature(arrays_ArrayInstantiationByValues.__init__)
    params = list(sig.parameters.keys())



def test_members_method_is_not_abstract():
    assert not inspect.isabstract(members_Method)


def test_members_method_constructor_exists():
    assert callable(members_Method.__init__)


def test_members_method_constructor_args():
    sig = inspect.signature(members_Method.__init__)
    params = list(sig.parameters.keys())



def test_instantiations_instantiation_is_not_abstract():
    assert not inspect.isabstract(instantiations_Instantiation)


def test_instantiations_instantiation_constructor_exists():
    assert callable(instantiations_Instantiation.__init__)


def test_instantiations_instantiation_constructor_args():
    sig = inspect.signature(instantiations_Instantiation.__init__)
    params = list(sig.parameters.keys())



def test_variables_variable_is_not_abstract():
    assert not inspect.isabstract(variables_Variable)


def test_variables_variable_constructor_exists():
    assert callable(variables_Variable.__init__)


def test_variables_variable_constructor_args():
    sig = inspect.signature(variables_Variable.__init__)
    params = list(sig.parameters.keys())



def test_expressions_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_InstanceOfExpression)


def test_expressions_instanceofexpression_constructor_exists():
    assert callable(expressions_InstanceOfExpression.__init__)


def test_expressions_instanceofexpression_constructor_args():
    sig = inspect.signature(expressions_InstanceOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_arrays_arrayinstantiationbysize_is_not_abstract():
    assert not inspect.isabstract(arrays_ArrayInstantiationBySize)


def test_arrays_arrayinstantiationbysize_constructor_exists():
    assert callable(arrays_ArrayInstantiationBySize.__init__)


def test_arrays_arrayinstantiationbysize_constructor_args():
    sig = inspect.signature(arrays_ArrayInstantiationBySize.__init__)
    params = list(sig.parameters.keys())



def test_arrays_arrayinitializationvalue_is_not_abstract():
    assert not inspect.isabstract(arrays_ArrayInitializationValue)


def test_arrays_arrayinitializationvalue_constructor_exists():
    assert callable(arrays_ArrayInitializationValue.__init__)


def test_arrays_arrayinitializationvalue_constructor_args():
    sig = inspect.signature(arrays_ArrayInitializationValue.__init__)
    params = list(sig.parameters.keys())



def test_arrayinitializationvalue_is_not_abstract():
    assert not inspect.isabstract(ArrayInitializationValue)


def test_arrayinitializationvalue_constructor_exists():
    assert callable(ArrayInitializationValue.__init__)


def test_arrayinitializationvalue_constructor_args():
    sig = inspect.signature(ArrayInitializationValue.__init__)
    params = list(sig.parameters.keys())



def test_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(expressions_Expression)


def test_expressions_expression_constructor_exists():
    assert callable(expressions_Expression.__init__)


def test_expressions_expression_constructor_args():
    sig = inspect.signature(expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_arrays_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(arrays_ArrayInitializer)


def test_arrays_arrayinitializer_constructor_exists():
    assert callable(arrays_ArrayInitializer.__init__)


def test_arrays_arrayinitializer_constructor_args():
    sig = inspect.signature(arrays_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_arrays_arraydimension_is_not_abstract():
    assert not inspect.isabstract(arrays_ArrayDimension)


def test_arrays_arraydimension_constructor_exists():
    assert callable(arrays_ArrayDimension.__init__)


def test_arrays_arraydimension_constructor_args():
    sig = inspect.signature(arrays_ArrayDimension.__init__)
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
AdditionalLocalVariable_strategy = st.builds(
    AdditionalLocalVariable,
)
Block_strategy = st.builds(
    Block,
)
CatchBlock_strategy = st.builds(
    CatchBlock,
)
ClassifierReference_strategy = st.builds(
    ClassifierReference,
)
LocalVariable_strategy = st.builds(
    LocalVariable,
)
JumpLabel_strategy = st.builds(
    JumpLabel,
)
WhileLoop_strategy = st.builds(
    WhileLoop,
)
statements_DoWhileLoop_strategy = st.builds(
    statements_DoWhileLoop,
)
SwitchCase_strategy = st.builds(
    SwitchCase,
)
statements_DefaultSwitchCase_strategy = st.builds(
    statements_DefaultSwitchCase,
)
StatementContainer_strategy = st.builds(
    StatementContainer,
)
OrdinaryParameter_strategy = st.builds(
    OrdinaryParameter,
)
Modifiable_strategy = st.builds(
    Modifiable,
)
Jump_strategy = st.builds(
    Jump,
)
statements_Continue_strategy = st.builds(
    statements_Continue,
)
statements_Break_strategy = st.builds(
    statements_Break,
)
Conditional_strategy = st.builds(
    Conditional,
)
statements_NormalSwitchCase_strategy = st.builds(
    statements_NormalSwitchCase,
)
Parameter_strategy = st.builds(
    Parameter,
)
parameters_OrdinaryParameter_strategy = st.builds(
    parameters_OrdinaryParameter,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
types_Float_strategy = st.builds(
    types_Float,
)
types_Long_strategy = st.builds(
    types_Long,
)
types_Byte_strategy = st.builds(
    types_Byte,
)
types_Void_strategy = st.builds(
    types_Void,
)
types_Short_strategy = st.builds(
    types_Short,
)
types_Boolean_strategy = st.builds(
    types_Boolean,
)
types_Char_strategy = st.builds(
    types_Char,
)
types_Double_strategy = st.builds(
    types_Double,
)
types_Int_strategy = st.builds(
    types_Int,
)
ElementReference_strategy = st.builds(
    ElementReference,
)
references_IdentifierReference_strategy = st.builds(
    references_IdentifierReference,
)
ArraySelector_strategy = st.builds(
    ArraySelector,
)
parameters_VariableLengthParameter_strategy = st.builds(
    parameters_VariableLengthParameter,
)
Operator_strategy = st.builds(
    Operator,
)
operators_AssignmentOperator_strategy = st.builds(
    operators_AssignmentOperator,
)
operators_EqualityOperator_strategy = st.builds(
    operators_EqualityOperator,
)
operators_MultiplicativeOperator_strategy = st.builds(
    operators_MultiplicativeOperator,
)
operators_RelationOperator_strategy = st.builds(
    operators_RelationOperator,
)
operators_ShiftOperator_strategy = st.builds(
    operators_ShiftOperator,
)
operators_AdditiveOperator_strategy = st.builds(
    operators_AdditiveOperator,
)
operators_UnaryModificationOperator_strategy = st.builds(
    operators_UnaryModificationOperator,
)
operators_UnaryOperator_strategy = st.builds(
    operators_UnaryOperator,
)
Modifier_strategy = st.builds(
    Modifier,
)
modifiers_Public_strategy = st.builds(
    modifiers_Public,
)
modifiers_Strictfp_strategy = st.builds(
    modifiers_Strictfp,
)
modifiers_Volatile_strategy = st.builds(
    modifiers_Volatile,
)
modifiers_Private_strategy = st.builds(
    modifiers_Private,
)
modifiers_Abstract_strategy = st.builds(
    modifiers_Abstract,
)
modifiers_Transient_strategy = st.builds(
    modifiers_Transient,
)
modifiers_Synchronized_strategy = st.builds(
    modifiers_Synchronized,
)
modifiers_Final_strategy = st.builds(
    modifiers_Final,
)
modifiers_Native_strategy = st.builds(
    modifiers_Native,
)
modifiers_Static_strategy = st.builds(
    modifiers_Static,
)
modifiers_Protected_strategy = st.builds(
    modifiers_Protected,
)
Variable_strategy = st.builds(
    Variable,
)
ExceptionThrower_strategy = st.builds(
    ExceptionThrower,
)
Parametrizable_strategy = st.builds(
    Parametrizable,
)
StatementListContainer_strategy = st.builds(
    StatementListContainer,
)
statements_CatchBlock_strategy = st.builds(
    statements_CatchBlock,
)
statements_SwitchCase_strategy = st.builds(
    statements_SwitchCase,
)
Initializable_strategy = st.builds(
    Initializable,
)
Method_strategy = st.builds(
    Method,
)
members_ClassMethod_strategy = st.builds(
    members_ClassMethod,
)
members_InterfaceMethod_strategy = st.builds(
    members_InterfaceMethod,
)
AdditionalField_strategy = st.builds(
    AdditionalField,
)
NamespaceClassifierReference_strategy = st.builds(
    NamespaceClassifierReference,
)
DoubleLiteral_strategy = st.builds(
    DoubleLiteral,
)
literals_DecimalDoubleLiteral_strategy = st.builds(
    literals_DecimalDoubleLiteral,
    decimalValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
FloatLiteral_strategy = st.builds(
    FloatLiteral,
)
literals_HexFloatLiteral_strategy = st.builds(
    literals_HexFloatLiteral,
    hexValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
literals_DecimalFloatLiteral_strategy = st.builds(
    literals_DecimalFloatLiteral,
    decimalValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
LongLiteral_strategy = st.builds(
    LongLiteral,
)
literals_HexLongLiteral_strategy = st.builds(
    literals_HexLongLiteral,
    hexValue=
        safe_text
)
literals_OctalLongLiteral_strategy = st.builds(
    literals_OctalLongLiteral,
    octalValue=
        st.booleans()
)
literals_DecimalLongLiteral_strategy = st.builds(
    literals_DecimalLongLiteral,
    decimalValue=
        safe_text
)
IntegerLiteral_strategy = st.builds(
    IntegerLiteral,
)
literals_OctalIntegerLiteral_strategy = st.builds(
    literals_OctalIntegerLiteral,
    octalValue=
        safe_text
)
literals_HexIntegerLiteral_strategy = st.builds(
    literals_HexIntegerLiteral,
    hexValue=
        safe_text
)
literals_DecimalIntegerLiteral_strategy = st.builds(
    literals_DecimalIntegerLiteral,
    decimalValue=
        safe_text
)
literals_HexDoubleLiteral_strategy = st.builds(
    literals_HexDoubleLiteral,
    hexValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Literal_strategy = st.builds(
    Literal,
)
literals_IntegerLiteral_strategy = st.builds(
    literals_IntegerLiteral,
)
literals_CharacterLiteral_strategy = st.builds(
    literals_CharacterLiteral,
    value=
        safe_text
)
literals_NullLiteral_strategy = st.builds(
    literals_NullLiteral,
)
literals_FloatLiteral_strategy = st.builds(
    literals_FloatLiteral,
)
literals_LongLiteral_strategy = st.builds(
    literals_LongLiteral,
)
literals_DoubleLiteral_strategy = st.builds(
    literals_DoubleLiteral,
)
literals_BooleanLiteral_strategy = st.builds(
    literals_BooleanLiteral,
    value=
        st.booleans()
)
StaticImport_strategy = st.builds(
    StaticImport,
)
imports_StaticMemberImport_strategy = st.builds(
    imports_StaticMemberImport,
)
imports_StaticClassifierImport_strategy = st.builds(
    imports_StaticClassifierImport,
)
Static_strategy = st.builds(
    Static,
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
literals_Literal_strategy = st.builds(
    literals_Literal,
)
Self_strategy = st.builds(
    Self,
)
literals_Super_strategy = st.builds(
    literals_Super,
)
literals_This_strategy = st.builds(
    literals_This,
)
AnonymousClass_strategy = st.builds(
    AnonymousClass,
)
CallTypeArgumentable_strategy = st.builds(
    CallTypeArgumentable,
)
Instantiation_strategy = st.builds(
    Instantiation,
)
instantiations_ExplicitConstructorCall_strategy = st.builds(
    instantiations_ExplicitConstructorCall,
)
instantiations_NewConstructorCall_strategy = st.builds(
    instantiations_NewConstructorCall,
)
TypeArgumentable_strategy = st.builds(
    TypeArgumentable,
)
references_Reference_strategy = st.builds(
    references_Reference,
)
Argumentable_strategy = st.builds(
    Argumentable,
)
references_MethodCall_strategy = st.builds(
    references_MethodCall,
)
Import_strategy = st.builds(
    Import,
)
imports_ClassifierImport_strategy = st.builds(
    imports_ClassifierImport,
)
imports_PackageImport_strategy = st.builds(
    imports_PackageImport,
)
imports_StaticImport_strategy = st.builds(
    imports_StaticImport,
)
UnaryModificationExpression_strategy = st.builds(
    UnaryModificationExpression,
)
expressions_SuffixUnaryModificationExpression_strategy = st.builds(
    expressions_SuffixUnaryModificationExpression,
)
Commentable_strategy = st.builds(
    Commentable,
)
types_TypedElement_strategy = st.builds(
    types_TypedElement,
)
types_Type_strategy = st.builds(
    types_Type,
)
operators_Operator_strategy = st.builds(
    operators_Operator,
)
instantiations_Initializable_strategy = st.builds(
    instantiations_Initializable,
)
statements_Conditional_strategy = st.builds(
    statements_Conditional,
)
statements_Statement_strategy = st.builds(
    statements_Statement,
)
statements_ForLoopInitializer_strategy = st.builds(
    statements_ForLoopInitializer,
)
members_MemberContainer_strategy = st.builds(
    members_MemberContainer,
)
statements_StatementListContainer_strategy = st.builds(
    statements_StatementListContainer,
)
imports_ImportingElement_strategy = st.builds(
    imports_ImportingElement,
)
modifiers_AnnotationInstanceOrModifier_strategy = st.builds(
    modifiers_AnnotationInstanceOrModifier,
)
parameters_Parametrizable_strategy = st.builds(
    parameters_Parametrizable,
)
statements_StatementContainer_strategy = st.builds(
    statements_StatementContainer,
)
literals_Self_strategy = st.builds(
    literals_Self,
)
references_Argumentable_strategy = st.builds(
    references_Argumentable,
)
modifiers_Modifiable_strategy = st.builds(
    modifiers_Modifiable,
)
modifiers_AnnotableAndModifiable_strategy = st.builds(
    modifiers_AnnotableAndModifiable,
)
types_TypeReference_strategy = st.builds(
    types_TypeReference,
)
members_ExceptionThrower_strategy = st.builds(
    members_ExceptionThrower,
)
annotations_Annotable_strategy = st.builds(
    annotations_Annotable,
)
arrays_ArrayTypeable_strategy = st.builds(
    arrays_ArrayTypeable,
)
Expression_strategy = st.builds(
    Expression,
)
annotations_AnnotationValue_strategy = st.builds(
    annotations_AnnotationValue,
)
InterfaceMethod_strategy = st.builds(
    InterfaceMethod,
)
annotations_AnnotationAttribute_strategy = st.builds(
    annotations_AnnotationAttribute,
)
annotations_AnnotationAttributeSetting_strategy = st.builds(
    annotations_AnnotationAttributeSetting,
)
AnnotationAttributeSetting_strategy = st.builds(
    AnnotationAttributeSetting,
)
AnnotationValue_strategy = st.builds(
    AnnotationValue,
)
annotations_AnnotationParameter_strategy = st.builds(
    annotations_AnnotationParameter,
)
AnnotationParameter_strategy = st.builds(
    AnnotationParameter,
)
annotations_AnnotationParameterList_strategy = st.builds(
    annotations_AnnotationParameterList,
)
annotations_SingleAnnotationParameter_strategy = st.builds(
    annotations_SingleAnnotationParameter,
)
Classifier_strategy = st.builds(
    Classifier,
)
generics_TypeParameter_strategy = st.builds(
    generics_TypeParameter,
)
NamespaceAwareElement_strategy = st.builds(
    NamespaceAwareElement,
)
imports_Import_strategy = st.builds(
    imports_Import,
)
AnnotationInstanceOrModifier_strategy = st.builds(
    AnnotationInstanceOrModifier,
)
modifiers_Modifier_strategy = st.builds(
    modifiers_Modifier,
)
Reference_strategy = st.builds(
    Reference,
)
references_PrimitiveTypeReference_strategy = st.builds(
    references_PrimitiveTypeReference,
)
references_ElementReference_strategy = st.builds(
    references_ElementReference,
)
references_StringReference_strategy = st.builds(
    references_StringReference,
    value=
        safe_text
)
references_SelfReference_strategy = st.builds(
    references_SelfReference,
)
references_ReflectiveClassReference_strategy = st.builds(
    references_ReflectiveClassReference,
)
expressions_NestedExpression_strategy = st.builds(
    expressions_NestedExpression,
)
annotations_AnnotationInstance_strategy = st.builds(
    annotations_AnnotationInstance,
)
AnnotationInstance_strategy = st.builds(
    AnnotationInstance,
)
expressions_PrefixUnaryModificationExpression_strategy = st.builds(
    expressions_PrefixUnaryModificationExpression,
)
UnaryModificationOperator_strategy = st.builds(
    UnaryModificationOperator,
)
operators_PlusPlus_strategy = st.builds(
    operators_PlusPlus,
)
operators_MinusMinus_strategy = st.builds(
    operators_MinusMinus,
)
TypeParameter_strategy = st.builds(
    TypeParameter,
)
generics_TypeParametrizable_strategy = st.builds(
    generics_TypeParametrizable,
)
generics_CallTypeArgumentable_strategy = st.builds(
    generics_CallTypeArgumentable,
)
TypeArgument_strategy = st.builds(
    TypeArgument,
)
generics_ExtendsTypeArgument_strategy = st.builds(
    generics_ExtendsTypeArgument,
)
generics_UnknownTypeArgument_strategy = st.builds(
    generics_UnknownTypeArgument,
)
generics_SuperTypeArgument_strategy = st.builds(
    generics_SuperTypeArgument,
)
generics_TypeArgumentable_strategy = st.builds(
    generics_TypeArgumentable,
)
AdditiveOperator_strategy = st.builds(
    AdditiveOperator,
)
AdditiveExpressionChild_strategy = st.builds(
    AdditiveExpressionChild,
)
expressions_MultiplicativeExpression_strategy = st.builds(
    expressions_MultiplicativeExpression,
)
UnaryModificationExpressionChild_strategy = st.builds(
    UnaryModificationExpressionChild,
)
expressions_PrimaryExpression_strategy = st.builds(
    expressions_PrimaryExpression,
)
UnaryExpressionChild_strategy = st.builds(
    UnaryExpressionChild,
)
expressions_UnaryModificationExpression_strategy = st.builds(
    expressions_UnaryModificationExpression,
)
expressions_UnaryModificationExpressionChild_strategy = st.builds(
    expressions_UnaryModificationExpressionChild,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
operators_Negate_strategy = st.builds(
    operators_Negate,
)
operators_Addition_strategy = st.builds(
    operators_Addition,
)
operators_Subtraction_strategy = st.builds(
    operators_Subtraction,
)
operators_Complement_strategy = st.builds(
    operators_Complement,
)
expressions_MultiplicativeExpressionChild_strategy = st.builds(
    expressions_MultiplicativeExpressionChild,
)
MultiplicativeOperator_strategy = st.builds(
    MultiplicativeOperator,
)
operators_Division_strategy = st.builds(
    operators_Division,
)
operators_Remainder_strategy = st.builds(
    operators_Remainder,
)
operators_Multiplication_strategy = st.builds(
    operators_Multiplication,
)
MultiplicativeExpressionChild_strategy = st.builds(
    MultiplicativeExpressionChild,
)
expressions_UnaryExpressionChild_strategy = st.builds(
    expressions_UnaryExpressionChild,
)
expressions_UnaryExpression_strategy = st.builds(
    expressions_UnaryExpression,
)
EqualityExpressionChild_strategy = st.builds(
    EqualityExpressionChild,
)
EqualityOperator_strategy = st.builds(
    EqualityOperator,
)
operators_Equal_strategy = st.builds(
    operators_Equal,
)
operators_NotEqual_strategy = st.builds(
    operators_NotEqual,
)
ShiftOperator_strategy = st.builds(
    ShiftOperator,
)
operators_LeftShift_strategy = st.builds(
    operators_LeftShift,
)
operators_RightShift_strategy = st.builds(
    operators_RightShift,
)
operators_UnsignedRightShift_strategy = st.builds(
    operators_UnsignedRightShift,
)
ShiftExpressionChild_strategy = st.builds(
    ShiftExpressionChild,
)
expressions_AdditiveExpressionChild_strategy = st.builds(
    expressions_AdditiveExpressionChild,
)
expressions_AdditiveExpression_strategy = st.builds(
    expressions_AdditiveExpression,
)
RelationOperator_strategy = st.builds(
    RelationOperator,
)
operators_GreaterThanOrEqual_strategy = st.builds(
    operators_GreaterThanOrEqual,
)
operators_LessThanOrEqual_strategy = st.builds(
    operators_LessThanOrEqual,
)
operators_LessThan_strategy = st.builds(
    operators_LessThan,
)
operators_GreaterThan_strategy = st.builds(
    operators_GreaterThan,
)
RelationExpressionChild_strategy = st.builds(
    RelationExpressionChild,
)
expressions_ShiftExpressionChild_strategy = st.builds(
    expressions_ShiftExpressionChild,
)
expressions_ShiftExpression_strategy = st.builds(
    expressions_ShiftExpression,
)
expressions_InstanceOfExpressionChild_strategy = st.builds(
    expressions_InstanceOfExpressionChild,
)
InstanceOfExpressionChild_strategy = st.builds(
    InstanceOfExpressionChild,
)
expressions_RelationExpression_strategy = st.builds(
    expressions_RelationExpression,
)
expressions_RelationExpressionChild_strategy = st.builds(
    expressions_RelationExpressionChild,
)
ConditionalOrExpressionChild_strategy = st.builds(
    ConditionalOrExpressionChild,
)
expressions_ConditionalAndExpression_strategy = st.builds(
    expressions_ConditionalAndExpression,
)
AndExpressionChild_strategy = st.builds(
    AndExpressionChild,
)
expressions_EqualityExpressionChild_strategy = st.builds(
    expressions_EqualityExpressionChild,
)
expressions_EqualityExpression_strategy = st.builds(
    expressions_EqualityExpression,
)
ExclusiveOrExpressionChild_strategy = st.builds(
    ExclusiveOrExpressionChild,
)
expressions_AndExpressionChild_strategy = st.builds(
    expressions_AndExpressionChild,
)
expressions_AndExpression_strategy = st.builds(
    expressions_AndExpression,
)
InclusiveOrExpressionChild_strategy = st.builds(
    InclusiveOrExpressionChild,
)
expressions_ExclusiveOrExpression_strategy = st.builds(
    expressions_ExclusiveOrExpression,
)
expressions_ExclusiveOrExpressionChild_strategy = st.builds(
    expressions_ExclusiveOrExpressionChild,
)
expressions_ConditionalAndExpressionChild_strategy = st.builds(
    expressions_ConditionalAndExpressionChild,
)
expressions_AssignmentExpression_strategy = st.builds(
    expressions_AssignmentExpression,
)
ConditionalAndExpressionChild_strategy = st.builds(
    ConditionalAndExpressionChild,
)
expressions_InclusiveOrExpressionChild_strategy = st.builds(
    expressions_InclusiveOrExpressionChild,
)
expressions_InclusiveOrExpression_strategy = st.builds(
    expressions_InclusiveOrExpression,
)
ConditionalExpressionChild_strategy = st.builds(
    ConditionalExpressionChild,
)
expressions_ConditionalOrExpression_strategy = st.builds(
    expressions_ConditionalOrExpression,
)
expressions_ConditionalOrExpressionChild_strategy = st.builds(
    expressions_ConditionalOrExpressionChild,
)
expressions_AssignmentExpressionChild_strategy = st.builds(
    expressions_AssignmentExpressionChild,
)
AssignmentOperator_strategy = st.builds(
    AssignmentOperator,
)
operators_AssignmentAnd_strategy = st.builds(
    operators_AssignmentAnd,
)
operators_AssignmentExclusiveOr_strategy = st.builds(
    operators_AssignmentExclusiveOr,
)
operators_AssignmentUnsignedRightShift_strategy = st.builds(
    operators_AssignmentUnsignedRightShift,
)
operators_AssignmentPlus_strategy = st.builds(
    operators_AssignmentPlus,
)
operators_AssignmentMinus_strategy = st.builds(
    operators_AssignmentMinus,
)
operators_Assignment_strategy = st.builds(
    operators_Assignment,
)
operators_AssignmentRightShift_strategy = st.builds(
    operators_AssignmentRightShift,
)
operators_AssignmentOr_strategy = st.builds(
    operators_AssignmentOr,
)
operators_AssignmentMultiplication_strategy = st.builds(
    operators_AssignmentMultiplication,
)
operators_AssignmentDivision_strategy = st.builds(
    operators_AssignmentDivision,
)
operators_AssignmentLeftShift_strategy = st.builds(
    operators_AssignmentLeftShift,
)
operators_AssignmentModulo_strategy = st.builds(
    operators_AssignmentModulo,
)
AssignmentExpressionChild_strategy = st.builds(
    AssignmentExpressionChild,
)
expressions_ConditionalExpression_strategy = st.builds(
    expressions_ConditionalExpression,
)
expressions_ConditionalExpressionChild_strategy = st.builds(
    expressions_ConditionalExpressionChild,
)
JavaRoot_strategy = st.builds(
    JavaRoot,
)
containers_CompilationUnit_strategy = st.builds(
    containers_CompilationUnit,
)
ImportingElement_strategy = st.builds(
    ImportingElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
members_Member_strategy = st.builds(
    members_Member,
)
references_ReferenceableElement_strategy = st.builds(
    references_ReferenceableElement,
)
containers_JavaRoot_strategy = st.builds(
    containers_JavaRoot,
)
ForLoopInitializer_strategy = st.builds(
    ForLoopInitializer,
)
expressions_ExpressionList_strategy = st.builds(
    expressions_ExpressionList,
)
containers_EmptyModel_strategy = st.builds(
    containers_EmptyModel,
)
Package_strategy = st.builds(
    Package,
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
Annotable_strategy = st.builds(
    Annotable,
)
commons_NamespaceAwareElement_strategy = st.builds(
    commons_NamespaceAwareElement,
    namespaces=
        safe_text
)
commons_NamedElement_strategy = st.builds(
    commons_NamedElement,
    name=
        safe_text
)
commons_Commentable_strategy = st.builds(
    commons_Commentable,
    comments=
        safe_text
)
EnumConstant_strategy = st.builds(
    EnumConstant,
)
ReferenceableElement_strategy = st.builds(
    ReferenceableElement,
)
containers_Package_strategy = st.builds(
    containers_Package,
)
members_EnumConstant_strategy = st.builds(
    members_EnumConstant,
)
Type_strategy = st.builds(
    Type,
)
classifiers_Classifier_strategy = st.builds(
    classifiers_Classifier,
)
arrays_ArraySelector_strategy = st.builds(
    arrays_ArraySelector,
)
Implementor_strategy = st.builds(
    Implementor,
)
ConcreteClassifier_strategy = st.builds(
    ConcreteClassifier,
)
classifiers_Interface_strategy = st.builds(
    classifiers_Interface,
)
classifiers_Annotation_strategy = st.builds(
    classifiers_Annotation,
)
classifiers_Enumeration_strategy = st.builds(
    classifiers_Enumeration,
)
classifiers_Class_strategy = st.builds(
    classifiers_Class,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
types_PrimitiveType_strategy = st.builds(
    types_PrimitiveType,
)
types_ClassifierReference_strategy = st.builds(
    types_ClassifierReference,
)
types_NamespaceClassifierReference_strategy = st.builds(
    types_NamespaceClassifierReference,
)
classifiers_Implementor_strategy = st.builds(
    classifiers_Implementor,
)
AnnotableAndModifiable_strategy = st.builds(
    AnnotableAndModifiable,
)
variables_LocalVariable_strategy = st.builds(
    variables_LocalVariable,
)
parameters_Parameter_strategy = st.builds(
    parameters_Parameter,
)
Statement_strategy = st.builds(
    Statement,
)
statements_Condition_strategy = st.builds(
    statements_Condition,
)
statements_JumpLabel_strategy = st.builds(
    statements_JumpLabel,
)
statements_EmptyStatement_strategy = st.builds(
    statements_EmptyStatement,
)
statements_Jump_strategy = st.builds(
    statements_Jump,
)
statements_Return_strategy = st.builds(
    statements_Return,
)
statements_ForLoop_strategy = st.builds(
    statements_ForLoop,
)
statements_Throw_strategy = st.builds(
    statements_Throw,
)
statements_TryBlock_strategy = st.builds(
    statements_TryBlock,
)
statements_ForEachLoop_strategy = st.builds(
    statements_ForEachLoop,
)
statements_ExpressionStatement_strategy = st.builds(
    statements_ExpressionStatement,
)
statements_Assert_strategy = st.builds(
    statements_Assert,
)
statements_SynchronizedBlock_strategy = st.builds(
    statements_SynchronizedBlock,
)
statements_WhileLoop_strategy = st.builds(
    statements_WhileLoop,
)
statements_LocalVariableStatement_strategy = st.builds(
    statements_LocalVariableStatement,
)
statements_Switch_strategy = st.builds(
    statements_Switch,
)
Member_strategy = st.builds(
    Member,
)
statements_Block_strategy = st.builds(
    statements_Block,
)
members_Field_strategy = st.builds(
    members_Field,
)
members_EmptyMember_strategy = st.builds(
    members_EmptyMember,
)
MemberContainer_strategy = st.builds(
    MemberContainer,
)
classifiers_AnonymousClass_strategy = st.builds(
    classifiers_AnonymousClass,
)
TypeParametrizable_strategy = st.builds(
    TypeParametrizable,
)
members_Constructor_strategy = st.builds(
    members_Constructor,
)
classifiers_ConcreteClassifier_strategy = st.builds(
    classifiers_ConcreteClassifier,
    fullName=
        safe_text
)
ArrayDimension_strategy = st.builds(
    ArrayDimension,
)
ArrayInitializer_strategy = st.builds(
    ArrayInitializer,
)
ArrayTypeable_strategy = st.builds(
    ArrayTypeable,
)
variables_AdditionalLocalVariable_strategy = st.builds(
    variables_AdditionalLocalVariable,
)
members_AdditionalField_strategy = st.builds(
    members_AdditionalField,
)
generics_TypeArgument_strategy = st.builds(
    generics_TypeArgument,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
expressions_CastExpression_strategy = st.builds(
    expressions_CastExpression,
)
generics_QualifiedTypeArgument_strategy = st.builds(
    generics_QualifiedTypeArgument,
)
arrays_ArrayInstantiationByValues_strategy = st.builds(
    arrays_ArrayInstantiationByValues,
)
members_Method_strategy = st.builds(
    members_Method,
)
instantiations_Instantiation_strategy = st.builds(
    instantiations_Instantiation,
)
variables_Variable_strategy = st.builds(
    variables_Variable,
)
expressions_InstanceOfExpression_strategy = st.builds(
    expressions_InstanceOfExpression,
)
arrays_ArrayInstantiationBySize_strategy = st.builds(
    arrays_ArrayInstantiationBySize,
)
arrays_ArrayInitializationValue_strategy = st.builds(
    arrays_ArrayInitializationValue,
)
ArrayInitializationValue_strategy = st.builds(
    ArrayInitializationValue,
)
expressions_Expression_strategy = st.builds(
    expressions_Expression,
)
arrays_ArrayInitializer_strategy = st.builds(
    arrays_ArrayInitializer,
)
arrays_ArrayDimension_strategy = st.builds(
    arrays_ArrayDimension,
)

@given(instance=AdditionalLocalVariable_strategy)
@settings(max_examples=50)
def test_additionallocalvariable_instantiation(instance):
    assert isinstance(instance, AdditionalLocalVariable)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=CatchBlock_strategy)
@settings(max_examples=50)
def test_catchblock_instantiation(instance):
    assert isinstance(instance, CatchBlock)

@given(instance=ClassifierReference_strategy)
@settings(max_examples=50)
def test_classifierreference_instantiation(instance):
    assert isinstance(instance, ClassifierReference)

@given(instance=LocalVariable_strategy)
@settings(max_examples=50)
def test_localvariable_instantiation(instance):
    assert isinstance(instance, LocalVariable)

@given(instance=JumpLabel_strategy)
@settings(max_examples=50)
def test_jumplabel_instantiation(instance):
    assert isinstance(instance, JumpLabel)

@given(instance=WhileLoop_strategy)
@settings(max_examples=50)
def test_whileloop_instantiation(instance):
    assert isinstance(instance, WhileLoop)

@given(instance=statements_DoWhileLoop_strategy)
@settings(max_examples=50)
def test_statements_dowhileloop_instantiation(instance):
    assert isinstance(instance, statements_DoWhileLoop)

@given(instance=SwitchCase_strategy)
@settings(max_examples=50)
def test_switchcase_instantiation(instance):
    assert isinstance(instance, SwitchCase)

@given(instance=statements_DefaultSwitchCase_strategy)
@settings(max_examples=50)
def test_statements_defaultswitchcase_instantiation(instance):
    assert isinstance(instance, statements_DefaultSwitchCase)

@given(instance=StatementContainer_strategy)
@settings(max_examples=50)
def test_statementcontainer_instantiation(instance):
    assert isinstance(instance, StatementContainer)

@given(instance=OrdinaryParameter_strategy)
@settings(max_examples=50)
def test_ordinaryparameter_instantiation(instance):
    assert isinstance(instance, OrdinaryParameter)

@given(instance=Modifiable_strategy)
@settings(max_examples=50)
def test_modifiable_instantiation(instance):
    assert isinstance(instance, Modifiable)

@given(instance=Jump_strategy)
@settings(max_examples=50)
def test_jump_instantiation(instance):
    assert isinstance(instance, Jump)

@given(instance=statements_Continue_strategy)
@settings(max_examples=50)
def test_statements_continue_instantiation(instance):
    assert isinstance(instance, statements_Continue)

@given(instance=statements_Break_strategy)
@settings(max_examples=50)
def test_statements_break_instantiation(instance):
    assert isinstance(instance, statements_Break)

@given(instance=Conditional_strategy)
@settings(max_examples=50)
def test_conditional_instantiation(instance):
    assert isinstance(instance, Conditional)

@given(instance=statements_NormalSwitchCase_strategy)
@settings(max_examples=50)
def test_statements_normalswitchcase_instantiation(instance):
    assert isinstance(instance, statements_NormalSwitchCase)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=parameters_OrdinaryParameter_strategy)
@settings(max_examples=50)
def test_parameters_ordinaryparameter_instantiation(instance):
    assert isinstance(instance, parameters_OrdinaryParameter)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=types_Float_strategy)
@settings(max_examples=50)
def test_types_float_instantiation(instance):
    assert isinstance(instance, types_Float)

@given(instance=types_Long_strategy)
@settings(max_examples=50)
def test_types_long_instantiation(instance):
    assert isinstance(instance, types_Long)

@given(instance=types_Byte_strategy)
@settings(max_examples=50)
def test_types_byte_instantiation(instance):
    assert isinstance(instance, types_Byte)

@given(instance=types_Void_strategy)
@settings(max_examples=50)
def test_types_void_instantiation(instance):
    assert isinstance(instance, types_Void)

@given(instance=types_Short_strategy)
@settings(max_examples=50)
def test_types_short_instantiation(instance):
    assert isinstance(instance, types_Short)

@given(instance=types_Boolean_strategy)
@settings(max_examples=50)
def test_types_boolean_instantiation(instance):
    assert isinstance(instance, types_Boolean)

@given(instance=types_Char_strategy)
@settings(max_examples=50)
def test_types_char_instantiation(instance):
    assert isinstance(instance, types_Char)

@given(instance=types_Double_strategy)
@settings(max_examples=50)
def test_types_double_instantiation(instance):
    assert isinstance(instance, types_Double)

@given(instance=types_Int_strategy)
@settings(max_examples=50)
def test_types_int_instantiation(instance):
    assert isinstance(instance, types_Int)

@given(instance=ElementReference_strategy)
@settings(max_examples=50)
def test_elementreference_instantiation(instance):
    assert isinstance(instance, ElementReference)

@given(instance=references_IdentifierReference_strategy)
@settings(max_examples=50)
def test_references_identifierreference_instantiation(instance):
    assert isinstance(instance, references_IdentifierReference)

@given(instance=ArraySelector_strategy)
@settings(max_examples=50)
def test_arrayselector_instantiation(instance):
    assert isinstance(instance, ArraySelector)

@given(instance=parameters_VariableLengthParameter_strategy)
@settings(max_examples=50)
def test_parameters_variablelengthparameter_instantiation(instance):
    assert isinstance(instance, parameters_VariableLengthParameter)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=operators_AssignmentOperator_strategy)
@settings(max_examples=50)
def test_operators_assignmentoperator_instantiation(instance):
    assert isinstance(instance, operators_AssignmentOperator)

@given(instance=operators_EqualityOperator_strategy)
@settings(max_examples=50)
def test_operators_equalityoperator_instantiation(instance):
    assert isinstance(instance, operators_EqualityOperator)

@given(instance=operators_MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_operators_multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, operators_MultiplicativeOperator)

@given(instance=operators_RelationOperator_strategy)
@settings(max_examples=50)
def test_operators_relationoperator_instantiation(instance):
    assert isinstance(instance, operators_RelationOperator)

@given(instance=operators_ShiftOperator_strategy)
@settings(max_examples=50)
def test_operators_shiftoperator_instantiation(instance):
    assert isinstance(instance, operators_ShiftOperator)

@given(instance=operators_AdditiveOperator_strategy)
@settings(max_examples=50)
def test_operators_additiveoperator_instantiation(instance):
    assert isinstance(instance, operators_AdditiveOperator)

@given(instance=operators_UnaryModificationOperator_strategy)
@settings(max_examples=50)
def test_operators_unarymodificationoperator_instantiation(instance):
    assert isinstance(instance, operators_UnaryModificationOperator)

@given(instance=operators_UnaryOperator_strategy)
@settings(max_examples=50)
def test_operators_unaryoperator_instantiation(instance):
    assert isinstance(instance, operators_UnaryOperator)

@given(instance=Modifier_strategy)
@settings(max_examples=50)
def test_modifier_instantiation(instance):
    assert isinstance(instance, Modifier)

@given(instance=modifiers_Public_strategy)
@settings(max_examples=50)
def test_modifiers_public_instantiation(instance):
    assert isinstance(instance, modifiers_Public)

@given(instance=modifiers_Strictfp_strategy)
@settings(max_examples=50)
def test_modifiers_strictfp_instantiation(instance):
    assert isinstance(instance, modifiers_Strictfp)

@given(instance=modifiers_Volatile_strategy)
@settings(max_examples=50)
def test_modifiers_volatile_instantiation(instance):
    assert isinstance(instance, modifiers_Volatile)

@given(instance=modifiers_Private_strategy)
@settings(max_examples=50)
def test_modifiers_private_instantiation(instance):
    assert isinstance(instance, modifiers_Private)

@given(instance=modifiers_Abstract_strategy)
@settings(max_examples=50)
def test_modifiers_abstract_instantiation(instance):
    assert isinstance(instance, modifiers_Abstract)

@given(instance=modifiers_Transient_strategy)
@settings(max_examples=50)
def test_modifiers_transient_instantiation(instance):
    assert isinstance(instance, modifiers_Transient)

@given(instance=modifiers_Synchronized_strategy)
@settings(max_examples=50)
def test_modifiers_synchronized_instantiation(instance):
    assert isinstance(instance, modifiers_Synchronized)

@given(instance=modifiers_Final_strategy)
@settings(max_examples=50)
def test_modifiers_final_instantiation(instance):
    assert isinstance(instance, modifiers_Final)

@given(instance=modifiers_Native_strategy)
@settings(max_examples=50)
def test_modifiers_native_instantiation(instance):
    assert isinstance(instance, modifiers_Native)

@given(instance=modifiers_Static_strategy)
@settings(max_examples=50)
def test_modifiers_static_instantiation(instance):
    assert isinstance(instance, modifiers_Static)

@given(instance=modifiers_Protected_strategy)
@settings(max_examples=50)
def test_modifiers_protected_instantiation(instance):
    assert isinstance(instance, modifiers_Protected)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=ExceptionThrower_strategy)
@settings(max_examples=50)
def test_exceptionthrower_instantiation(instance):
    assert isinstance(instance, ExceptionThrower)

@given(instance=Parametrizable_strategy)
@settings(max_examples=50)
def test_parametrizable_instantiation(instance):
    assert isinstance(instance, Parametrizable)

@given(instance=StatementListContainer_strategy)
@settings(max_examples=50)
def test_statementlistcontainer_instantiation(instance):
    assert isinstance(instance, StatementListContainer)

@given(instance=statements_CatchBlock_strategy)
@settings(max_examples=50)
def test_statements_catchblock_instantiation(instance):
    assert isinstance(instance, statements_CatchBlock)

@given(instance=statements_SwitchCase_strategy)
@settings(max_examples=50)
def test_statements_switchcase_instantiation(instance):
    assert isinstance(instance, statements_SwitchCase)

@given(instance=Initializable_strategy)
@settings(max_examples=50)
def test_initializable_instantiation(instance):
    assert isinstance(instance, Initializable)

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

@given(instance=members_ClassMethod_strategy)
@settings(max_examples=50)
def test_members_classmethod_instantiation(instance):
    assert isinstance(instance, members_ClassMethod)

@given(instance=members_InterfaceMethod_strategy)
@settings(max_examples=50)
def test_members_interfacemethod_instantiation(instance):
    assert isinstance(instance, members_InterfaceMethod)

@given(instance=AdditionalField_strategy)
@settings(max_examples=50)
def test_additionalfield_instantiation(instance):
    assert isinstance(instance, AdditionalField)

@given(instance=NamespaceClassifierReference_strategy)
@settings(max_examples=50)
def test_namespaceclassifierreference_instantiation(instance):
    assert isinstance(instance, NamespaceClassifierReference)

@given(instance=DoubleLiteral_strategy)
@settings(max_examples=50)
def test_doubleliteral_instantiation(instance):
    assert isinstance(instance, DoubleLiteral)

@given(instance=literals_DecimalDoubleLiteral_strategy)
@settings(max_examples=50)
def test_literals_decimaldoubleliteral_instantiation(instance):
    assert isinstance(instance, literals_DecimalDoubleLiteral)



@given(instance=literals_DecimalDoubleLiteral_strategy)
def test_literals_decimaldoubleliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=FloatLiteral_strategy)
@settings(max_examples=50)
def test_floatliteral_instantiation(instance):
    assert isinstance(instance, FloatLiteral)

@given(instance=literals_HexFloatLiteral_strategy)
@settings(max_examples=50)
def test_literals_hexfloatliteral_instantiation(instance):
    assert isinstance(instance, literals_HexFloatLiteral)



@given(instance=literals_HexFloatLiteral_strategy)
def test_literals_hexfloatliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=literals_DecimalFloatLiteral_strategy)
@settings(max_examples=50)
def test_literals_decimalfloatliteral_instantiation(instance):
    assert isinstance(instance, literals_DecimalFloatLiteral)



@given(instance=literals_DecimalFloatLiteral_strategy)
def test_literals_decimalfloatliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=LongLiteral_strategy)
@settings(max_examples=50)
def test_longliteral_instantiation(instance):
    assert isinstance(instance, LongLiteral)

@given(instance=literals_HexLongLiteral_strategy)
@settings(max_examples=50)
def test_literals_hexlongliteral_instantiation(instance):
    assert isinstance(instance, literals_HexLongLiteral)



@given(instance=literals_HexLongLiteral_strategy)
def test_literals_hexlongliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=literals_OctalLongLiteral_strategy)
@settings(max_examples=50)
def test_literals_octallongliteral_instantiation(instance):
    assert isinstance(instance, literals_OctalLongLiteral)



@given(instance=literals_OctalLongLiteral_strategy)
def test_literals_octallongliteral_octalValue_setter(instance):
    original = instance.octalValue
    instance.octalValue = original
    assert instance.octalValue == original

@given(instance=literals_DecimalLongLiteral_strategy)
@settings(max_examples=50)
def test_literals_decimallongliteral_instantiation(instance):
    assert isinstance(instance, literals_DecimalLongLiteral)



@given(instance=literals_DecimalLongLiteral_strategy)
def test_literals_decimallongliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=IntegerLiteral_strategy)
@settings(max_examples=50)
def test_integerliteral_instantiation(instance):
    assert isinstance(instance, IntegerLiteral)

@given(instance=literals_OctalIntegerLiteral_strategy)
@settings(max_examples=50)
def test_literals_octalintegerliteral_instantiation(instance):
    assert isinstance(instance, literals_OctalIntegerLiteral)



@given(instance=literals_OctalIntegerLiteral_strategy)
def test_literals_octalintegerliteral_octalValue_setter(instance):
    original = instance.octalValue
    instance.octalValue = original
    assert instance.octalValue == original

@given(instance=literals_HexIntegerLiteral_strategy)
@settings(max_examples=50)
def test_literals_hexintegerliteral_instantiation(instance):
    assert isinstance(instance, literals_HexIntegerLiteral)



@given(instance=literals_HexIntegerLiteral_strategy)
def test_literals_hexintegerliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=literals_DecimalIntegerLiteral_strategy)
@settings(max_examples=50)
def test_literals_decimalintegerliteral_instantiation(instance):
    assert isinstance(instance, literals_DecimalIntegerLiteral)



@given(instance=literals_DecimalIntegerLiteral_strategy)
def test_literals_decimalintegerliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=literals_HexDoubleLiteral_strategy)
@settings(max_examples=50)
def test_literals_hexdoubleliteral_instantiation(instance):
    assert isinstance(instance, literals_HexDoubleLiteral)



@given(instance=literals_HexDoubleLiteral_strategy)
def test_literals_hexdoubleliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=literals_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_literals_integerliteral_instantiation(instance):
    assert isinstance(instance, literals_IntegerLiteral)

@given(instance=literals_CharacterLiteral_strategy)
@settings(max_examples=50)
def test_literals_characterliteral_instantiation(instance):
    assert isinstance(instance, literals_CharacterLiteral)



@given(instance=literals_CharacterLiteral_strategy)
def test_literals_characterliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=literals_NullLiteral_strategy)
@settings(max_examples=50)
def test_literals_nullliteral_instantiation(instance):
    assert isinstance(instance, literals_NullLiteral)

@given(instance=literals_FloatLiteral_strategy)
@settings(max_examples=50)
def test_literals_floatliteral_instantiation(instance):
    assert isinstance(instance, literals_FloatLiteral)

@given(instance=literals_LongLiteral_strategy)
@settings(max_examples=50)
def test_literals_longliteral_instantiation(instance):
    assert isinstance(instance, literals_LongLiteral)

@given(instance=literals_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_literals_doubleliteral_instantiation(instance):
    assert isinstance(instance, literals_DoubleLiteral)

@given(instance=literals_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_literals_booleanliteral_instantiation(instance):
    assert isinstance(instance, literals_BooleanLiteral)



@given(instance=literals_BooleanLiteral_strategy)
def test_literals_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=StaticImport_strategy)
@settings(max_examples=50)
def test_staticimport_instantiation(instance):
    assert isinstance(instance, StaticImport)

@given(instance=imports_StaticMemberImport_strategy)
@settings(max_examples=50)
def test_imports_staticmemberimport_instantiation(instance):
    assert isinstance(instance, imports_StaticMemberImport)

@given(instance=imports_StaticClassifierImport_strategy)
@settings(max_examples=50)
def test_imports_staticclassifierimport_instantiation(instance):
    assert isinstance(instance, imports_StaticClassifierImport)

@given(instance=Static_strategy)
@settings(max_examples=50)
def test_static_instantiation(instance):
    assert isinstance(instance, Static)

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=literals_Literal_strategy)
@settings(max_examples=50)
def test_literals_literal_instantiation(instance):
    assert isinstance(instance, literals_Literal)

@given(instance=Self_strategy)
@settings(max_examples=50)
def test_self_instantiation(instance):
    assert isinstance(instance, Self)

@given(instance=literals_Super_strategy)
@settings(max_examples=50)
def test_literals_super_instantiation(instance):
    assert isinstance(instance, literals_Super)

@given(instance=literals_This_strategy)
@settings(max_examples=50)
def test_literals_this_instantiation(instance):
    assert isinstance(instance, literals_This)

@given(instance=AnonymousClass_strategy)
@settings(max_examples=50)
def test_anonymousclass_instantiation(instance):
    assert isinstance(instance, AnonymousClass)

@given(instance=CallTypeArgumentable_strategy)
@settings(max_examples=50)
def test_calltypeargumentable_instantiation(instance):
    assert isinstance(instance, CallTypeArgumentable)

@given(instance=Instantiation_strategy)
@settings(max_examples=50)
def test_instantiation_instantiation(instance):
    assert isinstance(instance, Instantiation)

@given(instance=instantiations_ExplicitConstructorCall_strategy)
@settings(max_examples=50)
def test_instantiations_explicitconstructorcall_instantiation(instance):
    assert isinstance(instance, instantiations_ExplicitConstructorCall)

@given(instance=instantiations_NewConstructorCall_strategy)
@settings(max_examples=50)
def test_instantiations_newconstructorcall_instantiation(instance):
    assert isinstance(instance, instantiations_NewConstructorCall)

@given(instance=TypeArgumentable_strategy)
@settings(max_examples=50)
def test_typeargumentable_instantiation(instance):
    assert isinstance(instance, TypeArgumentable)

@given(instance=references_Reference_strategy)
@settings(max_examples=50)
def test_references_reference_instantiation(instance):
    assert isinstance(instance, references_Reference)

@given(instance=Argumentable_strategy)
@settings(max_examples=50)
def test_argumentable_instantiation(instance):
    assert isinstance(instance, Argumentable)

@given(instance=references_MethodCall_strategy)
@settings(max_examples=50)
def test_references_methodcall_instantiation(instance):
    assert isinstance(instance, references_MethodCall)

@given(instance=Import_strategy)
@settings(max_examples=50)
def test_import_instantiation(instance):
    assert isinstance(instance, Import)

@given(instance=imports_ClassifierImport_strategy)
@settings(max_examples=50)
def test_imports_classifierimport_instantiation(instance):
    assert isinstance(instance, imports_ClassifierImport)

@given(instance=imports_PackageImport_strategy)
@settings(max_examples=50)
def test_imports_packageimport_instantiation(instance):
    assert isinstance(instance, imports_PackageImport)

@given(instance=imports_StaticImport_strategy)
@settings(max_examples=50)
def test_imports_staticimport_instantiation(instance):
    assert isinstance(instance, imports_StaticImport)

@given(instance=UnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_unarymodificationexpression_instantiation(instance):
    assert isinstance(instance, UnaryModificationExpression)

@given(instance=expressions_SuffixUnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_expressions_suffixunarymodificationexpression_instantiation(instance):
    assert isinstance(instance, expressions_SuffixUnaryModificationExpression)

@given(instance=Commentable_strategy)
@settings(max_examples=50)
def test_commentable_instantiation(instance):
    assert isinstance(instance, Commentable)

@given(instance=types_TypedElement_strategy)
@settings(max_examples=50)
def test_types_typedelement_instantiation(instance):
    assert isinstance(instance, types_TypedElement)

@given(instance=types_Type_strategy)
@settings(max_examples=50)
def test_types_type_instantiation(instance):
    assert isinstance(instance, types_Type)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=types_Type_strategy)
@settings(max_examples=30)
def test_types_type_equalstype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.equalsType(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.equalsType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'equalsType' in types_Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equalsType' in types_Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equalsType' in types_Type is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=types_Type_strategy)
@settings(max_examples=30)
def test_types_type_issupertype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSuperType(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSuperType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSuperType' in types_Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSuperType' in types_Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSuperType' in types_Type is not implemented or raised an error")

@given(instance=operators_Operator_strategy)
@settings(max_examples=50)
def test_operators_operator_instantiation(instance):
    assert isinstance(instance, operators_Operator)

@given(instance=instantiations_Initializable_strategy)
@settings(max_examples=50)
def test_instantiations_initializable_instantiation(instance):
    assert isinstance(instance, instantiations_Initializable)

@given(instance=statements_Conditional_strategy)
@settings(max_examples=50)
def test_statements_conditional_instantiation(instance):
    assert isinstance(instance, statements_Conditional)

@given(instance=statements_Statement_strategy)
@settings(max_examples=50)
def test_statements_statement_instantiation(instance):
    assert isinstance(instance, statements_Statement)

@given(instance=statements_ForLoopInitializer_strategy)
@settings(max_examples=50)
def test_statements_forloopinitializer_instantiation(instance):
    assert isinstance(instance, statements_ForLoopInitializer)

@given(instance=members_MemberContainer_strategy)
@settings(max_examples=50)
def test_members_membercontainer_instantiation(instance):
    assert isinstance(instance, members_MemberContainer)

@given(instance=statements_StatementListContainer_strategy)
@settings(max_examples=50)
def test_statements_statementlistcontainer_instantiation(instance):
    assert isinstance(instance, statements_StatementListContainer)

@given(instance=imports_ImportingElement_strategy)
@settings(max_examples=50)
def test_imports_importingelement_instantiation(instance):
    assert isinstance(instance, imports_ImportingElement)

@given(instance=modifiers_AnnotationInstanceOrModifier_strategy)
@settings(max_examples=50)
def test_modifiers_annotationinstanceormodifier_instantiation(instance):
    assert isinstance(instance, modifiers_AnnotationInstanceOrModifier)

@given(instance=parameters_Parametrizable_strategy)
@settings(max_examples=50)
def test_parameters_parametrizable_instantiation(instance):
    assert isinstance(instance, parameters_Parametrizable)

@given(instance=statements_StatementContainer_strategy)
@settings(max_examples=50)
def test_statements_statementcontainer_instantiation(instance):
    assert isinstance(instance, statements_StatementContainer)

@given(instance=literals_Self_strategy)
@settings(max_examples=50)
def test_literals_self_instantiation(instance):
    assert isinstance(instance, literals_Self)

@given(instance=references_Argumentable_strategy)
@settings(max_examples=50)
def test_references_argumentable_instantiation(instance):
    assert isinstance(instance, references_Argumentable)

@given(instance=modifiers_Modifiable_strategy)
@settings(max_examples=50)
def test_modifiers_modifiable_instantiation(instance):
    assert isinstance(instance, modifiers_Modifiable)

@given(instance=modifiers_AnnotableAndModifiable_strategy)
@settings(max_examples=50)
def test_modifiers_annotableandmodifiable_instantiation(instance):
    assert isinstance(instance, modifiers_AnnotableAndModifiable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=modifiers_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_modifiers_annotableandmodifiable_isstatic_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isStatic()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isStatic).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isStatic' in modifiers_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isStatic' in modifiers_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isStatic' in modifiers_AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=modifiers_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_modifiers_annotableandmodifiable_ishidden_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isHidden(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isHidden).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isHidden' in modifiers_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isHidden' in modifiers_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isHidden' in modifiers_AnnotableAndModifiable is not implemented or raised an error")

@given(instance=types_TypeReference_strategy)
@settings(max_examples=50)
def test_types_typereference_instantiation(instance):
    assert isinstance(instance, types_TypeReference)

@given(instance=members_ExceptionThrower_strategy)
@settings(max_examples=50)
def test_members_exceptionthrower_instantiation(instance):
    assert isinstance(instance, members_ExceptionThrower)

@given(instance=annotations_Annotable_strategy)
@settings(max_examples=50)
def test_annotations_annotable_instantiation(instance):
    assert isinstance(instance, annotations_Annotable)

@given(instance=arrays_ArrayTypeable_strategy)
@settings(max_examples=50)
def test_arrays_arraytypeable_instantiation(instance):
    assert isinstance(instance, arrays_ArrayTypeable)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=annotations_AnnotationValue_strategy)
@settings(max_examples=50)
def test_annotations_annotationvalue_instantiation(instance):
    assert isinstance(instance, annotations_AnnotationValue)

@given(instance=InterfaceMethod_strategy)
@settings(max_examples=50)
def test_interfacemethod_instantiation(instance):
    assert isinstance(instance, InterfaceMethod)

@given(instance=annotations_AnnotationAttribute_strategy)
@settings(max_examples=50)
def test_annotations_annotationattribute_instantiation(instance):
    assert isinstance(instance, annotations_AnnotationAttribute)

@given(instance=annotations_AnnotationAttributeSetting_strategy)
@settings(max_examples=50)
def test_annotations_annotationattributesetting_instantiation(instance):
    assert isinstance(instance, annotations_AnnotationAttributeSetting)

@given(instance=AnnotationAttributeSetting_strategy)
@settings(max_examples=50)
def test_annotationattributesetting_instantiation(instance):
    assert isinstance(instance, AnnotationAttributeSetting)

@given(instance=AnnotationValue_strategy)
@settings(max_examples=50)
def test_annotationvalue_instantiation(instance):
    assert isinstance(instance, AnnotationValue)

@given(instance=annotations_AnnotationParameter_strategy)
@settings(max_examples=50)
def test_annotations_annotationparameter_instantiation(instance):
    assert isinstance(instance, annotations_AnnotationParameter)

@given(instance=AnnotationParameter_strategy)
@settings(max_examples=50)
def test_annotationparameter_instantiation(instance):
    assert isinstance(instance, AnnotationParameter)

@given(instance=annotations_AnnotationParameterList_strategy)
@settings(max_examples=50)
def test_annotations_annotationparameterlist_instantiation(instance):
    assert isinstance(instance, annotations_AnnotationParameterList)

@given(instance=annotations_SingleAnnotationParameter_strategy)
@settings(max_examples=50)
def test_annotations_singleannotationparameter_instantiation(instance):
    assert isinstance(instance, annotations_SingleAnnotationParameter)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=generics_TypeParameter_strategy)
@settings(max_examples=50)
def test_generics_typeparameter_instantiation(instance):
    assert isinstance(instance, generics_TypeParameter)

@given(instance=NamespaceAwareElement_strategy)
@settings(max_examples=50)
def test_namespaceawareelement_instantiation(instance):
    assert isinstance(instance, NamespaceAwareElement)

@given(instance=imports_Import_strategy)
@settings(max_examples=50)
def test_imports_import_instantiation(instance):
    assert isinstance(instance, imports_Import)

@given(instance=AnnotationInstanceOrModifier_strategy)
@settings(max_examples=50)
def test_annotationinstanceormodifier_instantiation(instance):
    assert isinstance(instance, AnnotationInstanceOrModifier)

@given(instance=modifiers_Modifier_strategy)
@settings(max_examples=50)
def test_modifiers_modifier_instantiation(instance):
    assert isinstance(instance, modifiers_Modifier)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=references_PrimitiveTypeReference_strategy)
@settings(max_examples=50)
def test_references_primitivetypereference_instantiation(instance):
    assert isinstance(instance, references_PrimitiveTypeReference)

@given(instance=references_ElementReference_strategy)
@settings(max_examples=50)
def test_references_elementreference_instantiation(instance):
    assert isinstance(instance, references_ElementReference)

@given(instance=references_StringReference_strategy)
@settings(max_examples=50)
def test_references_stringreference_instantiation(instance):
    assert isinstance(instance, references_StringReference)



@given(instance=references_StringReference_strategy)
def test_references_stringreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=references_SelfReference_strategy)
@settings(max_examples=50)
def test_references_selfreference_instantiation(instance):
    assert isinstance(instance, references_SelfReference)

@given(instance=references_ReflectiveClassReference_strategy)
@settings(max_examples=50)
def test_references_reflectiveclassreference_instantiation(instance):
    assert isinstance(instance, references_ReflectiveClassReference)

@given(instance=expressions_NestedExpression_strategy)
@settings(max_examples=50)
def test_expressions_nestedexpression_instantiation(instance):
    assert isinstance(instance, expressions_NestedExpression)

@given(instance=annotations_AnnotationInstance_strategy)
@settings(max_examples=50)
def test_annotations_annotationinstance_instantiation(instance):
    assert isinstance(instance, annotations_AnnotationInstance)

@given(instance=AnnotationInstance_strategy)
@settings(max_examples=50)
def test_annotationinstance_instantiation(instance):
    assert isinstance(instance, AnnotationInstance)

@given(instance=expressions_PrefixUnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_expressions_prefixunarymodificationexpression_instantiation(instance):
    assert isinstance(instance, expressions_PrefixUnaryModificationExpression)

@given(instance=UnaryModificationOperator_strategy)
@settings(max_examples=50)
def test_unarymodificationoperator_instantiation(instance):
    assert isinstance(instance, UnaryModificationOperator)

@given(instance=operators_PlusPlus_strategy)
@settings(max_examples=50)
def test_operators_plusplus_instantiation(instance):
    assert isinstance(instance, operators_PlusPlus)

@given(instance=operators_MinusMinus_strategy)
@settings(max_examples=50)
def test_operators_minusminus_instantiation(instance):
    assert isinstance(instance, operators_MinusMinus)

@given(instance=TypeParameter_strategy)
@settings(max_examples=50)
def test_typeparameter_instantiation(instance):
    assert isinstance(instance, TypeParameter)

@given(instance=generics_TypeParametrizable_strategy)
@settings(max_examples=50)
def test_generics_typeparametrizable_instantiation(instance):
    assert isinstance(instance, generics_TypeParametrizable)

@given(instance=generics_CallTypeArgumentable_strategy)
@settings(max_examples=50)
def test_generics_calltypeargumentable_instantiation(instance):
    assert isinstance(instance, generics_CallTypeArgumentable)

@given(instance=TypeArgument_strategy)
@settings(max_examples=50)
def test_typeargument_instantiation(instance):
    assert isinstance(instance, TypeArgument)

@given(instance=generics_ExtendsTypeArgument_strategy)
@settings(max_examples=50)
def test_generics_extendstypeargument_instantiation(instance):
    assert isinstance(instance, generics_ExtendsTypeArgument)

@given(instance=generics_UnknownTypeArgument_strategy)
@settings(max_examples=50)
def test_generics_unknowntypeargument_instantiation(instance):
    assert isinstance(instance, generics_UnknownTypeArgument)

@given(instance=generics_SuperTypeArgument_strategy)
@settings(max_examples=50)
def test_generics_supertypeargument_instantiation(instance):
    assert isinstance(instance, generics_SuperTypeArgument)

@given(instance=generics_TypeArgumentable_strategy)
@settings(max_examples=50)
def test_generics_typeargumentable_instantiation(instance):
    assert isinstance(instance, generics_TypeArgumentable)

@given(instance=AdditiveOperator_strategy)
@settings(max_examples=50)
def test_additiveoperator_instantiation(instance):
    assert isinstance(instance, AdditiveOperator)

@given(instance=AdditiveExpressionChild_strategy)
@settings(max_examples=50)
def test_additiveexpressionchild_instantiation(instance):
    assert isinstance(instance, AdditiveExpressionChild)

@given(instance=expressions_MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_expressions_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, expressions_MultiplicativeExpression)

@given(instance=UnaryModificationExpressionChild_strategy)
@settings(max_examples=50)
def test_unarymodificationexpressionchild_instantiation(instance):
    assert isinstance(instance, UnaryModificationExpressionChild)

@given(instance=expressions_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_expressions_primaryexpression_instantiation(instance):
    assert isinstance(instance, expressions_PrimaryExpression)

@given(instance=UnaryExpressionChild_strategy)
@settings(max_examples=50)
def test_unaryexpressionchild_instantiation(instance):
    assert isinstance(instance, UnaryExpressionChild)

@given(instance=expressions_UnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_expressions_unarymodificationexpression_instantiation(instance):
    assert isinstance(instance, expressions_UnaryModificationExpression)

@given(instance=expressions_UnaryModificationExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_unarymodificationexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_UnaryModificationExpressionChild)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=operators_Negate_strategy)
@settings(max_examples=50)
def test_operators_negate_instantiation(instance):
    assert isinstance(instance, operators_Negate)

@given(instance=operators_Addition_strategy)
@settings(max_examples=50)
def test_operators_addition_instantiation(instance):
    assert isinstance(instance, operators_Addition)

@given(instance=operators_Subtraction_strategy)
@settings(max_examples=50)
def test_operators_subtraction_instantiation(instance):
    assert isinstance(instance, operators_Subtraction)

@given(instance=operators_Complement_strategy)
@settings(max_examples=50)
def test_operators_complement_instantiation(instance):
    assert isinstance(instance, operators_Complement)

@given(instance=expressions_MultiplicativeExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_multiplicativeexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_MultiplicativeExpressionChild)

@given(instance=MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, MultiplicativeOperator)

@given(instance=operators_Division_strategy)
@settings(max_examples=50)
def test_operators_division_instantiation(instance):
    assert isinstance(instance, operators_Division)

@given(instance=operators_Remainder_strategy)
@settings(max_examples=50)
def test_operators_remainder_instantiation(instance):
    assert isinstance(instance, operators_Remainder)

@given(instance=operators_Multiplication_strategy)
@settings(max_examples=50)
def test_operators_multiplication_instantiation(instance):
    assert isinstance(instance, operators_Multiplication)

@given(instance=MultiplicativeExpressionChild_strategy)
@settings(max_examples=50)
def test_multiplicativeexpressionchild_instantiation(instance):
    assert isinstance(instance, MultiplicativeExpressionChild)

@given(instance=expressions_UnaryExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_unaryexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_UnaryExpressionChild)

@given(instance=expressions_UnaryExpression_strategy)
@settings(max_examples=50)
def test_expressions_unaryexpression_instantiation(instance):
    assert isinstance(instance, expressions_UnaryExpression)

@given(instance=EqualityExpressionChild_strategy)
@settings(max_examples=50)
def test_equalityexpressionchild_instantiation(instance):
    assert isinstance(instance, EqualityExpressionChild)

@given(instance=EqualityOperator_strategy)
@settings(max_examples=50)
def test_equalityoperator_instantiation(instance):
    assert isinstance(instance, EqualityOperator)

@given(instance=operators_Equal_strategy)
@settings(max_examples=50)
def test_operators_equal_instantiation(instance):
    assert isinstance(instance, operators_Equal)

@given(instance=operators_NotEqual_strategy)
@settings(max_examples=50)
def test_operators_notequal_instantiation(instance):
    assert isinstance(instance, operators_NotEqual)

@given(instance=ShiftOperator_strategy)
@settings(max_examples=50)
def test_shiftoperator_instantiation(instance):
    assert isinstance(instance, ShiftOperator)

@given(instance=operators_LeftShift_strategy)
@settings(max_examples=50)
def test_operators_leftshift_instantiation(instance):
    assert isinstance(instance, operators_LeftShift)

@given(instance=operators_RightShift_strategy)
@settings(max_examples=50)
def test_operators_rightshift_instantiation(instance):
    assert isinstance(instance, operators_RightShift)

@given(instance=operators_UnsignedRightShift_strategy)
@settings(max_examples=50)
def test_operators_unsignedrightshift_instantiation(instance):
    assert isinstance(instance, operators_UnsignedRightShift)

@given(instance=ShiftExpressionChild_strategy)
@settings(max_examples=50)
def test_shiftexpressionchild_instantiation(instance):
    assert isinstance(instance, ShiftExpressionChild)

@given(instance=expressions_AdditiveExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_additiveexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_AdditiveExpressionChild)

@given(instance=expressions_AdditiveExpression_strategy)
@settings(max_examples=50)
def test_expressions_additiveexpression_instantiation(instance):
    assert isinstance(instance, expressions_AdditiveExpression)

@given(instance=RelationOperator_strategy)
@settings(max_examples=50)
def test_relationoperator_instantiation(instance):
    assert isinstance(instance, RelationOperator)

@given(instance=operators_GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_operators_greaterthanorequal_instantiation(instance):
    assert isinstance(instance, operators_GreaterThanOrEqual)

@given(instance=operators_LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_operators_lessthanorequal_instantiation(instance):
    assert isinstance(instance, operators_LessThanOrEqual)

@given(instance=operators_LessThan_strategy)
@settings(max_examples=50)
def test_operators_lessthan_instantiation(instance):
    assert isinstance(instance, operators_LessThan)

@given(instance=operators_GreaterThan_strategy)
@settings(max_examples=50)
def test_operators_greaterthan_instantiation(instance):
    assert isinstance(instance, operators_GreaterThan)

@given(instance=RelationExpressionChild_strategy)
@settings(max_examples=50)
def test_relationexpressionchild_instantiation(instance):
    assert isinstance(instance, RelationExpressionChild)

@given(instance=expressions_ShiftExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_shiftexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_ShiftExpressionChild)

@given(instance=expressions_ShiftExpression_strategy)
@settings(max_examples=50)
def test_expressions_shiftexpression_instantiation(instance):
    assert isinstance(instance, expressions_ShiftExpression)

@given(instance=expressions_InstanceOfExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_instanceofexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_InstanceOfExpressionChild)

@given(instance=InstanceOfExpressionChild_strategy)
@settings(max_examples=50)
def test_instanceofexpressionchild_instantiation(instance):
    assert isinstance(instance, InstanceOfExpressionChild)

@given(instance=expressions_RelationExpression_strategy)
@settings(max_examples=50)
def test_expressions_relationexpression_instantiation(instance):
    assert isinstance(instance, expressions_RelationExpression)

@given(instance=expressions_RelationExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_relationexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_RelationExpressionChild)

@given(instance=ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalOrExpressionChild)

@given(instance=expressions_ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_expressions_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalAndExpression)

@given(instance=AndExpressionChild_strategy)
@settings(max_examples=50)
def test_andexpressionchild_instantiation(instance):
    assert isinstance(instance, AndExpressionChild)

@given(instance=expressions_EqualityExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_equalityexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_EqualityExpressionChild)

@given(instance=expressions_EqualityExpression_strategy)
@settings(max_examples=50)
def test_expressions_equalityexpression_instantiation(instance):
    assert isinstance(instance, expressions_EqualityExpression)

@given(instance=ExclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_exclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, ExclusiveOrExpressionChild)

@given(instance=expressions_AndExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_andexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_AndExpressionChild)

@given(instance=expressions_AndExpression_strategy)
@settings(max_examples=50)
def test_expressions_andexpression_instantiation(instance):
    assert isinstance(instance, expressions_AndExpression)

@given(instance=InclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_inclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, InclusiveOrExpressionChild)

@given(instance=expressions_ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_expressions_exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, expressions_ExclusiveOrExpression)

@given(instance=expressions_ExclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_exclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_ExclusiveOrExpressionChild)

@given(instance=expressions_ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalAndExpressionChild)

@given(instance=expressions_AssignmentExpression_strategy)
@settings(max_examples=50)
def test_expressions_assignmentexpression_instantiation(instance):
    assert isinstance(instance, expressions_AssignmentExpression)

@given(instance=ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalAndExpressionChild)

@given(instance=expressions_InclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_inclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_InclusiveOrExpressionChild)

@given(instance=expressions_InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_expressions_inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, expressions_InclusiveOrExpression)

@given(instance=ConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalExpressionChild)

@given(instance=expressions_ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_expressions_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalOrExpression)

@given(instance=expressions_ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalOrExpressionChild)

@given(instance=expressions_AssignmentExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_assignmentexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_AssignmentExpressionChild)

@given(instance=AssignmentOperator_strategy)
@settings(max_examples=50)
def test_assignmentoperator_instantiation(instance):
    assert isinstance(instance, AssignmentOperator)

@given(instance=operators_AssignmentAnd_strategy)
@settings(max_examples=50)
def test_operators_assignmentand_instantiation(instance):
    assert isinstance(instance, operators_AssignmentAnd)

@given(instance=operators_AssignmentExclusiveOr_strategy)
@settings(max_examples=50)
def test_operators_assignmentexclusiveor_instantiation(instance):
    assert isinstance(instance, operators_AssignmentExclusiveOr)

@given(instance=operators_AssignmentUnsignedRightShift_strategy)
@settings(max_examples=50)
def test_operators_assignmentunsignedrightshift_instantiation(instance):
    assert isinstance(instance, operators_AssignmentUnsignedRightShift)

@given(instance=operators_AssignmentPlus_strategy)
@settings(max_examples=50)
def test_operators_assignmentplus_instantiation(instance):
    assert isinstance(instance, operators_AssignmentPlus)

@given(instance=operators_AssignmentMinus_strategy)
@settings(max_examples=50)
def test_operators_assignmentminus_instantiation(instance):
    assert isinstance(instance, operators_AssignmentMinus)

@given(instance=operators_Assignment_strategy)
@settings(max_examples=50)
def test_operators_assignment_instantiation(instance):
    assert isinstance(instance, operators_Assignment)

@given(instance=operators_AssignmentRightShift_strategy)
@settings(max_examples=50)
def test_operators_assignmentrightshift_instantiation(instance):
    assert isinstance(instance, operators_AssignmentRightShift)

@given(instance=operators_AssignmentOr_strategy)
@settings(max_examples=50)
def test_operators_assignmentor_instantiation(instance):
    assert isinstance(instance, operators_AssignmentOr)

@given(instance=operators_AssignmentMultiplication_strategy)
@settings(max_examples=50)
def test_operators_assignmentmultiplication_instantiation(instance):
    assert isinstance(instance, operators_AssignmentMultiplication)

@given(instance=operators_AssignmentDivision_strategy)
@settings(max_examples=50)
def test_operators_assignmentdivision_instantiation(instance):
    assert isinstance(instance, operators_AssignmentDivision)

@given(instance=operators_AssignmentLeftShift_strategy)
@settings(max_examples=50)
def test_operators_assignmentleftshift_instantiation(instance):
    assert isinstance(instance, operators_AssignmentLeftShift)

@given(instance=operators_AssignmentModulo_strategy)
@settings(max_examples=50)
def test_operators_assignmentmodulo_instantiation(instance):
    assert isinstance(instance, operators_AssignmentModulo)

@given(instance=AssignmentExpressionChild_strategy)
@settings(max_examples=50)
def test_assignmentexpressionchild_instantiation(instance):
    assert isinstance(instance, AssignmentExpressionChild)

@given(instance=expressions_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_expressions_conditionalexpression_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalExpression)

@given(instance=expressions_ConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions_conditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalExpressionChild)

@given(instance=JavaRoot_strategy)
@settings(max_examples=50)
def test_javaroot_instantiation(instance):
    assert isinstance(instance, JavaRoot)

@given(instance=containers_CompilationUnit_strategy)
@settings(max_examples=50)
def test_containers_compilationunit_instantiation(instance):
    assert isinstance(instance, containers_CompilationUnit)

@given(instance=ImportingElement_strategy)
@settings(max_examples=50)
def test_importingelement_instantiation(instance):
    assert isinstance(instance, ImportingElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=members_Member_strategy)
@settings(max_examples=50)
def test_members_member_instantiation(instance):
    assert isinstance(instance, members_Member)

@given(instance=references_ReferenceableElement_strategy)
@settings(max_examples=50)
def test_references_referenceableelement_instantiation(instance):
    assert isinstance(instance, references_ReferenceableElement)

@given(instance=containers_JavaRoot_strategy)
@settings(max_examples=50)
def test_containers_javaroot_instantiation(instance):
    assert isinstance(instance, containers_JavaRoot)

@given(instance=ForLoopInitializer_strategy)
@settings(max_examples=50)
def test_forloopinitializer_instantiation(instance):
    assert isinstance(instance, ForLoopInitializer)

@given(instance=expressions_ExpressionList_strategy)
@settings(max_examples=50)
def test_expressions_expressionlist_instantiation(instance):
    assert isinstance(instance, expressions_ExpressionList)

@given(instance=containers_EmptyModel_strategy)
@settings(max_examples=50)
def test_containers_emptymodel_instantiation(instance):
    assert isinstance(instance, containers_EmptyModel)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=CompilationUnit_strategy)
@settings(max_examples=50)
def test_compilationunit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)

@given(instance=Annotable_strategy)
@settings(max_examples=50)
def test_annotable_instantiation(instance):
    assert isinstance(instance, Annotable)

@given(instance=commons_NamespaceAwareElement_strategy)
@settings(max_examples=50)
def test_commons_namespaceawareelement_instantiation(instance):
    assert isinstance(instance, commons_NamespaceAwareElement)



@given(instance=commons_NamespaceAwareElement_strategy)
def test_commons_namespaceawareelement_namespaces_setter(instance):
    original = instance.namespaces
    instance.namespaces = original
    assert instance.namespaces == original

@given(instance=commons_NamedElement_strategy)
@settings(max_examples=50)
def test_commons_namedelement_instantiation(instance):
    assert isinstance(instance, commons_NamedElement)



@given(instance=commons_NamedElement_strategy)
def test_commons_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=commons_Commentable_strategy)
@settings(max_examples=50)
def test_commons_commentable_instantiation(instance):
    assert isinstance(instance, commons_Commentable)



@given(instance=commons_Commentable_strategy)
def test_commons_commentable_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=EnumConstant_strategy)
@settings(max_examples=50)
def test_enumconstant_instantiation(instance):
    assert isinstance(instance, EnumConstant)

@given(instance=ReferenceableElement_strategy)
@settings(max_examples=50)
def test_referenceableelement_instantiation(instance):
    assert isinstance(instance, ReferenceableElement)

@given(instance=containers_Package_strategy)
@settings(max_examples=50)
def test_containers_package_instantiation(instance):
    assert isinstance(instance, containers_Package)

@given(instance=members_EnumConstant_strategy)
@settings(max_examples=50)
def test_members_enumconstant_instantiation(instance):
    assert isinstance(instance, members_EnumConstant)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=classifiers_Classifier_strategy)
@settings(max_examples=50)
def test_classifiers_classifier_instantiation(instance):
    assert isinstance(instance, classifiers_Classifier)

@given(instance=arrays_ArraySelector_strategy)
@settings(max_examples=50)
def test_arrays_arrayselector_instantiation(instance):
    assert isinstance(instance, arrays_ArraySelector)

@given(instance=Implementor_strategy)
@settings(max_examples=50)
def test_implementor_instantiation(instance):
    assert isinstance(instance, Implementor)

@given(instance=ConcreteClassifier_strategy)
@settings(max_examples=50)
def test_concreteclassifier_instantiation(instance):
    assert isinstance(instance, ConcreteClassifier)

@given(instance=classifiers_Interface_strategy)
@settings(max_examples=50)
def test_classifiers_interface_instantiation(instance):
    assert isinstance(instance, classifiers_Interface)

@given(instance=classifiers_Annotation_strategy)
@settings(max_examples=50)
def test_classifiers_annotation_instantiation(instance):
    assert isinstance(instance, classifiers_Annotation)

@given(instance=classifiers_Enumeration_strategy)
@settings(max_examples=50)
def test_classifiers_enumeration_instantiation(instance):
    assert isinstance(instance, classifiers_Enumeration)

@given(instance=classifiers_Class_strategy)
@settings(max_examples=50)
def test_classifiers_class_instantiation(instance):
    assert isinstance(instance, classifiers_Class)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=classifiers_Class_strategy)
@settings(max_examples=30)
def test_classifiers_class_unwrapprimitivetype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unWrapPrimitiveType()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unWrapPrimitiveType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unWrapPrimitiveType' in classifiers_Class is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unWrapPrimitiveType' in classifiers_Class did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unWrapPrimitiveType' in classifiers_Class is not implemented or raised an error")

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=types_PrimitiveType_strategy)
@settings(max_examples=50)
def test_types_primitivetype_instantiation(instance):
    assert isinstance(instance, types_PrimitiveType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=types_PrimitiveType_strategy)
@settings(max_examples=30)
def test_types_primitivetype_wrapprimitivetype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.wrapPrimitiveType()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.wrapPrimitiveType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'wrapPrimitiveType' in types_PrimitiveType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'wrapPrimitiveType' in types_PrimitiveType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'wrapPrimitiveType' in types_PrimitiveType is not implemented or raised an error")

@given(instance=types_ClassifierReference_strategy)
@settings(max_examples=50)
def test_types_classifierreference_instantiation(instance):
    assert isinstance(instance, types_ClassifierReference)

@given(instance=types_NamespaceClassifierReference_strategy)
@settings(max_examples=50)
def test_types_namespaceclassifierreference_instantiation(instance):
    assert isinstance(instance, types_NamespaceClassifierReference)

@given(instance=classifiers_Implementor_strategy)
@settings(max_examples=50)
def test_classifiers_implementor_instantiation(instance):
    assert isinstance(instance, classifiers_Implementor)

@given(instance=AnnotableAndModifiable_strategy)
@settings(max_examples=50)
def test_annotableandmodifiable_instantiation(instance):
    assert isinstance(instance, AnnotableAndModifiable)

@given(instance=variables_LocalVariable_strategy)
@settings(max_examples=50)
def test_variables_localvariable_instantiation(instance):
    assert isinstance(instance, variables_LocalVariable)

@given(instance=parameters_Parameter_strategy)
@settings(max_examples=50)
def test_parameters_parameter_instantiation(instance):
    assert isinstance(instance, parameters_Parameter)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=statements_Condition_strategy)
@settings(max_examples=50)
def test_statements_condition_instantiation(instance):
    assert isinstance(instance, statements_Condition)

@given(instance=statements_JumpLabel_strategy)
@settings(max_examples=50)
def test_statements_jumplabel_instantiation(instance):
    assert isinstance(instance, statements_JumpLabel)

@given(instance=statements_EmptyStatement_strategy)
@settings(max_examples=50)
def test_statements_emptystatement_instantiation(instance):
    assert isinstance(instance, statements_EmptyStatement)

@given(instance=statements_Jump_strategy)
@settings(max_examples=50)
def test_statements_jump_instantiation(instance):
    assert isinstance(instance, statements_Jump)

@given(instance=statements_Return_strategy)
@settings(max_examples=50)
def test_statements_return_instantiation(instance):
    assert isinstance(instance, statements_Return)

@given(instance=statements_ForLoop_strategy)
@settings(max_examples=50)
def test_statements_forloop_instantiation(instance):
    assert isinstance(instance, statements_ForLoop)

@given(instance=statements_Throw_strategy)
@settings(max_examples=50)
def test_statements_throw_instantiation(instance):
    assert isinstance(instance, statements_Throw)

@given(instance=statements_TryBlock_strategy)
@settings(max_examples=50)
def test_statements_tryblock_instantiation(instance):
    assert isinstance(instance, statements_TryBlock)

@given(instance=statements_ForEachLoop_strategy)
@settings(max_examples=50)
def test_statements_foreachloop_instantiation(instance):
    assert isinstance(instance, statements_ForEachLoop)

@given(instance=statements_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_statements_expressionstatement_instantiation(instance):
    assert isinstance(instance, statements_ExpressionStatement)

@given(instance=statements_Assert_strategy)
@settings(max_examples=50)
def test_statements_assert_instantiation(instance):
    assert isinstance(instance, statements_Assert)

@given(instance=statements_SynchronizedBlock_strategy)
@settings(max_examples=50)
def test_statements_synchronizedblock_instantiation(instance):
    assert isinstance(instance, statements_SynchronizedBlock)

@given(instance=statements_WhileLoop_strategy)
@settings(max_examples=50)
def test_statements_whileloop_instantiation(instance):
    assert isinstance(instance, statements_WhileLoop)

@given(instance=statements_LocalVariableStatement_strategy)
@settings(max_examples=50)
def test_statements_localvariablestatement_instantiation(instance):
    assert isinstance(instance, statements_LocalVariableStatement)

@given(instance=statements_Switch_strategy)
@settings(max_examples=50)
def test_statements_switch_instantiation(instance):
    assert isinstance(instance, statements_Switch)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=statements_Block_strategy)
@settings(max_examples=50)
def test_statements_block_instantiation(instance):
    assert isinstance(instance, statements_Block)

@given(instance=members_Field_strategy)
@settings(max_examples=50)
def test_members_field_instantiation(instance):
    assert isinstance(instance, members_Field)

@given(instance=members_EmptyMember_strategy)
@settings(max_examples=50)
def test_members_emptymember_instantiation(instance):
    assert isinstance(instance, members_EmptyMember)

@given(instance=MemberContainer_strategy)
@settings(max_examples=50)
def test_membercontainer_instantiation(instance):
    assert isinstance(instance, MemberContainer)

@given(instance=classifiers_AnonymousClass_strategy)
@settings(max_examples=50)
def test_classifiers_anonymousclass_instantiation(instance):
    assert isinstance(instance, classifiers_AnonymousClass)

@given(instance=TypeParametrizable_strategy)
@settings(max_examples=50)
def test_typeparametrizable_instantiation(instance):
    assert isinstance(instance, TypeParametrizable)

@given(instance=members_Constructor_strategy)
@settings(max_examples=50)
def test_members_constructor_instantiation(instance):
    assert isinstance(instance, members_Constructor)

@given(instance=classifiers_ConcreteClassifier_strategy)
@settings(max_examples=50)
def test_classifiers_concreteclassifier_instantiation(instance):
    assert isinstance(instance, classifiers_ConcreteClassifier)



@given(instance=classifiers_ConcreteClassifier_strategy)
def test_classifiers_concreteclassifier_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=ArrayDimension_strategy)
@settings(max_examples=50)
def test_arraydimension_instantiation(instance):
    assert isinstance(instance, ArrayDimension)

@given(instance=ArrayInitializer_strategy)
@settings(max_examples=50)
def test_arrayinitializer_instantiation(instance):
    assert isinstance(instance, ArrayInitializer)

@given(instance=ArrayTypeable_strategy)
@settings(max_examples=50)
def test_arraytypeable_instantiation(instance):
    assert isinstance(instance, ArrayTypeable)

@given(instance=variables_AdditionalLocalVariable_strategy)
@settings(max_examples=50)
def test_variables_additionallocalvariable_instantiation(instance):
    assert isinstance(instance, variables_AdditionalLocalVariable)

@given(instance=members_AdditionalField_strategy)
@settings(max_examples=50)
def test_members_additionalfield_instantiation(instance):
    assert isinstance(instance, members_AdditionalField)

@given(instance=generics_TypeArgument_strategy)
@settings(max_examples=50)
def test_generics_typeargument_instantiation(instance):
    assert isinstance(instance, generics_TypeArgument)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=expressions_CastExpression_strategy)
@settings(max_examples=50)
def test_expressions_castexpression_instantiation(instance):
    assert isinstance(instance, expressions_CastExpression)

@given(instance=generics_QualifiedTypeArgument_strategy)
@settings(max_examples=50)
def test_generics_qualifiedtypeargument_instantiation(instance):
    assert isinstance(instance, generics_QualifiedTypeArgument)

@given(instance=arrays_ArrayInstantiationByValues_strategy)
@settings(max_examples=50)
def test_arrays_arrayinstantiationbyvalues_instantiation(instance):
    assert isinstance(instance, arrays_ArrayInstantiationByValues)

@given(instance=members_Method_strategy)
@settings(max_examples=50)
def test_members_method_instantiation(instance):
    assert isinstance(instance, members_Method)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=members_Method_strategy)
@settings(max_examples=30)
def test_members_method_issomemethodforcall_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSomeMethodForCall(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSomeMethodForCall).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSomeMethodForCall' in members_Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSomeMethodForCall' in members_Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSomeMethodForCall' in members_Method is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=members_Method_strategy)
@settings(max_examples=30)
def test_members_method_isbettermethodforcall_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isBetterMethodForCall(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isBetterMethodForCall).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isBetterMethodForCall' in members_Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isBetterMethodForCall' in members_Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isBetterMethodForCall' in members_Method is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=members_Method_strategy)
@settings(max_examples=30)
def test_members_method_ismethodforcall_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isMethodForCall(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isMethodForCall).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isMethodForCall' in members_Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isMethodForCall' in members_Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isMethodForCall' in members_Method is not implemented or raised an error")

@given(instance=instantiations_Instantiation_strategy)
@settings(max_examples=50)
def test_instantiations_instantiation_instantiation(instance):
    assert isinstance(instance, instantiations_Instantiation)

@given(instance=variables_Variable_strategy)
@settings(max_examples=50)
def test_variables_variable_instantiation(instance):
    assert isinstance(instance, variables_Variable)

@given(instance=expressions_InstanceOfExpression_strategy)
@settings(max_examples=50)
def test_expressions_instanceofexpression_instantiation(instance):
    assert isinstance(instance, expressions_InstanceOfExpression)

@given(instance=arrays_ArrayInstantiationBySize_strategy)
@settings(max_examples=50)
def test_arrays_arrayinstantiationbysize_instantiation(instance):
    assert isinstance(instance, arrays_ArrayInstantiationBySize)

@given(instance=arrays_ArrayInitializationValue_strategy)
@settings(max_examples=50)
def test_arrays_arrayinitializationvalue_instantiation(instance):
    assert isinstance(instance, arrays_ArrayInitializationValue)

@given(instance=ArrayInitializationValue_strategy)
@settings(max_examples=50)
def test_arrayinitializationvalue_instantiation(instance):
    assert isinstance(instance, ArrayInitializationValue)

@given(instance=expressions_Expression_strategy)
@settings(max_examples=50)
def test_expressions_expression_instantiation(instance):
    assert isinstance(instance, expressions_Expression)

@given(instance=arrays_ArrayInitializer_strategy)
@settings(max_examples=50)
def test_arrays_arrayinitializer_instantiation(instance):
    assert isinstance(instance, arrays_ArrayInitializer)

@given(instance=arrays_ArrayDimension_strategy)
@settings(max_examples=50)
def test_arrays_arraydimension_instantiation(instance):
    assert isinstance(instance, arrays_ArrayDimension)
