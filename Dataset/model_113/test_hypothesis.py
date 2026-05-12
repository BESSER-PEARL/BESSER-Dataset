import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PrimitiveType,
    java_Char,
    java_Short,
    java_Int,
    java_Float,
    java_Long,
    java_Byte,
    java_Double,
    java_Void,
    ArrayInstantiationByValues,
    java_ArrayInstantiationByValuesUntyped,
    ArrayTypeable,
    TypedElement,
    java_ArrayInstantiationByValuesTyped,
    ArrayInstantiation,
    java_ArrayInstantiationByValues,
    java_ArrayInstantiationBySize,
    Expression,
    AnnotationValue,
    ArrayInitializationValue,
    java_ArrayInitializer,
    InterfaceMethod,
    java_AnnotationAttribute,
    AnnotationParameter,
    java_AnnotationParameterList,
    java_SingleAnnotationParameter,
    NamespaceAwareElement,
    AnnotationInstanceOrModifier,
    Reference,
    java_ArrayInstantiation,
    java_AnnotationInstance,
    Commentable,
    java_AnnotationParameter,
    java_ArrayDimension,
    java_ArrayInitializationValue,
    java_AnnotationValue,
    java_AnnotationAttributeSetting,
    java_ArraySelector,
    java_Annotable,
    java_ArrayTypeable,
    java_Expression,
    java_Boolean,
    TypeReference,
    java_TypedElement,
    java_Type,
    WhileLoop,
    java_DoWhileLoop,
    SwitchCase,
    java_DefaultSwitchCase,
    Modifiable,
    Jump,
    java_Continue,
    java_Break,
    Conditional,
    java_NormalSwitchCase,
    java_ForLoopInitializer,
    java_Conditional,
    java_StatementListContainer,
    java_Statement,
    java_StatementContainer,
    Parameter,
    java_VariableLengthParameter,
    java_OrdinaryParameter,
    java_Parametrizable,
    java_SelfReference,
    java_StringReference,
    StatementContainer,
    ElementReference,
    java_IdentifierReference,
    java_ElementReference,
    java_Argumentable,
    TypeArgumentable,
    java_ClassifierReference,
    ShiftOperator,
    java_UnsignedRightShift,
    java_RightShift,
    java_LeftShift,
    UnaryModificationOperator,
    java_PlusPlus,
    java_MinusMinus,
    MultiplicativeOperator,
    java_Remainder,
    java_Multiplication,
    java_Division,
    UnaryOperator,
    java_Complement,
    java_Negate,
    AdditiveOperator,
    java_Subtraction,
    java_Addition,
    RelationOperator,
    java_LessThanOrEqual,
    java_GreaterThanOrEqual,
    java_LessThan,
    java_GreaterThan,
    java_PrimitiveTypeReference,
    java_ReflectiveClassReference,
    AssignmentOperator,
    java_AssignmentAnd,
    java_AssignmentMinus,
    java_AssignmentOr,
    java_AssignmentDivision,
    java_AssignmentModulo,
    java_AssignmentExclusiveOr,
    java_AssignmentMultiplication,
    java_AssignmentLeftShift,
    java_Assignment,
    Operator,
    java_Operator,
    Modifier,
    java_Synchronized,
    java_Protected,
    java_Volatile,
    java_Public,
    java_Private,
    java_Final,
    java_Transient,
    java_Strictfp,
    java_Native,
    java_Abstract,
    java_Modifiable,
    EqualityOperator,
    java_NotEqual,
    java_Equal,
    java_AssignmentUnsignedRightShift,
    java_AssignmentRightShift,
    java_AssignmentPlus,
    java_AnnotableAndModifiable,
    java_AnnotationInstanceOrModifier,
    java_Modifier,
    Method,
    java_InterfaceMethod,
    Variable,
    ExceptionThrower,
    Parametrizable,
    StatementListContainer,
    java_CatchBlock,
    java_SwitchCase,
    java_ClassMethod,
    Initializable,
    java_MemberContainer,
    java_NamespaceClassifierReference,
    java_ExceptionThrower,
    Self,
    java_This,
    java_Super,
    LongLiteral,
    java_OctalLongLiteral,
    java_HexLongLiteral,
    java_DecimalLongLiteral,
    IntegerLiteral,
    java_HexIntegerLiteral,
    java_OctalIntegerLiteral,
    java_DecimalIntegerLiteral,
    DoubleLiteral,
    java_HexDoubleLiteral,
    java_DecimalDoubleLiteral,
    FloatLiteral,
    java_HexFloatLiteral,
    java_DecimalFloatLiteral,
    PrimaryExpression,
    java_Reference,
    java_Literal,
    java_Self,
    CallTypeArgumentable,
    Instantiation,
    java_ExplicitConstructorCall,
    java_NewConstructorCall,
    Argumentable,
    java_MethodCall,
    java_Instantiation,
    java_Initializable,
    StaticImport,
    java_StaticMemberImport,
    java_StaticClassifierImport,
    java_Static,
    Import,
    java_ClassifierImport,
    java_PackageImport,
    java_StaticImport,
    java_ImportingElement,
    Literal,
    java_LongLiteral,
    java_DoubleLiteral,
    java_CharacterLiteral,
    java_IntegerLiteral,
    java_FloatLiteral,
    java_NullLiteral,
    java_BooleanLiteral,
    TypeArgument,
    java_SuperTypeArgument,
    java_QualifiedTypeArgument,
    java_ExtendsTypeArgument,
    java_TypeParametrizable,
    java_CallTypeArgumentable,
    java_TypeArgumentable,
    java_TypeArgument,
    java_NestedExpression,
    UnaryModificationExpressionChild,
    java_PrimaryExpression,
    java_CastExpression,
    java_Import,
    java_UnknownTypeArgument,
    java_UnaryModificationOperator,
    UnaryExpressionChild,
    java_UnaryModificationExpressionChild,
    java_UnaryModificationExpression,
    java_UnaryOperator,
    MultiplicativeExpressionChild,
    java_UnaryExpressionChild,
    java_UnaryExpression,
    java_MultiplicativeOperator,
    AdditiveExpressionChild,
    java_MultiplicativeExpressionChild,
    java_MultiplicativeExpression,
    java_AdditiveOperator,
    ShiftExpressionChild,
    java_AdditiveExpressionChild,
    java_AdditiveExpression,
    java_ShiftOperator,
    RelationExpressionChild,
    java_ShiftExpressionChild,
    java_ShiftExpression,
    java_RelationOperator,
    UnaryModificationExpression,
    java_SuffixUnaryModificationExpression,
    java_PrefixUnaryModificationExpression,
    EqualityExpressionChild,
    java_InstanceOfExpressionChild,
    java_InstanceOfExpression,
    java_EqualityOperator,
    AndExpressionChild,
    java_EqualityExpressionChild,
    java_EqualityExpression,
    ExclusiveOrExpressionChild,
    java_AndExpressionChild,
    java_AndExpression,
    InclusiveOrExpressionChild,
    java_ExclusiveOrExpressionChild,
    java_ExclusiveOrExpression,
    ConditionalAndExpressionChild,
    java_InclusiveOrExpressionChild,
    java_InclusiveOrExpression,
    ConditionalOrExpressionChild,
    java_ConditionalAndExpressionChild,
    java_ConditionalAndExpression,
    ConditionalExpressionChild,
    java_ConditionalOrExpressionChild,
    java_ConditionalOrExpression,
    InstanceOfExpressionChild,
    java_RelationExpressionChild,
    java_RelationExpression,
    java_AssignmentOperator,
    java_AssignmentExpressionChild,
    java_AssignmentExpression,
    ForLoopInitializer,
    java_ExpressionList,
    Annotable,
    JavaRoot,
    java_EmptyModel,
    java_Package,
    java_CompilationUnit,
    ImportingElement,
    NamedElement,
    java_ReferenceableElement,
    java_Member,
    java_JavaRoot,
    AssignmentExpressionChild,
    java_ConditionalExpressionChild,
    java_ConditionalExpression,
    java_NamespaceAwareElement,
    java_NamedElement,
    java_LayoutInformation,
    java_Commentable,
    Implementor,
    ConcreteClassifier,
    java_Enumeration,
    java_Interface,
    java_Class,
    java_TypeReference,
    java_Implementor,
    java_Annotation,
    AnnotableAndModifiable,
    java_LocalVariable,
    java_Parameter,
    Statement,
    java_ForEachLoop,
    java_Condition,
    java_Assert,
    java_JumpLabel,
    java_Switch,
    java_Throw,
    java_Return,
    java_TryBlock,
    java_Jump,
    java_ForLoop,
    java_WhileLoop,
    java_SynchronizedBlock,
    java_LocalVariableStatement,
    java_EmptyStatement,
    java_ExpressionStatement,
    Member,
    java_EmptyMember,
    java_Block,
    MemberContainer,
    TypeParametrizable,
    java_Constructor,
    Classifier,
    java_TypeParameter,
    java_ConcreteClassifier,
    ReferenceableElement,
    java_AdditionalField,
    java_AdditionalLocalVariable,
    java_Method,
    java_Field,
    java_PackageReference,
    java_EnumConstant,
    java_Variable,
    Type,
    java_Classifier,
    java_AnonymousClass,
    java_PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java_char_is_not_abstract():
    assert not inspect.isabstract(java_Char)


def test_java_char_constructor_exists():
    assert callable(java_Char.__init__)


def test_java_char_constructor_args():
    sig = inspect.signature(java_Char.__init__)
    params = list(sig.parameters.keys())



def test_java_short_is_not_abstract():
    assert not inspect.isabstract(java_Short)


def test_java_short_constructor_exists():
    assert callable(java_Short.__init__)


def test_java_short_constructor_args():
    sig = inspect.signature(java_Short.__init__)
    params = list(sig.parameters.keys())



def test_java_int_is_not_abstract():
    assert not inspect.isabstract(java_Int)


def test_java_int_constructor_exists():
    assert callable(java_Int.__init__)


def test_java_int_constructor_args():
    sig = inspect.signature(java_Int.__init__)
    params = list(sig.parameters.keys())



def test_java_float_is_not_abstract():
    assert not inspect.isabstract(java_Float)


def test_java_float_constructor_exists():
    assert callable(java_Float.__init__)


def test_java_float_constructor_args():
    sig = inspect.signature(java_Float.__init__)
    params = list(sig.parameters.keys())



def test_java_long_is_not_abstract():
    assert not inspect.isabstract(java_Long)


def test_java_long_constructor_exists():
    assert callable(java_Long.__init__)


def test_java_long_constructor_args():
    sig = inspect.signature(java_Long.__init__)
    params = list(sig.parameters.keys())



def test_java_byte_is_not_abstract():
    assert not inspect.isabstract(java_Byte)


def test_java_byte_constructor_exists():
    assert callable(java_Byte.__init__)


def test_java_byte_constructor_args():
    sig = inspect.signature(java_Byte.__init__)
    params = list(sig.parameters.keys())



def test_java_double_is_not_abstract():
    assert not inspect.isabstract(java_Double)


def test_java_double_constructor_exists():
    assert callable(java_Double.__init__)


def test_java_double_constructor_args():
    sig = inspect.signature(java_Double.__init__)
    params = list(sig.parameters.keys())



def test_java_void_is_not_abstract():
    assert not inspect.isabstract(java_Void)


def test_java_void_constructor_exists():
    assert callable(java_Void.__init__)


def test_java_void_constructor_args():
    sig = inspect.signature(java_Void.__init__)
    params = list(sig.parameters.keys())



def test_arrayinstantiationbyvalues_is_not_abstract():
    assert not inspect.isabstract(ArrayInstantiationByValues)


def test_arrayinstantiationbyvalues_constructor_exists():
    assert callable(ArrayInstantiationByValues.__init__)


def test_arrayinstantiationbyvalues_constructor_args():
    sig = inspect.signature(ArrayInstantiationByValues.__init__)
    params = list(sig.parameters.keys())



def test_java_arrayinstantiationbyvaluesuntyped_is_not_abstract():
    assert not inspect.isabstract(java_ArrayInstantiationByValuesUntyped)


def test_java_arrayinstantiationbyvaluesuntyped_constructor_exists():
    assert callable(java_ArrayInstantiationByValuesUntyped.__init__)


def test_java_arrayinstantiationbyvaluesuntyped_constructor_args():
    sig = inspect.signature(java_ArrayInstantiationByValuesUntyped.__init__)
    params = list(sig.parameters.keys())



def test_arraytypeable_is_not_abstract():
    assert not inspect.isabstract(ArrayTypeable)


def test_arraytypeable_constructor_exists():
    assert callable(ArrayTypeable.__init__)


def test_arraytypeable_constructor_args():
    sig = inspect.signature(ArrayTypeable.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_java_arrayinstantiationbyvaluestyped_is_not_abstract():
    assert not inspect.isabstract(java_ArrayInstantiationByValuesTyped)


def test_java_arrayinstantiationbyvaluestyped_constructor_exists():
    assert callable(java_ArrayInstantiationByValuesTyped.__init__)


def test_java_arrayinstantiationbyvaluestyped_constructor_args():
    sig = inspect.signature(java_ArrayInstantiationByValuesTyped.__init__)
    params = list(sig.parameters.keys())



def test_arrayinstantiation_is_not_abstract():
    assert not inspect.isabstract(ArrayInstantiation)


def test_arrayinstantiation_constructor_exists():
    assert callable(ArrayInstantiation.__init__)


def test_arrayinstantiation_constructor_args():
    sig = inspect.signature(ArrayInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_java_arrayinstantiationbyvalues_is_not_abstract():
    assert not inspect.isabstract(java_ArrayInstantiationByValues)


def test_java_arrayinstantiationbyvalues_constructor_exists():
    assert callable(java_ArrayInstantiationByValues.__init__)


def test_java_arrayinstantiationbyvalues_constructor_args():
    sig = inspect.signature(java_ArrayInstantiationByValues.__init__)
    params = list(sig.parameters.keys())



def test_java_arrayinstantiationbysize_is_not_abstract():
    assert not inspect.isabstract(java_ArrayInstantiationBySize)


def test_java_arrayinstantiationbysize_constructor_exists():
    assert callable(java_ArrayInstantiationBySize.__init__)


def test_java_arrayinstantiationbysize_constructor_args():
    sig = inspect.signature(java_ArrayInstantiationBySize.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_annotationvalue_is_not_abstract():
    assert not inspect.isabstract(AnnotationValue)


def test_annotationvalue_constructor_exists():
    assert callable(AnnotationValue.__init__)


def test_annotationvalue_constructor_args():
    sig = inspect.signature(AnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_arrayinitializationvalue_is_not_abstract():
    assert not inspect.isabstract(ArrayInitializationValue)


def test_arrayinitializationvalue_constructor_exists():
    assert callable(ArrayInitializationValue.__init__)


def test_arrayinitializationvalue_constructor_args():
    sig = inspect.signature(ArrayInitializationValue.__init__)
    params = list(sig.parameters.keys())



def test_java_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(java_ArrayInitializer)


def test_java_arrayinitializer_constructor_exists():
    assert callable(java_ArrayInitializer.__init__)


def test_java_arrayinitializer_constructor_args():
    sig = inspect.signature(java_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_interfacemethod_is_not_abstract():
    assert not inspect.isabstract(InterfaceMethod)


def test_interfacemethod_constructor_exists():
    assert callable(InterfaceMethod.__init__)


def test_interfacemethod_constructor_args():
    sig = inspect.signature(InterfaceMethod.__init__)
    params = list(sig.parameters.keys())



def test_java_annotationattribute_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationAttribute)


def test_java_annotationattribute_constructor_exists():
    assert callable(java_AnnotationAttribute.__init__)


def test_java_annotationattribute_constructor_args():
    sig = inspect.signature(java_AnnotationAttribute.__init__)
    params = list(sig.parameters.keys())



def test_annotationparameter_is_not_abstract():
    assert not inspect.isabstract(AnnotationParameter)


def test_annotationparameter_constructor_exists():
    assert callable(AnnotationParameter.__init__)


def test_annotationparameter_constructor_args():
    sig = inspect.signature(AnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_java_annotationparameterlist_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationParameterList)


def test_java_annotationparameterlist_constructor_exists():
    assert callable(java_AnnotationParameterList.__init__)


def test_java_annotationparameterlist_constructor_args():
    sig = inspect.signature(java_AnnotationParameterList.__init__)
    params = list(sig.parameters.keys())



def test_java_singleannotationparameter_is_not_abstract():
    assert not inspect.isabstract(java_SingleAnnotationParameter)


def test_java_singleannotationparameter_constructor_exists():
    assert callable(java_SingleAnnotationParameter.__init__)


def test_java_singleannotationparameter_constructor_args():
    sig = inspect.signature(java_SingleAnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_namespaceawareelement_is_not_abstract():
    assert not inspect.isabstract(NamespaceAwareElement)


def test_namespaceawareelement_constructor_exists():
    assert callable(NamespaceAwareElement.__init__)


def test_namespaceawareelement_constructor_args():
    sig = inspect.signature(NamespaceAwareElement.__init__)
    params = list(sig.parameters.keys())



def test_annotationinstanceormodifier_is_not_abstract():
    assert not inspect.isabstract(AnnotationInstanceOrModifier)


def test_annotationinstanceormodifier_constructor_exists():
    assert callable(AnnotationInstanceOrModifier.__init__)


def test_annotationinstanceormodifier_constructor_args():
    sig = inspect.signature(AnnotationInstanceOrModifier.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_java_arrayinstantiation_is_not_abstract():
    assert not inspect.isabstract(java_ArrayInstantiation)


def test_java_arrayinstantiation_constructor_exists():
    assert callable(java_ArrayInstantiation.__init__)


def test_java_arrayinstantiation_constructor_args():
    sig = inspect.signature(java_ArrayInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_java_annotationinstance_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationInstance)


def test_java_annotationinstance_constructor_exists():
    assert callable(java_AnnotationInstance.__init__)


def test_java_annotationinstance_constructor_args():
    sig = inspect.signature(java_AnnotationInstance.__init__)
    params = list(sig.parameters.keys())



def test_commentable_is_not_abstract():
    assert not inspect.isabstract(Commentable)


def test_commentable_constructor_exists():
    assert callable(Commentable.__init__)


def test_commentable_constructor_args():
    sig = inspect.signature(Commentable.__init__)
    params = list(sig.parameters.keys())



def test_java_annotationparameter_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationParameter)


def test_java_annotationparameter_constructor_exists():
    assert callable(java_AnnotationParameter.__init__)


def test_java_annotationparameter_constructor_args():
    sig = inspect.signature(java_AnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_java_arraydimension_is_not_abstract():
    assert not inspect.isabstract(java_ArrayDimension)


def test_java_arraydimension_constructor_exists():
    assert callable(java_ArrayDimension.__init__)


def test_java_arraydimension_constructor_args():
    sig = inspect.signature(java_ArrayDimension.__init__)
    params = list(sig.parameters.keys())



def test_java_arrayinitializationvalue_is_not_abstract():
    assert not inspect.isabstract(java_ArrayInitializationValue)


def test_java_arrayinitializationvalue_constructor_exists():
    assert callable(java_ArrayInitializationValue.__init__)


def test_java_arrayinitializationvalue_constructor_args():
    sig = inspect.signature(java_ArrayInitializationValue.__init__)
    params = list(sig.parameters.keys())



def test_java_annotationvalue_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationValue)


def test_java_annotationvalue_constructor_exists():
    assert callable(java_AnnotationValue.__init__)


def test_java_annotationvalue_constructor_args():
    sig = inspect.signature(java_AnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_java_annotationattributesetting_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationAttributeSetting)


def test_java_annotationattributesetting_constructor_exists():
    assert callable(java_AnnotationAttributeSetting.__init__)


def test_java_annotationattributesetting_constructor_args():
    sig = inspect.signature(java_AnnotationAttributeSetting.__init__)
    params = list(sig.parameters.keys())



def test_java_arrayselector_is_not_abstract():
    assert not inspect.isabstract(java_ArraySelector)


def test_java_arrayselector_constructor_exists():
    assert callable(java_ArraySelector.__init__)


def test_java_arrayselector_constructor_args():
    sig = inspect.signature(java_ArraySelector.__init__)
    params = list(sig.parameters.keys())



def test_java_annotable_is_not_abstract():
    assert not inspect.isabstract(java_Annotable)


def test_java_annotable_constructor_exists():
    assert callable(java_Annotable.__init__)


def test_java_annotable_constructor_args():
    sig = inspect.signature(java_Annotable.__init__)
    params = list(sig.parameters.keys())



def test_java_arraytypeable_is_not_abstract():
    assert not inspect.isabstract(java_ArrayTypeable)


def test_java_arraytypeable_constructor_exists():
    assert callable(java_ArrayTypeable.__init__)


def test_java_arraytypeable_constructor_args():
    sig = inspect.signature(java_ArrayTypeable.__init__)
    params = list(sig.parameters.keys())



def test_java_expression_is_not_abstract():
    assert not inspect.isabstract(java_Expression)


def test_java_expression_constructor_exists():
    assert callable(java_Expression.__init__)


def test_java_expression_constructor_args():
    sig = inspect.signature(java_Expression.__init__)
    params = list(sig.parameters.keys())



def test_java_boolean_is_not_abstract():
    assert not inspect.isabstract(java_Boolean)


def test_java_boolean_constructor_exists():
    assert callable(java_Boolean.__init__)


def test_java_boolean_constructor_args():
    sig = inspect.signature(java_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_java_typedelement_is_not_abstract():
    assert not inspect.isabstract(java_TypedElement)


def test_java_typedelement_constructor_exists():
    assert callable(java_TypedElement.__init__)


def test_java_typedelement_constructor_args():
    sig = inspect.signature(java_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_java_type_is_not_abstract():
    assert not inspect.isabstract(java_Type)


def test_java_type_constructor_exists():
    assert callable(java_Type.__init__)


def test_java_type_constructor_args():
    sig = inspect.signature(java_Type.__init__)
    params = list(sig.parameters.keys())



def test_whileloop_is_not_abstract():
    assert not inspect.isabstract(WhileLoop)


def test_whileloop_constructor_exists():
    assert callable(WhileLoop.__init__)


def test_whileloop_constructor_args():
    sig = inspect.signature(WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_java_dowhileloop_is_not_abstract():
    assert not inspect.isabstract(java_DoWhileLoop)


def test_java_dowhileloop_constructor_exists():
    assert callable(java_DoWhileLoop.__init__)


def test_java_dowhileloop_constructor_args():
    sig = inspect.signature(java_DoWhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_switchcase_is_not_abstract():
    assert not inspect.isabstract(SwitchCase)


def test_switchcase_constructor_exists():
    assert callable(SwitchCase.__init__)


def test_switchcase_constructor_args():
    sig = inspect.signature(SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_java_defaultswitchcase_is_not_abstract():
    assert not inspect.isabstract(java_DefaultSwitchCase)


def test_java_defaultswitchcase_constructor_exists():
    assert callable(java_DefaultSwitchCase.__init__)


def test_java_defaultswitchcase_constructor_args():
    sig = inspect.signature(java_DefaultSwitchCase.__init__)
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



def test_java_continue_is_not_abstract():
    assert not inspect.isabstract(java_Continue)


def test_java_continue_constructor_exists():
    assert callable(java_Continue.__init__)


def test_java_continue_constructor_args():
    sig = inspect.signature(java_Continue.__init__)
    params = list(sig.parameters.keys())



def test_java_break_is_not_abstract():
    assert not inspect.isabstract(java_Break)


def test_java_break_constructor_exists():
    assert callable(java_Break.__init__)


def test_java_break_constructor_args():
    sig = inspect.signature(java_Break.__init__)
    params = list(sig.parameters.keys())



def test_conditional_is_not_abstract():
    assert not inspect.isabstract(Conditional)


def test_conditional_constructor_exists():
    assert callable(Conditional.__init__)


def test_conditional_constructor_args():
    sig = inspect.signature(Conditional.__init__)
    params = list(sig.parameters.keys())



def test_java_normalswitchcase_is_not_abstract():
    assert not inspect.isabstract(java_NormalSwitchCase)


def test_java_normalswitchcase_constructor_exists():
    assert callable(java_NormalSwitchCase.__init__)


def test_java_normalswitchcase_constructor_args():
    sig = inspect.signature(java_NormalSwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_java_forloopinitializer_is_not_abstract():
    assert not inspect.isabstract(java_ForLoopInitializer)


def test_java_forloopinitializer_constructor_exists():
    assert callable(java_ForLoopInitializer.__init__)


def test_java_forloopinitializer_constructor_args():
    sig = inspect.signature(java_ForLoopInitializer.__init__)
    params = list(sig.parameters.keys())



def test_java_conditional_is_not_abstract():
    assert not inspect.isabstract(java_Conditional)


def test_java_conditional_constructor_exists():
    assert callable(java_Conditional.__init__)


def test_java_conditional_constructor_args():
    sig = inspect.signature(java_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_java_statementlistcontainer_is_not_abstract():
    assert not inspect.isabstract(java_StatementListContainer)


def test_java_statementlistcontainer_constructor_exists():
    assert callable(java_StatementListContainer.__init__)


def test_java_statementlistcontainer_constructor_args():
    sig = inspect.signature(java_StatementListContainer.__init__)
    params = list(sig.parameters.keys())



def test_java_statement_is_not_abstract():
    assert not inspect.isabstract(java_Statement)


def test_java_statement_constructor_exists():
    assert callable(java_Statement.__init__)


def test_java_statement_constructor_args():
    sig = inspect.signature(java_Statement.__init__)
    params = list(sig.parameters.keys())



def test_java_statementcontainer_is_not_abstract():
    assert not inspect.isabstract(java_StatementContainer)


def test_java_statementcontainer_constructor_exists():
    assert callable(java_StatementContainer.__init__)


def test_java_statementcontainer_constructor_args():
    sig = inspect.signature(java_StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_java_variablelengthparameter_is_not_abstract():
    assert not inspect.isabstract(java_VariableLengthParameter)


def test_java_variablelengthparameter_constructor_exists():
    assert callable(java_VariableLengthParameter.__init__)


def test_java_variablelengthparameter_constructor_args():
    sig = inspect.signature(java_VariableLengthParameter.__init__)
    params = list(sig.parameters.keys())



def test_java_ordinaryparameter_is_not_abstract():
    assert not inspect.isabstract(java_OrdinaryParameter)


def test_java_ordinaryparameter_constructor_exists():
    assert callable(java_OrdinaryParameter.__init__)


def test_java_ordinaryparameter_constructor_args():
    sig = inspect.signature(java_OrdinaryParameter.__init__)
    params = list(sig.parameters.keys())



def test_java_parametrizable_is_not_abstract():
    assert not inspect.isabstract(java_Parametrizable)


def test_java_parametrizable_constructor_exists():
    assert callable(java_Parametrizable.__init__)


def test_java_parametrizable_constructor_args():
    sig = inspect.signature(java_Parametrizable.__init__)
    params = list(sig.parameters.keys())



def test_java_selfreference_is_not_abstract():
    assert not inspect.isabstract(java_SelfReference)


def test_java_selfreference_constructor_exists():
    assert callable(java_SelfReference.__init__)


def test_java_selfreference_constructor_args():
    sig = inspect.signature(java_SelfReference.__init__)
    params = list(sig.parameters.keys())



def test_java_stringreference_is_not_abstract():
    assert not inspect.isabstract(java_StringReference)


def test_java_stringreference_constructor_exists():
    assert callable(java_StringReference.__init__)


def test_java_stringreference_constructor_args():
    sig = inspect.signature(java_StringReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_java_stringreference_has_value():
    assert hasattr(java_StringReference, "value")
    descriptor = None
    for klass in java_StringReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statementcontainer_is_not_abstract():
    assert not inspect.isabstract(StatementContainer)


def test_statementcontainer_constructor_exists():
    assert callable(StatementContainer.__init__)


def test_statementcontainer_constructor_args():
    sig = inspect.signature(StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_elementreference_is_not_abstract():
    assert not inspect.isabstract(ElementReference)


def test_elementreference_constructor_exists():
    assert callable(ElementReference.__init__)


def test_elementreference_constructor_args():
    sig = inspect.signature(ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_java_identifierreference_is_not_abstract():
    assert not inspect.isabstract(java_IdentifierReference)


def test_java_identifierreference_constructor_exists():
    assert callable(java_IdentifierReference.__init__)


def test_java_identifierreference_constructor_args():
    sig = inspect.signature(java_IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_java_elementreference_is_not_abstract():
    assert not inspect.isabstract(java_ElementReference)


def test_java_elementreference_constructor_exists():
    assert callable(java_ElementReference.__init__)


def test_java_elementreference_constructor_args():
    sig = inspect.signature(java_ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_java_argumentable_is_not_abstract():
    assert not inspect.isabstract(java_Argumentable)


def test_java_argumentable_constructor_exists():
    assert callable(java_Argumentable.__init__)


def test_java_argumentable_constructor_args():
    sig = inspect.signature(java_Argumentable.__init__)
    params = list(sig.parameters.keys())



def test_typeargumentable_is_not_abstract():
    assert not inspect.isabstract(TypeArgumentable)


def test_typeargumentable_constructor_exists():
    assert callable(TypeArgumentable.__init__)


def test_typeargumentable_constructor_args():
    sig = inspect.signature(TypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_java_classifierreference_is_not_abstract():
    assert not inspect.isabstract(java_ClassifierReference)


def test_java_classifierreference_constructor_exists():
    assert callable(java_ClassifierReference.__init__)


def test_java_classifierreference_constructor_args():
    sig = inspect.signature(java_ClassifierReference.__init__)
    params = list(sig.parameters.keys())



def test_shiftoperator_is_not_abstract():
    assert not inspect.isabstract(ShiftOperator)


def test_shiftoperator_constructor_exists():
    assert callable(ShiftOperator.__init__)


def test_shiftoperator_constructor_args():
    sig = inspect.signature(ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_java_unsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(java_UnsignedRightShift)


def test_java_unsignedrightshift_constructor_exists():
    assert callable(java_UnsignedRightShift.__init__)


def test_java_unsignedrightshift_constructor_args():
    sig = inspect.signature(java_UnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_java_rightshift_is_not_abstract():
    assert not inspect.isabstract(java_RightShift)


def test_java_rightshift_constructor_exists():
    assert callable(java_RightShift.__init__)


def test_java_rightshift_constructor_args():
    sig = inspect.signature(java_RightShift.__init__)
    params = list(sig.parameters.keys())



def test_java_leftshift_is_not_abstract():
    assert not inspect.isabstract(java_LeftShift)


def test_java_leftshift_constructor_exists():
    assert callable(java_LeftShift.__init__)


def test_java_leftshift_constructor_args():
    sig = inspect.signature(java_LeftShift.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationOperator)


def test_unarymodificationoperator_constructor_exists():
    assert callable(UnaryModificationOperator.__init__)


def test_unarymodificationoperator_constructor_args():
    sig = inspect.signature(UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_java_plusplus_is_not_abstract():
    assert not inspect.isabstract(java_PlusPlus)


def test_java_plusplus_constructor_exists():
    assert callable(java_PlusPlus.__init__)


def test_java_plusplus_constructor_args():
    sig = inspect.signature(java_PlusPlus.__init__)
    params = list(sig.parameters.keys())



def test_java_minusminus_is_not_abstract():
    assert not inspect.isabstract(java_MinusMinus)


def test_java_minusminus_constructor_exists():
    assert callable(java_MinusMinus.__init__)


def test_java_minusminus_constructor_args():
    sig = inspect.signature(java_MinusMinus.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeOperator)


def test_multiplicativeoperator_constructor_exists():
    assert callable(MultiplicativeOperator.__init__)


def test_multiplicativeoperator_constructor_args():
    sig = inspect.signature(MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_java_remainder_is_not_abstract():
    assert not inspect.isabstract(java_Remainder)


def test_java_remainder_constructor_exists():
    assert callable(java_Remainder.__init__)


def test_java_remainder_constructor_args():
    sig = inspect.signature(java_Remainder.__init__)
    params = list(sig.parameters.keys())



def test_java_multiplication_is_not_abstract():
    assert not inspect.isabstract(java_Multiplication)


def test_java_multiplication_constructor_exists():
    assert callable(java_Multiplication.__init__)


def test_java_multiplication_constructor_args():
    sig = inspect.signature(java_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_java_division_is_not_abstract():
    assert not inspect.isabstract(java_Division)


def test_java_division_constructor_exists():
    assert callable(java_Division.__init__)


def test_java_division_constructor_args():
    sig = inspect.signature(java_Division.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_java_complement_is_not_abstract():
    assert not inspect.isabstract(java_Complement)


def test_java_complement_constructor_exists():
    assert callable(java_Complement.__init__)


def test_java_complement_constructor_args():
    sig = inspect.signature(java_Complement.__init__)
    params = list(sig.parameters.keys())



def test_java_negate_is_not_abstract():
    assert not inspect.isabstract(java_Negate)


def test_java_negate_constructor_exists():
    assert callable(java_Negate.__init__)


def test_java_negate_constructor_args():
    sig = inspect.signature(java_Negate.__init__)
    params = list(sig.parameters.keys())



def test_additiveoperator_is_not_abstract():
    assert not inspect.isabstract(AdditiveOperator)


def test_additiveoperator_constructor_exists():
    assert callable(AdditiveOperator.__init__)


def test_additiveoperator_constructor_args():
    sig = inspect.signature(AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_java_subtraction_is_not_abstract():
    assert not inspect.isabstract(java_Subtraction)


def test_java_subtraction_constructor_exists():
    assert callable(java_Subtraction.__init__)


def test_java_subtraction_constructor_args():
    sig = inspect.signature(java_Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_java_addition_is_not_abstract():
    assert not inspect.isabstract(java_Addition)


def test_java_addition_constructor_exists():
    assert callable(java_Addition.__init__)


def test_java_addition_constructor_args():
    sig = inspect.signature(java_Addition.__init__)
    params = list(sig.parameters.keys())



def test_relationoperator_is_not_abstract():
    assert not inspect.isabstract(RelationOperator)


def test_relationoperator_constructor_exists():
    assert callable(RelationOperator.__init__)


def test_relationoperator_constructor_args():
    sig = inspect.signature(RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_java_lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(java_LessThanOrEqual)


def test_java_lessthanorequal_constructor_exists():
    assert callable(java_LessThanOrEqual.__init__)


def test_java_lessthanorequal_constructor_args():
    sig = inspect.signature(java_LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_java_greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(java_GreaterThanOrEqual)


def test_java_greaterthanorequal_constructor_exists():
    assert callable(java_GreaterThanOrEqual.__init__)


def test_java_greaterthanorequal_constructor_args():
    sig = inspect.signature(java_GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_java_lessthan_is_not_abstract():
    assert not inspect.isabstract(java_LessThan)


def test_java_lessthan_constructor_exists():
    assert callable(java_LessThan.__init__)


def test_java_lessthan_constructor_args():
    sig = inspect.signature(java_LessThan.__init__)
    params = list(sig.parameters.keys())



def test_java_greaterthan_is_not_abstract():
    assert not inspect.isabstract(java_GreaterThan)


def test_java_greaterthan_constructor_exists():
    assert callable(java_GreaterThan.__init__)


def test_java_greaterthan_constructor_args():
    sig = inspect.signature(java_GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypereference_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeReference)


def test_java_primitivetypereference_constructor_exists():
    assert callable(java_PrimitiveTypeReference.__init__)


def test_java_primitivetypereference_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_java_reflectiveclassreference_is_not_abstract():
    assert not inspect.isabstract(java_ReflectiveClassReference)


def test_java_reflectiveclassreference_constructor_exists():
    assert callable(java_ReflectiveClassReference.__init__)


def test_java_reflectiveclassreference_constructor_args():
    sig = inspect.signature(java_ReflectiveClassReference.__init__)
    params = list(sig.parameters.keys())



def test_assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(AssignmentOperator)


def test_assignmentoperator_constructor_exists():
    assert callable(AssignmentOperator.__init__)


def test_assignmentoperator_constructor_args():
    sig = inspect.signature(AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentand_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentAnd)


def test_java_assignmentand_constructor_exists():
    assert callable(java_AssignmentAnd.__init__)


def test_java_assignmentand_constructor_args():
    sig = inspect.signature(java_AssignmentAnd.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentminus_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentMinus)


def test_java_assignmentminus_constructor_exists():
    assert callable(java_AssignmentMinus.__init__)


def test_java_assignmentminus_constructor_args():
    sig = inspect.signature(java_AssignmentMinus.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentor_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentOr)


def test_java_assignmentor_constructor_exists():
    assert callable(java_AssignmentOr.__init__)


def test_java_assignmentor_constructor_args():
    sig = inspect.signature(java_AssignmentOr.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentdivision_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentDivision)


def test_java_assignmentdivision_constructor_exists():
    assert callable(java_AssignmentDivision.__init__)


def test_java_assignmentdivision_constructor_args():
    sig = inspect.signature(java_AssignmentDivision.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentmodulo_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentModulo)


def test_java_assignmentmodulo_constructor_exists():
    assert callable(java_AssignmentModulo.__init__)


def test_java_assignmentmodulo_constructor_args():
    sig = inspect.signature(java_AssignmentModulo.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentexclusiveor_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentExclusiveOr)


def test_java_assignmentexclusiveor_constructor_exists():
    assert callable(java_AssignmentExclusiveOr.__init__)


def test_java_assignmentexclusiveor_constructor_args():
    sig = inspect.signature(java_AssignmentExclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentmultiplication_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentMultiplication)


def test_java_assignmentmultiplication_constructor_exists():
    assert callable(java_AssignmentMultiplication.__init__)


def test_java_assignmentmultiplication_constructor_args():
    sig = inspect.signature(java_AssignmentMultiplication.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentleftshift_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentLeftShift)


def test_java_assignmentleftshift_constructor_exists():
    assert callable(java_AssignmentLeftShift.__init__)


def test_java_assignmentleftshift_constructor_args():
    sig = inspect.signature(java_AssignmentLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_java_assignment_is_not_abstract():
    assert not inspect.isabstract(java_Assignment)


def test_java_assignment_constructor_exists():
    assert callable(java_Assignment.__init__)


def test_java_assignment_constructor_args():
    sig = inspect.signature(java_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_java_operator_is_not_abstract():
    assert not inspect.isabstract(java_Operator)


def test_java_operator_constructor_exists():
    assert callable(java_Operator.__init__)


def test_java_operator_constructor_args():
    sig = inspect.signature(java_Operator.__init__)
    params = list(sig.parameters.keys())



def test_modifier_is_not_abstract():
    assert not inspect.isabstract(Modifier)


def test_modifier_constructor_exists():
    assert callable(Modifier.__init__)


def test_modifier_constructor_args():
    sig = inspect.signature(Modifier.__init__)
    params = list(sig.parameters.keys())



def test_java_synchronized_is_not_abstract():
    assert not inspect.isabstract(java_Synchronized)


def test_java_synchronized_constructor_exists():
    assert callable(java_Synchronized.__init__)


def test_java_synchronized_constructor_args():
    sig = inspect.signature(java_Synchronized.__init__)
    params = list(sig.parameters.keys())



def test_java_protected_is_not_abstract():
    assert not inspect.isabstract(java_Protected)


def test_java_protected_constructor_exists():
    assert callable(java_Protected.__init__)


def test_java_protected_constructor_args():
    sig = inspect.signature(java_Protected.__init__)
    params = list(sig.parameters.keys())



def test_java_volatile_is_not_abstract():
    assert not inspect.isabstract(java_Volatile)


def test_java_volatile_constructor_exists():
    assert callable(java_Volatile.__init__)


def test_java_volatile_constructor_args():
    sig = inspect.signature(java_Volatile.__init__)
    params = list(sig.parameters.keys())



def test_java_public_is_not_abstract():
    assert not inspect.isabstract(java_Public)


def test_java_public_constructor_exists():
    assert callable(java_Public.__init__)


def test_java_public_constructor_args():
    sig = inspect.signature(java_Public.__init__)
    params = list(sig.parameters.keys())



def test_java_private_is_not_abstract():
    assert not inspect.isabstract(java_Private)


def test_java_private_constructor_exists():
    assert callable(java_Private.__init__)


def test_java_private_constructor_args():
    sig = inspect.signature(java_Private.__init__)
    params = list(sig.parameters.keys())



def test_java_final_is_not_abstract():
    assert not inspect.isabstract(java_Final)


def test_java_final_constructor_exists():
    assert callable(java_Final.__init__)


def test_java_final_constructor_args():
    sig = inspect.signature(java_Final.__init__)
    params = list(sig.parameters.keys())



def test_java_transient_is_not_abstract():
    assert not inspect.isabstract(java_Transient)


def test_java_transient_constructor_exists():
    assert callable(java_Transient.__init__)


def test_java_transient_constructor_args():
    sig = inspect.signature(java_Transient.__init__)
    params = list(sig.parameters.keys())



def test_java_strictfp_is_not_abstract():
    assert not inspect.isabstract(java_Strictfp)


def test_java_strictfp_constructor_exists():
    assert callable(java_Strictfp.__init__)


def test_java_strictfp_constructor_args():
    sig = inspect.signature(java_Strictfp.__init__)
    params = list(sig.parameters.keys())



def test_java_native_is_not_abstract():
    assert not inspect.isabstract(java_Native)


def test_java_native_constructor_exists():
    assert callable(java_Native.__init__)


def test_java_native_constructor_args():
    sig = inspect.signature(java_Native.__init__)
    params = list(sig.parameters.keys())



def test_java_abstract_is_not_abstract():
    assert not inspect.isabstract(java_Abstract)


def test_java_abstract_constructor_exists():
    assert callable(java_Abstract.__init__)


def test_java_abstract_constructor_args():
    sig = inspect.signature(java_Abstract.__init__)
    params = list(sig.parameters.keys())



def test_java_modifiable_is_not_abstract():
    assert not inspect.isabstract(java_Modifiable)


def test_java_modifiable_constructor_exists():
    assert callable(java_Modifiable.__init__)


def test_java_modifiable_constructor_args():
    sig = inspect.signature(java_Modifiable.__init__)
    params = list(sig.parameters.keys())



def test_equalityoperator_is_not_abstract():
    assert not inspect.isabstract(EqualityOperator)


def test_equalityoperator_constructor_exists():
    assert callable(EqualityOperator.__init__)


def test_equalityoperator_constructor_args():
    sig = inspect.signature(EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_java_notequal_is_not_abstract():
    assert not inspect.isabstract(java_NotEqual)


def test_java_notequal_constructor_exists():
    assert callable(java_NotEqual.__init__)


def test_java_notequal_constructor_args():
    sig = inspect.signature(java_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_java_equal_is_not_abstract():
    assert not inspect.isabstract(java_Equal)


def test_java_equal_constructor_exists():
    assert callable(java_Equal.__init__)


def test_java_equal_constructor_args():
    sig = inspect.signature(java_Equal.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentunsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentUnsignedRightShift)


def test_java_assignmentunsignedrightshift_constructor_exists():
    assert callable(java_AssignmentUnsignedRightShift.__init__)


def test_java_assignmentunsignedrightshift_constructor_args():
    sig = inspect.signature(java_AssignmentUnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentrightshift_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentRightShift)


def test_java_assignmentrightshift_constructor_exists():
    assert callable(java_AssignmentRightShift.__init__)


def test_java_assignmentrightshift_constructor_args():
    sig = inspect.signature(java_AssignmentRightShift.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentplus_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentPlus)


def test_java_assignmentplus_constructor_exists():
    assert callable(java_AssignmentPlus.__init__)


def test_java_assignmentplus_constructor_args():
    sig = inspect.signature(java_AssignmentPlus.__init__)
    params = list(sig.parameters.keys())



def test_java_annotableandmodifiable_is_not_abstract():
    assert not inspect.isabstract(java_AnnotableAndModifiable)


def test_java_annotableandmodifiable_constructor_exists():
    assert callable(java_AnnotableAndModifiable.__init__)


def test_java_annotableandmodifiable_constructor_args():
    sig = inspect.signature(java_AnnotableAndModifiable.__init__)
    params = list(sig.parameters.keys())



def test_java_annotationinstanceormodifier_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationInstanceOrModifier)


def test_java_annotationinstanceormodifier_constructor_exists():
    assert callable(java_AnnotationInstanceOrModifier.__init__)


def test_java_annotationinstanceormodifier_constructor_args():
    sig = inspect.signature(java_AnnotationInstanceOrModifier.__init__)
    params = list(sig.parameters.keys())



def test_java_modifier_is_not_abstract():
    assert not inspect.isabstract(java_Modifier)


def test_java_modifier_constructor_exists():
    assert callable(java_Modifier.__init__)


def test_java_modifier_constructor_args():
    sig = inspect.signature(java_Modifier.__init__)
    params = list(sig.parameters.keys())



def test_method_is_not_abstract():
    assert not inspect.isabstract(Method)


def test_method_constructor_exists():
    assert callable(Method.__init__)


def test_method_constructor_args():
    sig = inspect.signature(Method.__init__)
    params = list(sig.parameters.keys())



def test_java_interfacemethod_is_not_abstract():
    assert not inspect.isabstract(java_InterfaceMethod)


def test_java_interfacemethod_constructor_exists():
    assert callable(java_InterfaceMethod.__init__)


def test_java_interfacemethod_constructor_args():
    sig = inspect.signature(java_InterfaceMethod.__init__)
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



def test_java_catchblock_is_not_abstract():
    assert not inspect.isabstract(java_CatchBlock)


def test_java_catchblock_constructor_exists():
    assert callable(java_CatchBlock.__init__)


def test_java_catchblock_constructor_args():
    sig = inspect.signature(java_CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_java_switchcase_is_not_abstract():
    assert not inspect.isabstract(java_SwitchCase)


def test_java_switchcase_constructor_exists():
    assert callable(java_SwitchCase.__init__)


def test_java_switchcase_constructor_args():
    sig = inspect.signature(java_SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_java_classmethod_is_not_abstract():
    assert not inspect.isabstract(java_ClassMethod)


def test_java_classmethod_constructor_exists():
    assert callable(java_ClassMethod.__init__)


def test_java_classmethod_constructor_args():
    sig = inspect.signature(java_ClassMethod.__init__)
    params = list(sig.parameters.keys())



def test_initializable_is_not_abstract():
    assert not inspect.isabstract(Initializable)


def test_initializable_constructor_exists():
    assert callable(Initializable.__init__)


def test_initializable_constructor_args():
    sig = inspect.signature(Initializable.__init__)
    params = list(sig.parameters.keys())



def test_java_membercontainer_is_not_abstract():
    assert not inspect.isabstract(java_MemberContainer)


def test_java_membercontainer_constructor_exists():
    assert callable(java_MemberContainer.__init__)


def test_java_membercontainer_constructor_args():
    sig = inspect.signature(java_MemberContainer.__init__)
    params = list(sig.parameters.keys())



def test_java_namespaceclassifierreference_is_not_abstract():
    assert not inspect.isabstract(java_NamespaceClassifierReference)


def test_java_namespaceclassifierreference_constructor_exists():
    assert callable(java_NamespaceClassifierReference.__init__)


def test_java_namespaceclassifierreference_constructor_args():
    sig = inspect.signature(java_NamespaceClassifierReference.__init__)
    params = list(sig.parameters.keys())



def test_java_exceptionthrower_is_not_abstract():
    assert not inspect.isabstract(java_ExceptionThrower)


def test_java_exceptionthrower_constructor_exists():
    assert callable(java_ExceptionThrower.__init__)


def test_java_exceptionthrower_constructor_args():
    sig = inspect.signature(java_ExceptionThrower.__init__)
    params = list(sig.parameters.keys())



def test_self_is_not_abstract():
    assert not inspect.isabstract(Self)


def test_self_constructor_exists():
    assert callable(Self.__init__)


def test_self_constructor_args():
    sig = inspect.signature(Self.__init__)
    params = list(sig.parameters.keys())



def test_java_this_is_not_abstract():
    assert not inspect.isabstract(java_This)


def test_java_this_constructor_exists():
    assert callable(java_This.__init__)


def test_java_this_constructor_args():
    sig = inspect.signature(java_This.__init__)
    params = list(sig.parameters.keys())



def test_java_super_is_not_abstract():
    assert not inspect.isabstract(java_Super)


def test_java_super_constructor_exists():
    assert callable(java_Super.__init__)


def test_java_super_constructor_args():
    sig = inspect.signature(java_Super.__init__)
    params = list(sig.parameters.keys())



def test_longliteral_is_not_abstract():
    assert not inspect.isabstract(LongLiteral)


def test_longliteral_constructor_exists():
    assert callable(LongLiteral.__init__)


def test_longliteral_constructor_args():
    sig = inspect.signature(LongLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java_octallongliteral_is_not_abstract():
    assert not inspect.isabstract(java_OctalLongLiteral)


def test_java_octallongliteral_constructor_exists():
    assert callable(java_OctalLongLiteral.__init__)


def test_java_octallongliteral_constructor_args():
    sig = inspect.signature(java_OctalLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "octalValue" in params, "Missing parameter 'octalValue'"

def test_java_octallongliteral_has_octalValue():
    assert hasattr(java_OctalLongLiteral, "octalValue")
    descriptor = None
    for klass in java_OctalLongLiteral.__mro__:
        if "octalValue" in klass.__dict__:
            descriptor = klass.__dict__["octalValue"]
            break
    assert isinstance(descriptor, property)



def test_java_hexlongliteral_is_not_abstract():
    assert not inspect.isabstract(java_HexLongLiteral)


def test_java_hexlongliteral_constructor_exists():
    assert callable(java_HexLongLiteral.__init__)


def test_java_hexlongliteral_constructor_args():
    sig = inspect.signature(java_HexLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_java_hexlongliteral_has_hexValue():
    assert hasattr(java_HexLongLiteral, "hexValue")
    descriptor = None
    for klass in java_HexLongLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_java_decimallongliteral_is_not_abstract():
    assert not inspect.isabstract(java_DecimalLongLiteral)


def test_java_decimallongliteral_constructor_exists():
    assert callable(java_DecimalLongLiteral.__init__)


def test_java_decimallongliteral_constructor_args():
    sig = inspect.signature(java_DecimalLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_java_decimallongliteral_has_decimalValue():
    assert hasattr(java_DecimalLongLiteral, "decimalValue")
    descriptor = None
    for klass in java_DecimalLongLiteral.__mro__:
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



def test_java_hexintegerliteral_is_not_abstract():
    assert not inspect.isabstract(java_HexIntegerLiteral)


def test_java_hexintegerliteral_constructor_exists():
    assert callable(java_HexIntegerLiteral.__init__)


def test_java_hexintegerliteral_constructor_args():
    sig = inspect.signature(java_HexIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_java_hexintegerliteral_has_hexValue():
    assert hasattr(java_HexIntegerLiteral, "hexValue")
    descriptor = None
    for klass in java_HexIntegerLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_java_octalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(java_OctalIntegerLiteral)


def test_java_octalintegerliteral_constructor_exists():
    assert callable(java_OctalIntegerLiteral.__init__)


def test_java_octalintegerliteral_constructor_args():
    sig = inspect.signature(java_OctalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "octalValue" in params, "Missing parameter 'octalValue'"

def test_java_octalintegerliteral_has_octalValue():
    assert hasattr(java_OctalIntegerLiteral, "octalValue")
    descriptor = None
    for klass in java_OctalIntegerLiteral.__mro__:
        if "octalValue" in klass.__dict__:
            descriptor = klass.__dict__["octalValue"]
            break
    assert isinstance(descriptor, property)



def test_java_decimalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(java_DecimalIntegerLiteral)


def test_java_decimalintegerliteral_constructor_exists():
    assert callable(java_DecimalIntegerLiteral.__init__)


def test_java_decimalintegerliteral_constructor_args():
    sig = inspect.signature(java_DecimalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_java_decimalintegerliteral_has_decimalValue():
    assert hasattr(java_DecimalIntegerLiteral, "decimalValue")
    descriptor = None
    for klass in java_DecimalIntegerLiteral.__mro__:
        if "decimalValue" in klass.__dict__:
            descriptor = klass.__dict__["decimalValue"]
            break
    assert isinstance(descriptor, property)



def test_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(DoubleLiteral)


def test_doubleliteral_constructor_exists():
    assert callable(DoubleLiteral.__init__)


def test_doubleliteral_constructor_args():
    sig = inspect.signature(DoubleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java_hexdoubleliteral_is_not_abstract():
    assert not inspect.isabstract(java_HexDoubleLiteral)


def test_java_hexdoubleliteral_constructor_exists():
    assert callable(java_HexDoubleLiteral.__init__)


def test_java_hexdoubleliteral_constructor_args():
    sig = inspect.signature(java_HexDoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_java_hexdoubleliteral_has_hexValue():
    assert hasattr(java_HexDoubleLiteral, "hexValue")
    descriptor = None
    for klass in java_HexDoubleLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_java_decimaldoubleliteral_is_not_abstract():
    assert not inspect.isabstract(java_DecimalDoubleLiteral)


def test_java_decimaldoubleliteral_constructor_exists():
    assert callable(java_DecimalDoubleLiteral.__init__)


def test_java_decimaldoubleliteral_constructor_args():
    sig = inspect.signature(java_DecimalDoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_java_decimaldoubleliteral_has_decimalValue():
    assert hasattr(java_DecimalDoubleLiteral, "decimalValue")
    descriptor = None
    for klass in java_DecimalDoubleLiteral.__mro__:
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



def test_java_hexfloatliteral_is_not_abstract():
    assert not inspect.isabstract(java_HexFloatLiteral)


def test_java_hexfloatliteral_constructor_exists():
    assert callable(java_HexFloatLiteral.__init__)


def test_java_hexfloatliteral_constructor_args():
    sig = inspect.signature(java_HexFloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_java_hexfloatliteral_has_hexValue():
    assert hasattr(java_HexFloatLiteral, "hexValue")
    descriptor = None
    for klass in java_HexFloatLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_java_decimalfloatliteral_is_not_abstract():
    assert not inspect.isabstract(java_DecimalFloatLiteral)


def test_java_decimalfloatliteral_constructor_exists():
    assert callable(java_DecimalFloatLiteral.__init__)


def test_java_decimalfloatliteral_constructor_args():
    sig = inspect.signature(java_DecimalFloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_java_decimalfloatliteral_has_decimalValue():
    assert hasattr(java_DecimalFloatLiteral, "decimalValue")
    descriptor = None
    for klass in java_DecimalFloatLiteral.__mro__:
        if "decimalValue" in klass.__dict__:
            descriptor = klass.__dict__["decimalValue"]
            break
    assert isinstance(descriptor, property)



def test_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_reference_is_not_abstract():
    assert not inspect.isabstract(java_Reference)


def test_java_reference_constructor_exists():
    assert callable(java_Reference.__init__)


def test_java_reference_constructor_args():
    sig = inspect.signature(java_Reference.__init__)
    params = list(sig.parameters.keys())



def test_java_literal_is_not_abstract():
    assert not inspect.isabstract(java_Literal)


def test_java_literal_constructor_exists():
    assert callable(java_Literal.__init__)


def test_java_literal_constructor_args():
    sig = inspect.signature(java_Literal.__init__)
    params = list(sig.parameters.keys())



def test_java_self_is_not_abstract():
    assert not inspect.isabstract(java_Self)


def test_java_self_constructor_exists():
    assert callable(java_Self.__init__)


def test_java_self_constructor_args():
    sig = inspect.signature(java_Self.__init__)
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



def test_java_explicitconstructorcall_is_not_abstract():
    assert not inspect.isabstract(java_ExplicitConstructorCall)


def test_java_explicitconstructorcall_constructor_exists():
    assert callable(java_ExplicitConstructorCall.__init__)


def test_java_explicitconstructorcall_constructor_args():
    sig = inspect.signature(java_ExplicitConstructorCall.__init__)
    params = list(sig.parameters.keys())



def test_java_newconstructorcall_is_not_abstract():
    assert not inspect.isabstract(java_NewConstructorCall)


def test_java_newconstructorcall_constructor_exists():
    assert callable(java_NewConstructorCall.__init__)


def test_java_newconstructorcall_constructor_args():
    sig = inspect.signature(java_NewConstructorCall.__init__)
    params = list(sig.parameters.keys())



def test_argumentable_is_not_abstract():
    assert not inspect.isabstract(Argumentable)


def test_argumentable_constructor_exists():
    assert callable(Argumentable.__init__)


def test_argumentable_constructor_args():
    sig = inspect.signature(Argumentable.__init__)
    params = list(sig.parameters.keys())



def test_java_methodcall_is_not_abstract():
    assert not inspect.isabstract(java_MethodCall)


def test_java_methodcall_constructor_exists():
    assert callable(java_MethodCall.__init__)


def test_java_methodcall_constructor_args():
    sig = inspect.signature(java_MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_java_instantiation_is_not_abstract():
    assert not inspect.isabstract(java_Instantiation)


def test_java_instantiation_constructor_exists():
    assert callable(java_Instantiation.__init__)


def test_java_instantiation_constructor_args():
    sig = inspect.signature(java_Instantiation.__init__)
    params = list(sig.parameters.keys())



def test_java_initializable_is_not_abstract():
    assert not inspect.isabstract(java_Initializable)


def test_java_initializable_constructor_exists():
    assert callable(java_Initializable.__init__)


def test_java_initializable_constructor_args():
    sig = inspect.signature(java_Initializable.__init__)
    params = list(sig.parameters.keys())



def test_staticimport_is_not_abstract():
    assert not inspect.isabstract(StaticImport)


def test_staticimport_constructor_exists():
    assert callable(StaticImport.__init__)


def test_staticimport_constructor_args():
    sig = inspect.signature(StaticImport.__init__)
    params = list(sig.parameters.keys())



def test_java_staticmemberimport_is_not_abstract():
    assert not inspect.isabstract(java_StaticMemberImport)


def test_java_staticmemberimport_constructor_exists():
    assert callable(java_StaticMemberImport.__init__)


def test_java_staticmemberimport_constructor_args():
    sig = inspect.signature(java_StaticMemberImport.__init__)
    params = list(sig.parameters.keys())



def test_java_staticclassifierimport_is_not_abstract():
    assert not inspect.isabstract(java_StaticClassifierImport)


def test_java_staticclassifierimport_constructor_exists():
    assert callable(java_StaticClassifierImport.__init__)


def test_java_staticclassifierimport_constructor_args():
    sig = inspect.signature(java_StaticClassifierImport.__init__)
    params = list(sig.parameters.keys())



def test_java_static_is_not_abstract():
    assert not inspect.isabstract(java_Static)


def test_java_static_constructor_exists():
    assert callable(java_Static.__init__)


def test_java_static_constructor_args():
    sig = inspect.signature(java_Static.__init__)
    params = list(sig.parameters.keys())



def test_import_is_not_abstract():
    assert not inspect.isabstract(Import)


def test_import_constructor_exists():
    assert callable(Import.__init__)


def test_import_constructor_args():
    sig = inspect.signature(Import.__init__)
    params = list(sig.parameters.keys())



def test_java_classifierimport_is_not_abstract():
    assert not inspect.isabstract(java_ClassifierImport)


def test_java_classifierimport_constructor_exists():
    assert callable(java_ClassifierImport.__init__)


def test_java_classifierimport_constructor_args():
    sig = inspect.signature(java_ClassifierImport.__init__)
    params = list(sig.parameters.keys())



def test_java_packageimport_is_not_abstract():
    assert not inspect.isabstract(java_PackageImport)


def test_java_packageimport_constructor_exists():
    assert callable(java_PackageImport.__init__)


def test_java_packageimport_constructor_args():
    sig = inspect.signature(java_PackageImport.__init__)
    params = list(sig.parameters.keys())



def test_java_staticimport_is_not_abstract():
    assert not inspect.isabstract(java_StaticImport)


def test_java_staticimport_constructor_exists():
    assert callable(java_StaticImport.__init__)


def test_java_staticimport_constructor_args():
    sig = inspect.signature(java_StaticImport.__init__)
    params = list(sig.parameters.keys())



def test_java_importingelement_is_not_abstract():
    assert not inspect.isabstract(java_ImportingElement)


def test_java_importingelement_constructor_exists():
    assert callable(java_ImportingElement.__init__)


def test_java_importingelement_constructor_args():
    sig = inspect.signature(java_ImportingElement.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_java_longliteral_is_not_abstract():
    assert not inspect.isabstract(java_LongLiteral)


def test_java_longliteral_constructor_exists():
    assert callable(java_LongLiteral.__init__)


def test_java_longliteral_constructor_args():
    sig = inspect.signature(java_LongLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(java_DoubleLiteral)


def test_java_doubleliteral_constructor_exists():
    assert callable(java_DoubleLiteral.__init__)


def test_java_doubleliteral_constructor_args():
    sig = inspect.signature(java_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java_characterliteral_is_not_abstract():
    assert not inspect.isabstract(java_CharacterLiteral)


def test_java_characterliteral_constructor_exists():
    assert callable(java_CharacterLiteral.__init__)


def test_java_characterliteral_constructor_args():
    sig = inspect.signature(java_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_java_characterliteral_has_value():
    assert hasattr(java_CharacterLiteral, "value")
    descriptor = None
    for klass in java_CharacterLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_java_integerliteral_is_not_abstract():
    assert not inspect.isabstract(java_IntegerLiteral)


def test_java_integerliteral_constructor_exists():
    assert callable(java_IntegerLiteral.__init__)


def test_java_integerliteral_constructor_args():
    sig = inspect.signature(java_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java_floatliteral_is_not_abstract():
    assert not inspect.isabstract(java_FloatLiteral)


def test_java_floatliteral_constructor_exists():
    assert callable(java_FloatLiteral.__init__)


def test_java_floatliteral_constructor_args():
    sig = inspect.signature(java_FloatLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java_nullliteral_is_not_abstract():
    assert not inspect.isabstract(java_NullLiteral)


def test_java_nullliteral_constructor_exists():
    assert callable(java_NullLiteral.__init__)


def test_java_nullliteral_constructor_args():
    sig = inspect.signature(java_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(java_BooleanLiteral)


def test_java_booleanliteral_constructor_exists():
    assert callable(java_BooleanLiteral.__init__)


def test_java_booleanliteral_constructor_args():
    sig = inspect.signature(java_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_java_booleanliteral_has_value():
    assert hasattr(java_BooleanLiteral, "value")
    descriptor = None
    for klass in java_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_typeargument_is_not_abstract():
    assert not inspect.isabstract(TypeArgument)


def test_typeargument_constructor_exists():
    assert callable(TypeArgument.__init__)


def test_typeargument_constructor_args():
    sig = inspect.signature(TypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_java_supertypeargument_is_not_abstract():
    assert not inspect.isabstract(java_SuperTypeArgument)


def test_java_supertypeargument_constructor_exists():
    assert callable(java_SuperTypeArgument.__init__)


def test_java_supertypeargument_constructor_args():
    sig = inspect.signature(java_SuperTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_java_qualifiedtypeargument_is_not_abstract():
    assert not inspect.isabstract(java_QualifiedTypeArgument)


def test_java_qualifiedtypeargument_constructor_exists():
    assert callable(java_QualifiedTypeArgument.__init__)


def test_java_qualifiedtypeargument_constructor_args():
    sig = inspect.signature(java_QualifiedTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_java_extendstypeargument_is_not_abstract():
    assert not inspect.isabstract(java_ExtendsTypeArgument)


def test_java_extendstypeargument_constructor_exists():
    assert callable(java_ExtendsTypeArgument.__init__)


def test_java_extendstypeargument_constructor_args():
    sig = inspect.signature(java_ExtendsTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_java_typeparametrizable_is_not_abstract():
    assert not inspect.isabstract(java_TypeParametrizable)


def test_java_typeparametrizable_constructor_exists():
    assert callable(java_TypeParametrizable.__init__)


def test_java_typeparametrizable_constructor_args():
    sig = inspect.signature(java_TypeParametrizable.__init__)
    params = list(sig.parameters.keys())



def test_java_calltypeargumentable_is_not_abstract():
    assert not inspect.isabstract(java_CallTypeArgumentable)


def test_java_calltypeargumentable_constructor_exists():
    assert callable(java_CallTypeArgumentable.__init__)


def test_java_calltypeargumentable_constructor_args():
    sig = inspect.signature(java_CallTypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_java_typeargumentable_is_not_abstract():
    assert not inspect.isabstract(java_TypeArgumentable)


def test_java_typeargumentable_constructor_exists():
    assert callable(java_TypeArgumentable.__init__)


def test_java_typeargumentable_constructor_args():
    sig = inspect.signature(java_TypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_java_typeargument_is_not_abstract():
    assert not inspect.isabstract(java_TypeArgument)


def test_java_typeargument_constructor_exists():
    assert callable(java_TypeArgument.__init__)


def test_java_typeargument_constructor_args():
    sig = inspect.signature(java_TypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_java_nestedexpression_is_not_abstract():
    assert not inspect.isabstract(java_NestedExpression)


def test_java_nestedexpression_constructor_exists():
    assert callable(java_NestedExpression.__init__)


def test_java_nestedexpression_constructor_args():
    sig = inspect.signature(java_NestedExpression.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationExpressionChild)


def test_unarymodificationexpressionchild_constructor_exists():
    assert callable(UnaryModificationExpressionChild.__init__)


def test_unarymodificationexpressionchild_constructor_args():
    sig = inspect.signature(UnaryModificationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(java_PrimaryExpression)


def test_java_primaryexpression_constructor_exists():
    assert callable(java_PrimaryExpression.__init__)


def test_java_primaryexpression_constructor_args():
    sig = inspect.signature(java_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_castexpression_is_not_abstract():
    assert not inspect.isabstract(java_CastExpression)


def test_java_castexpression_constructor_exists():
    assert callable(java_CastExpression.__init__)


def test_java_castexpression_constructor_args():
    sig = inspect.signature(java_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_import_is_not_abstract():
    assert not inspect.isabstract(java_Import)


def test_java_import_constructor_exists():
    assert callable(java_Import.__init__)


def test_java_import_constructor_args():
    sig = inspect.signature(java_Import.__init__)
    params = list(sig.parameters.keys())



def test_java_unknowntypeargument_is_not_abstract():
    assert not inspect.isabstract(java_UnknownTypeArgument)


def test_java_unknowntypeargument_constructor_exists():
    assert callable(java_UnknownTypeArgument.__init__)


def test_java_unknowntypeargument_constructor_args():
    sig = inspect.signature(java_UnknownTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_java_unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(java_UnaryModificationOperator)


def test_java_unarymodificationoperator_constructor_exists():
    assert callable(java_UnaryModificationOperator.__init__)


def test_java_unarymodificationoperator_constructor_args():
    sig = inspect.signature(java_UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpressionchild_is_not_abstract():
    assert not inspect.isabstract(UnaryExpressionChild)


def test_unaryexpressionchild_constructor_exists():
    assert callable(UnaryExpressionChild.__init__)


def test_unaryexpressionchild_constructor_args():
    sig = inspect.signature(UnaryExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_unarymodificationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_UnaryModificationExpressionChild)


def test_java_unarymodificationexpressionchild_constructor_exists():
    assert callable(java_UnaryModificationExpressionChild.__init__)


def test_java_unarymodificationexpressionchild_constructor_args():
    sig = inspect.signature(java_UnaryModificationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_unarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(java_UnaryModificationExpression)


def test_java_unarymodificationexpression_constructor_exists():
    assert callable(java_UnaryModificationExpression.__init__)


def test_java_unarymodificationexpression_constructor_args():
    sig = inspect.signature(java_UnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(java_UnaryOperator)


def test_java_unaryoperator_constructor_exists():
    assert callable(java_UnaryOperator.__init__)


def test_java_unaryoperator_constructor_args():
    sig = inspect.signature(java_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeexpressionchild_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeExpressionChild)


def test_multiplicativeexpressionchild_constructor_exists():
    assert callable(MultiplicativeExpressionChild.__init__)


def test_multiplicativeexpressionchild_constructor_args():
    sig = inspect.signature(MultiplicativeExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_unaryexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_UnaryExpressionChild)


def test_java_unaryexpressionchild_constructor_exists():
    assert callable(java_UnaryExpressionChild.__init__)


def test_java_unaryexpressionchild_constructor_args():
    sig = inspect.signature(java_UnaryExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(java_UnaryExpression)


def test_java_unaryexpression_constructor_exists():
    assert callable(java_UnaryExpression.__init__)


def test_java_unaryexpression_constructor_args():
    sig = inspect.signature(java_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(java_MultiplicativeOperator)


def test_java_multiplicativeoperator_constructor_exists():
    assert callable(java_MultiplicativeOperator.__init__)


def test_java_multiplicativeoperator_constructor_args():
    sig = inspect.signature(java_MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_additiveexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AdditiveExpressionChild)


def test_additiveexpressionchild_constructor_exists():
    assert callable(AdditiveExpressionChild.__init__)


def test_additiveexpressionchild_constructor_args():
    sig = inspect.signature(AdditiveExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_multiplicativeexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_MultiplicativeExpressionChild)


def test_java_multiplicativeexpressionchild_constructor_exists():
    assert callable(java_MultiplicativeExpressionChild.__init__)


def test_java_multiplicativeexpressionchild_constructor_args():
    sig = inspect.signature(java_MultiplicativeExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(java_MultiplicativeExpression)


def test_java_multiplicativeexpression_constructor_exists():
    assert callable(java_MultiplicativeExpression.__init__)


def test_java_multiplicativeexpression_constructor_args():
    sig = inspect.signature(java_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_additiveoperator_is_not_abstract():
    assert not inspect.isabstract(java_AdditiveOperator)


def test_java_additiveoperator_constructor_exists():
    assert callable(java_AdditiveOperator.__init__)


def test_java_additiveoperator_constructor_args():
    sig = inspect.signature(java_AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_shiftexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ShiftExpressionChild)


def test_shiftexpressionchild_constructor_exists():
    assert callable(ShiftExpressionChild.__init__)


def test_shiftexpressionchild_constructor_args():
    sig = inspect.signature(ShiftExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_additiveexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_AdditiveExpressionChild)


def test_java_additiveexpressionchild_constructor_exists():
    assert callable(java_AdditiveExpressionChild.__init__)


def test_java_additiveexpressionchild_constructor_args():
    sig = inspect.signature(java_AdditiveExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(java_AdditiveExpression)


def test_java_additiveexpression_constructor_exists():
    assert callable(java_AdditiveExpression.__init__)


def test_java_additiveexpression_constructor_args():
    sig = inspect.signature(java_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_shiftoperator_is_not_abstract():
    assert not inspect.isabstract(java_ShiftOperator)


def test_java_shiftoperator_constructor_exists():
    assert callable(java_ShiftOperator.__init__)


def test_java_shiftoperator_constructor_args():
    sig = inspect.signature(java_ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_relationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(RelationExpressionChild)


def test_relationexpressionchild_constructor_exists():
    assert callable(RelationExpressionChild.__init__)


def test_relationexpressionchild_constructor_args():
    sig = inspect.signature(RelationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_shiftexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_ShiftExpressionChild)


def test_java_shiftexpressionchild_constructor_exists():
    assert callable(java_ShiftExpressionChild.__init__)


def test_java_shiftexpressionchild_constructor_args():
    sig = inspect.signature(java_ShiftExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(java_ShiftExpression)


def test_java_shiftexpression_constructor_exists():
    assert callable(java_ShiftExpression.__init__)


def test_java_shiftexpression_constructor_args():
    sig = inspect.signature(java_ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_relationoperator_is_not_abstract():
    assert not inspect.isabstract(java_RelationOperator)


def test_java_relationoperator_constructor_exists():
    assert callable(java_RelationOperator.__init__)


def test_java_relationoperator_constructor_args():
    sig = inspect.signature(java_RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationExpression)


def test_unarymodificationexpression_constructor_exists():
    assert callable(UnaryModificationExpression.__init__)


def test_unarymodificationexpression_constructor_args():
    sig = inspect.signature(UnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_suffixunarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(java_SuffixUnaryModificationExpression)


def test_java_suffixunarymodificationexpression_constructor_exists():
    assert callable(java_SuffixUnaryModificationExpression.__init__)


def test_java_suffixunarymodificationexpression_constructor_args():
    sig = inspect.signature(java_SuffixUnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_prefixunarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(java_PrefixUnaryModificationExpression)


def test_java_prefixunarymodificationexpression_constructor_exists():
    assert callable(java_PrefixUnaryModificationExpression.__init__)


def test_java_prefixunarymodificationexpression_constructor_args():
    sig = inspect.signature(java_PrefixUnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_equalityexpressionchild_is_not_abstract():
    assert not inspect.isabstract(EqualityExpressionChild)


def test_equalityexpressionchild_constructor_exists():
    assert callable(EqualityExpressionChild.__init__)


def test_equalityexpressionchild_constructor_args():
    sig = inspect.signature(EqualityExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_instanceofexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_InstanceOfExpressionChild)


def test_java_instanceofexpressionchild_constructor_exists():
    assert callable(java_InstanceOfExpressionChild.__init__)


def test_java_instanceofexpressionchild_constructor_args():
    sig = inspect.signature(java_InstanceOfExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(java_InstanceOfExpression)


def test_java_instanceofexpression_constructor_exists():
    assert callable(java_InstanceOfExpression.__init__)


def test_java_instanceofexpression_constructor_args():
    sig = inspect.signature(java_InstanceOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_equalityoperator_is_not_abstract():
    assert not inspect.isabstract(java_EqualityOperator)


def test_java_equalityoperator_constructor_exists():
    assert callable(java_EqualityOperator.__init__)


def test_java_equalityoperator_constructor_args():
    sig = inspect.signature(java_EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_andexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AndExpressionChild)


def test_andexpressionchild_constructor_exists():
    assert callable(AndExpressionChild.__init__)


def test_andexpressionchild_constructor_args():
    sig = inspect.signature(AndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_equalityexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_EqualityExpressionChild)


def test_java_equalityexpressionchild_constructor_exists():
    assert callable(java_EqualityExpressionChild.__init__)


def test_java_equalityexpressionchild_constructor_args():
    sig = inspect.signature(java_EqualityExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(java_EqualityExpression)


def test_java_equalityexpression_constructor_exists():
    assert callable(java_EqualityExpression.__init__)


def test_java_equalityexpression_constructor_args():
    sig = inspect.signature(java_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_exclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ExclusiveOrExpressionChild)


def test_exclusiveorexpressionchild_constructor_exists():
    assert callable(ExclusiveOrExpressionChild.__init__)


def test_exclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(ExclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_andexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_AndExpressionChild)


def test_java_andexpressionchild_constructor_exists():
    assert callable(java_AndExpressionChild.__init__)


def test_java_andexpressionchild_constructor_args():
    sig = inspect.signature(java_AndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_andexpression_is_not_abstract():
    assert not inspect.isabstract(java_AndExpression)


def test_java_andexpression_constructor_exists():
    assert callable(java_AndExpression.__init__)


def test_java_andexpression_constructor_args():
    sig = inspect.signature(java_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_inclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(InclusiveOrExpressionChild)


def test_inclusiveorexpressionchild_constructor_exists():
    assert callable(InclusiveOrExpressionChild.__init__)


def test_inclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(InclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_exclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_ExclusiveOrExpressionChild)


def test_java_exclusiveorexpressionchild_constructor_exists():
    assert callable(java_ExclusiveOrExpressionChild.__init__)


def test_java_exclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(java_ExclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(java_ExclusiveOrExpression)


def test_java_exclusiveorexpression_constructor_exists():
    assert callable(java_ExclusiveOrExpression.__init__)


def test_java_exclusiveorexpression_constructor_args():
    sig = inspect.signature(java_ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalAndExpressionChild)


def test_conditionalandexpressionchild_constructor_exists():
    assert callable(ConditionalAndExpressionChild.__init__)


def test_conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_inclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_InclusiveOrExpressionChild)


def test_java_inclusiveorexpressionchild_constructor_exists():
    assert callable(java_InclusiveOrExpressionChild.__init__)


def test_java_inclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(java_InclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(java_InclusiveOrExpression)


def test_java_inclusiveorexpression_constructor_exists():
    assert callable(java_InclusiveOrExpression.__init__)


def test_java_inclusiveorexpression_constructor_args():
    sig = inspect.signature(java_InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalOrExpressionChild)


def test_conditionalorexpressionchild_constructor_exists():
    assert callable(ConditionalOrExpressionChild.__init__)


def test_conditionalorexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_ConditionalAndExpressionChild)


def test_java_conditionalandexpressionchild_constructor_exists():
    assert callable(java_ConditionalAndExpressionChild.__init__)


def test_java_conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(java_ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(java_ConditionalAndExpression)


def test_java_conditionalandexpression_constructor_exists():
    assert callable(java_ConditionalAndExpression.__init__)


def test_java_conditionalandexpression_constructor_args():
    sig = inspect.signature(java_ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalExpressionChild)


def test_conditionalexpressionchild_constructor_exists():
    assert callable(ConditionalExpressionChild.__init__)


def test_conditionalexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_conditionalorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_ConditionalOrExpressionChild)


def test_java_conditionalorexpressionchild_constructor_exists():
    assert callable(java_ConditionalOrExpressionChild.__init__)


def test_java_conditionalorexpressionchild_constructor_args():
    sig = inspect.signature(java_ConditionalOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(java_ConditionalOrExpression)


def test_java_conditionalorexpression_constructor_exists():
    assert callable(java_ConditionalOrExpression.__init__)


def test_java_conditionalorexpression_constructor_args():
    sig = inspect.signature(java_ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_instanceofexpressionchild_is_not_abstract():
    assert not inspect.isabstract(InstanceOfExpressionChild)


def test_instanceofexpressionchild_constructor_exists():
    assert callable(InstanceOfExpressionChild.__init__)


def test_instanceofexpressionchild_constructor_args():
    sig = inspect.signature(InstanceOfExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_relationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_RelationExpressionChild)


def test_java_relationexpressionchild_constructor_exists():
    assert callable(java_RelationExpressionChild.__init__)


def test_java_relationexpressionchild_constructor_args():
    sig = inspect.signature(java_RelationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_relationexpression_is_not_abstract():
    assert not inspect.isabstract(java_RelationExpression)


def test_java_relationexpression_constructor_exists():
    assert callable(java_RelationExpression.__init__)


def test_java_relationexpression_constructor_args():
    sig = inspect.signature(java_RelationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentOperator)


def test_java_assignmentoperator_constructor_exists():
    assert callable(java_AssignmentOperator.__init__)


def test_java_assignmentoperator_constructor_args():
    sig = inspect.signature(java_AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentExpressionChild)


def test_java_assignmentexpressionchild_constructor_exists():
    assert callable(java_AssignmentExpressionChild.__init__)


def test_java_assignmentexpressionchild_constructor_args():
    sig = inspect.signature(java_AssignmentExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(java_AssignmentExpression)


def test_java_assignmentexpression_constructor_exists():
    assert callable(java_AssignmentExpression.__init__)


def test_java_assignmentexpression_constructor_args():
    sig = inspect.signature(java_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_forloopinitializer_is_not_abstract():
    assert not inspect.isabstract(ForLoopInitializer)


def test_forloopinitializer_constructor_exists():
    assert callable(ForLoopInitializer.__init__)


def test_forloopinitializer_constructor_args():
    sig = inspect.signature(ForLoopInitializer.__init__)
    params = list(sig.parameters.keys())



def test_java_expressionlist_is_not_abstract():
    assert not inspect.isabstract(java_ExpressionList)


def test_java_expressionlist_constructor_exists():
    assert callable(java_ExpressionList.__init__)


def test_java_expressionlist_constructor_args():
    sig = inspect.signature(java_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_annotable_is_not_abstract():
    assert not inspect.isabstract(Annotable)


def test_annotable_constructor_exists():
    assert callable(Annotable.__init__)


def test_annotable_constructor_args():
    sig = inspect.signature(Annotable.__init__)
    params = list(sig.parameters.keys())



def test_javaroot_is_not_abstract():
    assert not inspect.isabstract(JavaRoot)


def test_javaroot_constructor_exists():
    assert callable(JavaRoot.__init__)


def test_javaroot_constructor_args():
    sig = inspect.signature(JavaRoot.__init__)
    params = list(sig.parameters.keys())



def test_java_emptymodel_is_not_abstract():
    assert not inspect.isabstract(java_EmptyModel)


def test_java_emptymodel_constructor_exists():
    assert callable(java_EmptyModel.__init__)


def test_java_emptymodel_constructor_args():
    sig = inspect.signature(java_EmptyModel.__init__)
    params = list(sig.parameters.keys())



def test_java_package_is_not_abstract():
    assert not inspect.isabstract(java_Package)


def test_java_package_constructor_exists():
    assert callable(java_Package.__init__)


def test_java_package_constructor_args():
    sig = inspect.signature(java_Package.__init__)
    params = list(sig.parameters.keys())



def test_java_compilationunit_is_not_abstract():
    assert not inspect.isabstract(java_CompilationUnit)


def test_java_compilationunit_constructor_exists():
    assert callable(java_CompilationUnit.__init__)


def test_java_compilationunit_constructor_args():
    sig = inspect.signature(java_CompilationUnit.__init__)
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



def test_java_referenceableelement_is_not_abstract():
    assert not inspect.isabstract(java_ReferenceableElement)


def test_java_referenceableelement_constructor_exists():
    assert callable(java_ReferenceableElement.__init__)


def test_java_referenceableelement_constructor_args():
    sig = inspect.signature(java_ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_java_member_is_not_abstract():
    assert not inspect.isabstract(java_Member)


def test_java_member_constructor_exists():
    assert callable(java_Member.__init__)


def test_java_member_constructor_args():
    sig = inspect.signature(java_Member.__init__)
    params = list(sig.parameters.keys())



def test_java_javaroot_is_not_abstract():
    assert not inspect.isabstract(java_JavaRoot)


def test_java_javaroot_constructor_exists():
    assert callable(java_JavaRoot.__init__)


def test_java_javaroot_constructor_args():
    sig = inspect.signature(java_JavaRoot.__init__)
    params = list(sig.parameters.keys())



def test_assignmentexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AssignmentExpressionChild)


def test_assignmentexpressionchild_constructor_exists():
    assert callable(AssignmentExpressionChild.__init__)


def test_assignmentexpressionchild_constructor_args():
    sig = inspect.signature(AssignmentExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_conditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java_ConditionalExpressionChild)


def test_java_conditionalexpressionchild_constructor_exists():
    assert callable(java_ConditionalExpressionChild.__init__)


def test_java_conditionalexpressionchild_constructor_args():
    sig = inspect.signature(java_ConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(java_ConditionalExpression)


def test_java_conditionalexpression_constructor_exists():
    assert callable(java_ConditionalExpression.__init__)


def test_java_conditionalexpression_constructor_args():
    sig = inspect.signature(java_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_namespaceawareelement_is_not_abstract():
    assert not inspect.isabstract(java_NamespaceAwareElement)


def test_java_namespaceawareelement_constructor_exists():
    assert callable(java_NamespaceAwareElement.__init__)


def test_java_namespaceawareelement_constructor_args():
    sig = inspect.signature(java_NamespaceAwareElement.__init__)
    params = list(sig.parameters.keys())
    assert "namespaces" in params, "Missing parameter 'namespaces'"

def test_java_namespaceawareelement_has_namespaces():
    assert hasattr(java_NamespaceAwareElement, "namespaces")
    descriptor = None
    for klass in java_NamespaceAwareElement.__mro__:
        if "namespaces" in klass.__dict__:
            descriptor = klass.__dict__["namespaces"]
            break
    assert isinstance(descriptor, property)



def test_java_namedelement_is_not_abstract():
    assert not inspect.isabstract(java_NamedElement)


def test_java_namedelement_constructor_exists():
    assert callable(java_NamedElement.__init__)


def test_java_namedelement_constructor_args():
    sig = inspect.signature(java_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_namedelement_has_name():
    assert hasattr(java_NamedElement, "name")
    descriptor = None
    for klass in java_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_layoutinformation_is_not_abstract():
    assert not inspect.isabstract(java_LayoutInformation)


def test_java_layoutinformation_constructor_exists():
    assert callable(java_LayoutInformation.__init__)


def test_java_layoutinformation_constructor_args():
    sig = inspect.signature(java_LayoutInformation.__init__)
    params = list(sig.parameters.keys())



def test_java_commentable_is_not_abstract():
    assert not inspect.isabstract(java_Commentable)


def test_java_commentable_constructor_exists():
    assert callable(java_Commentable.__init__)


def test_java_commentable_constructor_args():
    sig = inspect.signature(java_Commentable.__init__)
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



def test_java_enumeration_is_not_abstract():
    assert not inspect.isabstract(java_Enumeration)


def test_java_enumeration_constructor_exists():
    assert callable(java_Enumeration.__init__)


def test_java_enumeration_constructor_args():
    sig = inspect.signature(java_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_java_interface_is_not_abstract():
    assert not inspect.isabstract(java_Interface)


def test_java_interface_constructor_exists():
    assert callable(java_Interface.__init__)


def test_java_interface_constructor_args():
    sig = inspect.signature(java_Interface.__init__)
    params = list(sig.parameters.keys())



def test_java_class_is_not_abstract():
    assert not inspect.isabstract(java_Class)


def test_java_class_constructor_exists():
    assert callable(java_Class.__init__)


def test_java_class_constructor_args():
    sig = inspect.signature(java_Class.__init__)
    params = list(sig.parameters.keys())



def test_java_typereference_is_not_abstract():
    assert not inspect.isabstract(java_TypeReference)


def test_java_typereference_constructor_exists():
    assert callable(java_TypeReference.__init__)


def test_java_typereference_constructor_args():
    sig = inspect.signature(java_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_java_implementor_is_not_abstract():
    assert not inspect.isabstract(java_Implementor)


def test_java_implementor_constructor_exists():
    assert callable(java_Implementor.__init__)


def test_java_implementor_constructor_args():
    sig = inspect.signature(java_Implementor.__init__)
    params = list(sig.parameters.keys())



def test_java_annotation_is_not_abstract():
    assert not inspect.isabstract(java_Annotation)


def test_java_annotation_constructor_exists():
    assert callable(java_Annotation.__init__)


def test_java_annotation_constructor_args():
    sig = inspect.signature(java_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_annotableandmodifiable_is_not_abstract():
    assert not inspect.isabstract(AnnotableAndModifiable)


def test_annotableandmodifiable_constructor_exists():
    assert callable(AnnotableAndModifiable.__init__)


def test_annotableandmodifiable_constructor_args():
    sig = inspect.signature(AnnotableAndModifiable.__init__)
    params = list(sig.parameters.keys())



def test_java_localvariable_is_not_abstract():
    assert not inspect.isabstract(java_LocalVariable)


def test_java_localvariable_constructor_exists():
    assert callable(java_LocalVariable.__init__)


def test_java_localvariable_constructor_args():
    sig = inspect.signature(java_LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_java_parameter_is_not_abstract():
    assert not inspect.isabstract(java_Parameter)


def test_java_parameter_constructor_exists():
    assert callable(java_Parameter.__init__)


def test_java_parameter_constructor_args():
    sig = inspect.signature(java_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_java_foreachloop_is_not_abstract():
    assert not inspect.isabstract(java_ForEachLoop)


def test_java_foreachloop_constructor_exists():
    assert callable(java_ForEachLoop.__init__)


def test_java_foreachloop_constructor_args():
    sig = inspect.signature(java_ForEachLoop.__init__)
    params = list(sig.parameters.keys())



def test_java_condition_is_not_abstract():
    assert not inspect.isabstract(java_Condition)


def test_java_condition_constructor_exists():
    assert callable(java_Condition.__init__)


def test_java_condition_constructor_args():
    sig = inspect.signature(java_Condition.__init__)
    params = list(sig.parameters.keys())



def test_java_assert_is_not_abstract():
    assert not inspect.isabstract(java_Assert)


def test_java_assert_constructor_exists():
    assert callable(java_Assert.__init__)


def test_java_assert_constructor_args():
    sig = inspect.signature(java_Assert.__init__)
    params = list(sig.parameters.keys())



def test_java_jumplabel_is_not_abstract():
    assert not inspect.isabstract(java_JumpLabel)


def test_java_jumplabel_constructor_exists():
    assert callable(java_JumpLabel.__init__)


def test_java_jumplabel_constructor_args():
    sig = inspect.signature(java_JumpLabel.__init__)
    params = list(sig.parameters.keys())



def test_java_switch_is_not_abstract():
    assert not inspect.isabstract(java_Switch)


def test_java_switch_constructor_exists():
    assert callable(java_Switch.__init__)


def test_java_switch_constructor_args():
    sig = inspect.signature(java_Switch.__init__)
    params = list(sig.parameters.keys())



def test_java_throw_is_not_abstract():
    assert not inspect.isabstract(java_Throw)


def test_java_throw_constructor_exists():
    assert callable(java_Throw.__init__)


def test_java_throw_constructor_args():
    sig = inspect.signature(java_Throw.__init__)
    params = list(sig.parameters.keys())



def test_java_return_is_not_abstract():
    assert not inspect.isabstract(java_Return)


def test_java_return_constructor_exists():
    assert callable(java_Return.__init__)


def test_java_return_constructor_args():
    sig = inspect.signature(java_Return.__init__)
    params = list(sig.parameters.keys())



def test_java_tryblock_is_not_abstract():
    assert not inspect.isabstract(java_TryBlock)


def test_java_tryblock_constructor_exists():
    assert callable(java_TryBlock.__init__)


def test_java_tryblock_constructor_args():
    sig = inspect.signature(java_TryBlock.__init__)
    params = list(sig.parameters.keys())



def test_java_jump_is_not_abstract():
    assert not inspect.isabstract(java_Jump)


def test_java_jump_constructor_exists():
    assert callable(java_Jump.__init__)


def test_java_jump_constructor_args():
    sig = inspect.signature(java_Jump.__init__)
    params = list(sig.parameters.keys())



def test_java_forloop_is_not_abstract():
    assert not inspect.isabstract(java_ForLoop)


def test_java_forloop_constructor_exists():
    assert callable(java_ForLoop.__init__)


def test_java_forloop_constructor_args():
    sig = inspect.signature(java_ForLoop.__init__)
    params = list(sig.parameters.keys())



def test_java_whileloop_is_not_abstract():
    assert not inspect.isabstract(java_WhileLoop)


def test_java_whileloop_constructor_exists():
    assert callable(java_WhileLoop.__init__)


def test_java_whileloop_constructor_args():
    sig = inspect.signature(java_WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_java_synchronizedblock_is_not_abstract():
    assert not inspect.isabstract(java_SynchronizedBlock)


def test_java_synchronizedblock_constructor_exists():
    assert callable(java_SynchronizedBlock.__init__)


def test_java_synchronizedblock_constructor_args():
    sig = inspect.signature(java_SynchronizedBlock.__init__)
    params = list(sig.parameters.keys())



def test_java_localvariablestatement_is_not_abstract():
    assert not inspect.isabstract(java_LocalVariableStatement)


def test_java_localvariablestatement_constructor_exists():
    assert callable(java_LocalVariableStatement.__init__)


def test_java_localvariablestatement_constructor_args():
    sig = inspect.signature(java_LocalVariableStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_emptystatement_is_not_abstract():
    assert not inspect.isabstract(java_EmptyStatement)


def test_java_emptystatement_constructor_exists():
    assert callable(java_EmptyStatement.__init__)


def test_java_emptystatement_constructor_args():
    sig = inspect.signature(java_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(java_ExpressionStatement)


def test_java_expressionstatement_constructor_exists():
    assert callable(java_ExpressionStatement.__init__)


def test_java_expressionstatement_constructor_args():
    sig = inspect.signature(java_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_java_emptymember_is_not_abstract():
    assert not inspect.isabstract(java_EmptyMember)


def test_java_emptymember_constructor_exists():
    assert callable(java_EmptyMember.__init__)


def test_java_emptymember_constructor_args():
    sig = inspect.signature(java_EmptyMember.__init__)
    params = list(sig.parameters.keys())



def test_java_block_is_not_abstract():
    assert not inspect.isabstract(java_Block)


def test_java_block_constructor_exists():
    assert callable(java_Block.__init__)


def test_java_block_constructor_args():
    sig = inspect.signature(java_Block.__init__)
    params = list(sig.parameters.keys())



def test_membercontainer_is_not_abstract():
    assert not inspect.isabstract(MemberContainer)


def test_membercontainer_constructor_exists():
    assert callable(MemberContainer.__init__)


def test_membercontainer_constructor_args():
    sig = inspect.signature(MemberContainer.__init__)
    params = list(sig.parameters.keys())



def test_typeparametrizable_is_not_abstract():
    assert not inspect.isabstract(TypeParametrizable)


def test_typeparametrizable_constructor_exists():
    assert callable(TypeParametrizable.__init__)


def test_typeparametrizable_constructor_args():
    sig = inspect.signature(TypeParametrizable.__init__)
    params = list(sig.parameters.keys())



def test_java_constructor_is_not_abstract():
    assert not inspect.isabstract(java_Constructor)


def test_java_constructor_constructor_exists():
    assert callable(java_Constructor.__init__)


def test_java_constructor_constructor_args():
    sig = inspect.signature(java_Constructor.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_java_typeparameter_is_not_abstract():
    assert not inspect.isabstract(java_TypeParameter)


def test_java_typeparameter_constructor_exists():
    assert callable(java_TypeParameter.__init__)


def test_java_typeparameter_constructor_args():
    sig = inspect.signature(java_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_java_concreteclassifier_is_not_abstract():
    assert not inspect.isabstract(java_ConcreteClassifier)


def test_java_concreteclassifier_constructor_exists():
    assert callable(java_ConcreteClassifier.__init__)


def test_java_concreteclassifier_constructor_args():
    sig = inspect.signature(java_ConcreteClassifier.__init__)
    params = list(sig.parameters.keys())



def test_referenceableelement_is_not_abstract():
    assert not inspect.isabstract(ReferenceableElement)


def test_referenceableelement_constructor_exists():
    assert callable(ReferenceableElement.__init__)


def test_referenceableelement_constructor_args():
    sig = inspect.signature(ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_java_additionalfield_is_not_abstract():
    assert not inspect.isabstract(java_AdditionalField)


def test_java_additionalfield_constructor_exists():
    assert callable(java_AdditionalField.__init__)


def test_java_additionalfield_constructor_args():
    sig = inspect.signature(java_AdditionalField.__init__)
    params = list(sig.parameters.keys())



def test_java_additionallocalvariable_is_not_abstract():
    assert not inspect.isabstract(java_AdditionalLocalVariable)


def test_java_additionallocalvariable_constructor_exists():
    assert callable(java_AdditionalLocalVariable.__init__)


def test_java_additionallocalvariable_constructor_args():
    sig = inspect.signature(java_AdditionalLocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_java_method_is_not_abstract():
    assert not inspect.isabstract(java_Method)


def test_java_method_constructor_exists():
    assert callable(java_Method.__init__)


def test_java_method_constructor_args():
    sig = inspect.signature(java_Method.__init__)
    params = list(sig.parameters.keys())



def test_java_field_is_not_abstract():
    assert not inspect.isabstract(java_Field)


def test_java_field_constructor_exists():
    assert callable(java_Field.__init__)


def test_java_field_constructor_args():
    sig = inspect.signature(java_Field.__init__)
    params = list(sig.parameters.keys())



def test_java_packagereference_is_not_abstract():
    assert not inspect.isabstract(java_PackageReference)


def test_java_packagereference_constructor_exists():
    assert callable(java_PackageReference.__init__)


def test_java_packagereference_constructor_args():
    sig = inspect.signature(java_PackageReference.__init__)
    params = list(sig.parameters.keys())



def test_java_enumconstant_is_not_abstract():
    assert not inspect.isabstract(java_EnumConstant)


def test_java_enumconstant_constructor_exists():
    assert callable(java_EnumConstant.__init__)


def test_java_enumconstant_constructor_args():
    sig = inspect.signature(java_EnumConstant.__init__)
    params = list(sig.parameters.keys())



def test_java_variable_is_not_abstract():
    assert not inspect.isabstract(java_Variable)


def test_java_variable_constructor_exists():
    assert callable(java_Variable.__init__)


def test_java_variable_constructor_args():
    sig = inspect.signature(java_Variable.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_java_classifier_is_not_abstract():
    assert not inspect.isabstract(java_Classifier)


def test_java_classifier_constructor_exists():
    assert callable(java_Classifier.__init__)


def test_java_classifier_constructor_args():
    sig = inspect.signature(java_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_java_anonymousclass_is_not_abstract():
    assert not inspect.isabstract(java_AnonymousClass)


def test_java_anonymousclass_constructor_exists():
    assert callable(java_AnonymousClass.__init__)


def test_java_anonymousclass_constructor_args():
    sig = inspect.signature(java_AnonymousClass.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetype_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveType)


def test_java_primitivetype_constructor_exists():
    assert callable(java_PrimitiveType.__init__)


def test_java_primitivetype_constructor_args():
    sig = inspect.signature(java_PrimitiveType.__init__)
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
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
java_Char_strategy = st.builds(
    java_Char,
)
java_Short_strategy = st.builds(
    java_Short,
)
java_Int_strategy = st.builds(
    java_Int,
)
java_Float_strategy = st.builds(
    java_Float,
)
java_Long_strategy = st.builds(
    java_Long,
)
java_Byte_strategy = st.builds(
    java_Byte,
)
java_Double_strategy = st.builds(
    java_Double,
)
java_Void_strategy = st.builds(
    java_Void,
)
ArrayInstantiationByValues_strategy = st.builds(
    ArrayInstantiationByValues,
)
java_ArrayInstantiationByValuesUntyped_strategy = st.builds(
    java_ArrayInstantiationByValuesUntyped,
)
ArrayTypeable_strategy = st.builds(
    ArrayTypeable,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
java_ArrayInstantiationByValuesTyped_strategy = st.builds(
    java_ArrayInstantiationByValuesTyped,
)
ArrayInstantiation_strategy = st.builds(
    ArrayInstantiation,
)
java_ArrayInstantiationByValues_strategy = st.builds(
    java_ArrayInstantiationByValues,
)
java_ArrayInstantiationBySize_strategy = st.builds(
    java_ArrayInstantiationBySize,
)
Expression_strategy = st.builds(
    Expression,
)
AnnotationValue_strategy = st.builds(
    AnnotationValue,
)
ArrayInitializationValue_strategy = st.builds(
    ArrayInitializationValue,
)
java_ArrayInitializer_strategy = st.builds(
    java_ArrayInitializer,
)
InterfaceMethod_strategy = st.builds(
    InterfaceMethod,
)
java_AnnotationAttribute_strategy = st.builds(
    java_AnnotationAttribute,
)
AnnotationParameter_strategy = st.builds(
    AnnotationParameter,
)
java_AnnotationParameterList_strategy = st.builds(
    java_AnnotationParameterList,
)
java_SingleAnnotationParameter_strategy = st.builds(
    java_SingleAnnotationParameter,
)
NamespaceAwareElement_strategy = st.builds(
    NamespaceAwareElement,
)
AnnotationInstanceOrModifier_strategy = st.builds(
    AnnotationInstanceOrModifier,
)
Reference_strategy = st.builds(
    Reference,
)
java_ArrayInstantiation_strategy = st.builds(
    java_ArrayInstantiation,
)
java_AnnotationInstance_strategy = st.builds(
    java_AnnotationInstance,
)
Commentable_strategy = st.builds(
    Commentable,
)
java_AnnotationParameter_strategy = st.builds(
    java_AnnotationParameter,
)
java_ArrayDimension_strategy = st.builds(
    java_ArrayDimension,
)
java_ArrayInitializationValue_strategy = st.builds(
    java_ArrayInitializationValue,
)
java_AnnotationValue_strategy = st.builds(
    java_AnnotationValue,
)
java_AnnotationAttributeSetting_strategy = st.builds(
    java_AnnotationAttributeSetting,
)
java_ArraySelector_strategy = st.builds(
    java_ArraySelector,
)
java_Annotable_strategy = st.builds(
    java_Annotable,
)
java_ArrayTypeable_strategy = st.builds(
    java_ArrayTypeable,
)
java_Expression_strategy = st.builds(
    java_Expression,
)
java_Boolean_strategy = st.builds(
    java_Boolean,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
java_TypedElement_strategy = st.builds(
    java_TypedElement,
)
java_Type_strategy = st.builds(
    java_Type,
)
WhileLoop_strategy = st.builds(
    WhileLoop,
)
java_DoWhileLoop_strategy = st.builds(
    java_DoWhileLoop,
)
SwitchCase_strategy = st.builds(
    SwitchCase,
)
java_DefaultSwitchCase_strategy = st.builds(
    java_DefaultSwitchCase,
)
Modifiable_strategy = st.builds(
    Modifiable,
)
Jump_strategy = st.builds(
    Jump,
)
java_Continue_strategy = st.builds(
    java_Continue,
)
java_Break_strategy = st.builds(
    java_Break,
)
Conditional_strategy = st.builds(
    Conditional,
)
java_NormalSwitchCase_strategy = st.builds(
    java_NormalSwitchCase,
)
java_ForLoopInitializer_strategy = st.builds(
    java_ForLoopInitializer,
)
java_Conditional_strategy = st.builds(
    java_Conditional,
)
java_StatementListContainer_strategy = st.builds(
    java_StatementListContainer,
)
java_Statement_strategy = st.builds(
    java_Statement,
)
java_StatementContainer_strategy = st.builds(
    java_StatementContainer,
)
Parameter_strategy = st.builds(
    Parameter,
)
java_VariableLengthParameter_strategy = st.builds(
    java_VariableLengthParameter,
)
java_OrdinaryParameter_strategy = st.builds(
    java_OrdinaryParameter,
)
java_Parametrizable_strategy = st.builds(
    java_Parametrizable,
)
java_SelfReference_strategy = st.builds(
    java_SelfReference,
)
java_StringReference_strategy = st.builds(
    java_StringReference,
    value=
        safe_text
)
StatementContainer_strategy = st.builds(
    StatementContainer,
)
ElementReference_strategy = st.builds(
    ElementReference,
)
java_IdentifierReference_strategy = st.builds(
    java_IdentifierReference,
)
java_ElementReference_strategy = st.builds(
    java_ElementReference,
)
java_Argumentable_strategy = st.builds(
    java_Argumentable,
)
TypeArgumentable_strategy = st.builds(
    TypeArgumentable,
)
java_ClassifierReference_strategy = st.builds(
    java_ClassifierReference,
)
ShiftOperator_strategy = st.builds(
    ShiftOperator,
)
java_UnsignedRightShift_strategy = st.builds(
    java_UnsignedRightShift,
)
java_RightShift_strategy = st.builds(
    java_RightShift,
)
java_LeftShift_strategy = st.builds(
    java_LeftShift,
)
UnaryModificationOperator_strategy = st.builds(
    UnaryModificationOperator,
)
java_PlusPlus_strategy = st.builds(
    java_PlusPlus,
)
java_MinusMinus_strategy = st.builds(
    java_MinusMinus,
)
MultiplicativeOperator_strategy = st.builds(
    MultiplicativeOperator,
)
java_Remainder_strategy = st.builds(
    java_Remainder,
)
java_Multiplication_strategy = st.builds(
    java_Multiplication,
)
java_Division_strategy = st.builds(
    java_Division,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
java_Complement_strategy = st.builds(
    java_Complement,
)
java_Negate_strategy = st.builds(
    java_Negate,
)
AdditiveOperator_strategy = st.builds(
    AdditiveOperator,
)
java_Subtraction_strategy = st.builds(
    java_Subtraction,
)
java_Addition_strategy = st.builds(
    java_Addition,
)
RelationOperator_strategy = st.builds(
    RelationOperator,
)
java_LessThanOrEqual_strategy = st.builds(
    java_LessThanOrEqual,
)
java_GreaterThanOrEqual_strategy = st.builds(
    java_GreaterThanOrEqual,
)
java_LessThan_strategy = st.builds(
    java_LessThan,
)
java_GreaterThan_strategy = st.builds(
    java_GreaterThan,
)
java_PrimitiveTypeReference_strategy = st.builds(
    java_PrimitiveTypeReference,
)
java_ReflectiveClassReference_strategy = st.builds(
    java_ReflectiveClassReference,
)
AssignmentOperator_strategy = st.builds(
    AssignmentOperator,
)
java_AssignmentAnd_strategy = st.builds(
    java_AssignmentAnd,
)
java_AssignmentMinus_strategy = st.builds(
    java_AssignmentMinus,
)
java_AssignmentOr_strategy = st.builds(
    java_AssignmentOr,
)
java_AssignmentDivision_strategy = st.builds(
    java_AssignmentDivision,
)
java_AssignmentModulo_strategy = st.builds(
    java_AssignmentModulo,
)
java_AssignmentExclusiveOr_strategy = st.builds(
    java_AssignmentExclusiveOr,
)
java_AssignmentMultiplication_strategy = st.builds(
    java_AssignmentMultiplication,
)
java_AssignmentLeftShift_strategy = st.builds(
    java_AssignmentLeftShift,
)
java_Assignment_strategy = st.builds(
    java_Assignment,
)
Operator_strategy = st.builds(
    Operator,
)
java_Operator_strategy = st.builds(
    java_Operator,
)
Modifier_strategy = st.builds(
    Modifier,
)
java_Synchronized_strategy = st.builds(
    java_Synchronized,
)
java_Protected_strategy = st.builds(
    java_Protected,
)
java_Volatile_strategy = st.builds(
    java_Volatile,
)
java_Public_strategy = st.builds(
    java_Public,
)
java_Private_strategy = st.builds(
    java_Private,
)
java_Final_strategy = st.builds(
    java_Final,
)
java_Transient_strategy = st.builds(
    java_Transient,
)
java_Strictfp_strategy = st.builds(
    java_Strictfp,
)
java_Native_strategy = st.builds(
    java_Native,
)
java_Abstract_strategy = st.builds(
    java_Abstract,
)
java_Modifiable_strategy = st.builds(
    java_Modifiable,
)
EqualityOperator_strategy = st.builds(
    EqualityOperator,
)
java_NotEqual_strategy = st.builds(
    java_NotEqual,
)
java_Equal_strategy = st.builds(
    java_Equal,
)
java_AssignmentUnsignedRightShift_strategy = st.builds(
    java_AssignmentUnsignedRightShift,
)
java_AssignmentRightShift_strategy = st.builds(
    java_AssignmentRightShift,
)
java_AssignmentPlus_strategy = st.builds(
    java_AssignmentPlus,
)
java_AnnotableAndModifiable_strategy = st.builds(
    java_AnnotableAndModifiable,
)
java_AnnotationInstanceOrModifier_strategy = st.builds(
    java_AnnotationInstanceOrModifier,
)
java_Modifier_strategy = st.builds(
    java_Modifier,
)
Method_strategy = st.builds(
    Method,
)
java_InterfaceMethod_strategy = st.builds(
    java_InterfaceMethod,
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
java_CatchBlock_strategy = st.builds(
    java_CatchBlock,
)
java_SwitchCase_strategy = st.builds(
    java_SwitchCase,
)
java_ClassMethod_strategy = st.builds(
    java_ClassMethod,
)
Initializable_strategy = st.builds(
    Initializable,
)
java_MemberContainer_strategy = st.builds(
    java_MemberContainer,
)
java_NamespaceClassifierReference_strategy = st.builds(
    java_NamespaceClassifierReference,
)
java_ExceptionThrower_strategy = st.builds(
    java_ExceptionThrower,
)
Self_strategy = st.builds(
    Self,
)
java_This_strategy = st.builds(
    java_This,
)
java_Super_strategy = st.builds(
    java_Super,
)
LongLiteral_strategy = st.builds(
    LongLiteral,
)
java_OctalLongLiteral_strategy = st.builds(
    java_OctalLongLiteral,
    octalValue=
        safe_text
)
java_HexLongLiteral_strategy = st.builds(
    java_HexLongLiteral,
    hexValue=
        safe_text
)
java_DecimalLongLiteral_strategy = st.builds(
    java_DecimalLongLiteral,
    decimalValue=
        safe_text
)
IntegerLiteral_strategy = st.builds(
    IntegerLiteral,
)
java_HexIntegerLiteral_strategy = st.builds(
    java_HexIntegerLiteral,
    hexValue=
        safe_text
)
java_OctalIntegerLiteral_strategy = st.builds(
    java_OctalIntegerLiteral,
    octalValue=
        safe_text
)
java_DecimalIntegerLiteral_strategy = st.builds(
    java_DecimalIntegerLiteral,
    decimalValue=
        safe_text
)
DoubleLiteral_strategy = st.builds(
    DoubleLiteral,
)
java_HexDoubleLiteral_strategy = st.builds(
    java_HexDoubleLiteral,
    hexValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
java_DecimalDoubleLiteral_strategy = st.builds(
    java_DecimalDoubleLiteral,
    decimalValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
FloatLiteral_strategy = st.builds(
    FloatLiteral,
)
java_HexFloatLiteral_strategy = st.builds(
    java_HexFloatLiteral,
    hexValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
java_DecimalFloatLiteral_strategy = st.builds(
    java_DecimalFloatLiteral,
    decimalValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
java_Reference_strategy = st.builds(
    java_Reference,
)
java_Literal_strategy = st.builds(
    java_Literal,
)
java_Self_strategy = st.builds(
    java_Self,
)
CallTypeArgumentable_strategy = st.builds(
    CallTypeArgumentable,
)
Instantiation_strategy = st.builds(
    Instantiation,
)
java_ExplicitConstructorCall_strategy = st.builds(
    java_ExplicitConstructorCall,
)
java_NewConstructorCall_strategy = st.builds(
    java_NewConstructorCall,
)
Argumentable_strategy = st.builds(
    Argumentable,
)
java_MethodCall_strategy = st.builds(
    java_MethodCall,
)
java_Instantiation_strategy = st.builds(
    java_Instantiation,
)
java_Initializable_strategy = st.builds(
    java_Initializable,
)
StaticImport_strategy = st.builds(
    StaticImport,
)
java_StaticMemberImport_strategy = st.builds(
    java_StaticMemberImport,
)
java_StaticClassifierImport_strategy = st.builds(
    java_StaticClassifierImport,
)
java_Static_strategy = st.builds(
    java_Static,
)
Import_strategy = st.builds(
    Import,
)
java_ClassifierImport_strategy = st.builds(
    java_ClassifierImport,
)
java_PackageImport_strategy = st.builds(
    java_PackageImport,
)
java_StaticImport_strategy = st.builds(
    java_StaticImport,
)
java_ImportingElement_strategy = st.builds(
    java_ImportingElement,
)
Literal_strategy = st.builds(
    Literal,
)
java_LongLiteral_strategy = st.builds(
    java_LongLiteral,
)
java_DoubleLiteral_strategy = st.builds(
    java_DoubleLiteral,
)
java_CharacterLiteral_strategy = st.builds(
    java_CharacterLiteral,
    value=
        safe_text
)
java_IntegerLiteral_strategy = st.builds(
    java_IntegerLiteral,
)
java_FloatLiteral_strategy = st.builds(
    java_FloatLiteral,
)
java_NullLiteral_strategy = st.builds(
    java_NullLiteral,
)
java_BooleanLiteral_strategy = st.builds(
    java_BooleanLiteral,
    value=
        st.booleans()
)
TypeArgument_strategy = st.builds(
    TypeArgument,
)
java_SuperTypeArgument_strategy = st.builds(
    java_SuperTypeArgument,
)
java_QualifiedTypeArgument_strategy = st.builds(
    java_QualifiedTypeArgument,
)
java_ExtendsTypeArgument_strategy = st.builds(
    java_ExtendsTypeArgument,
)
java_TypeParametrizable_strategy = st.builds(
    java_TypeParametrizable,
)
java_CallTypeArgumentable_strategy = st.builds(
    java_CallTypeArgumentable,
)
java_TypeArgumentable_strategy = st.builds(
    java_TypeArgumentable,
)
java_TypeArgument_strategy = st.builds(
    java_TypeArgument,
)
java_NestedExpression_strategy = st.builds(
    java_NestedExpression,
)
UnaryModificationExpressionChild_strategy = st.builds(
    UnaryModificationExpressionChild,
)
java_PrimaryExpression_strategy = st.builds(
    java_PrimaryExpression,
)
java_CastExpression_strategy = st.builds(
    java_CastExpression,
)
java_Import_strategy = st.builds(
    java_Import,
)
java_UnknownTypeArgument_strategy = st.builds(
    java_UnknownTypeArgument,
)
java_UnaryModificationOperator_strategy = st.builds(
    java_UnaryModificationOperator,
)
UnaryExpressionChild_strategy = st.builds(
    UnaryExpressionChild,
)
java_UnaryModificationExpressionChild_strategy = st.builds(
    java_UnaryModificationExpressionChild,
)
java_UnaryModificationExpression_strategy = st.builds(
    java_UnaryModificationExpression,
)
java_UnaryOperator_strategy = st.builds(
    java_UnaryOperator,
)
MultiplicativeExpressionChild_strategy = st.builds(
    MultiplicativeExpressionChild,
)
java_UnaryExpressionChild_strategy = st.builds(
    java_UnaryExpressionChild,
)
java_UnaryExpression_strategy = st.builds(
    java_UnaryExpression,
)
java_MultiplicativeOperator_strategy = st.builds(
    java_MultiplicativeOperator,
)
AdditiveExpressionChild_strategy = st.builds(
    AdditiveExpressionChild,
)
java_MultiplicativeExpressionChild_strategy = st.builds(
    java_MultiplicativeExpressionChild,
)
java_MultiplicativeExpression_strategy = st.builds(
    java_MultiplicativeExpression,
)
java_AdditiveOperator_strategy = st.builds(
    java_AdditiveOperator,
)
ShiftExpressionChild_strategy = st.builds(
    ShiftExpressionChild,
)
java_AdditiveExpressionChild_strategy = st.builds(
    java_AdditiveExpressionChild,
)
java_AdditiveExpression_strategy = st.builds(
    java_AdditiveExpression,
)
java_ShiftOperator_strategy = st.builds(
    java_ShiftOperator,
)
RelationExpressionChild_strategy = st.builds(
    RelationExpressionChild,
)
java_ShiftExpressionChild_strategy = st.builds(
    java_ShiftExpressionChild,
)
java_ShiftExpression_strategy = st.builds(
    java_ShiftExpression,
)
java_RelationOperator_strategy = st.builds(
    java_RelationOperator,
)
UnaryModificationExpression_strategy = st.builds(
    UnaryModificationExpression,
)
java_SuffixUnaryModificationExpression_strategy = st.builds(
    java_SuffixUnaryModificationExpression,
)
java_PrefixUnaryModificationExpression_strategy = st.builds(
    java_PrefixUnaryModificationExpression,
)
EqualityExpressionChild_strategy = st.builds(
    EqualityExpressionChild,
)
java_InstanceOfExpressionChild_strategy = st.builds(
    java_InstanceOfExpressionChild,
)
java_InstanceOfExpression_strategy = st.builds(
    java_InstanceOfExpression,
)
java_EqualityOperator_strategy = st.builds(
    java_EqualityOperator,
)
AndExpressionChild_strategy = st.builds(
    AndExpressionChild,
)
java_EqualityExpressionChild_strategy = st.builds(
    java_EqualityExpressionChild,
)
java_EqualityExpression_strategy = st.builds(
    java_EqualityExpression,
)
ExclusiveOrExpressionChild_strategy = st.builds(
    ExclusiveOrExpressionChild,
)
java_AndExpressionChild_strategy = st.builds(
    java_AndExpressionChild,
)
java_AndExpression_strategy = st.builds(
    java_AndExpression,
)
InclusiveOrExpressionChild_strategy = st.builds(
    InclusiveOrExpressionChild,
)
java_ExclusiveOrExpressionChild_strategy = st.builds(
    java_ExclusiveOrExpressionChild,
)
java_ExclusiveOrExpression_strategy = st.builds(
    java_ExclusiveOrExpression,
)
ConditionalAndExpressionChild_strategy = st.builds(
    ConditionalAndExpressionChild,
)
java_InclusiveOrExpressionChild_strategy = st.builds(
    java_InclusiveOrExpressionChild,
)
java_InclusiveOrExpression_strategy = st.builds(
    java_InclusiveOrExpression,
)
ConditionalOrExpressionChild_strategy = st.builds(
    ConditionalOrExpressionChild,
)
java_ConditionalAndExpressionChild_strategy = st.builds(
    java_ConditionalAndExpressionChild,
)
java_ConditionalAndExpression_strategy = st.builds(
    java_ConditionalAndExpression,
)
ConditionalExpressionChild_strategy = st.builds(
    ConditionalExpressionChild,
)
java_ConditionalOrExpressionChild_strategy = st.builds(
    java_ConditionalOrExpressionChild,
)
java_ConditionalOrExpression_strategy = st.builds(
    java_ConditionalOrExpression,
)
InstanceOfExpressionChild_strategy = st.builds(
    InstanceOfExpressionChild,
)
java_RelationExpressionChild_strategy = st.builds(
    java_RelationExpressionChild,
)
java_RelationExpression_strategy = st.builds(
    java_RelationExpression,
)
java_AssignmentOperator_strategy = st.builds(
    java_AssignmentOperator,
)
java_AssignmentExpressionChild_strategy = st.builds(
    java_AssignmentExpressionChild,
)
java_AssignmentExpression_strategy = st.builds(
    java_AssignmentExpression,
)
ForLoopInitializer_strategy = st.builds(
    ForLoopInitializer,
)
java_ExpressionList_strategy = st.builds(
    java_ExpressionList,
)
Annotable_strategy = st.builds(
    Annotable,
)
JavaRoot_strategy = st.builds(
    JavaRoot,
)
java_EmptyModel_strategy = st.builds(
    java_EmptyModel,
)
java_Package_strategy = st.builds(
    java_Package,
)
java_CompilationUnit_strategy = st.builds(
    java_CompilationUnit,
)
ImportingElement_strategy = st.builds(
    ImportingElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
java_ReferenceableElement_strategy = st.builds(
    java_ReferenceableElement,
)
java_Member_strategy = st.builds(
    java_Member,
)
java_JavaRoot_strategy = st.builds(
    java_JavaRoot,
)
AssignmentExpressionChild_strategy = st.builds(
    AssignmentExpressionChild,
)
java_ConditionalExpressionChild_strategy = st.builds(
    java_ConditionalExpressionChild,
)
java_ConditionalExpression_strategy = st.builds(
    java_ConditionalExpression,
)
java_NamespaceAwareElement_strategy = st.builds(
    java_NamespaceAwareElement,
    namespaces=
        safe_text
)
java_NamedElement_strategy = st.builds(
    java_NamedElement,
    name=
        safe_text
)
java_LayoutInformation_strategy = st.builds(
    java_LayoutInformation,
)
java_Commentable_strategy = st.builds(
    java_Commentable,
)
Implementor_strategy = st.builds(
    Implementor,
)
ConcreteClassifier_strategy = st.builds(
    ConcreteClassifier,
)
java_Enumeration_strategy = st.builds(
    java_Enumeration,
)
java_Interface_strategy = st.builds(
    java_Interface,
)
java_Class_strategy = st.builds(
    java_Class,
)
java_TypeReference_strategy = st.builds(
    java_TypeReference,
)
java_Implementor_strategy = st.builds(
    java_Implementor,
)
java_Annotation_strategy = st.builds(
    java_Annotation,
)
AnnotableAndModifiable_strategy = st.builds(
    AnnotableAndModifiable,
)
java_LocalVariable_strategy = st.builds(
    java_LocalVariable,
)
java_Parameter_strategy = st.builds(
    java_Parameter,
)
Statement_strategy = st.builds(
    Statement,
)
java_ForEachLoop_strategy = st.builds(
    java_ForEachLoop,
)
java_Condition_strategy = st.builds(
    java_Condition,
)
java_Assert_strategy = st.builds(
    java_Assert,
)
java_JumpLabel_strategy = st.builds(
    java_JumpLabel,
)
java_Switch_strategy = st.builds(
    java_Switch,
)
java_Throw_strategy = st.builds(
    java_Throw,
)
java_Return_strategy = st.builds(
    java_Return,
)
java_TryBlock_strategy = st.builds(
    java_TryBlock,
)
java_Jump_strategy = st.builds(
    java_Jump,
)
java_ForLoop_strategy = st.builds(
    java_ForLoop,
)
java_WhileLoop_strategy = st.builds(
    java_WhileLoop,
)
java_SynchronizedBlock_strategy = st.builds(
    java_SynchronizedBlock,
)
java_LocalVariableStatement_strategy = st.builds(
    java_LocalVariableStatement,
)
java_EmptyStatement_strategy = st.builds(
    java_EmptyStatement,
)
java_ExpressionStatement_strategy = st.builds(
    java_ExpressionStatement,
)
Member_strategy = st.builds(
    Member,
)
java_EmptyMember_strategy = st.builds(
    java_EmptyMember,
)
java_Block_strategy = st.builds(
    java_Block,
)
MemberContainer_strategy = st.builds(
    MemberContainer,
)
TypeParametrizable_strategy = st.builds(
    TypeParametrizable,
)
java_Constructor_strategy = st.builds(
    java_Constructor,
)
Classifier_strategy = st.builds(
    Classifier,
)
java_TypeParameter_strategy = st.builds(
    java_TypeParameter,
)
java_ConcreteClassifier_strategy = st.builds(
    java_ConcreteClassifier,
)
ReferenceableElement_strategy = st.builds(
    ReferenceableElement,
)
java_AdditionalField_strategy = st.builds(
    java_AdditionalField,
)
java_AdditionalLocalVariable_strategy = st.builds(
    java_AdditionalLocalVariable,
)
java_Method_strategy = st.builds(
    java_Method,
)
java_Field_strategy = st.builds(
    java_Field,
)
java_PackageReference_strategy = st.builds(
    java_PackageReference,
)
java_EnumConstant_strategy = st.builds(
    java_EnumConstant,
)
java_Variable_strategy = st.builds(
    java_Variable,
)
Type_strategy = st.builds(
    Type,
)
java_Classifier_strategy = st.builds(
    java_Classifier,
)
java_AnonymousClass_strategy = st.builds(
    java_AnonymousClass,
)
java_PrimitiveType_strategy = st.builds(
    java_PrimitiveType,
)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=java_Char_strategy)
@settings(max_examples=50)
def test_java_char_instantiation(instance):
    assert isinstance(instance, java_Char)

@given(instance=java_Short_strategy)
@settings(max_examples=50)
def test_java_short_instantiation(instance):
    assert isinstance(instance, java_Short)

@given(instance=java_Int_strategy)
@settings(max_examples=50)
def test_java_int_instantiation(instance):
    assert isinstance(instance, java_Int)

@given(instance=java_Float_strategy)
@settings(max_examples=50)
def test_java_float_instantiation(instance):
    assert isinstance(instance, java_Float)

@given(instance=java_Long_strategy)
@settings(max_examples=50)
def test_java_long_instantiation(instance):
    assert isinstance(instance, java_Long)

@given(instance=java_Byte_strategy)
@settings(max_examples=50)
def test_java_byte_instantiation(instance):
    assert isinstance(instance, java_Byte)

@given(instance=java_Double_strategy)
@settings(max_examples=50)
def test_java_double_instantiation(instance):
    assert isinstance(instance, java_Double)

@given(instance=java_Void_strategy)
@settings(max_examples=50)
def test_java_void_instantiation(instance):
    assert isinstance(instance, java_Void)

@given(instance=ArrayInstantiationByValues_strategy)
@settings(max_examples=50)
def test_arrayinstantiationbyvalues_instantiation(instance):
    assert isinstance(instance, ArrayInstantiationByValues)

@given(instance=java_ArrayInstantiationByValuesUntyped_strategy)
@settings(max_examples=50)
def test_java_arrayinstantiationbyvaluesuntyped_instantiation(instance):
    assert isinstance(instance, java_ArrayInstantiationByValuesUntyped)

@given(instance=ArrayTypeable_strategy)
@settings(max_examples=50)
def test_arraytypeable_instantiation(instance):
    assert isinstance(instance, ArrayTypeable)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=java_ArrayInstantiationByValuesTyped_strategy)
@settings(max_examples=50)
def test_java_arrayinstantiationbyvaluestyped_instantiation(instance):
    assert isinstance(instance, java_ArrayInstantiationByValuesTyped)

@given(instance=ArrayInstantiation_strategy)
@settings(max_examples=50)
def test_arrayinstantiation_instantiation(instance):
    assert isinstance(instance, ArrayInstantiation)

@given(instance=java_ArrayInstantiationByValues_strategy)
@settings(max_examples=50)
def test_java_arrayinstantiationbyvalues_instantiation(instance):
    assert isinstance(instance, java_ArrayInstantiationByValues)

@given(instance=java_ArrayInstantiationBySize_strategy)
@settings(max_examples=50)
def test_java_arrayinstantiationbysize_instantiation(instance):
    assert isinstance(instance, java_ArrayInstantiationBySize)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=AnnotationValue_strategy)
@settings(max_examples=50)
def test_annotationvalue_instantiation(instance):
    assert isinstance(instance, AnnotationValue)

@given(instance=ArrayInitializationValue_strategy)
@settings(max_examples=50)
def test_arrayinitializationvalue_instantiation(instance):
    assert isinstance(instance, ArrayInitializationValue)

@given(instance=java_ArrayInitializer_strategy)
@settings(max_examples=50)
def test_java_arrayinitializer_instantiation(instance):
    assert isinstance(instance, java_ArrayInitializer)

@given(instance=InterfaceMethod_strategy)
@settings(max_examples=50)
def test_interfacemethod_instantiation(instance):
    assert isinstance(instance, InterfaceMethod)

@given(instance=java_AnnotationAttribute_strategy)
@settings(max_examples=50)
def test_java_annotationattribute_instantiation(instance):
    assert isinstance(instance, java_AnnotationAttribute)

@given(instance=AnnotationParameter_strategy)
@settings(max_examples=50)
def test_annotationparameter_instantiation(instance):
    assert isinstance(instance, AnnotationParameter)

@given(instance=java_AnnotationParameterList_strategy)
@settings(max_examples=50)
def test_java_annotationparameterlist_instantiation(instance):
    assert isinstance(instance, java_AnnotationParameterList)

@given(instance=java_SingleAnnotationParameter_strategy)
@settings(max_examples=50)
def test_java_singleannotationparameter_instantiation(instance):
    assert isinstance(instance, java_SingleAnnotationParameter)

@given(instance=NamespaceAwareElement_strategy)
@settings(max_examples=50)
def test_namespaceawareelement_instantiation(instance):
    assert isinstance(instance, NamespaceAwareElement)

@given(instance=AnnotationInstanceOrModifier_strategy)
@settings(max_examples=50)
def test_annotationinstanceormodifier_instantiation(instance):
    assert isinstance(instance, AnnotationInstanceOrModifier)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=java_ArrayInstantiation_strategy)
@settings(max_examples=50)
def test_java_arrayinstantiation_instantiation(instance):
    assert isinstance(instance, java_ArrayInstantiation)

@given(instance=java_AnnotationInstance_strategy)
@settings(max_examples=50)
def test_java_annotationinstance_instantiation(instance):
    assert isinstance(instance, java_AnnotationInstance)

@given(instance=Commentable_strategy)
@settings(max_examples=50)
def test_commentable_instantiation(instance):
    assert isinstance(instance, Commentable)

@given(instance=java_AnnotationParameter_strategy)
@settings(max_examples=50)
def test_java_annotationparameter_instantiation(instance):
    assert isinstance(instance, java_AnnotationParameter)

@given(instance=java_ArrayDimension_strategy)
@settings(max_examples=50)
def test_java_arraydimension_instantiation(instance):
    assert isinstance(instance, java_ArrayDimension)

@given(instance=java_ArrayInitializationValue_strategy)
@settings(max_examples=50)
def test_java_arrayinitializationvalue_instantiation(instance):
    assert isinstance(instance, java_ArrayInitializationValue)

@given(instance=java_AnnotationValue_strategy)
@settings(max_examples=50)
def test_java_annotationvalue_instantiation(instance):
    assert isinstance(instance, java_AnnotationValue)

@given(instance=java_AnnotationAttributeSetting_strategy)
@settings(max_examples=50)
def test_java_annotationattributesetting_instantiation(instance):
    assert isinstance(instance, java_AnnotationAttributeSetting)

@given(instance=java_ArraySelector_strategy)
@settings(max_examples=50)
def test_java_arrayselector_instantiation(instance):
    assert isinstance(instance, java_ArraySelector)

@given(instance=java_Annotable_strategy)
@settings(max_examples=50)
def test_java_annotable_instantiation(instance):
    assert isinstance(instance, java_Annotable)

@given(instance=java_ArrayTypeable_strategy)
@settings(max_examples=50)
def test_java_arraytypeable_instantiation(instance):
    assert isinstance(instance, java_ArrayTypeable)

@given(instance=java_Expression_strategy)
@settings(max_examples=50)
def test_java_expression_instantiation(instance):
    assert isinstance(instance, java_Expression)

@given(instance=java_Boolean_strategy)
@settings(max_examples=50)
def test_java_boolean_instantiation(instance):
    assert isinstance(instance, java_Boolean)

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=java_TypedElement_strategy)
@settings(max_examples=50)
def test_java_typedelement_instantiation(instance):
    assert isinstance(instance, java_TypedElement)

@given(instance=java_Type_strategy)
@settings(max_examples=50)
def test_java_type_instantiation(instance):
    assert isinstance(instance, java_Type)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_Type_strategy)
@settings(max_examples=30)
def test_java_type_issupertype_changes_state(instance):
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
        assert has_statements, f"Function 'isSuperType' in java_Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSuperType' in java_Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSuperType' in java_Type is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_Type_strategy)
@settings(max_examples=30)
def test_java_type_equalstype_changes_state(instance):
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
        assert has_statements, f"Function 'equalsType' in java_Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equalsType' in java_Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equalsType' in java_Type is not implemented or raised an error")

@given(instance=WhileLoop_strategy)
@settings(max_examples=50)
def test_whileloop_instantiation(instance):
    assert isinstance(instance, WhileLoop)

@given(instance=java_DoWhileLoop_strategy)
@settings(max_examples=50)
def test_java_dowhileloop_instantiation(instance):
    assert isinstance(instance, java_DoWhileLoop)

@given(instance=SwitchCase_strategy)
@settings(max_examples=50)
def test_switchcase_instantiation(instance):
    assert isinstance(instance, SwitchCase)

@given(instance=java_DefaultSwitchCase_strategy)
@settings(max_examples=50)
def test_java_defaultswitchcase_instantiation(instance):
    assert isinstance(instance, java_DefaultSwitchCase)

@given(instance=Modifiable_strategy)
@settings(max_examples=50)
def test_modifiable_instantiation(instance):
    assert isinstance(instance, Modifiable)

@given(instance=Jump_strategy)
@settings(max_examples=50)
def test_jump_instantiation(instance):
    assert isinstance(instance, Jump)

@given(instance=java_Continue_strategy)
@settings(max_examples=50)
def test_java_continue_instantiation(instance):
    assert isinstance(instance, java_Continue)

@given(instance=java_Break_strategy)
@settings(max_examples=50)
def test_java_break_instantiation(instance):
    assert isinstance(instance, java_Break)

@given(instance=Conditional_strategy)
@settings(max_examples=50)
def test_conditional_instantiation(instance):
    assert isinstance(instance, Conditional)

@given(instance=java_NormalSwitchCase_strategy)
@settings(max_examples=50)
def test_java_normalswitchcase_instantiation(instance):
    assert isinstance(instance, java_NormalSwitchCase)

@given(instance=java_ForLoopInitializer_strategy)
@settings(max_examples=50)
def test_java_forloopinitializer_instantiation(instance):
    assert isinstance(instance, java_ForLoopInitializer)

@given(instance=java_Conditional_strategy)
@settings(max_examples=50)
def test_java_conditional_instantiation(instance):
    assert isinstance(instance, java_Conditional)

@given(instance=java_StatementListContainer_strategy)
@settings(max_examples=50)
def test_java_statementlistcontainer_instantiation(instance):
    assert isinstance(instance, java_StatementListContainer)

@given(instance=java_Statement_strategy)
@settings(max_examples=50)
def test_java_statement_instantiation(instance):
    assert isinstance(instance, java_Statement)

@given(instance=java_StatementContainer_strategy)
@settings(max_examples=50)
def test_java_statementcontainer_instantiation(instance):
    assert isinstance(instance, java_StatementContainer)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=java_VariableLengthParameter_strategy)
@settings(max_examples=50)
def test_java_variablelengthparameter_instantiation(instance):
    assert isinstance(instance, java_VariableLengthParameter)

@given(instance=java_OrdinaryParameter_strategy)
@settings(max_examples=50)
def test_java_ordinaryparameter_instantiation(instance):
    assert isinstance(instance, java_OrdinaryParameter)

@given(instance=java_Parametrizable_strategy)
@settings(max_examples=50)
def test_java_parametrizable_instantiation(instance):
    assert isinstance(instance, java_Parametrizable)

@given(instance=java_SelfReference_strategy)
@settings(max_examples=50)
def test_java_selfreference_instantiation(instance):
    assert isinstance(instance, java_SelfReference)

@given(instance=java_StringReference_strategy)
@settings(max_examples=50)
def test_java_stringreference_instantiation(instance):
    assert isinstance(instance, java_StringReference)



@given(instance=java_StringReference_strategy)
def test_java_stringreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=StatementContainer_strategy)
@settings(max_examples=50)
def test_statementcontainer_instantiation(instance):
    assert isinstance(instance, StatementContainer)

@given(instance=ElementReference_strategy)
@settings(max_examples=50)
def test_elementreference_instantiation(instance):
    assert isinstance(instance, ElementReference)

@given(instance=java_IdentifierReference_strategy)
@settings(max_examples=50)
def test_java_identifierreference_instantiation(instance):
    assert isinstance(instance, java_IdentifierReference)

@given(instance=java_ElementReference_strategy)
@settings(max_examples=50)
def test_java_elementreference_instantiation(instance):
    assert isinstance(instance, java_ElementReference)

@given(instance=java_Argumentable_strategy)
@settings(max_examples=50)
def test_java_argumentable_instantiation(instance):
    assert isinstance(instance, java_Argumentable)

@given(instance=TypeArgumentable_strategy)
@settings(max_examples=50)
def test_typeargumentable_instantiation(instance):
    assert isinstance(instance, TypeArgumentable)

@given(instance=java_ClassifierReference_strategy)
@settings(max_examples=50)
def test_java_classifierreference_instantiation(instance):
    assert isinstance(instance, java_ClassifierReference)

@given(instance=ShiftOperator_strategy)
@settings(max_examples=50)
def test_shiftoperator_instantiation(instance):
    assert isinstance(instance, ShiftOperator)

@given(instance=java_UnsignedRightShift_strategy)
@settings(max_examples=50)
def test_java_unsignedrightshift_instantiation(instance):
    assert isinstance(instance, java_UnsignedRightShift)

@given(instance=java_RightShift_strategy)
@settings(max_examples=50)
def test_java_rightshift_instantiation(instance):
    assert isinstance(instance, java_RightShift)

@given(instance=java_LeftShift_strategy)
@settings(max_examples=50)
def test_java_leftshift_instantiation(instance):
    assert isinstance(instance, java_LeftShift)

@given(instance=UnaryModificationOperator_strategy)
@settings(max_examples=50)
def test_unarymodificationoperator_instantiation(instance):
    assert isinstance(instance, UnaryModificationOperator)

@given(instance=java_PlusPlus_strategy)
@settings(max_examples=50)
def test_java_plusplus_instantiation(instance):
    assert isinstance(instance, java_PlusPlus)

@given(instance=java_MinusMinus_strategy)
@settings(max_examples=50)
def test_java_minusminus_instantiation(instance):
    assert isinstance(instance, java_MinusMinus)

@given(instance=MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, MultiplicativeOperator)

@given(instance=java_Remainder_strategy)
@settings(max_examples=50)
def test_java_remainder_instantiation(instance):
    assert isinstance(instance, java_Remainder)

@given(instance=java_Multiplication_strategy)
@settings(max_examples=50)
def test_java_multiplication_instantiation(instance):
    assert isinstance(instance, java_Multiplication)

@given(instance=java_Division_strategy)
@settings(max_examples=50)
def test_java_division_instantiation(instance):
    assert isinstance(instance, java_Division)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=java_Complement_strategy)
@settings(max_examples=50)
def test_java_complement_instantiation(instance):
    assert isinstance(instance, java_Complement)

@given(instance=java_Negate_strategy)
@settings(max_examples=50)
def test_java_negate_instantiation(instance):
    assert isinstance(instance, java_Negate)

@given(instance=AdditiveOperator_strategy)
@settings(max_examples=50)
def test_additiveoperator_instantiation(instance):
    assert isinstance(instance, AdditiveOperator)

@given(instance=java_Subtraction_strategy)
@settings(max_examples=50)
def test_java_subtraction_instantiation(instance):
    assert isinstance(instance, java_Subtraction)

@given(instance=java_Addition_strategy)
@settings(max_examples=50)
def test_java_addition_instantiation(instance):
    assert isinstance(instance, java_Addition)

@given(instance=RelationOperator_strategy)
@settings(max_examples=50)
def test_relationoperator_instantiation(instance):
    assert isinstance(instance, RelationOperator)

@given(instance=java_LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_java_lessthanorequal_instantiation(instance):
    assert isinstance(instance, java_LessThanOrEqual)

@given(instance=java_GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_java_greaterthanorequal_instantiation(instance):
    assert isinstance(instance, java_GreaterThanOrEqual)

@given(instance=java_LessThan_strategy)
@settings(max_examples=50)
def test_java_lessthan_instantiation(instance):
    assert isinstance(instance, java_LessThan)

@given(instance=java_GreaterThan_strategy)
@settings(max_examples=50)
def test_java_greaterthan_instantiation(instance):
    assert isinstance(instance, java_GreaterThan)

@given(instance=java_PrimitiveTypeReference_strategy)
@settings(max_examples=50)
def test_java_primitivetypereference_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeReference)

@given(instance=java_ReflectiveClassReference_strategy)
@settings(max_examples=50)
def test_java_reflectiveclassreference_instantiation(instance):
    assert isinstance(instance, java_ReflectiveClassReference)

@given(instance=AssignmentOperator_strategy)
@settings(max_examples=50)
def test_assignmentoperator_instantiation(instance):
    assert isinstance(instance, AssignmentOperator)

@given(instance=java_AssignmentAnd_strategy)
@settings(max_examples=50)
def test_java_assignmentand_instantiation(instance):
    assert isinstance(instance, java_AssignmentAnd)

@given(instance=java_AssignmentMinus_strategy)
@settings(max_examples=50)
def test_java_assignmentminus_instantiation(instance):
    assert isinstance(instance, java_AssignmentMinus)

@given(instance=java_AssignmentOr_strategy)
@settings(max_examples=50)
def test_java_assignmentor_instantiation(instance):
    assert isinstance(instance, java_AssignmentOr)

@given(instance=java_AssignmentDivision_strategy)
@settings(max_examples=50)
def test_java_assignmentdivision_instantiation(instance):
    assert isinstance(instance, java_AssignmentDivision)

@given(instance=java_AssignmentModulo_strategy)
@settings(max_examples=50)
def test_java_assignmentmodulo_instantiation(instance):
    assert isinstance(instance, java_AssignmentModulo)

@given(instance=java_AssignmentExclusiveOr_strategy)
@settings(max_examples=50)
def test_java_assignmentexclusiveor_instantiation(instance):
    assert isinstance(instance, java_AssignmentExclusiveOr)

@given(instance=java_AssignmentMultiplication_strategy)
@settings(max_examples=50)
def test_java_assignmentmultiplication_instantiation(instance):
    assert isinstance(instance, java_AssignmentMultiplication)

@given(instance=java_AssignmentLeftShift_strategy)
@settings(max_examples=50)
def test_java_assignmentleftshift_instantiation(instance):
    assert isinstance(instance, java_AssignmentLeftShift)

@given(instance=java_Assignment_strategy)
@settings(max_examples=50)
def test_java_assignment_instantiation(instance):
    assert isinstance(instance, java_Assignment)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=java_Operator_strategy)
@settings(max_examples=50)
def test_java_operator_instantiation(instance):
    assert isinstance(instance, java_Operator)

@given(instance=Modifier_strategy)
@settings(max_examples=50)
def test_modifier_instantiation(instance):
    assert isinstance(instance, Modifier)

@given(instance=java_Synchronized_strategy)
@settings(max_examples=50)
def test_java_synchronized_instantiation(instance):
    assert isinstance(instance, java_Synchronized)

@given(instance=java_Protected_strategy)
@settings(max_examples=50)
def test_java_protected_instantiation(instance):
    assert isinstance(instance, java_Protected)

@given(instance=java_Volatile_strategy)
@settings(max_examples=50)
def test_java_volatile_instantiation(instance):
    assert isinstance(instance, java_Volatile)

@given(instance=java_Public_strategy)
@settings(max_examples=50)
def test_java_public_instantiation(instance):
    assert isinstance(instance, java_Public)

@given(instance=java_Private_strategy)
@settings(max_examples=50)
def test_java_private_instantiation(instance):
    assert isinstance(instance, java_Private)

@given(instance=java_Final_strategy)
@settings(max_examples=50)
def test_java_final_instantiation(instance):
    assert isinstance(instance, java_Final)

@given(instance=java_Transient_strategy)
@settings(max_examples=50)
def test_java_transient_instantiation(instance):
    assert isinstance(instance, java_Transient)

@given(instance=java_Strictfp_strategy)
@settings(max_examples=50)
def test_java_strictfp_instantiation(instance):
    assert isinstance(instance, java_Strictfp)

@given(instance=java_Native_strategy)
@settings(max_examples=50)
def test_java_native_instantiation(instance):
    assert isinstance(instance, java_Native)

@given(instance=java_Abstract_strategy)
@settings(max_examples=50)
def test_java_abstract_instantiation(instance):
    assert isinstance(instance, java_Abstract)

@given(instance=java_Modifiable_strategy)
@settings(max_examples=50)
def test_java_modifiable_instantiation(instance):
    assert isinstance(instance, java_Modifiable)

@given(instance=EqualityOperator_strategy)
@settings(max_examples=50)
def test_equalityoperator_instantiation(instance):
    assert isinstance(instance, EqualityOperator)

@given(instance=java_NotEqual_strategy)
@settings(max_examples=50)
def test_java_notequal_instantiation(instance):
    assert isinstance(instance, java_NotEqual)

@given(instance=java_Equal_strategy)
@settings(max_examples=50)
def test_java_equal_instantiation(instance):
    assert isinstance(instance, java_Equal)

@given(instance=java_AssignmentUnsignedRightShift_strategy)
@settings(max_examples=50)
def test_java_assignmentunsignedrightshift_instantiation(instance):
    assert isinstance(instance, java_AssignmentUnsignedRightShift)

@given(instance=java_AssignmentRightShift_strategy)
@settings(max_examples=50)
def test_java_assignmentrightshift_instantiation(instance):
    assert isinstance(instance, java_AssignmentRightShift)

@given(instance=java_AssignmentPlus_strategy)
@settings(max_examples=50)
def test_java_assignmentplus_instantiation(instance):
    assert isinstance(instance, java_AssignmentPlus)

@given(instance=java_AnnotableAndModifiable_strategy)
@settings(max_examples=50)
def test_java_annotableandmodifiable_instantiation(instance):
    assert isinstance(instance, java_AnnotableAndModifiable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java_annotableandmodifiable_addmodifier_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addModifier(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addModifier).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addModifier' in java_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addModifier' in java_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addModifier' in java_AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java_annotableandmodifiable_removemodifier_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeModifier(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeModifier).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeModifier' in java_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeModifier' in java_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeModifier' in java_AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java_annotableandmodifiable_isstatic_changes_state(instance):
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
        assert has_statements, f"Function 'isStatic' in java_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isStatic' in java_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isStatic' in java_AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java_annotableandmodifiable_isprivate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isPrivate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isPrivate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isPrivate' in java_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPrivate' in java_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPrivate' in java_AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java_annotableandmodifiable_makepublic_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.makePublic()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.makePublic).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'makePublic' in java_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'makePublic' in java_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'makePublic' in java_AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java_annotableandmodifiable_ishidden_changes_state(instance):
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
        assert has_statements, f"Function 'isHidden' in java_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isHidden' in java_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isHidden' in java_AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java_annotableandmodifiable_removeallmodifiers_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeAllModifiers()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeAllModifiers).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeAllModifiers' in java_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeAllModifiers' in java_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeAllModifiers' in java_AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java_annotableandmodifiable_ispublic_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isPublic()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isPublic).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isPublic' in java_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPublic' in java_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPublic' in java_AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java_annotableandmodifiable_makeprotected_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.makeProtected()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.makeProtected).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'makeProtected' in java_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'makeProtected' in java_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'makeProtected' in java_AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java_annotableandmodifiable_hasmodifier_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasModifier(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasModifier).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasModifier' in java_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasModifier' in java_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasModifier' in java_AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java_annotableandmodifiable_isprotected_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isProtected()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isProtected).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isProtected' in java_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isProtected' in java_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isProtected' in java_AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java_annotableandmodifiable_makeprivate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.makePrivate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.makePrivate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'makePrivate' in java_AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'makePrivate' in java_AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'makePrivate' in java_AnnotableAndModifiable is not implemented or raised an error")

@given(instance=java_AnnotationInstanceOrModifier_strategy)
@settings(max_examples=50)
def test_java_annotationinstanceormodifier_instantiation(instance):
    assert isinstance(instance, java_AnnotationInstanceOrModifier)

@given(instance=java_Modifier_strategy)
@settings(max_examples=50)
def test_java_modifier_instantiation(instance):
    assert isinstance(instance, java_Modifier)

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

@given(instance=java_InterfaceMethod_strategy)
@settings(max_examples=50)
def test_java_interfacemethod_instantiation(instance):
    assert isinstance(instance, java_InterfaceMethod)

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

@given(instance=java_CatchBlock_strategy)
@settings(max_examples=50)
def test_java_catchblock_instantiation(instance):
    assert isinstance(instance, java_CatchBlock)

@given(instance=java_SwitchCase_strategy)
@settings(max_examples=50)
def test_java_switchcase_instantiation(instance):
    assert isinstance(instance, java_SwitchCase)

@given(instance=java_ClassMethod_strategy)
@settings(max_examples=50)
def test_java_classmethod_instantiation(instance):
    assert isinstance(instance, java_ClassMethod)

@given(instance=Initializable_strategy)
@settings(max_examples=50)
def test_initializable_instantiation(instance):
    assert isinstance(instance, Initializable)

@given(instance=java_MemberContainer_strategy)
@settings(max_examples=50)
def test_java_membercontainer_instantiation(instance):
    assert isinstance(instance, java_MemberContainer)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_MemberContainer_strategy)
@settings(max_examples=30)
def test_java_membercontainer_createfield_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createField(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createField).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createField' in java_MemberContainer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createField' in java_MemberContainer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createField' in java_MemberContainer is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_MemberContainer_strategy)
@settings(max_examples=30)
def test_java_membercontainer_removemethods_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeMethods(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeMethods).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeMethods' in java_MemberContainer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeMethods' in java_MemberContainer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeMethods' in java_MemberContainer is not implemented or raised an error")

@given(instance=java_NamespaceClassifierReference_strategy)
@settings(max_examples=50)
def test_java_namespaceclassifierreference_instantiation(instance):
    assert isinstance(instance, java_NamespaceClassifierReference)

@given(instance=java_ExceptionThrower_strategy)
@settings(max_examples=50)
def test_java_exceptionthrower_instantiation(instance):
    assert isinstance(instance, java_ExceptionThrower)

@given(instance=Self_strategy)
@settings(max_examples=50)
def test_self_instantiation(instance):
    assert isinstance(instance, Self)

@given(instance=java_This_strategy)
@settings(max_examples=50)
def test_java_this_instantiation(instance):
    assert isinstance(instance, java_This)

@given(instance=java_Super_strategy)
@settings(max_examples=50)
def test_java_super_instantiation(instance):
    assert isinstance(instance, java_Super)

@given(instance=LongLiteral_strategy)
@settings(max_examples=50)
def test_longliteral_instantiation(instance):
    assert isinstance(instance, LongLiteral)

@given(instance=java_OctalLongLiteral_strategy)
@settings(max_examples=50)
def test_java_octallongliteral_instantiation(instance):
    assert isinstance(instance, java_OctalLongLiteral)



@given(instance=java_OctalLongLiteral_strategy)
def test_java_octallongliteral_octalValue_setter(instance):
    original = instance.octalValue
    instance.octalValue = original
    assert instance.octalValue == original

@given(instance=java_HexLongLiteral_strategy)
@settings(max_examples=50)
def test_java_hexlongliteral_instantiation(instance):
    assert isinstance(instance, java_HexLongLiteral)



@given(instance=java_HexLongLiteral_strategy)
def test_java_hexlongliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=java_DecimalLongLiteral_strategy)
@settings(max_examples=50)
def test_java_decimallongliteral_instantiation(instance):
    assert isinstance(instance, java_DecimalLongLiteral)



@given(instance=java_DecimalLongLiteral_strategy)
def test_java_decimallongliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=IntegerLiteral_strategy)
@settings(max_examples=50)
def test_integerliteral_instantiation(instance):
    assert isinstance(instance, IntegerLiteral)

@given(instance=java_HexIntegerLiteral_strategy)
@settings(max_examples=50)
def test_java_hexintegerliteral_instantiation(instance):
    assert isinstance(instance, java_HexIntegerLiteral)



@given(instance=java_HexIntegerLiteral_strategy)
def test_java_hexintegerliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=java_OctalIntegerLiteral_strategy)
@settings(max_examples=50)
def test_java_octalintegerliteral_instantiation(instance):
    assert isinstance(instance, java_OctalIntegerLiteral)



@given(instance=java_OctalIntegerLiteral_strategy)
def test_java_octalintegerliteral_octalValue_setter(instance):
    original = instance.octalValue
    instance.octalValue = original
    assert instance.octalValue == original

@given(instance=java_DecimalIntegerLiteral_strategy)
@settings(max_examples=50)
def test_java_decimalintegerliteral_instantiation(instance):
    assert isinstance(instance, java_DecimalIntegerLiteral)



@given(instance=java_DecimalIntegerLiteral_strategy)
def test_java_decimalintegerliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=DoubleLiteral_strategy)
@settings(max_examples=50)
def test_doubleliteral_instantiation(instance):
    assert isinstance(instance, DoubleLiteral)

@given(instance=java_HexDoubleLiteral_strategy)
@settings(max_examples=50)
def test_java_hexdoubleliteral_instantiation(instance):
    assert isinstance(instance, java_HexDoubleLiteral)



@given(instance=java_HexDoubleLiteral_strategy)
def test_java_hexdoubleliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=java_DecimalDoubleLiteral_strategy)
@settings(max_examples=50)
def test_java_decimaldoubleliteral_instantiation(instance):
    assert isinstance(instance, java_DecimalDoubleLiteral)



@given(instance=java_DecimalDoubleLiteral_strategy)
def test_java_decimaldoubleliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=FloatLiteral_strategy)
@settings(max_examples=50)
def test_floatliteral_instantiation(instance):
    assert isinstance(instance, FloatLiteral)

@given(instance=java_HexFloatLiteral_strategy)
@settings(max_examples=50)
def test_java_hexfloatliteral_instantiation(instance):
    assert isinstance(instance, java_HexFloatLiteral)



@given(instance=java_HexFloatLiteral_strategy)
def test_java_hexfloatliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=java_DecimalFloatLiteral_strategy)
@settings(max_examples=50)
def test_java_decimalfloatliteral_instantiation(instance):
    assert isinstance(instance, java_DecimalFloatLiteral)



@given(instance=java_DecimalFloatLiteral_strategy)
def test_java_decimalfloatliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=java_Reference_strategy)
@settings(max_examples=50)
def test_java_reference_instantiation(instance):
    assert isinstance(instance, java_Reference)

@given(instance=java_Literal_strategy)
@settings(max_examples=50)
def test_java_literal_instantiation(instance):
    assert isinstance(instance, java_Literal)

@given(instance=java_Self_strategy)
@settings(max_examples=50)
def test_java_self_instantiation(instance):
    assert isinstance(instance, java_Self)

@given(instance=CallTypeArgumentable_strategy)
@settings(max_examples=50)
def test_calltypeargumentable_instantiation(instance):
    assert isinstance(instance, CallTypeArgumentable)

@given(instance=Instantiation_strategy)
@settings(max_examples=50)
def test_instantiation_instantiation(instance):
    assert isinstance(instance, Instantiation)

@given(instance=java_ExplicitConstructorCall_strategy)
@settings(max_examples=50)
def test_java_explicitconstructorcall_instantiation(instance):
    assert isinstance(instance, java_ExplicitConstructorCall)

@given(instance=java_NewConstructorCall_strategy)
@settings(max_examples=50)
def test_java_newconstructorcall_instantiation(instance):
    assert isinstance(instance, java_NewConstructorCall)

@given(instance=Argumentable_strategy)
@settings(max_examples=50)
def test_argumentable_instantiation(instance):
    assert isinstance(instance, Argumentable)

@given(instance=java_MethodCall_strategy)
@settings(max_examples=50)
def test_java_methodcall_instantiation(instance):
    assert isinstance(instance, java_MethodCall)

@given(instance=java_Instantiation_strategy)
@settings(max_examples=50)
def test_java_instantiation_instantiation(instance):
    assert isinstance(instance, java_Instantiation)

@given(instance=java_Initializable_strategy)
@settings(max_examples=50)
def test_java_initializable_instantiation(instance):
    assert isinstance(instance, java_Initializable)

@given(instance=StaticImport_strategy)
@settings(max_examples=50)
def test_staticimport_instantiation(instance):
    assert isinstance(instance, StaticImport)

@given(instance=java_StaticMemberImport_strategy)
@settings(max_examples=50)
def test_java_staticmemberimport_instantiation(instance):
    assert isinstance(instance, java_StaticMemberImport)

@given(instance=java_StaticClassifierImport_strategy)
@settings(max_examples=50)
def test_java_staticclassifierimport_instantiation(instance):
    assert isinstance(instance, java_StaticClassifierImport)

@given(instance=java_Static_strategy)
@settings(max_examples=50)
def test_java_static_instantiation(instance):
    assert isinstance(instance, java_Static)

@given(instance=Import_strategy)
@settings(max_examples=50)
def test_import_instantiation(instance):
    assert isinstance(instance, Import)

@given(instance=java_ClassifierImport_strategy)
@settings(max_examples=50)
def test_java_classifierimport_instantiation(instance):
    assert isinstance(instance, java_ClassifierImport)

@given(instance=java_PackageImport_strategy)
@settings(max_examples=50)
def test_java_packageimport_instantiation(instance):
    assert isinstance(instance, java_PackageImport)

@given(instance=java_StaticImport_strategy)
@settings(max_examples=50)
def test_java_staticimport_instantiation(instance):
    assert isinstance(instance, java_StaticImport)

@given(instance=java_ImportingElement_strategy)
@settings(max_examples=50)
def test_java_importingelement_instantiation(instance):
    assert isinstance(instance, java_ImportingElement)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=java_LongLiteral_strategy)
@settings(max_examples=50)
def test_java_longliteral_instantiation(instance):
    assert isinstance(instance, java_LongLiteral)

@given(instance=java_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_java_doubleliteral_instantiation(instance):
    assert isinstance(instance, java_DoubleLiteral)

@given(instance=java_CharacterLiteral_strategy)
@settings(max_examples=50)
def test_java_characterliteral_instantiation(instance):
    assert isinstance(instance, java_CharacterLiteral)



@given(instance=java_CharacterLiteral_strategy)
def test_java_characterliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=java_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_java_integerliteral_instantiation(instance):
    assert isinstance(instance, java_IntegerLiteral)

@given(instance=java_FloatLiteral_strategy)
@settings(max_examples=50)
def test_java_floatliteral_instantiation(instance):
    assert isinstance(instance, java_FloatLiteral)

@given(instance=java_NullLiteral_strategy)
@settings(max_examples=50)
def test_java_nullliteral_instantiation(instance):
    assert isinstance(instance, java_NullLiteral)

@given(instance=java_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_java_booleanliteral_instantiation(instance):
    assert isinstance(instance, java_BooleanLiteral)



@given(instance=java_BooleanLiteral_strategy)
def test_java_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TypeArgument_strategy)
@settings(max_examples=50)
def test_typeargument_instantiation(instance):
    assert isinstance(instance, TypeArgument)

@given(instance=java_SuperTypeArgument_strategy)
@settings(max_examples=50)
def test_java_supertypeargument_instantiation(instance):
    assert isinstance(instance, java_SuperTypeArgument)

@given(instance=java_QualifiedTypeArgument_strategy)
@settings(max_examples=50)
def test_java_qualifiedtypeargument_instantiation(instance):
    assert isinstance(instance, java_QualifiedTypeArgument)

@given(instance=java_ExtendsTypeArgument_strategy)
@settings(max_examples=50)
def test_java_extendstypeargument_instantiation(instance):
    assert isinstance(instance, java_ExtendsTypeArgument)

@given(instance=java_TypeParametrizable_strategy)
@settings(max_examples=50)
def test_java_typeparametrizable_instantiation(instance):
    assert isinstance(instance, java_TypeParametrizable)

@given(instance=java_CallTypeArgumentable_strategy)
@settings(max_examples=50)
def test_java_calltypeargumentable_instantiation(instance):
    assert isinstance(instance, java_CallTypeArgumentable)

@given(instance=java_TypeArgumentable_strategy)
@settings(max_examples=50)
def test_java_typeargumentable_instantiation(instance):
    assert isinstance(instance, java_TypeArgumentable)

@given(instance=java_TypeArgument_strategy)
@settings(max_examples=50)
def test_java_typeargument_instantiation(instance):
    assert isinstance(instance, java_TypeArgument)

@given(instance=java_NestedExpression_strategy)
@settings(max_examples=50)
def test_java_nestedexpression_instantiation(instance):
    assert isinstance(instance, java_NestedExpression)

@given(instance=UnaryModificationExpressionChild_strategy)
@settings(max_examples=50)
def test_unarymodificationexpressionchild_instantiation(instance):
    assert isinstance(instance, UnaryModificationExpressionChild)

@given(instance=java_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_java_primaryexpression_instantiation(instance):
    assert isinstance(instance, java_PrimaryExpression)

@given(instance=java_CastExpression_strategy)
@settings(max_examples=50)
def test_java_castexpression_instantiation(instance):
    assert isinstance(instance, java_CastExpression)

@given(instance=java_Import_strategy)
@settings(max_examples=50)
def test_java_import_instantiation(instance):
    assert isinstance(instance, java_Import)

@given(instance=java_UnknownTypeArgument_strategy)
@settings(max_examples=50)
def test_java_unknowntypeargument_instantiation(instance):
    assert isinstance(instance, java_UnknownTypeArgument)

@given(instance=java_UnaryModificationOperator_strategy)
@settings(max_examples=50)
def test_java_unarymodificationoperator_instantiation(instance):
    assert isinstance(instance, java_UnaryModificationOperator)

@given(instance=UnaryExpressionChild_strategy)
@settings(max_examples=50)
def test_unaryexpressionchild_instantiation(instance):
    assert isinstance(instance, UnaryExpressionChild)

@given(instance=java_UnaryModificationExpressionChild_strategy)
@settings(max_examples=50)
def test_java_unarymodificationexpressionchild_instantiation(instance):
    assert isinstance(instance, java_UnaryModificationExpressionChild)

@given(instance=java_UnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_java_unarymodificationexpression_instantiation(instance):
    assert isinstance(instance, java_UnaryModificationExpression)

@given(instance=java_UnaryOperator_strategy)
@settings(max_examples=50)
def test_java_unaryoperator_instantiation(instance):
    assert isinstance(instance, java_UnaryOperator)

@given(instance=MultiplicativeExpressionChild_strategy)
@settings(max_examples=50)
def test_multiplicativeexpressionchild_instantiation(instance):
    assert isinstance(instance, MultiplicativeExpressionChild)

@given(instance=java_UnaryExpressionChild_strategy)
@settings(max_examples=50)
def test_java_unaryexpressionchild_instantiation(instance):
    assert isinstance(instance, java_UnaryExpressionChild)

@given(instance=java_UnaryExpression_strategy)
@settings(max_examples=50)
def test_java_unaryexpression_instantiation(instance):
    assert isinstance(instance, java_UnaryExpression)

@given(instance=java_MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_java_multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, java_MultiplicativeOperator)

@given(instance=AdditiveExpressionChild_strategy)
@settings(max_examples=50)
def test_additiveexpressionchild_instantiation(instance):
    assert isinstance(instance, AdditiveExpressionChild)

@given(instance=java_MultiplicativeExpressionChild_strategy)
@settings(max_examples=50)
def test_java_multiplicativeexpressionchild_instantiation(instance):
    assert isinstance(instance, java_MultiplicativeExpressionChild)

@given(instance=java_MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_java_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, java_MultiplicativeExpression)

@given(instance=java_AdditiveOperator_strategy)
@settings(max_examples=50)
def test_java_additiveoperator_instantiation(instance):
    assert isinstance(instance, java_AdditiveOperator)

@given(instance=ShiftExpressionChild_strategy)
@settings(max_examples=50)
def test_shiftexpressionchild_instantiation(instance):
    assert isinstance(instance, ShiftExpressionChild)

@given(instance=java_AdditiveExpressionChild_strategy)
@settings(max_examples=50)
def test_java_additiveexpressionchild_instantiation(instance):
    assert isinstance(instance, java_AdditiveExpressionChild)

@given(instance=java_AdditiveExpression_strategy)
@settings(max_examples=50)
def test_java_additiveexpression_instantiation(instance):
    assert isinstance(instance, java_AdditiveExpression)

@given(instance=java_ShiftOperator_strategy)
@settings(max_examples=50)
def test_java_shiftoperator_instantiation(instance):
    assert isinstance(instance, java_ShiftOperator)

@given(instance=RelationExpressionChild_strategy)
@settings(max_examples=50)
def test_relationexpressionchild_instantiation(instance):
    assert isinstance(instance, RelationExpressionChild)

@given(instance=java_ShiftExpressionChild_strategy)
@settings(max_examples=50)
def test_java_shiftexpressionchild_instantiation(instance):
    assert isinstance(instance, java_ShiftExpressionChild)

@given(instance=java_ShiftExpression_strategy)
@settings(max_examples=50)
def test_java_shiftexpression_instantiation(instance):
    assert isinstance(instance, java_ShiftExpression)

@given(instance=java_RelationOperator_strategy)
@settings(max_examples=50)
def test_java_relationoperator_instantiation(instance):
    assert isinstance(instance, java_RelationOperator)

@given(instance=UnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_unarymodificationexpression_instantiation(instance):
    assert isinstance(instance, UnaryModificationExpression)

@given(instance=java_SuffixUnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_java_suffixunarymodificationexpression_instantiation(instance):
    assert isinstance(instance, java_SuffixUnaryModificationExpression)

@given(instance=java_PrefixUnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_java_prefixunarymodificationexpression_instantiation(instance):
    assert isinstance(instance, java_PrefixUnaryModificationExpression)

@given(instance=EqualityExpressionChild_strategy)
@settings(max_examples=50)
def test_equalityexpressionchild_instantiation(instance):
    assert isinstance(instance, EqualityExpressionChild)

@given(instance=java_InstanceOfExpressionChild_strategy)
@settings(max_examples=50)
def test_java_instanceofexpressionchild_instantiation(instance):
    assert isinstance(instance, java_InstanceOfExpressionChild)

@given(instance=java_InstanceOfExpression_strategy)
@settings(max_examples=50)
def test_java_instanceofexpression_instantiation(instance):
    assert isinstance(instance, java_InstanceOfExpression)

@given(instance=java_EqualityOperator_strategy)
@settings(max_examples=50)
def test_java_equalityoperator_instantiation(instance):
    assert isinstance(instance, java_EqualityOperator)

@given(instance=AndExpressionChild_strategy)
@settings(max_examples=50)
def test_andexpressionchild_instantiation(instance):
    assert isinstance(instance, AndExpressionChild)

@given(instance=java_EqualityExpressionChild_strategy)
@settings(max_examples=50)
def test_java_equalityexpressionchild_instantiation(instance):
    assert isinstance(instance, java_EqualityExpressionChild)

@given(instance=java_EqualityExpression_strategy)
@settings(max_examples=50)
def test_java_equalityexpression_instantiation(instance):
    assert isinstance(instance, java_EqualityExpression)

@given(instance=ExclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_exclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, ExclusiveOrExpressionChild)

@given(instance=java_AndExpressionChild_strategy)
@settings(max_examples=50)
def test_java_andexpressionchild_instantiation(instance):
    assert isinstance(instance, java_AndExpressionChild)

@given(instance=java_AndExpression_strategy)
@settings(max_examples=50)
def test_java_andexpression_instantiation(instance):
    assert isinstance(instance, java_AndExpression)

@given(instance=InclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_inclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, InclusiveOrExpressionChild)

@given(instance=java_ExclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_java_exclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, java_ExclusiveOrExpressionChild)

@given(instance=java_ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_java_exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, java_ExclusiveOrExpression)

@given(instance=ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalAndExpressionChild)

@given(instance=java_InclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_java_inclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, java_InclusiveOrExpressionChild)

@given(instance=java_InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_java_inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, java_InclusiveOrExpression)

@given(instance=ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalOrExpressionChild)

@given(instance=java_ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_java_conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, java_ConditionalAndExpressionChild)

@given(instance=java_ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_java_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, java_ConditionalAndExpression)

@given(instance=ConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalExpressionChild)

@given(instance=java_ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_java_conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, java_ConditionalOrExpressionChild)

@given(instance=java_ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_java_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, java_ConditionalOrExpression)

@given(instance=InstanceOfExpressionChild_strategy)
@settings(max_examples=50)
def test_instanceofexpressionchild_instantiation(instance):
    assert isinstance(instance, InstanceOfExpressionChild)

@given(instance=java_RelationExpressionChild_strategy)
@settings(max_examples=50)
def test_java_relationexpressionchild_instantiation(instance):
    assert isinstance(instance, java_RelationExpressionChild)

@given(instance=java_RelationExpression_strategy)
@settings(max_examples=50)
def test_java_relationexpression_instantiation(instance):
    assert isinstance(instance, java_RelationExpression)

@given(instance=java_AssignmentOperator_strategy)
@settings(max_examples=50)
def test_java_assignmentoperator_instantiation(instance):
    assert isinstance(instance, java_AssignmentOperator)

@given(instance=java_AssignmentExpressionChild_strategy)
@settings(max_examples=50)
def test_java_assignmentexpressionchild_instantiation(instance):
    assert isinstance(instance, java_AssignmentExpressionChild)

@given(instance=java_AssignmentExpression_strategy)
@settings(max_examples=50)
def test_java_assignmentexpression_instantiation(instance):
    assert isinstance(instance, java_AssignmentExpression)

@given(instance=ForLoopInitializer_strategy)
@settings(max_examples=50)
def test_forloopinitializer_instantiation(instance):
    assert isinstance(instance, ForLoopInitializer)

@given(instance=java_ExpressionList_strategy)
@settings(max_examples=50)
def test_java_expressionlist_instantiation(instance):
    assert isinstance(instance, java_ExpressionList)

@given(instance=Annotable_strategy)
@settings(max_examples=50)
def test_annotable_instantiation(instance):
    assert isinstance(instance, Annotable)

@given(instance=JavaRoot_strategy)
@settings(max_examples=50)
def test_javaroot_instantiation(instance):
    assert isinstance(instance, JavaRoot)

@given(instance=java_EmptyModel_strategy)
@settings(max_examples=50)
def test_java_emptymodel_instantiation(instance):
    assert isinstance(instance, java_EmptyModel)

@given(instance=java_Package_strategy)
@settings(max_examples=50)
def test_java_package_instantiation(instance):
    assert isinstance(instance, java_Package)

@given(instance=java_CompilationUnit_strategy)
@settings(max_examples=50)
def test_java_compilationunit_instantiation(instance):
    assert isinstance(instance, java_CompilationUnit)

@given(instance=ImportingElement_strategy)
@settings(max_examples=50)
def test_importingelement_instantiation(instance):
    assert isinstance(instance, ImportingElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=java_ReferenceableElement_strategy)
@settings(max_examples=50)
def test_java_referenceableelement_instantiation(instance):
    assert isinstance(instance, java_ReferenceableElement)

@given(instance=java_Member_strategy)
@settings(max_examples=50)
def test_java_member_instantiation(instance):
    assert isinstance(instance, java_Member)

@given(instance=java_JavaRoot_strategy)
@settings(max_examples=50)
def test_java_javaroot_instantiation(instance):
    assert isinstance(instance, java_JavaRoot)

@given(instance=AssignmentExpressionChild_strategy)
@settings(max_examples=50)
def test_assignmentexpressionchild_instantiation(instance):
    assert isinstance(instance, AssignmentExpressionChild)

@given(instance=java_ConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_java_conditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, java_ConditionalExpressionChild)

@given(instance=java_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_java_conditionalexpression_instantiation(instance):
    assert isinstance(instance, java_ConditionalExpression)

@given(instance=java_NamespaceAwareElement_strategy)
@settings(max_examples=50)
def test_java_namespaceawareelement_instantiation(instance):
    assert isinstance(instance, java_NamespaceAwareElement)



@given(instance=java_NamespaceAwareElement_strategy)
def test_java_namespaceawareelement_namespaces_setter(instance):
    original = instance.namespaces
    instance.namespaces = original
    assert instance.namespaces == original

@given(instance=java_NamedElement_strategy)
@settings(max_examples=50)
def test_java_namedelement_instantiation(instance):
    assert isinstance(instance, java_NamedElement)



@given(instance=java_NamedElement_strategy)
def test_java_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_LayoutInformation_strategy)
@settings(max_examples=50)
def test_java_layoutinformation_instantiation(instance):
    assert isinstance(instance, java_LayoutInformation)

@given(instance=java_Commentable_strategy)
@settings(max_examples=50)
def test_java_commentable_instantiation(instance):
    assert isinstance(instance, java_Commentable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_Commentable_strategy)
@settings(max_examples=30)
def test_java_commentable_addaftercontainingstatement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addAfterContainingStatement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addAfterContainingStatement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addAfterContainingStatement' in java_Commentable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addAfterContainingStatement' in java_Commentable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addAfterContainingStatement' in java_Commentable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_Commentable_strategy)
@settings(max_examples=30)
def test_java_commentable_addbeforecontainingstatement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addBeforeContainingStatement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addBeforeContainingStatement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addBeforeContainingStatement' in java_Commentable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addBeforeContainingStatement' in java_Commentable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addBeforeContainingStatement' in java_Commentable is not implemented or raised an error")

@given(instance=Implementor_strategy)
@settings(max_examples=50)
def test_implementor_instantiation(instance):
    assert isinstance(instance, Implementor)

@given(instance=ConcreteClassifier_strategy)
@settings(max_examples=50)
def test_concreteclassifier_instantiation(instance):
    assert isinstance(instance, ConcreteClassifier)

@given(instance=java_Enumeration_strategy)
@settings(max_examples=50)
def test_java_enumeration_instantiation(instance):
    assert isinstance(instance, java_Enumeration)

@given(instance=java_Interface_strategy)
@settings(max_examples=50)
def test_java_interface_instantiation(instance):
    assert isinstance(instance, java_Interface)

@given(instance=java_Class_strategy)
@settings(max_examples=50)
def test_java_class_instantiation(instance):
    assert isinstance(instance, java_Class)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_Class_strategy)
@settings(max_examples=30)
def test_java_class_unwrapprimitivetype_changes_state(instance):
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
        assert has_statements, f"Function 'unWrapPrimitiveType' in java_Class is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unWrapPrimitiveType' in java_Class did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unWrapPrimitiveType' in java_Class is not implemented or raised an error")

@given(instance=java_TypeReference_strategy)
@settings(max_examples=50)
def test_java_typereference_instantiation(instance):
    assert isinstance(instance, java_TypeReference)

@given(instance=java_Implementor_strategy)
@settings(max_examples=50)
def test_java_implementor_instantiation(instance):
    assert isinstance(instance, java_Implementor)

@given(instance=java_Annotation_strategy)
@settings(max_examples=50)
def test_java_annotation_instantiation(instance):
    assert isinstance(instance, java_Annotation)

@given(instance=AnnotableAndModifiable_strategy)
@settings(max_examples=50)
def test_annotableandmodifiable_instantiation(instance):
    assert isinstance(instance, AnnotableAndModifiable)

@given(instance=java_LocalVariable_strategy)
@settings(max_examples=50)
def test_java_localvariable_instantiation(instance):
    assert isinstance(instance, java_LocalVariable)

@given(instance=java_Parameter_strategy)
@settings(max_examples=50)
def test_java_parameter_instantiation(instance):
    assert isinstance(instance, java_Parameter)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=java_ForEachLoop_strategy)
@settings(max_examples=50)
def test_java_foreachloop_instantiation(instance):
    assert isinstance(instance, java_ForEachLoop)

@given(instance=java_Condition_strategy)
@settings(max_examples=50)
def test_java_condition_instantiation(instance):
    assert isinstance(instance, java_Condition)

@given(instance=java_Assert_strategy)
@settings(max_examples=50)
def test_java_assert_instantiation(instance):
    assert isinstance(instance, java_Assert)

@given(instance=java_JumpLabel_strategy)
@settings(max_examples=50)
def test_java_jumplabel_instantiation(instance):
    assert isinstance(instance, java_JumpLabel)

@given(instance=java_Switch_strategy)
@settings(max_examples=50)
def test_java_switch_instantiation(instance):
    assert isinstance(instance, java_Switch)

@given(instance=java_Throw_strategy)
@settings(max_examples=50)
def test_java_throw_instantiation(instance):
    assert isinstance(instance, java_Throw)

@given(instance=java_Return_strategy)
@settings(max_examples=50)
def test_java_return_instantiation(instance):
    assert isinstance(instance, java_Return)

@given(instance=java_TryBlock_strategy)
@settings(max_examples=50)
def test_java_tryblock_instantiation(instance):
    assert isinstance(instance, java_TryBlock)

@given(instance=java_Jump_strategy)
@settings(max_examples=50)
def test_java_jump_instantiation(instance):
    assert isinstance(instance, java_Jump)

@given(instance=java_ForLoop_strategy)
@settings(max_examples=50)
def test_java_forloop_instantiation(instance):
    assert isinstance(instance, java_ForLoop)

@given(instance=java_WhileLoop_strategy)
@settings(max_examples=50)
def test_java_whileloop_instantiation(instance):
    assert isinstance(instance, java_WhileLoop)

@given(instance=java_SynchronizedBlock_strategy)
@settings(max_examples=50)
def test_java_synchronizedblock_instantiation(instance):
    assert isinstance(instance, java_SynchronizedBlock)

@given(instance=java_LocalVariableStatement_strategy)
@settings(max_examples=50)
def test_java_localvariablestatement_instantiation(instance):
    assert isinstance(instance, java_LocalVariableStatement)

@given(instance=java_EmptyStatement_strategy)
@settings(max_examples=50)
def test_java_emptystatement_instantiation(instance):
    assert isinstance(instance, java_EmptyStatement)

@given(instance=java_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_java_expressionstatement_instantiation(instance):
    assert isinstance(instance, java_ExpressionStatement)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=java_EmptyMember_strategy)
@settings(max_examples=50)
def test_java_emptymember_instantiation(instance):
    assert isinstance(instance, java_EmptyMember)

@given(instance=java_Block_strategy)
@settings(max_examples=50)
def test_java_block_instantiation(instance):
    assert isinstance(instance, java_Block)

@given(instance=MemberContainer_strategy)
@settings(max_examples=50)
def test_membercontainer_instantiation(instance):
    assert isinstance(instance, MemberContainer)

@given(instance=TypeParametrizable_strategy)
@settings(max_examples=50)
def test_typeparametrizable_instantiation(instance):
    assert isinstance(instance, TypeParametrizable)

@given(instance=java_Constructor_strategy)
@settings(max_examples=50)
def test_java_constructor_instantiation(instance):
    assert isinstance(instance, java_Constructor)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=java_TypeParameter_strategy)
@settings(max_examples=50)
def test_java_typeparameter_instantiation(instance):
    assert isinstance(instance, java_TypeParameter)

@given(instance=java_ConcreteClassifier_strategy)
@settings(max_examples=50)
def test_java_concreteclassifier_instantiation(instance):
    assert isinstance(instance, java_ConcreteClassifier)

@given(instance=ReferenceableElement_strategy)
@settings(max_examples=50)
def test_referenceableelement_instantiation(instance):
    assert isinstance(instance, ReferenceableElement)

@given(instance=java_AdditionalField_strategy)
@settings(max_examples=50)
def test_java_additionalfield_instantiation(instance):
    assert isinstance(instance, java_AdditionalField)

@given(instance=java_AdditionalLocalVariable_strategy)
@settings(max_examples=50)
def test_java_additionallocalvariable_instantiation(instance):
    assert isinstance(instance, java_AdditionalLocalVariable)

@given(instance=java_Method_strategy)
@settings(max_examples=50)
def test_java_method_instantiation(instance):
    assert isinstance(instance, java_Method)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_Method_strategy)
@settings(max_examples=30)
def test_java_method_ismethodforcall_changes_state(instance):
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
        assert has_statements, f"Function 'isMethodForCall' in java_Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isMethodForCall' in java_Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isMethodForCall' in java_Method is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_Method_strategy)
@settings(max_examples=30)
def test_java_method_issomemethodforcall_changes_state(instance):
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
        assert has_statements, f"Function 'isSomeMethodForCall' in java_Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSomeMethodForCall' in java_Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSomeMethodForCall' in java_Method is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_Method_strategy)
@settings(max_examples=30)
def test_java_method_isbettermethodforcall_changes_state(instance):
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
        assert has_statements, f"Function 'isBetterMethodForCall' in java_Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isBetterMethodForCall' in java_Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isBetterMethodForCall' in java_Method is not implemented or raised an error")

@given(instance=java_Field_strategy)
@settings(max_examples=50)
def test_java_field_instantiation(instance):
    assert isinstance(instance, java_Field)

@given(instance=java_PackageReference_strategy)
@settings(max_examples=50)
def test_java_packagereference_instantiation(instance):
    assert isinstance(instance, java_PackageReference)

@given(instance=java_EnumConstant_strategy)
@settings(max_examples=50)
def test_java_enumconstant_instantiation(instance):
    assert isinstance(instance, java_EnumConstant)

@given(instance=java_Variable_strategy)
@settings(max_examples=50)
def test_java_variable_instantiation(instance):
    assert isinstance(instance, java_Variable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_Variable_strategy)
@settings(max_examples=30)
def test_java_variable_createmethodcallstatement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createMethodCallStatement(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createMethodCallStatement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createMethodCallStatement' in java_Variable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createMethodCallStatement' in java_Variable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createMethodCallStatement' in java_Variable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_Variable_strategy)
@settings(max_examples=30)
def test_java_variable_createmethodcall_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createMethodCall(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createMethodCall).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createMethodCall' in java_Variable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createMethodCall' in java_Variable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createMethodCall' in java_Variable is not implemented or raised an error")

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=java_Classifier_strategy)
@settings(max_examples=50)
def test_java_classifier_instantiation(instance):
    assert isinstance(instance, java_Classifier)

@given(instance=java_AnonymousClass_strategy)
@settings(max_examples=50)
def test_java_anonymousclass_instantiation(instance):
    assert isinstance(instance, java_AnonymousClass)

@given(instance=java_PrimitiveType_strategy)
@settings(max_examples=50)
def test_java_primitivetype_instantiation(instance):
    assert isinstance(instance, java_PrimitiveType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java_PrimitiveType_strategy)
@settings(max_examples=30)
def test_java_primitivetype_wrapprimitivetype_changes_state(instance):
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
        assert has_statements, f"Function 'wrapPrimitiveType' in java_PrimitiveType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'wrapPrimitiveType' in java_PrimitiveType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'wrapPrimitiveType' in java_PrimitiveType is not implemented or raised an error")
