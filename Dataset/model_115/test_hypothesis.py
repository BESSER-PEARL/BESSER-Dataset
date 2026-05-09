import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UnaryOperator,
    c::sharp::operators::ExclusiveOr,
    c::sharp::operators::And,
    c::sharp::operators::ConditionalOr,
    c::sharp::operators::InclusiveOr,
    c::sharp::operators::ConditionalAnd,
    c::sharp::operators::Complement,
    MultiplicativeOperator,
    c::sharp::operators::Remainder,
    c::sharp::operators::Multiplication,
    c::sharp::operators::Division,
    operators::UnaryOperator,
    operators::AdditiveOperator,
    c::sharp::operators::Subtraction,
    c::sharp::operators::Addition,
    RelationOperator,
    c::sharp::operators::LessThanOrEqual,
    c::sharp::operators::GreaterThanOrEqual,
    c::sharp::operators::LessThan,
    c::sharp::operators::GreaterThan,
    EqualityOperator,
    c::sharp::operators::NotEqual,
    c::sharp::operators::Equal,
    Operator,
    c::sharp::operators::UnaryModificationOperator,
    c::sharp::operators::RelationOperator,
    c::sharp::operators::MultiplicativeOperator,
    c::sharp::operators::EqualityOperator,
    c::sharp::operators::UnaryOperator,
    c::sharp::operators::ShiftOperator,
    c::sharp::operators::AssignmentOperator,
    c::sharp::operators::AdditiveOperator,
    c::sharp::operators::Operator,
    c::sharp::keywords::Event,
    c::sharp::keywords::Return,
    c::sharp::keywords::Default,
    c::sharp::keywords::Case,
    c::sharp::keywords::Params,
    c::sharp::keywords::Ref,
    c::sharp::keywords::Out,
    ShiftOperator,
    c::sharp::operators::UnsignedRightShift,
    c::sharp::operators::RightShift,
    c::sharp::operators::LeftShift,
    c::sharp::operators::Negate,
    UnaryModificationOperator,
    c::sharp::operators::PlusPlus,
    c::sharp::operators::MinusMinus,
    Literal,
    c::sharp::literals::RealLiteral,
    c::sharp::literals::DecimalIntegerLiteral,
    c::sharp::literals::HexadecimalIntegerLiteral,
    c::sharp::literals::BooleanLiteral,
    c::sharp::modifiers::Modifier,
    ReferenceType,
    c::sharp::types::ClassOrInterfaceOrDelegateOrEnumType,
    c::sharp::literals::StringLiteral,
    c::sharp::literals::CharacterLiteral,
    c::sharp::literals::This,
    c::sharp::literals::NullLiteral,
    types::Type,
    types::NonArrayType,
    c::sharp::types::SimpleType,
    c::sharp::types::PointerType,
    c::sharp::types::ReferenceType,
    c::sharp::types::NonArrayType,
    c::sharp::types::Type,
    ConditionalOr,
    ConditionalAndExpression,
    c::sharp::expressions::ConditionalOrExpression,
    ConditionalAnd,
    InclusiveOrExpression,
    c::sharp::expressions::ConditionalAndExpression,
    InclusiveOr,
    ExclusiveOrExpression,
    c::sharp::expressions::InclusiveOrExpression,
    ExclusiveOr,
    AndExpression,
    c::sharp::expressions::ExclusiveOrExpression,
    And,
    EqualityExpression,
    c::sharp::expressions::AndExpression,
    NotEqual,
    Equal,
    LessThanOrEqual,
    LessThan,
    ShiftExpression,
    c::sharp::expressions::RelationalExpression,
    AdditiveExpression,
    LeftShift,
    RightShift,
    c::sharp::expressions::ShiftExpression,
    MultiplicativeExpression,
    c::sharp::expressions::AdditiveExpression,
    Remainder,
    Division,
    c::sharp::expressions::MultiplicativeExpression,
    c::sharp::expressions::AddressOfExpression,
    RelationalExpression,
    c::sharp::expressions::EqualityExpression,
    GreaterThanOrEqual,
    GreaterThan,
    c::sharp::classes::FixedParameter,
    ParameterArray,
    Expression,
    VariableInitializer,
    c::sharp::arrays::ArrayInitializer,
    c::sharp::arrays::StackallocInitializer,
    VariableDeclarator,
    ConstantDeclarator,
    c::sharp::classes::VariableInitializer,
    Statement,
    c::sharp::classes::Block,
    classes::ClassMemberDeclaration,
    namespaces::NamespaceMemberDeclaration,
    c::sharp::namespaces::TypeDeclaration,
    c::sharp::namespaces::NamespaceBody,
    NamespaceBody,
    c::sharp::namespaces::NamespaceMemberDeclaration,
    NamespaceOrTypeName,
    FixedParameter,
    c::sharp::classes::FormalParameterList,
    Block,
    FormalParameterList,
    Type,
    c::sharp::classes::ClassMemberDeclaration,
    ClassOrInterfaceOrDelegateOrEnumType,
    c::sharp::classes::ClassBase,
    ClassMemberDeclaration,
    c::sharp::classes::ConstantDeclaration,
    c::sharp::classes::FieldDeclaration,
    ClassBase,
    Modifier,
    c::sharp::modifiers::ReadOnly,
    c::sharp::modifiers::Partial,
    c::sharp::modifiers::Protected,
    c::sharp::modifiers::Unsafe,
    c::sharp::modifiers::Sealed,
    c::sharp::modifiers::Abstract,
    c::sharp::modifiers::Static,
    c::sharp::modifiers::Private,
    c::sharp::modifiers::Internal,
    c::sharp::modifiers::Volatile,
    c::sharp::modifiers::Public,
    c::sharp::modifiers::OverrideModifier,
    c::sharp::modifiers::New,
    c::sharp::modifiers::Extern,
    c::sharp::modifiers::Virtual,
    Attributes,
    namespaces::TypeDeclaration,
    NamedElement,
    c::sharp::namespaces::UsingDirective,
    NamespaceMemberDeclaration,
    c::sharp::namespaces::Namespace,
    GlobalAttributes,
    UsingDirective,
    c::sharp::namespaces::CompilationUnit,
    expressions::PrimaryNoArrayCreationExpression,
    common::NamedElement,
    c::sharp::classes::Method,
    c::sharp::classes::Class,
    c::sharp::common::Identifier,
    Identifier,
    c::sharp::common::NamespaceOrTypeName,
    c::sharp::common::NamedElement,
    AssignmentOperator,
    c::sharp::operators::AssignmentMinus,
    c::sharp::operators::AssignmentRightShift,
    c::sharp::operators::AssignmentOr,
    c::sharp::operators::Assignment,
    c::sharp::operators::AssignmentAnd,
    c::sharp::operators::AssignmentModulo,
    c::sharp::operators::AssignmentPlus,
    c::sharp::operators::AssignmentDivision,
    c::sharp::operators::AssignmentMultiplication,
    c::sharp::operators::AssignmentLeftShift,
    c::sharp::operators::AssignmentExclusiveOr,
    c::sharp::operators::AssignmentUnsignedRightShift,
    expressions::Expression,
    ConditionalOrExpression,
    c::sharp::expressions::ConditionalExpression,
    AddressOfExpression,
    c::sharp::expressions::CastExpression,
    UnaryExpression,
    Multiplication,
    Complement,
    Negate,
    Subtraction,
    Addition,
    MemberAccess,
    c::sharp::expressions::UnaryExpression,
    ArrayInitializer,
    CastExpression,
    PreDecrementExpression,
    PreIncrementExpression,
    ArgumentList,
    expressions::StatementExpression,
    c::sharp::expressions::ObjectCreationExpression,
    c::sharp::expressions::AssignmentExpression,
    expressions::PrimaryExtendedExpressionType,
    c::sharp::expressions::PostDecrementExpression,
    c::sharp::expressions::PostIncrementExpression,
    c::sharp::expressions::InvocationExpression,
    SimpleType,
    c::sharp::types::Object,
    c::sharp::types::Short,
    c::sharp::types::Char,
    c::sharp::types::UInt,
    c::sharp::types::Int,
    c::sharp::types::Byte,
    c::sharp::types::SByte,
    c::sharp::types::ULong,
    c::sharp::types::Long,
    c::sharp::types::Double,
    c::sharp::types::Decimal,
    c::sharp::types::Bool,
    c::sharp::types::UShort,
    c::sharp::types::Float,
    c::sharp::types::Void,
    c::sharp::types::String,
    PrimaryExtendedExpressionType,
    c::sharp::expressions::ElementAccess,
    c::sharp::expressions::PointerMemberAccess,
    c::sharp::expressions::MemberAccess,
    c::sharp::expressions::PrimaryExtendedExpressionType,
    PrimaryExpression,
    c::sharp::expressions::ArrayCreationExpression,
    c::sharp::expressions::PrimaryNoArrayCreationExpression,
    c::sharp::expressions::PrimaryExpression,
    Argument,
    c::sharp::expressions::ArgumentList,
    c::sharp::expressions::Argument,
    c::sharp::expressions::ExpressionList,
    classes::VariableInitializer,
    PrimaryNoArrayCreationExpression,
    c::sharp::expressions::CheckedExpression,
    c::sharp::expressions::SizeOfExpression,
    c::sharp::expressions::UncheckedExpression,
    c::sharp::expressions::ParenthesizedExpression,
    c::sharp::expressions::DelegateCreationExpression,
    c::sharp::expressions::TypeOfExpression,
    c::sharp::literals::Literal,
    c::sharp::expressions::BaseAccess,
    c::sharp::statements::ConstantDeclarator,
    c::sharp::statements::LocalConstantDeclaration,
    c::sharp::statements::VariableDeclarator,
    c::sharp::expressions::StatementExpression,
    statements::ResourceAcquisition,
    c::sharp::expressions::Expression,
    statements::ForInitializer,
    c::sharp::statements::VariableDeclaration,
    c::sharp::statements::FixedPointerDeclarator,
    FixedPointerDeclarator,
    PointerType,
    c::sharp::statements::FinallyClause,
    c::sharp::statements::GeneralCatchClause,
    c::sharp::statements::SpecificCatchClause,
    FinallyClause,
    ResourceAcquisition,
    c::sharp::statements::ResourceAcquisition,
    JumpStatement,
    c::sharp::statements::ThrowStatement,
    c::sharp::statements::ReturnStatement,
    c::sharp::statements::ContinueStatement,
    c::sharp::statements::GotoStatement,
    c::sharp::statements::BreakStatement,
    c::sharp::statements::ForInitializer,
    GeneralCatchClause,
    SpecificCatchClause,
    ForInitializer,
    c::sharp::expressions::StatementExpressionList,
    IterationStatement,
    c::sharp::statements::ForeachStatement,
    c::sharp::statements::ForStatement,
    c::sharp::statements::DoStatement,
    c::sharp::statements::WhileStatement,
    Case,
    Default,
    c::sharp::statements::SwitchLabel,
    SwitchLabel,
    c::sharp::statements::SwitchSection,
    SwitchSection,
    Unsafe,
    EmbeddedStatement,
    c::sharp::statements::LockStatement,
    c::sharp::statements::ExpressionStatement,
    c::sharp::statements::UsingStatement,
    c::sharp::statements::UncheckedStatement,
    c::sharp::statements::CheckedStatement,
    c::sharp::statements::EmptyStatement,
    c::sharp::statements::JumpStatement,
    c::sharp::statements::FixedStatement,
    c::sharp::statements::IterationStatement,
    c::sharp::statements::TryStatement,
    c::sharp::statements::SimpleEmbeddedStatement,
    c::sharp::statements::EmbeddedStatement,
    LocalConstantDeclaration,
    VariableDeclaration,
    c::sharp::statements::DeclarationStatement,
    StatementExpressionList,
    SelectionStatement,
    c::sharp::statements::SwitchStatement,
    c::sharp::statements::IfStatement,
    c::sharp::statements::SelectionStatement,
    StatementExpression,
    c::sharp::expressions::PreDecrementExpression,
    c::sharp::expressions::PreIncrementExpression,
    c::sharp::attributes::Attributes,
    c::sharp::attributes::GlobalAttributeTarget,
    Attribute,
    GlobalAttributeTarget,
    c::sharp::attributes::GlobalAttributes,
    c::sharp::arrays::RankSpecifier,
    RankSpecifier,
    NonArrayType,
    c::sharp::arrays::ArrayType,
    statements::Statement,
    c::sharp::statements::LabeledStatement,
    c::sharp::statements::Statement,
    c::sharp::attributes::NamedArgument,
    NamedArgument,
    c::sharp::attributes::NamedArgumentList,
    NamedArgumentList,
    ExpressionList,
    c::sharp::attributes::AttributeArguments,
    AttributeArguments,
    c::sharp::attributes::Attribute,
    Return,
    Event,
    c::sharp::attributes::AttributeTarget,
    AttributeTarget,
    ArrayType,
    Params,
    c::sharp::classes::ParameterArray,
    Out,
    Ref,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::exclusiveor_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::ExclusiveOr)


def test_c::sharp::operators::exclusiveor_constructor_exists():
    assert callable(c::sharp::operators::ExclusiveOr.__init__)


def test_c::sharp::operators::exclusiveor_constructor_args():
    sig = inspect.signature(c::sharp::operators::ExclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::and_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::And)


def test_c::sharp::operators::and_constructor_exists():
    assert callable(c::sharp::operators::And.__init__)


def test_c::sharp::operators::and_constructor_args():
    sig = inspect.signature(c::sharp::operators::And.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::conditionalor_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::ConditionalOr)


def test_c::sharp::operators::conditionalor_constructor_exists():
    assert callable(c::sharp::operators::ConditionalOr.__init__)


def test_c::sharp::operators::conditionalor_constructor_args():
    sig = inspect.signature(c::sharp::operators::ConditionalOr.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::inclusiveor_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::InclusiveOr)


def test_c::sharp::operators::inclusiveor_constructor_exists():
    assert callable(c::sharp::operators::InclusiveOr.__init__)


def test_c::sharp::operators::inclusiveor_constructor_args():
    sig = inspect.signature(c::sharp::operators::InclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::conditionaland_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::ConditionalAnd)


def test_c::sharp::operators::conditionaland_constructor_exists():
    assert callable(c::sharp::operators::ConditionalAnd.__init__)


def test_c::sharp::operators::conditionaland_constructor_args():
    sig = inspect.signature(c::sharp::operators::ConditionalAnd.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::complement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::Complement)


def test_c::sharp::operators::complement_constructor_exists():
    assert callable(c::sharp::operators::Complement.__init__)


def test_c::sharp::operators::complement_constructor_args():
    sig = inspect.signature(c::sharp::operators::Complement.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeOperator)


def test_multiplicativeoperator_constructor_exists():
    assert callable(MultiplicativeOperator.__init__)


def test_multiplicativeoperator_constructor_args():
    sig = inspect.signature(MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::remainder_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::Remainder)


def test_c::sharp::operators::remainder_constructor_exists():
    assert callable(c::sharp::operators::Remainder.__init__)


def test_c::sharp::operators::remainder_constructor_args():
    sig = inspect.signature(c::sharp::operators::Remainder.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::multiplication_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::Multiplication)


def test_c::sharp::operators::multiplication_constructor_exists():
    assert callable(c::sharp::operators::Multiplication.__init__)


def test_c::sharp::operators::multiplication_constructor_args():
    sig = inspect.signature(c::sharp::operators::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::division_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::Division)


def test_c::sharp::operators::division_constructor_exists():
    assert callable(c::sharp::operators::Division.__init__)


def test_c::sharp::operators::division_constructor_args():
    sig = inspect.signature(c::sharp::operators::Division.__init__)
    params = list(sig.parameters.keys())



def test_operators::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(operators::UnaryOperator)


def test_operators::unaryoperator_constructor_exists():
    assert callable(operators::UnaryOperator.__init__)


def test_operators::unaryoperator_constructor_args():
    sig = inspect.signature(operators::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators::additiveoperator_is_not_abstract():
    assert not inspect.isabstract(operators::AdditiveOperator)


def test_operators::additiveoperator_constructor_exists():
    assert callable(operators::AdditiveOperator.__init__)


def test_operators::additiveoperator_constructor_args():
    sig = inspect.signature(operators::AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::subtraction_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::Subtraction)


def test_c::sharp::operators::subtraction_constructor_exists():
    assert callable(c::sharp::operators::Subtraction.__init__)


def test_c::sharp::operators::subtraction_constructor_args():
    sig = inspect.signature(c::sharp::operators::Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::addition_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::Addition)


def test_c::sharp::operators::addition_constructor_exists():
    assert callable(c::sharp::operators::Addition.__init__)


def test_c::sharp::operators::addition_constructor_args():
    sig = inspect.signature(c::sharp::operators::Addition.__init__)
    params = list(sig.parameters.keys())



def test_relationoperator_is_not_abstract():
    assert not inspect.isabstract(RelationOperator)


def test_relationoperator_constructor_exists():
    assert callable(RelationOperator.__init__)


def test_relationoperator_constructor_args():
    sig = inspect.signature(RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::LessThanOrEqual)


def test_c::sharp::operators::lessthanorequal_constructor_exists():
    assert callable(c::sharp::operators::LessThanOrEqual.__init__)


def test_c::sharp::operators::lessthanorequal_constructor_args():
    sig = inspect.signature(c::sharp::operators::LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::GreaterThanOrEqual)


def test_c::sharp::operators::greaterthanorequal_constructor_exists():
    assert callable(c::sharp::operators::GreaterThanOrEqual.__init__)


def test_c::sharp::operators::greaterthanorequal_constructor_args():
    sig = inspect.signature(c::sharp::operators::GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::lessthan_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::LessThan)


def test_c::sharp::operators::lessthan_constructor_exists():
    assert callable(c::sharp::operators::LessThan.__init__)


def test_c::sharp::operators::lessthan_constructor_args():
    sig = inspect.signature(c::sharp::operators::LessThan.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::greaterthan_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::GreaterThan)


def test_c::sharp::operators::greaterthan_constructor_exists():
    assert callable(c::sharp::operators::GreaterThan.__init__)


def test_c::sharp::operators::greaterthan_constructor_args():
    sig = inspect.signature(c::sharp::operators::GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_equalityoperator_is_not_abstract():
    assert not inspect.isabstract(EqualityOperator)


def test_equalityoperator_constructor_exists():
    assert callable(EqualityOperator.__init__)


def test_equalityoperator_constructor_args():
    sig = inspect.signature(EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::notequal_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::NotEqual)


def test_c::sharp::operators::notequal_constructor_exists():
    assert callable(c::sharp::operators::NotEqual.__init__)


def test_c::sharp::operators::notequal_constructor_args():
    sig = inspect.signature(c::sharp::operators::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::equal_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::Equal)


def test_c::sharp::operators::equal_constructor_exists():
    assert callable(c::sharp::operators::Equal.__init__)


def test_c::sharp::operators::equal_constructor_args():
    sig = inspect.signature(c::sharp::operators::Equal.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::UnaryModificationOperator)


def test_c::sharp::operators::unarymodificationoperator_constructor_exists():
    assert callable(c::sharp::operators::UnaryModificationOperator.__init__)


def test_c::sharp::operators::unarymodificationoperator_constructor_args():
    sig = inspect.signature(c::sharp::operators::UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::relationoperator_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::RelationOperator)


def test_c::sharp::operators::relationoperator_constructor_exists():
    assert callable(c::sharp::operators::RelationOperator.__init__)


def test_c::sharp::operators::relationoperator_constructor_args():
    sig = inspect.signature(c::sharp::operators::RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::MultiplicativeOperator)


def test_c::sharp::operators::multiplicativeoperator_constructor_exists():
    assert callable(c::sharp::operators::MultiplicativeOperator.__init__)


def test_c::sharp::operators::multiplicativeoperator_constructor_args():
    sig = inspect.signature(c::sharp::operators::MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::equalityoperator_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::EqualityOperator)


def test_c::sharp::operators::equalityoperator_constructor_exists():
    assert callable(c::sharp::operators::EqualityOperator.__init__)


def test_c::sharp::operators::equalityoperator_constructor_args():
    sig = inspect.signature(c::sharp::operators::EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::UnaryOperator)


def test_c::sharp::operators::unaryoperator_constructor_exists():
    assert callable(c::sharp::operators::UnaryOperator.__init__)


def test_c::sharp::operators::unaryoperator_constructor_args():
    sig = inspect.signature(c::sharp::operators::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::shiftoperator_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::ShiftOperator)


def test_c::sharp::operators::shiftoperator_constructor_exists():
    assert callable(c::sharp::operators::ShiftOperator.__init__)


def test_c::sharp::operators::shiftoperator_constructor_args():
    sig = inspect.signature(c::sharp::operators::ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::AssignmentOperator)


def test_c::sharp::operators::assignmentoperator_constructor_exists():
    assert callable(c::sharp::operators::AssignmentOperator.__init__)


def test_c::sharp::operators::assignmentoperator_constructor_args():
    sig = inspect.signature(c::sharp::operators::AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::additiveoperator_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::AdditiveOperator)


def test_c::sharp::operators::additiveoperator_constructor_exists():
    assert callable(c::sharp::operators::AdditiveOperator.__init__)


def test_c::sharp::operators::additiveoperator_constructor_args():
    sig = inspect.signature(c::sharp::operators::AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::operator_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::Operator)


def test_c::sharp::operators::operator_constructor_exists():
    assert callable(c::sharp::operators::Operator.__init__)


def test_c::sharp::operators::operator_constructor_args():
    sig = inspect.signature(c::sharp::operators::Operator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::keywords::event_is_not_abstract():
    assert not inspect.isabstract(c::sharp::keywords::Event)


def test_c::sharp::keywords::event_constructor_exists():
    assert callable(c::sharp::keywords::Event.__init__)


def test_c::sharp::keywords::event_constructor_args():
    sig = inspect.signature(c::sharp::keywords::Event.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::keywords::return_is_not_abstract():
    assert not inspect.isabstract(c::sharp::keywords::Return)


def test_c::sharp::keywords::return_constructor_exists():
    assert callable(c::sharp::keywords::Return.__init__)


def test_c::sharp::keywords::return_constructor_args():
    sig = inspect.signature(c::sharp::keywords::Return.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::keywords::default_is_not_abstract():
    assert not inspect.isabstract(c::sharp::keywords::Default)


def test_c::sharp::keywords::default_constructor_exists():
    assert callable(c::sharp::keywords::Default.__init__)


def test_c::sharp::keywords::default_constructor_args():
    sig = inspect.signature(c::sharp::keywords::Default.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::keywords::case_is_not_abstract():
    assert not inspect.isabstract(c::sharp::keywords::Case)


def test_c::sharp::keywords::case_constructor_exists():
    assert callable(c::sharp::keywords::Case.__init__)


def test_c::sharp::keywords::case_constructor_args():
    sig = inspect.signature(c::sharp::keywords::Case.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::keywords::params_is_not_abstract():
    assert not inspect.isabstract(c::sharp::keywords::Params)


def test_c::sharp::keywords::params_constructor_exists():
    assert callable(c::sharp::keywords::Params.__init__)


def test_c::sharp::keywords::params_constructor_args():
    sig = inspect.signature(c::sharp::keywords::Params.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::keywords::ref_is_not_abstract():
    assert not inspect.isabstract(c::sharp::keywords::Ref)


def test_c::sharp::keywords::ref_constructor_exists():
    assert callable(c::sharp::keywords::Ref.__init__)


def test_c::sharp::keywords::ref_constructor_args():
    sig = inspect.signature(c::sharp::keywords::Ref.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::keywords::out_is_not_abstract():
    assert not inspect.isabstract(c::sharp::keywords::Out)


def test_c::sharp::keywords::out_constructor_exists():
    assert callable(c::sharp::keywords::Out.__init__)


def test_c::sharp::keywords::out_constructor_args():
    sig = inspect.signature(c::sharp::keywords::Out.__init__)
    params = list(sig.parameters.keys())



def test_shiftoperator_is_not_abstract():
    assert not inspect.isabstract(ShiftOperator)


def test_shiftoperator_constructor_exists():
    assert callable(ShiftOperator.__init__)


def test_shiftoperator_constructor_args():
    sig = inspect.signature(ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::unsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::UnsignedRightShift)


def test_c::sharp::operators::unsignedrightshift_constructor_exists():
    assert callable(c::sharp::operators::UnsignedRightShift.__init__)


def test_c::sharp::operators::unsignedrightshift_constructor_args():
    sig = inspect.signature(c::sharp::operators::UnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::rightshift_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::RightShift)


def test_c::sharp::operators::rightshift_constructor_exists():
    assert callable(c::sharp::operators::RightShift.__init__)


def test_c::sharp::operators::rightshift_constructor_args():
    sig = inspect.signature(c::sharp::operators::RightShift.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::leftshift_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::LeftShift)


def test_c::sharp::operators::leftshift_constructor_exists():
    assert callable(c::sharp::operators::LeftShift.__init__)


def test_c::sharp::operators::leftshift_constructor_args():
    sig = inspect.signature(c::sharp::operators::LeftShift.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::negate_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::Negate)


def test_c::sharp::operators::negate_constructor_exists():
    assert callable(c::sharp::operators::Negate.__init__)


def test_c::sharp::operators::negate_constructor_args():
    sig = inspect.signature(c::sharp::operators::Negate.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationOperator)


def test_unarymodificationoperator_constructor_exists():
    assert callable(UnaryModificationOperator.__init__)


def test_unarymodificationoperator_constructor_args():
    sig = inspect.signature(UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::plusplus_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::PlusPlus)


def test_c::sharp::operators::plusplus_constructor_exists():
    assert callable(c::sharp::operators::PlusPlus.__init__)


def test_c::sharp::operators::plusplus_constructor_args():
    sig = inspect.signature(c::sharp::operators::PlusPlus.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::minusminus_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::MinusMinus)


def test_c::sharp::operators::minusminus_constructor_exists():
    assert callable(c::sharp::operators::MinusMinus.__init__)


def test_c::sharp::operators::minusminus_constructor_args():
    sig = inspect.signature(c::sharp::operators::MinusMinus.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::literals::realliteral_is_not_abstract():
    assert not inspect.isabstract(c::sharp::literals::RealLiteral)


def test_c::sharp::literals::realliteral_constructor_exists():
    assert callable(c::sharp::literals::RealLiteral.__init__)


def test_c::sharp::literals::realliteral_constructor_args():
    sig = inspect.signature(c::sharp::literals::RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c::sharp::literals::realliteral_has_value():
    assert hasattr(c::sharp::literals::RealLiteral, "value")
    descriptor = None
    for klass in c::sharp::literals::RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c::sharp::literals::decimalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(c::sharp::literals::DecimalIntegerLiteral)


def test_c::sharp::literals::decimalintegerliteral_constructor_exists():
    assert callable(c::sharp::literals::DecimalIntegerLiteral.__init__)


def test_c::sharp::literals::decimalintegerliteral_constructor_args():
    sig = inspect.signature(c::sharp::literals::DecimalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c::sharp::literals::decimalintegerliteral_has_value():
    assert hasattr(c::sharp::literals::DecimalIntegerLiteral, "value")
    descriptor = None
    for klass in c::sharp::literals::DecimalIntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c::sharp::literals::hexadecimalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(c::sharp::literals::HexadecimalIntegerLiteral)


def test_c::sharp::literals::hexadecimalintegerliteral_constructor_exists():
    assert callable(c::sharp::literals::HexadecimalIntegerLiteral.__init__)


def test_c::sharp::literals::hexadecimalintegerliteral_constructor_args():
    sig = inspect.signature(c::sharp::literals::HexadecimalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c::sharp::literals::hexadecimalintegerliteral_has_value():
    assert hasattr(c::sharp::literals::HexadecimalIntegerLiteral, "value")
    descriptor = None
    for klass in c::sharp::literals::HexadecimalIntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c::sharp::literals::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(c::sharp::literals::BooleanLiteral)


def test_c::sharp::literals::booleanliteral_constructor_exists():
    assert callable(c::sharp::literals::BooleanLiteral.__init__)


def test_c::sharp::literals::booleanliteral_constructor_args():
    sig = inspect.signature(c::sharp::literals::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c::sharp::literals::booleanliteral_has_value():
    assert hasattr(c::sharp::literals::BooleanLiteral, "value")
    descriptor = None
    for klass in c::sharp::literals::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c::sharp::modifiers::modifier_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::Modifier)


def test_c::sharp::modifiers::modifier_constructor_exists():
    assert callable(c::sharp::modifiers::Modifier.__init__)


def test_c::sharp::modifiers::modifier_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::Modifier.__init__)
    params = list(sig.parameters.keys())



def test_referencetype_is_not_abstract():
    assert not inspect.isabstract(ReferenceType)


def test_referencetype_constructor_exists():
    assert callable(ReferenceType.__init__)


def test_referencetype_constructor_args():
    sig = inspect.signature(ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::classorinterfaceordelegateorenumtype_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::ClassOrInterfaceOrDelegateOrEnumType)


def test_c::sharp::types::classorinterfaceordelegateorenumtype_constructor_exists():
    assert callable(c::sharp::types::ClassOrInterfaceOrDelegateOrEnumType.__init__)


def test_c::sharp::types::classorinterfaceordelegateorenumtype_constructor_args():
    sig = inspect.signature(c::sharp::types::ClassOrInterfaceOrDelegateOrEnumType.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::literals::stringliteral_is_not_abstract():
    assert not inspect.isabstract(c::sharp::literals::StringLiteral)


def test_c::sharp::literals::stringliteral_constructor_exists():
    assert callable(c::sharp::literals::StringLiteral.__init__)


def test_c::sharp::literals::stringliteral_constructor_args():
    sig = inspect.signature(c::sharp::literals::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c::sharp::literals::stringliteral_has_value():
    assert hasattr(c::sharp::literals::StringLiteral, "value")
    descriptor = None
    for klass in c::sharp::literals::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c::sharp::literals::characterliteral_is_not_abstract():
    assert not inspect.isabstract(c::sharp::literals::CharacterLiteral)


def test_c::sharp::literals::characterliteral_constructor_exists():
    assert callable(c::sharp::literals::CharacterLiteral.__init__)


def test_c::sharp::literals::characterliteral_constructor_args():
    sig = inspect.signature(c::sharp::literals::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c::sharp::literals::characterliteral_has_value():
    assert hasattr(c::sharp::literals::CharacterLiteral, "value")
    descriptor = None
    for klass in c::sharp::literals::CharacterLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c::sharp::literals::this_is_not_abstract():
    assert not inspect.isabstract(c::sharp::literals::This)


def test_c::sharp::literals::this_constructor_exists():
    assert callable(c::sharp::literals::This.__init__)


def test_c::sharp::literals::this_constructor_args():
    sig = inspect.signature(c::sharp::literals::This.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::literals::nullliteral_is_not_abstract():
    assert not inspect.isabstract(c::sharp::literals::NullLiteral)


def test_c::sharp::literals::nullliteral_constructor_exists():
    assert callable(c::sharp::literals::NullLiteral.__init__)


def test_c::sharp::literals::nullliteral_constructor_args():
    sig = inspect.signature(c::sharp::literals::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_types::type_is_not_abstract():
    assert not inspect.isabstract(types::Type)


def test_types::type_constructor_exists():
    assert callable(types::Type.__init__)


def test_types::type_constructor_args():
    sig = inspect.signature(types::Type.__init__)
    params = list(sig.parameters.keys())



def test_types::nonarraytype_is_not_abstract():
    assert not inspect.isabstract(types::NonArrayType)


def test_types::nonarraytype_constructor_exists():
    assert callable(types::NonArrayType.__init__)


def test_types::nonarraytype_constructor_args():
    sig = inspect.signature(types::NonArrayType.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::simpletype_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::SimpleType)


def test_c::sharp::types::simpletype_constructor_exists():
    assert callable(c::sharp::types::SimpleType.__init__)


def test_c::sharp::types::simpletype_constructor_args():
    sig = inspect.signature(c::sharp::types::SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::pointertype_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::PointerType)


def test_c::sharp::types::pointertype_constructor_exists():
    assert callable(c::sharp::types::PointerType.__init__)


def test_c::sharp::types::pointertype_constructor_args():
    sig = inspect.signature(c::sharp::types::PointerType.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::referencetype_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::ReferenceType)


def test_c::sharp::types::referencetype_constructor_exists():
    assert callable(c::sharp::types::ReferenceType.__init__)


def test_c::sharp::types::referencetype_constructor_args():
    sig = inspect.signature(c::sharp::types::ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::nonarraytype_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::NonArrayType)


def test_c::sharp::types::nonarraytype_constructor_exists():
    assert callable(c::sharp::types::NonArrayType.__init__)


def test_c::sharp::types::nonarraytype_constructor_args():
    sig = inspect.signature(c::sharp::types::NonArrayType.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::type_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::Type)


def test_c::sharp::types::type_constructor_exists():
    assert callable(c::sharp::types::Type.__init__)


def test_c::sharp::types::type_constructor_args():
    sig = inspect.signature(c::sharp::types::Type.__init__)
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



def test_c::sharp::expressions::conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::ConditionalOrExpression)


def test_c::sharp::expressions::conditionalorexpression_constructor_exists():
    assert callable(c::sharp::expressions::ConditionalOrExpression.__init__)


def test_c::sharp::expressions::conditionalorexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionaland_is_not_abstract():
    assert not inspect.isabstract(ConditionalAnd)


def test_conditionaland_constructor_exists():
    assert callable(ConditionalAnd.__init__)


def test_conditionaland_constructor_args():
    sig = inspect.signature(ConditionalAnd.__init__)
    params = list(sig.parameters.keys())



def test_inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(InclusiveOrExpression)


def test_inclusiveorexpression_constructor_exists():
    assert callable(InclusiveOrExpression.__init__)


def test_inclusiveorexpression_constructor_args():
    sig = inspect.signature(InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::ConditionalAndExpression)


def test_c::sharp::expressions::conditionalandexpression_constructor_exists():
    assert callable(c::sharp::expressions::ConditionalAndExpression.__init__)


def test_c::sharp::expressions::conditionalandexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::ConditionalAndExpression.__init__)
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



def test_c::sharp::expressions::inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::InclusiveOrExpression)


def test_c::sharp::expressions::inclusiveorexpression_constructor_exists():
    assert callable(c::sharp::expressions::InclusiveOrExpression.__init__)


def test_c::sharp::expressions::inclusiveorexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::InclusiveOrExpression.__init__)
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



def test_c::sharp::expressions::exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::ExclusiveOrExpression)


def test_c::sharp::expressions::exclusiveorexpression_constructor_exists():
    assert callable(c::sharp::expressions::ExclusiveOrExpression.__init__)


def test_c::sharp::expressions::exclusiveorexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::ExclusiveOrExpression.__init__)
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



def test_c::sharp::expressions::andexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::AndExpression)


def test_c::sharp::expressions::andexpression_constructor_exists():
    assert callable(c::sharp::expressions::AndExpression.__init__)


def test_c::sharp::expressions::andexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::AndExpression.__init__)
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



def test_c::sharp::expressions::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::RelationalExpression)


def test_c::sharp::expressions::relationalexpression_constructor_exists():
    assert callable(c::sharp::expressions::RelationalExpression.__init__)


def test_c::sharp::expressions::relationalexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::RelationalExpression.__init__)
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



def test_c::sharp::expressions::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::ShiftExpression)


def test_c::sharp::expressions::shiftexpression_constructor_exists():
    assert callable(c::sharp::expressions::ShiftExpression.__init__)


def test_c::sharp::expressions::shiftexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeExpression)


def test_multiplicativeexpression_constructor_exists():
    assert callable(MultiplicativeExpression.__init__)


def test_multiplicativeexpression_constructor_args():
    sig = inspect.signature(MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::AdditiveExpression)


def test_c::sharp::expressions::additiveexpression_constructor_exists():
    assert callable(c::sharp::expressions::AdditiveExpression.__init__)


def test_c::sharp::expressions::additiveexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::AdditiveExpression.__init__)
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



def test_c::sharp::expressions::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::MultiplicativeExpression)


def test_c::sharp::expressions::multiplicativeexpression_constructor_exists():
    assert callable(c::sharp::expressions::MultiplicativeExpression.__init__)


def test_c::sharp::expressions::multiplicativeexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::addressofexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::AddressOfExpression)


def test_c::sharp::expressions::addressofexpression_constructor_exists():
    assert callable(c::sharp::expressions::AddressOfExpression.__init__)


def test_c::sharp::expressions::addressofexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::AddressOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(RelationalExpression)


def test_relationalexpression_constructor_exists():
    assert callable(RelationalExpression.__init__)


def test_relationalexpression_constructor_args():
    sig = inspect.signature(RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::EqualityExpression)


def test_c::sharp::expressions::equalityexpression_constructor_exists():
    assert callable(c::sharp::expressions::EqualityExpression.__init__)


def test_c::sharp::expressions::equalityexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::EqualityExpression.__init__)
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



def test_c::sharp::classes::fixedparameter_is_not_abstract():
    assert not inspect.isabstract(c::sharp::classes::FixedParameter)


def test_c::sharp::classes::fixedparameter_constructor_exists():
    assert callable(c::sharp::classes::FixedParameter.__init__)


def test_c::sharp::classes::fixedparameter_constructor_args():
    sig = inspect.signature(c::sharp::classes::FixedParameter.__init__)
    params = list(sig.parameters.keys())



def test_parameterarray_is_not_abstract():
    assert not inspect.isabstract(ParameterArray)


def test_parameterarray_constructor_exists():
    assert callable(ParameterArray.__init__)


def test_parameterarray_constructor_args():
    sig = inspect.signature(ParameterArray.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(VariableInitializer)


def test_variableinitializer_constructor_exists():
    assert callable(VariableInitializer.__init__)


def test_variableinitializer_constructor_args():
    sig = inspect.signature(VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::arrays::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(c::sharp::arrays::ArrayInitializer)


def test_c::sharp::arrays::arrayinitializer_constructor_exists():
    assert callable(c::sharp::arrays::ArrayInitializer.__init__)


def test_c::sharp::arrays::arrayinitializer_constructor_args():
    sig = inspect.signature(c::sharp::arrays::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::arrays::stackallocinitializer_is_not_abstract():
    assert not inspect.isabstract(c::sharp::arrays::StackallocInitializer)


def test_c::sharp::arrays::stackallocinitializer_constructor_exists():
    assert callable(c::sharp::arrays::StackallocInitializer.__init__)


def test_c::sharp::arrays::stackallocinitializer_constructor_args():
    sig = inspect.signature(c::sharp::arrays::StackallocInitializer.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarator_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarator)


def test_variabledeclarator_constructor_exists():
    assert callable(VariableDeclarator.__init__)


def test_variabledeclarator_constructor_args():
    sig = inspect.signature(VariableDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_constantdeclarator_is_not_abstract():
    assert not inspect.isabstract(ConstantDeclarator)


def test_constantdeclarator_constructor_exists():
    assert callable(ConstantDeclarator.__init__)


def test_constantdeclarator_constructor_args():
    sig = inspect.signature(ConstantDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::classes::variableinitializer_is_not_abstract():
    assert not inspect.isabstract(c::sharp::classes::VariableInitializer)


def test_c::sharp::classes::variableinitializer_constructor_exists():
    assert callable(c::sharp::classes::VariableInitializer.__init__)


def test_c::sharp::classes::variableinitializer_constructor_args():
    sig = inspect.signature(c::sharp::classes::VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::classes::block_is_not_abstract():
    assert not inspect.isabstract(c::sharp::classes::Block)


def test_c::sharp::classes::block_constructor_exists():
    assert callable(c::sharp::classes::Block.__init__)


def test_c::sharp::classes::block_constructor_args():
    sig = inspect.signature(c::sharp::classes::Block.__init__)
    params = list(sig.parameters.keys())



def test_classes::classmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(classes::ClassMemberDeclaration)


def test_classes::classmemberdeclaration_constructor_exists():
    assert callable(classes::ClassMemberDeclaration.__init__)


def test_classes::classmemberdeclaration_constructor_args():
    sig = inspect.signature(classes::ClassMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_namespaces::namespacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(namespaces::NamespaceMemberDeclaration)


def test_namespaces::namespacememberdeclaration_constructor_exists():
    assert callable(namespaces::NamespaceMemberDeclaration.__init__)


def test_namespaces::namespacememberdeclaration_constructor_args():
    sig = inspect.signature(namespaces::NamespaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::namespaces::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(c::sharp::namespaces::TypeDeclaration)


def test_c::sharp::namespaces::typedeclaration_constructor_exists():
    assert callable(c::sharp::namespaces::TypeDeclaration.__init__)


def test_c::sharp::namespaces::typedeclaration_constructor_args():
    sig = inspect.signature(c::sharp::namespaces::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::namespaces::namespacebody_is_not_abstract():
    assert not inspect.isabstract(c::sharp::namespaces::NamespaceBody)


def test_c::sharp::namespaces::namespacebody_constructor_exists():
    assert callable(c::sharp::namespaces::NamespaceBody.__init__)


def test_c::sharp::namespaces::namespacebody_constructor_args():
    sig = inspect.signature(c::sharp::namespaces::NamespaceBody.__init__)
    params = list(sig.parameters.keys())



def test_namespacebody_is_not_abstract():
    assert not inspect.isabstract(NamespaceBody)


def test_namespacebody_constructor_exists():
    assert callable(NamespaceBody.__init__)


def test_namespacebody_constructor_args():
    sig = inspect.signature(NamespaceBody.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::namespaces::namespacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(c::sharp::namespaces::NamespaceMemberDeclaration)


def test_c::sharp::namespaces::namespacememberdeclaration_constructor_exists():
    assert callable(c::sharp::namespaces::NamespaceMemberDeclaration.__init__)


def test_c::sharp::namespaces::namespacememberdeclaration_constructor_args():
    sig = inspect.signature(c::sharp::namespaces::NamespaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_namespaceortypename_is_not_abstract():
    assert not inspect.isabstract(NamespaceOrTypeName)


def test_namespaceortypename_constructor_exists():
    assert callable(NamespaceOrTypeName.__init__)


def test_namespaceortypename_constructor_args():
    sig = inspect.signature(NamespaceOrTypeName.__init__)
    params = list(sig.parameters.keys())



def test_fixedparameter_is_not_abstract():
    assert not inspect.isabstract(FixedParameter)


def test_fixedparameter_constructor_exists():
    assert callable(FixedParameter.__init__)


def test_fixedparameter_constructor_args():
    sig = inspect.signature(FixedParameter.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::classes::formalparameterlist_is_not_abstract():
    assert not inspect.isabstract(c::sharp::classes::FormalParameterList)


def test_c::sharp::classes::formalparameterlist_constructor_exists():
    assert callable(c::sharp::classes::FormalParameterList.__init__)


def test_c::sharp::classes::formalparameterlist_constructor_args():
    sig = inspect.signature(c::sharp::classes::FormalParameterList.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
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



def test_c::sharp::classes::classmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(c::sharp::classes::ClassMemberDeclaration)


def test_c::sharp::classes::classmemberdeclaration_constructor_exists():
    assert callable(c::sharp::classes::ClassMemberDeclaration.__init__)


def test_c::sharp::classes::classmemberdeclaration_constructor_args():
    sig = inspect.signature(c::sharp::classes::ClassMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_classorinterfaceordelegateorenumtype_is_not_abstract():
    assert not inspect.isabstract(ClassOrInterfaceOrDelegateOrEnumType)


def test_classorinterfaceordelegateorenumtype_constructor_exists():
    assert callable(ClassOrInterfaceOrDelegateOrEnumType.__init__)


def test_classorinterfaceordelegateorenumtype_constructor_args():
    sig = inspect.signature(ClassOrInterfaceOrDelegateOrEnumType.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::classes::classbase_is_not_abstract():
    assert not inspect.isabstract(c::sharp::classes::ClassBase)


def test_c::sharp::classes::classbase_constructor_exists():
    assert callable(c::sharp::classes::ClassBase.__init__)


def test_c::sharp::classes::classbase_constructor_args():
    sig = inspect.signature(c::sharp::classes::ClassBase.__init__)
    params = list(sig.parameters.keys())



def test_classmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(ClassMemberDeclaration)


def test_classmemberdeclaration_constructor_exists():
    assert callable(ClassMemberDeclaration.__init__)


def test_classmemberdeclaration_constructor_args():
    sig = inspect.signature(ClassMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::classes::constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(c::sharp::classes::ConstantDeclaration)


def test_c::sharp::classes::constantdeclaration_constructor_exists():
    assert callable(c::sharp::classes::ConstantDeclaration.__init__)


def test_c::sharp::classes::constantdeclaration_constructor_args():
    sig = inspect.signature(c::sharp::classes::ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::classes::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(c::sharp::classes::FieldDeclaration)


def test_c::sharp::classes::fielddeclaration_constructor_exists():
    assert callable(c::sharp::classes::FieldDeclaration.__init__)


def test_c::sharp::classes::fielddeclaration_constructor_args():
    sig = inspect.signature(c::sharp::classes::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



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



def test_c::sharp::modifiers::readonly_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::ReadOnly)


def test_c::sharp::modifiers::readonly_constructor_exists():
    assert callable(c::sharp::modifiers::ReadOnly.__init__)


def test_c::sharp::modifiers::readonly_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::ReadOnly.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::partial_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::Partial)


def test_c::sharp::modifiers::partial_constructor_exists():
    assert callable(c::sharp::modifiers::Partial.__init__)


def test_c::sharp::modifiers::partial_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::Partial.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::protected_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::Protected)


def test_c::sharp::modifiers::protected_constructor_exists():
    assert callable(c::sharp::modifiers::Protected.__init__)


def test_c::sharp::modifiers::protected_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::Protected.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::unsafe_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::Unsafe)


def test_c::sharp::modifiers::unsafe_constructor_exists():
    assert callable(c::sharp::modifiers::Unsafe.__init__)


def test_c::sharp::modifiers::unsafe_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::Unsafe.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::sealed_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::Sealed)


def test_c::sharp::modifiers::sealed_constructor_exists():
    assert callable(c::sharp::modifiers::Sealed.__init__)


def test_c::sharp::modifiers::sealed_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::Sealed.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::abstract_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::Abstract)


def test_c::sharp::modifiers::abstract_constructor_exists():
    assert callable(c::sharp::modifiers::Abstract.__init__)


def test_c::sharp::modifiers::abstract_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::Abstract.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::static_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::Static)


def test_c::sharp::modifiers::static_constructor_exists():
    assert callable(c::sharp::modifiers::Static.__init__)


def test_c::sharp::modifiers::static_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::Static.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::private_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::Private)


def test_c::sharp::modifiers::private_constructor_exists():
    assert callable(c::sharp::modifiers::Private.__init__)


def test_c::sharp::modifiers::private_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::Private.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::internal_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::Internal)


def test_c::sharp::modifiers::internal_constructor_exists():
    assert callable(c::sharp::modifiers::Internal.__init__)


def test_c::sharp::modifiers::internal_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::Internal.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::volatile_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::Volatile)


def test_c::sharp::modifiers::volatile_constructor_exists():
    assert callable(c::sharp::modifiers::Volatile.__init__)


def test_c::sharp::modifiers::volatile_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::Volatile.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::public_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::Public)


def test_c::sharp::modifiers::public_constructor_exists():
    assert callable(c::sharp::modifiers::Public.__init__)


def test_c::sharp::modifiers::public_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::Public.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::overridemodifier_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::OverrideModifier)


def test_c::sharp::modifiers::overridemodifier_constructor_exists():
    assert callable(c::sharp::modifiers::OverrideModifier.__init__)


def test_c::sharp::modifiers::overridemodifier_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::OverrideModifier.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::new_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::New)


def test_c::sharp::modifiers::new_constructor_exists():
    assert callable(c::sharp::modifiers::New.__init__)


def test_c::sharp::modifiers::new_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::New.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::extern_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::Extern)


def test_c::sharp::modifiers::extern_constructor_exists():
    assert callable(c::sharp::modifiers::Extern.__init__)


def test_c::sharp::modifiers::extern_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::Extern.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::modifiers::virtual_is_not_abstract():
    assert not inspect.isabstract(c::sharp::modifiers::Virtual)


def test_c::sharp::modifiers::virtual_constructor_exists():
    assert callable(c::sharp::modifiers::Virtual.__init__)


def test_c::sharp::modifiers::virtual_constructor_args():
    sig = inspect.signature(c::sharp::modifiers::Virtual.__init__)
    params = list(sig.parameters.keys())



def test_attributes_is_not_abstract():
    assert not inspect.isabstract(Attributes)


def test_attributes_constructor_exists():
    assert callable(Attributes.__init__)


def test_attributes_constructor_args():
    sig = inspect.signature(Attributes.__init__)
    params = list(sig.parameters.keys())



def test_namespaces::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(namespaces::TypeDeclaration)


def test_namespaces::typedeclaration_constructor_exists():
    assert callable(namespaces::TypeDeclaration.__init__)


def test_namespaces::typedeclaration_constructor_args():
    sig = inspect.signature(namespaces::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::namespaces::usingdirective_is_not_abstract():
    assert not inspect.isabstract(c::sharp::namespaces::UsingDirective)


def test_c::sharp::namespaces::usingdirective_constructor_exists():
    assert callable(c::sharp::namespaces::UsingDirective.__init__)


def test_c::sharp::namespaces::usingdirective_constructor_args():
    sig = inspect.signature(c::sharp::namespaces::UsingDirective.__init__)
    params = list(sig.parameters.keys())



def test_namespacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(NamespaceMemberDeclaration)


def test_namespacememberdeclaration_constructor_exists():
    assert callable(NamespaceMemberDeclaration.__init__)


def test_namespacememberdeclaration_constructor_args():
    sig = inspect.signature(NamespaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::namespaces::namespace_is_not_abstract():
    assert not inspect.isabstract(c::sharp::namespaces::Namespace)


def test_c::sharp::namespaces::namespace_constructor_exists():
    assert callable(c::sharp::namespaces::Namespace.__init__)


def test_c::sharp::namespaces::namespace_constructor_args():
    sig = inspect.signature(c::sharp::namespaces::Namespace.__init__)
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



def test_c::sharp::namespaces::compilationunit_is_not_abstract():
    assert not inspect.isabstract(c::sharp::namespaces::CompilationUnit)


def test_c::sharp::namespaces::compilationunit_constructor_exists():
    assert callable(c::sharp::namespaces::CompilationUnit.__init__)


def test_c::sharp::namespaces::compilationunit_constructor_args():
    sig = inspect.signature(c::sharp::namespaces::CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_expressions::primarynoarraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::PrimaryNoArrayCreationExpression)


def test_expressions::primarynoarraycreationexpression_constructor_exists():
    assert callable(expressions::PrimaryNoArrayCreationExpression.__init__)


def test_expressions::primarynoarraycreationexpression_constructor_args():
    sig = inspect.signature(expressions::PrimaryNoArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_common::namedelement_is_not_abstract():
    assert not inspect.isabstract(common::NamedElement)


def test_common::namedelement_constructor_exists():
    assert callable(common::NamedElement.__init__)


def test_common::namedelement_constructor_args():
    sig = inspect.signature(common::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::classes::method_is_not_abstract():
    assert not inspect.isabstract(c::sharp::classes::Method)


def test_c::sharp::classes::method_constructor_exists():
    assert callable(c::sharp::classes::Method.__init__)


def test_c::sharp::classes::method_constructor_args():
    sig = inspect.signature(c::sharp::classes::Method.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::classes::class_is_not_abstract():
    assert not inspect.isabstract(c::sharp::classes::Class)


def test_c::sharp::classes::class_constructor_exists():
    assert callable(c::sharp::classes::Class.__init__)


def test_c::sharp::classes::class_constructor_args():
    sig = inspect.signature(c::sharp::classes::Class.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::common::identifier_is_not_abstract():
    assert not inspect.isabstract(c::sharp::common::Identifier)


def test_c::sharp::common::identifier_constructor_exists():
    assert callable(c::sharp::common::Identifier.__init__)


def test_c::sharp::common::identifier_constructor_args():
    sig = inspect.signature(c::sharp::common::Identifier.__init__)
    params = list(sig.parameters.keys())



def test_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::common::namespaceortypename_is_not_abstract():
    assert not inspect.isabstract(c::sharp::common::NamespaceOrTypeName)


def test_c::sharp::common::namespaceortypename_constructor_exists():
    assert callable(c::sharp::common::NamespaceOrTypeName.__init__)


def test_c::sharp::common::namespaceortypename_constructor_args():
    sig = inspect.signature(c::sharp::common::NamespaceOrTypeName.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::common::namedelement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::common::NamedElement)


def test_c::sharp::common::namedelement_constructor_exists():
    assert callable(c::sharp::common::NamedElement.__init__)


def test_c::sharp::common::namedelement_constructor_args():
    sig = inspect.signature(c::sharp::common::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_c::sharp::common::namedelement_has_name():
    assert hasattr(c::sharp::common::NamedElement, "name")
    descriptor = None
    for klass in c::sharp::common::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(AssignmentOperator)


def test_assignmentoperator_constructor_exists():
    assert callable(AssignmentOperator.__init__)


def test_assignmentoperator_constructor_args():
    sig = inspect.signature(AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::assignmentminus_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::AssignmentMinus)


def test_c::sharp::operators::assignmentminus_constructor_exists():
    assert callable(c::sharp::operators::AssignmentMinus.__init__)


def test_c::sharp::operators::assignmentminus_constructor_args():
    sig = inspect.signature(c::sharp::operators::AssignmentMinus.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::assignmentrightshift_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::AssignmentRightShift)


def test_c::sharp::operators::assignmentrightshift_constructor_exists():
    assert callable(c::sharp::operators::AssignmentRightShift.__init__)


def test_c::sharp::operators::assignmentrightshift_constructor_args():
    sig = inspect.signature(c::sharp::operators::AssignmentRightShift.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::assignmentor_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::AssignmentOr)


def test_c::sharp::operators::assignmentor_constructor_exists():
    assert callable(c::sharp::operators::AssignmentOr.__init__)


def test_c::sharp::operators::assignmentor_constructor_args():
    sig = inspect.signature(c::sharp::operators::AssignmentOr.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::assignment_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::Assignment)


def test_c::sharp::operators::assignment_constructor_exists():
    assert callable(c::sharp::operators::Assignment.__init__)


def test_c::sharp::operators::assignment_constructor_args():
    sig = inspect.signature(c::sharp::operators::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::assignmentand_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::AssignmentAnd)


def test_c::sharp::operators::assignmentand_constructor_exists():
    assert callable(c::sharp::operators::AssignmentAnd.__init__)


def test_c::sharp::operators::assignmentand_constructor_args():
    sig = inspect.signature(c::sharp::operators::AssignmentAnd.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::assignmentmodulo_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::AssignmentModulo)


def test_c::sharp::operators::assignmentmodulo_constructor_exists():
    assert callable(c::sharp::operators::AssignmentModulo.__init__)


def test_c::sharp::operators::assignmentmodulo_constructor_args():
    sig = inspect.signature(c::sharp::operators::AssignmentModulo.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::assignmentplus_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::AssignmentPlus)


def test_c::sharp::operators::assignmentplus_constructor_exists():
    assert callable(c::sharp::operators::AssignmentPlus.__init__)


def test_c::sharp::operators::assignmentplus_constructor_args():
    sig = inspect.signature(c::sharp::operators::AssignmentPlus.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::assignmentdivision_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::AssignmentDivision)


def test_c::sharp::operators::assignmentdivision_constructor_exists():
    assert callable(c::sharp::operators::AssignmentDivision.__init__)


def test_c::sharp::operators::assignmentdivision_constructor_args():
    sig = inspect.signature(c::sharp::operators::AssignmentDivision.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::assignmentmultiplication_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::AssignmentMultiplication)


def test_c::sharp::operators::assignmentmultiplication_constructor_exists():
    assert callable(c::sharp::operators::AssignmentMultiplication.__init__)


def test_c::sharp::operators::assignmentmultiplication_constructor_args():
    sig = inspect.signature(c::sharp::operators::AssignmentMultiplication.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::assignmentleftshift_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::AssignmentLeftShift)


def test_c::sharp::operators::assignmentleftshift_constructor_exists():
    assert callable(c::sharp::operators::AssignmentLeftShift.__init__)


def test_c::sharp::operators::assignmentleftshift_constructor_args():
    sig = inspect.signature(c::sharp::operators::AssignmentLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::assignmentexclusiveor_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::AssignmentExclusiveOr)


def test_c::sharp::operators::assignmentexclusiveor_constructor_exists():
    assert callable(c::sharp::operators::AssignmentExclusiveOr.__init__)


def test_c::sharp::operators::assignmentexclusiveor_constructor_args():
    sig = inspect.signature(c::sharp::operators::AssignmentExclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::operators::assignmentunsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(c::sharp::operators::AssignmentUnsignedRightShift)


def test_c::sharp::operators::assignmentunsignedrightshift_constructor_exists():
    assert callable(c::sharp::operators::AssignmentUnsignedRightShift.__init__)


def test_c::sharp::operators::assignmentunsignedrightshift_constructor_args():
    sig = inspect.signature(c::sharp::operators::AssignmentUnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_expressions::expression_is_not_abstract():
    assert not inspect.isabstract(expressions::Expression)


def test_expressions::expression_constructor_exists():
    assert callable(expressions::Expression.__init__)


def test_expressions::expression_constructor_args():
    sig = inspect.signature(expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(ConditionalOrExpression)


def test_conditionalorexpression_constructor_exists():
    assert callable(ConditionalOrExpression.__init__)


def test_conditionalorexpression_constructor_args():
    sig = inspect.signature(ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::ConditionalExpression)


def test_c::sharp::expressions::conditionalexpression_constructor_exists():
    assert callable(c::sharp::expressions::ConditionalExpression.__init__)


def test_c::sharp::expressions::conditionalexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_addressofexpression_is_not_abstract():
    assert not inspect.isabstract(AddressOfExpression)


def test_addressofexpression_constructor_exists():
    assert callable(AddressOfExpression.__init__)


def test_addressofexpression_constructor_args():
    sig = inspect.signature(AddressOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::castexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::CastExpression)


def test_c::sharp::expressions::castexpression_constructor_exists():
    assert callable(c::sharp::expressions::CastExpression.__init__)


def test_c::sharp::expressions::castexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::CastExpression.__init__)
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



def test_c::sharp::expressions::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::UnaryExpression)


def test_c::sharp::expressions::unaryexpression_constructor_exists():
    assert callable(c::sharp::expressions::UnaryExpression.__init__)


def test_c::sharp::expressions::unaryexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(ArrayInitializer)


def test_arrayinitializer_constructor_exists():
    assert callable(ArrayInitializer.__init__)


def test_arrayinitializer_constructor_args():
    sig = inspect.signature(ArrayInitializer.__init__)
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



def test_preincrementexpression_is_not_abstract():
    assert not inspect.isabstract(PreIncrementExpression)


def test_preincrementexpression_constructor_exists():
    assert callable(PreIncrementExpression.__init__)


def test_preincrementexpression_constructor_args():
    sig = inspect.signature(PreIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_argumentlist_is_not_abstract():
    assert not inspect.isabstract(ArgumentList)


def test_argumentlist_constructor_exists():
    assert callable(ArgumentList.__init__)


def test_argumentlist_constructor_args():
    sig = inspect.signature(ArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_expressions::statementexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::StatementExpression)


def test_expressions::statementexpression_constructor_exists():
    assert callable(expressions::StatementExpression.__init__)


def test_expressions::statementexpression_constructor_args():
    sig = inspect.signature(expressions::StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::objectcreationexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::ObjectCreationExpression)


def test_c::sharp::expressions::objectcreationexpression_constructor_exists():
    assert callable(c::sharp::expressions::ObjectCreationExpression.__init__)


def test_c::sharp::expressions::objectcreationexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::ObjectCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::AssignmentExpression)


def test_c::sharp::expressions::assignmentexpression_constructor_exists():
    assert callable(c::sharp::expressions::AssignmentExpression.__init__)


def test_c::sharp::expressions::assignmentexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::primaryextendedexpressiontype_is_not_abstract():
    assert not inspect.isabstract(expressions::PrimaryExtendedExpressionType)


def test_expressions::primaryextendedexpressiontype_constructor_exists():
    assert callable(expressions::PrimaryExtendedExpressionType.__init__)


def test_expressions::primaryextendedexpressiontype_constructor_args():
    sig = inspect.signature(expressions::PrimaryExtendedExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::postdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::PostDecrementExpression)


def test_c::sharp::expressions::postdecrementexpression_constructor_exists():
    assert callable(c::sharp::expressions::PostDecrementExpression.__init__)


def test_c::sharp::expressions::postdecrementexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::PostDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::postincrementexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::PostIncrementExpression)


def test_c::sharp::expressions::postincrementexpression_constructor_exists():
    assert callable(c::sharp::expressions::PostIncrementExpression.__init__)


def test_c::sharp::expressions::postincrementexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::PostIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::invocationexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::InvocationExpression)


def test_c::sharp::expressions::invocationexpression_constructor_exists():
    assert callable(c::sharp::expressions::InvocationExpression.__init__)


def test_c::sharp::expressions::invocationexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::InvocationExpression.__init__)
    params = list(sig.parameters.keys())



def test_simpletype_is_not_abstract():
    assert not inspect.isabstract(SimpleType)


def test_simpletype_constructor_exists():
    assert callable(SimpleType.__init__)


def test_simpletype_constructor_args():
    sig = inspect.signature(SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::object_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::Object)


def test_c::sharp::types::object_constructor_exists():
    assert callable(c::sharp::types::Object.__init__)


def test_c::sharp::types::object_constructor_args():
    sig = inspect.signature(c::sharp::types::Object.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::short_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::Short)


def test_c::sharp::types::short_constructor_exists():
    assert callable(c::sharp::types::Short.__init__)


def test_c::sharp::types::short_constructor_args():
    sig = inspect.signature(c::sharp::types::Short.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::char_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::Char)


def test_c::sharp::types::char_constructor_exists():
    assert callable(c::sharp::types::Char.__init__)


def test_c::sharp::types::char_constructor_args():
    sig = inspect.signature(c::sharp::types::Char.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::uint_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::UInt)


def test_c::sharp::types::uint_constructor_exists():
    assert callable(c::sharp::types::UInt.__init__)


def test_c::sharp::types::uint_constructor_args():
    sig = inspect.signature(c::sharp::types::UInt.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::int_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::Int)


def test_c::sharp::types::int_constructor_exists():
    assert callable(c::sharp::types::Int.__init__)


def test_c::sharp::types::int_constructor_args():
    sig = inspect.signature(c::sharp::types::Int.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::byte_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::Byte)


def test_c::sharp::types::byte_constructor_exists():
    assert callable(c::sharp::types::Byte.__init__)


def test_c::sharp::types::byte_constructor_args():
    sig = inspect.signature(c::sharp::types::Byte.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::sbyte_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::SByte)


def test_c::sharp::types::sbyte_constructor_exists():
    assert callable(c::sharp::types::SByte.__init__)


def test_c::sharp::types::sbyte_constructor_args():
    sig = inspect.signature(c::sharp::types::SByte.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::ulong_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::ULong)


def test_c::sharp::types::ulong_constructor_exists():
    assert callable(c::sharp::types::ULong.__init__)


def test_c::sharp::types::ulong_constructor_args():
    sig = inspect.signature(c::sharp::types::ULong.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::long_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::Long)


def test_c::sharp::types::long_constructor_exists():
    assert callable(c::sharp::types::Long.__init__)


def test_c::sharp::types::long_constructor_args():
    sig = inspect.signature(c::sharp::types::Long.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::double_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::Double)


def test_c::sharp::types::double_constructor_exists():
    assert callable(c::sharp::types::Double.__init__)


def test_c::sharp::types::double_constructor_args():
    sig = inspect.signature(c::sharp::types::Double.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::decimal_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::Decimal)


def test_c::sharp::types::decimal_constructor_exists():
    assert callable(c::sharp::types::Decimal.__init__)


def test_c::sharp::types::decimal_constructor_args():
    sig = inspect.signature(c::sharp::types::Decimal.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::bool_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::Bool)


def test_c::sharp::types::bool_constructor_exists():
    assert callable(c::sharp::types::Bool.__init__)


def test_c::sharp::types::bool_constructor_args():
    sig = inspect.signature(c::sharp::types::Bool.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::ushort_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::UShort)


def test_c::sharp::types::ushort_constructor_exists():
    assert callable(c::sharp::types::UShort.__init__)


def test_c::sharp::types::ushort_constructor_args():
    sig = inspect.signature(c::sharp::types::UShort.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::float_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::Float)


def test_c::sharp::types::float_constructor_exists():
    assert callable(c::sharp::types::Float.__init__)


def test_c::sharp::types::float_constructor_args():
    sig = inspect.signature(c::sharp::types::Float.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::void_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::Void)


def test_c::sharp::types::void_constructor_exists():
    assert callable(c::sharp::types::Void.__init__)


def test_c::sharp::types::void_constructor_args():
    sig = inspect.signature(c::sharp::types::Void.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::types::string_is_not_abstract():
    assert not inspect.isabstract(c::sharp::types::String)


def test_c::sharp::types::string_constructor_exists():
    assert callable(c::sharp::types::String.__init__)


def test_c::sharp::types::string_constructor_args():
    sig = inspect.signature(c::sharp::types::String.__init__)
    params = list(sig.parameters.keys())



def test_primaryextendedexpressiontype_is_not_abstract():
    assert not inspect.isabstract(PrimaryExtendedExpressionType)


def test_primaryextendedexpressiontype_constructor_exists():
    assert callable(PrimaryExtendedExpressionType.__init__)


def test_primaryextendedexpressiontype_constructor_args():
    sig = inspect.signature(PrimaryExtendedExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::elementaccess_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::ElementAccess)


def test_c::sharp::expressions::elementaccess_constructor_exists():
    assert callable(c::sharp::expressions::ElementAccess.__init__)


def test_c::sharp::expressions::elementaccess_constructor_args():
    sig = inspect.signature(c::sharp::expressions::ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::pointermemberaccess_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::PointerMemberAccess)


def test_c::sharp::expressions::pointermemberaccess_constructor_exists():
    assert callable(c::sharp::expressions::PointerMemberAccess.__init__)


def test_c::sharp::expressions::pointermemberaccess_constructor_args():
    sig = inspect.signature(c::sharp::expressions::PointerMemberAccess.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::memberaccess_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::MemberAccess)


def test_c::sharp::expressions::memberaccess_constructor_exists():
    assert callable(c::sharp::expressions::MemberAccess.__init__)


def test_c::sharp::expressions::memberaccess_constructor_args():
    sig = inspect.signature(c::sharp::expressions::MemberAccess.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::primaryextendedexpressiontype_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::PrimaryExtendedExpressionType)


def test_c::sharp::expressions::primaryextendedexpressiontype_constructor_exists():
    assert callable(c::sharp::expressions::PrimaryExtendedExpressionType.__init__)


def test_c::sharp::expressions::primaryextendedexpressiontype_constructor_args():
    sig = inspect.signature(c::sharp::expressions::PrimaryExtendedExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::arraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::ArrayCreationExpression)


def test_c::sharp::expressions::arraycreationexpression_constructor_exists():
    assert callable(c::sharp::expressions::ArrayCreationExpression.__init__)


def test_c::sharp::expressions::arraycreationexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::ArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::primarynoarraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::PrimaryNoArrayCreationExpression)


def test_c::sharp::expressions::primarynoarraycreationexpression_constructor_exists():
    assert callable(c::sharp::expressions::PrimaryNoArrayCreationExpression.__init__)


def test_c::sharp::expressions::primarynoarraycreationexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::PrimaryNoArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::PrimaryExpression)


def test_c::sharp::expressions::primaryexpression_constructor_exists():
    assert callable(c::sharp::expressions::PrimaryExpression.__init__)


def test_c::sharp::expressions::primaryexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_argument_is_not_abstract():
    assert not inspect.isabstract(Argument)


def test_argument_constructor_exists():
    assert callable(Argument.__init__)


def test_argument_constructor_args():
    sig = inspect.signature(Argument.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::argumentlist_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::ArgumentList)


def test_c::sharp::expressions::argumentlist_constructor_exists():
    assert callable(c::sharp::expressions::ArgumentList.__init__)


def test_c::sharp::expressions::argumentlist_constructor_args():
    sig = inspect.signature(c::sharp::expressions::ArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::argument_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::Argument)


def test_c::sharp::expressions::argument_constructor_exists():
    assert callable(c::sharp::expressions::Argument.__init__)


def test_c::sharp::expressions::argument_constructor_args():
    sig = inspect.signature(c::sharp::expressions::Argument.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::expressionlist_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::ExpressionList)


def test_c::sharp::expressions::expressionlist_constructor_exists():
    assert callable(c::sharp::expressions::ExpressionList.__init__)


def test_c::sharp::expressions::expressionlist_constructor_args():
    sig = inspect.signature(c::sharp::expressions::ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_classes::variableinitializer_is_not_abstract():
    assert not inspect.isabstract(classes::VariableInitializer)


def test_classes::variableinitializer_constructor_exists():
    assert callable(classes::VariableInitializer.__init__)


def test_classes::variableinitializer_constructor_args():
    sig = inspect.signature(classes::VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_primarynoarraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryNoArrayCreationExpression)


def test_primarynoarraycreationexpression_constructor_exists():
    assert callable(PrimaryNoArrayCreationExpression.__init__)


def test_primarynoarraycreationexpression_constructor_args():
    sig = inspect.signature(PrimaryNoArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::checkedexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::CheckedExpression)


def test_c::sharp::expressions::checkedexpression_constructor_exists():
    assert callable(c::sharp::expressions::CheckedExpression.__init__)


def test_c::sharp::expressions::checkedexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::CheckedExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::sizeofexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::SizeOfExpression)


def test_c::sharp::expressions::sizeofexpression_constructor_exists():
    assert callable(c::sharp::expressions::SizeOfExpression.__init__)


def test_c::sharp::expressions::sizeofexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::SizeOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::uncheckedexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::UncheckedExpression)


def test_c::sharp::expressions::uncheckedexpression_constructor_exists():
    assert callable(c::sharp::expressions::UncheckedExpression.__init__)


def test_c::sharp::expressions::uncheckedexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::UncheckedExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::ParenthesizedExpression)


def test_c::sharp::expressions::parenthesizedexpression_constructor_exists():
    assert callable(c::sharp::expressions::ParenthesizedExpression.__init__)


def test_c::sharp::expressions::parenthesizedexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::delegatecreationexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::DelegateCreationExpression)


def test_c::sharp::expressions::delegatecreationexpression_constructor_exists():
    assert callable(c::sharp::expressions::DelegateCreationExpression.__init__)


def test_c::sharp::expressions::delegatecreationexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::DelegateCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::typeofexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::TypeOfExpression)


def test_c::sharp::expressions::typeofexpression_constructor_exists():
    assert callable(c::sharp::expressions::TypeOfExpression.__init__)


def test_c::sharp::expressions::typeofexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::TypeOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::literals::literal_is_not_abstract():
    assert not inspect.isabstract(c::sharp::literals::Literal)


def test_c::sharp::literals::literal_constructor_exists():
    assert callable(c::sharp::literals::Literal.__init__)


def test_c::sharp::literals::literal_constructor_args():
    sig = inspect.signature(c::sharp::literals::Literal.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::baseaccess_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::BaseAccess)


def test_c::sharp::expressions::baseaccess_constructor_exists():
    assert callable(c::sharp::expressions::BaseAccess.__init__)


def test_c::sharp::expressions::baseaccess_constructor_args():
    sig = inspect.signature(c::sharp::expressions::BaseAccess.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::constantdeclarator_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::ConstantDeclarator)


def test_c::sharp::statements::constantdeclarator_constructor_exists():
    assert callable(c::sharp::statements::ConstantDeclarator.__init__)


def test_c::sharp::statements::constantdeclarator_constructor_args():
    sig = inspect.signature(c::sharp::statements::ConstantDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::localconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::LocalConstantDeclaration)


def test_c::sharp::statements::localconstantdeclaration_constructor_exists():
    assert callable(c::sharp::statements::LocalConstantDeclaration.__init__)


def test_c::sharp::statements::localconstantdeclaration_constructor_args():
    sig = inspect.signature(c::sharp::statements::LocalConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::variabledeclarator_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::VariableDeclarator)


def test_c::sharp::statements::variabledeclarator_constructor_exists():
    assert callable(c::sharp::statements::VariableDeclarator.__init__)


def test_c::sharp::statements::variabledeclarator_constructor_args():
    sig = inspect.signature(c::sharp::statements::VariableDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::statementexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::StatementExpression)


def test_c::sharp::expressions::statementexpression_constructor_exists():
    assert callable(c::sharp::expressions::StatementExpression.__init__)


def test_c::sharp::expressions::statementexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_statements::resourceacquisition_is_not_abstract():
    assert not inspect.isabstract(statements::ResourceAcquisition)


def test_statements::resourceacquisition_constructor_exists():
    assert callable(statements::ResourceAcquisition.__init__)


def test_statements::resourceacquisition_constructor_args():
    sig = inspect.signature(statements::ResourceAcquisition.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::expression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::Expression)


def test_c::sharp::expressions::expression_constructor_exists():
    assert callable(c::sharp::expressions::Expression.__init__)


def test_c::sharp::expressions::expression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statements::forinitializer_is_not_abstract():
    assert not inspect.isabstract(statements::ForInitializer)


def test_statements::forinitializer_constructor_exists():
    assert callable(statements::ForInitializer.__init__)


def test_statements::forinitializer_constructor_args():
    sig = inspect.signature(statements::ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::VariableDeclaration)


def test_c::sharp::statements::variabledeclaration_constructor_exists():
    assert callable(c::sharp::statements::VariableDeclaration.__init__)


def test_c::sharp::statements::variabledeclaration_constructor_args():
    sig = inspect.signature(c::sharp::statements::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::fixedpointerdeclarator_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::FixedPointerDeclarator)


def test_c::sharp::statements::fixedpointerdeclarator_constructor_exists():
    assert callable(c::sharp::statements::FixedPointerDeclarator.__init__)


def test_c::sharp::statements::fixedpointerdeclarator_constructor_args():
    sig = inspect.signature(c::sharp::statements::FixedPointerDeclarator.__init__)
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



def test_c::sharp::statements::finallyclause_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::FinallyClause)


def test_c::sharp::statements::finallyclause_constructor_exists():
    assert callable(c::sharp::statements::FinallyClause.__init__)


def test_c::sharp::statements::finallyclause_constructor_args():
    sig = inspect.signature(c::sharp::statements::FinallyClause.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::generalcatchclause_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::GeneralCatchClause)


def test_c::sharp::statements::generalcatchclause_constructor_exists():
    assert callable(c::sharp::statements::GeneralCatchClause.__init__)


def test_c::sharp::statements::generalcatchclause_constructor_args():
    sig = inspect.signature(c::sharp::statements::GeneralCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::specificcatchclause_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::SpecificCatchClause)


def test_c::sharp::statements::specificcatchclause_constructor_exists():
    assert callable(c::sharp::statements::SpecificCatchClause.__init__)


def test_c::sharp::statements::specificcatchclause_constructor_args():
    sig = inspect.signature(c::sharp::statements::SpecificCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_finallyclause_is_not_abstract():
    assert not inspect.isabstract(FinallyClause)


def test_finallyclause_constructor_exists():
    assert callable(FinallyClause.__init__)


def test_finallyclause_constructor_args():
    sig = inspect.signature(FinallyClause.__init__)
    params = list(sig.parameters.keys())



def test_resourceacquisition_is_not_abstract():
    assert not inspect.isabstract(ResourceAcquisition)


def test_resourceacquisition_constructor_exists():
    assert callable(ResourceAcquisition.__init__)


def test_resourceacquisition_constructor_args():
    sig = inspect.signature(ResourceAcquisition.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::resourceacquisition_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::ResourceAcquisition)


def test_c::sharp::statements::resourceacquisition_constructor_exists():
    assert callable(c::sharp::statements::ResourceAcquisition.__init__)


def test_c::sharp::statements::resourceacquisition_constructor_args():
    sig = inspect.signature(c::sharp::statements::ResourceAcquisition.__init__)
    params = list(sig.parameters.keys())



def test_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(JumpStatement)


def test_jumpstatement_constructor_exists():
    assert callable(JumpStatement.__init__)


def test_jumpstatement_constructor_args():
    sig = inspect.signature(JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::throwstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::ThrowStatement)


def test_c::sharp::statements::throwstatement_constructor_exists():
    assert callable(c::sharp::statements::ThrowStatement.__init__)


def test_c::sharp::statements::throwstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::returnstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::ReturnStatement)


def test_c::sharp::statements::returnstatement_constructor_exists():
    assert callable(c::sharp::statements::ReturnStatement.__init__)


def test_c::sharp::statements::returnstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::continuestatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::ContinueStatement)


def test_c::sharp::statements::continuestatement_constructor_exists():
    assert callable(c::sharp::statements::ContinueStatement.__init__)


def test_c::sharp::statements::continuestatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::gotostatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::GotoStatement)


def test_c::sharp::statements::gotostatement_constructor_exists():
    assert callable(c::sharp::statements::GotoStatement.__init__)


def test_c::sharp::statements::gotostatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::GotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::breakstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::BreakStatement)


def test_c::sharp::statements::breakstatement_constructor_exists():
    assert callable(c::sharp::statements::BreakStatement.__init__)


def test_c::sharp::statements::breakstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::forinitializer_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::ForInitializer)


def test_c::sharp::statements::forinitializer_constructor_exists():
    assert callable(c::sharp::statements::ForInitializer.__init__)


def test_c::sharp::statements::forinitializer_constructor_args():
    sig = inspect.signature(c::sharp::statements::ForInitializer.__init__)
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



def test_forinitializer_is_not_abstract():
    assert not inspect.isabstract(ForInitializer)


def test_forinitializer_constructor_exists():
    assert callable(ForInitializer.__init__)


def test_forinitializer_constructor_args():
    sig = inspect.signature(ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::statementexpressionlist_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::StatementExpressionList)


def test_c::sharp::expressions::statementexpressionlist_constructor_exists():
    assert callable(c::sharp::expressions::StatementExpressionList.__init__)


def test_c::sharp::expressions::statementexpressionlist_constructor_args():
    sig = inspect.signature(c::sharp::expressions::StatementExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_iterationstatement_is_not_abstract():
    assert not inspect.isabstract(IterationStatement)


def test_iterationstatement_constructor_exists():
    assert callable(IterationStatement.__init__)


def test_iterationstatement_constructor_args():
    sig = inspect.signature(IterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::foreachstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::ForeachStatement)


def test_c::sharp::statements::foreachstatement_constructor_exists():
    assert callable(c::sharp::statements::ForeachStatement.__init__)


def test_c::sharp::statements::foreachstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::ForeachStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::forstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::ForStatement)


def test_c::sharp::statements::forstatement_constructor_exists():
    assert callable(c::sharp::statements::ForStatement.__init__)


def test_c::sharp::statements::forstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::dostatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::DoStatement)


def test_c::sharp::statements::dostatement_constructor_exists():
    assert callable(c::sharp::statements::DoStatement.__init__)


def test_c::sharp::statements::dostatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::whilestatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::WhileStatement)


def test_c::sharp::statements::whilestatement_constructor_exists():
    assert callable(c::sharp::statements::WhileStatement.__init__)


def test_c::sharp::statements::whilestatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_case_is_not_abstract():
    assert not inspect.isabstract(Case)


def test_case_constructor_exists():
    assert callable(Case.__init__)


def test_case_constructor_args():
    sig = inspect.signature(Case.__init__)
    params = list(sig.parameters.keys())



def test_default_is_not_abstract():
    assert not inspect.isabstract(Default)


def test_default_constructor_exists():
    assert callable(Default.__init__)


def test_default_constructor_args():
    sig = inspect.signature(Default.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::switchlabel_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::SwitchLabel)


def test_c::sharp::statements::switchlabel_constructor_exists():
    assert callable(c::sharp::statements::SwitchLabel.__init__)


def test_c::sharp::statements::switchlabel_constructor_args():
    sig = inspect.signature(c::sharp::statements::SwitchLabel.__init__)
    params = list(sig.parameters.keys())



def test_switchlabel_is_not_abstract():
    assert not inspect.isabstract(SwitchLabel)


def test_switchlabel_constructor_exists():
    assert callable(SwitchLabel.__init__)


def test_switchlabel_constructor_args():
    sig = inspect.signature(SwitchLabel.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::switchsection_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::SwitchSection)


def test_c::sharp::statements::switchsection_constructor_exists():
    assert callable(c::sharp::statements::SwitchSection.__init__)


def test_c::sharp::statements::switchsection_constructor_args():
    sig = inspect.signature(c::sharp::statements::SwitchSection.__init__)
    params = list(sig.parameters.keys())



def test_switchsection_is_not_abstract():
    assert not inspect.isabstract(SwitchSection)


def test_switchsection_constructor_exists():
    assert callable(SwitchSection.__init__)


def test_switchsection_constructor_args():
    sig = inspect.signature(SwitchSection.__init__)
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



def test_c::sharp::statements::lockstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::LockStatement)


def test_c::sharp::statements::lockstatement_constructor_exists():
    assert callable(c::sharp::statements::LockStatement.__init__)


def test_c::sharp::statements::lockstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::LockStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::ExpressionStatement)


def test_c::sharp::statements::expressionstatement_constructor_exists():
    assert callable(c::sharp::statements::ExpressionStatement.__init__)


def test_c::sharp::statements::expressionstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::usingstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::UsingStatement)


def test_c::sharp::statements::usingstatement_constructor_exists():
    assert callable(c::sharp::statements::UsingStatement.__init__)


def test_c::sharp::statements::usingstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::UsingStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::uncheckedstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::UncheckedStatement)


def test_c::sharp::statements::uncheckedstatement_constructor_exists():
    assert callable(c::sharp::statements::UncheckedStatement.__init__)


def test_c::sharp::statements::uncheckedstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::UncheckedStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::checkedstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::CheckedStatement)


def test_c::sharp::statements::checkedstatement_constructor_exists():
    assert callable(c::sharp::statements::CheckedStatement.__init__)


def test_c::sharp::statements::checkedstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::CheckedStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::emptystatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::EmptyStatement)


def test_c::sharp::statements::emptystatement_constructor_exists():
    assert callable(c::sharp::statements::EmptyStatement.__init__)


def test_c::sharp::statements::emptystatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::jumpstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::JumpStatement)


def test_c::sharp::statements::jumpstatement_constructor_exists():
    assert callable(c::sharp::statements::JumpStatement.__init__)


def test_c::sharp::statements::jumpstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::fixedstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::FixedStatement)


def test_c::sharp::statements::fixedstatement_constructor_exists():
    assert callable(c::sharp::statements::FixedStatement.__init__)


def test_c::sharp::statements::fixedstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::FixedStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::iterationstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::IterationStatement)


def test_c::sharp::statements::iterationstatement_constructor_exists():
    assert callable(c::sharp::statements::IterationStatement.__init__)


def test_c::sharp::statements::iterationstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::IterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::trystatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::TryStatement)


def test_c::sharp::statements::trystatement_constructor_exists():
    assert callable(c::sharp::statements::TryStatement.__init__)


def test_c::sharp::statements::trystatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::simpleembeddedstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::SimpleEmbeddedStatement)


def test_c::sharp::statements::simpleembeddedstatement_constructor_exists():
    assert callable(c::sharp::statements::SimpleEmbeddedStatement.__init__)


def test_c::sharp::statements::simpleembeddedstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::SimpleEmbeddedStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::embeddedstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::EmbeddedStatement)


def test_c::sharp::statements::embeddedstatement_constructor_exists():
    assert callable(c::sharp::statements::EmbeddedStatement.__init__)


def test_c::sharp::statements::embeddedstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::EmbeddedStatement.__init__)
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



def test_c::sharp::statements::declarationstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::DeclarationStatement)


def test_c::sharp::statements::declarationstatement_constructor_exists():
    assert callable(c::sharp::statements::DeclarationStatement.__init__)


def test_c::sharp::statements::declarationstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::DeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_statementexpressionlist_is_not_abstract():
    assert not inspect.isabstract(StatementExpressionList)


def test_statementexpressionlist_constructor_exists():
    assert callable(StatementExpressionList.__init__)


def test_statementexpressionlist_constructor_args():
    sig = inspect.signature(StatementExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_selectionstatement_is_not_abstract():
    assert not inspect.isabstract(SelectionStatement)


def test_selectionstatement_constructor_exists():
    assert callable(SelectionStatement.__init__)


def test_selectionstatement_constructor_args():
    sig = inspect.signature(SelectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::switchstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::SwitchStatement)


def test_c::sharp::statements::switchstatement_constructor_exists():
    assert callable(c::sharp::statements::SwitchStatement.__init__)


def test_c::sharp::statements::switchstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::ifstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::IfStatement)


def test_c::sharp::statements::ifstatement_constructor_exists():
    assert callable(c::sharp::statements::IfStatement.__init__)


def test_c::sharp::statements::ifstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::selectionstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::SelectionStatement)


def test_c::sharp::statements::selectionstatement_constructor_exists():
    assert callable(c::sharp::statements::SelectionStatement.__init__)


def test_c::sharp::statements::selectionstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::SelectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_statementexpression_is_not_abstract():
    assert not inspect.isabstract(StatementExpression)


def test_statementexpression_constructor_exists():
    assert callable(StatementExpression.__init__)


def test_statementexpression_constructor_args():
    sig = inspect.signature(StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::predecrementexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::PreDecrementExpression)


def test_c::sharp::expressions::predecrementexpression_constructor_exists():
    assert callable(c::sharp::expressions::PreDecrementExpression.__init__)


def test_c::sharp::expressions::predecrementexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::PreDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::expressions::preincrementexpression_is_not_abstract():
    assert not inspect.isabstract(c::sharp::expressions::PreIncrementExpression)


def test_c::sharp::expressions::preincrementexpression_constructor_exists():
    assert callable(c::sharp::expressions::PreIncrementExpression.__init__)


def test_c::sharp::expressions::preincrementexpression_constructor_args():
    sig = inspect.signature(c::sharp::expressions::PreIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::attributes::attributes_is_not_abstract():
    assert not inspect.isabstract(c::sharp::attributes::Attributes)


def test_c::sharp::attributes::attributes_constructor_exists():
    assert callable(c::sharp::attributes::Attributes.__init__)


def test_c::sharp::attributes::attributes_constructor_args():
    sig = inspect.signature(c::sharp::attributes::Attributes.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::attributes::globalattributetarget_is_not_abstract():
    assert not inspect.isabstract(c::sharp::attributes::GlobalAttributeTarget)


def test_c::sharp::attributes::globalattributetarget_constructor_exists():
    assert callable(c::sharp::attributes::GlobalAttributeTarget.__init__)


def test_c::sharp::attributes::globalattributetarget_constructor_args():
    sig = inspect.signature(c::sharp::attributes::GlobalAttributeTarget.__init__)
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



def test_c::sharp::attributes::globalattributes_is_not_abstract():
    assert not inspect.isabstract(c::sharp::attributes::GlobalAttributes)


def test_c::sharp::attributes::globalattributes_constructor_exists():
    assert callable(c::sharp::attributes::GlobalAttributes.__init__)


def test_c::sharp::attributes::globalattributes_constructor_args():
    sig = inspect.signature(c::sharp::attributes::GlobalAttributes.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::arrays::rankspecifier_is_not_abstract():
    assert not inspect.isabstract(c::sharp::arrays::RankSpecifier)


def test_c::sharp::arrays::rankspecifier_constructor_exists():
    assert callable(c::sharp::arrays::RankSpecifier.__init__)


def test_c::sharp::arrays::rankspecifier_constructor_args():
    sig = inspect.signature(c::sharp::arrays::RankSpecifier.__init__)
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



def test_c::sharp::arrays::arraytype_is_not_abstract():
    assert not inspect.isabstract(c::sharp::arrays::ArrayType)


def test_c::sharp::arrays::arraytype_constructor_exists():
    assert callable(c::sharp::arrays::ArrayType.__init__)


def test_c::sharp::arrays::arraytype_constructor_args():
    sig = inspect.signature(c::sharp::arrays::ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_statements::statement_is_not_abstract():
    assert not inspect.isabstract(statements::Statement)


def test_statements::statement_constructor_exists():
    assert callable(statements::Statement.__init__)


def test_statements::statement_constructor_args():
    sig = inspect.signature(statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::LabeledStatement)


def test_c::sharp::statements::labeledstatement_constructor_exists():
    assert callable(c::sharp::statements::LabeledStatement.__init__)


def test_c::sharp::statements::labeledstatement_constructor_args():
    sig = inspect.signature(c::sharp::statements::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::statements::statement_is_not_abstract():
    assert not inspect.isabstract(c::sharp::statements::Statement)


def test_c::sharp::statements::statement_constructor_exists():
    assert callable(c::sharp::statements::Statement.__init__)


def test_c::sharp::statements::statement_constructor_args():
    sig = inspect.signature(c::sharp::statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::attributes::namedargument_is_not_abstract():
    assert not inspect.isabstract(c::sharp::attributes::NamedArgument)


def test_c::sharp::attributes::namedargument_constructor_exists():
    assert callable(c::sharp::attributes::NamedArgument.__init__)


def test_c::sharp::attributes::namedargument_constructor_args():
    sig = inspect.signature(c::sharp::attributes::NamedArgument.__init__)
    params = list(sig.parameters.keys())



def test_namedargument_is_not_abstract():
    assert not inspect.isabstract(NamedArgument)


def test_namedargument_constructor_exists():
    assert callable(NamedArgument.__init__)


def test_namedargument_constructor_args():
    sig = inspect.signature(NamedArgument.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::attributes::namedargumentlist_is_not_abstract():
    assert not inspect.isabstract(c::sharp::attributes::NamedArgumentList)


def test_c::sharp::attributes::namedargumentlist_constructor_exists():
    assert callable(c::sharp::attributes::NamedArgumentList.__init__)


def test_c::sharp::attributes::namedargumentlist_constructor_args():
    sig = inspect.signature(c::sharp::attributes::NamedArgumentList.__init__)
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



def test_c::sharp::attributes::attributearguments_is_not_abstract():
    assert not inspect.isabstract(c::sharp::attributes::AttributeArguments)


def test_c::sharp::attributes::attributearguments_constructor_exists():
    assert callable(c::sharp::attributes::AttributeArguments.__init__)


def test_c::sharp::attributes::attributearguments_constructor_args():
    sig = inspect.signature(c::sharp::attributes::AttributeArguments.__init__)
    params = list(sig.parameters.keys())



def test_attributearguments_is_not_abstract():
    assert not inspect.isabstract(AttributeArguments)


def test_attributearguments_constructor_exists():
    assert callable(AttributeArguments.__init__)


def test_attributearguments_constructor_args():
    sig = inspect.signature(AttributeArguments.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::attributes::attribute_is_not_abstract():
    assert not inspect.isabstract(c::sharp::attributes::Attribute)


def test_c::sharp::attributes::attribute_constructor_exists():
    assert callable(c::sharp::attributes::Attribute.__init__)


def test_c::sharp::attributes::attribute_constructor_args():
    sig = inspect.signature(c::sharp::attributes::Attribute.__init__)
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



def test_c::sharp::attributes::attributetarget_is_not_abstract():
    assert not inspect.isabstract(c::sharp::attributes::AttributeTarget)


def test_c::sharp::attributes::attributetarget_constructor_exists():
    assert callable(c::sharp::attributes::AttributeTarget.__init__)


def test_c::sharp::attributes::attributetarget_constructor_args():
    sig = inspect.signature(c::sharp::attributes::AttributeTarget.__init__)
    params = list(sig.parameters.keys())



def test_attributetarget_is_not_abstract():
    assert not inspect.isabstract(AttributeTarget)


def test_attributetarget_constructor_exists():
    assert callable(AttributeTarget.__init__)


def test_attributetarget_constructor_args():
    sig = inspect.signature(AttributeTarget.__init__)
    params = list(sig.parameters.keys())



def test_arraytype_is_not_abstract():
    assert not inspect.isabstract(ArrayType)


def test_arraytype_constructor_exists():
    assert callable(ArrayType.__init__)


def test_arraytype_constructor_args():
    sig = inspect.signature(ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_params_is_not_abstract():
    assert not inspect.isabstract(Params)


def test_params_constructor_exists():
    assert callable(Params.__init__)


def test_params_constructor_args():
    sig = inspect.signature(Params.__init__)
    params = list(sig.parameters.keys())



def test_c::sharp::classes::parameterarray_is_not_abstract():
    assert not inspect.isabstract(c::sharp::classes::ParameterArray)


def test_c::sharp::classes::parameterarray_constructor_exists():
    assert callable(c::sharp::classes::ParameterArray.__init__)


def test_c::sharp::classes::parameterarray_constructor_args():
    sig = inspect.signature(c::sharp::classes::ParameterArray.__init__)
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
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
c::sharp::operators::ExclusiveOr_strategy = st.builds(
    c::sharp::operators::ExclusiveOr,
)
c::sharp::operators::And_strategy = st.builds(
    c::sharp::operators::And,
)
c::sharp::operators::ConditionalOr_strategy = st.builds(
    c::sharp::operators::ConditionalOr,
)
c::sharp::operators::InclusiveOr_strategy = st.builds(
    c::sharp::operators::InclusiveOr,
)
c::sharp::operators::ConditionalAnd_strategy = st.builds(
    c::sharp::operators::ConditionalAnd,
)
c::sharp::operators::Complement_strategy = st.builds(
    c::sharp::operators::Complement,
)
MultiplicativeOperator_strategy = st.builds(
    MultiplicativeOperator,
)
c::sharp::operators::Remainder_strategy = st.builds(
    c::sharp::operators::Remainder,
)
c::sharp::operators::Multiplication_strategy = st.builds(
    c::sharp::operators::Multiplication,
)
c::sharp::operators::Division_strategy = st.builds(
    c::sharp::operators::Division,
)
operators::UnaryOperator_strategy = st.builds(
    operators::UnaryOperator,
)
operators::AdditiveOperator_strategy = st.builds(
    operators::AdditiveOperator,
)
c::sharp::operators::Subtraction_strategy = st.builds(
    c::sharp::operators::Subtraction,
)
c::sharp::operators::Addition_strategy = st.builds(
    c::sharp::operators::Addition,
)
RelationOperator_strategy = st.builds(
    RelationOperator,
)
c::sharp::operators::LessThanOrEqual_strategy = st.builds(
    c::sharp::operators::LessThanOrEqual,
)
c::sharp::operators::GreaterThanOrEqual_strategy = st.builds(
    c::sharp::operators::GreaterThanOrEqual,
)
c::sharp::operators::LessThan_strategy = st.builds(
    c::sharp::operators::LessThan,
)
c::sharp::operators::GreaterThan_strategy = st.builds(
    c::sharp::operators::GreaterThan,
)
EqualityOperator_strategy = st.builds(
    EqualityOperator,
)
c::sharp::operators::NotEqual_strategy = st.builds(
    c::sharp::operators::NotEqual,
)
c::sharp::operators::Equal_strategy = st.builds(
    c::sharp::operators::Equal,
)
Operator_strategy = st.builds(
    Operator,
)
c::sharp::operators::UnaryModificationOperator_strategy = st.builds(
    c::sharp::operators::UnaryModificationOperator,
)
c::sharp::operators::RelationOperator_strategy = st.builds(
    c::sharp::operators::RelationOperator,
)
c::sharp::operators::MultiplicativeOperator_strategy = st.builds(
    c::sharp::operators::MultiplicativeOperator,
)
c::sharp::operators::EqualityOperator_strategy = st.builds(
    c::sharp::operators::EqualityOperator,
)
c::sharp::operators::UnaryOperator_strategy = st.builds(
    c::sharp::operators::UnaryOperator,
)
c::sharp::operators::ShiftOperator_strategy = st.builds(
    c::sharp::operators::ShiftOperator,
)
c::sharp::operators::AssignmentOperator_strategy = st.builds(
    c::sharp::operators::AssignmentOperator,
)
c::sharp::operators::AdditiveOperator_strategy = st.builds(
    c::sharp::operators::AdditiveOperator,
)
c::sharp::operators::Operator_strategy = st.builds(
    c::sharp::operators::Operator,
)
c::sharp::keywords::Event_strategy = st.builds(
    c::sharp::keywords::Event,
)
c::sharp::keywords::Return_strategy = st.builds(
    c::sharp::keywords::Return,
)
c::sharp::keywords::Default_strategy = st.builds(
    c::sharp::keywords::Default,
)
c::sharp::keywords::Case_strategy = st.builds(
    c::sharp::keywords::Case,
)
c::sharp::keywords::Params_strategy = st.builds(
    c::sharp::keywords::Params,
)
c::sharp::keywords::Ref_strategy = st.builds(
    c::sharp::keywords::Ref,
)
c::sharp::keywords::Out_strategy = st.builds(
    c::sharp::keywords::Out,
)
ShiftOperator_strategy = st.builds(
    ShiftOperator,
)
c::sharp::operators::UnsignedRightShift_strategy = st.builds(
    c::sharp::operators::UnsignedRightShift,
)
c::sharp::operators::RightShift_strategy = st.builds(
    c::sharp::operators::RightShift,
)
c::sharp::operators::LeftShift_strategy = st.builds(
    c::sharp::operators::LeftShift,
)
c::sharp::operators::Negate_strategy = st.builds(
    c::sharp::operators::Negate,
)
UnaryModificationOperator_strategy = st.builds(
    UnaryModificationOperator,
)
c::sharp::operators::PlusPlus_strategy = st.builds(
    c::sharp::operators::PlusPlus,
)
c::sharp::operators::MinusMinus_strategy = st.builds(
    c::sharp::operators::MinusMinus,
)
Literal_strategy = st.builds(
    Literal,
)
c::sharp::literals::RealLiteral_strategy = st.builds(
    c::sharp::literals::RealLiteral,
    value=
        safe_text
)
c::sharp::literals::DecimalIntegerLiteral_strategy = st.builds(
    c::sharp::literals::DecimalIntegerLiteral,
    value=
        safe_text
)
c::sharp::literals::HexadecimalIntegerLiteral_strategy = st.builds(
    c::sharp::literals::HexadecimalIntegerLiteral,
    value=
        safe_text
)
c::sharp::literals::BooleanLiteral_strategy = st.builds(
    c::sharp::literals::BooleanLiteral,
    value=
        st.booleans()
)
c::sharp::modifiers::Modifier_strategy = st.builds(
    c::sharp::modifiers::Modifier,
)
ReferenceType_strategy = st.builds(
    ReferenceType,
)
c::sharp::types::ClassOrInterfaceOrDelegateOrEnumType_strategy = st.builds(
    c::sharp::types::ClassOrInterfaceOrDelegateOrEnumType,
)
c::sharp::literals::StringLiteral_strategy = st.builds(
    c::sharp::literals::StringLiteral,
    value=
        safe_text
)
c::sharp::literals::CharacterLiteral_strategy = st.builds(
    c::sharp::literals::CharacterLiteral,
    value=
        safe_text
)
c::sharp::literals::This_strategy = st.builds(
    c::sharp::literals::This,
)
c::sharp::literals::NullLiteral_strategy = st.builds(
    c::sharp::literals::NullLiteral,
)
types::Type_strategy = st.builds(
    types::Type,
)
types::NonArrayType_strategy = st.builds(
    types::NonArrayType,
)
c::sharp::types::SimpleType_strategy = st.builds(
    c::sharp::types::SimpleType,
)
c::sharp::types::PointerType_strategy = st.builds(
    c::sharp::types::PointerType,
)
c::sharp::types::ReferenceType_strategy = st.builds(
    c::sharp::types::ReferenceType,
)
c::sharp::types::NonArrayType_strategy = st.builds(
    c::sharp::types::NonArrayType,
)
c::sharp::types::Type_strategy = st.builds(
    c::sharp::types::Type,
)
ConditionalOr_strategy = st.builds(
    ConditionalOr,
)
ConditionalAndExpression_strategy = st.builds(
    ConditionalAndExpression,
)
c::sharp::expressions::ConditionalOrExpression_strategy = st.builds(
    c::sharp::expressions::ConditionalOrExpression,
)
ConditionalAnd_strategy = st.builds(
    ConditionalAnd,
)
InclusiveOrExpression_strategy = st.builds(
    InclusiveOrExpression,
)
c::sharp::expressions::ConditionalAndExpression_strategy = st.builds(
    c::sharp::expressions::ConditionalAndExpression,
)
InclusiveOr_strategy = st.builds(
    InclusiveOr,
)
ExclusiveOrExpression_strategy = st.builds(
    ExclusiveOrExpression,
)
c::sharp::expressions::InclusiveOrExpression_strategy = st.builds(
    c::sharp::expressions::InclusiveOrExpression,
)
ExclusiveOr_strategy = st.builds(
    ExclusiveOr,
)
AndExpression_strategy = st.builds(
    AndExpression,
)
c::sharp::expressions::ExclusiveOrExpression_strategy = st.builds(
    c::sharp::expressions::ExclusiveOrExpression,
)
And_strategy = st.builds(
    And,
)
EqualityExpression_strategy = st.builds(
    EqualityExpression,
)
c::sharp::expressions::AndExpression_strategy = st.builds(
    c::sharp::expressions::AndExpression,
)
NotEqual_strategy = st.builds(
    NotEqual,
)
Equal_strategy = st.builds(
    Equal,
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
c::sharp::expressions::RelationalExpression_strategy = st.builds(
    c::sharp::expressions::RelationalExpression,
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
c::sharp::expressions::ShiftExpression_strategy = st.builds(
    c::sharp::expressions::ShiftExpression,
)
MultiplicativeExpression_strategy = st.builds(
    MultiplicativeExpression,
)
c::sharp::expressions::AdditiveExpression_strategy = st.builds(
    c::sharp::expressions::AdditiveExpression,
)
Remainder_strategy = st.builds(
    Remainder,
)
Division_strategy = st.builds(
    Division,
)
c::sharp::expressions::MultiplicativeExpression_strategy = st.builds(
    c::sharp::expressions::MultiplicativeExpression,
)
c::sharp::expressions::AddressOfExpression_strategy = st.builds(
    c::sharp::expressions::AddressOfExpression,
)
RelationalExpression_strategy = st.builds(
    RelationalExpression,
)
c::sharp::expressions::EqualityExpression_strategy = st.builds(
    c::sharp::expressions::EqualityExpression,
)
GreaterThanOrEqual_strategy = st.builds(
    GreaterThanOrEqual,
)
GreaterThan_strategy = st.builds(
    GreaterThan,
)
c::sharp::classes::FixedParameter_strategy = st.builds(
    c::sharp::classes::FixedParameter,
)
ParameterArray_strategy = st.builds(
    ParameterArray,
)
Expression_strategy = st.builds(
    Expression,
)
VariableInitializer_strategy = st.builds(
    VariableInitializer,
)
c::sharp::arrays::ArrayInitializer_strategy = st.builds(
    c::sharp::arrays::ArrayInitializer,
)
c::sharp::arrays::StackallocInitializer_strategy = st.builds(
    c::sharp::arrays::StackallocInitializer,
)
VariableDeclarator_strategy = st.builds(
    VariableDeclarator,
)
ConstantDeclarator_strategy = st.builds(
    ConstantDeclarator,
)
c::sharp::classes::VariableInitializer_strategy = st.builds(
    c::sharp::classes::VariableInitializer,
)
Statement_strategy = st.builds(
    Statement,
)
c::sharp::classes::Block_strategy = st.builds(
    c::sharp::classes::Block,
)
classes::ClassMemberDeclaration_strategy = st.builds(
    classes::ClassMemberDeclaration,
)
namespaces::NamespaceMemberDeclaration_strategy = st.builds(
    namespaces::NamespaceMemberDeclaration,
)
c::sharp::namespaces::TypeDeclaration_strategy = st.builds(
    c::sharp::namespaces::TypeDeclaration,
)
c::sharp::namespaces::NamespaceBody_strategy = st.builds(
    c::sharp::namespaces::NamespaceBody,
)
NamespaceBody_strategy = st.builds(
    NamespaceBody,
)
c::sharp::namespaces::NamespaceMemberDeclaration_strategy = st.builds(
    c::sharp::namespaces::NamespaceMemberDeclaration,
)
NamespaceOrTypeName_strategy = st.builds(
    NamespaceOrTypeName,
)
FixedParameter_strategy = st.builds(
    FixedParameter,
)
c::sharp::classes::FormalParameterList_strategy = st.builds(
    c::sharp::classes::FormalParameterList,
)
Block_strategy = st.builds(
    Block,
)
FormalParameterList_strategy = st.builds(
    FormalParameterList,
)
Type_strategy = st.builds(
    Type,
)
c::sharp::classes::ClassMemberDeclaration_strategy = st.builds(
    c::sharp::classes::ClassMemberDeclaration,
)
ClassOrInterfaceOrDelegateOrEnumType_strategy = st.builds(
    ClassOrInterfaceOrDelegateOrEnumType,
)
c::sharp::classes::ClassBase_strategy = st.builds(
    c::sharp::classes::ClassBase,
)
ClassMemberDeclaration_strategy = st.builds(
    ClassMemberDeclaration,
)
c::sharp::classes::ConstantDeclaration_strategy = st.builds(
    c::sharp::classes::ConstantDeclaration,
)
c::sharp::classes::FieldDeclaration_strategy = st.builds(
    c::sharp::classes::FieldDeclaration,
)
ClassBase_strategy = st.builds(
    ClassBase,
)
Modifier_strategy = st.builds(
    Modifier,
)
c::sharp::modifiers::ReadOnly_strategy = st.builds(
    c::sharp::modifiers::ReadOnly,
)
c::sharp::modifiers::Partial_strategy = st.builds(
    c::sharp::modifiers::Partial,
)
c::sharp::modifiers::Protected_strategy = st.builds(
    c::sharp::modifiers::Protected,
)
c::sharp::modifiers::Unsafe_strategy = st.builds(
    c::sharp::modifiers::Unsafe,
)
c::sharp::modifiers::Sealed_strategy = st.builds(
    c::sharp::modifiers::Sealed,
)
c::sharp::modifiers::Abstract_strategy = st.builds(
    c::sharp::modifiers::Abstract,
)
c::sharp::modifiers::Static_strategy = st.builds(
    c::sharp::modifiers::Static,
)
c::sharp::modifiers::Private_strategy = st.builds(
    c::sharp::modifiers::Private,
)
c::sharp::modifiers::Internal_strategy = st.builds(
    c::sharp::modifiers::Internal,
)
c::sharp::modifiers::Volatile_strategy = st.builds(
    c::sharp::modifiers::Volatile,
)
c::sharp::modifiers::Public_strategy = st.builds(
    c::sharp::modifiers::Public,
)
c::sharp::modifiers::OverrideModifier_strategy = st.builds(
    c::sharp::modifiers::OverrideModifier,
)
c::sharp::modifiers::New_strategy = st.builds(
    c::sharp::modifiers::New,
)
c::sharp::modifiers::Extern_strategy = st.builds(
    c::sharp::modifiers::Extern,
)
c::sharp::modifiers::Virtual_strategy = st.builds(
    c::sharp::modifiers::Virtual,
)
Attributes_strategy = st.builds(
    Attributes,
)
namespaces::TypeDeclaration_strategy = st.builds(
    namespaces::TypeDeclaration,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
c::sharp::namespaces::UsingDirective_strategy = st.builds(
    c::sharp::namespaces::UsingDirective,
)
NamespaceMemberDeclaration_strategy = st.builds(
    NamespaceMemberDeclaration,
)
c::sharp::namespaces::Namespace_strategy = st.builds(
    c::sharp::namespaces::Namespace,
)
GlobalAttributes_strategy = st.builds(
    GlobalAttributes,
)
UsingDirective_strategy = st.builds(
    UsingDirective,
)
c::sharp::namespaces::CompilationUnit_strategy = st.builds(
    c::sharp::namespaces::CompilationUnit,
)
expressions::PrimaryNoArrayCreationExpression_strategy = st.builds(
    expressions::PrimaryNoArrayCreationExpression,
)
common::NamedElement_strategy = st.builds(
    common::NamedElement,
)
c::sharp::classes::Method_strategy = st.builds(
    c::sharp::classes::Method,
)
c::sharp::classes::Class_strategy = st.builds(
    c::sharp::classes::Class,
)
c::sharp::common::Identifier_strategy = st.builds(
    c::sharp::common::Identifier,
)
Identifier_strategy = st.builds(
    Identifier,
)
c::sharp::common::NamespaceOrTypeName_strategy = st.builds(
    c::sharp::common::NamespaceOrTypeName,
)
c::sharp::common::NamedElement_strategy = st.builds(
    c::sharp::common::NamedElement,
    name=
        safe_text
)
AssignmentOperator_strategy = st.builds(
    AssignmentOperator,
)
c::sharp::operators::AssignmentMinus_strategy = st.builds(
    c::sharp::operators::AssignmentMinus,
)
c::sharp::operators::AssignmentRightShift_strategy = st.builds(
    c::sharp::operators::AssignmentRightShift,
)
c::sharp::operators::AssignmentOr_strategy = st.builds(
    c::sharp::operators::AssignmentOr,
)
c::sharp::operators::Assignment_strategy = st.builds(
    c::sharp::operators::Assignment,
)
c::sharp::operators::AssignmentAnd_strategy = st.builds(
    c::sharp::operators::AssignmentAnd,
)
c::sharp::operators::AssignmentModulo_strategy = st.builds(
    c::sharp::operators::AssignmentModulo,
)
c::sharp::operators::AssignmentPlus_strategy = st.builds(
    c::sharp::operators::AssignmentPlus,
)
c::sharp::operators::AssignmentDivision_strategy = st.builds(
    c::sharp::operators::AssignmentDivision,
)
c::sharp::operators::AssignmentMultiplication_strategy = st.builds(
    c::sharp::operators::AssignmentMultiplication,
)
c::sharp::operators::AssignmentLeftShift_strategy = st.builds(
    c::sharp::operators::AssignmentLeftShift,
)
c::sharp::operators::AssignmentExclusiveOr_strategy = st.builds(
    c::sharp::operators::AssignmentExclusiveOr,
)
c::sharp::operators::AssignmentUnsignedRightShift_strategy = st.builds(
    c::sharp::operators::AssignmentUnsignedRightShift,
)
expressions::Expression_strategy = st.builds(
    expressions::Expression,
)
ConditionalOrExpression_strategy = st.builds(
    ConditionalOrExpression,
)
c::sharp::expressions::ConditionalExpression_strategy = st.builds(
    c::sharp::expressions::ConditionalExpression,
)
AddressOfExpression_strategy = st.builds(
    AddressOfExpression,
)
c::sharp::expressions::CastExpression_strategy = st.builds(
    c::sharp::expressions::CastExpression,
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
c::sharp::expressions::UnaryExpression_strategy = st.builds(
    c::sharp::expressions::UnaryExpression,
)
ArrayInitializer_strategy = st.builds(
    ArrayInitializer,
)
CastExpression_strategy = st.builds(
    CastExpression,
)
PreDecrementExpression_strategy = st.builds(
    PreDecrementExpression,
)
PreIncrementExpression_strategy = st.builds(
    PreIncrementExpression,
)
ArgumentList_strategy = st.builds(
    ArgumentList,
)
expressions::StatementExpression_strategy = st.builds(
    expressions::StatementExpression,
)
c::sharp::expressions::ObjectCreationExpression_strategy = st.builds(
    c::sharp::expressions::ObjectCreationExpression,
)
c::sharp::expressions::AssignmentExpression_strategy = st.builds(
    c::sharp::expressions::AssignmentExpression,
)
expressions::PrimaryExtendedExpressionType_strategy = st.builds(
    expressions::PrimaryExtendedExpressionType,
)
c::sharp::expressions::PostDecrementExpression_strategy = st.builds(
    c::sharp::expressions::PostDecrementExpression,
)
c::sharp::expressions::PostIncrementExpression_strategy = st.builds(
    c::sharp::expressions::PostIncrementExpression,
)
c::sharp::expressions::InvocationExpression_strategy = st.builds(
    c::sharp::expressions::InvocationExpression,
)
SimpleType_strategy = st.builds(
    SimpleType,
)
c::sharp::types::Object_strategy = st.builds(
    c::sharp::types::Object,
)
c::sharp::types::Short_strategy = st.builds(
    c::sharp::types::Short,
)
c::sharp::types::Char_strategy = st.builds(
    c::sharp::types::Char,
)
c::sharp::types::UInt_strategy = st.builds(
    c::sharp::types::UInt,
)
c::sharp::types::Int_strategy = st.builds(
    c::sharp::types::Int,
)
c::sharp::types::Byte_strategy = st.builds(
    c::sharp::types::Byte,
)
c::sharp::types::SByte_strategy = st.builds(
    c::sharp::types::SByte,
)
c::sharp::types::ULong_strategy = st.builds(
    c::sharp::types::ULong,
)
c::sharp::types::Long_strategy = st.builds(
    c::sharp::types::Long,
)
c::sharp::types::Double_strategy = st.builds(
    c::sharp::types::Double,
)
c::sharp::types::Decimal_strategy = st.builds(
    c::sharp::types::Decimal,
)
c::sharp::types::Bool_strategy = st.builds(
    c::sharp::types::Bool,
)
c::sharp::types::UShort_strategy = st.builds(
    c::sharp::types::UShort,
)
c::sharp::types::Float_strategy = st.builds(
    c::sharp::types::Float,
)
c::sharp::types::Void_strategy = st.builds(
    c::sharp::types::Void,
)
c::sharp::types::String_strategy = st.builds(
    c::sharp::types::String,
)
PrimaryExtendedExpressionType_strategy = st.builds(
    PrimaryExtendedExpressionType,
)
c::sharp::expressions::ElementAccess_strategy = st.builds(
    c::sharp::expressions::ElementAccess,
)
c::sharp::expressions::PointerMemberAccess_strategy = st.builds(
    c::sharp::expressions::PointerMemberAccess,
)
c::sharp::expressions::MemberAccess_strategy = st.builds(
    c::sharp::expressions::MemberAccess,
)
c::sharp::expressions::PrimaryExtendedExpressionType_strategy = st.builds(
    c::sharp::expressions::PrimaryExtendedExpressionType,
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
c::sharp::expressions::ArrayCreationExpression_strategy = st.builds(
    c::sharp::expressions::ArrayCreationExpression,
)
c::sharp::expressions::PrimaryNoArrayCreationExpression_strategy = st.builds(
    c::sharp::expressions::PrimaryNoArrayCreationExpression,
)
c::sharp::expressions::PrimaryExpression_strategy = st.builds(
    c::sharp::expressions::PrimaryExpression,
)
Argument_strategy = st.builds(
    Argument,
)
c::sharp::expressions::ArgumentList_strategy = st.builds(
    c::sharp::expressions::ArgumentList,
)
c::sharp::expressions::Argument_strategy = st.builds(
    c::sharp::expressions::Argument,
)
c::sharp::expressions::ExpressionList_strategy = st.builds(
    c::sharp::expressions::ExpressionList,
)
classes::VariableInitializer_strategy = st.builds(
    classes::VariableInitializer,
)
PrimaryNoArrayCreationExpression_strategy = st.builds(
    PrimaryNoArrayCreationExpression,
)
c::sharp::expressions::CheckedExpression_strategy = st.builds(
    c::sharp::expressions::CheckedExpression,
)
c::sharp::expressions::SizeOfExpression_strategy = st.builds(
    c::sharp::expressions::SizeOfExpression,
)
c::sharp::expressions::UncheckedExpression_strategy = st.builds(
    c::sharp::expressions::UncheckedExpression,
)
c::sharp::expressions::ParenthesizedExpression_strategy = st.builds(
    c::sharp::expressions::ParenthesizedExpression,
)
c::sharp::expressions::DelegateCreationExpression_strategy = st.builds(
    c::sharp::expressions::DelegateCreationExpression,
)
c::sharp::expressions::TypeOfExpression_strategy = st.builds(
    c::sharp::expressions::TypeOfExpression,
)
c::sharp::literals::Literal_strategy = st.builds(
    c::sharp::literals::Literal,
)
c::sharp::expressions::BaseAccess_strategy = st.builds(
    c::sharp::expressions::BaseAccess,
)
c::sharp::statements::ConstantDeclarator_strategy = st.builds(
    c::sharp::statements::ConstantDeclarator,
)
c::sharp::statements::LocalConstantDeclaration_strategy = st.builds(
    c::sharp::statements::LocalConstantDeclaration,
)
c::sharp::statements::VariableDeclarator_strategy = st.builds(
    c::sharp::statements::VariableDeclarator,
)
c::sharp::expressions::StatementExpression_strategy = st.builds(
    c::sharp::expressions::StatementExpression,
)
statements::ResourceAcquisition_strategy = st.builds(
    statements::ResourceAcquisition,
)
c::sharp::expressions::Expression_strategy = st.builds(
    c::sharp::expressions::Expression,
)
statements::ForInitializer_strategy = st.builds(
    statements::ForInitializer,
)
c::sharp::statements::VariableDeclaration_strategy = st.builds(
    c::sharp::statements::VariableDeclaration,
)
c::sharp::statements::FixedPointerDeclarator_strategy = st.builds(
    c::sharp::statements::FixedPointerDeclarator,
)
FixedPointerDeclarator_strategy = st.builds(
    FixedPointerDeclarator,
)
PointerType_strategy = st.builds(
    PointerType,
)
c::sharp::statements::FinallyClause_strategy = st.builds(
    c::sharp::statements::FinallyClause,
)
c::sharp::statements::GeneralCatchClause_strategy = st.builds(
    c::sharp::statements::GeneralCatchClause,
)
c::sharp::statements::SpecificCatchClause_strategy = st.builds(
    c::sharp::statements::SpecificCatchClause,
)
FinallyClause_strategy = st.builds(
    FinallyClause,
)
ResourceAcquisition_strategy = st.builds(
    ResourceAcquisition,
)
c::sharp::statements::ResourceAcquisition_strategy = st.builds(
    c::sharp::statements::ResourceAcquisition,
)
JumpStatement_strategy = st.builds(
    JumpStatement,
)
c::sharp::statements::ThrowStatement_strategy = st.builds(
    c::sharp::statements::ThrowStatement,
)
c::sharp::statements::ReturnStatement_strategy = st.builds(
    c::sharp::statements::ReturnStatement,
)
c::sharp::statements::ContinueStatement_strategy = st.builds(
    c::sharp::statements::ContinueStatement,
)
c::sharp::statements::GotoStatement_strategy = st.builds(
    c::sharp::statements::GotoStatement,
)
c::sharp::statements::BreakStatement_strategy = st.builds(
    c::sharp::statements::BreakStatement,
)
c::sharp::statements::ForInitializer_strategy = st.builds(
    c::sharp::statements::ForInitializer,
)
GeneralCatchClause_strategy = st.builds(
    GeneralCatchClause,
)
SpecificCatchClause_strategy = st.builds(
    SpecificCatchClause,
)
ForInitializer_strategy = st.builds(
    ForInitializer,
)
c::sharp::expressions::StatementExpressionList_strategy = st.builds(
    c::sharp::expressions::StatementExpressionList,
)
IterationStatement_strategy = st.builds(
    IterationStatement,
)
c::sharp::statements::ForeachStatement_strategy = st.builds(
    c::sharp::statements::ForeachStatement,
)
c::sharp::statements::ForStatement_strategy = st.builds(
    c::sharp::statements::ForStatement,
)
c::sharp::statements::DoStatement_strategy = st.builds(
    c::sharp::statements::DoStatement,
)
c::sharp::statements::WhileStatement_strategy = st.builds(
    c::sharp::statements::WhileStatement,
)
Case_strategy = st.builds(
    Case,
)
Default_strategy = st.builds(
    Default,
)
c::sharp::statements::SwitchLabel_strategy = st.builds(
    c::sharp::statements::SwitchLabel,
)
SwitchLabel_strategy = st.builds(
    SwitchLabel,
)
c::sharp::statements::SwitchSection_strategy = st.builds(
    c::sharp::statements::SwitchSection,
)
SwitchSection_strategy = st.builds(
    SwitchSection,
)
Unsafe_strategy = st.builds(
    Unsafe,
)
EmbeddedStatement_strategy = st.builds(
    EmbeddedStatement,
)
c::sharp::statements::LockStatement_strategy = st.builds(
    c::sharp::statements::LockStatement,
)
c::sharp::statements::ExpressionStatement_strategy = st.builds(
    c::sharp::statements::ExpressionStatement,
)
c::sharp::statements::UsingStatement_strategy = st.builds(
    c::sharp::statements::UsingStatement,
)
c::sharp::statements::UncheckedStatement_strategy = st.builds(
    c::sharp::statements::UncheckedStatement,
)
c::sharp::statements::CheckedStatement_strategy = st.builds(
    c::sharp::statements::CheckedStatement,
)
c::sharp::statements::EmptyStatement_strategy = st.builds(
    c::sharp::statements::EmptyStatement,
)
c::sharp::statements::JumpStatement_strategy = st.builds(
    c::sharp::statements::JumpStatement,
)
c::sharp::statements::FixedStatement_strategy = st.builds(
    c::sharp::statements::FixedStatement,
)
c::sharp::statements::IterationStatement_strategy = st.builds(
    c::sharp::statements::IterationStatement,
)
c::sharp::statements::TryStatement_strategy = st.builds(
    c::sharp::statements::TryStatement,
)
c::sharp::statements::SimpleEmbeddedStatement_strategy = st.builds(
    c::sharp::statements::SimpleEmbeddedStatement,
)
c::sharp::statements::EmbeddedStatement_strategy = st.builds(
    c::sharp::statements::EmbeddedStatement,
)
LocalConstantDeclaration_strategy = st.builds(
    LocalConstantDeclaration,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
c::sharp::statements::DeclarationStatement_strategy = st.builds(
    c::sharp::statements::DeclarationStatement,
)
StatementExpressionList_strategy = st.builds(
    StatementExpressionList,
)
SelectionStatement_strategy = st.builds(
    SelectionStatement,
)
c::sharp::statements::SwitchStatement_strategy = st.builds(
    c::sharp::statements::SwitchStatement,
)
c::sharp::statements::IfStatement_strategy = st.builds(
    c::sharp::statements::IfStatement,
)
c::sharp::statements::SelectionStatement_strategy = st.builds(
    c::sharp::statements::SelectionStatement,
)
StatementExpression_strategy = st.builds(
    StatementExpression,
)
c::sharp::expressions::PreDecrementExpression_strategy = st.builds(
    c::sharp::expressions::PreDecrementExpression,
)
c::sharp::expressions::PreIncrementExpression_strategy = st.builds(
    c::sharp::expressions::PreIncrementExpression,
)
c::sharp::attributes::Attributes_strategy = st.builds(
    c::sharp::attributes::Attributes,
)
c::sharp::attributes::GlobalAttributeTarget_strategy = st.builds(
    c::sharp::attributes::GlobalAttributeTarget,
)
Attribute_strategy = st.builds(
    Attribute,
)
GlobalAttributeTarget_strategy = st.builds(
    GlobalAttributeTarget,
)
c::sharp::attributes::GlobalAttributes_strategy = st.builds(
    c::sharp::attributes::GlobalAttributes,
)
c::sharp::arrays::RankSpecifier_strategy = st.builds(
    c::sharp::arrays::RankSpecifier,
)
RankSpecifier_strategy = st.builds(
    RankSpecifier,
)
NonArrayType_strategy = st.builds(
    NonArrayType,
)
c::sharp::arrays::ArrayType_strategy = st.builds(
    c::sharp::arrays::ArrayType,
)
statements::Statement_strategy = st.builds(
    statements::Statement,
)
c::sharp::statements::LabeledStatement_strategy = st.builds(
    c::sharp::statements::LabeledStatement,
)
c::sharp::statements::Statement_strategy = st.builds(
    c::sharp::statements::Statement,
)
c::sharp::attributes::NamedArgument_strategy = st.builds(
    c::sharp::attributes::NamedArgument,
)
NamedArgument_strategy = st.builds(
    NamedArgument,
)
c::sharp::attributes::NamedArgumentList_strategy = st.builds(
    c::sharp::attributes::NamedArgumentList,
)
NamedArgumentList_strategy = st.builds(
    NamedArgumentList,
)
ExpressionList_strategy = st.builds(
    ExpressionList,
)
c::sharp::attributes::AttributeArguments_strategy = st.builds(
    c::sharp::attributes::AttributeArguments,
)
AttributeArguments_strategy = st.builds(
    AttributeArguments,
)
c::sharp::attributes::Attribute_strategy = st.builds(
    c::sharp::attributes::Attribute,
)
Return_strategy = st.builds(
    Return,
)
Event_strategy = st.builds(
    Event,
)
c::sharp::attributes::AttributeTarget_strategy = st.builds(
    c::sharp::attributes::AttributeTarget,
)
AttributeTarget_strategy = st.builds(
    AttributeTarget,
)
ArrayType_strategy = st.builds(
    ArrayType,
)
Params_strategy = st.builds(
    Params,
)
c::sharp::classes::ParameterArray_strategy = st.builds(
    c::sharp::classes::ParameterArray,
)
Out_strategy = st.builds(
    Out,
)
Ref_strategy = st.builds(
    Ref,
)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=c::sharp::operators::ExclusiveOr_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::exclusiveor_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::ExclusiveOr)

@given(instance=c::sharp::operators::And_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::and_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::And)

@given(instance=c::sharp::operators::ConditionalOr_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::conditionalor_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::ConditionalOr)

@given(instance=c::sharp::operators::InclusiveOr_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::inclusiveor_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::InclusiveOr)

@given(instance=c::sharp::operators::ConditionalAnd_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::conditionaland_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::ConditionalAnd)

@given(instance=c::sharp::operators::Complement_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::complement_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::Complement)

@given(instance=MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, MultiplicativeOperator)

@given(instance=c::sharp::operators::Remainder_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::remainder_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::Remainder)

@given(instance=c::sharp::operators::Multiplication_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::multiplication_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::Multiplication)

@given(instance=c::sharp::operators::Division_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::division_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::Division)

@given(instance=operators::UnaryOperator_strategy)
@settings(max_examples=50)
def test_operators::unaryoperator_instantiation(instance):
    assert isinstance(instance, operators::UnaryOperator)

@given(instance=operators::AdditiveOperator_strategy)
@settings(max_examples=50)
def test_operators::additiveoperator_instantiation(instance):
    assert isinstance(instance, operators::AdditiveOperator)

@given(instance=c::sharp::operators::Subtraction_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::subtraction_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::Subtraction)

@given(instance=c::sharp::operators::Addition_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::addition_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::Addition)

@given(instance=RelationOperator_strategy)
@settings(max_examples=50)
def test_relationoperator_instantiation(instance):
    assert isinstance(instance, RelationOperator)

@given(instance=c::sharp::operators::LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::lessthanorequal_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::LessThanOrEqual)

@given(instance=c::sharp::operators::GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::greaterthanorequal_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::GreaterThanOrEqual)

@given(instance=c::sharp::operators::LessThan_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::lessthan_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::LessThan)

@given(instance=c::sharp::operators::GreaterThan_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::greaterthan_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::GreaterThan)

@given(instance=EqualityOperator_strategy)
@settings(max_examples=50)
def test_equalityoperator_instantiation(instance):
    assert isinstance(instance, EqualityOperator)

@given(instance=c::sharp::operators::NotEqual_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::notequal_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::NotEqual)

@given(instance=c::sharp::operators::Equal_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::equal_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::Equal)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=c::sharp::operators::UnaryModificationOperator_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::unarymodificationoperator_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::UnaryModificationOperator)

@given(instance=c::sharp::operators::RelationOperator_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::relationoperator_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::RelationOperator)

@given(instance=c::sharp::operators::MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::MultiplicativeOperator)

@given(instance=c::sharp::operators::EqualityOperator_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::equalityoperator_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::EqualityOperator)

@given(instance=c::sharp::operators::UnaryOperator_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::unaryoperator_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::UnaryOperator)

@given(instance=c::sharp::operators::ShiftOperator_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::shiftoperator_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::ShiftOperator)

@given(instance=c::sharp::operators::AssignmentOperator_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::assignmentoperator_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::AssignmentOperator)

@given(instance=c::sharp::operators::AdditiveOperator_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::additiveoperator_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::AdditiveOperator)

@given(instance=c::sharp::operators::Operator_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::operator_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::Operator)

@given(instance=c::sharp::keywords::Event_strategy)
@settings(max_examples=50)
def test_c::sharp::keywords::event_instantiation(instance):
    assert isinstance(instance, c::sharp::keywords::Event)

@given(instance=c::sharp::keywords::Return_strategy)
@settings(max_examples=50)
def test_c::sharp::keywords::return_instantiation(instance):
    assert isinstance(instance, c::sharp::keywords::Return)

@given(instance=c::sharp::keywords::Default_strategy)
@settings(max_examples=50)
def test_c::sharp::keywords::default_instantiation(instance):
    assert isinstance(instance, c::sharp::keywords::Default)

@given(instance=c::sharp::keywords::Case_strategy)
@settings(max_examples=50)
def test_c::sharp::keywords::case_instantiation(instance):
    assert isinstance(instance, c::sharp::keywords::Case)

@given(instance=c::sharp::keywords::Params_strategy)
@settings(max_examples=50)
def test_c::sharp::keywords::params_instantiation(instance):
    assert isinstance(instance, c::sharp::keywords::Params)

@given(instance=c::sharp::keywords::Ref_strategy)
@settings(max_examples=50)
def test_c::sharp::keywords::ref_instantiation(instance):
    assert isinstance(instance, c::sharp::keywords::Ref)

@given(instance=c::sharp::keywords::Out_strategy)
@settings(max_examples=50)
def test_c::sharp::keywords::out_instantiation(instance):
    assert isinstance(instance, c::sharp::keywords::Out)

@given(instance=ShiftOperator_strategy)
@settings(max_examples=50)
def test_shiftoperator_instantiation(instance):
    assert isinstance(instance, ShiftOperator)

@given(instance=c::sharp::operators::UnsignedRightShift_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::unsignedrightshift_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::UnsignedRightShift)

@given(instance=c::sharp::operators::RightShift_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::rightshift_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::RightShift)

@given(instance=c::sharp::operators::LeftShift_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::leftshift_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::LeftShift)

@given(instance=c::sharp::operators::Negate_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::negate_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::Negate)

@given(instance=UnaryModificationOperator_strategy)
@settings(max_examples=50)
def test_unarymodificationoperator_instantiation(instance):
    assert isinstance(instance, UnaryModificationOperator)

@given(instance=c::sharp::operators::PlusPlus_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::plusplus_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::PlusPlus)

@given(instance=c::sharp::operators::MinusMinus_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::minusminus_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::MinusMinus)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=c::sharp::literals::RealLiteral_strategy)
@settings(max_examples=50)
def test_c::sharp::literals::realliteral_instantiation(instance):
    assert isinstance(instance, c::sharp::literals::RealLiteral)

@given(instance=c::sharp::literals::RealLiteral_strategy)
def test_c::sharp::literals::realliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=c::sharp::literals::RealLiteral_strategy)
def test_c::sharp::literals::realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=c::sharp::literals::DecimalIntegerLiteral_strategy)
@settings(max_examples=50)
def test_c::sharp::literals::decimalintegerliteral_instantiation(instance):
    assert isinstance(instance, c::sharp::literals::DecimalIntegerLiteral)

@given(instance=c::sharp::literals::DecimalIntegerLiteral_strategy)
def test_c::sharp::literals::decimalintegerliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=c::sharp::literals::DecimalIntegerLiteral_strategy)
def test_c::sharp::literals::decimalintegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=c::sharp::literals::HexadecimalIntegerLiteral_strategy)
@settings(max_examples=50)
def test_c::sharp::literals::hexadecimalintegerliteral_instantiation(instance):
    assert isinstance(instance, c::sharp::literals::HexadecimalIntegerLiteral)

@given(instance=c::sharp::literals::HexadecimalIntegerLiteral_strategy)
def test_c::sharp::literals::hexadecimalintegerliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=c::sharp::literals::HexadecimalIntegerLiteral_strategy)
def test_c::sharp::literals::hexadecimalintegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=c::sharp::literals::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_c::sharp::literals::booleanliteral_instantiation(instance):
    assert isinstance(instance, c::sharp::literals::BooleanLiteral)

@given(instance=c::sharp::literals::BooleanLiteral_strategy)
def test_c::sharp::literals::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=c::sharp::literals::BooleanLiteral_strategy)
def test_c::sharp::literals::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=c::sharp::modifiers::Modifier_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::modifier_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::Modifier)

@given(instance=ReferenceType_strategy)
@settings(max_examples=50)
def test_referencetype_instantiation(instance):
    assert isinstance(instance, ReferenceType)

@given(instance=c::sharp::types::ClassOrInterfaceOrDelegateOrEnumType_strategy)
@settings(max_examples=50)
def test_c::sharp::types::classorinterfaceordelegateorenumtype_instantiation(instance):
    assert isinstance(instance, c::sharp::types::ClassOrInterfaceOrDelegateOrEnumType)

@given(instance=c::sharp::literals::StringLiteral_strategy)
@settings(max_examples=50)
def test_c::sharp::literals::stringliteral_instantiation(instance):
    assert isinstance(instance, c::sharp::literals::StringLiteral)

@given(instance=c::sharp::literals::StringLiteral_strategy)
def test_c::sharp::literals::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=c::sharp::literals::StringLiteral_strategy)
def test_c::sharp::literals::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=c::sharp::literals::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_c::sharp::literals::characterliteral_instantiation(instance):
    assert isinstance(instance, c::sharp::literals::CharacterLiteral)

@given(instance=c::sharp::literals::CharacterLiteral_strategy)
def test_c::sharp::literals::characterliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=c::sharp::literals::CharacterLiteral_strategy)
def test_c::sharp::literals::characterliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=c::sharp::literals::This_strategy)
@settings(max_examples=50)
def test_c::sharp::literals::this_instantiation(instance):
    assert isinstance(instance, c::sharp::literals::This)

@given(instance=c::sharp::literals::NullLiteral_strategy)
@settings(max_examples=50)
def test_c::sharp::literals::nullliteral_instantiation(instance):
    assert isinstance(instance, c::sharp::literals::NullLiteral)

@given(instance=types::Type_strategy)
@settings(max_examples=50)
def test_types::type_instantiation(instance):
    assert isinstance(instance, types::Type)

@given(instance=types::NonArrayType_strategy)
@settings(max_examples=50)
def test_types::nonarraytype_instantiation(instance):
    assert isinstance(instance, types::NonArrayType)

@given(instance=c::sharp::types::SimpleType_strategy)
@settings(max_examples=50)
def test_c::sharp::types::simpletype_instantiation(instance):
    assert isinstance(instance, c::sharp::types::SimpleType)

@given(instance=c::sharp::types::PointerType_strategy)
@settings(max_examples=50)
def test_c::sharp::types::pointertype_instantiation(instance):
    assert isinstance(instance, c::sharp::types::PointerType)

@given(instance=c::sharp::types::ReferenceType_strategy)
@settings(max_examples=50)
def test_c::sharp::types::referencetype_instantiation(instance):
    assert isinstance(instance, c::sharp::types::ReferenceType)

@given(instance=c::sharp::types::NonArrayType_strategy)
@settings(max_examples=50)
def test_c::sharp::types::nonarraytype_instantiation(instance):
    assert isinstance(instance, c::sharp::types::NonArrayType)

@given(instance=c::sharp::types::Type_strategy)
@settings(max_examples=50)
def test_c::sharp::types::type_instantiation(instance):
    assert isinstance(instance, c::sharp::types::Type)

@given(instance=ConditionalOr_strategy)
@settings(max_examples=50)
def test_conditionalor_instantiation(instance):
    assert isinstance(instance, ConditionalOr)

@given(instance=ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, ConditionalAndExpression)

@given(instance=c::sharp::expressions::ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::conditionalorexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::ConditionalOrExpression)

@given(instance=ConditionalAnd_strategy)
@settings(max_examples=50)
def test_conditionaland_instantiation(instance):
    assert isinstance(instance, ConditionalAnd)

@given(instance=InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, InclusiveOrExpression)

@given(instance=c::sharp::expressions::ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::conditionalandexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::ConditionalAndExpression)

@given(instance=InclusiveOr_strategy)
@settings(max_examples=50)
def test_inclusiveor_instantiation(instance):
    assert isinstance(instance, InclusiveOr)

@given(instance=ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, ExclusiveOrExpression)

@given(instance=c::sharp::expressions::InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::InclusiveOrExpression)

@given(instance=ExclusiveOr_strategy)
@settings(max_examples=50)
def test_exclusiveor_instantiation(instance):
    assert isinstance(instance, ExclusiveOr)

@given(instance=AndExpression_strategy)
@settings(max_examples=50)
def test_andexpression_instantiation(instance):
    assert isinstance(instance, AndExpression)

@given(instance=c::sharp::expressions::ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::ExclusiveOrExpression)

@given(instance=And_strategy)
@settings(max_examples=50)
def test_and_instantiation(instance):
    assert isinstance(instance, And)

@given(instance=EqualityExpression_strategy)
@settings(max_examples=50)
def test_equalityexpression_instantiation(instance):
    assert isinstance(instance, EqualityExpression)

@given(instance=c::sharp::expressions::AndExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::andexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::AndExpression)

@given(instance=NotEqual_strategy)
@settings(max_examples=50)
def test_notequal_instantiation(instance):
    assert isinstance(instance, NotEqual)

@given(instance=Equal_strategy)
@settings(max_examples=50)
def test_equal_instantiation(instance):
    assert isinstance(instance, Equal)

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

@given(instance=c::sharp::expressions::RelationalExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::relationalexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::RelationalExpression)

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

@given(instance=c::sharp::expressions::ShiftExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::shiftexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::ShiftExpression)

@given(instance=MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, MultiplicativeExpression)

@given(instance=c::sharp::expressions::AdditiveExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::additiveexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::AdditiveExpression)

@given(instance=Remainder_strategy)
@settings(max_examples=50)
def test_remainder_instantiation(instance):
    assert isinstance(instance, Remainder)

@given(instance=Division_strategy)
@settings(max_examples=50)
def test_division_instantiation(instance):
    assert isinstance(instance, Division)

@given(instance=c::sharp::expressions::MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::MultiplicativeExpression)

@given(instance=c::sharp::expressions::AddressOfExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::addressofexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::AddressOfExpression)

@given(instance=RelationalExpression_strategy)
@settings(max_examples=50)
def test_relationalexpression_instantiation(instance):
    assert isinstance(instance, RelationalExpression)

@given(instance=c::sharp::expressions::EqualityExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::equalityexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::EqualityExpression)

@given(instance=GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_greaterthanorequal_instantiation(instance):
    assert isinstance(instance, GreaterThanOrEqual)

@given(instance=GreaterThan_strategy)
@settings(max_examples=50)
def test_greaterthan_instantiation(instance):
    assert isinstance(instance, GreaterThan)

@given(instance=c::sharp::classes::FixedParameter_strategy)
@settings(max_examples=50)
def test_c::sharp::classes::fixedparameter_instantiation(instance):
    assert isinstance(instance, c::sharp::classes::FixedParameter)

@given(instance=ParameterArray_strategy)
@settings(max_examples=50)
def test_parameterarray_instantiation(instance):
    assert isinstance(instance, ParameterArray)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=VariableInitializer_strategy)
@settings(max_examples=50)
def test_variableinitializer_instantiation(instance):
    assert isinstance(instance, VariableInitializer)

@given(instance=c::sharp::arrays::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_c::sharp::arrays::arrayinitializer_instantiation(instance):
    assert isinstance(instance, c::sharp::arrays::ArrayInitializer)

@given(instance=c::sharp::arrays::StackallocInitializer_strategy)
@settings(max_examples=50)
def test_c::sharp::arrays::stackallocinitializer_instantiation(instance):
    assert isinstance(instance, c::sharp::arrays::StackallocInitializer)

@given(instance=VariableDeclarator_strategy)
@settings(max_examples=50)
def test_variabledeclarator_instantiation(instance):
    assert isinstance(instance, VariableDeclarator)

@given(instance=ConstantDeclarator_strategy)
@settings(max_examples=50)
def test_constantdeclarator_instantiation(instance):
    assert isinstance(instance, ConstantDeclarator)

@given(instance=c::sharp::classes::VariableInitializer_strategy)
@settings(max_examples=50)
def test_c::sharp::classes::variableinitializer_instantiation(instance):
    assert isinstance(instance, c::sharp::classes::VariableInitializer)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=c::sharp::classes::Block_strategy)
@settings(max_examples=50)
def test_c::sharp::classes::block_instantiation(instance):
    assert isinstance(instance, c::sharp::classes::Block)

@given(instance=classes::ClassMemberDeclaration_strategy)
@settings(max_examples=50)
def test_classes::classmemberdeclaration_instantiation(instance):
    assert isinstance(instance, classes::ClassMemberDeclaration)

@given(instance=namespaces::NamespaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_namespaces::namespacememberdeclaration_instantiation(instance):
    assert isinstance(instance, namespaces::NamespaceMemberDeclaration)

@given(instance=c::sharp::namespaces::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_c::sharp::namespaces::typedeclaration_instantiation(instance):
    assert isinstance(instance, c::sharp::namespaces::TypeDeclaration)

@given(instance=c::sharp::namespaces::NamespaceBody_strategy)
@settings(max_examples=50)
def test_c::sharp::namespaces::namespacebody_instantiation(instance):
    assert isinstance(instance, c::sharp::namespaces::NamespaceBody)

@given(instance=NamespaceBody_strategy)
@settings(max_examples=50)
def test_namespacebody_instantiation(instance):
    assert isinstance(instance, NamespaceBody)

@given(instance=c::sharp::namespaces::NamespaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_c::sharp::namespaces::namespacememberdeclaration_instantiation(instance):
    assert isinstance(instance, c::sharp::namespaces::NamespaceMemberDeclaration)

@given(instance=NamespaceOrTypeName_strategy)
@settings(max_examples=50)
def test_namespaceortypename_instantiation(instance):
    assert isinstance(instance, NamespaceOrTypeName)

@given(instance=FixedParameter_strategy)
@settings(max_examples=50)
def test_fixedparameter_instantiation(instance):
    assert isinstance(instance, FixedParameter)

@given(instance=c::sharp::classes::FormalParameterList_strategy)
@settings(max_examples=50)
def test_c::sharp::classes::formalparameterlist_instantiation(instance):
    assert isinstance(instance, c::sharp::classes::FormalParameterList)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=FormalParameterList_strategy)
@settings(max_examples=50)
def test_formalparameterlist_instantiation(instance):
    assert isinstance(instance, FormalParameterList)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=c::sharp::classes::ClassMemberDeclaration_strategy)
@settings(max_examples=50)
def test_c::sharp::classes::classmemberdeclaration_instantiation(instance):
    assert isinstance(instance, c::sharp::classes::ClassMemberDeclaration)

@given(instance=ClassOrInterfaceOrDelegateOrEnumType_strategy)
@settings(max_examples=50)
def test_classorinterfaceordelegateorenumtype_instantiation(instance):
    assert isinstance(instance, ClassOrInterfaceOrDelegateOrEnumType)

@given(instance=c::sharp::classes::ClassBase_strategy)
@settings(max_examples=50)
def test_c::sharp::classes::classbase_instantiation(instance):
    assert isinstance(instance, c::sharp::classes::ClassBase)

@given(instance=ClassMemberDeclaration_strategy)
@settings(max_examples=50)
def test_classmemberdeclaration_instantiation(instance):
    assert isinstance(instance, ClassMemberDeclaration)

@given(instance=c::sharp::classes::ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_c::sharp::classes::constantdeclaration_instantiation(instance):
    assert isinstance(instance, c::sharp::classes::ConstantDeclaration)

@given(instance=c::sharp::classes::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_c::sharp::classes::fielddeclaration_instantiation(instance):
    assert isinstance(instance, c::sharp::classes::FieldDeclaration)

@given(instance=ClassBase_strategy)
@settings(max_examples=50)
def test_classbase_instantiation(instance):
    assert isinstance(instance, ClassBase)

@given(instance=Modifier_strategy)
@settings(max_examples=50)
def test_modifier_instantiation(instance):
    assert isinstance(instance, Modifier)

@given(instance=c::sharp::modifiers::ReadOnly_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::readonly_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::ReadOnly)

@given(instance=c::sharp::modifiers::Partial_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::partial_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::Partial)

@given(instance=c::sharp::modifiers::Protected_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::protected_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::Protected)

@given(instance=c::sharp::modifiers::Unsafe_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::unsafe_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::Unsafe)

@given(instance=c::sharp::modifiers::Sealed_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::sealed_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::Sealed)

@given(instance=c::sharp::modifiers::Abstract_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::abstract_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::Abstract)

@given(instance=c::sharp::modifiers::Static_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::static_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::Static)

@given(instance=c::sharp::modifiers::Private_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::private_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::Private)

@given(instance=c::sharp::modifiers::Internal_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::internal_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::Internal)

@given(instance=c::sharp::modifiers::Volatile_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::volatile_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::Volatile)

@given(instance=c::sharp::modifiers::Public_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::public_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::Public)

@given(instance=c::sharp::modifiers::OverrideModifier_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::overridemodifier_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::OverrideModifier)

@given(instance=c::sharp::modifiers::New_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::new_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::New)

@given(instance=c::sharp::modifiers::Extern_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::extern_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::Extern)

@given(instance=c::sharp::modifiers::Virtual_strategy)
@settings(max_examples=50)
def test_c::sharp::modifiers::virtual_instantiation(instance):
    assert isinstance(instance, c::sharp::modifiers::Virtual)

@given(instance=Attributes_strategy)
@settings(max_examples=50)
def test_attributes_instantiation(instance):
    assert isinstance(instance, Attributes)

@given(instance=namespaces::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_namespaces::typedeclaration_instantiation(instance):
    assert isinstance(instance, namespaces::TypeDeclaration)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=c::sharp::namespaces::UsingDirective_strategy)
@settings(max_examples=50)
def test_c::sharp::namespaces::usingdirective_instantiation(instance):
    assert isinstance(instance, c::sharp::namespaces::UsingDirective)

@given(instance=NamespaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_namespacememberdeclaration_instantiation(instance):
    assert isinstance(instance, NamespaceMemberDeclaration)

@given(instance=c::sharp::namespaces::Namespace_strategy)
@settings(max_examples=50)
def test_c::sharp::namespaces::namespace_instantiation(instance):
    assert isinstance(instance, c::sharp::namespaces::Namespace)

@given(instance=GlobalAttributes_strategy)
@settings(max_examples=50)
def test_globalattributes_instantiation(instance):
    assert isinstance(instance, GlobalAttributes)

@given(instance=UsingDirective_strategy)
@settings(max_examples=50)
def test_usingdirective_instantiation(instance):
    assert isinstance(instance, UsingDirective)

@given(instance=c::sharp::namespaces::CompilationUnit_strategy)
@settings(max_examples=50)
def test_c::sharp::namespaces::compilationunit_instantiation(instance):
    assert isinstance(instance, c::sharp::namespaces::CompilationUnit)

@given(instance=expressions::PrimaryNoArrayCreationExpression_strategy)
@settings(max_examples=50)
def test_expressions::primarynoarraycreationexpression_instantiation(instance):
    assert isinstance(instance, expressions::PrimaryNoArrayCreationExpression)

@given(instance=common::NamedElement_strategy)
@settings(max_examples=50)
def test_common::namedelement_instantiation(instance):
    assert isinstance(instance, common::NamedElement)

@given(instance=c::sharp::classes::Method_strategy)
@settings(max_examples=50)
def test_c::sharp::classes::method_instantiation(instance):
    assert isinstance(instance, c::sharp::classes::Method)

@given(instance=c::sharp::classes::Class_strategy)
@settings(max_examples=50)
def test_c::sharp::classes::class_instantiation(instance):
    assert isinstance(instance, c::sharp::classes::Class)

@given(instance=c::sharp::common::Identifier_strategy)
@settings(max_examples=50)
def test_c::sharp::common::identifier_instantiation(instance):
    assert isinstance(instance, c::sharp::common::Identifier)

@given(instance=Identifier_strategy)
@settings(max_examples=50)
def test_identifier_instantiation(instance):
    assert isinstance(instance, Identifier)

@given(instance=c::sharp::common::NamespaceOrTypeName_strategy)
@settings(max_examples=50)
def test_c::sharp::common::namespaceortypename_instantiation(instance):
    assert isinstance(instance, c::sharp::common::NamespaceOrTypeName)

@given(instance=c::sharp::common::NamedElement_strategy)
@settings(max_examples=50)
def test_c::sharp::common::namedelement_instantiation(instance):
    assert isinstance(instance, c::sharp::common::NamedElement)

@given(instance=c::sharp::common::NamedElement_strategy)
def test_c::sharp::common::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=c::sharp::common::NamedElement_strategy)
def test_c::sharp::common::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AssignmentOperator_strategy)
@settings(max_examples=50)
def test_assignmentoperator_instantiation(instance):
    assert isinstance(instance, AssignmentOperator)

@given(instance=c::sharp::operators::AssignmentMinus_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::assignmentminus_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::AssignmentMinus)

@given(instance=c::sharp::operators::AssignmentRightShift_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::assignmentrightshift_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::AssignmentRightShift)

@given(instance=c::sharp::operators::AssignmentOr_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::assignmentor_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::AssignmentOr)

@given(instance=c::sharp::operators::Assignment_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::assignment_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::Assignment)

@given(instance=c::sharp::operators::AssignmentAnd_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::assignmentand_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::AssignmentAnd)

@given(instance=c::sharp::operators::AssignmentModulo_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::assignmentmodulo_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::AssignmentModulo)

@given(instance=c::sharp::operators::AssignmentPlus_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::assignmentplus_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::AssignmentPlus)

@given(instance=c::sharp::operators::AssignmentDivision_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::assignmentdivision_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::AssignmentDivision)

@given(instance=c::sharp::operators::AssignmentMultiplication_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::assignmentmultiplication_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::AssignmentMultiplication)

@given(instance=c::sharp::operators::AssignmentLeftShift_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::assignmentleftshift_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::AssignmentLeftShift)

@given(instance=c::sharp::operators::AssignmentExclusiveOr_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::assignmentexclusiveor_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::AssignmentExclusiveOr)

@given(instance=c::sharp::operators::AssignmentUnsignedRightShift_strategy)
@settings(max_examples=50)
def test_c::sharp::operators::assignmentunsignedrightshift_instantiation(instance):
    assert isinstance(instance, c::sharp::operators::AssignmentUnsignedRightShift)

@given(instance=expressions::Expression_strategy)
@settings(max_examples=50)
def test_expressions::expression_instantiation(instance):
    assert isinstance(instance, expressions::Expression)

@given(instance=ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, ConditionalOrExpression)

@given(instance=c::sharp::expressions::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::conditionalexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::ConditionalExpression)

@given(instance=AddressOfExpression_strategy)
@settings(max_examples=50)
def test_addressofexpression_instantiation(instance):
    assert isinstance(instance, AddressOfExpression)

@given(instance=c::sharp::expressions::CastExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::castexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::CastExpression)

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

@given(instance=c::sharp::expressions::UnaryExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::unaryexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::UnaryExpression)

@given(instance=ArrayInitializer_strategy)
@settings(max_examples=50)
def test_arrayinitializer_instantiation(instance):
    assert isinstance(instance, ArrayInitializer)

@given(instance=CastExpression_strategy)
@settings(max_examples=50)
def test_castexpression_instantiation(instance):
    assert isinstance(instance, CastExpression)

@given(instance=PreDecrementExpression_strategy)
@settings(max_examples=50)
def test_predecrementexpression_instantiation(instance):
    assert isinstance(instance, PreDecrementExpression)

@given(instance=PreIncrementExpression_strategy)
@settings(max_examples=50)
def test_preincrementexpression_instantiation(instance):
    assert isinstance(instance, PreIncrementExpression)

@given(instance=ArgumentList_strategy)
@settings(max_examples=50)
def test_argumentlist_instantiation(instance):
    assert isinstance(instance, ArgumentList)

@given(instance=expressions::StatementExpression_strategy)
@settings(max_examples=50)
def test_expressions::statementexpression_instantiation(instance):
    assert isinstance(instance, expressions::StatementExpression)

@given(instance=c::sharp::expressions::ObjectCreationExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::objectcreationexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::ObjectCreationExpression)

@given(instance=c::sharp::expressions::AssignmentExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::assignmentexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::AssignmentExpression)

@given(instance=expressions::PrimaryExtendedExpressionType_strategy)
@settings(max_examples=50)
def test_expressions::primaryextendedexpressiontype_instantiation(instance):
    assert isinstance(instance, expressions::PrimaryExtendedExpressionType)

@given(instance=c::sharp::expressions::PostDecrementExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::postdecrementexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::PostDecrementExpression)

@given(instance=c::sharp::expressions::PostIncrementExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::postincrementexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::PostIncrementExpression)

@given(instance=c::sharp::expressions::InvocationExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::invocationexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::InvocationExpression)

@given(instance=SimpleType_strategy)
@settings(max_examples=50)
def test_simpletype_instantiation(instance):
    assert isinstance(instance, SimpleType)

@given(instance=c::sharp::types::Object_strategy)
@settings(max_examples=50)
def test_c::sharp::types::object_instantiation(instance):
    assert isinstance(instance, c::sharp::types::Object)

@given(instance=c::sharp::types::Short_strategy)
@settings(max_examples=50)
def test_c::sharp::types::short_instantiation(instance):
    assert isinstance(instance, c::sharp::types::Short)

@given(instance=c::sharp::types::Char_strategy)
@settings(max_examples=50)
def test_c::sharp::types::char_instantiation(instance):
    assert isinstance(instance, c::sharp::types::Char)

@given(instance=c::sharp::types::UInt_strategy)
@settings(max_examples=50)
def test_c::sharp::types::uint_instantiation(instance):
    assert isinstance(instance, c::sharp::types::UInt)

@given(instance=c::sharp::types::Int_strategy)
@settings(max_examples=50)
def test_c::sharp::types::int_instantiation(instance):
    assert isinstance(instance, c::sharp::types::Int)

@given(instance=c::sharp::types::Byte_strategy)
@settings(max_examples=50)
def test_c::sharp::types::byte_instantiation(instance):
    assert isinstance(instance, c::sharp::types::Byte)

@given(instance=c::sharp::types::SByte_strategy)
@settings(max_examples=50)
def test_c::sharp::types::sbyte_instantiation(instance):
    assert isinstance(instance, c::sharp::types::SByte)

@given(instance=c::sharp::types::ULong_strategy)
@settings(max_examples=50)
def test_c::sharp::types::ulong_instantiation(instance):
    assert isinstance(instance, c::sharp::types::ULong)

@given(instance=c::sharp::types::Long_strategy)
@settings(max_examples=50)
def test_c::sharp::types::long_instantiation(instance):
    assert isinstance(instance, c::sharp::types::Long)

@given(instance=c::sharp::types::Double_strategy)
@settings(max_examples=50)
def test_c::sharp::types::double_instantiation(instance):
    assert isinstance(instance, c::sharp::types::Double)

@given(instance=c::sharp::types::Decimal_strategy)
@settings(max_examples=50)
def test_c::sharp::types::decimal_instantiation(instance):
    assert isinstance(instance, c::sharp::types::Decimal)

@given(instance=c::sharp::types::Bool_strategy)
@settings(max_examples=50)
def test_c::sharp::types::bool_instantiation(instance):
    assert isinstance(instance, c::sharp::types::Bool)

@given(instance=c::sharp::types::UShort_strategy)
@settings(max_examples=50)
def test_c::sharp::types::ushort_instantiation(instance):
    assert isinstance(instance, c::sharp::types::UShort)

@given(instance=c::sharp::types::Float_strategy)
@settings(max_examples=50)
def test_c::sharp::types::float_instantiation(instance):
    assert isinstance(instance, c::sharp::types::Float)

@given(instance=c::sharp::types::Void_strategy)
@settings(max_examples=50)
def test_c::sharp::types::void_instantiation(instance):
    assert isinstance(instance, c::sharp::types::Void)

@given(instance=c::sharp::types::String_strategy)
@settings(max_examples=50)
def test_c::sharp::types::string_instantiation(instance):
    assert isinstance(instance, c::sharp::types::String)

@given(instance=PrimaryExtendedExpressionType_strategy)
@settings(max_examples=50)
def test_primaryextendedexpressiontype_instantiation(instance):
    assert isinstance(instance, PrimaryExtendedExpressionType)

@given(instance=c::sharp::expressions::ElementAccess_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::elementaccess_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::ElementAccess)

@given(instance=c::sharp::expressions::PointerMemberAccess_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::pointermemberaccess_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::PointerMemberAccess)

@given(instance=c::sharp::expressions::MemberAccess_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::memberaccess_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::MemberAccess)

@given(instance=c::sharp::expressions::PrimaryExtendedExpressionType_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::primaryextendedexpressiontype_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::PrimaryExtendedExpressionType)

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=c::sharp::expressions::ArrayCreationExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::arraycreationexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::ArrayCreationExpression)

@given(instance=c::sharp::expressions::PrimaryNoArrayCreationExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::primarynoarraycreationexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::PrimaryNoArrayCreationExpression)

@given(instance=c::sharp::expressions::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::primaryexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::PrimaryExpression)

@given(instance=Argument_strategy)
@settings(max_examples=50)
def test_argument_instantiation(instance):
    assert isinstance(instance, Argument)

@given(instance=c::sharp::expressions::ArgumentList_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::argumentlist_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::ArgumentList)

@given(instance=c::sharp::expressions::Argument_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::argument_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::Argument)

@given(instance=c::sharp::expressions::ExpressionList_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::expressionlist_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::ExpressionList)

@given(instance=classes::VariableInitializer_strategy)
@settings(max_examples=50)
def test_classes::variableinitializer_instantiation(instance):
    assert isinstance(instance, classes::VariableInitializer)

@given(instance=PrimaryNoArrayCreationExpression_strategy)
@settings(max_examples=50)
def test_primarynoarraycreationexpression_instantiation(instance):
    assert isinstance(instance, PrimaryNoArrayCreationExpression)

@given(instance=c::sharp::expressions::CheckedExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::checkedexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::CheckedExpression)

@given(instance=c::sharp::expressions::SizeOfExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::sizeofexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::SizeOfExpression)

@given(instance=c::sharp::expressions::UncheckedExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::uncheckedexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::UncheckedExpression)

@given(instance=c::sharp::expressions::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::ParenthesizedExpression)

@given(instance=c::sharp::expressions::DelegateCreationExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::delegatecreationexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::DelegateCreationExpression)

@given(instance=c::sharp::expressions::TypeOfExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::typeofexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::TypeOfExpression)

@given(instance=c::sharp::literals::Literal_strategy)
@settings(max_examples=50)
def test_c::sharp::literals::literal_instantiation(instance):
    assert isinstance(instance, c::sharp::literals::Literal)

@given(instance=c::sharp::expressions::BaseAccess_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::baseaccess_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::BaseAccess)

@given(instance=c::sharp::statements::ConstantDeclarator_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::constantdeclarator_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::ConstantDeclarator)

@given(instance=c::sharp::statements::LocalConstantDeclaration_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::localconstantdeclaration_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::LocalConstantDeclaration)

@given(instance=c::sharp::statements::VariableDeclarator_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::variabledeclarator_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::VariableDeclarator)

@given(instance=c::sharp::expressions::StatementExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::statementexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::StatementExpression)

@given(instance=statements::ResourceAcquisition_strategy)
@settings(max_examples=50)
def test_statements::resourceacquisition_instantiation(instance):
    assert isinstance(instance, statements::ResourceAcquisition)

@given(instance=c::sharp::expressions::Expression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::expression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::Expression)

@given(instance=statements::ForInitializer_strategy)
@settings(max_examples=50)
def test_statements::forinitializer_instantiation(instance):
    assert isinstance(instance, statements::ForInitializer)

@given(instance=c::sharp::statements::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::variabledeclaration_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::VariableDeclaration)

@given(instance=c::sharp::statements::FixedPointerDeclarator_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::fixedpointerdeclarator_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::FixedPointerDeclarator)

@given(instance=FixedPointerDeclarator_strategy)
@settings(max_examples=50)
def test_fixedpointerdeclarator_instantiation(instance):
    assert isinstance(instance, FixedPointerDeclarator)

@given(instance=PointerType_strategy)
@settings(max_examples=50)
def test_pointertype_instantiation(instance):
    assert isinstance(instance, PointerType)

@given(instance=c::sharp::statements::FinallyClause_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::finallyclause_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::FinallyClause)

@given(instance=c::sharp::statements::GeneralCatchClause_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::generalcatchclause_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::GeneralCatchClause)

@given(instance=c::sharp::statements::SpecificCatchClause_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::specificcatchclause_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::SpecificCatchClause)

@given(instance=FinallyClause_strategy)
@settings(max_examples=50)
def test_finallyclause_instantiation(instance):
    assert isinstance(instance, FinallyClause)

@given(instance=ResourceAcquisition_strategy)
@settings(max_examples=50)
def test_resourceacquisition_instantiation(instance):
    assert isinstance(instance, ResourceAcquisition)

@given(instance=c::sharp::statements::ResourceAcquisition_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::resourceacquisition_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::ResourceAcquisition)

@given(instance=JumpStatement_strategy)
@settings(max_examples=50)
def test_jumpstatement_instantiation(instance):
    assert isinstance(instance, JumpStatement)

@given(instance=c::sharp::statements::ThrowStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::throwstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::ThrowStatement)

@given(instance=c::sharp::statements::ReturnStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::returnstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::ReturnStatement)

@given(instance=c::sharp::statements::ContinueStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::continuestatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::ContinueStatement)

@given(instance=c::sharp::statements::GotoStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::gotostatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::GotoStatement)

@given(instance=c::sharp::statements::BreakStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::breakstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::BreakStatement)

@given(instance=c::sharp::statements::ForInitializer_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::forinitializer_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::ForInitializer)

@given(instance=GeneralCatchClause_strategy)
@settings(max_examples=50)
def test_generalcatchclause_instantiation(instance):
    assert isinstance(instance, GeneralCatchClause)

@given(instance=SpecificCatchClause_strategy)
@settings(max_examples=50)
def test_specificcatchclause_instantiation(instance):
    assert isinstance(instance, SpecificCatchClause)

@given(instance=ForInitializer_strategy)
@settings(max_examples=50)
def test_forinitializer_instantiation(instance):
    assert isinstance(instance, ForInitializer)

@given(instance=c::sharp::expressions::StatementExpressionList_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::statementexpressionlist_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::StatementExpressionList)

@given(instance=IterationStatement_strategy)
@settings(max_examples=50)
def test_iterationstatement_instantiation(instance):
    assert isinstance(instance, IterationStatement)

@given(instance=c::sharp::statements::ForeachStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::foreachstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::ForeachStatement)

@given(instance=c::sharp::statements::ForStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::forstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::ForStatement)

@given(instance=c::sharp::statements::DoStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::dostatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::DoStatement)

@given(instance=c::sharp::statements::WhileStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::whilestatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::WhileStatement)

@given(instance=Case_strategy)
@settings(max_examples=50)
def test_case_instantiation(instance):
    assert isinstance(instance, Case)

@given(instance=Default_strategy)
@settings(max_examples=50)
def test_default_instantiation(instance):
    assert isinstance(instance, Default)

@given(instance=c::sharp::statements::SwitchLabel_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::switchlabel_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::SwitchLabel)

@given(instance=SwitchLabel_strategy)
@settings(max_examples=50)
def test_switchlabel_instantiation(instance):
    assert isinstance(instance, SwitchLabel)

@given(instance=c::sharp::statements::SwitchSection_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::switchsection_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::SwitchSection)

@given(instance=SwitchSection_strategy)
@settings(max_examples=50)
def test_switchsection_instantiation(instance):
    assert isinstance(instance, SwitchSection)

@given(instance=Unsafe_strategy)
@settings(max_examples=50)
def test_unsafe_instantiation(instance):
    assert isinstance(instance, Unsafe)

@given(instance=EmbeddedStatement_strategy)
@settings(max_examples=50)
def test_embeddedstatement_instantiation(instance):
    assert isinstance(instance, EmbeddedStatement)

@given(instance=c::sharp::statements::LockStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::lockstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::LockStatement)

@given(instance=c::sharp::statements::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::expressionstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::ExpressionStatement)

@given(instance=c::sharp::statements::UsingStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::usingstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::UsingStatement)

@given(instance=c::sharp::statements::UncheckedStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::uncheckedstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::UncheckedStatement)

@given(instance=c::sharp::statements::CheckedStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::checkedstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::CheckedStatement)

@given(instance=c::sharp::statements::EmptyStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::emptystatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::EmptyStatement)

@given(instance=c::sharp::statements::JumpStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::jumpstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::JumpStatement)

@given(instance=c::sharp::statements::FixedStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::fixedstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::FixedStatement)

@given(instance=c::sharp::statements::IterationStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::iterationstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::IterationStatement)

@given(instance=c::sharp::statements::TryStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::trystatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::TryStatement)

@given(instance=c::sharp::statements::SimpleEmbeddedStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::simpleembeddedstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::SimpleEmbeddedStatement)

@given(instance=c::sharp::statements::EmbeddedStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::embeddedstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::EmbeddedStatement)

@given(instance=LocalConstantDeclaration_strategy)
@settings(max_examples=50)
def test_localconstantdeclaration_instantiation(instance):
    assert isinstance(instance, LocalConstantDeclaration)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=c::sharp::statements::DeclarationStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::declarationstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::DeclarationStatement)

@given(instance=StatementExpressionList_strategy)
@settings(max_examples=50)
def test_statementexpressionlist_instantiation(instance):
    assert isinstance(instance, StatementExpressionList)

@given(instance=SelectionStatement_strategy)
@settings(max_examples=50)
def test_selectionstatement_instantiation(instance):
    assert isinstance(instance, SelectionStatement)

@given(instance=c::sharp::statements::SwitchStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::switchstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::SwitchStatement)

@given(instance=c::sharp::statements::IfStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::ifstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::IfStatement)

@given(instance=c::sharp::statements::SelectionStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::selectionstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::SelectionStatement)

@given(instance=StatementExpression_strategy)
@settings(max_examples=50)
def test_statementexpression_instantiation(instance):
    assert isinstance(instance, StatementExpression)

@given(instance=c::sharp::expressions::PreDecrementExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::predecrementexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::PreDecrementExpression)

@given(instance=c::sharp::expressions::PreIncrementExpression_strategy)
@settings(max_examples=50)
def test_c::sharp::expressions::preincrementexpression_instantiation(instance):
    assert isinstance(instance, c::sharp::expressions::PreIncrementExpression)

@given(instance=c::sharp::attributes::Attributes_strategy)
@settings(max_examples=50)
def test_c::sharp::attributes::attributes_instantiation(instance):
    assert isinstance(instance, c::sharp::attributes::Attributes)

@given(instance=c::sharp::attributes::GlobalAttributeTarget_strategy)
@settings(max_examples=50)
def test_c::sharp::attributes::globalattributetarget_instantiation(instance):
    assert isinstance(instance, c::sharp::attributes::GlobalAttributeTarget)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=GlobalAttributeTarget_strategy)
@settings(max_examples=50)
def test_globalattributetarget_instantiation(instance):
    assert isinstance(instance, GlobalAttributeTarget)

@given(instance=c::sharp::attributes::GlobalAttributes_strategy)
@settings(max_examples=50)
def test_c::sharp::attributes::globalattributes_instantiation(instance):
    assert isinstance(instance, c::sharp::attributes::GlobalAttributes)

@given(instance=c::sharp::arrays::RankSpecifier_strategy)
@settings(max_examples=50)
def test_c::sharp::arrays::rankspecifier_instantiation(instance):
    assert isinstance(instance, c::sharp::arrays::RankSpecifier)

@given(instance=RankSpecifier_strategy)
@settings(max_examples=50)
def test_rankspecifier_instantiation(instance):
    assert isinstance(instance, RankSpecifier)

@given(instance=NonArrayType_strategy)
@settings(max_examples=50)
def test_nonarraytype_instantiation(instance):
    assert isinstance(instance, NonArrayType)

@given(instance=c::sharp::arrays::ArrayType_strategy)
@settings(max_examples=50)
def test_c::sharp::arrays::arraytype_instantiation(instance):
    assert isinstance(instance, c::sharp::arrays::ArrayType)

@given(instance=statements::Statement_strategy)
@settings(max_examples=50)
def test_statements::statement_instantiation(instance):
    assert isinstance(instance, statements::Statement)

@given(instance=c::sharp::statements::LabeledStatement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::labeledstatement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::LabeledStatement)

@given(instance=c::sharp::statements::Statement_strategy)
@settings(max_examples=50)
def test_c::sharp::statements::statement_instantiation(instance):
    assert isinstance(instance, c::sharp::statements::Statement)

@given(instance=c::sharp::attributes::NamedArgument_strategy)
@settings(max_examples=50)
def test_c::sharp::attributes::namedargument_instantiation(instance):
    assert isinstance(instance, c::sharp::attributes::NamedArgument)

@given(instance=NamedArgument_strategy)
@settings(max_examples=50)
def test_namedargument_instantiation(instance):
    assert isinstance(instance, NamedArgument)

@given(instance=c::sharp::attributes::NamedArgumentList_strategy)
@settings(max_examples=50)
def test_c::sharp::attributes::namedargumentlist_instantiation(instance):
    assert isinstance(instance, c::sharp::attributes::NamedArgumentList)

@given(instance=NamedArgumentList_strategy)
@settings(max_examples=50)
def test_namedargumentlist_instantiation(instance):
    assert isinstance(instance, NamedArgumentList)

@given(instance=ExpressionList_strategy)
@settings(max_examples=50)
def test_expressionlist_instantiation(instance):
    assert isinstance(instance, ExpressionList)

@given(instance=c::sharp::attributes::AttributeArguments_strategy)
@settings(max_examples=50)
def test_c::sharp::attributes::attributearguments_instantiation(instance):
    assert isinstance(instance, c::sharp::attributes::AttributeArguments)

@given(instance=AttributeArguments_strategy)
@settings(max_examples=50)
def test_attributearguments_instantiation(instance):
    assert isinstance(instance, AttributeArguments)

@given(instance=c::sharp::attributes::Attribute_strategy)
@settings(max_examples=50)
def test_c::sharp::attributes::attribute_instantiation(instance):
    assert isinstance(instance, c::sharp::attributes::Attribute)

@given(instance=Return_strategy)
@settings(max_examples=50)
def test_return_instantiation(instance):
    assert isinstance(instance, Return)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=c::sharp::attributes::AttributeTarget_strategy)
@settings(max_examples=50)
def test_c::sharp::attributes::attributetarget_instantiation(instance):
    assert isinstance(instance, c::sharp::attributes::AttributeTarget)

@given(instance=AttributeTarget_strategy)
@settings(max_examples=50)
def test_attributetarget_instantiation(instance):
    assert isinstance(instance, AttributeTarget)

@given(instance=ArrayType_strategy)
@settings(max_examples=50)
def test_arraytype_instantiation(instance):
    assert isinstance(instance, ArrayType)

@given(instance=Params_strategy)
@settings(max_examples=50)
def test_params_instantiation(instance):
    assert isinstance(instance, Params)

@given(instance=c::sharp::classes::ParameterArray_strategy)
@settings(max_examples=50)
def test_c::sharp::classes::parameterarray_instantiation(instance):
    assert isinstance(instance, c::sharp::classes::ParameterArray)

@given(instance=Out_strategy)
@settings(max_examples=50)
def test_out_instantiation(instance):
    assert isinstance(instance, Out)

@given(instance=Ref_strategy)
@settings(max_examples=50)
def test_ref_instantiation(instance):
    assert isinstance(instance, Ref)
