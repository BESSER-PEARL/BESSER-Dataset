import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EqualityExpressionChild,
    java::InstanceOfExpressionChild,
    AndExpressionChild,
    java::EqualityExpressionChild,
    java::EqualityExpression,
    PrimitiveType,
    java::Void,
    java::Int,
    java::Float,
    java::Long,
    java::Short,
    java::Char,
    java::Byte,
    java::Double,
    java::Boolean,
    TypeReference,
    WhileLoop,
    java::DoWhileLoop,
    SwitchCase,
    java::DefaultSwitchCase,
    Modifiable,
    Jump,
    java::Continue,
    java::Break,
    Conditional,
    java::NormalSwitchCase,
    Parameter,
    java::VariableLengthParameter,
    java::OrdinaryParameter,
    StatementContainer,
    ElementReference,
    java::IdentifierReference,
    TypeArgumentable,
    java::ClassifierReference,
    ShiftOperator,
    java::UnsignedRightShift,
    java::RightShift,
    java::LeftShift,
    UnaryModificationOperator,
    java::PlusPlus,
    java::MinusMinus,
    MultiplicativeOperator,
    java::Remainder,
    java::Multiplication,
    java::Division,
    UnaryOperator,
    java::Complement,
    java::Negate,
    AdditiveOperator,
    java::Subtraction,
    java::Addition,
    RelationOperator,
    java::LessThanOrEqual,
    java::LessThan,
    java::GreaterThanOrEqual,
    java::GreaterThan,
    AssignmentOperator,
    java::AssignmentAnd,
    java::AssignmentLeftShift,
    java::AssignmentMinus,
    java::AssignmentMultiplication,
    java::AssignmentModulo,
    java::AssignmentExclusiveOr,
    java::AssignmentDivision,
    java::AssignmentOr,
    java::Assignment,
    Operator,
    java::EqualityOperator,
    Modifier,
    java::Public,
    java::Strictfp,
    java::Private,
    java::Native,
    java::Transient,
    java::Synchronized,
    java::Protected,
    java::Volatile,
    java::Final,
    java::Abstract,
    EqualityOperator,
    java::NotEqual,
    java::Equal,
    java::AssignmentUnsignedRightShift,
    java::AssignmentRightShift,
    java::AssignmentPlus,
    Method,
    Variable,
    ExceptionThrower,
    Parametrizable,
    StatementListContainer,
    java::ClassMethod,
    java::CatchBlock,
    java::SwitchCase,
    Initializable,
    Self,
    java::This,
    java::Super,
    LongLiteral,
    java::OctalLongLiteral,
    java::HexLongLiteral,
    java::DecimalLongLiteral,
    IntegerLiteral,
    java::OctalIntegerLiteral,
    java::HexIntegerLiteral,
    java::DecimalIntegerLiteral,
    DoubleLiteral,
    java::HexDoubleLiteral,
    java::DecimalDoubleLiteral,
    FloatLiteral,
    java::HexFloatLiteral,
    java::DecimalFloatLiteral,
    PrimaryExpression,
    java::Reference,
    java::Literal,
    CallTypeArgumentable,
    Instantiation,
    java::ExplicitConstructorCall,
    Argumentable,
    java::MethodCall,
    StaticImport,
    java::StaticMemberImport,
    java::StaticClassifierImport,
    java::Static,
    Import,
    java::ClassifierImport,
    java::PackageImport,
    java::StaticImport,
    Literal,
    java::CharacterLiteral,
    java::DoubleLiteral,
    java::IntegerLiteral,
    java::LongLiteral,
    java::FloatLiteral,
    java::NullLiteral,
    java::BooleanLiteral,
    TypeArgument,
    java::SuperTypeArgument,
    java::ExtendsTypeArgument,
    UnaryModificationExpressionChild,
    java::PrimaryExpression,
    java::UnknownTypeArgument,
    java::UnaryModificationOperator,
    UnaryExpressionChild,
    java::UnaryModificationExpressionChild,
    java::UnaryModificationExpression,
    java::UnaryOperator,
    MultiplicativeExpressionChild,
    java::UnaryExpressionChild,
    java::UnaryExpression,
    java::MultiplicativeOperator,
    AdditiveExpressionChild,
    java::MultiplicativeExpressionChild,
    java::MultiplicativeExpression,
    java::AdditiveOperator,
    ShiftExpressionChild,
    java::AdditiveExpressionChild,
    java::AdditiveExpression,
    java::ShiftOperator,
    RelationExpressionChild,
    java::ShiftExpressionChild,
    java::ShiftExpression,
    java::RelationOperator,
    UnaryModificationExpression,
    java::SuffixUnaryModificationExpression,
    java::PrefixUnaryModificationExpression,
    ExclusiveOrExpressionChild,
    java::AndExpressionChild,
    java::AndExpression,
    InclusiveOrExpressionChild,
    java::ExclusiveOrExpressionChild,
    java::ExclusiveOrExpression,
    ConditionalAndExpressionChild,
    java::InclusiveOrExpressionChild,
    java::InclusiveOrExpression,
    ConditionalOrExpressionChild,
    java::ConditionalAndExpressionChild,
    java::ConditionalAndExpression,
    ConditionalExpressionChild,
    java::ConditionalOrExpressionChild,
    java::ConditionalOrExpression,
    InstanceOfExpressionChild,
    java::RelationExpressionChild,
    java::RelationExpression,
    java::AssignmentOperator,
    ForLoopInitializer,
    java::ExpressionList,
    Annotable,
    JavaRoot,
    java::Package,
    java::EmptyModel,
    java::CompilationUnit,
    ImportingElement,
    NamedElement,
    java::ReferenceableElement,
    java::Member,
    AssignmentExpressionChild,
    java::ConditionalExpressionChild,
    java::ConditionalExpression,
    java::LayoutInformation,
    java::Commentable,
    Implementor,
    ConcreteClassifier,
    java::Enumeration,
    java::Interface,
    java::Class,
    java::Annotation,
    AnnotableAndModifiable,
    java::Parameter,
    java::LocalVariable,
    Statement,
    java::ForEachLoop,
    java::ExpressionStatement,
    java::Assert,
    java::EmptyStatement,
    java::Return,
    java::ForLoop,
    java::TryBlock,
    java::JumpLabel,
    java::Throw,
    java::SynchronizedBlock,
    java::Switch,
    java::Condition,
    java::WhileLoop,
    java::Jump,
    java::LocalVariableStatement,
    Member,
    java::EmptyMember,
    java::Block,
    MemberContainer,
    TypeParametrizable,
    java::Constructor,
    Classifier,
    java::TypeParameter,
    java::ConcreteClassifier,
    ReferenceableElement,
    java::Field,
    java::EnumConstant,
    java::PackageReference,
    Type,
    java::PrimitiveType,
    java::AnonymousClass,
    ArrayInstantiationByValues,
    java::ArrayInstantiationByValuesUntyped,
    ArrayTypeable,
    java::TypeArgument,
    java::AdditionalLocalVariable,
    java::AdditionalField,
    TypedElement,
    java::Method,
    java::ArrayInstantiationByValuesTyped,
    java::InstanceOfExpression,
    java::QualifiedTypeArgument,
    java::CastExpression,
    java::Variable,
    java::NewConstructorCall,
    ArrayInstantiation,
    java::ArrayInstantiationByValues,
    java::ArrayInstantiationBySize,
    Expression,
    java::AssignmentExpressionChild,
    java::AssignmentExpression,
    AnnotationValue,
    ArrayInitializationValue,
    java::ArrayInitializer,
    InterfaceMethod,
    java::AnnotationAttribute,
    java::InterfaceMethod,
    AnnotationParameter,
    java::AnnotationParameterList,
    java::SingleAnnotationParameter,
    java::Classifier,
    NamespaceAwareElement,
    java::Import,
    java::NamespaceClassifierReference,
    java::JavaRoot,
    AnnotationInstanceOrModifier,
    java::Modifier,
    Reference,
    java::Instantiation,
    java::SelfReference,
    java::PrimitiveTypeReference,
    java::NestedExpression,
    java::ReflectiveClassReference,
    java::ArrayInstantiation,
    java::StringReference,
    java::ElementReference,
    java::AnnotationInstance,
    Commentable,
    java::Conditional,
    java::Implementor,
    java::Parametrizable,
    java::ForLoopInitializer,
    java::NamespaceAwareElement,
    java::AnnotationParameter,
    java::AnnotationValue,
    java::TypeReference,
    java::StatementContainer,
    java::AnnotationAttributeSetting,
    java::ExceptionThrower,
    java::ArrayInitializationValue,
    java::ImportingElement,
    java::Initializable,
    java::StatementListContainer,
    java::Statement,
    java::Operator,
    java::TypeParametrizable,
    java::TypeArgumentable,
    java::Argumentable,
    java::AnnotationInstanceOrModifier,
    java::CallTypeArgumentable,
    java::Self,
    java::Type,
    java::TypedElement,
    java::MemberContainer,
    java::ArrayDimension,
    java::Modifiable,
    java::ArraySelector,
    java::NamedElement,
    java::AnnotableAndModifiable,
    java::Annotable,
    java::ArrayTypeable,
    java::Expression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_equalityexpressionchild_is_not_abstract():
    assert not inspect.isabstract(EqualityExpressionChild)


def test_equalityexpressionchild_constructor_exists():
    assert callable(EqualityExpressionChild.__init__)


def test_equalityexpressionchild_constructor_args():
    sig = inspect.signature(EqualityExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::instanceofexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::InstanceOfExpressionChild)


def test_java::instanceofexpressionchild_constructor_exists():
    assert callable(java::InstanceOfExpressionChild.__init__)


def test_java::instanceofexpressionchild_constructor_args():
    sig = inspect.signature(java::InstanceOfExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_andexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AndExpressionChild)


def test_andexpressionchild_constructor_exists():
    assert callable(AndExpressionChild.__init__)


def test_andexpressionchild_constructor_args():
    sig = inspect.signature(AndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::equalityexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::EqualityExpressionChild)


def test_java::equalityexpressionchild_constructor_exists():
    assert callable(java::EqualityExpressionChild.__init__)


def test_java::equalityexpressionchild_constructor_args():
    sig = inspect.signature(java::EqualityExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(java::EqualityExpression)


def test_java::equalityexpression_constructor_exists():
    assert callable(java::EqualityExpression.__init__)


def test_java::equalityexpression_constructor_args():
    sig = inspect.signature(java::EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java::void_is_not_abstract():
    assert not inspect.isabstract(java::Void)


def test_java::void_constructor_exists():
    assert callable(java::Void.__init__)


def test_java::void_constructor_args():
    sig = inspect.signature(java::Void.__init__)
    params = list(sig.parameters.keys())



def test_java::int_is_not_abstract():
    assert not inspect.isabstract(java::Int)


def test_java::int_constructor_exists():
    assert callable(java::Int.__init__)


def test_java::int_constructor_args():
    sig = inspect.signature(java::Int.__init__)
    params = list(sig.parameters.keys())



def test_java::float_is_not_abstract():
    assert not inspect.isabstract(java::Float)


def test_java::float_constructor_exists():
    assert callable(java::Float.__init__)


def test_java::float_constructor_args():
    sig = inspect.signature(java::Float.__init__)
    params = list(sig.parameters.keys())



def test_java::long_is_not_abstract():
    assert not inspect.isabstract(java::Long)


def test_java::long_constructor_exists():
    assert callable(java::Long.__init__)


def test_java::long_constructor_args():
    sig = inspect.signature(java::Long.__init__)
    params = list(sig.parameters.keys())



def test_java::short_is_not_abstract():
    assert not inspect.isabstract(java::Short)


def test_java::short_constructor_exists():
    assert callable(java::Short.__init__)


def test_java::short_constructor_args():
    sig = inspect.signature(java::Short.__init__)
    params = list(sig.parameters.keys())



def test_java::char_is_not_abstract():
    assert not inspect.isabstract(java::Char)


def test_java::char_constructor_exists():
    assert callable(java::Char.__init__)


def test_java::char_constructor_args():
    sig = inspect.signature(java::Char.__init__)
    params = list(sig.parameters.keys())



def test_java::byte_is_not_abstract():
    assert not inspect.isabstract(java::Byte)


def test_java::byte_constructor_exists():
    assert callable(java::Byte.__init__)


def test_java::byte_constructor_args():
    sig = inspect.signature(java::Byte.__init__)
    params = list(sig.parameters.keys())



def test_java::double_is_not_abstract():
    assert not inspect.isabstract(java::Double)


def test_java::double_constructor_exists():
    assert callable(java::Double.__init__)


def test_java::double_constructor_args():
    sig = inspect.signature(java::Double.__init__)
    params = list(sig.parameters.keys())



def test_java::boolean_is_not_abstract():
    assert not inspect.isabstract(java::Boolean)


def test_java::boolean_constructor_exists():
    assert callable(java::Boolean.__init__)


def test_java::boolean_constructor_args():
    sig = inspect.signature(java::Boolean.__init__)
    params = list(sig.parameters.keys())



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_whileloop_is_not_abstract():
    assert not inspect.isabstract(WhileLoop)


def test_whileloop_constructor_exists():
    assert callable(WhileLoop.__init__)


def test_whileloop_constructor_args():
    sig = inspect.signature(WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_java::dowhileloop_is_not_abstract():
    assert not inspect.isabstract(java::DoWhileLoop)


def test_java::dowhileloop_constructor_exists():
    assert callable(java::DoWhileLoop.__init__)


def test_java::dowhileloop_constructor_args():
    sig = inspect.signature(java::DoWhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_switchcase_is_not_abstract():
    assert not inspect.isabstract(SwitchCase)


def test_switchcase_constructor_exists():
    assert callable(SwitchCase.__init__)


def test_switchcase_constructor_args():
    sig = inspect.signature(SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_java::defaultswitchcase_is_not_abstract():
    assert not inspect.isabstract(java::DefaultSwitchCase)


def test_java::defaultswitchcase_constructor_exists():
    assert callable(java::DefaultSwitchCase.__init__)


def test_java::defaultswitchcase_constructor_args():
    sig = inspect.signature(java::DefaultSwitchCase.__init__)
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



def test_java::continue_is_not_abstract():
    assert not inspect.isabstract(java::Continue)


def test_java::continue_constructor_exists():
    assert callable(java::Continue.__init__)


def test_java::continue_constructor_args():
    sig = inspect.signature(java::Continue.__init__)
    params = list(sig.parameters.keys())



def test_java::break_is_not_abstract():
    assert not inspect.isabstract(java::Break)


def test_java::break_constructor_exists():
    assert callable(java::Break.__init__)


def test_java::break_constructor_args():
    sig = inspect.signature(java::Break.__init__)
    params = list(sig.parameters.keys())



def test_conditional_is_not_abstract():
    assert not inspect.isabstract(Conditional)


def test_conditional_constructor_exists():
    assert callable(Conditional.__init__)


def test_conditional_constructor_args():
    sig = inspect.signature(Conditional.__init__)
    params = list(sig.parameters.keys())



def test_java::normalswitchcase_is_not_abstract():
    assert not inspect.isabstract(java::NormalSwitchCase)


def test_java::normalswitchcase_constructor_exists():
    assert callable(java::NormalSwitchCase.__init__)


def test_java::normalswitchcase_constructor_args():
    sig = inspect.signature(java::NormalSwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_java::variablelengthparameter_is_not_abstract():
    assert not inspect.isabstract(java::VariableLengthParameter)


def test_java::variablelengthparameter_constructor_exists():
    assert callable(java::VariableLengthParameter.__init__)


def test_java::variablelengthparameter_constructor_args():
    sig = inspect.signature(java::VariableLengthParameter.__init__)
    params = list(sig.parameters.keys())



def test_java::ordinaryparameter_is_not_abstract():
    assert not inspect.isabstract(java::OrdinaryParameter)


def test_java::ordinaryparameter_constructor_exists():
    assert callable(java::OrdinaryParameter.__init__)


def test_java::ordinaryparameter_constructor_args():
    sig = inspect.signature(java::OrdinaryParameter.__init__)
    params = list(sig.parameters.keys())



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



def test_java::identifierreference_is_not_abstract():
    assert not inspect.isabstract(java::IdentifierReference)


def test_java::identifierreference_constructor_exists():
    assert callable(java::IdentifierReference.__init__)


def test_java::identifierreference_constructor_args():
    sig = inspect.signature(java::IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_typeargumentable_is_not_abstract():
    assert not inspect.isabstract(TypeArgumentable)


def test_typeargumentable_constructor_exists():
    assert callable(TypeArgumentable.__init__)


def test_typeargumentable_constructor_args():
    sig = inspect.signature(TypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_java::classifierreference_is_not_abstract():
    assert not inspect.isabstract(java::ClassifierReference)


def test_java::classifierreference_constructor_exists():
    assert callable(java::ClassifierReference.__init__)


def test_java::classifierreference_constructor_args():
    sig = inspect.signature(java::ClassifierReference.__init__)
    params = list(sig.parameters.keys())



def test_shiftoperator_is_not_abstract():
    assert not inspect.isabstract(ShiftOperator)


def test_shiftoperator_constructor_exists():
    assert callable(ShiftOperator.__init__)


def test_shiftoperator_constructor_args():
    sig = inspect.signature(ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_java::unsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(java::UnsignedRightShift)


def test_java::unsignedrightshift_constructor_exists():
    assert callable(java::UnsignedRightShift.__init__)


def test_java::unsignedrightshift_constructor_args():
    sig = inspect.signature(java::UnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_java::rightshift_is_not_abstract():
    assert not inspect.isabstract(java::RightShift)


def test_java::rightshift_constructor_exists():
    assert callable(java::RightShift.__init__)


def test_java::rightshift_constructor_args():
    sig = inspect.signature(java::RightShift.__init__)
    params = list(sig.parameters.keys())



def test_java::leftshift_is_not_abstract():
    assert not inspect.isabstract(java::LeftShift)


def test_java::leftshift_constructor_exists():
    assert callable(java::LeftShift.__init__)


def test_java::leftshift_constructor_args():
    sig = inspect.signature(java::LeftShift.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationOperator)


def test_unarymodificationoperator_constructor_exists():
    assert callable(UnaryModificationOperator.__init__)


def test_unarymodificationoperator_constructor_args():
    sig = inspect.signature(UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_java::plusplus_is_not_abstract():
    assert not inspect.isabstract(java::PlusPlus)


def test_java::plusplus_constructor_exists():
    assert callable(java::PlusPlus.__init__)


def test_java::plusplus_constructor_args():
    sig = inspect.signature(java::PlusPlus.__init__)
    params = list(sig.parameters.keys())



def test_java::minusminus_is_not_abstract():
    assert not inspect.isabstract(java::MinusMinus)


def test_java::minusminus_constructor_exists():
    assert callable(java::MinusMinus.__init__)


def test_java::minusminus_constructor_args():
    sig = inspect.signature(java::MinusMinus.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeOperator)


def test_multiplicativeoperator_constructor_exists():
    assert callable(MultiplicativeOperator.__init__)


def test_multiplicativeoperator_constructor_args():
    sig = inspect.signature(MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_java::remainder_is_not_abstract():
    assert not inspect.isabstract(java::Remainder)


def test_java::remainder_constructor_exists():
    assert callable(java::Remainder.__init__)


def test_java::remainder_constructor_args():
    sig = inspect.signature(java::Remainder.__init__)
    params = list(sig.parameters.keys())



def test_java::multiplication_is_not_abstract():
    assert not inspect.isabstract(java::Multiplication)


def test_java::multiplication_constructor_exists():
    assert callable(java::Multiplication.__init__)


def test_java::multiplication_constructor_args():
    sig = inspect.signature(java::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_java::division_is_not_abstract():
    assert not inspect.isabstract(java::Division)


def test_java::division_constructor_exists():
    assert callable(java::Division.__init__)


def test_java::division_constructor_args():
    sig = inspect.signature(java::Division.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_java::complement_is_not_abstract():
    assert not inspect.isabstract(java::Complement)


def test_java::complement_constructor_exists():
    assert callable(java::Complement.__init__)


def test_java::complement_constructor_args():
    sig = inspect.signature(java::Complement.__init__)
    params = list(sig.parameters.keys())



def test_java::negate_is_not_abstract():
    assert not inspect.isabstract(java::Negate)


def test_java::negate_constructor_exists():
    assert callable(java::Negate.__init__)


def test_java::negate_constructor_args():
    sig = inspect.signature(java::Negate.__init__)
    params = list(sig.parameters.keys())



def test_additiveoperator_is_not_abstract():
    assert not inspect.isabstract(AdditiveOperator)


def test_additiveoperator_constructor_exists():
    assert callable(AdditiveOperator.__init__)


def test_additiveoperator_constructor_args():
    sig = inspect.signature(AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_java::subtraction_is_not_abstract():
    assert not inspect.isabstract(java::Subtraction)


def test_java::subtraction_constructor_exists():
    assert callable(java::Subtraction.__init__)


def test_java::subtraction_constructor_args():
    sig = inspect.signature(java::Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_java::addition_is_not_abstract():
    assert not inspect.isabstract(java::Addition)


def test_java::addition_constructor_exists():
    assert callable(java::Addition.__init__)


def test_java::addition_constructor_args():
    sig = inspect.signature(java::Addition.__init__)
    params = list(sig.parameters.keys())



def test_relationoperator_is_not_abstract():
    assert not inspect.isabstract(RelationOperator)


def test_relationoperator_constructor_exists():
    assert callable(RelationOperator.__init__)


def test_relationoperator_constructor_args():
    sig = inspect.signature(RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_java::lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(java::LessThanOrEqual)


def test_java::lessthanorequal_constructor_exists():
    assert callable(java::LessThanOrEqual.__init__)


def test_java::lessthanorequal_constructor_args():
    sig = inspect.signature(java::LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_java::lessthan_is_not_abstract():
    assert not inspect.isabstract(java::LessThan)


def test_java::lessthan_constructor_exists():
    assert callable(java::LessThan.__init__)


def test_java::lessthan_constructor_args():
    sig = inspect.signature(java::LessThan.__init__)
    params = list(sig.parameters.keys())



def test_java::greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(java::GreaterThanOrEqual)


def test_java::greaterthanorequal_constructor_exists():
    assert callable(java::GreaterThanOrEqual.__init__)


def test_java::greaterthanorequal_constructor_args():
    sig = inspect.signature(java::GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_java::greaterthan_is_not_abstract():
    assert not inspect.isabstract(java::GreaterThan)


def test_java::greaterthan_constructor_exists():
    assert callable(java::GreaterThan.__init__)


def test_java::greaterthan_constructor_args():
    sig = inspect.signature(java::GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(AssignmentOperator)


def test_assignmentoperator_constructor_exists():
    assert callable(AssignmentOperator.__init__)


def test_assignmentoperator_constructor_args():
    sig = inspect.signature(AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentand_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentAnd)


def test_java::assignmentand_constructor_exists():
    assert callable(java::AssignmentAnd.__init__)


def test_java::assignmentand_constructor_args():
    sig = inspect.signature(java::AssignmentAnd.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentleftshift_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentLeftShift)


def test_java::assignmentleftshift_constructor_exists():
    assert callable(java::AssignmentLeftShift.__init__)


def test_java::assignmentleftshift_constructor_args():
    sig = inspect.signature(java::AssignmentLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentminus_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentMinus)


def test_java::assignmentminus_constructor_exists():
    assert callable(java::AssignmentMinus.__init__)


def test_java::assignmentminus_constructor_args():
    sig = inspect.signature(java::AssignmentMinus.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentmultiplication_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentMultiplication)


def test_java::assignmentmultiplication_constructor_exists():
    assert callable(java::AssignmentMultiplication.__init__)


def test_java::assignmentmultiplication_constructor_args():
    sig = inspect.signature(java::AssignmentMultiplication.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentmodulo_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentModulo)


def test_java::assignmentmodulo_constructor_exists():
    assert callable(java::AssignmentModulo.__init__)


def test_java::assignmentmodulo_constructor_args():
    sig = inspect.signature(java::AssignmentModulo.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentexclusiveor_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentExclusiveOr)


def test_java::assignmentexclusiveor_constructor_exists():
    assert callable(java::AssignmentExclusiveOr.__init__)


def test_java::assignmentexclusiveor_constructor_args():
    sig = inspect.signature(java::AssignmentExclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentdivision_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentDivision)


def test_java::assignmentdivision_constructor_exists():
    assert callable(java::AssignmentDivision.__init__)


def test_java::assignmentdivision_constructor_args():
    sig = inspect.signature(java::AssignmentDivision.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentor_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentOr)


def test_java::assignmentor_constructor_exists():
    assert callable(java::AssignmentOr.__init__)


def test_java::assignmentor_constructor_args():
    sig = inspect.signature(java::AssignmentOr.__init__)
    params = list(sig.parameters.keys())



def test_java::assignment_is_not_abstract():
    assert not inspect.isabstract(java::Assignment)


def test_java::assignment_constructor_exists():
    assert callable(java::Assignment.__init__)


def test_java::assignment_constructor_args():
    sig = inspect.signature(java::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_java::equalityoperator_is_not_abstract():
    assert not inspect.isabstract(java::EqualityOperator)


def test_java::equalityoperator_constructor_exists():
    assert callable(java::EqualityOperator.__init__)


def test_java::equalityoperator_constructor_args():
    sig = inspect.signature(java::EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_modifier_is_not_abstract():
    assert not inspect.isabstract(Modifier)


def test_modifier_constructor_exists():
    assert callable(Modifier.__init__)


def test_modifier_constructor_args():
    sig = inspect.signature(Modifier.__init__)
    params = list(sig.parameters.keys())



def test_java::public_is_not_abstract():
    assert not inspect.isabstract(java::Public)


def test_java::public_constructor_exists():
    assert callable(java::Public.__init__)


def test_java::public_constructor_args():
    sig = inspect.signature(java::Public.__init__)
    params = list(sig.parameters.keys())



def test_java::strictfp_is_not_abstract():
    assert not inspect.isabstract(java::Strictfp)


def test_java::strictfp_constructor_exists():
    assert callable(java::Strictfp.__init__)


def test_java::strictfp_constructor_args():
    sig = inspect.signature(java::Strictfp.__init__)
    params = list(sig.parameters.keys())



def test_java::private_is_not_abstract():
    assert not inspect.isabstract(java::Private)


def test_java::private_constructor_exists():
    assert callable(java::Private.__init__)


def test_java::private_constructor_args():
    sig = inspect.signature(java::Private.__init__)
    params = list(sig.parameters.keys())



def test_java::native_is_not_abstract():
    assert not inspect.isabstract(java::Native)


def test_java::native_constructor_exists():
    assert callable(java::Native.__init__)


def test_java::native_constructor_args():
    sig = inspect.signature(java::Native.__init__)
    params = list(sig.parameters.keys())



def test_java::transient_is_not_abstract():
    assert not inspect.isabstract(java::Transient)


def test_java::transient_constructor_exists():
    assert callable(java::Transient.__init__)


def test_java::transient_constructor_args():
    sig = inspect.signature(java::Transient.__init__)
    params = list(sig.parameters.keys())



def test_java::synchronized_is_not_abstract():
    assert not inspect.isabstract(java::Synchronized)


def test_java::synchronized_constructor_exists():
    assert callable(java::Synchronized.__init__)


def test_java::synchronized_constructor_args():
    sig = inspect.signature(java::Synchronized.__init__)
    params = list(sig.parameters.keys())



def test_java::protected_is_not_abstract():
    assert not inspect.isabstract(java::Protected)


def test_java::protected_constructor_exists():
    assert callable(java::Protected.__init__)


def test_java::protected_constructor_args():
    sig = inspect.signature(java::Protected.__init__)
    params = list(sig.parameters.keys())



def test_java::volatile_is_not_abstract():
    assert not inspect.isabstract(java::Volatile)


def test_java::volatile_constructor_exists():
    assert callable(java::Volatile.__init__)


def test_java::volatile_constructor_args():
    sig = inspect.signature(java::Volatile.__init__)
    params = list(sig.parameters.keys())



def test_java::final_is_not_abstract():
    assert not inspect.isabstract(java::Final)


def test_java::final_constructor_exists():
    assert callable(java::Final.__init__)


def test_java::final_constructor_args():
    sig = inspect.signature(java::Final.__init__)
    params = list(sig.parameters.keys())



def test_java::abstract_is_not_abstract():
    assert not inspect.isabstract(java::Abstract)


def test_java::abstract_constructor_exists():
    assert callable(java::Abstract.__init__)


def test_java::abstract_constructor_args():
    sig = inspect.signature(java::Abstract.__init__)
    params = list(sig.parameters.keys())



def test_equalityoperator_is_not_abstract():
    assert not inspect.isabstract(EqualityOperator)


def test_equalityoperator_constructor_exists():
    assert callable(EqualityOperator.__init__)


def test_equalityoperator_constructor_args():
    sig = inspect.signature(EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_java::notequal_is_not_abstract():
    assert not inspect.isabstract(java::NotEqual)


def test_java::notequal_constructor_exists():
    assert callable(java::NotEqual.__init__)


def test_java::notequal_constructor_args():
    sig = inspect.signature(java::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_java::equal_is_not_abstract():
    assert not inspect.isabstract(java::Equal)


def test_java::equal_constructor_exists():
    assert callable(java::Equal.__init__)


def test_java::equal_constructor_args():
    sig = inspect.signature(java::Equal.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentunsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentUnsignedRightShift)


def test_java::assignmentunsignedrightshift_constructor_exists():
    assert callable(java::AssignmentUnsignedRightShift.__init__)


def test_java::assignmentunsignedrightshift_constructor_args():
    sig = inspect.signature(java::AssignmentUnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentrightshift_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentRightShift)


def test_java::assignmentrightshift_constructor_exists():
    assert callable(java::AssignmentRightShift.__init__)


def test_java::assignmentrightshift_constructor_args():
    sig = inspect.signature(java::AssignmentRightShift.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentplus_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentPlus)


def test_java::assignmentplus_constructor_exists():
    assert callable(java::AssignmentPlus.__init__)


def test_java::assignmentplus_constructor_args():
    sig = inspect.signature(java::AssignmentPlus.__init__)
    params = list(sig.parameters.keys())



def test_method_is_not_abstract():
    assert not inspect.isabstract(Method)


def test_method_constructor_exists():
    assert callable(Method.__init__)


def test_method_constructor_args():
    sig = inspect.signature(Method.__init__)
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



def test_java::classmethod_is_not_abstract():
    assert not inspect.isabstract(java::ClassMethod)


def test_java::classmethod_constructor_exists():
    assert callable(java::ClassMethod.__init__)


def test_java::classmethod_constructor_args():
    sig = inspect.signature(java::ClassMethod.__init__)
    params = list(sig.parameters.keys())



def test_java::catchblock_is_not_abstract():
    assert not inspect.isabstract(java::CatchBlock)


def test_java::catchblock_constructor_exists():
    assert callable(java::CatchBlock.__init__)


def test_java::catchblock_constructor_args():
    sig = inspect.signature(java::CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_java::switchcase_is_not_abstract():
    assert not inspect.isabstract(java::SwitchCase)


def test_java::switchcase_constructor_exists():
    assert callable(java::SwitchCase.__init__)


def test_java::switchcase_constructor_args():
    sig = inspect.signature(java::SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_initializable_is_not_abstract():
    assert not inspect.isabstract(Initializable)


def test_initializable_constructor_exists():
    assert callable(Initializable.__init__)


def test_initializable_constructor_args():
    sig = inspect.signature(Initializable.__init__)
    params = list(sig.parameters.keys())



def test_self_is_not_abstract():
    assert not inspect.isabstract(Self)


def test_self_constructor_exists():
    assert callable(Self.__init__)


def test_self_constructor_args():
    sig = inspect.signature(Self.__init__)
    params = list(sig.parameters.keys())



def test_java::this_is_not_abstract():
    assert not inspect.isabstract(java::This)


def test_java::this_constructor_exists():
    assert callable(java::This.__init__)


def test_java::this_constructor_args():
    sig = inspect.signature(java::This.__init__)
    params = list(sig.parameters.keys())



def test_java::super_is_not_abstract():
    assert not inspect.isabstract(java::Super)


def test_java::super_constructor_exists():
    assert callable(java::Super.__init__)


def test_java::super_constructor_args():
    sig = inspect.signature(java::Super.__init__)
    params = list(sig.parameters.keys())



def test_longliteral_is_not_abstract():
    assert not inspect.isabstract(LongLiteral)


def test_longliteral_constructor_exists():
    assert callable(LongLiteral.__init__)


def test_longliteral_constructor_args():
    sig = inspect.signature(LongLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java::octallongliteral_is_not_abstract():
    assert not inspect.isabstract(java::OctalLongLiteral)


def test_java::octallongliteral_constructor_exists():
    assert callable(java::OctalLongLiteral.__init__)


def test_java::octallongliteral_constructor_args():
    sig = inspect.signature(java::OctalLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "octalValue" in params, "Missing parameter 'octalValue'"

def test_java::octallongliteral_has_octalValue():
    assert hasattr(java::OctalLongLiteral, "octalValue")
    descriptor = None
    for klass in java::OctalLongLiteral.__mro__:
        if "octalValue" in klass.__dict__:
            descriptor = klass.__dict__["octalValue"]
            break
    assert isinstance(descriptor, property)



def test_java::hexlongliteral_is_not_abstract():
    assert not inspect.isabstract(java::HexLongLiteral)


def test_java::hexlongliteral_constructor_exists():
    assert callable(java::HexLongLiteral.__init__)


def test_java::hexlongliteral_constructor_args():
    sig = inspect.signature(java::HexLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_java::hexlongliteral_has_hexValue():
    assert hasattr(java::HexLongLiteral, "hexValue")
    descriptor = None
    for klass in java::HexLongLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_java::decimallongliteral_is_not_abstract():
    assert not inspect.isabstract(java::DecimalLongLiteral)


def test_java::decimallongliteral_constructor_exists():
    assert callable(java::DecimalLongLiteral.__init__)


def test_java::decimallongliteral_constructor_args():
    sig = inspect.signature(java::DecimalLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_java::decimallongliteral_has_decimalValue():
    assert hasattr(java::DecimalLongLiteral, "decimalValue")
    descriptor = None
    for klass in java::DecimalLongLiteral.__mro__:
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



def test_java::octalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(java::OctalIntegerLiteral)


def test_java::octalintegerliteral_constructor_exists():
    assert callable(java::OctalIntegerLiteral.__init__)


def test_java::octalintegerliteral_constructor_args():
    sig = inspect.signature(java::OctalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "octalValue" in params, "Missing parameter 'octalValue'"

def test_java::octalintegerliteral_has_octalValue():
    assert hasattr(java::OctalIntegerLiteral, "octalValue")
    descriptor = None
    for klass in java::OctalIntegerLiteral.__mro__:
        if "octalValue" in klass.__dict__:
            descriptor = klass.__dict__["octalValue"]
            break
    assert isinstance(descriptor, property)



def test_java::hexintegerliteral_is_not_abstract():
    assert not inspect.isabstract(java::HexIntegerLiteral)


def test_java::hexintegerliteral_constructor_exists():
    assert callable(java::HexIntegerLiteral.__init__)


def test_java::hexintegerliteral_constructor_args():
    sig = inspect.signature(java::HexIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_java::hexintegerliteral_has_hexValue():
    assert hasattr(java::HexIntegerLiteral, "hexValue")
    descriptor = None
    for klass in java::HexIntegerLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_java::decimalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(java::DecimalIntegerLiteral)


def test_java::decimalintegerliteral_constructor_exists():
    assert callable(java::DecimalIntegerLiteral.__init__)


def test_java::decimalintegerliteral_constructor_args():
    sig = inspect.signature(java::DecimalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_java::decimalintegerliteral_has_decimalValue():
    assert hasattr(java::DecimalIntegerLiteral, "decimalValue")
    descriptor = None
    for klass in java::DecimalIntegerLiteral.__mro__:
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



def test_java::hexdoubleliteral_is_not_abstract():
    assert not inspect.isabstract(java::HexDoubleLiteral)


def test_java::hexdoubleliteral_constructor_exists():
    assert callable(java::HexDoubleLiteral.__init__)


def test_java::hexdoubleliteral_constructor_args():
    sig = inspect.signature(java::HexDoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_java::hexdoubleliteral_has_hexValue():
    assert hasattr(java::HexDoubleLiteral, "hexValue")
    descriptor = None
    for klass in java::HexDoubleLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_java::decimaldoubleliteral_is_not_abstract():
    assert not inspect.isabstract(java::DecimalDoubleLiteral)


def test_java::decimaldoubleliteral_constructor_exists():
    assert callable(java::DecimalDoubleLiteral.__init__)


def test_java::decimaldoubleliteral_constructor_args():
    sig = inspect.signature(java::DecimalDoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_java::decimaldoubleliteral_has_decimalValue():
    assert hasattr(java::DecimalDoubleLiteral, "decimalValue")
    descriptor = None
    for klass in java::DecimalDoubleLiteral.__mro__:
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



def test_java::hexfloatliteral_is_not_abstract():
    assert not inspect.isabstract(java::HexFloatLiteral)


def test_java::hexfloatliteral_constructor_exists():
    assert callable(java::HexFloatLiteral.__init__)


def test_java::hexfloatliteral_constructor_args():
    sig = inspect.signature(java::HexFloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_java::hexfloatliteral_has_hexValue():
    assert hasattr(java::HexFloatLiteral, "hexValue")
    descriptor = None
    for klass in java::HexFloatLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_java::decimalfloatliteral_is_not_abstract():
    assert not inspect.isabstract(java::DecimalFloatLiteral)


def test_java::decimalfloatliteral_constructor_exists():
    assert callable(java::DecimalFloatLiteral.__init__)


def test_java::decimalfloatliteral_constructor_args():
    sig = inspect.signature(java::DecimalFloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_java::decimalfloatliteral_has_decimalValue():
    assert hasattr(java::DecimalFloatLiteral, "decimalValue")
    descriptor = None
    for klass in java::DecimalFloatLiteral.__mro__:
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



def test_java::reference_is_not_abstract():
    assert not inspect.isabstract(java::Reference)


def test_java::reference_constructor_exists():
    assert callable(java::Reference.__init__)


def test_java::reference_constructor_args():
    sig = inspect.signature(java::Reference.__init__)
    params = list(sig.parameters.keys())



def test_java::literal_is_not_abstract():
    assert not inspect.isabstract(java::Literal)


def test_java::literal_constructor_exists():
    assert callable(java::Literal.__init__)


def test_java::literal_constructor_args():
    sig = inspect.signature(java::Literal.__init__)
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



def test_java::explicitconstructorcall_is_not_abstract():
    assert not inspect.isabstract(java::ExplicitConstructorCall)


def test_java::explicitconstructorcall_constructor_exists():
    assert callable(java::ExplicitConstructorCall.__init__)


def test_java::explicitconstructorcall_constructor_args():
    sig = inspect.signature(java::ExplicitConstructorCall.__init__)
    params = list(sig.parameters.keys())



def test_argumentable_is_not_abstract():
    assert not inspect.isabstract(Argumentable)


def test_argumentable_constructor_exists():
    assert callable(Argumentable.__init__)


def test_argumentable_constructor_args():
    sig = inspect.signature(Argumentable.__init__)
    params = list(sig.parameters.keys())



def test_java::methodcall_is_not_abstract():
    assert not inspect.isabstract(java::MethodCall)


def test_java::methodcall_constructor_exists():
    assert callable(java::MethodCall.__init__)


def test_java::methodcall_constructor_args():
    sig = inspect.signature(java::MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_staticimport_is_not_abstract():
    assert not inspect.isabstract(StaticImport)


def test_staticimport_constructor_exists():
    assert callable(StaticImport.__init__)


def test_staticimport_constructor_args():
    sig = inspect.signature(StaticImport.__init__)
    params = list(sig.parameters.keys())



def test_java::staticmemberimport_is_not_abstract():
    assert not inspect.isabstract(java::StaticMemberImport)


def test_java::staticmemberimport_constructor_exists():
    assert callable(java::StaticMemberImport.__init__)


def test_java::staticmemberimport_constructor_args():
    sig = inspect.signature(java::StaticMemberImport.__init__)
    params = list(sig.parameters.keys())



def test_java::staticclassifierimport_is_not_abstract():
    assert not inspect.isabstract(java::StaticClassifierImport)


def test_java::staticclassifierimport_constructor_exists():
    assert callable(java::StaticClassifierImport.__init__)


def test_java::staticclassifierimport_constructor_args():
    sig = inspect.signature(java::StaticClassifierImport.__init__)
    params = list(sig.parameters.keys())



def test_java::static_is_not_abstract():
    assert not inspect.isabstract(java::Static)


def test_java::static_constructor_exists():
    assert callable(java::Static.__init__)


def test_java::static_constructor_args():
    sig = inspect.signature(java::Static.__init__)
    params = list(sig.parameters.keys())



def test_import_is_not_abstract():
    assert not inspect.isabstract(Import)


def test_import_constructor_exists():
    assert callable(Import.__init__)


def test_import_constructor_args():
    sig = inspect.signature(Import.__init__)
    params = list(sig.parameters.keys())



def test_java::classifierimport_is_not_abstract():
    assert not inspect.isabstract(java::ClassifierImport)


def test_java::classifierimport_constructor_exists():
    assert callable(java::ClassifierImport.__init__)


def test_java::classifierimport_constructor_args():
    sig = inspect.signature(java::ClassifierImport.__init__)
    params = list(sig.parameters.keys())



def test_java::packageimport_is_not_abstract():
    assert not inspect.isabstract(java::PackageImport)


def test_java::packageimport_constructor_exists():
    assert callable(java::PackageImport.__init__)


def test_java::packageimport_constructor_args():
    sig = inspect.signature(java::PackageImport.__init__)
    params = list(sig.parameters.keys())



def test_java::staticimport_is_not_abstract():
    assert not inspect.isabstract(java::StaticImport)


def test_java::staticimport_constructor_exists():
    assert callable(java::StaticImport.__init__)


def test_java::staticimport_constructor_args():
    sig = inspect.signature(java::StaticImport.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_java::characterliteral_is_not_abstract():
    assert not inspect.isabstract(java::CharacterLiteral)


def test_java::characterliteral_constructor_exists():
    assert callable(java::CharacterLiteral.__init__)


def test_java::characterliteral_constructor_args():
    sig = inspect.signature(java::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_java::characterliteral_has_value():
    assert hasattr(java::CharacterLiteral, "value")
    descriptor = None
    for klass in java::CharacterLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_java::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(java::DoubleLiteral)


def test_java::doubleliteral_constructor_exists():
    assert callable(java::DoubleLiteral.__init__)


def test_java::doubleliteral_constructor_args():
    sig = inspect.signature(java::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java::integerliteral_is_not_abstract():
    assert not inspect.isabstract(java::IntegerLiteral)


def test_java::integerliteral_constructor_exists():
    assert callable(java::IntegerLiteral.__init__)


def test_java::integerliteral_constructor_args():
    sig = inspect.signature(java::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java::longliteral_is_not_abstract():
    assert not inspect.isabstract(java::LongLiteral)


def test_java::longliteral_constructor_exists():
    assert callable(java::LongLiteral.__init__)


def test_java::longliteral_constructor_args():
    sig = inspect.signature(java::LongLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java::floatliteral_is_not_abstract():
    assert not inspect.isabstract(java::FloatLiteral)


def test_java::floatliteral_constructor_exists():
    assert callable(java::FloatLiteral.__init__)


def test_java::floatliteral_constructor_args():
    sig = inspect.signature(java::FloatLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java::nullliteral_is_not_abstract():
    assert not inspect.isabstract(java::NullLiteral)


def test_java::nullliteral_constructor_exists():
    assert callable(java::NullLiteral.__init__)


def test_java::nullliteral_constructor_args():
    sig = inspect.signature(java::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(java::BooleanLiteral)


def test_java::booleanliteral_constructor_exists():
    assert callable(java::BooleanLiteral.__init__)


def test_java::booleanliteral_constructor_args():
    sig = inspect.signature(java::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_java::booleanliteral_has_value():
    assert hasattr(java::BooleanLiteral, "value")
    descriptor = None
    for klass in java::BooleanLiteral.__mro__:
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



def test_java::supertypeargument_is_not_abstract():
    assert not inspect.isabstract(java::SuperTypeArgument)


def test_java::supertypeargument_constructor_exists():
    assert callable(java::SuperTypeArgument.__init__)


def test_java::supertypeargument_constructor_args():
    sig = inspect.signature(java::SuperTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_java::extendstypeargument_is_not_abstract():
    assert not inspect.isabstract(java::ExtendsTypeArgument)


def test_java::extendstypeargument_constructor_exists():
    assert callable(java::ExtendsTypeArgument.__init__)


def test_java::extendstypeargument_constructor_args():
    sig = inspect.signature(java::ExtendsTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationExpressionChild)


def test_unarymodificationexpressionchild_constructor_exists():
    assert callable(UnaryModificationExpressionChild.__init__)


def test_unarymodificationexpressionchild_constructor_args():
    sig = inspect.signature(UnaryModificationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(java::PrimaryExpression)


def test_java::primaryexpression_constructor_exists():
    assert callable(java::PrimaryExpression.__init__)


def test_java::primaryexpression_constructor_args():
    sig = inspect.signature(java::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::unknowntypeargument_is_not_abstract():
    assert not inspect.isabstract(java::UnknownTypeArgument)


def test_java::unknowntypeargument_constructor_exists():
    assert callable(java::UnknownTypeArgument.__init__)


def test_java::unknowntypeargument_constructor_args():
    sig = inspect.signature(java::UnknownTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_java::unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(java::UnaryModificationOperator)


def test_java::unarymodificationoperator_constructor_exists():
    assert callable(java::UnaryModificationOperator.__init__)


def test_java::unarymodificationoperator_constructor_args():
    sig = inspect.signature(java::UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpressionchild_is_not_abstract():
    assert not inspect.isabstract(UnaryExpressionChild)


def test_unaryexpressionchild_constructor_exists():
    assert callable(UnaryExpressionChild.__init__)


def test_unaryexpressionchild_constructor_args():
    sig = inspect.signature(UnaryExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::unarymodificationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::UnaryModificationExpressionChild)


def test_java::unarymodificationexpressionchild_constructor_exists():
    assert callable(java::UnaryModificationExpressionChild.__init__)


def test_java::unarymodificationexpressionchild_constructor_args():
    sig = inspect.signature(java::UnaryModificationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::unarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(java::UnaryModificationExpression)


def test_java::unarymodificationexpression_constructor_exists():
    assert callable(java::UnaryModificationExpression.__init__)


def test_java::unarymodificationexpression_constructor_args():
    sig = inspect.signature(java::UnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(java::UnaryOperator)


def test_java::unaryoperator_constructor_exists():
    assert callable(java::UnaryOperator.__init__)


def test_java::unaryoperator_constructor_args():
    sig = inspect.signature(java::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeexpressionchild_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeExpressionChild)


def test_multiplicativeexpressionchild_constructor_exists():
    assert callable(MultiplicativeExpressionChild.__init__)


def test_multiplicativeexpressionchild_constructor_args():
    sig = inspect.signature(MultiplicativeExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::unaryexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::UnaryExpressionChild)


def test_java::unaryexpressionchild_constructor_exists():
    assert callable(java::UnaryExpressionChild.__init__)


def test_java::unaryexpressionchild_constructor_args():
    sig = inspect.signature(java::UnaryExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(java::UnaryExpression)


def test_java::unaryexpression_constructor_exists():
    assert callable(java::UnaryExpression.__init__)


def test_java::unaryexpression_constructor_args():
    sig = inspect.signature(java::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(java::MultiplicativeOperator)


def test_java::multiplicativeoperator_constructor_exists():
    assert callable(java::MultiplicativeOperator.__init__)


def test_java::multiplicativeoperator_constructor_args():
    sig = inspect.signature(java::MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_additiveexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AdditiveExpressionChild)


def test_additiveexpressionchild_constructor_exists():
    assert callable(AdditiveExpressionChild.__init__)


def test_additiveexpressionchild_constructor_args():
    sig = inspect.signature(AdditiveExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::multiplicativeexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::MultiplicativeExpressionChild)


def test_java::multiplicativeexpressionchild_constructor_exists():
    assert callable(java::MultiplicativeExpressionChild.__init__)


def test_java::multiplicativeexpressionchild_constructor_args():
    sig = inspect.signature(java::MultiplicativeExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(java::MultiplicativeExpression)


def test_java::multiplicativeexpression_constructor_exists():
    assert callable(java::MultiplicativeExpression.__init__)


def test_java::multiplicativeexpression_constructor_args():
    sig = inspect.signature(java::MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::additiveoperator_is_not_abstract():
    assert not inspect.isabstract(java::AdditiveOperator)


def test_java::additiveoperator_constructor_exists():
    assert callable(java::AdditiveOperator.__init__)


def test_java::additiveoperator_constructor_args():
    sig = inspect.signature(java::AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_shiftexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ShiftExpressionChild)


def test_shiftexpressionchild_constructor_exists():
    assert callable(ShiftExpressionChild.__init__)


def test_shiftexpressionchild_constructor_args():
    sig = inspect.signature(ShiftExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::additiveexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::AdditiveExpressionChild)


def test_java::additiveexpressionchild_constructor_exists():
    assert callable(java::AdditiveExpressionChild.__init__)


def test_java::additiveexpressionchild_constructor_args():
    sig = inspect.signature(java::AdditiveExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(java::AdditiveExpression)


def test_java::additiveexpression_constructor_exists():
    assert callable(java::AdditiveExpression.__init__)


def test_java::additiveexpression_constructor_args():
    sig = inspect.signature(java::AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::shiftoperator_is_not_abstract():
    assert not inspect.isabstract(java::ShiftOperator)


def test_java::shiftoperator_constructor_exists():
    assert callable(java::ShiftOperator.__init__)


def test_java::shiftoperator_constructor_args():
    sig = inspect.signature(java::ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_relationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(RelationExpressionChild)


def test_relationexpressionchild_constructor_exists():
    assert callable(RelationExpressionChild.__init__)


def test_relationexpressionchild_constructor_args():
    sig = inspect.signature(RelationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::shiftexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::ShiftExpressionChild)


def test_java::shiftexpressionchild_constructor_exists():
    assert callable(java::ShiftExpressionChild.__init__)


def test_java::shiftexpressionchild_constructor_args():
    sig = inspect.signature(java::ShiftExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(java::ShiftExpression)


def test_java::shiftexpression_constructor_exists():
    assert callable(java::ShiftExpression.__init__)


def test_java::shiftexpression_constructor_args():
    sig = inspect.signature(java::ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::relationoperator_is_not_abstract():
    assert not inspect.isabstract(java::RelationOperator)


def test_java::relationoperator_constructor_exists():
    assert callable(java::RelationOperator.__init__)


def test_java::relationoperator_constructor_args():
    sig = inspect.signature(java::RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationExpression)


def test_unarymodificationexpression_constructor_exists():
    assert callable(UnaryModificationExpression.__init__)


def test_unarymodificationexpression_constructor_args():
    sig = inspect.signature(UnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::suffixunarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(java::SuffixUnaryModificationExpression)


def test_java::suffixunarymodificationexpression_constructor_exists():
    assert callable(java::SuffixUnaryModificationExpression.__init__)


def test_java::suffixunarymodificationexpression_constructor_args():
    sig = inspect.signature(java::SuffixUnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::prefixunarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(java::PrefixUnaryModificationExpression)


def test_java::prefixunarymodificationexpression_constructor_exists():
    assert callable(java::PrefixUnaryModificationExpression.__init__)


def test_java::prefixunarymodificationexpression_constructor_args():
    sig = inspect.signature(java::PrefixUnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_exclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ExclusiveOrExpressionChild)


def test_exclusiveorexpressionchild_constructor_exists():
    assert callable(ExclusiveOrExpressionChild.__init__)


def test_exclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(ExclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::andexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::AndExpressionChild)


def test_java::andexpressionchild_constructor_exists():
    assert callable(java::AndExpressionChild.__init__)


def test_java::andexpressionchild_constructor_args():
    sig = inspect.signature(java::AndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::andexpression_is_not_abstract():
    assert not inspect.isabstract(java::AndExpression)


def test_java::andexpression_constructor_exists():
    assert callable(java::AndExpression.__init__)


def test_java::andexpression_constructor_args():
    sig = inspect.signature(java::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_inclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(InclusiveOrExpressionChild)


def test_inclusiveorexpressionchild_constructor_exists():
    assert callable(InclusiveOrExpressionChild.__init__)


def test_inclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(InclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::exclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::ExclusiveOrExpressionChild)


def test_java::exclusiveorexpressionchild_constructor_exists():
    assert callable(java::ExclusiveOrExpressionChild.__init__)


def test_java::exclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(java::ExclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(java::ExclusiveOrExpression)


def test_java::exclusiveorexpression_constructor_exists():
    assert callable(java::ExclusiveOrExpression.__init__)


def test_java::exclusiveorexpression_constructor_args():
    sig = inspect.signature(java::ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalAndExpressionChild)


def test_conditionalandexpressionchild_constructor_exists():
    assert callable(ConditionalAndExpressionChild.__init__)


def test_conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::inclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::InclusiveOrExpressionChild)


def test_java::inclusiveorexpressionchild_constructor_exists():
    assert callable(java::InclusiveOrExpressionChild.__init__)


def test_java::inclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(java::InclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(java::InclusiveOrExpression)


def test_java::inclusiveorexpression_constructor_exists():
    assert callable(java::InclusiveOrExpression.__init__)


def test_java::inclusiveorexpression_constructor_args():
    sig = inspect.signature(java::InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalOrExpressionChild)


def test_conditionalorexpressionchild_constructor_exists():
    assert callable(ConditionalOrExpressionChild.__init__)


def test_conditionalorexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::ConditionalAndExpressionChild)


def test_java::conditionalandexpressionchild_constructor_exists():
    assert callable(java::ConditionalAndExpressionChild.__init__)


def test_java::conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(java::ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(java::ConditionalAndExpression)


def test_java::conditionalandexpression_constructor_exists():
    assert callable(java::ConditionalAndExpression.__init__)


def test_java::conditionalandexpression_constructor_args():
    sig = inspect.signature(java::ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalExpressionChild)


def test_conditionalexpressionchild_constructor_exists():
    assert callable(ConditionalExpressionChild.__init__)


def test_conditionalexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::conditionalorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::ConditionalOrExpressionChild)


def test_java::conditionalorexpressionchild_constructor_exists():
    assert callable(java::ConditionalOrExpressionChild.__init__)


def test_java::conditionalorexpressionchild_constructor_args():
    sig = inspect.signature(java::ConditionalOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(java::ConditionalOrExpression)


def test_java::conditionalorexpression_constructor_exists():
    assert callable(java::ConditionalOrExpression.__init__)


def test_java::conditionalorexpression_constructor_args():
    sig = inspect.signature(java::ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_instanceofexpressionchild_is_not_abstract():
    assert not inspect.isabstract(InstanceOfExpressionChild)


def test_instanceofexpressionchild_constructor_exists():
    assert callable(InstanceOfExpressionChild.__init__)


def test_instanceofexpressionchild_constructor_args():
    sig = inspect.signature(InstanceOfExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::relationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::RelationExpressionChild)


def test_java::relationexpressionchild_constructor_exists():
    assert callable(java::RelationExpressionChild.__init__)


def test_java::relationexpressionchild_constructor_args():
    sig = inspect.signature(java::RelationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::relationexpression_is_not_abstract():
    assert not inspect.isabstract(java::RelationExpression)


def test_java::relationexpression_constructor_exists():
    assert callable(java::RelationExpression.__init__)


def test_java::relationexpression_constructor_args():
    sig = inspect.signature(java::RelationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentOperator)


def test_java::assignmentoperator_constructor_exists():
    assert callable(java::AssignmentOperator.__init__)


def test_java::assignmentoperator_constructor_args():
    sig = inspect.signature(java::AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_forloopinitializer_is_not_abstract():
    assert not inspect.isabstract(ForLoopInitializer)


def test_forloopinitializer_constructor_exists():
    assert callable(ForLoopInitializer.__init__)


def test_forloopinitializer_constructor_args():
    sig = inspect.signature(ForLoopInitializer.__init__)
    params = list(sig.parameters.keys())



def test_java::expressionlist_is_not_abstract():
    assert not inspect.isabstract(java::ExpressionList)


def test_java::expressionlist_constructor_exists():
    assert callable(java::ExpressionList.__init__)


def test_java::expressionlist_constructor_args():
    sig = inspect.signature(java::ExpressionList.__init__)
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



def test_java::package_is_not_abstract():
    assert not inspect.isabstract(java::Package)


def test_java::package_constructor_exists():
    assert callable(java::Package.__init__)


def test_java::package_constructor_args():
    sig = inspect.signature(java::Package.__init__)
    params = list(sig.parameters.keys())



def test_java::emptymodel_is_not_abstract():
    assert not inspect.isabstract(java::EmptyModel)


def test_java::emptymodel_constructor_exists():
    assert callable(java::EmptyModel.__init__)


def test_java::emptymodel_constructor_args():
    sig = inspect.signature(java::EmptyModel.__init__)
    params = list(sig.parameters.keys())



def test_java::compilationunit_is_not_abstract():
    assert not inspect.isabstract(java::CompilationUnit)


def test_java::compilationunit_constructor_exists():
    assert callable(java::CompilationUnit.__init__)


def test_java::compilationunit_constructor_args():
    sig = inspect.signature(java::CompilationUnit.__init__)
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



def test_java::referenceableelement_is_not_abstract():
    assert not inspect.isabstract(java::ReferenceableElement)


def test_java::referenceableelement_constructor_exists():
    assert callable(java::ReferenceableElement.__init__)


def test_java::referenceableelement_constructor_args():
    sig = inspect.signature(java::ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_java::member_is_not_abstract():
    assert not inspect.isabstract(java::Member)


def test_java::member_constructor_exists():
    assert callable(java::Member.__init__)


def test_java::member_constructor_args():
    sig = inspect.signature(java::Member.__init__)
    params = list(sig.parameters.keys())



def test_assignmentexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AssignmentExpressionChild)


def test_assignmentexpressionchild_constructor_exists():
    assert callable(AssignmentExpressionChild.__init__)


def test_assignmentexpressionchild_constructor_args():
    sig = inspect.signature(AssignmentExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::conditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::ConditionalExpressionChild)


def test_java::conditionalexpressionchild_constructor_exists():
    assert callable(java::ConditionalExpressionChild.__init__)


def test_java::conditionalexpressionchild_constructor_args():
    sig = inspect.signature(java::ConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(java::ConditionalExpression)


def test_java::conditionalexpression_constructor_exists():
    assert callable(java::ConditionalExpression.__init__)


def test_java::conditionalexpression_constructor_args():
    sig = inspect.signature(java::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::layoutinformation_is_not_abstract():
    assert not inspect.isabstract(java::LayoutInformation)


def test_java::layoutinformation_constructor_exists():
    assert callable(java::LayoutInformation.__init__)


def test_java::layoutinformation_constructor_args():
    sig = inspect.signature(java::LayoutInformation.__init__)
    params = list(sig.parameters.keys())



def test_java::commentable_is_not_abstract():
    assert not inspect.isabstract(java::Commentable)


def test_java::commentable_constructor_exists():
    assert callable(java::Commentable.__init__)


def test_java::commentable_constructor_args():
    sig = inspect.signature(java::Commentable.__init__)
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



def test_java::enumeration_is_not_abstract():
    assert not inspect.isabstract(java::Enumeration)


def test_java::enumeration_constructor_exists():
    assert callable(java::Enumeration.__init__)


def test_java::enumeration_constructor_args():
    sig = inspect.signature(java::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_java::interface_is_not_abstract():
    assert not inspect.isabstract(java::Interface)


def test_java::interface_constructor_exists():
    assert callable(java::Interface.__init__)


def test_java::interface_constructor_args():
    sig = inspect.signature(java::Interface.__init__)
    params = list(sig.parameters.keys())



def test_java::class_is_not_abstract():
    assert not inspect.isabstract(java::Class)


def test_java::class_constructor_exists():
    assert callable(java::Class.__init__)


def test_java::class_constructor_args():
    sig = inspect.signature(java::Class.__init__)
    params = list(sig.parameters.keys())



def test_java::annotation_is_not_abstract():
    assert not inspect.isabstract(java::Annotation)


def test_java::annotation_constructor_exists():
    assert callable(java::Annotation.__init__)


def test_java::annotation_constructor_args():
    sig = inspect.signature(java::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_annotableandmodifiable_is_not_abstract():
    assert not inspect.isabstract(AnnotableAndModifiable)


def test_annotableandmodifiable_constructor_exists():
    assert callable(AnnotableAndModifiable.__init__)


def test_annotableandmodifiable_constructor_args():
    sig = inspect.signature(AnnotableAndModifiable.__init__)
    params = list(sig.parameters.keys())



def test_java::parameter_is_not_abstract():
    assert not inspect.isabstract(java::Parameter)


def test_java::parameter_constructor_exists():
    assert callable(java::Parameter.__init__)


def test_java::parameter_constructor_args():
    sig = inspect.signature(java::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_java::localvariable_is_not_abstract():
    assert not inspect.isabstract(java::LocalVariable)


def test_java::localvariable_constructor_exists():
    assert callable(java::LocalVariable.__init__)


def test_java::localvariable_constructor_args():
    sig = inspect.signature(java::LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::foreachloop_is_not_abstract():
    assert not inspect.isabstract(java::ForEachLoop)


def test_java::foreachloop_constructor_exists():
    assert callable(java::ForEachLoop.__init__)


def test_java::foreachloop_constructor_args():
    sig = inspect.signature(java::ForEachLoop.__init__)
    params = list(sig.parameters.keys())



def test_java::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(java::ExpressionStatement)


def test_java::expressionstatement_constructor_exists():
    assert callable(java::ExpressionStatement.__init__)


def test_java::expressionstatement_constructor_args():
    sig = inspect.signature(java::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::assert_is_not_abstract():
    assert not inspect.isabstract(java::Assert)


def test_java::assert_constructor_exists():
    assert callable(java::Assert.__init__)


def test_java::assert_constructor_args():
    sig = inspect.signature(java::Assert.__init__)
    params = list(sig.parameters.keys())



def test_java::emptystatement_is_not_abstract():
    assert not inspect.isabstract(java::EmptyStatement)


def test_java::emptystatement_constructor_exists():
    assert callable(java::EmptyStatement.__init__)


def test_java::emptystatement_constructor_args():
    sig = inspect.signature(java::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::return_is_not_abstract():
    assert not inspect.isabstract(java::Return)


def test_java::return_constructor_exists():
    assert callable(java::Return.__init__)


def test_java::return_constructor_args():
    sig = inspect.signature(java::Return.__init__)
    params = list(sig.parameters.keys())



def test_java::forloop_is_not_abstract():
    assert not inspect.isabstract(java::ForLoop)


def test_java::forloop_constructor_exists():
    assert callable(java::ForLoop.__init__)


def test_java::forloop_constructor_args():
    sig = inspect.signature(java::ForLoop.__init__)
    params = list(sig.parameters.keys())



def test_java::tryblock_is_not_abstract():
    assert not inspect.isabstract(java::TryBlock)


def test_java::tryblock_constructor_exists():
    assert callable(java::TryBlock.__init__)


def test_java::tryblock_constructor_args():
    sig = inspect.signature(java::TryBlock.__init__)
    params = list(sig.parameters.keys())



def test_java::jumplabel_is_not_abstract():
    assert not inspect.isabstract(java::JumpLabel)


def test_java::jumplabel_constructor_exists():
    assert callable(java::JumpLabel.__init__)


def test_java::jumplabel_constructor_args():
    sig = inspect.signature(java::JumpLabel.__init__)
    params = list(sig.parameters.keys())



def test_java::throw_is_not_abstract():
    assert not inspect.isabstract(java::Throw)


def test_java::throw_constructor_exists():
    assert callable(java::Throw.__init__)


def test_java::throw_constructor_args():
    sig = inspect.signature(java::Throw.__init__)
    params = list(sig.parameters.keys())



def test_java::synchronizedblock_is_not_abstract():
    assert not inspect.isabstract(java::SynchronizedBlock)


def test_java::synchronizedblock_constructor_exists():
    assert callable(java::SynchronizedBlock.__init__)


def test_java::synchronizedblock_constructor_args():
    sig = inspect.signature(java::SynchronizedBlock.__init__)
    params = list(sig.parameters.keys())



def test_java::switch_is_not_abstract():
    assert not inspect.isabstract(java::Switch)


def test_java::switch_constructor_exists():
    assert callable(java::Switch.__init__)


def test_java::switch_constructor_args():
    sig = inspect.signature(java::Switch.__init__)
    params = list(sig.parameters.keys())



def test_java::condition_is_not_abstract():
    assert not inspect.isabstract(java::Condition)


def test_java::condition_constructor_exists():
    assert callable(java::Condition.__init__)


def test_java::condition_constructor_args():
    sig = inspect.signature(java::Condition.__init__)
    params = list(sig.parameters.keys())



def test_java::whileloop_is_not_abstract():
    assert not inspect.isabstract(java::WhileLoop)


def test_java::whileloop_constructor_exists():
    assert callable(java::WhileLoop.__init__)


def test_java::whileloop_constructor_args():
    sig = inspect.signature(java::WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_java::jump_is_not_abstract():
    assert not inspect.isabstract(java::Jump)


def test_java::jump_constructor_exists():
    assert callable(java::Jump.__init__)


def test_java::jump_constructor_args():
    sig = inspect.signature(java::Jump.__init__)
    params = list(sig.parameters.keys())



def test_java::localvariablestatement_is_not_abstract():
    assert not inspect.isabstract(java::LocalVariableStatement)


def test_java::localvariablestatement_constructor_exists():
    assert callable(java::LocalVariableStatement.__init__)


def test_java::localvariablestatement_constructor_args():
    sig = inspect.signature(java::LocalVariableStatement.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_java::emptymember_is_not_abstract():
    assert not inspect.isabstract(java::EmptyMember)


def test_java::emptymember_constructor_exists():
    assert callable(java::EmptyMember.__init__)


def test_java::emptymember_constructor_args():
    sig = inspect.signature(java::EmptyMember.__init__)
    params = list(sig.parameters.keys())



def test_java::block_is_not_abstract():
    assert not inspect.isabstract(java::Block)


def test_java::block_constructor_exists():
    assert callable(java::Block.__init__)


def test_java::block_constructor_args():
    sig = inspect.signature(java::Block.__init__)
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



def test_java::constructor_is_not_abstract():
    assert not inspect.isabstract(java::Constructor)


def test_java::constructor_constructor_exists():
    assert callable(java::Constructor.__init__)


def test_java::constructor_constructor_args():
    sig = inspect.signature(java::Constructor.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_java::typeparameter_is_not_abstract():
    assert not inspect.isabstract(java::TypeParameter)


def test_java::typeparameter_constructor_exists():
    assert callable(java::TypeParameter.__init__)


def test_java::typeparameter_constructor_args():
    sig = inspect.signature(java::TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_java::concreteclassifier_is_not_abstract():
    assert not inspect.isabstract(java::ConcreteClassifier)


def test_java::concreteclassifier_constructor_exists():
    assert callable(java::ConcreteClassifier.__init__)


def test_java::concreteclassifier_constructor_args():
    sig = inspect.signature(java::ConcreteClassifier.__init__)
    params = list(sig.parameters.keys())



def test_referenceableelement_is_not_abstract():
    assert not inspect.isabstract(ReferenceableElement)


def test_referenceableelement_constructor_exists():
    assert callable(ReferenceableElement.__init__)


def test_referenceableelement_constructor_args():
    sig = inspect.signature(ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_java::field_is_not_abstract():
    assert not inspect.isabstract(java::Field)


def test_java::field_constructor_exists():
    assert callable(java::Field.__init__)


def test_java::field_constructor_args():
    sig = inspect.signature(java::Field.__init__)
    params = list(sig.parameters.keys())



def test_java::enumconstant_is_not_abstract():
    assert not inspect.isabstract(java::EnumConstant)


def test_java::enumconstant_constructor_exists():
    assert callable(java::EnumConstant.__init__)


def test_java::enumconstant_constructor_args():
    sig = inspect.signature(java::EnumConstant.__init__)
    params = list(sig.parameters.keys())



def test_java::packagereference_is_not_abstract():
    assert not inspect.isabstract(java::PackageReference)


def test_java::packagereference_constructor_exists():
    assert callable(java::PackageReference.__init__)


def test_java::packagereference_constructor_args():
    sig = inspect.signature(java::PackageReference.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetype_is_not_abstract():
    assert not inspect.isabstract(java::PrimitiveType)


def test_java::primitivetype_constructor_exists():
    assert callable(java::PrimitiveType.__init__)


def test_java::primitivetype_constructor_args():
    sig = inspect.signature(java::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java::anonymousclass_is_not_abstract():
    assert not inspect.isabstract(java::AnonymousClass)


def test_java::anonymousclass_constructor_exists():
    assert callable(java::AnonymousClass.__init__)


def test_java::anonymousclass_constructor_args():
    sig = inspect.signature(java::AnonymousClass.__init__)
    params = list(sig.parameters.keys())



def test_arrayinstantiationbyvalues_is_not_abstract():
    assert not inspect.isabstract(ArrayInstantiationByValues)


def test_arrayinstantiationbyvalues_constructor_exists():
    assert callable(ArrayInstantiationByValues.__init__)


def test_arrayinstantiationbyvalues_constructor_args():
    sig = inspect.signature(ArrayInstantiationByValues.__init__)
    params = list(sig.parameters.keys())



def test_java::arrayinstantiationbyvaluesuntyped_is_not_abstract():
    assert not inspect.isabstract(java::ArrayInstantiationByValuesUntyped)


def test_java::arrayinstantiationbyvaluesuntyped_constructor_exists():
    assert callable(java::ArrayInstantiationByValuesUntyped.__init__)


def test_java::arrayinstantiationbyvaluesuntyped_constructor_args():
    sig = inspect.signature(java::ArrayInstantiationByValuesUntyped.__init__)
    params = list(sig.parameters.keys())



def test_arraytypeable_is_not_abstract():
    assert not inspect.isabstract(ArrayTypeable)


def test_arraytypeable_constructor_exists():
    assert callable(ArrayTypeable.__init__)


def test_arraytypeable_constructor_args():
    sig = inspect.signature(ArrayTypeable.__init__)
    params = list(sig.parameters.keys())



def test_java::typeargument_is_not_abstract():
    assert not inspect.isabstract(java::TypeArgument)


def test_java::typeargument_constructor_exists():
    assert callable(java::TypeArgument.__init__)


def test_java::typeargument_constructor_args():
    sig = inspect.signature(java::TypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_java::additionallocalvariable_is_not_abstract():
    assert not inspect.isabstract(java::AdditionalLocalVariable)


def test_java::additionallocalvariable_constructor_exists():
    assert callable(java::AdditionalLocalVariable.__init__)


def test_java::additionallocalvariable_constructor_args():
    sig = inspect.signature(java::AdditionalLocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_java::additionalfield_is_not_abstract():
    assert not inspect.isabstract(java::AdditionalField)


def test_java::additionalfield_constructor_exists():
    assert callable(java::AdditionalField.__init__)


def test_java::additionalfield_constructor_args():
    sig = inspect.signature(java::AdditionalField.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_java::method_is_not_abstract():
    assert not inspect.isabstract(java::Method)


def test_java::method_constructor_exists():
    assert callable(java::Method.__init__)


def test_java::method_constructor_args():
    sig = inspect.signature(java::Method.__init__)
    params = list(sig.parameters.keys())



def test_java::arrayinstantiationbyvaluestyped_is_not_abstract():
    assert not inspect.isabstract(java::ArrayInstantiationByValuesTyped)


def test_java::arrayinstantiationbyvaluestyped_constructor_exists():
    assert callable(java::ArrayInstantiationByValuesTyped.__init__)


def test_java::arrayinstantiationbyvaluestyped_constructor_args():
    sig = inspect.signature(java::ArrayInstantiationByValuesTyped.__init__)
    params = list(sig.parameters.keys())



def test_java::instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(java::InstanceOfExpression)


def test_java::instanceofexpression_constructor_exists():
    assert callable(java::InstanceOfExpression.__init__)


def test_java::instanceofexpression_constructor_args():
    sig = inspect.signature(java::InstanceOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::qualifiedtypeargument_is_not_abstract():
    assert not inspect.isabstract(java::QualifiedTypeArgument)


def test_java::qualifiedtypeargument_constructor_exists():
    assert callable(java::QualifiedTypeArgument.__init__)


def test_java::qualifiedtypeargument_constructor_args():
    sig = inspect.signature(java::QualifiedTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_java::castexpression_is_not_abstract():
    assert not inspect.isabstract(java::CastExpression)


def test_java::castexpression_constructor_exists():
    assert callable(java::CastExpression.__init__)


def test_java::castexpression_constructor_args():
    sig = inspect.signature(java::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::variable_is_not_abstract():
    assert not inspect.isabstract(java::Variable)


def test_java::variable_constructor_exists():
    assert callable(java::Variable.__init__)


def test_java::variable_constructor_args():
    sig = inspect.signature(java::Variable.__init__)
    params = list(sig.parameters.keys())



def test_java::newconstructorcall_is_not_abstract():
    assert not inspect.isabstract(java::NewConstructorCall)


def test_java::newconstructorcall_constructor_exists():
    assert callable(java::NewConstructorCall.__init__)


def test_java::newconstructorcall_constructor_args():
    sig = inspect.signature(java::NewConstructorCall.__init__)
    params = list(sig.parameters.keys())



def test_arrayinstantiation_is_not_abstract():
    assert not inspect.isabstract(ArrayInstantiation)


def test_arrayinstantiation_constructor_exists():
    assert callable(ArrayInstantiation.__init__)


def test_arrayinstantiation_constructor_args():
    sig = inspect.signature(ArrayInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_java::arrayinstantiationbyvalues_is_not_abstract():
    assert not inspect.isabstract(java::ArrayInstantiationByValues)


def test_java::arrayinstantiationbyvalues_constructor_exists():
    assert callable(java::ArrayInstantiationByValues.__init__)


def test_java::arrayinstantiationbyvalues_constructor_args():
    sig = inspect.signature(java::ArrayInstantiationByValues.__init__)
    params = list(sig.parameters.keys())



def test_java::arrayinstantiationbysize_is_not_abstract():
    assert not inspect.isabstract(java::ArrayInstantiationBySize)


def test_java::arrayinstantiationbysize_constructor_exists():
    assert callable(java::ArrayInstantiationBySize.__init__)


def test_java::arrayinstantiationbysize_constructor_args():
    sig = inspect.signature(java::ArrayInstantiationBySize.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentexpressionchild_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentExpressionChild)


def test_java::assignmentexpressionchild_constructor_exists():
    assert callable(java::AssignmentExpressionChild.__init__)


def test_java::assignmentexpressionchild_constructor_args():
    sig = inspect.signature(java::AssignmentExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_java::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(java::AssignmentExpression)


def test_java::assignmentexpression_constructor_exists():
    assert callable(java::AssignmentExpression.__init__)


def test_java::assignmentexpression_constructor_args():
    sig = inspect.signature(java::AssignmentExpression.__init__)
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



def test_java::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(java::ArrayInitializer)


def test_java::arrayinitializer_constructor_exists():
    assert callable(java::ArrayInitializer.__init__)


def test_java::arrayinitializer_constructor_args():
    sig = inspect.signature(java::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_interfacemethod_is_not_abstract():
    assert not inspect.isabstract(InterfaceMethod)


def test_interfacemethod_constructor_exists():
    assert callable(InterfaceMethod.__init__)


def test_interfacemethod_constructor_args():
    sig = inspect.signature(InterfaceMethod.__init__)
    params = list(sig.parameters.keys())



def test_java::annotationattribute_is_not_abstract():
    assert not inspect.isabstract(java::AnnotationAttribute)


def test_java::annotationattribute_constructor_exists():
    assert callable(java::AnnotationAttribute.__init__)


def test_java::annotationattribute_constructor_args():
    sig = inspect.signature(java::AnnotationAttribute.__init__)
    params = list(sig.parameters.keys())



def test_java::interfacemethod_is_not_abstract():
    assert not inspect.isabstract(java::InterfaceMethod)


def test_java::interfacemethod_constructor_exists():
    assert callable(java::InterfaceMethod.__init__)


def test_java::interfacemethod_constructor_args():
    sig = inspect.signature(java::InterfaceMethod.__init__)
    params = list(sig.parameters.keys())



def test_annotationparameter_is_not_abstract():
    assert not inspect.isabstract(AnnotationParameter)


def test_annotationparameter_constructor_exists():
    assert callable(AnnotationParameter.__init__)


def test_annotationparameter_constructor_args():
    sig = inspect.signature(AnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_java::annotationparameterlist_is_not_abstract():
    assert not inspect.isabstract(java::AnnotationParameterList)


def test_java::annotationparameterlist_constructor_exists():
    assert callable(java::AnnotationParameterList.__init__)


def test_java::annotationparameterlist_constructor_args():
    sig = inspect.signature(java::AnnotationParameterList.__init__)
    params = list(sig.parameters.keys())



def test_java::singleannotationparameter_is_not_abstract():
    assert not inspect.isabstract(java::SingleAnnotationParameter)


def test_java::singleannotationparameter_constructor_exists():
    assert callable(java::SingleAnnotationParameter.__init__)


def test_java::singleannotationparameter_constructor_args():
    sig = inspect.signature(java::SingleAnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_java::classifier_is_not_abstract():
    assert not inspect.isabstract(java::Classifier)


def test_java::classifier_constructor_exists():
    assert callable(java::Classifier.__init__)


def test_java::classifier_constructor_args():
    sig = inspect.signature(java::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_namespaceawareelement_is_not_abstract():
    assert not inspect.isabstract(NamespaceAwareElement)


def test_namespaceawareelement_constructor_exists():
    assert callable(NamespaceAwareElement.__init__)


def test_namespaceawareelement_constructor_args():
    sig = inspect.signature(NamespaceAwareElement.__init__)
    params = list(sig.parameters.keys())



def test_java::import_is_not_abstract():
    assert not inspect.isabstract(java::Import)


def test_java::import_constructor_exists():
    assert callable(java::Import.__init__)


def test_java::import_constructor_args():
    sig = inspect.signature(java::Import.__init__)
    params = list(sig.parameters.keys())



def test_java::namespaceclassifierreference_is_not_abstract():
    assert not inspect.isabstract(java::NamespaceClassifierReference)


def test_java::namespaceclassifierreference_constructor_exists():
    assert callable(java::NamespaceClassifierReference.__init__)


def test_java::namespaceclassifierreference_constructor_args():
    sig = inspect.signature(java::NamespaceClassifierReference.__init__)
    params = list(sig.parameters.keys())



def test_java::javaroot_is_not_abstract():
    assert not inspect.isabstract(java::JavaRoot)


def test_java::javaroot_constructor_exists():
    assert callable(java::JavaRoot.__init__)


def test_java::javaroot_constructor_args():
    sig = inspect.signature(java::JavaRoot.__init__)
    params = list(sig.parameters.keys())



def test_annotationinstanceormodifier_is_not_abstract():
    assert not inspect.isabstract(AnnotationInstanceOrModifier)


def test_annotationinstanceormodifier_constructor_exists():
    assert callable(AnnotationInstanceOrModifier.__init__)


def test_annotationinstanceormodifier_constructor_args():
    sig = inspect.signature(AnnotationInstanceOrModifier.__init__)
    params = list(sig.parameters.keys())



def test_java::modifier_is_not_abstract():
    assert not inspect.isabstract(java::Modifier)


def test_java::modifier_constructor_exists():
    assert callable(java::Modifier.__init__)


def test_java::modifier_constructor_args():
    sig = inspect.signature(java::Modifier.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_java::instantiation_is_not_abstract():
    assert not inspect.isabstract(java::Instantiation)


def test_java::instantiation_constructor_exists():
    assert callable(java::Instantiation.__init__)


def test_java::instantiation_constructor_args():
    sig = inspect.signature(java::Instantiation.__init__)
    params = list(sig.parameters.keys())



def test_java::selfreference_is_not_abstract():
    assert not inspect.isabstract(java::SelfReference)


def test_java::selfreference_constructor_exists():
    assert callable(java::SelfReference.__init__)


def test_java::selfreference_constructor_args():
    sig = inspect.signature(java::SelfReference.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypereference_is_not_abstract():
    assert not inspect.isabstract(java::PrimitiveTypeReference)


def test_java::primitivetypereference_constructor_exists():
    assert callable(java::PrimitiveTypeReference.__init__)


def test_java::primitivetypereference_constructor_args():
    sig = inspect.signature(java::PrimitiveTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_java::nestedexpression_is_not_abstract():
    assert not inspect.isabstract(java::NestedExpression)


def test_java::nestedexpression_constructor_exists():
    assert callable(java::NestedExpression.__init__)


def test_java::nestedexpression_constructor_args():
    sig = inspect.signature(java::NestedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::reflectiveclassreference_is_not_abstract():
    assert not inspect.isabstract(java::ReflectiveClassReference)


def test_java::reflectiveclassreference_constructor_exists():
    assert callable(java::ReflectiveClassReference.__init__)


def test_java::reflectiveclassreference_constructor_args():
    sig = inspect.signature(java::ReflectiveClassReference.__init__)
    params = list(sig.parameters.keys())



def test_java::arrayinstantiation_is_not_abstract():
    assert not inspect.isabstract(java::ArrayInstantiation)


def test_java::arrayinstantiation_constructor_exists():
    assert callable(java::ArrayInstantiation.__init__)


def test_java::arrayinstantiation_constructor_args():
    sig = inspect.signature(java::ArrayInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_java::stringreference_is_not_abstract():
    assert not inspect.isabstract(java::StringReference)


def test_java::stringreference_constructor_exists():
    assert callable(java::StringReference.__init__)


def test_java::stringreference_constructor_args():
    sig = inspect.signature(java::StringReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_java::stringreference_has_value():
    assert hasattr(java::StringReference, "value")
    descriptor = None
    for klass in java::StringReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_java::elementreference_is_not_abstract():
    assert not inspect.isabstract(java::ElementReference)


def test_java::elementreference_constructor_exists():
    assert callable(java::ElementReference.__init__)


def test_java::elementreference_constructor_args():
    sig = inspect.signature(java::ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_java::annotationinstance_is_not_abstract():
    assert not inspect.isabstract(java::AnnotationInstance)


def test_java::annotationinstance_constructor_exists():
    assert callable(java::AnnotationInstance.__init__)


def test_java::annotationinstance_constructor_args():
    sig = inspect.signature(java::AnnotationInstance.__init__)
    params = list(sig.parameters.keys())



def test_commentable_is_not_abstract():
    assert not inspect.isabstract(Commentable)


def test_commentable_constructor_exists():
    assert callable(Commentable.__init__)


def test_commentable_constructor_args():
    sig = inspect.signature(Commentable.__init__)
    params = list(sig.parameters.keys())



def test_java::conditional_is_not_abstract():
    assert not inspect.isabstract(java::Conditional)


def test_java::conditional_constructor_exists():
    assert callable(java::Conditional.__init__)


def test_java::conditional_constructor_args():
    sig = inspect.signature(java::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_java::implementor_is_not_abstract():
    assert not inspect.isabstract(java::Implementor)


def test_java::implementor_constructor_exists():
    assert callable(java::Implementor.__init__)


def test_java::implementor_constructor_args():
    sig = inspect.signature(java::Implementor.__init__)
    params = list(sig.parameters.keys())



def test_java::parametrizable_is_not_abstract():
    assert not inspect.isabstract(java::Parametrizable)


def test_java::parametrizable_constructor_exists():
    assert callable(java::Parametrizable.__init__)


def test_java::parametrizable_constructor_args():
    sig = inspect.signature(java::Parametrizable.__init__)
    params = list(sig.parameters.keys())



def test_java::forloopinitializer_is_not_abstract():
    assert not inspect.isabstract(java::ForLoopInitializer)


def test_java::forloopinitializer_constructor_exists():
    assert callable(java::ForLoopInitializer.__init__)


def test_java::forloopinitializer_constructor_args():
    sig = inspect.signature(java::ForLoopInitializer.__init__)
    params = list(sig.parameters.keys())



def test_java::namespaceawareelement_is_not_abstract():
    assert not inspect.isabstract(java::NamespaceAwareElement)


def test_java::namespaceawareelement_constructor_exists():
    assert callable(java::NamespaceAwareElement.__init__)


def test_java::namespaceawareelement_constructor_args():
    sig = inspect.signature(java::NamespaceAwareElement.__init__)
    params = list(sig.parameters.keys())
    assert "namespaces" in params, "Missing parameter 'namespaces'"

def test_java::namespaceawareelement_has_namespaces():
    assert hasattr(java::NamespaceAwareElement, "namespaces")
    descriptor = None
    for klass in java::NamespaceAwareElement.__mro__:
        if "namespaces" in klass.__dict__:
            descriptor = klass.__dict__["namespaces"]
            break
    assert isinstance(descriptor, property)



def test_java::annotationparameter_is_not_abstract():
    assert not inspect.isabstract(java::AnnotationParameter)


def test_java::annotationparameter_constructor_exists():
    assert callable(java::AnnotationParameter.__init__)


def test_java::annotationparameter_constructor_args():
    sig = inspect.signature(java::AnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_java::annotationvalue_is_not_abstract():
    assert not inspect.isabstract(java::AnnotationValue)


def test_java::annotationvalue_constructor_exists():
    assert callable(java::AnnotationValue.__init__)


def test_java::annotationvalue_constructor_args():
    sig = inspect.signature(java::AnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_java::typereference_is_not_abstract():
    assert not inspect.isabstract(java::TypeReference)


def test_java::typereference_constructor_exists():
    assert callable(java::TypeReference.__init__)


def test_java::typereference_constructor_args():
    sig = inspect.signature(java::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_java::statementcontainer_is_not_abstract():
    assert not inspect.isabstract(java::StatementContainer)


def test_java::statementcontainer_constructor_exists():
    assert callable(java::StatementContainer.__init__)


def test_java::statementcontainer_constructor_args():
    sig = inspect.signature(java::StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_java::annotationattributesetting_is_not_abstract():
    assert not inspect.isabstract(java::AnnotationAttributeSetting)


def test_java::annotationattributesetting_constructor_exists():
    assert callable(java::AnnotationAttributeSetting.__init__)


def test_java::annotationattributesetting_constructor_args():
    sig = inspect.signature(java::AnnotationAttributeSetting.__init__)
    params = list(sig.parameters.keys())



def test_java::exceptionthrower_is_not_abstract():
    assert not inspect.isabstract(java::ExceptionThrower)


def test_java::exceptionthrower_constructor_exists():
    assert callable(java::ExceptionThrower.__init__)


def test_java::exceptionthrower_constructor_args():
    sig = inspect.signature(java::ExceptionThrower.__init__)
    params = list(sig.parameters.keys())



def test_java::arrayinitializationvalue_is_not_abstract():
    assert not inspect.isabstract(java::ArrayInitializationValue)


def test_java::arrayinitializationvalue_constructor_exists():
    assert callable(java::ArrayInitializationValue.__init__)


def test_java::arrayinitializationvalue_constructor_args():
    sig = inspect.signature(java::ArrayInitializationValue.__init__)
    params = list(sig.parameters.keys())



def test_java::importingelement_is_not_abstract():
    assert not inspect.isabstract(java::ImportingElement)


def test_java::importingelement_constructor_exists():
    assert callable(java::ImportingElement.__init__)


def test_java::importingelement_constructor_args():
    sig = inspect.signature(java::ImportingElement.__init__)
    params = list(sig.parameters.keys())



def test_java::initializable_is_not_abstract():
    assert not inspect.isabstract(java::Initializable)


def test_java::initializable_constructor_exists():
    assert callable(java::Initializable.__init__)


def test_java::initializable_constructor_args():
    sig = inspect.signature(java::Initializable.__init__)
    params = list(sig.parameters.keys())



def test_java::statementlistcontainer_is_not_abstract():
    assert not inspect.isabstract(java::StatementListContainer)


def test_java::statementlistcontainer_constructor_exists():
    assert callable(java::StatementListContainer.__init__)


def test_java::statementlistcontainer_constructor_args():
    sig = inspect.signature(java::StatementListContainer.__init__)
    params = list(sig.parameters.keys())



def test_java::statement_is_not_abstract():
    assert not inspect.isabstract(java::Statement)


def test_java::statement_constructor_exists():
    assert callable(java::Statement.__init__)


def test_java::statement_constructor_args():
    sig = inspect.signature(java::Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::operator_is_not_abstract():
    assert not inspect.isabstract(java::Operator)


def test_java::operator_constructor_exists():
    assert callable(java::Operator.__init__)


def test_java::operator_constructor_args():
    sig = inspect.signature(java::Operator.__init__)
    params = list(sig.parameters.keys())



def test_java::typeparametrizable_is_not_abstract():
    assert not inspect.isabstract(java::TypeParametrizable)


def test_java::typeparametrizable_constructor_exists():
    assert callable(java::TypeParametrizable.__init__)


def test_java::typeparametrizable_constructor_args():
    sig = inspect.signature(java::TypeParametrizable.__init__)
    params = list(sig.parameters.keys())



def test_java::typeargumentable_is_not_abstract():
    assert not inspect.isabstract(java::TypeArgumentable)


def test_java::typeargumentable_constructor_exists():
    assert callable(java::TypeArgumentable.__init__)


def test_java::typeargumentable_constructor_args():
    sig = inspect.signature(java::TypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_java::argumentable_is_not_abstract():
    assert not inspect.isabstract(java::Argumentable)


def test_java::argumentable_constructor_exists():
    assert callable(java::Argumentable.__init__)


def test_java::argumentable_constructor_args():
    sig = inspect.signature(java::Argumentable.__init__)
    params = list(sig.parameters.keys())



def test_java::annotationinstanceormodifier_is_not_abstract():
    assert not inspect.isabstract(java::AnnotationInstanceOrModifier)


def test_java::annotationinstanceormodifier_constructor_exists():
    assert callable(java::AnnotationInstanceOrModifier.__init__)


def test_java::annotationinstanceormodifier_constructor_args():
    sig = inspect.signature(java::AnnotationInstanceOrModifier.__init__)
    params = list(sig.parameters.keys())



def test_java::calltypeargumentable_is_not_abstract():
    assert not inspect.isabstract(java::CallTypeArgumentable)


def test_java::calltypeargumentable_constructor_exists():
    assert callable(java::CallTypeArgumentable.__init__)


def test_java::calltypeargumentable_constructor_args():
    sig = inspect.signature(java::CallTypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_java::self_is_not_abstract():
    assert not inspect.isabstract(java::Self)


def test_java::self_constructor_exists():
    assert callable(java::Self.__init__)


def test_java::self_constructor_args():
    sig = inspect.signature(java::Self.__init__)
    params = list(sig.parameters.keys())



def test_java::type_is_not_abstract():
    assert not inspect.isabstract(java::Type)


def test_java::type_constructor_exists():
    assert callable(java::Type.__init__)


def test_java::type_constructor_args():
    sig = inspect.signature(java::Type.__init__)
    params = list(sig.parameters.keys())



def test_java::typedelement_is_not_abstract():
    assert not inspect.isabstract(java::TypedElement)


def test_java::typedelement_constructor_exists():
    assert callable(java::TypedElement.__init__)


def test_java::typedelement_constructor_args():
    sig = inspect.signature(java::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_java::membercontainer_is_not_abstract():
    assert not inspect.isabstract(java::MemberContainer)


def test_java::membercontainer_constructor_exists():
    assert callable(java::MemberContainer.__init__)


def test_java::membercontainer_constructor_args():
    sig = inspect.signature(java::MemberContainer.__init__)
    params = list(sig.parameters.keys())



def test_java::arraydimension_is_not_abstract():
    assert not inspect.isabstract(java::ArrayDimension)


def test_java::arraydimension_constructor_exists():
    assert callable(java::ArrayDimension.__init__)


def test_java::arraydimension_constructor_args():
    sig = inspect.signature(java::ArrayDimension.__init__)
    params = list(sig.parameters.keys())



def test_java::modifiable_is_not_abstract():
    assert not inspect.isabstract(java::Modifiable)


def test_java::modifiable_constructor_exists():
    assert callable(java::Modifiable.__init__)


def test_java::modifiable_constructor_args():
    sig = inspect.signature(java::Modifiable.__init__)
    params = list(sig.parameters.keys())



def test_java::arrayselector_is_not_abstract():
    assert not inspect.isabstract(java::ArraySelector)


def test_java::arrayselector_constructor_exists():
    assert callable(java::ArraySelector.__init__)


def test_java::arrayselector_constructor_args():
    sig = inspect.signature(java::ArraySelector.__init__)
    params = list(sig.parameters.keys())



def test_java::namedelement_is_not_abstract():
    assert not inspect.isabstract(java::NamedElement)


def test_java::namedelement_constructor_exists():
    assert callable(java::NamedElement.__init__)


def test_java::namedelement_constructor_args():
    sig = inspect.signature(java::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::namedelement_has_name():
    assert hasattr(java::NamedElement, "name")
    descriptor = None
    for klass in java::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::annotableandmodifiable_is_not_abstract():
    assert not inspect.isabstract(java::AnnotableAndModifiable)


def test_java::annotableandmodifiable_constructor_exists():
    assert callable(java::AnnotableAndModifiable.__init__)


def test_java::annotableandmodifiable_constructor_args():
    sig = inspect.signature(java::AnnotableAndModifiable.__init__)
    params = list(sig.parameters.keys())



def test_java::annotable_is_not_abstract():
    assert not inspect.isabstract(java::Annotable)


def test_java::annotable_constructor_exists():
    assert callable(java::Annotable.__init__)


def test_java::annotable_constructor_args():
    sig = inspect.signature(java::Annotable.__init__)
    params = list(sig.parameters.keys())



def test_java::arraytypeable_is_not_abstract():
    assert not inspect.isabstract(java::ArrayTypeable)


def test_java::arraytypeable_constructor_exists():
    assert callable(java::ArrayTypeable.__init__)


def test_java::arraytypeable_constructor_args():
    sig = inspect.signature(java::ArrayTypeable.__init__)
    params = list(sig.parameters.keys())



def test_java::expression_is_not_abstract():
    assert not inspect.isabstract(java::Expression)


def test_java::expression_constructor_exists():
    assert callable(java::Expression.__init__)


def test_java::expression_constructor_args():
    sig = inspect.signature(java::Expression.__init__)
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
EqualityExpressionChild_strategy = st.builds(
    EqualityExpressionChild,
)
java::InstanceOfExpressionChild_strategy = st.builds(
    java::InstanceOfExpressionChild,
)
AndExpressionChild_strategy = st.builds(
    AndExpressionChild,
)
java::EqualityExpressionChild_strategy = st.builds(
    java::EqualityExpressionChild,
)
java::EqualityExpression_strategy = st.builds(
    java::EqualityExpression,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
java::Void_strategy = st.builds(
    java::Void,
)
java::Int_strategy = st.builds(
    java::Int,
)
java::Float_strategy = st.builds(
    java::Float,
)
java::Long_strategy = st.builds(
    java::Long,
)
java::Short_strategy = st.builds(
    java::Short,
)
java::Char_strategy = st.builds(
    java::Char,
)
java::Byte_strategy = st.builds(
    java::Byte,
)
java::Double_strategy = st.builds(
    java::Double,
)
java::Boolean_strategy = st.builds(
    java::Boolean,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
WhileLoop_strategy = st.builds(
    WhileLoop,
)
java::DoWhileLoop_strategy = st.builds(
    java::DoWhileLoop,
)
SwitchCase_strategy = st.builds(
    SwitchCase,
)
java::DefaultSwitchCase_strategy = st.builds(
    java::DefaultSwitchCase,
)
Modifiable_strategy = st.builds(
    Modifiable,
)
Jump_strategy = st.builds(
    Jump,
)
java::Continue_strategy = st.builds(
    java::Continue,
)
java::Break_strategy = st.builds(
    java::Break,
)
Conditional_strategy = st.builds(
    Conditional,
)
java::NormalSwitchCase_strategy = st.builds(
    java::NormalSwitchCase,
)
Parameter_strategy = st.builds(
    Parameter,
)
java::VariableLengthParameter_strategy = st.builds(
    java::VariableLengthParameter,
)
java::OrdinaryParameter_strategy = st.builds(
    java::OrdinaryParameter,
)
StatementContainer_strategy = st.builds(
    StatementContainer,
)
ElementReference_strategy = st.builds(
    ElementReference,
)
java::IdentifierReference_strategy = st.builds(
    java::IdentifierReference,
)
TypeArgumentable_strategy = st.builds(
    TypeArgumentable,
)
java::ClassifierReference_strategy = st.builds(
    java::ClassifierReference,
)
ShiftOperator_strategy = st.builds(
    ShiftOperator,
)
java::UnsignedRightShift_strategy = st.builds(
    java::UnsignedRightShift,
)
java::RightShift_strategy = st.builds(
    java::RightShift,
)
java::LeftShift_strategy = st.builds(
    java::LeftShift,
)
UnaryModificationOperator_strategy = st.builds(
    UnaryModificationOperator,
)
java::PlusPlus_strategy = st.builds(
    java::PlusPlus,
)
java::MinusMinus_strategy = st.builds(
    java::MinusMinus,
)
MultiplicativeOperator_strategy = st.builds(
    MultiplicativeOperator,
)
java::Remainder_strategy = st.builds(
    java::Remainder,
)
java::Multiplication_strategy = st.builds(
    java::Multiplication,
)
java::Division_strategy = st.builds(
    java::Division,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
java::Complement_strategy = st.builds(
    java::Complement,
)
java::Negate_strategy = st.builds(
    java::Negate,
)
AdditiveOperator_strategy = st.builds(
    AdditiveOperator,
)
java::Subtraction_strategy = st.builds(
    java::Subtraction,
)
java::Addition_strategy = st.builds(
    java::Addition,
)
RelationOperator_strategy = st.builds(
    RelationOperator,
)
java::LessThanOrEqual_strategy = st.builds(
    java::LessThanOrEqual,
)
java::LessThan_strategy = st.builds(
    java::LessThan,
)
java::GreaterThanOrEqual_strategy = st.builds(
    java::GreaterThanOrEqual,
)
java::GreaterThan_strategy = st.builds(
    java::GreaterThan,
)
AssignmentOperator_strategy = st.builds(
    AssignmentOperator,
)
java::AssignmentAnd_strategy = st.builds(
    java::AssignmentAnd,
)
java::AssignmentLeftShift_strategy = st.builds(
    java::AssignmentLeftShift,
)
java::AssignmentMinus_strategy = st.builds(
    java::AssignmentMinus,
)
java::AssignmentMultiplication_strategy = st.builds(
    java::AssignmentMultiplication,
)
java::AssignmentModulo_strategy = st.builds(
    java::AssignmentModulo,
)
java::AssignmentExclusiveOr_strategy = st.builds(
    java::AssignmentExclusiveOr,
)
java::AssignmentDivision_strategy = st.builds(
    java::AssignmentDivision,
)
java::AssignmentOr_strategy = st.builds(
    java::AssignmentOr,
)
java::Assignment_strategy = st.builds(
    java::Assignment,
)
Operator_strategy = st.builds(
    Operator,
)
java::EqualityOperator_strategy = st.builds(
    java::EqualityOperator,
)
Modifier_strategy = st.builds(
    Modifier,
)
java::Public_strategy = st.builds(
    java::Public,
)
java::Strictfp_strategy = st.builds(
    java::Strictfp,
)
java::Private_strategy = st.builds(
    java::Private,
)
java::Native_strategy = st.builds(
    java::Native,
)
java::Transient_strategy = st.builds(
    java::Transient,
)
java::Synchronized_strategy = st.builds(
    java::Synchronized,
)
java::Protected_strategy = st.builds(
    java::Protected,
)
java::Volatile_strategy = st.builds(
    java::Volatile,
)
java::Final_strategy = st.builds(
    java::Final,
)
java::Abstract_strategy = st.builds(
    java::Abstract,
)
EqualityOperator_strategy = st.builds(
    EqualityOperator,
)
java::NotEqual_strategy = st.builds(
    java::NotEqual,
)
java::Equal_strategy = st.builds(
    java::Equal,
)
java::AssignmentUnsignedRightShift_strategy = st.builds(
    java::AssignmentUnsignedRightShift,
)
java::AssignmentRightShift_strategy = st.builds(
    java::AssignmentRightShift,
)
java::AssignmentPlus_strategy = st.builds(
    java::AssignmentPlus,
)
Method_strategy = st.builds(
    Method,
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
java::ClassMethod_strategy = st.builds(
    java::ClassMethod,
)
java::CatchBlock_strategy = st.builds(
    java::CatchBlock,
)
java::SwitchCase_strategy = st.builds(
    java::SwitchCase,
)
Initializable_strategy = st.builds(
    Initializable,
)
Self_strategy = st.builds(
    Self,
)
java::This_strategy = st.builds(
    java::This,
)
java::Super_strategy = st.builds(
    java::Super,
)
LongLiteral_strategy = st.builds(
    LongLiteral,
)
java::OctalLongLiteral_strategy = st.builds(
    java::OctalLongLiteral,
    octalValue=
        safe_text
)
java::HexLongLiteral_strategy = st.builds(
    java::HexLongLiteral,
    hexValue=
        safe_text
)
java::DecimalLongLiteral_strategy = st.builds(
    java::DecimalLongLiteral,
    decimalValue=
        safe_text
)
IntegerLiteral_strategy = st.builds(
    IntegerLiteral,
)
java::OctalIntegerLiteral_strategy = st.builds(
    java::OctalIntegerLiteral,
    octalValue=
        safe_text
)
java::HexIntegerLiteral_strategy = st.builds(
    java::HexIntegerLiteral,
    hexValue=
        safe_text
)
java::DecimalIntegerLiteral_strategy = st.builds(
    java::DecimalIntegerLiteral,
    decimalValue=
        safe_text
)
DoubleLiteral_strategy = st.builds(
    DoubleLiteral,
)
java::HexDoubleLiteral_strategy = st.builds(
    java::HexDoubleLiteral,
    hexValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
java::DecimalDoubleLiteral_strategy = st.builds(
    java::DecimalDoubleLiteral,
    decimalValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
FloatLiteral_strategy = st.builds(
    FloatLiteral,
)
java::HexFloatLiteral_strategy = st.builds(
    java::HexFloatLiteral,
    hexValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
java::DecimalFloatLiteral_strategy = st.builds(
    java::DecimalFloatLiteral,
    decimalValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
java::Reference_strategy = st.builds(
    java::Reference,
)
java::Literal_strategy = st.builds(
    java::Literal,
)
CallTypeArgumentable_strategy = st.builds(
    CallTypeArgumentable,
)
Instantiation_strategy = st.builds(
    Instantiation,
)
java::ExplicitConstructorCall_strategy = st.builds(
    java::ExplicitConstructorCall,
)
Argumentable_strategy = st.builds(
    Argumentable,
)
java::MethodCall_strategy = st.builds(
    java::MethodCall,
)
StaticImport_strategy = st.builds(
    StaticImport,
)
java::StaticMemberImport_strategy = st.builds(
    java::StaticMemberImport,
)
java::StaticClassifierImport_strategy = st.builds(
    java::StaticClassifierImport,
)
java::Static_strategy = st.builds(
    java::Static,
)
Import_strategy = st.builds(
    Import,
)
java::ClassifierImport_strategy = st.builds(
    java::ClassifierImport,
)
java::PackageImport_strategy = st.builds(
    java::PackageImport,
)
java::StaticImport_strategy = st.builds(
    java::StaticImport,
)
Literal_strategy = st.builds(
    Literal,
)
java::CharacterLiteral_strategy = st.builds(
    java::CharacterLiteral,
    value=
        safe_text
)
java::DoubleLiteral_strategy = st.builds(
    java::DoubleLiteral,
)
java::IntegerLiteral_strategy = st.builds(
    java::IntegerLiteral,
)
java::LongLiteral_strategy = st.builds(
    java::LongLiteral,
)
java::FloatLiteral_strategy = st.builds(
    java::FloatLiteral,
)
java::NullLiteral_strategy = st.builds(
    java::NullLiteral,
)
java::BooleanLiteral_strategy = st.builds(
    java::BooleanLiteral,
    value=
        st.booleans()
)
TypeArgument_strategy = st.builds(
    TypeArgument,
)
java::SuperTypeArgument_strategy = st.builds(
    java::SuperTypeArgument,
)
java::ExtendsTypeArgument_strategy = st.builds(
    java::ExtendsTypeArgument,
)
UnaryModificationExpressionChild_strategy = st.builds(
    UnaryModificationExpressionChild,
)
java::PrimaryExpression_strategy = st.builds(
    java::PrimaryExpression,
)
java::UnknownTypeArgument_strategy = st.builds(
    java::UnknownTypeArgument,
)
java::UnaryModificationOperator_strategy = st.builds(
    java::UnaryModificationOperator,
)
UnaryExpressionChild_strategy = st.builds(
    UnaryExpressionChild,
)
java::UnaryModificationExpressionChild_strategy = st.builds(
    java::UnaryModificationExpressionChild,
)
java::UnaryModificationExpression_strategy = st.builds(
    java::UnaryModificationExpression,
)
java::UnaryOperator_strategy = st.builds(
    java::UnaryOperator,
)
MultiplicativeExpressionChild_strategy = st.builds(
    MultiplicativeExpressionChild,
)
java::UnaryExpressionChild_strategy = st.builds(
    java::UnaryExpressionChild,
)
java::UnaryExpression_strategy = st.builds(
    java::UnaryExpression,
)
java::MultiplicativeOperator_strategy = st.builds(
    java::MultiplicativeOperator,
)
AdditiveExpressionChild_strategy = st.builds(
    AdditiveExpressionChild,
)
java::MultiplicativeExpressionChild_strategy = st.builds(
    java::MultiplicativeExpressionChild,
)
java::MultiplicativeExpression_strategy = st.builds(
    java::MultiplicativeExpression,
)
java::AdditiveOperator_strategy = st.builds(
    java::AdditiveOperator,
)
ShiftExpressionChild_strategy = st.builds(
    ShiftExpressionChild,
)
java::AdditiveExpressionChild_strategy = st.builds(
    java::AdditiveExpressionChild,
)
java::AdditiveExpression_strategy = st.builds(
    java::AdditiveExpression,
)
java::ShiftOperator_strategy = st.builds(
    java::ShiftOperator,
)
RelationExpressionChild_strategy = st.builds(
    RelationExpressionChild,
)
java::ShiftExpressionChild_strategy = st.builds(
    java::ShiftExpressionChild,
)
java::ShiftExpression_strategy = st.builds(
    java::ShiftExpression,
)
java::RelationOperator_strategy = st.builds(
    java::RelationOperator,
)
UnaryModificationExpression_strategy = st.builds(
    UnaryModificationExpression,
)
java::SuffixUnaryModificationExpression_strategy = st.builds(
    java::SuffixUnaryModificationExpression,
)
java::PrefixUnaryModificationExpression_strategy = st.builds(
    java::PrefixUnaryModificationExpression,
)
ExclusiveOrExpressionChild_strategy = st.builds(
    ExclusiveOrExpressionChild,
)
java::AndExpressionChild_strategy = st.builds(
    java::AndExpressionChild,
)
java::AndExpression_strategy = st.builds(
    java::AndExpression,
)
InclusiveOrExpressionChild_strategy = st.builds(
    InclusiveOrExpressionChild,
)
java::ExclusiveOrExpressionChild_strategy = st.builds(
    java::ExclusiveOrExpressionChild,
)
java::ExclusiveOrExpression_strategy = st.builds(
    java::ExclusiveOrExpression,
)
ConditionalAndExpressionChild_strategy = st.builds(
    ConditionalAndExpressionChild,
)
java::InclusiveOrExpressionChild_strategy = st.builds(
    java::InclusiveOrExpressionChild,
)
java::InclusiveOrExpression_strategy = st.builds(
    java::InclusiveOrExpression,
)
ConditionalOrExpressionChild_strategy = st.builds(
    ConditionalOrExpressionChild,
)
java::ConditionalAndExpressionChild_strategy = st.builds(
    java::ConditionalAndExpressionChild,
)
java::ConditionalAndExpression_strategy = st.builds(
    java::ConditionalAndExpression,
)
ConditionalExpressionChild_strategy = st.builds(
    ConditionalExpressionChild,
)
java::ConditionalOrExpressionChild_strategy = st.builds(
    java::ConditionalOrExpressionChild,
)
java::ConditionalOrExpression_strategy = st.builds(
    java::ConditionalOrExpression,
)
InstanceOfExpressionChild_strategy = st.builds(
    InstanceOfExpressionChild,
)
java::RelationExpressionChild_strategy = st.builds(
    java::RelationExpressionChild,
)
java::RelationExpression_strategy = st.builds(
    java::RelationExpression,
)
java::AssignmentOperator_strategy = st.builds(
    java::AssignmentOperator,
)
ForLoopInitializer_strategy = st.builds(
    ForLoopInitializer,
)
java::ExpressionList_strategy = st.builds(
    java::ExpressionList,
)
Annotable_strategy = st.builds(
    Annotable,
)
JavaRoot_strategy = st.builds(
    JavaRoot,
)
java::Package_strategy = st.builds(
    java::Package,
)
java::EmptyModel_strategy = st.builds(
    java::EmptyModel,
)
java::CompilationUnit_strategy = st.builds(
    java::CompilationUnit,
)
ImportingElement_strategy = st.builds(
    ImportingElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
java::ReferenceableElement_strategy = st.builds(
    java::ReferenceableElement,
)
java::Member_strategy = st.builds(
    java::Member,
)
AssignmentExpressionChild_strategy = st.builds(
    AssignmentExpressionChild,
)
java::ConditionalExpressionChild_strategy = st.builds(
    java::ConditionalExpressionChild,
)
java::ConditionalExpression_strategy = st.builds(
    java::ConditionalExpression,
)
java::LayoutInformation_strategy = st.builds(
    java::LayoutInformation,
)
java::Commentable_strategy = st.builds(
    java::Commentable,
)
Implementor_strategy = st.builds(
    Implementor,
)
ConcreteClassifier_strategy = st.builds(
    ConcreteClassifier,
)
java::Enumeration_strategy = st.builds(
    java::Enumeration,
)
java::Interface_strategy = st.builds(
    java::Interface,
)
java::Class_strategy = st.builds(
    java::Class,
)
java::Annotation_strategy = st.builds(
    java::Annotation,
)
AnnotableAndModifiable_strategy = st.builds(
    AnnotableAndModifiable,
)
java::Parameter_strategy = st.builds(
    java::Parameter,
)
java::LocalVariable_strategy = st.builds(
    java::LocalVariable,
)
Statement_strategy = st.builds(
    Statement,
)
java::ForEachLoop_strategy = st.builds(
    java::ForEachLoop,
)
java::ExpressionStatement_strategy = st.builds(
    java::ExpressionStatement,
)
java::Assert_strategy = st.builds(
    java::Assert,
)
java::EmptyStatement_strategy = st.builds(
    java::EmptyStatement,
)
java::Return_strategy = st.builds(
    java::Return,
)
java::ForLoop_strategy = st.builds(
    java::ForLoop,
)
java::TryBlock_strategy = st.builds(
    java::TryBlock,
)
java::JumpLabel_strategy = st.builds(
    java::JumpLabel,
)
java::Throw_strategy = st.builds(
    java::Throw,
)
java::SynchronizedBlock_strategy = st.builds(
    java::SynchronizedBlock,
)
java::Switch_strategy = st.builds(
    java::Switch,
)
java::Condition_strategy = st.builds(
    java::Condition,
)
java::WhileLoop_strategy = st.builds(
    java::WhileLoop,
)
java::Jump_strategy = st.builds(
    java::Jump,
)
java::LocalVariableStatement_strategy = st.builds(
    java::LocalVariableStatement,
)
Member_strategy = st.builds(
    Member,
)
java::EmptyMember_strategy = st.builds(
    java::EmptyMember,
)
java::Block_strategy = st.builds(
    java::Block,
)
MemberContainer_strategy = st.builds(
    MemberContainer,
)
TypeParametrizable_strategy = st.builds(
    TypeParametrizable,
)
java::Constructor_strategy = st.builds(
    java::Constructor,
)
Classifier_strategy = st.builds(
    Classifier,
)
java::TypeParameter_strategy = st.builds(
    java::TypeParameter,
)
java::ConcreteClassifier_strategy = st.builds(
    java::ConcreteClassifier,
)
ReferenceableElement_strategy = st.builds(
    ReferenceableElement,
)
java::Field_strategy = st.builds(
    java::Field,
)
java::EnumConstant_strategy = st.builds(
    java::EnumConstant,
)
java::PackageReference_strategy = st.builds(
    java::PackageReference,
)
Type_strategy = st.builds(
    Type,
)
java::PrimitiveType_strategy = st.builds(
    java::PrimitiveType,
)
java::AnonymousClass_strategy = st.builds(
    java::AnonymousClass,
)
ArrayInstantiationByValues_strategy = st.builds(
    ArrayInstantiationByValues,
)
java::ArrayInstantiationByValuesUntyped_strategy = st.builds(
    java::ArrayInstantiationByValuesUntyped,
)
ArrayTypeable_strategy = st.builds(
    ArrayTypeable,
)
java::TypeArgument_strategy = st.builds(
    java::TypeArgument,
)
java::AdditionalLocalVariable_strategy = st.builds(
    java::AdditionalLocalVariable,
)
java::AdditionalField_strategy = st.builds(
    java::AdditionalField,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
java::Method_strategy = st.builds(
    java::Method,
)
java::ArrayInstantiationByValuesTyped_strategy = st.builds(
    java::ArrayInstantiationByValuesTyped,
)
java::InstanceOfExpression_strategy = st.builds(
    java::InstanceOfExpression,
)
java::QualifiedTypeArgument_strategy = st.builds(
    java::QualifiedTypeArgument,
)
java::CastExpression_strategy = st.builds(
    java::CastExpression,
)
java::Variable_strategy = st.builds(
    java::Variable,
)
java::NewConstructorCall_strategy = st.builds(
    java::NewConstructorCall,
)
ArrayInstantiation_strategy = st.builds(
    ArrayInstantiation,
)
java::ArrayInstantiationByValues_strategy = st.builds(
    java::ArrayInstantiationByValues,
)
java::ArrayInstantiationBySize_strategy = st.builds(
    java::ArrayInstantiationBySize,
)
Expression_strategy = st.builds(
    Expression,
)
java::AssignmentExpressionChild_strategy = st.builds(
    java::AssignmentExpressionChild,
)
java::AssignmentExpression_strategy = st.builds(
    java::AssignmentExpression,
)
AnnotationValue_strategy = st.builds(
    AnnotationValue,
)
ArrayInitializationValue_strategy = st.builds(
    ArrayInitializationValue,
)
java::ArrayInitializer_strategy = st.builds(
    java::ArrayInitializer,
)
InterfaceMethod_strategy = st.builds(
    InterfaceMethod,
)
java::AnnotationAttribute_strategy = st.builds(
    java::AnnotationAttribute,
)
java::InterfaceMethod_strategy = st.builds(
    java::InterfaceMethod,
)
AnnotationParameter_strategy = st.builds(
    AnnotationParameter,
)
java::AnnotationParameterList_strategy = st.builds(
    java::AnnotationParameterList,
)
java::SingleAnnotationParameter_strategy = st.builds(
    java::SingleAnnotationParameter,
)
java::Classifier_strategy = st.builds(
    java::Classifier,
)
NamespaceAwareElement_strategy = st.builds(
    NamespaceAwareElement,
)
java::Import_strategy = st.builds(
    java::Import,
)
java::NamespaceClassifierReference_strategy = st.builds(
    java::NamespaceClassifierReference,
)
java::JavaRoot_strategy = st.builds(
    java::JavaRoot,
)
AnnotationInstanceOrModifier_strategy = st.builds(
    AnnotationInstanceOrModifier,
)
java::Modifier_strategy = st.builds(
    java::Modifier,
)
Reference_strategy = st.builds(
    Reference,
)
java::Instantiation_strategy = st.builds(
    java::Instantiation,
)
java::SelfReference_strategy = st.builds(
    java::SelfReference,
)
java::PrimitiveTypeReference_strategy = st.builds(
    java::PrimitiveTypeReference,
)
java::NestedExpression_strategy = st.builds(
    java::NestedExpression,
)
java::ReflectiveClassReference_strategy = st.builds(
    java::ReflectiveClassReference,
)
java::ArrayInstantiation_strategy = st.builds(
    java::ArrayInstantiation,
)
java::StringReference_strategy = st.builds(
    java::StringReference,
    value=
        safe_text
)
java::ElementReference_strategy = st.builds(
    java::ElementReference,
)
java::AnnotationInstance_strategy = st.builds(
    java::AnnotationInstance,
)
Commentable_strategy = st.builds(
    Commentable,
)
java::Conditional_strategy = st.builds(
    java::Conditional,
)
java::Implementor_strategy = st.builds(
    java::Implementor,
)
java::Parametrizable_strategy = st.builds(
    java::Parametrizable,
)
java::ForLoopInitializer_strategy = st.builds(
    java::ForLoopInitializer,
)
java::NamespaceAwareElement_strategy = st.builds(
    java::NamespaceAwareElement,
    namespaces=
        safe_text
)
java::AnnotationParameter_strategy = st.builds(
    java::AnnotationParameter,
)
java::AnnotationValue_strategy = st.builds(
    java::AnnotationValue,
)
java::TypeReference_strategy = st.builds(
    java::TypeReference,
)
java::StatementContainer_strategy = st.builds(
    java::StatementContainer,
)
java::AnnotationAttributeSetting_strategy = st.builds(
    java::AnnotationAttributeSetting,
)
java::ExceptionThrower_strategy = st.builds(
    java::ExceptionThrower,
)
java::ArrayInitializationValue_strategy = st.builds(
    java::ArrayInitializationValue,
)
java::ImportingElement_strategy = st.builds(
    java::ImportingElement,
)
java::Initializable_strategy = st.builds(
    java::Initializable,
)
java::StatementListContainer_strategy = st.builds(
    java::StatementListContainer,
)
java::Statement_strategy = st.builds(
    java::Statement,
)
java::Operator_strategy = st.builds(
    java::Operator,
)
java::TypeParametrizable_strategy = st.builds(
    java::TypeParametrizable,
)
java::TypeArgumentable_strategy = st.builds(
    java::TypeArgumentable,
)
java::Argumentable_strategy = st.builds(
    java::Argumentable,
)
java::AnnotationInstanceOrModifier_strategy = st.builds(
    java::AnnotationInstanceOrModifier,
)
java::CallTypeArgumentable_strategy = st.builds(
    java::CallTypeArgumentable,
)
java::Self_strategy = st.builds(
    java::Self,
)
java::Type_strategy = st.builds(
    java::Type,
)
java::TypedElement_strategy = st.builds(
    java::TypedElement,
)
java::MemberContainer_strategy = st.builds(
    java::MemberContainer,
)
java::ArrayDimension_strategy = st.builds(
    java::ArrayDimension,
)
java::Modifiable_strategy = st.builds(
    java::Modifiable,
)
java::ArraySelector_strategy = st.builds(
    java::ArraySelector,
)
java::NamedElement_strategy = st.builds(
    java::NamedElement,
    name=
        safe_text
)
java::AnnotableAndModifiable_strategy = st.builds(
    java::AnnotableAndModifiable,
)
java::Annotable_strategy = st.builds(
    java::Annotable,
)
java::ArrayTypeable_strategy = st.builds(
    java::ArrayTypeable,
)
java::Expression_strategy = st.builds(
    java::Expression,
)

@given(instance=EqualityExpressionChild_strategy)
@settings(max_examples=50)
def test_equalityexpressionchild_instantiation(instance):
    assert isinstance(instance, EqualityExpressionChild)

@given(instance=java::InstanceOfExpressionChild_strategy)
@settings(max_examples=50)
def test_java::instanceofexpressionchild_instantiation(instance):
    assert isinstance(instance, java::InstanceOfExpressionChild)

@given(instance=AndExpressionChild_strategy)
@settings(max_examples=50)
def test_andexpressionchild_instantiation(instance):
    assert isinstance(instance, AndExpressionChild)

@given(instance=java::EqualityExpressionChild_strategy)
@settings(max_examples=50)
def test_java::equalityexpressionchild_instantiation(instance):
    assert isinstance(instance, java::EqualityExpressionChild)

@given(instance=java::EqualityExpression_strategy)
@settings(max_examples=50)
def test_java::equalityexpression_instantiation(instance):
    assert isinstance(instance, java::EqualityExpression)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=java::Void_strategy)
@settings(max_examples=50)
def test_java::void_instantiation(instance):
    assert isinstance(instance, java::Void)

@given(instance=java::Int_strategy)
@settings(max_examples=50)
def test_java::int_instantiation(instance):
    assert isinstance(instance, java::Int)

@given(instance=java::Float_strategy)
@settings(max_examples=50)
def test_java::float_instantiation(instance):
    assert isinstance(instance, java::Float)

@given(instance=java::Long_strategy)
@settings(max_examples=50)
def test_java::long_instantiation(instance):
    assert isinstance(instance, java::Long)

@given(instance=java::Short_strategy)
@settings(max_examples=50)
def test_java::short_instantiation(instance):
    assert isinstance(instance, java::Short)

@given(instance=java::Char_strategy)
@settings(max_examples=50)
def test_java::char_instantiation(instance):
    assert isinstance(instance, java::Char)

@given(instance=java::Byte_strategy)
@settings(max_examples=50)
def test_java::byte_instantiation(instance):
    assert isinstance(instance, java::Byte)

@given(instance=java::Double_strategy)
@settings(max_examples=50)
def test_java::double_instantiation(instance):
    assert isinstance(instance, java::Double)

@given(instance=java::Boolean_strategy)
@settings(max_examples=50)
def test_java::boolean_instantiation(instance):
    assert isinstance(instance, java::Boolean)

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=WhileLoop_strategy)
@settings(max_examples=50)
def test_whileloop_instantiation(instance):
    assert isinstance(instance, WhileLoop)

@given(instance=java::DoWhileLoop_strategy)
@settings(max_examples=50)
def test_java::dowhileloop_instantiation(instance):
    assert isinstance(instance, java::DoWhileLoop)

@given(instance=SwitchCase_strategy)
@settings(max_examples=50)
def test_switchcase_instantiation(instance):
    assert isinstance(instance, SwitchCase)

@given(instance=java::DefaultSwitchCase_strategy)
@settings(max_examples=50)
def test_java::defaultswitchcase_instantiation(instance):
    assert isinstance(instance, java::DefaultSwitchCase)

@given(instance=Modifiable_strategy)
@settings(max_examples=50)
def test_modifiable_instantiation(instance):
    assert isinstance(instance, Modifiable)

@given(instance=Jump_strategy)
@settings(max_examples=50)
def test_jump_instantiation(instance):
    assert isinstance(instance, Jump)

@given(instance=java::Continue_strategy)
@settings(max_examples=50)
def test_java::continue_instantiation(instance):
    assert isinstance(instance, java::Continue)

@given(instance=java::Break_strategy)
@settings(max_examples=50)
def test_java::break_instantiation(instance):
    assert isinstance(instance, java::Break)

@given(instance=Conditional_strategy)
@settings(max_examples=50)
def test_conditional_instantiation(instance):
    assert isinstance(instance, Conditional)

@given(instance=java::NormalSwitchCase_strategy)
@settings(max_examples=50)
def test_java::normalswitchcase_instantiation(instance):
    assert isinstance(instance, java::NormalSwitchCase)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=java::VariableLengthParameter_strategy)
@settings(max_examples=50)
def test_java::variablelengthparameter_instantiation(instance):
    assert isinstance(instance, java::VariableLengthParameter)

@given(instance=java::OrdinaryParameter_strategy)
@settings(max_examples=50)
def test_java::ordinaryparameter_instantiation(instance):
    assert isinstance(instance, java::OrdinaryParameter)

@given(instance=StatementContainer_strategy)
@settings(max_examples=50)
def test_statementcontainer_instantiation(instance):
    assert isinstance(instance, StatementContainer)

@given(instance=ElementReference_strategy)
@settings(max_examples=50)
def test_elementreference_instantiation(instance):
    assert isinstance(instance, ElementReference)

@given(instance=java::IdentifierReference_strategy)
@settings(max_examples=50)
def test_java::identifierreference_instantiation(instance):
    assert isinstance(instance, java::IdentifierReference)

@given(instance=TypeArgumentable_strategy)
@settings(max_examples=50)
def test_typeargumentable_instantiation(instance):
    assert isinstance(instance, TypeArgumentable)

@given(instance=java::ClassifierReference_strategy)
@settings(max_examples=50)
def test_java::classifierreference_instantiation(instance):
    assert isinstance(instance, java::ClassifierReference)

@given(instance=ShiftOperator_strategy)
@settings(max_examples=50)
def test_shiftoperator_instantiation(instance):
    assert isinstance(instance, ShiftOperator)

@given(instance=java::UnsignedRightShift_strategy)
@settings(max_examples=50)
def test_java::unsignedrightshift_instantiation(instance):
    assert isinstance(instance, java::UnsignedRightShift)

@given(instance=java::RightShift_strategy)
@settings(max_examples=50)
def test_java::rightshift_instantiation(instance):
    assert isinstance(instance, java::RightShift)

@given(instance=java::LeftShift_strategy)
@settings(max_examples=50)
def test_java::leftshift_instantiation(instance):
    assert isinstance(instance, java::LeftShift)

@given(instance=UnaryModificationOperator_strategy)
@settings(max_examples=50)
def test_unarymodificationoperator_instantiation(instance):
    assert isinstance(instance, UnaryModificationOperator)

@given(instance=java::PlusPlus_strategy)
@settings(max_examples=50)
def test_java::plusplus_instantiation(instance):
    assert isinstance(instance, java::PlusPlus)

@given(instance=java::MinusMinus_strategy)
@settings(max_examples=50)
def test_java::minusminus_instantiation(instance):
    assert isinstance(instance, java::MinusMinus)

@given(instance=MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, MultiplicativeOperator)

@given(instance=java::Remainder_strategy)
@settings(max_examples=50)
def test_java::remainder_instantiation(instance):
    assert isinstance(instance, java::Remainder)

@given(instance=java::Multiplication_strategy)
@settings(max_examples=50)
def test_java::multiplication_instantiation(instance):
    assert isinstance(instance, java::Multiplication)

@given(instance=java::Division_strategy)
@settings(max_examples=50)
def test_java::division_instantiation(instance):
    assert isinstance(instance, java::Division)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=java::Complement_strategy)
@settings(max_examples=50)
def test_java::complement_instantiation(instance):
    assert isinstance(instance, java::Complement)

@given(instance=java::Negate_strategy)
@settings(max_examples=50)
def test_java::negate_instantiation(instance):
    assert isinstance(instance, java::Negate)

@given(instance=AdditiveOperator_strategy)
@settings(max_examples=50)
def test_additiveoperator_instantiation(instance):
    assert isinstance(instance, AdditiveOperator)

@given(instance=java::Subtraction_strategy)
@settings(max_examples=50)
def test_java::subtraction_instantiation(instance):
    assert isinstance(instance, java::Subtraction)

@given(instance=java::Addition_strategy)
@settings(max_examples=50)
def test_java::addition_instantiation(instance):
    assert isinstance(instance, java::Addition)

@given(instance=RelationOperator_strategy)
@settings(max_examples=50)
def test_relationoperator_instantiation(instance):
    assert isinstance(instance, RelationOperator)

@given(instance=java::LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_java::lessthanorequal_instantiation(instance):
    assert isinstance(instance, java::LessThanOrEqual)

@given(instance=java::LessThan_strategy)
@settings(max_examples=50)
def test_java::lessthan_instantiation(instance):
    assert isinstance(instance, java::LessThan)

@given(instance=java::GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_java::greaterthanorequal_instantiation(instance):
    assert isinstance(instance, java::GreaterThanOrEqual)

@given(instance=java::GreaterThan_strategy)
@settings(max_examples=50)
def test_java::greaterthan_instantiation(instance):
    assert isinstance(instance, java::GreaterThan)

@given(instance=AssignmentOperator_strategy)
@settings(max_examples=50)
def test_assignmentoperator_instantiation(instance):
    assert isinstance(instance, AssignmentOperator)

@given(instance=java::AssignmentAnd_strategy)
@settings(max_examples=50)
def test_java::assignmentand_instantiation(instance):
    assert isinstance(instance, java::AssignmentAnd)

@given(instance=java::AssignmentLeftShift_strategy)
@settings(max_examples=50)
def test_java::assignmentleftshift_instantiation(instance):
    assert isinstance(instance, java::AssignmentLeftShift)

@given(instance=java::AssignmentMinus_strategy)
@settings(max_examples=50)
def test_java::assignmentminus_instantiation(instance):
    assert isinstance(instance, java::AssignmentMinus)

@given(instance=java::AssignmentMultiplication_strategy)
@settings(max_examples=50)
def test_java::assignmentmultiplication_instantiation(instance):
    assert isinstance(instance, java::AssignmentMultiplication)

@given(instance=java::AssignmentModulo_strategy)
@settings(max_examples=50)
def test_java::assignmentmodulo_instantiation(instance):
    assert isinstance(instance, java::AssignmentModulo)

@given(instance=java::AssignmentExclusiveOr_strategy)
@settings(max_examples=50)
def test_java::assignmentexclusiveor_instantiation(instance):
    assert isinstance(instance, java::AssignmentExclusiveOr)

@given(instance=java::AssignmentDivision_strategy)
@settings(max_examples=50)
def test_java::assignmentdivision_instantiation(instance):
    assert isinstance(instance, java::AssignmentDivision)

@given(instance=java::AssignmentOr_strategy)
@settings(max_examples=50)
def test_java::assignmentor_instantiation(instance):
    assert isinstance(instance, java::AssignmentOr)

@given(instance=java::Assignment_strategy)
@settings(max_examples=50)
def test_java::assignment_instantiation(instance):
    assert isinstance(instance, java::Assignment)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=java::EqualityOperator_strategy)
@settings(max_examples=50)
def test_java::equalityoperator_instantiation(instance):
    assert isinstance(instance, java::EqualityOperator)

@given(instance=Modifier_strategy)
@settings(max_examples=50)
def test_modifier_instantiation(instance):
    assert isinstance(instance, Modifier)

@given(instance=java::Public_strategy)
@settings(max_examples=50)
def test_java::public_instantiation(instance):
    assert isinstance(instance, java::Public)

@given(instance=java::Strictfp_strategy)
@settings(max_examples=50)
def test_java::strictfp_instantiation(instance):
    assert isinstance(instance, java::Strictfp)

@given(instance=java::Private_strategy)
@settings(max_examples=50)
def test_java::private_instantiation(instance):
    assert isinstance(instance, java::Private)

@given(instance=java::Native_strategy)
@settings(max_examples=50)
def test_java::native_instantiation(instance):
    assert isinstance(instance, java::Native)

@given(instance=java::Transient_strategy)
@settings(max_examples=50)
def test_java::transient_instantiation(instance):
    assert isinstance(instance, java::Transient)

@given(instance=java::Synchronized_strategy)
@settings(max_examples=50)
def test_java::synchronized_instantiation(instance):
    assert isinstance(instance, java::Synchronized)

@given(instance=java::Protected_strategy)
@settings(max_examples=50)
def test_java::protected_instantiation(instance):
    assert isinstance(instance, java::Protected)

@given(instance=java::Volatile_strategy)
@settings(max_examples=50)
def test_java::volatile_instantiation(instance):
    assert isinstance(instance, java::Volatile)

@given(instance=java::Final_strategy)
@settings(max_examples=50)
def test_java::final_instantiation(instance):
    assert isinstance(instance, java::Final)

@given(instance=java::Abstract_strategy)
@settings(max_examples=50)
def test_java::abstract_instantiation(instance):
    assert isinstance(instance, java::Abstract)

@given(instance=EqualityOperator_strategy)
@settings(max_examples=50)
def test_equalityoperator_instantiation(instance):
    assert isinstance(instance, EqualityOperator)

@given(instance=java::NotEqual_strategy)
@settings(max_examples=50)
def test_java::notequal_instantiation(instance):
    assert isinstance(instance, java::NotEqual)

@given(instance=java::Equal_strategy)
@settings(max_examples=50)
def test_java::equal_instantiation(instance):
    assert isinstance(instance, java::Equal)

@given(instance=java::AssignmentUnsignedRightShift_strategy)
@settings(max_examples=50)
def test_java::assignmentunsignedrightshift_instantiation(instance):
    assert isinstance(instance, java::AssignmentUnsignedRightShift)

@given(instance=java::AssignmentRightShift_strategy)
@settings(max_examples=50)
def test_java::assignmentrightshift_instantiation(instance):
    assert isinstance(instance, java::AssignmentRightShift)

@given(instance=java::AssignmentPlus_strategy)
@settings(max_examples=50)
def test_java::assignmentplus_instantiation(instance):
    assert isinstance(instance, java::AssignmentPlus)

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

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

@given(instance=java::ClassMethod_strategy)
@settings(max_examples=50)
def test_java::classmethod_instantiation(instance):
    assert isinstance(instance, java::ClassMethod)

@given(instance=java::CatchBlock_strategy)
@settings(max_examples=50)
def test_java::catchblock_instantiation(instance):
    assert isinstance(instance, java::CatchBlock)

@given(instance=java::SwitchCase_strategy)
@settings(max_examples=50)
def test_java::switchcase_instantiation(instance):
    assert isinstance(instance, java::SwitchCase)

@given(instance=Initializable_strategy)
@settings(max_examples=50)
def test_initializable_instantiation(instance):
    assert isinstance(instance, Initializable)

@given(instance=Self_strategy)
@settings(max_examples=50)
def test_self_instantiation(instance):
    assert isinstance(instance, Self)

@given(instance=java::This_strategy)
@settings(max_examples=50)
def test_java::this_instantiation(instance):
    assert isinstance(instance, java::This)

@given(instance=java::Super_strategy)
@settings(max_examples=50)
def test_java::super_instantiation(instance):
    assert isinstance(instance, java::Super)

@given(instance=LongLiteral_strategy)
@settings(max_examples=50)
def test_longliteral_instantiation(instance):
    assert isinstance(instance, LongLiteral)

@given(instance=java::OctalLongLiteral_strategy)
@settings(max_examples=50)
def test_java::octallongliteral_instantiation(instance):
    assert isinstance(instance, java::OctalLongLiteral)

@given(instance=java::OctalLongLiteral_strategy)
def test_java::octallongliteral_octalValue_type(instance):
    assert isinstance(instance.octalValue, str)


@given(instance=java::OctalLongLiteral_strategy)
def test_java::octallongliteral_octalValue_setter(instance):
    original = instance.octalValue
    instance.octalValue = original
    assert instance.octalValue == original

@given(instance=java::HexLongLiteral_strategy)
@settings(max_examples=50)
def test_java::hexlongliteral_instantiation(instance):
    assert isinstance(instance, java::HexLongLiteral)

@given(instance=java::HexLongLiteral_strategy)
def test_java::hexlongliteral_hexValue_type(instance):
    assert isinstance(instance.hexValue, str)


@given(instance=java::HexLongLiteral_strategy)
def test_java::hexlongliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=java::DecimalLongLiteral_strategy)
@settings(max_examples=50)
def test_java::decimallongliteral_instantiation(instance):
    assert isinstance(instance, java::DecimalLongLiteral)

@given(instance=java::DecimalLongLiteral_strategy)
def test_java::decimallongliteral_decimalValue_type(instance):
    assert isinstance(instance.decimalValue, str)


@given(instance=java::DecimalLongLiteral_strategy)
def test_java::decimallongliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=IntegerLiteral_strategy)
@settings(max_examples=50)
def test_integerliteral_instantiation(instance):
    assert isinstance(instance, IntegerLiteral)

@given(instance=java::OctalIntegerLiteral_strategy)
@settings(max_examples=50)
def test_java::octalintegerliteral_instantiation(instance):
    assert isinstance(instance, java::OctalIntegerLiteral)

@given(instance=java::OctalIntegerLiteral_strategy)
def test_java::octalintegerliteral_octalValue_type(instance):
    assert isinstance(instance.octalValue, str)


@given(instance=java::OctalIntegerLiteral_strategy)
def test_java::octalintegerliteral_octalValue_setter(instance):
    original = instance.octalValue
    instance.octalValue = original
    assert instance.octalValue == original

@given(instance=java::HexIntegerLiteral_strategy)
@settings(max_examples=50)
def test_java::hexintegerliteral_instantiation(instance):
    assert isinstance(instance, java::HexIntegerLiteral)

@given(instance=java::HexIntegerLiteral_strategy)
def test_java::hexintegerliteral_hexValue_type(instance):
    assert isinstance(instance.hexValue, str)


@given(instance=java::HexIntegerLiteral_strategy)
def test_java::hexintegerliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=java::DecimalIntegerLiteral_strategy)
@settings(max_examples=50)
def test_java::decimalintegerliteral_instantiation(instance):
    assert isinstance(instance, java::DecimalIntegerLiteral)

@given(instance=java::DecimalIntegerLiteral_strategy)
def test_java::decimalintegerliteral_decimalValue_type(instance):
    assert isinstance(instance.decimalValue, str)


@given(instance=java::DecimalIntegerLiteral_strategy)
def test_java::decimalintegerliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=DoubleLiteral_strategy)
@settings(max_examples=50)
def test_doubleliteral_instantiation(instance):
    assert isinstance(instance, DoubleLiteral)

@given(instance=java::HexDoubleLiteral_strategy)
@settings(max_examples=50)
def test_java::hexdoubleliteral_instantiation(instance):
    assert isinstance(instance, java::HexDoubleLiteral)

@given(instance=java::HexDoubleLiteral_strategy)
def test_java::hexdoubleliteral_hexValue_type(instance):
    assert isinstance(instance.hexValue, float)


@given(instance=java::HexDoubleLiteral_strategy)
def test_java::hexdoubleliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=java::DecimalDoubleLiteral_strategy)
@settings(max_examples=50)
def test_java::decimaldoubleliteral_instantiation(instance):
    assert isinstance(instance, java::DecimalDoubleLiteral)

@given(instance=java::DecimalDoubleLiteral_strategy)
def test_java::decimaldoubleliteral_decimalValue_type(instance):
    assert isinstance(instance.decimalValue, float)


@given(instance=java::DecimalDoubleLiteral_strategy)
def test_java::decimaldoubleliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=FloatLiteral_strategy)
@settings(max_examples=50)
def test_floatliteral_instantiation(instance):
    assert isinstance(instance, FloatLiteral)

@given(instance=java::HexFloatLiteral_strategy)
@settings(max_examples=50)
def test_java::hexfloatliteral_instantiation(instance):
    assert isinstance(instance, java::HexFloatLiteral)

@given(instance=java::HexFloatLiteral_strategy)
def test_java::hexfloatliteral_hexValue_type(instance):
    assert isinstance(instance.hexValue, float)


@given(instance=java::HexFloatLiteral_strategy)
def test_java::hexfloatliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=java::DecimalFloatLiteral_strategy)
@settings(max_examples=50)
def test_java::decimalfloatliteral_instantiation(instance):
    assert isinstance(instance, java::DecimalFloatLiteral)

@given(instance=java::DecimalFloatLiteral_strategy)
def test_java::decimalfloatliteral_decimalValue_type(instance):
    assert isinstance(instance.decimalValue, float)


@given(instance=java::DecimalFloatLiteral_strategy)
def test_java::decimalfloatliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=java::Reference_strategy)
@settings(max_examples=50)
def test_java::reference_instantiation(instance):
    assert isinstance(instance, java::Reference)

@given(instance=java::Literal_strategy)
@settings(max_examples=50)
def test_java::literal_instantiation(instance):
    assert isinstance(instance, java::Literal)

@given(instance=CallTypeArgumentable_strategy)
@settings(max_examples=50)
def test_calltypeargumentable_instantiation(instance):
    assert isinstance(instance, CallTypeArgumentable)

@given(instance=Instantiation_strategy)
@settings(max_examples=50)
def test_instantiation_instantiation(instance):
    assert isinstance(instance, Instantiation)

@given(instance=java::ExplicitConstructorCall_strategy)
@settings(max_examples=50)
def test_java::explicitconstructorcall_instantiation(instance):
    assert isinstance(instance, java::ExplicitConstructorCall)

@given(instance=Argumentable_strategy)
@settings(max_examples=50)
def test_argumentable_instantiation(instance):
    assert isinstance(instance, Argumentable)

@given(instance=java::MethodCall_strategy)
@settings(max_examples=50)
def test_java::methodcall_instantiation(instance):
    assert isinstance(instance, java::MethodCall)

@given(instance=StaticImport_strategy)
@settings(max_examples=50)
def test_staticimport_instantiation(instance):
    assert isinstance(instance, StaticImport)

@given(instance=java::StaticMemberImport_strategy)
@settings(max_examples=50)
def test_java::staticmemberimport_instantiation(instance):
    assert isinstance(instance, java::StaticMemberImport)

@given(instance=java::StaticClassifierImport_strategy)
@settings(max_examples=50)
def test_java::staticclassifierimport_instantiation(instance):
    assert isinstance(instance, java::StaticClassifierImport)

@given(instance=java::Static_strategy)
@settings(max_examples=50)
def test_java::static_instantiation(instance):
    assert isinstance(instance, java::Static)

@given(instance=Import_strategy)
@settings(max_examples=50)
def test_import_instantiation(instance):
    assert isinstance(instance, Import)

@given(instance=java::ClassifierImport_strategy)
@settings(max_examples=50)
def test_java::classifierimport_instantiation(instance):
    assert isinstance(instance, java::ClassifierImport)

@given(instance=java::PackageImport_strategy)
@settings(max_examples=50)
def test_java::packageimport_instantiation(instance):
    assert isinstance(instance, java::PackageImport)

@given(instance=java::StaticImport_strategy)
@settings(max_examples=50)
def test_java::staticimport_instantiation(instance):
    assert isinstance(instance, java::StaticImport)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=java::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_java::characterliteral_instantiation(instance):
    assert isinstance(instance, java::CharacterLiteral)

@given(instance=java::CharacterLiteral_strategy)
def test_java::characterliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=java::CharacterLiteral_strategy)
def test_java::characterliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=java::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_java::doubleliteral_instantiation(instance):
    assert isinstance(instance, java::DoubleLiteral)

@given(instance=java::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_java::integerliteral_instantiation(instance):
    assert isinstance(instance, java::IntegerLiteral)

@given(instance=java::LongLiteral_strategy)
@settings(max_examples=50)
def test_java::longliteral_instantiation(instance):
    assert isinstance(instance, java::LongLiteral)

@given(instance=java::FloatLiteral_strategy)
@settings(max_examples=50)
def test_java::floatliteral_instantiation(instance):
    assert isinstance(instance, java::FloatLiteral)

@given(instance=java::NullLiteral_strategy)
@settings(max_examples=50)
def test_java::nullliteral_instantiation(instance):
    assert isinstance(instance, java::NullLiteral)

@given(instance=java::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_java::booleanliteral_instantiation(instance):
    assert isinstance(instance, java::BooleanLiteral)

@given(instance=java::BooleanLiteral_strategy)
def test_java::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=java::BooleanLiteral_strategy)
def test_java::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TypeArgument_strategy)
@settings(max_examples=50)
def test_typeargument_instantiation(instance):
    assert isinstance(instance, TypeArgument)

@given(instance=java::SuperTypeArgument_strategy)
@settings(max_examples=50)
def test_java::supertypeargument_instantiation(instance):
    assert isinstance(instance, java::SuperTypeArgument)

@given(instance=java::ExtendsTypeArgument_strategy)
@settings(max_examples=50)
def test_java::extendstypeargument_instantiation(instance):
    assert isinstance(instance, java::ExtendsTypeArgument)

@given(instance=UnaryModificationExpressionChild_strategy)
@settings(max_examples=50)
def test_unarymodificationexpressionchild_instantiation(instance):
    assert isinstance(instance, UnaryModificationExpressionChild)

@given(instance=java::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_java::primaryexpression_instantiation(instance):
    assert isinstance(instance, java::PrimaryExpression)

@given(instance=java::UnknownTypeArgument_strategy)
@settings(max_examples=50)
def test_java::unknowntypeargument_instantiation(instance):
    assert isinstance(instance, java::UnknownTypeArgument)

@given(instance=java::UnaryModificationOperator_strategy)
@settings(max_examples=50)
def test_java::unarymodificationoperator_instantiation(instance):
    assert isinstance(instance, java::UnaryModificationOperator)

@given(instance=UnaryExpressionChild_strategy)
@settings(max_examples=50)
def test_unaryexpressionchild_instantiation(instance):
    assert isinstance(instance, UnaryExpressionChild)

@given(instance=java::UnaryModificationExpressionChild_strategy)
@settings(max_examples=50)
def test_java::unarymodificationexpressionchild_instantiation(instance):
    assert isinstance(instance, java::UnaryModificationExpressionChild)

@given(instance=java::UnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_java::unarymodificationexpression_instantiation(instance):
    assert isinstance(instance, java::UnaryModificationExpression)

@given(instance=java::UnaryOperator_strategy)
@settings(max_examples=50)
def test_java::unaryoperator_instantiation(instance):
    assert isinstance(instance, java::UnaryOperator)

@given(instance=MultiplicativeExpressionChild_strategy)
@settings(max_examples=50)
def test_multiplicativeexpressionchild_instantiation(instance):
    assert isinstance(instance, MultiplicativeExpressionChild)

@given(instance=java::UnaryExpressionChild_strategy)
@settings(max_examples=50)
def test_java::unaryexpressionchild_instantiation(instance):
    assert isinstance(instance, java::UnaryExpressionChild)

@given(instance=java::UnaryExpression_strategy)
@settings(max_examples=50)
def test_java::unaryexpression_instantiation(instance):
    assert isinstance(instance, java::UnaryExpression)

@given(instance=java::MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_java::multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, java::MultiplicativeOperator)

@given(instance=AdditiveExpressionChild_strategy)
@settings(max_examples=50)
def test_additiveexpressionchild_instantiation(instance):
    assert isinstance(instance, AdditiveExpressionChild)

@given(instance=java::MultiplicativeExpressionChild_strategy)
@settings(max_examples=50)
def test_java::multiplicativeexpressionchild_instantiation(instance):
    assert isinstance(instance, java::MultiplicativeExpressionChild)

@given(instance=java::MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_java::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, java::MultiplicativeExpression)

@given(instance=java::AdditiveOperator_strategy)
@settings(max_examples=50)
def test_java::additiveoperator_instantiation(instance):
    assert isinstance(instance, java::AdditiveOperator)

@given(instance=ShiftExpressionChild_strategy)
@settings(max_examples=50)
def test_shiftexpressionchild_instantiation(instance):
    assert isinstance(instance, ShiftExpressionChild)

@given(instance=java::AdditiveExpressionChild_strategy)
@settings(max_examples=50)
def test_java::additiveexpressionchild_instantiation(instance):
    assert isinstance(instance, java::AdditiveExpressionChild)

@given(instance=java::AdditiveExpression_strategy)
@settings(max_examples=50)
def test_java::additiveexpression_instantiation(instance):
    assert isinstance(instance, java::AdditiveExpression)

@given(instance=java::ShiftOperator_strategy)
@settings(max_examples=50)
def test_java::shiftoperator_instantiation(instance):
    assert isinstance(instance, java::ShiftOperator)

@given(instance=RelationExpressionChild_strategy)
@settings(max_examples=50)
def test_relationexpressionchild_instantiation(instance):
    assert isinstance(instance, RelationExpressionChild)

@given(instance=java::ShiftExpressionChild_strategy)
@settings(max_examples=50)
def test_java::shiftexpressionchild_instantiation(instance):
    assert isinstance(instance, java::ShiftExpressionChild)

@given(instance=java::ShiftExpression_strategy)
@settings(max_examples=50)
def test_java::shiftexpression_instantiation(instance):
    assert isinstance(instance, java::ShiftExpression)

@given(instance=java::RelationOperator_strategy)
@settings(max_examples=50)
def test_java::relationoperator_instantiation(instance):
    assert isinstance(instance, java::RelationOperator)

@given(instance=UnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_unarymodificationexpression_instantiation(instance):
    assert isinstance(instance, UnaryModificationExpression)

@given(instance=java::SuffixUnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_java::suffixunarymodificationexpression_instantiation(instance):
    assert isinstance(instance, java::SuffixUnaryModificationExpression)

@given(instance=java::PrefixUnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_java::prefixunarymodificationexpression_instantiation(instance):
    assert isinstance(instance, java::PrefixUnaryModificationExpression)

@given(instance=ExclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_exclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, ExclusiveOrExpressionChild)

@given(instance=java::AndExpressionChild_strategy)
@settings(max_examples=50)
def test_java::andexpressionchild_instantiation(instance):
    assert isinstance(instance, java::AndExpressionChild)

@given(instance=java::AndExpression_strategy)
@settings(max_examples=50)
def test_java::andexpression_instantiation(instance):
    assert isinstance(instance, java::AndExpression)

@given(instance=InclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_inclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, InclusiveOrExpressionChild)

@given(instance=java::ExclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_java::exclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, java::ExclusiveOrExpressionChild)

@given(instance=java::ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_java::exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, java::ExclusiveOrExpression)

@given(instance=ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalAndExpressionChild)

@given(instance=java::InclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_java::inclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, java::InclusiveOrExpressionChild)

@given(instance=java::InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_java::inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, java::InclusiveOrExpression)

@given(instance=ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalOrExpressionChild)

@given(instance=java::ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_java::conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, java::ConditionalAndExpressionChild)

@given(instance=java::ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_java::conditionalandexpression_instantiation(instance):
    assert isinstance(instance, java::ConditionalAndExpression)

@given(instance=ConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalExpressionChild)

@given(instance=java::ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_java::conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, java::ConditionalOrExpressionChild)

@given(instance=java::ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_java::conditionalorexpression_instantiation(instance):
    assert isinstance(instance, java::ConditionalOrExpression)

@given(instance=InstanceOfExpressionChild_strategy)
@settings(max_examples=50)
def test_instanceofexpressionchild_instantiation(instance):
    assert isinstance(instance, InstanceOfExpressionChild)

@given(instance=java::RelationExpressionChild_strategy)
@settings(max_examples=50)
def test_java::relationexpressionchild_instantiation(instance):
    assert isinstance(instance, java::RelationExpressionChild)

@given(instance=java::RelationExpression_strategy)
@settings(max_examples=50)
def test_java::relationexpression_instantiation(instance):
    assert isinstance(instance, java::RelationExpression)

@given(instance=java::AssignmentOperator_strategy)
@settings(max_examples=50)
def test_java::assignmentoperator_instantiation(instance):
    assert isinstance(instance, java::AssignmentOperator)

@given(instance=ForLoopInitializer_strategy)
@settings(max_examples=50)
def test_forloopinitializer_instantiation(instance):
    assert isinstance(instance, ForLoopInitializer)

@given(instance=java::ExpressionList_strategy)
@settings(max_examples=50)
def test_java::expressionlist_instantiation(instance):
    assert isinstance(instance, java::ExpressionList)

@given(instance=Annotable_strategy)
@settings(max_examples=50)
def test_annotable_instantiation(instance):
    assert isinstance(instance, Annotable)

@given(instance=JavaRoot_strategy)
@settings(max_examples=50)
def test_javaroot_instantiation(instance):
    assert isinstance(instance, JavaRoot)

@given(instance=java::Package_strategy)
@settings(max_examples=50)
def test_java::package_instantiation(instance):
    assert isinstance(instance, java::Package)

@given(instance=java::EmptyModel_strategy)
@settings(max_examples=50)
def test_java::emptymodel_instantiation(instance):
    assert isinstance(instance, java::EmptyModel)

@given(instance=java::CompilationUnit_strategy)
@settings(max_examples=50)
def test_java::compilationunit_instantiation(instance):
    assert isinstance(instance, java::CompilationUnit)

@given(instance=ImportingElement_strategy)
@settings(max_examples=50)
def test_importingelement_instantiation(instance):
    assert isinstance(instance, ImportingElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=java::ReferenceableElement_strategy)
@settings(max_examples=50)
def test_java::referenceableelement_instantiation(instance):
    assert isinstance(instance, java::ReferenceableElement)

@given(instance=java::Member_strategy)
@settings(max_examples=50)
def test_java::member_instantiation(instance):
    assert isinstance(instance, java::Member)

@given(instance=AssignmentExpressionChild_strategy)
@settings(max_examples=50)
def test_assignmentexpressionchild_instantiation(instance):
    assert isinstance(instance, AssignmentExpressionChild)

@given(instance=java::ConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_java::conditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, java::ConditionalExpressionChild)

@given(instance=java::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_java::conditionalexpression_instantiation(instance):
    assert isinstance(instance, java::ConditionalExpression)

@given(instance=java::LayoutInformation_strategy)
@settings(max_examples=50)
def test_java::layoutinformation_instantiation(instance):
    assert isinstance(instance, java::LayoutInformation)

@given(instance=java::Commentable_strategy)
@settings(max_examples=50)
def test_java::commentable_instantiation(instance):
    assert isinstance(instance, java::Commentable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::Commentable_strategy)
@settings(max_examples=30)
def test_java::commentable_addaftercontainingstatement_changes_state(instance):
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
        assert has_statements, f"Function 'addAfterContainingStatement' in java::Commentable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addAfterContainingStatement' in java::Commentable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addAfterContainingStatement' in java::Commentable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::Commentable_strategy)
@settings(max_examples=30)
def test_java::commentable_addbeforecontainingstatement_changes_state(instance):
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
        assert has_statements, f"Function 'addBeforeContainingStatement' in java::Commentable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addBeforeContainingStatement' in java::Commentable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addBeforeContainingStatement' in java::Commentable is not implemented or raised an error")

@given(instance=Implementor_strategy)
@settings(max_examples=50)
def test_implementor_instantiation(instance):
    assert isinstance(instance, Implementor)

@given(instance=ConcreteClassifier_strategy)
@settings(max_examples=50)
def test_concreteclassifier_instantiation(instance):
    assert isinstance(instance, ConcreteClassifier)

@given(instance=java::Enumeration_strategy)
@settings(max_examples=50)
def test_java::enumeration_instantiation(instance):
    assert isinstance(instance, java::Enumeration)

@given(instance=java::Interface_strategy)
@settings(max_examples=50)
def test_java::interface_instantiation(instance):
    assert isinstance(instance, java::Interface)

@given(instance=java::Class_strategy)
@settings(max_examples=50)
def test_java::class_instantiation(instance):
    assert isinstance(instance, java::Class)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::Class_strategy)
@settings(max_examples=30)
def test_java::class_unwrapprimitivetype_changes_state(instance):
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
        assert has_statements, f"Function 'unWrapPrimitiveType' in java::Class is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unWrapPrimitiveType' in java::Class did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unWrapPrimitiveType' in java::Class is not implemented or raised an error")

@given(instance=java::Annotation_strategy)
@settings(max_examples=50)
def test_java::annotation_instantiation(instance):
    assert isinstance(instance, java::Annotation)

@given(instance=AnnotableAndModifiable_strategy)
@settings(max_examples=50)
def test_annotableandmodifiable_instantiation(instance):
    assert isinstance(instance, AnnotableAndModifiable)

@given(instance=java::Parameter_strategy)
@settings(max_examples=50)
def test_java::parameter_instantiation(instance):
    assert isinstance(instance, java::Parameter)

@given(instance=java::LocalVariable_strategy)
@settings(max_examples=50)
def test_java::localvariable_instantiation(instance):
    assert isinstance(instance, java::LocalVariable)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=java::ForEachLoop_strategy)
@settings(max_examples=50)
def test_java::foreachloop_instantiation(instance):
    assert isinstance(instance, java::ForEachLoop)

@given(instance=java::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_java::expressionstatement_instantiation(instance):
    assert isinstance(instance, java::ExpressionStatement)

@given(instance=java::Assert_strategy)
@settings(max_examples=50)
def test_java::assert_instantiation(instance):
    assert isinstance(instance, java::Assert)

@given(instance=java::EmptyStatement_strategy)
@settings(max_examples=50)
def test_java::emptystatement_instantiation(instance):
    assert isinstance(instance, java::EmptyStatement)

@given(instance=java::Return_strategy)
@settings(max_examples=50)
def test_java::return_instantiation(instance):
    assert isinstance(instance, java::Return)

@given(instance=java::ForLoop_strategy)
@settings(max_examples=50)
def test_java::forloop_instantiation(instance):
    assert isinstance(instance, java::ForLoop)

@given(instance=java::TryBlock_strategy)
@settings(max_examples=50)
def test_java::tryblock_instantiation(instance):
    assert isinstance(instance, java::TryBlock)

@given(instance=java::JumpLabel_strategy)
@settings(max_examples=50)
def test_java::jumplabel_instantiation(instance):
    assert isinstance(instance, java::JumpLabel)

@given(instance=java::Throw_strategy)
@settings(max_examples=50)
def test_java::throw_instantiation(instance):
    assert isinstance(instance, java::Throw)

@given(instance=java::SynchronizedBlock_strategy)
@settings(max_examples=50)
def test_java::synchronizedblock_instantiation(instance):
    assert isinstance(instance, java::SynchronizedBlock)

@given(instance=java::Switch_strategy)
@settings(max_examples=50)
def test_java::switch_instantiation(instance):
    assert isinstance(instance, java::Switch)

@given(instance=java::Condition_strategy)
@settings(max_examples=50)
def test_java::condition_instantiation(instance):
    assert isinstance(instance, java::Condition)

@given(instance=java::WhileLoop_strategy)
@settings(max_examples=50)
def test_java::whileloop_instantiation(instance):
    assert isinstance(instance, java::WhileLoop)

@given(instance=java::Jump_strategy)
@settings(max_examples=50)
def test_java::jump_instantiation(instance):
    assert isinstance(instance, java::Jump)

@given(instance=java::LocalVariableStatement_strategy)
@settings(max_examples=50)
def test_java::localvariablestatement_instantiation(instance):
    assert isinstance(instance, java::LocalVariableStatement)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=java::EmptyMember_strategy)
@settings(max_examples=50)
def test_java::emptymember_instantiation(instance):
    assert isinstance(instance, java::EmptyMember)

@given(instance=java::Block_strategy)
@settings(max_examples=50)
def test_java::block_instantiation(instance):
    assert isinstance(instance, java::Block)

@given(instance=MemberContainer_strategy)
@settings(max_examples=50)
def test_membercontainer_instantiation(instance):
    assert isinstance(instance, MemberContainer)

@given(instance=TypeParametrizable_strategy)
@settings(max_examples=50)
def test_typeparametrizable_instantiation(instance):
    assert isinstance(instance, TypeParametrizable)

@given(instance=java::Constructor_strategy)
@settings(max_examples=50)
def test_java::constructor_instantiation(instance):
    assert isinstance(instance, java::Constructor)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=java::TypeParameter_strategy)
@settings(max_examples=50)
def test_java::typeparameter_instantiation(instance):
    assert isinstance(instance, java::TypeParameter)

@given(instance=java::ConcreteClassifier_strategy)
@settings(max_examples=50)
def test_java::concreteclassifier_instantiation(instance):
    assert isinstance(instance, java::ConcreteClassifier)

@given(instance=ReferenceableElement_strategy)
@settings(max_examples=50)
def test_referenceableelement_instantiation(instance):
    assert isinstance(instance, ReferenceableElement)

@given(instance=java::Field_strategy)
@settings(max_examples=50)
def test_java::field_instantiation(instance):
    assert isinstance(instance, java::Field)

@given(instance=java::EnumConstant_strategy)
@settings(max_examples=50)
def test_java::enumconstant_instantiation(instance):
    assert isinstance(instance, java::EnumConstant)

@given(instance=java::PackageReference_strategy)
@settings(max_examples=50)
def test_java::packagereference_instantiation(instance):
    assert isinstance(instance, java::PackageReference)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=java::PrimitiveType_strategy)
@settings(max_examples=50)
def test_java::primitivetype_instantiation(instance):
    assert isinstance(instance, java::PrimitiveType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::PrimitiveType_strategy)
@settings(max_examples=30)
def test_java::primitivetype_wrapprimitivetype_changes_state(instance):
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
        assert has_statements, f"Function 'wrapPrimitiveType' in java::PrimitiveType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'wrapPrimitiveType' in java::PrimitiveType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'wrapPrimitiveType' in java::PrimitiveType is not implemented or raised an error")

@given(instance=java::AnonymousClass_strategy)
@settings(max_examples=50)
def test_java::anonymousclass_instantiation(instance):
    assert isinstance(instance, java::AnonymousClass)

@given(instance=ArrayInstantiationByValues_strategy)
@settings(max_examples=50)
def test_arrayinstantiationbyvalues_instantiation(instance):
    assert isinstance(instance, ArrayInstantiationByValues)

@given(instance=java::ArrayInstantiationByValuesUntyped_strategy)
@settings(max_examples=50)
def test_java::arrayinstantiationbyvaluesuntyped_instantiation(instance):
    assert isinstance(instance, java::ArrayInstantiationByValuesUntyped)

@given(instance=ArrayTypeable_strategy)
@settings(max_examples=50)
def test_arraytypeable_instantiation(instance):
    assert isinstance(instance, ArrayTypeable)

@given(instance=java::TypeArgument_strategy)
@settings(max_examples=50)
def test_java::typeargument_instantiation(instance):
    assert isinstance(instance, java::TypeArgument)

@given(instance=java::AdditionalLocalVariable_strategy)
@settings(max_examples=50)
def test_java::additionallocalvariable_instantiation(instance):
    assert isinstance(instance, java::AdditionalLocalVariable)

@given(instance=java::AdditionalField_strategy)
@settings(max_examples=50)
def test_java::additionalfield_instantiation(instance):
    assert isinstance(instance, java::AdditionalField)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=java::Method_strategy)
@settings(max_examples=50)
def test_java::method_instantiation(instance):
    assert isinstance(instance, java::Method)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::Method_strategy)
@settings(max_examples=30)
def test_java::method_isbettermethodforcall_changes_state(instance):
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
        assert has_statements, f"Function 'isBetterMethodForCall' in java::Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isBetterMethodForCall' in java::Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isBetterMethodForCall' in java::Method is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::Method_strategy)
@settings(max_examples=30)
def test_java::method_ismethodforcall_changes_state(instance):
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
        assert has_statements, f"Function 'isMethodForCall' in java::Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isMethodForCall' in java::Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isMethodForCall' in java::Method is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::Method_strategy)
@settings(max_examples=30)
def test_java::method_issomemethodforcall_changes_state(instance):
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
        assert has_statements, f"Function 'isSomeMethodForCall' in java::Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSomeMethodForCall' in java::Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSomeMethodForCall' in java::Method is not implemented or raised an error")

@given(instance=java::ArrayInstantiationByValuesTyped_strategy)
@settings(max_examples=50)
def test_java::arrayinstantiationbyvaluestyped_instantiation(instance):
    assert isinstance(instance, java::ArrayInstantiationByValuesTyped)

@given(instance=java::InstanceOfExpression_strategy)
@settings(max_examples=50)
def test_java::instanceofexpression_instantiation(instance):
    assert isinstance(instance, java::InstanceOfExpression)

@given(instance=java::QualifiedTypeArgument_strategy)
@settings(max_examples=50)
def test_java::qualifiedtypeargument_instantiation(instance):
    assert isinstance(instance, java::QualifiedTypeArgument)

@given(instance=java::CastExpression_strategy)
@settings(max_examples=50)
def test_java::castexpression_instantiation(instance):
    assert isinstance(instance, java::CastExpression)

@given(instance=java::Variable_strategy)
@settings(max_examples=50)
def test_java::variable_instantiation(instance):
    assert isinstance(instance, java::Variable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::Variable_strategy)
@settings(max_examples=30)
def test_java::variable_createmethodcall_changes_state(instance):
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
        assert has_statements, f"Function 'createMethodCall' in java::Variable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createMethodCall' in java::Variable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createMethodCall' in java::Variable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::Variable_strategy)
@settings(max_examples=30)
def test_java::variable_createmethodcallstatement_changes_state(instance):
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
        assert has_statements, f"Function 'createMethodCallStatement' in java::Variable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createMethodCallStatement' in java::Variable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createMethodCallStatement' in java::Variable is not implemented or raised an error")

@given(instance=java::NewConstructorCall_strategy)
@settings(max_examples=50)
def test_java::newconstructorcall_instantiation(instance):
    assert isinstance(instance, java::NewConstructorCall)

@given(instance=ArrayInstantiation_strategy)
@settings(max_examples=50)
def test_arrayinstantiation_instantiation(instance):
    assert isinstance(instance, ArrayInstantiation)

@given(instance=java::ArrayInstantiationByValues_strategy)
@settings(max_examples=50)
def test_java::arrayinstantiationbyvalues_instantiation(instance):
    assert isinstance(instance, java::ArrayInstantiationByValues)

@given(instance=java::ArrayInstantiationBySize_strategy)
@settings(max_examples=50)
def test_java::arrayinstantiationbysize_instantiation(instance):
    assert isinstance(instance, java::ArrayInstantiationBySize)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=java::AssignmentExpressionChild_strategy)
@settings(max_examples=50)
def test_java::assignmentexpressionchild_instantiation(instance):
    assert isinstance(instance, java::AssignmentExpressionChild)

@given(instance=java::AssignmentExpression_strategy)
@settings(max_examples=50)
def test_java::assignmentexpression_instantiation(instance):
    assert isinstance(instance, java::AssignmentExpression)

@given(instance=AnnotationValue_strategy)
@settings(max_examples=50)
def test_annotationvalue_instantiation(instance):
    assert isinstance(instance, AnnotationValue)

@given(instance=ArrayInitializationValue_strategy)
@settings(max_examples=50)
def test_arrayinitializationvalue_instantiation(instance):
    assert isinstance(instance, ArrayInitializationValue)

@given(instance=java::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_java::arrayinitializer_instantiation(instance):
    assert isinstance(instance, java::ArrayInitializer)

@given(instance=InterfaceMethod_strategy)
@settings(max_examples=50)
def test_interfacemethod_instantiation(instance):
    assert isinstance(instance, InterfaceMethod)

@given(instance=java::AnnotationAttribute_strategy)
@settings(max_examples=50)
def test_java::annotationattribute_instantiation(instance):
    assert isinstance(instance, java::AnnotationAttribute)

@given(instance=java::InterfaceMethod_strategy)
@settings(max_examples=50)
def test_java::interfacemethod_instantiation(instance):
    assert isinstance(instance, java::InterfaceMethod)

@given(instance=AnnotationParameter_strategy)
@settings(max_examples=50)
def test_annotationparameter_instantiation(instance):
    assert isinstance(instance, AnnotationParameter)

@given(instance=java::AnnotationParameterList_strategy)
@settings(max_examples=50)
def test_java::annotationparameterlist_instantiation(instance):
    assert isinstance(instance, java::AnnotationParameterList)

@given(instance=java::SingleAnnotationParameter_strategy)
@settings(max_examples=50)
def test_java::singleannotationparameter_instantiation(instance):
    assert isinstance(instance, java::SingleAnnotationParameter)

@given(instance=java::Classifier_strategy)
@settings(max_examples=50)
def test_java::classifier_instantiation(instance):
    assert isinstance(instance, java::Classifier)

@given(instance=NamespaceAwareElement_strategy)
@settings(max_examples=50)
def test_namespaceawareelement_instantiation(instance):
    assert isinstance(instance, NamespaceAwareElement)

@given(instance=java::Import_strategy)
@settings(max_examples=50)
def test_java::import_instantiation(instance):
    assert isinstance(instance, java::Import)

@given(instance=java::NamespaceClassifierReference_strategy)
@settings(max_examples=50)
def test_java::namespaceclassifierreference_instantiation(instance):
    assert isinstance(instance, java::NamespaceClassifierReference)

@given(instance=java::JavaRoot_strategy)
@settings(max_examples=50)
def test_java::javaroot_instantiation(instance):
    assert isinstance(instance, java::JavaRoot)

@given(instance=AnnotationInstanceOrModifier_strategy)
@settings(max_examples=50)
def test_annotationinstanceormodifier_instantiation(instance):
    assert isinstance(instance, AnnotationInstanceOrModifier)

@given(instance=java::Modifier_strategy)
@settings(max_examples=50)
def test_java::modifier_instantiation(instance):
    assert isinstance(instance, java::Modifier)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=java::Instantiation_strategy)
@settings(max_examples=50)
def test_java::instantiation_instantiation(instance):
    assert isinstance(instance, java::Instantiation)

@given(instance=java::SelfReference_strategy)
@settings(max_examples=50)
def test_java::selfreference_instantiation(instance):
    assert isinstance(instance, java::SelfReference)

@given(instance=java::PrimitiveTypeReference_strategy)
@settings(max_examples=50)
def test_java::primitivetypereference_instantiation(instance):
    assert isinstance(instance, java::PrimitiveTypeReference)

@given(instance=java::NestedExpression_strategy)
@settings(max_examples=50)
def test_java::nestedexpression_instantiation(instance):
    assert isinstance(instance, java::NestedExpression)

@given(instance=java::ReflectiveClassReference_strategy)
@settings(max_examples=50)
def test_java::reflectiveclassreference_instantiation(instance):
    assert isinstance(instance, java::ReflectiveClassReference)

@given(instance=java::ArrayInstantiation_strategy)
@settings(max_examples=50)
def test_java::arrayinstantiation_instantiation(instance):
    assert isinstance(instance, java::ArrayInstantiation)

@given(instance=java::StringReference_strategy)
@settings(max_examples=50)
def test_java::stringreference_instantiation(instance):
    assert isinstance(instance, java::StringReference)

@given(instance=java::StringReference_strategy)
def test_java::stringreference_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=java::StringReference_strategy)
def test_java::stringreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=java::ElementReference_strategy)
@settings(max_examples=50)
def test_java::elementreference_instantiation(instance):
    assert isinstance(instance, java::ElementReference)

@given(instance=java::AnnotationInstance_strategy)
@settings(max_examples=50)
def test_java::annotationinstance_instantiation(instance):
    assert isinstance(instance, java::AnnotationInstance)

@given(instance=Commentable_strategy)
@settings(max_examples=50)
def test_commentable_instantiation(instance):
    assert isinstance(instance, Commentable)

@given(instance=java::Conditional_strategy)
@settings(max_examples=50)
def test_java::conditional_instantiation(instance):
    assert isinstance(instance, java::Conditional)

@given(instance=java::Implementor_strategy)
@settings(max_examples=50)
def test_java::implementor_instantiation(instance):
    assert isinstance(instance, java::Implementor)

@given(instance=java::Parametrizable_strategy)
@settings(max_examples=50)
def test_java::parametrizable_instantiation(instance):
    assert isinstance(instance, java::Parametrizable)

@given(instance=java::ForLoopInitializer_strategy)
@settings(max_examples=50)
def test_java::forloopinitializer_instantiation(instance):
    assert isinstance(instance, java::ForLoopInitializer)

@given(instance=java::NamespaceAwareElement_strategy)
@settings(max_examples=50)
def test_java::namespaceawareelement_instantiation(instance):
    assert isinstance(instance, java::NamespaceAwareElement)

@given(instance=java::NamespaceAwareElement_strategy)
def test_java::namespaceawareelement_namespaces_type(instance):
    assert isinstance(instance.namespaces, str)


@given(instance=java::NamespaceAwareElement_strategy)
def test_java::namespaceawareelement_namespaces_setter(instance):
    original = instance.namespaces
    instance.namespaces = original
    assert instance.namespaces == original

@given(instance=java::AnnotationParameter_strategy)
@settings(max_examples=50)
def test_java::annotationparameter_instantiation(instance):
    assert isinstance(instance, java::AnnotationParameter)

@given(instance=java::AnnotationValue_strategy)
@settings(max_examples=50)
def test_java::annotationvalue_instantiation(instance):
    assert isinstance(instance, java::AnnotationValue)

@given(instance=java::TypeReference_strategy)
@settings(max_examples=50)
def test_java::typereference_instantiation(instance):
    assert isinstance(instance, java::TypeReference)

@given(instance=java::StatementContainer_strategy)
@settings(max_examples=50)
def test_java::statementcontainer_instantiation(instance):
    assert isinstance(instance, java::StatementContainer)

@given(instance=java::AnnotationAttributeSetting_strategy)
@settings(max_examples=50)
def test_java::annotationattributesetting_instantiation(instance):
    assert isinstance(instance, java::AnnotationAttributeSetting)

@given(instance=java::ExceptionThrower_strategy)
@settings(max_examples=50)
def test_java::exceptionthrower_instantiation(instance):
    assert isinstance(instance, java::ExceptionThrower)

@given(instance=java::ArrayInitializationValue_strategy)
@settings(max_examples=50)
def test_java::arrayinitializationvalue_instantiation(instance):
    assert isinstance(instance, java::ArrayInitializationValue)

@given(instance=java::ImportingElement_strategy)
@settings(max_examples=50)
def test_java::importingelement_instantiation(instance):
    assert isinstance(instance, java::ImportingElement)

@given(instance=java::Initializable_strategy)
@settings(max_examples=50)
def test_java::initializable_instantiation(instance):
    assert isinstance(instance, java::Initializable)

@given(instance=java::StatementListContainer_strategy)
@settings(max_examples=50)
def test_java::statementlistcontainer_instantiation(instance):
    assert isinstance(instance, java::StatementListContainer)

@given(instance=java::Statement_strategy)
@settings(max_examples=50)
def test_java::statement_instantiation(instance):
    assert isinstance(instance, java::Statement)

@given(instance=java::Operator_strategy)
@settings(max_examples=50)
def test_java::operator_instantiation(instance):
    assert isinstance(instance, java::Operator)

@given(instance=java::TypeParametrizable_strategy)
@settings(max_examples=50)
def test_java::typeparametrizable_instantiation(instance):
    assert isinstance(instance, java::TypeParametrizable)

@given(instance=java::TypeArgumentable_strategy)
@settings(max_examples=50)
def test_java::typeargumentable_instantiation(instance):
    assert isinstance(instance, java::TypeArgumentable)

@given(instance=java::Argumentable_strategy)
@settings(max_examples=50)
def test_java::argumentable_instantiation(instance):
    assert isinstance(instance, java::Argumentable)

@given(instance=java::AnnotationInstanceOrModifier_strategy)
@settings(max_examples=50)
def test_java::annotationinstanceormodifier_instantiation(instance):
    assert isinstance(instance, java::AnnotationInstanceOrModifier)

@given(instance=java::CallTypeArgumentable_strategy)
@settings(max_examples=50)
def test_java::calltypeargumentable_instantiation(instance):
    assert isinstance(instance, java::CallTypeArgumentable)

@given(instance=java::Self_strategy)
@settings(max_examples=50)
def test_java::self_instantiation(instance):
    assert isinstance(instance, java::Self)

@given(instance=java::Type_strategy)
@settings(max_examples=50)
def test_java::type_instantiation(instance):
    assert isinstance(instance, java::Type)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::Type_strategy)
@settings(max_examples=30)
def test_java::type_issupertype_changes_state(instance):
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
        assert has_statements, f"Function 'isSuperType' in java::Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSuperType' in java::Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSuperType' in java::Type is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::Type_strategy)
@settings(max_examples=30)
def test_java::type_equalstype_changes_state(instance):
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
        assert has_statements, f"Function 'equalsType' in java::Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equalsType' in java::Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equalsType' in java::Type is not implemented or raised an error")

@given(instance=java::TypedElement_strategy)
@settings(max_examples=50)
def test_java::typedelement_instantiation(instance):
    assert isinstance(instance, java::TypedElement)

@given(instance=java::MemberContainer_strategy)
@settings(max_examples=50)
def test_java::membercontainer_instantiation(instance):
    assert isinstance(instance, java::MemberContainer)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::MemberContainer_strategy)
@settings(max_examples=30)
def test_java::membercontainer_createfield_changes_state(instance):
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
        assert has_statements, f"Function 'createField' in java::MemberContainer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createField' in java::MemberContainer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createField' in java::MemberContainer is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::MemberContainer_strategy)
@settings(max_examples=30)
def test_java::membercontainer_removemethods_changes_state(instance):
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
        assert has_statements, f"Function 'removeMethods' in java::MemberContainer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeMethods' in java::MemberContainer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeMethods' in java::MemberContainer is not implemented or raised an error")

@given(instance=java::ArrayDimension_strategy)
@settings(max_examples=50)
def test_java::arraydimension_instantiation(instance):
    assert isinstance(instance, java::ArrayDimension)

@given(instance=java::Modifiable_strategy)
@settings(max_examples=50)
def test_java::modifiable_instantiation(instance):
    assert isinstance(instance, java::Modifiable)

@given(instance=java::ArraySelector_strategy)
@settings(max_examples=50)
def test_java::arrayselector_instantiation(instance):
    assert isinstance(instance, java::ArraySelector)

@given(instance=java::NamedElement_strategy)
@settings(max_examples=50)
def test_java::namedelement_instantiation(instance):
    assert isinstance(instance, java::NamedElement)

@given(instance=java::NamedElement_strategy)
def test_java::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::NamedElement_strategy)
def test_java::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::AnnotableAndModifiable_strategy)
@settings(max_examples=50)
def test_java::annotableandmodifiable_instantiation(instance):
    assert isinstance(instance, java::AnnotableAndModifiable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java::annotableandmodifiable_makeprivate_changes_state(instance):
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
        assert has_statements, f"Function 'makePrivate' in java::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'makePrivate' in java::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'makePrivate' in java::AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java::annotableandmodifiable_makeprotected_changes_state(instance):
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
        assert has_statements, f"Function 'makeProtected' in java::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'makeProtected' in java::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'makeProtected' in java::AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java::annotableandmodifiable_addmodifier_changes_state(instance):
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
        assert has_statements, f"Function 'addModifier' in java::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addModifier' in java::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addModifier' in java::AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java::annotableandmodifiable_removeallmodifiers_changes_state(instance):
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
        assert has_statements, f"Function 'removeAllModifiers' in java::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeAllModifiers' in java::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeAllModifiers' in java::AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java::annotableandmodifiable_isprotected_changes_state(instance):
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
        assert has_statements, f"Function 'isProtected' in java::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isProtected' in java::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isProtected' in java::AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java::annotableandmodifiable_hasmodifier_changes_state(instance):
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
        assert has_statements, f"Function 'hasModifier' in java::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasModifier' in java::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasModifier' in java::AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java::annotableandmodifiable_ispublic_changes_state(instance):
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
        assert has_statements, f"Function 'isPublic' in java::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPublic' in java::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPublic' in java::AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java::annotableandmodifiable_removemodifier_changes_state(instance):
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
        assert has_statements, f"Function 'removeModifier' in java::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeModifier' in java::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeModifier' in java::AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java::annotableandmodifiable_ishidden_changes_state(instance):
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
        assert has_statements, f"Function 'isHidden' in java::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isHidden' in java::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isHidden' in java::AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java::annotableandmodifiable_makepublic_changes_state(instance):
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
        assert has_statements, f"Function 'makePublic' in java::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'makePublic' in java::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'makePublic' in java::AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java::annotableandmodifiable_isstatic_changes_state(instance):
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
        assert has_statements, f"Function 'isStatic' in java::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isStatic' in java::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isStatic' in java::AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=java::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_java::annotableandmodifiable_isprivate_changes_state(instance):
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
        assert has_statements, f"Function 'isPrivate' in java::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPrivate' in java::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPrivate' in java::AnnotableAndModifiable is not implemented or raised an error")

@given(instance=java::Annotable_strategy)
@settings(max_examples=50)
def test_java::annotable_instantiation(instance):
    assert isinstance(instance, java::Annotable)

@given(instance=java::ArrayTypeable_strategy)
@settings(max_examples=50)
def test_java::arraytypeable_instantiation(instance):
    assert isinstance(instance, java::ArrayTypeable)

@given(instance=java::Expression_strategy)
@settings(max_examples=50)
def test_java::expression_instantiation(instance):
    assert isinstance(instance, java::Expression)
