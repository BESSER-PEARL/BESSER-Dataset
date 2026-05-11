import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Assignable,
    robochart::ArrayAssignable,
    robochart::VarRef,
    robochart::VarSelection,
    robochart::NamedExpression,
    BinaryExpression,
    robochart::Different,
    robochart::LessOrEqual,
    robochart::GreaterOrEqual,
    robochart::And,
    robochart::Minus,
    robochart::Mult,
    robochart::GreaterThan,
    robochart::Or,
    robochart::Div,
    robochart::Cat,
    robochart::Equals,
    robochart::Implies,
    robochart::Modulus,
    robochart::Plus,
    robochart::LessThan,
    robochart::Iff,
    LambdaExp,
    robochart::DefiniteDescription,
    QuantifierExpression,
    robochart::Exists,
    robochart::Forall,
    Expression,
    robochart::LetExpression,
    robochart::RefExp,
    robochart::StringExp,
    robochart::IsExp,
    robochart::IdExp,
    robochart::IntegerExp,
    robochart::Not,
    robochart::TupleExp,
    robochart::SetExp,
    robochart::StateClockExp,
    robochart::IfExpression,
    robochart::SetRange,
    robochart::EnumExp,
    robochart::FromExp,
    robochart::ToExp,
    robochart::AsExp,
    robochart::FloatExp,
    robochart::ParExp,
    robochart::Neg,
    robochart::ArrayExp,
    robochart::CallExp,
    robochart::ElseExp,
    robochart::LambdaExp,
    robochart::SetComp,
    robochart::QuantifierExpression,
    robochart::WaitingConditionRef,
    robochart::ClockExp,
    robochart::InExp,
    robochart::BooleanExp,
    robochart::Selection,
    robochart::BinaryExpression,
    robochart::TypeExp,
    robochart::SeqExp,
    robochart::VarExp,
    robochart::RangeExp,
    robochart::ResultExp,
    robochart::Assignable,
    Statement,
    robochart::SendEvent,
    robochart::IfStmt,
    robochart::Wait,
    robochart::ParStmt,
    robochart::Assignment,
    robochart::Skip,
    robochart::Call,
    robochart::SeqStatement,
    robochart::TimedStatement,
    robochart::ClockReset,
    robochart::ConnectionNode,
    robochart::Connection,
    Controller,
    robochart::ControllerRef,
    Action,
    robochart::ExitAction,
    robochart::DuringAction,
    robochart::EntryAction,
    State,
    robochart::Final,
    robochart::Action,
    Junction,
    robochart::Initial,
    Node,
    robochart::Junction,
    robochart::Statement,
    robochart::Trigger,
    robochart::ProbabilisticJunction,
    RoboticPlatform,
    Context,
    robochart::NodeContainer,
    NodeContainer,
    robochart::State,
    robochart::StateMachineBody,
    StateMachine,
    Variable,
    robochart::BasicContext,
    BasicContext,
    robochart::Context,
    Reference,
    robochart::StateMachineRef,
    robochart::RoboticPlatformRef,
    robochart::Reference,
    StateMachineBody,
    OperationSig,
    Operation,
    robochart::OperationRef,
    ConnectionNode,
    robochart::VariableList,
    SetType,
    robochart::SeqType,
    RelationType,
    robochart::FunctionType,
    robochart::Parameter,
    robochart::Expression,
    TypedNamedElement,
    robochart::Member,
    robochart::Type,
    NamedExpression,
    Member,
    robochart::Variable,
    robochart::Field,
    Type,
    robochart::SetType,
    robochart::TypeRef,
    robochart::VectorType,
    robochart::RelationType,
    robochart::AnyType,
    robochart::MatrixType,
    robochart::ProductType,
    robochart::StateMachineDef,
    TypeDecl,
    robochart::Literal,
    robochart::Enumeration,
    robochart::RecordType,
    robochart::NameType,
    robochart::PrimitiveType,
    NamedElement,
    robochart::RoboticPlatform,
    robochart::Operation,
    robochart::TypedNamedElement,
    robochart::Transition,
    robochart::Event,
    robochart::WaitingCondition,
    robochart::TypeDecl,
    robochart::Declaration,
    robochart::Clock,
    robochart::Node,
    robochart::OperationSig,
    robochart::StateMachine,
    robochart::Controller,
    robochart::NamedElement,
    robochart::Function,
    robochart::OperationDef,
    robochart::RCModule,
    robochart::ControllerDef,
    robochart::RoboticPlatformDef,
    robochart::Interface,
    BasicPackage,
    robochart::RCPackage,
    robochart::Import,
    robochart::BasicPackage,
    TriggerType,
    VariableModifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_assignable_is_not_abstract():
    assert not inspect.isabstract(Assignable)


def test_assignable_constructor_exists():
    assert callable(Assignable.__init__)


def test_assignable_constructor_args():
    sig = inspect.signature(Assignable.__init__)
    params = list(sig.parameters.keys())



def test_robochart::arrayassignable_is_not_abstract():
    assert not inspect.isabstract(robochart::ArrayAssignable)


def test_robochart::arrayassignable_constructor_exists():
    assert callable(robochart::ArrayAssignable.__init__)


def test_robochart::arrayassignable_constructor_args():
    sig = inspect.signature(robochart::ArrayAssignable.__init__)
    params = list(sig.parameters.keys())



def test_robochart::varref_is_not_abstract():
    assert not inspect.isabstract(robochart::VarRef)


def test_robochart::varref_constructor_exists():
    assert callable(robochart::VarRef.__init__)


def test_robochart::varref_constructor_args():
    sig = inspect.signature(robochart::VarRef.__init__)
    params = list(sig.parameters.keys())



def test_robochart::varselection_is_not_abstract():
    assert not inspect.isabstract(robochart::VarSelection)


def test_robochart::varselection_constructor_exists():
    assert callable(robochart::VarSelection.__init__)


def test_robochart::varselection_constructor_args():
    sig = inspect.signature(robochart::VarSelection.__init__)
    params = list(sig.parameters.keys())



def test_robochart::namedexpression_is_not_abstract():
    assert not inspect.isabstract(robochart::NamedExpression)


def test_robochart::namedexpression_constructor_exists():
    assert callable(robochart::NamedExpression.__init__)


def test_robochart::namedexpression_constructor_args():
    sig = inspect.signature(robochart::NamedExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_robochart::different_is_not_abstract():
    assert not inspect.isabstract(robochart::Different)


def test_robochart::different_constructor_exists():
    assert callable(robochart::Different.__init__)


def test_robochart::different_constructor_args():
    sig = inspect.signature(robochart::Different.__init__)
    params = list(sig.parameters.keys())



def test_robochart::lessorequal_is_not_abstract():
    assert not inspect.isabstract(robochart::LessOrEqual)


def test_robochart::lessorequal_constructor_exists():
    assert callable(robochart::LessOrEqual.__init__)


def test_robochart::lessorequal_constructor_args():
    sig = inspect.signature(robochart::LessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_robochart::greaterorequal_is_not_abstract():
    assert not inspect.isabstract(robochart::GreaterOrEqual)


def test_robochart::greaterorequal_constructor_exists():
    assert callable(robochart::GreaterOrEqual.__init__)


def test_robochart::greaterorequal_constructor_args():
    sig = inspect.signature(robochart::GreaterOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_robochart::and_is_not_abstract():
    assert not inspect.isabstract(robochart::And)


def test_robochart::and_constructor_exists():
    assert callable(robochart::And.__init__)


def test_robochart::and_constructor_args():
    sig = inspect.signature(robochart::And.__init__)
    params = list(sig.parameters.keys())



def test_robochart::minus_is_not_abstract():
    assert not inspect.isabstract(robochart::Minus)


def test_robochart::minus_constructor_exists():
    assert callable(robochart::Minus.__init__)


def test_robochart::minus_constructor_args():
    sig = inspect.signature(robochart::Minus.__init__)
    params = list(sig.parameters.keys())



def test_robochart::mult_is_not_abstract():
    assert not inspect.isabstract(robochart::Mult)


def test_robochart::mult_constructor_exists():
    assert callable(robochart::Mult.__init__)


def test_robochart::mult_constructor_args():
    sig = inspect.signature(robochart::Mult.__init__)
    params = list(sig.parameters.keys())



def test_robochart::greaterthan_is_not_abstract():
    assert not inspect.isabstract(robochart::GreaterThan)


def test_robochart::greaterthan_constructor_exists():
    assert callable(robochart::GreaterThan.__init__)


def test_robochart::greaterthan_constructor_args():
    sig = inspect.signature(robochart::GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_robochart::or_is_not_abstract():
    assert not inspect.isabstract(robochart::Or)


def test_robochart::or_constructor_exists():
    assert callable(robochart::Or.__init__)


def test_robochart::or_constructor_args():
    sig = inspect.signature(robochart::Or.__init__)
    params = list(sig.parameters.keys())



def test_robochart::div_is_not_abstract():
    assert not inspect.isabstract(robochart::Div)


def test_robochart::div_constructor_exists():
    assert callable(robochart::Div.__init__)


def test_robochart::div_constructor_args():
    sig = inspect.signature(robochart::Div.__init__)
    params = list(sig.parameters.keys())



def test_robochart::cat_is_not_abstract():
    assert not inspect.isabstract(robochart::Cat)


def test_robochart::cat_constructor_exists():
    assert callable(robochart::Cat.__init__)


def test_robochart::cat_constructor_args():
    sig = inspect.signature(robochart::Cat.__init__)
    params = list(sig.parameters.keys())



def test_robochart::equals_is_not_abstract():
    assert not inspect.isabstract(robochart::Equals)


def test_robochart::equals_constructor_exists():
    assert callable(robochart::Equals.__init__)


def test_robochart::equals_constructor_args():
    sig = inspect.signature(robochart::Equals.__init__)
    params = list(sig.parameters.keys())



def test_robochart::implies_is_not_abstract():
    assert not inspect.isabstract(robochart::Implies)


def test_robochart::implies_constructor_exists():
    assert callable(robochart::Implies.__init__)


def test_robochart::implies_constructor_args():
    sig = inspect.signature(robochart::Implies.__init__)
    params = list(sig.parameters.keys())



def test_robochart::modulus_is_not_abstract():
    assert not inspect.isabstract(robochart::Modulus)


def test_robochart::modulus_constructor_exists():
    assert callable(robochart::Modulus.__init__)


def test_robochart::modulus_constructor_args():
    sig = inspect.signature(robochart::Modulus.__init__)
    params = list(sig.parameters.keys())



def test_robochart::plus_is_not_abstract():
    assert not inspect.isabstract(robochart::Plus)


def test_robochart::plus_constructor_exists():
    assert callable(robochart::Plus.__init__)


def test_robochart::plus_constructor_args():
    sig = inspect.signature(robochart::Plus.__init__)
    params = list(sig.parameters.keys())



def test_robochart::lessthan_is_not_abstract():
    assert not inspect.isabstract(robochart::LessThan)


def test_robochart::lessthan_constructor_exists():
    assert callable(robochart::LessThan.__init__)


def test_robochart::lessthan_constructor_args():
    sig = inspect.signature(robochart::LessThan.__init__)
    params = list(sig.parameters.keys())



def test_robochart::iff_is_not_abstract():
    assert not inspect.isabstract(robochart::Iff)


def test_robochart::iff_constructor_exists():
    assert callable(robochart::Iff.__init__)


def test_robochart::iff_constructor_args():
    sig = inspect.signature(robochart::Iff.__init__)
    params = list(sig.parameters.keys())



def test_lambdaexp_is_not_abstract():
    assert not inspect.isabstract(LambdaExp)


def test_lambdaexp_constructor_exists():
    assert callable(LambdaExp.__init__)


def test_lambdaexp_constructor_args():
    sig = inspect.signature(LambdaExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::definitedescription_is_not_abstract():
    assert not inspect.isabstract(robochart::DefiniteDescription)


def test_robochart::definitedescription_constructor_exists():
    assert callable(robochart::DefiniteDescription.__init__)


def test_robochart::definitedescription_constructor_args():
    sig = inspect.signature(robochart::DefiniteDescription.__init__)
    params = list(sig.parameters.keys())



def test_quantifierexpression_is_not_abstract():
    assert not inspect.isabstract(QuantifierExpression)


def test_quantifierexpression_constructor_exists():
    assert callable(QuantifierExpression.__init__)


def test_quantifierexpression_constructor_args():
    sig = inspect.signature(QuantifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_robochart::exists_is_not_abstract():
    assert not inspect.isabstract(robochart::Exists)


def test_robochart::exists_constructor_exists():
    assert callable(robochart::Exists.__init__)


def test_robochart::exists_constructor_args():
    sig = inspect.signature(robochart::Exists.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"

def test_robochart::exists_has_unique():
    assert hasattr(robochart::Exists, "unique")
    descriptor = None
    for klass in robochart::Exists.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_robochart::forall_is_not_abstract():
    assert not inspect.isabstract(robochart::Forall)


def test_robochart::forall_constructor_exists():
    assert callable(robochart::Forall.__init__)


def test_robochart::forall_constructor_args():
    sig = inspect.signature(robochart::Forall.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_robochart::letexpression_is_not_abstract():
    assert not inspect.isabstract(robochart::LetExpression)


def test_robochart::letexpression_constructor_exists():
    assert callable(robochart::LetExpression.__init__)


def test_robochart::letexpression_constructor_args():
    sig = inspect.signature(robochart::LetExpression.__init__)
    params = list(sig.parameters.keys())



def test_robochart::refexp_is_not_abstract():
    assert not inspect.isabstract(robochart::RefExp)


def test_robochart::refexp_constructor_exists():
    assert callable(robochart::RefExp.__init__)


def test_robochart::refexp_constructor_args():
    sig = inspect.signature(robochart::RefExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::stringexp_is_not_abstract():
    assert not inspect.isabstract(robochart::StringExp)


def test_robochart::stringexp_constructor_exists():
    assert callable(robochart::StringExp.__init__)


def test_robochart::stringexp_constructor_args():
    sig = inspect.signature(robochart::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_robochart::stringexp_has_value():
    assert hasattr(robochart::StringExp, "value")
    descriptor = None
    for klass in robochart::StringExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_robochart::isexp_is_not_abstract():
    assert not inspect.isabstract(robochart::IsExp)


def test_robochart::isexp_constructor_exists():
    assert callable(robochart::IsExp.__init__)


def test_robochart::isexp_constructor_args():
    sig = inspect.signature(robochart::IsExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::idexp_is_not_abstract():
    assert not inspect.isabstract(robochart::IdExp)


def test_robochart::idexp_constructor_exists():
    assert callable(robochart::IdExp.__init__)


def test_robochart::idexp_constructor_args():
    sig = inspect.signature(robochart::IdExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::integerexp_is_not_abstract():
    assert not inspect.isabstract(robochart::IntegerExp)


def test_robochart::integerexp_constructor_exists():
    assert callable(robochart::IntegerExp.__init__)


def test_robochart::integerexp_constructor_args():
    sig = inspect.signature(robochart::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_robochart::integerexp_has_value():
    assert hasattr(robochart::IntegerExp, "value")
    descriptor = None
    for klass in robochart::IntegerExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_robochart::not_is_not_abstract():
    assert not inspect.isabstract(robochart::Not)


def test_robochart::not_constructor_exists():
    assert callable(robochart::Not.__init__)


def test_robochart::not_constructor_args():
    sig = inspect.signature(robochart::Not.__init__)
    params = list(sig.parameters.keys())



def test_robochart::tupleexp_is_not_abstract():
    assert not inspect.isabstract(robochart::TupleExp)


def test_robochart::tupleexp_constructor_exists():
    assert callable(robochart::TupleExp.__init__)


def test_robochart::tupleexp_constructor_args():
    sig = inspect.signature(robochart::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::setexp_is_not_abstract():
    assert not inspect.isabstract(robochart::SetExp)


def test_robochart::setexp_constructor_exists():
    assert callable(robochart::SetExp.__init__)


def test_robochart::setexp_constructor_args():
    sig = inspect.signature(robochart::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::stateclockexp_is_not_abstract():
    assert not inspect.isabstract(robochart::StateClockExp)


def test_robochart::stateclockexp_constructor_exists():
    assert callable(robochart::StateClockExp.__init__)


def test_robochart::stateclockexp_constructor_args():
    sig = inspect.signature(robochart::StateClockExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::ifexpression_is_not_abstract():
    assert not inspect.isabstract(robochart::IfExpression)


def test_robochart::ifexpression_constructor_exists():
    assert callable(robochart::IfExpression.__init__)


def test_robochart::ifexpression_constructor_args():
    sig = inspect.signature(robochart::IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_robochart::setrange_is_not_abstract():
    assert not inspect.isabstract(robochart::SetRange)


def test_robochart::setrange_constructor_exists():
    assert callable(robochart::SetRange.__init__)


def test_robochart::setrange_constructor_args():
    sig = inspect.signature(robochart::SetRange.__init__)
    params = list(sig.parameters.keys())



def test_robochart::enumexp_is_not_abstract():
    assert not inspect.isabstract(robochart::EnumExp)


def test_robochart::enumexp_constructor_exists():
    assert callable(robochart::EnumExp.__init__)


def test_robochart::enumexp_constructor_args():
    sig = inspect.signature(robochart::EnumExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::fromexp_is_not_abstract():
    assert not inspect.isabstract(robochart::FromExp)


def test_robochart::fromexp_constructor_exists():
    assert callable(robochart::FromExp.__init__)


def test_robochart::fromexp_constructor_args():
    sig = inspect.signature(robochart::FromExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::toexp_is_not_abstract():
    assert not inspect.isabstract(robochart::ToExp)


def test_robochart::toexp_constructor_exists():
    assert callable(robochart::ToExp.__init__)


def test_robochart::toexp_constructor_args():
    sig = inspect.signature(robochart::ToExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::asexp_is_not_abstract():
    assert not inspect.isabstract(robochart::AsExp)


def test_robochart::asexp_constructor_exists():
    assert callable(robochart::AsExp.__init__)


def test_robochart::asexp_constructor_args():
    sig = inspect.signature(robochart::AsExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::floatexp_is_not_abstract():
    assert not inspect.isabstract(robochart::FloatExp)


def test_robochart::floatexp_constructor_exists():
    assert callable(robochart::FloatExp.__init__)


def test_robochart::floatexp_constructor_args():
    sig = inspect.signature(robochart::FloatExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_robochart::floatexp_has_value():
    assert hasattr(robochart::FloatExp, "value")
    descriptor = None
    for klass in robochart::FloatExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_robochart::parexp_is_not_abstract():
    assert not inspect.isabstract(robochart::ParExp)


def test_robochart::parexp_constructor_exists():
    assert callable(robochart::ParExp.__init__)


def test_robochart::parexp_constructor_args():
    sig = inspect.signature(robochart::ParExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::neg_is_not_abstract():
    assert not inspect.isabstract(robochart::Neg)


def test_robochart::neg_constructor_exists():
    assert callable(robochart::Neg.__init__)


def test_robochart::neg_constructor_args():
    sig = inspect.signature(robochart::Neg.__init__)
    params = list(sig.parameters.keys())



def test_robochart::arrayexp_is_not_abstract():
    assert not inspect.isabstract(robochart::ArrayExp)


def test_robochart::arrayexp_constructor_exists():
    assert callable(robochart::ArrayExp.__init__)


def test_robochart::arrayexp_constructor_args():
    sig = inspect.signature(robochart::ArrayExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::callexp_is_not_abstract():
    assert not inspect.isabstract(robochart::CallExp)


def test_robochart::callexp_constructor_exists():
    assert callable(robochart::CallExp.__init__)


def test_robochart::callexp_constructor_args():
    sig = inspect.signature(robochart::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::elseexp_is_not_abstract():
    assert not inspect.isabstract(robochart::ElseExp)


def test_robochart::elseexp_constructor_exists():
    assert callable(robochart::ElseExp.__init__)


def test_robochart::elseexp_constructor_args():
    sig = inspect.signature(robochart::ElseExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::lambdaexp_is_not_abstract():
    assert not inspect.isabstract(robochart::LambdaExp)


def test_robochart::lambdaexp_constructor_exists():
    assert callable(robochart::LambdaExp.__init__)


def test_robochart::lambdaexp_constructor_args():
    sig = inspect.signature(robochart::LambdaExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::setcomp_is_not_abstract():
    assert not inspect.isabstract(robochart::SetComp)


def test_robochart::setcomp_constructor_exists():
    assert callable(robochart::SetComp.__init__)


def test_robochart::setcomp_constructor_args():
    sig = inspect.signature(robochart::SetComp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::quantifierexpression_is_not_abstract():
    assert not inspect.isabstract(robochart::QuantifierExpression)


def test_robochart::quantifierexpression_constructor_exists():
    assert callable(robochart::QuantifierExpression.__init__)


def test_robochart::quantifierexpression_constructor_args():
    sig = inspect.signature(robochart::QuantifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_robochart::waitingconditionref_is_not_abstract():
    assert not inspect.isabstract(robochart::WaitingConditionRef)


def test_robochart::waitingconditionref_constructor_exists():
    assert callable(robochart::WaitingConditionRef.__init__)


def test_robochart::waitingconditionref_constructor_args():
    sig = inspect.signature(robochart::WaitingConditionRef.__init__)
    params = list(sig.parameters.keys())



def test_robochart::clockexp_is_not_abstract():
    assert not inspect.isabstract(robochart::ClockExp)


def test_robochart::clockexp_constructor_exists():
    assert callable(robochart::ClockExp.__init__)


def test_robochart::clockexp_constructor_args():
    sig = inspect.signature(robochart::ClockExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::inexp_is_not_abstract():
    assert not inspect.isabstract(robochart::InExp)


def test_robochart::inexp_constructor_exists():
    assert callable(robochart::InExp.__init__)


def test_robochart::inexp_constructor_args():
    sig = inspect.signature(robochart::InExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::booleanexp_is_not_abstract():
    assert not inspect.isabstract(robochart::BooleanExp)


def test_robochart::booleanexp_constructor_exists():
    assert callable(robochart::BooleanExp.__init__)


def test_robochart::booleanexp_constructor_args():
    sig = inspect.signature(robochart::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_robochart::booleanexp_has_value():
    assert hasattr(robochart::BooleanExp, "value")
    descriptor = None
    for klass in robochart::BooleanExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_robochart::selection_is_not_abstract():
    assert not inspect.isabstract(robochart::Selection)


def test_robochart::selection_constructor_exists():
    assert callable(robochart::Selection.__init__)


def test_robochart::selection_constructor_args():
    sig = inspect.signature(robochart::Selection.__init__)
    params = list(sig.parameters.keys())



def test_robochart::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(robochart::BinaryExpression)


def test_robochart::binaryexpression_constructor_exists():
    assert callable(robochart::BinaryExpression.__init__)


def test_robochart::binaryexpression_constructor_args():
    sig = inspect.signature(robochart::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_robochart::typeexp_is_not_abstract():
    assert not inspect.isabstract(robochart::TypeExp)


def test_robochart::typeexp_constructor_exists():
    assert callable(robochart::TypeExp.__init__)


def test_robochart::typeexp_constructor_args():
    sig = inspect.signature(robochart::TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::seqexp_is_not_abstract():
    assert not inspect.isabstract(robochart::SeqExp)


def test_robochart::seqexp_constructor_exists():
    assert callable(robochart::SeqExp.__init__)


def test_robochart::seqexp_constructor_args():
    sig = inspect.signature(robochart::SeqExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::varexp_is_not_abstract():
    assert not inspect.isabstract(robochart::VarExp)


def test_robochart::varexp_constructor_exists():
    assert callable(robochart::VarExp.__init__)


def test_robochart::varexp_constructor_args():
    sig = inspect.signature(robochart::VarExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::rangeexp_is_not_abstract():
    assert not inspect.isabstract(robochart::RangeExp)


def test_robochart::rangeexp_constructor_exists():
    assert callable(robochart::RangeExp.__init__)


def test_robochart::rangeexp_constructor_args():
    sig = inspect.signature(robochart::RangeExp.__init__)
    params = list(sig.parameters.keys())
    assert "linterval" in params, "Missing parameter 'linterval'"
    assert "rinterval" in params, "Missing parameter 'rinterval'"

def test_robochart::rangeexp_has_linterval():
    assert hasattr(robochart::RangeExp, "linterval")
    descriptor = None
    for klass in robochart::RangeExp.__mro__:
        if "linterval" in klass.__dict__:
            descriptor = klass.__dict__["linterval"]
            break
    assert isinstance(descriptor, property)

def test_robochart::rangeexp_has_rinterval():
    assert hasattr(robochart::RangeExp, "rinterval")
    descriptor = None
    for klass in robochart::RangeExp.__mro__:
        if "rinterval" in klass.__dict__:
            descriptor = klass.__dict__["rinterval"]
            break
    assert isinstance(descriptor, property)



def test_robochart::resultexp_is_not_abstract():
    assert not inspect.isabstract(robochart::ResultExp)


def test_robochart::resultexp_constructor_exists():
    assert callable(robochart::ResultExp.__init__)


def test_robochart::resultexp_constructor_args():
    sig = inspect.signature(robochart::ResultExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart::assignable_is_not_abstract():
    assert not inspect.isabstract(robochart::Assignable)


def test_robochart::assignable_constructor_exists():
    assert callable(robochart::Assignable.__init__)


def test_robochart::assignable_constructor_args():
    sig = inspect.signature(robochart::Assignable.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_robochart::sendevent_is_not_abstract():
    assert not inspect.isabstract(robochart::SendEvent)


def test_robochart::sendevent_constructor_exists():
    assert callable(robochart::SendEvent.__init__)


def test_robochart::sendevent_constructor_args():
    sig = inspect.signature(robochart::SendEvent.__init__)
    params = list(sig.parameters.keys())



def test_robochart::ifstmt_is_not_abstract():
    assert not inspect.isabstract(robochart::IfStmt)


def test_robochart::ifstmt_constructor_exists():
    assert callable(robochart::IfStmt.__init__)


def test_robochart::ifstmt_constructor_args():
    sig = inspect.signature(robochart::IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_robochart::wait_is_not_abstract():
    assert not inspect.isabstract(robochart::Wait)


def test_robochart::wait_constructor_exists():
    assert callable(robochart::Wait.__init__)


def test_robochart::wait_constructor_args():
    sig = inspect.signature(robochart::Wait.__init__)
    params = list(sig.parameters.keys())



def test_robochart::parstmt_is_not_abstract():
    assert not inspect.isabstract(robochart::ParStmt)


def test_robochart::parstmt_constructor_exists():
    assert callable(robochart::ParStmt.__init__)


def test_robochart::parstmt_constructor_args():
    sig = inspect.signature(robochart::ParStmt.__init__)
    params = list(sig.parameters.keys())



def test_robochart::assignment_is_not_abstract():
    assert not inspect.isabstract(robochart::Assignment)


def test_robochart::assignment_constructor_exists():
    assert callable(robochart::Assignment.__init__)


def test_robochart::assignment_constructor_args():
    sig = inspect.signature(robochart::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_robochart::skip_is_not_abstract():
    assert not inspect.isabstract(robochart::Skip)


def test_robochart::skip_constructor_exists():
    assert callable(robochart::Skip.__init__)


def test_robochart::skip_constructor_args():
    sig = inspect.signature(robochart::Skip.__init__)
    params = list(sig.parameters.keys())



def test_robochart::call_is_not_abstract():
    assert not inspect.isabstract(robochart::Call)


def test_robochart::call_constructor_exists():
    assert callable(robochart::Call.__init__)


def test_robochart::call_constructor_args():
    sig = inspect.signature(robochart::Call.__init__)
    params = list(sig.parameters.keys())



def test_robochart::seqstatement_is_not_abstract():
    assert not inspect.isabstract(robochart::SeqStatement)


def test_robochart::seqstatement_constructor_exists():
    assert callable(robochart::SeqStatement.__init__)


def test_robochart::seqstatement_constructor_args():
    sig = inspect.signature(robochart::SeqStatement.__init__)
    params = list(sig.parameters.keys())



def test_robochart::timedstatement_is_not_abstract():
    assert not inspect.isabstract(robochart::TimedStatement)


def test_robochart::timedstatement_constructor_exists():
    assert callable(robochart::TimedStatement.__init__)


def test_robochart::timedstatement_constructor_args():
    sig = inspect.signature(robochart::TimedStatement.__init__)
    params = list(sig.parameters.keys())



def test_robochart::clockreset_is_not_abstract():
    assert not inspect.isabstract(robochart::ClockReset)


def test_robochart::clockreset_constructor_exists():
    assert callable(robochart::ClockReset.__init__)


def test_robochart::clockreset_constructor_args():
    sig = inspect.signature(robochart::ClockReset.__init__)
    params = list(sig.parameters.keys())



def test_robochart::connectionnode_is_not_abstract():
    assert not inspect.isabstract(robochart::ConnectionNode)


def test_robochart::connectionnode_constructor_exists():
    assert callable(robochart::ConnectionNode.__init__)


def test_robochart::connectionnode_constructor_args():
    sig = inspect.signature(robochart::ConnectionNode.__init__)
    params = list(sig.parameters.keys())



def test_robochart::connection_is_not_abstract():
    assert not inspect.isabstract(robochart::Connection)


def test_robochart::connection_constructor_exists():
    assert callable(robochart::Connection.__init__)


def test_robochart::connection_constructor_args():
    sig = inspect.signature(robochart::Connection.__init__)
    params = list(sig.parameters.keys())
    assert "async_" in params, "Missing parameter 'async_'"
    assert "bidirec" in params, "Missing parameter 'bidirec'"

def test_robochart::connection_has_async_():
    assert hasattr(robochart::Connection, "async_")
    descriptor = None
    for klass in robochart::Connection.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_robochart::connection_has_bidirec():
    assert hasattr(robochart::Connection, "bidirec")
    descriptor = None
    for klass in robochart::Connection.__mro__:
        if "bidirec" in klass.__dict__:
            descriptor = klass.__dict__["bidirec"]
            break
    assert isinstance(descriptor, property)



def test_controller_is_not_abstract():
    assert not inspect.isabstract(Controller)


def test_controller_constructor_exists():
    assert callable(Controller.__init__)


def test_controller_constructor_args():
    sig = inspect.signature(Controller.__init__)
    params = list(sig.parameters.keys())



def test_robochart::controllerref_is_not_abstract():
    assert not inspect.isabstract(robochart::ControllerRef)


def test_robochart::controllerref_constructor_exists():
    assert callable(robochart::ControllerRef.__init__)


def test_robochart::controllerref_constructor_args():
    sig = inspect.signature(robochart::ControllerRef.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_robochart::exitaction_is_not_abstract():
    assert not inspect.isabstract(robochart::ExitAction)


def test_robochart::exitaction_constructor_exists():
    assert callable(robochart::ExitAction.__init__)


def test_robochart::exitaction_constructor_args():
    sig = inspect.signature(robochart::ExitAction.__init__)
    params = list(sig.parameters.keys())



def test_robochart::duringaction_is_not_abstract():
    assert not inspect.isabstract(robochart::DuringAction)


def test_robochart::duringaction_constructor_exists():
    assert callable(robochart::DuringAction.__init__)


def test_robochart::duringaction_constructor_args():
    sig = inspect.signature(robochart::DuringAction.__init__)
    params = list(sig.parameters.keys())



def test_robochart::entryaction_is_not_abstract():
    assert not inspect.isabstract(robochart::EntryAction)


def test_robochart::entryaction_constructor_exists():
    assert callable(robochart::EntryAction.__init__)


def test_robochart::entryaction_constructor_args():
    sig = inspect.signature(robochart::EntryAction.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_robochart::final_is_not_abstract():
    assert not inspect.isabstract(robochart::Final)


def test_robochart::final_constructor_exists():
    assert callable(robochart::Final.__init__)


def test_robochart::final_constructor_args():
    sig = inspect.signature(robochart::Final.__init__)
    params = list(sig.parameters.keys())



def test_robochart::action_is_not_abstract():
    assert not inspect.isabstract(robochart::Action)


def test_robochart::action_constructor_exists():
    assert callable(robochart::Action.__init__)


def test_robochart::action_constructor_args():
    sig = inspect.signature(robochart::Action.__init__)
    params = list(sig.parameters.keys())



def test_junction_is_not_abstract():
    assert not inspect.isabstract(Junction)


def test_junction_constructor_exists():
    assert callable(Junction.__init__)


def test_junction_constructor_args():
    sig = inspect.signature(Junction.__init__)
    params = list(sig.parameters.keys())



def test_robochart::initial_is_not_abstract():
    assert not inspect.isabstract(robochart::Initial)


def test_robochart::initial_constructor_exists():
    assert callable(robochart::Initial.__init__)


def test_robochart::initial_constructor_args():
    sig = inspect.signature(robochart::Initial.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_robochart::junction_is_not_abstract():
    assert not inspect.isabstract(robochart::Junction)


def test_robochart::junction_constructor_exists():
    assert callable(robochart::Junction.__init__)


def test_robochart::junction_constructor_args():
    sig = inspect.signature(robochart::Junction.__init__)
    params = list(sig.parameters.keys())



def test_robochart::statement_is_not_abstract():
    assert not inspect.isabstract(robochart::Statement)


def test_robochart::statement_constructor_exists():
    assert callable(robochart::Statement.__init__)


def test_robochart::statement_constructor_args():
    sig = inspect.signature(robochart::Statement.__init__)
    params = list(sig.parameters.keys())



def test_robochart::trigger_is_not_abstract():
    assert not inspect.isabstract(robochart::Trigger)


def test_robochart::trigger_constructor_exists():
    assert callable(robochart::Trigger.__init__)


def test_robochart::trigger_constructor_args():
    sig = inspect.signature(robochart::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "_type" in params, "Missing parameter '_type'"

def test_robochart::trigger_has__type():
    assert hasattr(robochart::Trigger, "_type")
    descriptor = None
    for klass in robochart::Trigger.__mro__:
        if "_type" in klass.__dict__:
            descriptor = klass.__dict__["_type"]
            break
    assert isinstance(descriptor, property)



def test_robochart::probabilisticjunction_is_not_abstract():
    assert not inspect.isabstract(robochart::ProbabilisticJunction)


def test_robochart::probabilisticjunction_constructor_exists():
    assert callable(robochart::ProbabilisticJunction.__init__)


def test_robochart::probabilisticjunction_constructor_args():
    sig = inspect.signature(robochart::ProbabilisticJunction.__init__)
    params = list(sig.parameters.keys())



def test_roboticplatform_is_not_abstract():
    assert not inspect.isabstract(RoboticPlatform)


def test_roboticplatform_constructor_exists():
    assert callable(RoboticPlatform.__init__)


def test_roboticplatform_constructor_args():
    sig = inspect.signature(RoboticPlatform.__init__)
    params = list(sig.parameters.keys())



def test_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_context_constructor_exists():
    assert callable(Context.__init__)


def test_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_robochart::nodecontainer_is_not_abstract():
    assert not inspect.isabstract(robochart::NodeContainer)


def test_robochart::nodecontainer_constructor_exists():
    assert callable(robochart::NodeContainer.__init__)


def test_robochart::nodecontainer_constructor_args():
    sig = inspect.signature(robochart::NodeContainer.__init__)
    params = list(sig.parameters.keys())



def test_nodecontainer_is_not_abstract():
    assert not inspect.isabstract(NodeContainer)


def test_nodecontainer_constructor_exists():
    assert callable(NodeContainer.__init__)


def test_nodecontainer_constructor_args():
    sig = inspect.signature(NodeContainer.__init__)
    params = list(sig.parameters.keys())



def test_robochart::state_is_not_abstract():
    assert not inspect.isabstract(robochart::State)


def test_robochart::state_constructor_exists():
    assert callable(robochart::State.__init__)


def test_robochart::state_constructor_args():
    sig = inspect.signature(robochart::State.__init__)
    params = list(sig.parameters.keys())



def test_robochart::statemachinebody_is_not_abstract():
    assert not inspect.isabstract(robochart::StateMachineBody)


def test_robochart::statemachinebody_constructor_exists():
    assert callable(robochart::StateMachineBody.__init__)


def test_robochart::statemachinebody_constructor_args():
    sig = inspect.signature(robochart::StateMachineBody.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_robochart::basiccontext_is_not_abstract():
    assert not inspect.isabstract(robochart::BasicContext)


def test_robochart::basiccontext_constructor_exists():
    assert callable(robochart::BasicContext.__init__)


def test_robochart::basiccontext_constructor_args():
    sig = inspect.signature(robochart::BasicContext.__init__)
    params = list(sig.parameters.keys())



def test_basiccontext_is_not_abstract():
    assert not inspect.isabstract(BasicContext)


def test_basiccontext_constructor_exists():
    assert callable(BasicContext.__init__)


def test_basiccontext_constructor_args():
    sig = inspect.signature(BasicContext.__init__)
    params = list(sig.parameters.keys())



def test_robochart::context_is_not_abstract():
    assert not inspect.isabstract(robochart::Context)


def test_robochart::context_constructor_exists():
    assert callable(robochart::Context.__init__)


def test_robochart::context_constructor_args():
    sig = inspect.signature(robochart::Context.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_robochart::statemachineref_is_not_abstract():
    assert not inspect.isabstract(robochart::StateMachineRef)


def test_robochart::statemachineref_constructor_exists():
    assert callable(robochart::StateMachineRef.__init__)


def test_robochart::statemachineref_constructor_args():
    sig = inspect.signature(robochart::StateMachineRef.__init__)
    params = list(sig.parameters.keys())



def test_robochart::roboticplatformref_is_not_abstract():
    assert not inspect.isabstract(robochart::RoboticPlatformRef)


def test_robochart::roboticplatformref_constructor_exists():
    assert callable(robochart::RoboticPlatformRef.__init__)


def test_robochart::roboticplatformref_constructor_args():
    sig = inspect.signature(robochart::RoboticPlatformRef.__init__)
    params = list(sig.parameters.keys())



def test_robochart::reference_is_not_abstract():
    assert not inspect.isabstract(robochart::Reference)


def test_robochart::reference_constructor_exists():
    assert callable(robochart::Reference.__init__)


def test_robochart::reference_constructor_args():
    sig = inspect.signature(robochart::Reference.__init__)
    params = list(sig.parameters.keys())



def test_statemachinebody_is_not_abstract():
    assert not inspect.isabstract(StateMachineBody)


def test_statemachinebody_constructor_exists():
    assert callable(StateMachineBody.__init__)


def test_statemachinebody_constructor_args():
    sig = inspect.signature(StateMachineBody.__init__)
    params = list(sig.parameters.keys())



def test_operationsig_is_not_abstract():
    assert not inspect.isabstract(OperationSig)


def test_operationsig_constructor_exists():
    assert callable(OperationSig.__init__)


def test_operationsig_constructor_args():
    sig = inspect.signature(OperationSig.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_robochart::operationref_is_not_abstract():
    assert not inspect.isabstract(robochart::OperationRef)


def test_robochart::operationref_constructor_exists():
    assert callable(robochart::OperationRef.__init__)


def test_robochart::operationref_constructor_args():
    sig = inspect.signature(robochart::OperationRef.__init__)
    params = list(sig.parameters.keys())



def test_connectionnode_is_not_abstract():
    assert not inspect.isabstract(ConnectionNode)


def test_connectionnode_constructor_exists():
    assert callable(ConnectionNode.__init__)


def test_connectionnode_constructor_args():
    sig = inspect.signature(ConnectionNode.__init__)
    params = list(sig.parameters.keys())



def test_robochart::variablelist_is_not_abstract():
    assert not inspect.isabstract(robochart::VariableList)


def test_robochart::variablelist_constructor_exists():
    assert callable(robochart::VariableList.__init__)


def test_robochart::variablelist_constructor_args():
    sig = inspect.signature(robochart::VariableList.__init__)
    params = list(sig.parameters.keys())
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_robochart::variablelist_has_modifier():
    assert hasattr(robochart::VariableList, "modifier")
    descriptor = None
    for klass in robochart::VariableList.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_settype_is_not_abstract():
    assert not inspect.isabstract(SetType)


def test_settype_constructor_exists():
    assert callable(SetType.__init__)


def test_settype_constructor_args():
    sig = inspect.signature(SetType.__init__)
    params = list(sig.parameters.keys())



def test_robochart::seqtype_is_not_abstract():
    assert not inspect.isabstract(robochart::SeqType)


def test_robochart::seqtype_constructor_exists():
    assert callable(robochart::SeqType.__init__)


def test_robochart::seqtype_constructor_args():
    sig = inspect.signature(robochart::SeqType.__init__)
    params = list(sig.parameters.keys())



def test_relationtype_is_not_abstract():
    assert not inspect.isabstract(RelationType)


def test_relationtype_constructor_exists():
    assert callable(RelationType.__init__)


def test_relationtype_constructor_args():
    sig = inspect.signature(RelationType.__init__)
    params = list(sig.parameters.keys())



def test_robochart::functiontype_is_not_abstract():
    assert not inspect.isabstract(robochart::FunctionType)


def test_robochart::functiontype_constructor_exists():
    assert callable(robochart::FunctionType.__init__)


def test_robochart::functiontype_constructor_args():
    sig = inspect.signature(robochart::FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_robochart::parameter_is_not_abstract():
    assert not inspect.isabstract(robochart::Parameter)


def test_robochart::parameter_constructor_exists():
    assert callable(robochart::Parameter.__init__)


def test_robochart::parameter_constructor_args():
    sig = inspect.signature(robochart::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_robochart::expression_is_not_abstract():
    assert not inspect.isabstract(robochart::Expression)


def test_robochart::expression_constructor_exists():
    assert callable(robochart::Expression.__init__)


def test_robochart::expression_constructor_args():
    sig = inspect.signature(robochart::Expression.__init__)
    params = list(sig.parameters.keys())



def test_typednamedelement_is_not_abstract():
    assert not inspect.isabstract(TypedNamedElement)


def test_typednamedelement_constructor_exists():
    assert callable(TypedNamedElement.__init__)


def test_typednamedelement_constructor_args():
    sig = inspect.signature(TypedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_robochart::member_is_not_abstract():
    assert not inspect.isabstract(robochart::Member)


def test_robochart::member_constructor_exists():
    assert callable(robochart::Member.__init__)


def test_robochart::member_constructor_args():
    sig = inspect.signature(robochart::Member.__init__)
    params = list(sig.parameters.keys())



def test_robochart::type_is_not_abstract():
    assert not inspect.isabstract(robochart::Type)


def test_robochart::type_constructor_exists():
    assert callable(robochart::Type.__init__)


def test_robochart::type_constructor_args():
    sig = inspect.signature(robochart::Type.__init__)
    params = list(sig.parameters.keys())



def test_namedexpression_is_not_abstract():
    assert not inspect.isabstract(NamedExpression)


def test_namedexpression_constructor_exists():
    assert callable(NamedExpression.__init__)


def test_namedexpression_constructor_args():
    sig = inspect.signature(NamedExpression.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_robochart::variable_is_not_abstract():
    assert not inspect.isabstract(robochart::Variable)


def test_robochart::variable_constructor_exists():
    assert callable(robochart::Variable.__init__)


def test_robochart::variable_constructor_args():
    sig = inspect.signature(robochart::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_robochart::variable_has_modifier():
    assert hasattr(robochart::Variable, "modifier")
    descriptor = None
    for klass in robochart::Variable.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_robochart::field_is_not_abstract():
    assert not inspect.isabstract(robochart::Field)


def test_robochart::field_constructor_exists():
    assert callable(robochart::Field.__init__)


def test_robochart::field_constructor_args():
    sig = inspect.signature(robochart::Field.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_robochart::settype_is_not_abstract():
    assert not inspect.isabstract(robochart::SetType)


def test_robochart::settype_constructor_exists():
    assert callable(robochart::SetType.__init__)


def test_robochart::settype_constructor_args():
    sig = inspect.signature(robochart::SetType.__init__)
    params = list(sig.parameters.keys())



def test_robochart::typeref_is_not_abstract():
    assert not inspect.isabstract(robochart::TypeRef)


def test_robochart::typeref_constructor_exists():
    assert callable(robochart::TypeRef.__init__)


def test_robochart::typeref_constructor_args():
    sig = inspect.signature(robochart::TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_robochart::vectortype_is_not_abstract():
    assert not inspect.isabstract(robochart::VectorType)


def test_robochart::vectortype_constructor_exists():
    assert callable(robochart::VectorType.__init__)


def test_robochart::vectortype_constructor_args():
    sig = inspect.signature(robochart::VectorType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_robochart::vectortype_has_size():
    assert hasattr(robochart::VectorType, "size")
    descriptor = None
    for klass in robochart::VectorType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_robochart::relationtype_is_not_abstract():
    assert not inspect.isabstract(robochart::RelationType)


def test_robochart::relationtype_constructor_exists():
    assert callable(robochart::RelationType.__init__)


def test_robochart::relationtype_constructor_args():
    sig = inspect.signature(robochart::RelationType.__init__)
    params = list(sig.parameters.keys())



def test_robochart::anytype_is_not_abstract():
    assert not inspect.isabstract(robochart::AnyType)


def test_robochart::anytype_constructor_exists():
    assert callable(robochart::AnyType.__init__)


def test_robochart::anytype_constructor_args():
    sig = inspect.signature(robochart::AnyType.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_robochart::anytype_has_identifier():
    assert hasattr(robochart::AnyType, "identifier")
    descriptor = None
    for klass in robochart::AnyType.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_robochart::matrixtype_is_not_abstract():
    assert not inspect.isabstract(robochart::MatrixType)


def test_robochart::matrixtype_constructor_exists():
    assert callable(robochart::MatrixType.__init__)


def test_robochart::matrixtype_constructor_args():
    sig = inspect.signature(robochart::MatrixType.__init__)
    params = list(sig.parameters.keys())
    assert "columns" in params, "Missing parameter 'columns'"
    assert "rows" in params, "Missing parameter 'rows'"

def test_robochart::matrixtype_has_columns():
    assert hasattr(robochart::MatrixType, "columns")
    descriptor = None
    for klass in robochart::MatrixType.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)

def test_robochart::matrixtype_has_rows():
    assert hasattr(robochart::MatrixType, "rows")
    descriptor = None
    for klass in robochart::MatrixType.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)



def test_robochart::producttype_is_not_abstract():
    assert not inspect.isabstract(robochart::ProductType)


def test_robochart::producttype_constructor_exists():
    assert callable(robochart::ProductType.__init__)


def test_robochart::producttype_constructor_args():
    sig = inspect.signature(robochart::ProductType.__init__)
    params = list(sig.parameters.keys())



def test_robochart::statemachinedef_is_not_abstract():
    assert not inspect.isabstract(robochart::StateMachineDef)


def test_robochart::statemachinedef_constructor_exists():
    assert callable(robochart::StateMachineDef.__init__)


def test_robochart::statemachinedef_constructor_args():
    sig = inspect.signature(robochart::StateMachineDef.__init__)
    params = list(sig.parameters.keys())



def test_typedecl_is_not_abstract():
    assert not inspect.isabstract(TypeDecl)


def test_typedecl_constructor_exists():
    assert callable(TypeDecl.__init__)


def test_typedecl_constructor_args():
    sig = inspect.signature(TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_robochart::literal_is_not_abstract():
    assert not inspect.isabstract(robochart::Literal)


def test_robochart::literal_constructor_exists():
    assert callable(robochart::Literal.__init__)


def test_robochart::literal_constructor_args():
    sig = inspect.signature(robochart::Literal.__init__)
    params = list(sig.parameters.keys())



def test_robochart::enumeration_is_not_abstract():
    assert not inspect.isabstract(robochart::Enumeration)


def test_robochart::enumeration_constructor_exists():
    assert callable(robochart::Enumeration.__init__)


def test_robochart::enumeration_constructor_args():
    sig = inspect.signature(robochart::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_robochart::recordtype_is_not_abstract():
    assert not inspect.isabstract(robochart::RecordType)


def test_robochart::recordtype_constructor_exists():
    assert callable(robochart::RecordType.__init__)


def test_robochart::recordtype_constructor_args():
    sig = inspect.signature(robochart::RecordType.__init__)
    params = list(sig.parameters.keys())



def test_robochart::nametype_is_not_abstract():
    assert not inspect.isabstract(robochart::NameType)


def test_robochart::nametype_constructor_exists():
    assert callable(robochart::NameType.__init__)


def test_robochart::nametype_constructor_args():
    sig = inspect.signature(robochart::NameType.__init__)
    params = list(sig.parameters.keys())



def test_robochart::primitivetype_is_not_abstract():
    assert not inspect.isabstract(robochart::PrimitiveType)


def test_robochart::primitivetype_constructor_exists():
    assert callable(robochart::PrimitiveType.__init__)


def test_robochart::primitivetype_constructor_args():
    sig = inspect.signature(robochart::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_robochart::roboticplatform_is_not_abstract():
    assert not inspect.isabstract(robochart::RoboticPlatform)


def test_robochart::roboticplatform_constructor_exists():
    assert callable(robochart::RoboticPlatform.__init__)


def test_robochart::roboticplatform_constructor_args():
    sig = inspect.signature(robochart::RoboticPlatform.__init__)
    params = list(sig.parameters.keys())



def test_robochart::operation_is_not_abstract():
    assert not inspect.isabstract(robochart::Operation)


def test_robochart::operation_constructor_exists():
    assert callable(robochart::Operation.__init__)


def test_robochart::operation_constructor_args():
    sig = inspect.signature(robochart::Operation.__init__)
    params = list(sig.parameters.keys())



def test_robochart::typednamedelement_is_not_abstract():
    assert not inspect.isabstract(robochart::TypedNamedElement)


def test_robochart::typednamedelement_constructor_exists():
    assert callable(robochart::TypedNamedElement.__init__)


def test_robochart::typednamedelement_constructor_args():
    sig = inspect.signature(robochart::TypedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_robochart::transition_is_not_abstract():
    assert not inspect.isabstract(robochart::Transition)


def test_robochart::transition_constructor_exists():
    assert callable(robochart::Transition.__init__)


def test_robochart::transition_constructor_args():
    sig = inspect.signature(robochart::Transition.__init__)
    params = list(sig.parameters.keys())



def test_robochart::event_is_not_abstract():
    assert not inspect.isabstract(robochart::Event)


def test_robochart::event_constructor_exists():
    assert callable(robochart::Event.__init__)


def test_robochart::event_constructor_args():
    sig = inspect.signature(robochart::Event.__init__)
    params = list(sig.parameters.keys())
    assert "broadcast" in params, "Missing parameter 'broadcast'"

def test_robochart::event_has_broadcast():
    assert hasattr(robochart::Event, "broadcast")
    descriptor = None
    for klass in robochart::Event.__mro__:
        if "broadcast" in klass.__dict__:
            descriptor = klass.__dict__["broadcast"]
            break
    assert isinstance(descriptor, property)



def test_robochart::waitingcondition_is_not_abstract():
    assert not inspect.isabstract(robochart::WaitingCondition)


def test_robochart::waitingcondition_constructor_exists():
    assert callable(robochart::WaitingCondition.__init__)


def test_robochart::waitingcondition_constructor_args():
    sig = inspect.signature(robochart::WaitingCondition.__init__)
    params = list(sig.parameters.keys())



def test_robochart::typedecl_is_not_abstract():
    assert not inspect.isabstract(robochart::TypeDecl)


def test_robochart::typedecl_constructor_exists():
    assert callable(robochart::TypeDecl.__init__)


def test_robochart::typedecl_constructor_args():
    sig = inspect.signature(robochart::TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_robochart::declaration_is_not_abstract():
    assert not inspect.isabstract(robochart::Declaration)


def test_robochart::declaration_constructor_exists():
    assert callable(robochart::Declaration.__init__)


def test_robochart::declaration_constructor_args():
    sig = inspect.signature(robochart::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_robochart::clock_is_not_abstract():
    assert not inspect.isabstract(robochart::Clock)


def test_robochart::clock_constructor_exists():
    assert callable(robochart::Clock.__init__)


def test_robochart::clock_constructor_args():
    sig = inspect.signature(robochart::Clock.__init__)
    params = list(sig.parameters.keys())



def test_robochart::node_is_not_abstract():
    assert not inspect.isabstract(robochart::Node)


def test_robochart::node_constructor_exists():
    assert callable(robochart::Node.__init__)


def test_robochart::node_constructor_args():
    sig = inspect.signature(robochart::Node.__init__)
    params = list(sig.parameters.keys())



def test_robochart::operationsig_is_not_abstract():
    assert not inspect.isabstract(robochart::OperationSig)


def test_robochart::operationsig_constructor_exists():
    assert callable(robochart::OperationSig.__init__)


def test_robochart::operationsig_constructor_args():
    sig = inspect.signature(robochart::OperationSig.__init__)
    params = list(sig.parameters.keys())
    assert "terminates" in params, "Missing parameter 'terminates'"

def test_robochart::operationsig_has_terminates():
    assert hasattr(robochart::OperationSig, "terminates")
    descriptor = None
    for klass in robochart::OperationSig.__mro__:
        if "terminates" in klass.__dict__:
            descriptor = klass.__dict__["terminates"]
            break
    assert isinstance(descriptor, property)



def test_robochart::statemachine_is_not_abstract():
    assert not inspect.isabstract(robochart::StateMachine)


def test_robochart::statemachine_constructor_exists():
    assert callable(robochart::StateMachine.__init__)


def test_robochart::statemachine_constructor_args():
    sig = inspect.signature(robochart::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_robochart::controller_is_not_abstract():
    assert not inspect.isabstract(robochart::Controller)


def test_robochart::controller_constructor_exists():
    assert callable(robochart::Controller.__init__)


def test_robochart::controller_constructor_args():
    sig = inspect.signature(robochart::Controller.__init__)
    params = list(sig.parameters.keys())



def test_robochart::namedelement_is_not_abstract():
    assert not inspect.isabstract(robochart::NamedElement)


def test_robochart::namedelement_constructor_exists():
    assert callable(robochart::NamedElement.__init__)


def test_robochart::namedelement_constructor_args():
    sig = inspect.signature(robochart::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_robochart::namedelement_has_name():
    assert hasattr(robochart::NamedElement, "name")
    descriptor = None
    for klass in robochart::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_robochart::function_is_not_abstract():
    assert not inspect.isabstract(robochart::Function)


def test_robochart::function_constructor_exists():
    assert callable(robochart::Function.__init__)


def test_robochart::function_constructor_args():
    sig = inspect.signature(robochart::Function.__init__)
    params = list(sig.parameters.keys())



def test_robochart::operationdef_is_not_abstract():
    assert not inspect.isabstract(robochart::OperationDef)


def test_robochart::operationdef_constructor_exists():
    assert callable(robochart::OperationDef.__init__)


def test_robochart::operationdef_constructor_args():
    sig = inspect.signature(robochart::OperationDef.__init__)
    params = list(sig.parameters.keys())



def test_robochart::rcmodule_is_not_abstract():
    assert not inspect.isabstract(robochart::RCModule)


def test_robochart::rcmodule_constructor_exists():
    assert callable(robochart::RCModule.__init__)


def test_robochart::rcmodule_constructor_args():
    sig = inspect.signature(robochart::RCModule.__init__)
    params = list(sig.parameters.keys())



def test_robochart::controllerdef_is_not_abstract():
    assert not inspect.isabstract(robochart::ControllerDef)


def test_robochart::controllerdef_constructor_exists():
    assert callable(robochart::ControllerDef.__init__)


def test_robochart::controllerdef_constructor_args():
    sig = inspect.signature(robochart::ControllerDef.__init__)
    params = list(sig.parameters.keys())



def test_robochart::roboticplatformdef_is_not_abstract():
    assert not inspect.isabstract(robochart::RoboticPlatformDef)


def test_robochart::roboticplatformdef_constructor_exists():
    assert callable(robochart::RoboticPlatformDef.__init__)


def test_robochart::roboticplatformdef_constructor_args():
    sig = inspect.signature(robochart::RoboticPlatformDef.__init__)
    params = list(sig.parameters.keys())



def test_robochart::interface_is_not_abstract():
    assert not inspect.isabstract(robochart::Interface)


def test_robochart::interface_constructor_exists():
    assert callable(robochart::Interface.__init__)


def test_robochart::interface_constructor_args():
    sig = inspect.signature(robochart::Interface.__init__)
    params = list(sig.parameters.keys())



def test_basicpackage_is_not_abstract():
    assert not inspect.isabstract(BasicPackage)


def test_basicpackage_constructor_exists():
    assert callable(BasicPackage.__init__)


def test_basicpackage_constructor_args():
    sig = inspect.signature(BasicPackage.__init__)
    params = list(sig.parameters.keys())



def test_robochart::rcpackage_is_not_abstract():
    assert not inspect.isabstract(robochart::RCPackage)


def test_robochart::rcpackage_constructor_exists():
    assert callable(robochart::RCPackage.__init__)


def test_robochart::rcpackage_constructor_args():
    sig = inspect.signature(robochart::RCPackage.__init__)
    params = list(sig.parameters.keys())



def test_robochart::import_is_not_abstract():
    assert not inspect.isabstract(robochart::Import)


def test_robochart::import_constructor_exists():
    assert callable(robochart::Import.__init__)


def test_robochart::import_constructor_args():
    sig = inspect.signature(robochart::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_robochart::import_has_importedNamespace():
    assert hasattr(robochart::Import, "importedNamespace")
    descriptor = None
    for klass in robochart::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_robochart::basicpackage_is_not_abstract():
    assert not inspect.isabstract(robochart::BasicPackage)


def test_robochart::basicpackage_constructor_exists():
    assert callable(robochart::BasicPackage.__init__)


def test_robochart::basicpackage_constructor_args():
    sig = inspect.signature(robochart::BasicPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_robochart::basicpackage_has_name():
    assert hasattr(robochart::BasicPackage, "name")
    descriptor = None
    for klass in robochart::BasicPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_triggertype_exists():
    # Check that the Enumeration exists
    assert TriggerType is not None

def test_triggertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerType]
    expected_literals = [
        "SIMPLE",
        "EMPTY",
        "SYNC",
        "OUTPUT",
        "INPUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerType"

def test_variablemodifier_exists():
    # Check that the Enumeration exists
    assert VariableModifier is not None

def test_variablemodifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariableModifier]
    expected_literals = [
        "VAR",
        "CONST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariableModifier"


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
Assignable_strategy = st.builds(
    Assignable,
)
robochart::ArrayAssignable_strategy = st.builds(
    robochart::ArrayAssignable,
)
robochart::VarRef_strategy = st.builds(
    robochart::VarRef,
)
robochart::VarSelection_strategy = st.builds(
    robochart::VarSelection,
)
robochart::NamedExpression_strategy = st.builds(
    robochart::NamedExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
robochart::Different_strategy = st.builds(
    robochart::Different,
)
robochart::LessOrEqual_strategy = st.builds(
    robochart::LessOrEqual,
)
robochart::GreaterOrEqual_strategy = st.builds(
    robochart::GreaterOrEqual,
)
robochart::And_strategy = st.builds(
    robochart::And,
)
robochart::Minus_strategy = st.builds(
    robochart::Minus,
)
robochart::Mult_strategy = st.builds(
    robochart::Mult,
)
robochart::GreaterThan_strategy = st.builds(
    robochart::GreaterThan,
)
robochart::Or_strategy = st.builds(
    robochart::Or,
)
robochart::Div_strategy = st.builds(
    robochart::Div,
)
robochart::Cat_strategy = st.builds(
    robochart::Cat,
)
robochart::Equals_strategy = st.builds(
    robochart::Equals,
)
robochart::Implies_strategy = st.builds(
    robochart::Implies,
)
robochart::Modulus_strategy = st.builds(
    robochart::Modulus,
)
robochart::Plus_strategy = st.builds(
    robochart::Plus,
)
robochart::LessThan_strategy = st.builds(
    robochart::LessThan,
)
robochart::Iff_strategy = st.builds(
    robochart::Iff,
)
LambdaExp_strategy = st.builds(
    LambdaExp,
)
robochart::DefiniteDescription_strategy = st.builds(
    robochart::DefiniteDescription,
)
QuantifierExpression_strategy = st.builds(
    QuantifierExpression,
)
robochart::Exists_strategy = st.builds(
    robochart::Exists,
    unique=
        st.booleans()
)
robochart::Forall_strategy = st.builds(
    robochart::Forall,
)
Expression_strategy = st.builds(
    Expression,
)
robochart::LetExpression_strategy = st.builds(
    robochart::LetExpression,
)
robochart::RefExp_strategy = st.builds(
    robochart::RefExp,
)
robochart::StringExp_strategy = st.builds(
    robochart::StringExp,
    value=
        safe_text
)
robochart::IsExp_strategy = st.builds(
    robochart::IsExp,
)
robochart::IdExp_strategy = st.builds(
    robochart::IdExp,
)
robochart::IntegerExp_strategy = st.builds(
    robochart::IntegerExp,
    value=
        st.integers()
)
robochart::Not_strategy = st.builds(
    robochart::Not,
)
robochart::TupleExp_strategy = st.builds(
    robochart::TupleExp,
)
robochart::SetExp_strategy = st.builds(
    robochart::SetExp,
)
robochart::StateClockExp_strategy = st.builds(
    robochart::StateClockExp,
)
robochart::IfExpression_strategy = st.builds(
    robochart::IfExpression,
)
robochart::SetRange_strategy = st.builds(
    robochart::SetRange,
)
robochart::EnumExp_strategy = st.builds(
    robochart::EnumExp,
)
robochart::FromExp_strategy = st.builds(
    robochart::FromExp,
)
robochart::ToExp_strategy = st.builds(
    robochart::ToExp,
)
robochart::AsExp_strategy = st.builds(
    robochart::AsExp,
)
robochart::FloatExp_strategy = st.builds(
    robochart::FloatExp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
robochart::ParExp_strategy = st.builds(
    robochart::ParExp,
)
robochart::Neg_strategy = st.builds(
    robochart::Neg,
)
robochart::ArrayExp_strategy = st.builds(
    robochart::ArrayExp,
)
robochart::CallExp_strategy = st.builds(
    robochart::CallExp,
)
robochart::ElseExp_strategy = st.builds(
    robochart::ElseExp,
)
robochart::LambdaExp_strategy = st.builds(
    robochart::LambdaExp,
)
robochart::SetComp_strategy = st.builds(
    robochart::SetComp,
)
robochart::QuantifierExpression_strategy = st.builds(
    robochart::QuantifierExpression,
)
robochart::WaitingConditionRef_strategy = st.builds(
    robochart::WaitingConditionRef,
)
robochart::ClockExp_strategy = st.builds(
    robochart::ClockExp,
)
robochart::InExp_strategy = st.builds(
    robochart::InExp,
)
robochart::BooleanExp_strategy = st.builds(
    robochart::BooleanExp,
    value=
        safe_text
)
robochart::Selection_strategy = st.builds(
    robochart::Selection,
)
robochart::BinaryExpression_strategy = st.builds(
    robochart::BinaryExpression,
)
robochart::TypeExp_strategy = st.builds(
    robochart::TypeExp,
)
robochart::SeqExp_strategy = st.builds(
    robochart::SeqExp,
)
robochart::VarExp_strategy = st.builds(
    robochart::VarExp,
)
robochart::RangeExp_strategy = st.builds(
    robochart::RangeExp,
    linterval=
        safe_text,
    rinterval=
        safe_text
)
robochart::ResultExp_strategy = st.builds(
    robochart::ResultExp,
)
robochart::Assignable_strategy = st.builds(
    robochart::Assignable,
)
Statement_strategy = st.builds(
    Statement,
)
robochart::SendEvent_strategy = st.builds(
    robochart::SendEvent,
)
robochart::IfStmt_strategy = st.builds(
    robochart::IfStmt,
)
robochart::Wait_strategy = st.builds(
    robochart::Wait,
)
robochart::ParStmt_strategy = st.builds(
    robochart::ParStmt,
)
robochart::Assignment_strategy = st.builds(
    robochart::Assignment,
)
robochart::Skip_strategy = st.builds(
    robochart::Skip,
)
robochart::Call_strategy = st.builds(
    robochart::Call,
)
robochart::SeqStatement_strategy = st.builds(
    robochart::SeqStatement,
)
robochart::TimedStatement_strategy = st.builds(
    robochart::TimedStatement,
)
robochart::ClockReset_strategy = st.builds(
    robochart::ClockReset,
)
robochart::ConnectionNode_strategy = st.builds(
    robochart::ConnectionNode,
)
robochart::Connection_strategy = st.builds(
    robochart::Connection,
    async_=
        st.booleans(),
    bidirec=
        st.booleans()
)
Controller_strategy = st.builds(
    Controller,
)
robochart::ControllerRef_strategy = st.builds(
    robochart::ControllerRef,
)
Action_strategy = st.builds(
    Action,
)
robochart::ExitAction_strategy = st.builds(
    robochart::ExitAction,
)
robochart::DuringAction_strategy = st.builds(
    robochart::DuringAction,
)
robochart::EntryAction_strategy = st.builds(
    robochart::EntryAction,
)
State_strategy = st.builds(
    State,
)
robochart::Final_strategy = st.builds(
    robochart::Final,
)
robochart::Action_strategy = st.builds(
    robochart::Action,
)
Junction_strategy = st.builds(
    Junction,
)
robochart::Initial_strategy = st.builds(
    robochart::Initial,
)
Node_strategy = st.builds(
    Node,
)
robochart::Junction_strategy = st.builds(
    robochart::Junction,
)
robochart::Statement_strategy = st.builds(
    robochart::Statement,
)
robochart::Trigger_strategy = st.builds(
    robochart::Trigger,
    _type=
        safe_text
)
robochart::ProbabilisticJunction_strategy = st.builds(
    robochart::ProbabilisticJunction,
)
RoboticPlatform_strategy = st.builds(
    RoboticPlatform,
)
Context_strategy = st.builds(
    Context,
)
robochart::NodeContainer_strategy = st.builds(
    robochart::NodeContainer,
)
NodeContainer_strategy = st.builds(
    NodeContainer,
)
robochart::State_strategy = st.builds(
    robochart::State,
)
robochart::StateMachineBody_strategy = st.builds(
    robochart::StateMachineBody,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
Variable_strategy = st.builds(
    Variable,
)
robochart::BasicContext_strategy = st.builds(
    robochart::BasicContext,
)
BasicContext_strategy = st.builds(
    BasicContext,
)
robochart::Context_strategy = st.builds(
    robochart::Context,
)
Reference_strategy = st.builds(
    Reference,
)
robochart::StateMachineRef_strategy = st.builds(
    robochart::StateMachineRef,
)
robochart::RoboticPlatformRef_strategy = st.builds(
    robochart::RoboticPlatformRef,
)
robochart::Reference_strategy = st.builds(
    robochart::Reference,
)
StateMachineBody_strategy = st.builds(
    StateMachineBody,
)
OperationSig_strategy = st.builds(
    OperationSig,
)
Operation_strategy = st.builds(
    Operation,
)
robochart::OperationRef_strategy = st.builds(
    robochart::OperationRef,
)
ConnectionNode_strategy = st.builds(
    ConnectionNode,
)
robochart::VariableList_strategy = st.builds(
    robochart::VariableList,
    modifier=
        safe_text
)
SetType_strategy = st.builds(
    SetType,
)
robochart::SeqType_strategy = st.builds(
    robochart::SeqType,
)
RelationType_strategy = st.builds(
    RelationType,
)
robochart::FunctionType_strategy = st.builds(
    robochart::FunctionType,
)
robochart::Parameter_strategy = st.builds(
    robochart::Parameter,
)
robochart::Expression_strategy = st.builds(
    robochart::Expression,
)
TypedNamedElement_strategy = st.builds(
    TypedNamedElement,
)
robochart::Member_strategy = st.builds(
    robochart::Member,
)
robochart::Type_strategy = st.builds(
    robochart::Type,
)
NamedExpression_strategy = st.builds(
    NamedExpression,
)
Member_strategy = st.builds(
    Member,
)
robochart::Variable_strategy = st.builds(
    robochart::Variable,
    modifier=
        safe_text
)
robochart::Field_strategy = st.builds(
    robochart::Field,
)
Type_strategy = st.builds(
    Type,
)
robochart::SetType_strategy = st.builds(
    robochart::SetType,
)
robochart::TypeRef_strategy = st.builds(
    robochart::TypeRef,
)
robochart::VectorType_strategy = st.builds(
    robochart::VectorType,
    size=
        st.integers()
)
robochart::RelationType_strategy = st.builds(
    robochart::RelationType,
)
robochart::AnyType_strategy = st.builds(
    robochart::AnyType,
    identifier=
        safe_text
)
robochart::MatrixType_strategy = st.builds(
    robochart::MatrixType,
    columns=
        st.integers(),
    rows=
        st.integers()
)
robochart::ProductType_strategy = st.builds(
    robochart::ProductType,
)
robochart::StateMachineDef_strategy = st.builds(
    robochart::StateMachineDef,
)
TypeDecl_strategy = st.builds(
    TypeDecl,
)
robochart::Literal_strategy = st.builds(
    robochart::Literal,
)
robochart::Enumeration_strategy = st.builds(
    robochart::Enumeration,
)
robochart::RecordType_strategy = st.builds(
    robochart::RecordType,
)
robochart::NameType_strategy = st.builds(
    robochart::NameType,
)
robochart::PrimitiveType_strategy = st.builds(
    robochart::PrimitiveType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
robochart::RoboticPlatform_strategy = st.builds(
    robochart::RoboticPlatform,
)
robochart::Operation_strategy = st.builds(
    robochart::Operation,
)
robochart::TypedNamedElement_strategy = st.builds(
    robochart::TypedNamedElement,
)
robochart::Transition_strategy = st.builds(
    robochart::Transition,
)
robochart::Event_strategy = st.builds(
    robochart::Event,
    broadcast=
        st.booleans()
)
robochart::WaitingCondition_strategy = st.builds(
    robochart::WaitingCondition,
)
robochart::TypeDecl_strategy = st.builds(
    robochart::TypeDecl,
)
robochart::Declaration_strategy = st.builds(
    robochart::Declaration,
)
robochart::Clock_strategy = st.builds(
    robochart::Clock,
)
robochart::Node_strategy = st.builds(
    robochart::Node,
)
robochart::OperationSig_strategy = st.builds(
    robochart::OperationSig,
    terminates=
        st.booleans()
)
robochart::StateMachine_strategy = st.builds(
    robochart::StateMachine,
)
robochart::Controller_strategy = st.builds(
    robochart::Controller,
)
robochart::NamedElement_strategy = st.builds(
    robochart::NamedElement,
    name=
        safe_text
)
robochart::Function_strategy = st.builds(
    robochart::Function,
)
robochart::OperationDef_strategy = st.builds(
    robochart::OperationDef,
)
robochart::RCModule_strategy = st.builds(
    robochart::RCModule,
)
robochart::ControllerDef_strategy = st.builds(
    robochart::ControllerDef,
)
robochart::RoboticPlatformDef_strategy = st.builds(
    robochart::RoboticPlatformDef,
)
robochart::Interface_strategy = st.builds(
    robochart::Interface,
)
BasicPackage_strategy = st.builds(
    BasicPackage,
)
robochart::RCPackage_strategy = st.builds(
    robochart::RCPackage,
)
robochart::Import_strategy = st.builds(
    robochart::Import,
    importedNamespace=
        safe_text
)
robochart::BasicPackage_strategy = st.builds(
    robochart::BasicPackage,
    name=
        safe_text
)

@given(instance=Assignable_strategy)
@settings(max_examples=50)
def test_assignable_instantiation(instance):
    assert isinstance(instance, Assignable)

@given(instance=robochart::ArrayAssignable_strategy)
@settings(max_examples=50)
def test_robochart::arrayassignable_instantiation(instance):
    assert isinstance(instance, robochart::ArrayAssignable)

@given(instance=robochart::VarRef_strategy)
@settings(max_examples=50)
def test_robochart::varref_instantiation(instance):
    assert isinstance(instance, robochart::VarRef)

@given(instance=robochart::VarSelection_strategy)
@settings(max_examples=50)
def test_robochart::varselection_instantiation(instance):
    assert isinstance(instance, robochart::VarSelection)

@given(instance=robochart::NamedExpression_strategy)
@settings(max_examples=50)
def test_robochart::namedexpression_instantiation(instance):
    assert isinstance(instance, robochart::NamedExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=robochart::Different_strategy)
@settings(max_examples=50)
def test_robochart::different_instantiation(instance):
    assert isinstance(instance, robochart::Different)

@given(instance=robochart::LessOrEqual_strategy)
@settings(max_examples=50)
def test_robochart::lessorequal_instantiation(instance):
    assert isinstance(instance, robochart::LessOrEqual)

@given(instance=robochart::GreaterOrEqual_strategy)
@settings(max_examples=50)
def test_robochart::greaterorequal_instantiation(instance):
    assert isinstance(instance, robochart::GreaterOrEqual)

@given(instance=robochart::And_strategy)
@settings(max_examples=50)
def test_robochart::and_instantiation(instance):
    assert isinstance(instance, robochart::And)

@given(instance=robochart::Minus_strategy)
@settings(max_examples=50)
def test_robochart::minus_instantiation(instance):
    assert isinstance(instance, robochart::Minus)

@given(instance=robochart::Mult_strategy)
@settings(max_examples=50)
def test_robochart::mult_instantiation(instance):
    assert isinstance(instance, robochart::Mult)

@given(instance=robochart::GreaterThan_strategy)
@settings(max_examples=50)
def test_robochart::greaterthan_instantiation(instance):
    assert isinstance(instance, robochart::GreaterThan)

@given(instance=robochart::Or_strategy)
@settings(max_examples=50)
def test_robochart::or_instantiation(instance):
    assert isinstance(instance, robochart::Or)

@given(instance=robochart::Div_strategy)
@settings(max_examples=50)
def test_robochart::div_instantiation(instance):
    assert isinstance(instance, robochart::Div)

@given(instance=robochart::Cat_strategy)
@settings(max_examples=50)
def test_robochart::cat_instantiation(instance):
    assert isinstance(instance, robochart::Cat)

@given(instance=robochart::Equals_strategy)
@settings(max_examples=50)
def test_robochart::equals_instantiation(instance):
    assert isinstance(instance, robochart::Equals)

@given(instance=robochart::Implies_strategy)
@settings(max_examples=50)
def test_robochart::implies_instantiation(instance):
    assert isinstance(instance, robochart::Implies)

@given(instance=robochart::Modulus_strategy)
@settings(max_examples=50)
def test_robochart::modulus_instantiation(instance):
    assert isinstance(instance, robochart::Modulus)

@given(instance=robochart::Plus_strategy)
@settings(max_examples=50)
def test_robochart::plus_instantiation(instance):
    assert isinstance(instance, robochart::Plus)

@given(instance=robochart::LessThan_strategy)
@settings(max_examples=50)
def test_robochart::lessthan_instantiation(instance):
    assert isinstance(instance, robochart::LessThan)

@given(instance=robochart::Iff_strategy)
@settings(max_examples=50)
def test_robochart::iff_instantiation(instance):
    assert isinstance(instance, robochart::Iff)

@given(instance=LambdaExp_strategy)
@settings(max_examples=50)
def test_lambdaexp_instantiation(instance):
    assert isinstance(instance, LambdaExp)

@given(instance=robochart::DefiniteDescription_strategy)
@settings(max_examples=50)
def test_robochart::definitedescription_instantiation(instance):
    assert isinstance(instance, robochart::DefiniteDescription)

@given(instance=QuantifierExpression_strategy)
@settings(max_examples=50)
def test_quantifierexpression_instantiation(instance):
    assert isinstance(instance, QuantifierExpression)

@given(instance=robochart::Exists_strategy)
@settings(max_examples=50)
def test_robochart::exists_instantiation(instance):
    assert isinstance(instance, robochart::Exists)

@given(instance=robochart::Exists_strategy)
def test_robochart::exists_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=robochart::Exists_strategy)
def test_robochart::exists_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=robochart::Forall_strategy)
@settings(max_examples=50)
def test_robochart::forall_instantiation(instance):
    assert isinstance(instance, robochart::Forall)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=robochart::LetExpression_strategy)
@settings(max_examples=50)
def test_robochart::letexpression_instantiation(instance):
    assert isinstance(instance, robochart::LetExpression)

@given(instance=robochart::RefExp_strategy)
@settings(max_examples=50)
def test_robochart::refexp_instantiation(instance):
    assert isinstance(instance, robochart::RefExp)

@given(instance=robochart::StringExp_strategy)
@settings(max_examples=50)
def test_robochart::stringexp_instantiation(instance):
    assert isinstance(instance, robochart::StringExp)

@given(instance=robochart::StringExp_strategy)
def test_robochart::stringexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=robochart::StringExp_strategy)
def test_robochart::stringexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=robochart::IsExp_strategy)
@settings(max_examples=50)
def test_robochart::isexp_instantiation(instance):
    assert isinstance(instance, robochart::IsExp)

@given(instance=robochart::IdExp_strategy)
@settings(max_examples=50)
def test_robochart::idexp_instantiation(instance):
    assert isinstance(instance, robochart::IdExp)

@given(instance=robochart::IntegerExp_strategy)
@settings(max_examples=50)
def test_robochart::integerexp_instantiation(instance):
    assert isinstance(instance, robochart::IntegerExp)

@given(instance=robochart::IntegerExp_strategy)
def test_robochart::integerexp_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=robochart::IntegerExp_strategy)
def test_robochart::integerexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=robochart::Not_strategy)
@settings(max_examples=50)
def test_robochart::not_instantiation(instance):
    assert isinstance(instance, robochart::Not)

@given(instance=robochart::TupleExp_strategy)
@settings(max_examples=50)
def test_robochart::tupleexp_instantiation(instance):
    assert isinstance(instance, robochart::TupleExp)

@given(instance=robochart::SetExp_strategy)
@settings(max_examples=50)
def test_robochart::setexp_instantiation(instance):
    assert isinstance(instance, robochart::SetExp)

@given(instance=robochart::StateClockExp_strategy)
@settings(max_examples=50)
def test_robochart::stateclockexp_instantiation(instance):
    assert isinstance(instance, robochart::StateClockExp)

@given(instance=robochart::IfExpression_strategy)
@settings(max_examples=50)
def test_robochart::ifexpression_instantiation(instance):
    assert isinstance(instance, robochart::IfExpression)

@given(instance=robochart::SetRange_strategy)
@settings(max_examples=50)
def test_robochart::setrange_instantiation(instance):
    assert isinstance(instance, robochart::SetRange)

@given(instance=robochart::EnumExp_strategy)
@settings(max_examples=50)
def test_robochart::enumexp_instantiation(instance):
    assert isinstance(instance, robochart::EnumExp)

@given(instance=robochart::FromExp_strategy)
@settings(max_examples=50)
def test_robochart::fromexp_instantiation(instance):
    assert isinstance(instance, robochart::FromExp)

@given(instance=robochart::ToExp_strategy)
@settings(max_examples=50)
def test_robochart::toexp_instantiation(instance):
    assert isinstance(instance, robochart::ToExp)

@given(instance=robochart::AsExp_strategy)
@settings(max_examples=50)
def test_robochart::asexp_instantiation(instance):
    assert isinstance(instance, robochart::AsExp)

@given(instance=robochart::FloatExp_strategy)
@settings(max_examples=50)
def test_robochart::floatexp_instantiation(instance):
    assert isinstance(instance, robochart::FloatExp)

@given(instance=robochart::FloatExp_strategy)
def test_robochart::floatexp_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=robochart::FloatExp_strategy)
def test_robochart::floatexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=robochart::ParExp_strategy)
@settings(max_examples=50)
def test_robochart::parexp_instantiation(instance):
    assert isinstance(instance, robochart::ParExp)

@given(instance=robochart::Neg_strategy)
@settings(max_examples=50)
def test_robochart::neg_instantiation(instance):
    assert isinstance(instance, robochart::Neg)

@given(instance=robochart::ArrayExp_strategy)
@settings(max_examples=50)
def test_robochart::arrayexp_instantiation(instance):
    assert isinstance(instance, robochart::ArrayExp)

@given(instance=robochart::CallExp_strategy)
@settings(max_examples=50)
def test_robochart::callexp_instantiation(instance):
    assert isinstance(instance, robochart::CallExp)

@given(instance=robochart::ElseExp_strategy)
@settings(max_examples=50)
def test_robochart::elseexp_instantiation(instance):
    assert isinstance(instance, robochart::ElseExp)

@given(instance=robochart::LambdaExp_strategy)
@settings(max_examples=50)
def test_robochart::lambdaexp_instantiation(instance):
    assert isinstance(instance, robochart::LambdaExp)

@given(instance=robochart::SetComp_strategy)
@settings(max_examples=50)
def test_robochart::setcomp_instantiation(instance):
    assert isinstance(instance, robochart::SetComp)

@given(instance=robochart::QuantifierExpression_strategy)
@settings(max_examples=50)
def test_robochart::quantifierexpression_instantiation(instance):
    assert isinstance(instance, robochart::QuantifierExpression)

@given(instance=robochart::WaitingConditionRef_strategy)
@settings(max_examples=50)
def test_robochart::waitingconditionref_instantiation(instance):
    assert isinstance(instance, robochart::WaitingConditionRef)

@given(instance=robochart::ClockExp_strategy)
@settings(max_examples=50)
def test_robochart::clockexp_instantiation(instance):
    assert isinstance(instance, robochart::ClockExp)

@given(instance=robochart::InExp_strategy)
@settings(max_examples=50)
def test_robochart::inexp_instantiation(instance):
    assert isinstance(instance, robochart::InExp)

@given(instance=robochart::BooleanExp_strategy)
@settings(max_examples=50)
def test_robochart::booleanexp_instantiation(instance):
    assert isinstance(instance, robochart::BooleanExp)

@given(instance=robochart::BooleanExp_strategy)
def test_robochart::booleanexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=robochart::BooleanExp_strategy)
def test_robochart::booleanexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=robochart::Selection_strategy)
@settings(max_examples=50)
def test_robochart::selection_instantiation(instance):
    assert isinstance(instance, robochart::Selection)

@given(instance=robochart::BinaryExpression_strategy)
@settings(max_examples=50)
def test_robochart::binaryexpression_instantiation(instance):
    assert isinstance(instance, robochart::BinaryExpression)

@given(instance=robochart::TypeExp_strategy)
@settings(max_examples=50)
def test_robochart::typeexp_instantiation(instance):
    assert isinstance(instance, robochart::TypeExp)

@given(instance=robochart::SeqExp_strategy)
@settings(max_examples=50)
def test_robochart::seqexp_instantiation(instance):
    assert isinstance(instance, robochart::SeqExp)

@given(instance=robochart::VarExp_strategy)
@settings(max_examples=50)
def test_robochart::varexp_instantiation(instance):
    assert isinstance(instance, robochart::VarExp)

@given(instance=robochart::RangeExp_strategy)
@settings(max_examples=50)
def test_robochart::rangeexp_instantiation(instance):
    assert isinstance(instance, robochart::RangeExp)

@given(instance=robochart::RangeExp_strategy)
def test_robochart::rangeexp_linterval_type(instance):
    assert isinstance(instance.linterval, str)


@given(instance=robochart::RangeExp_strategy)
def test_robochart::rangeexp_linterval_setter(instance):
    original = instance.linterval
    instance.linterval = original
    assert instance.linterval == original

@given(instance=robochart::RangeExp_strategy)
def test_robochart::rangeexp_rinterval_type(instance):
    assert isinstance(instance.rinterval, str)


@given(instance=robochart::RangeExp_strategy)
def test_robochart::rangeexp_rinterval_setter(instance):
    original = instance.rinterval
    instance.rinterval = original
    assert instance.rinterval == original

@given(instance=robochart::ResultExp_strategy)
@settings(max_examples=50)
def test_robochart::resultexp_instantiation(instance):
    assert isinstance(instance, robochart::ResultExp)

@given(instance=robochart::Assignable_strategy)
@settings(max_examples=50)
def test_robochart::assignable_instantiation(instance):
    assert isinstance(instance, robochart::Assignable)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=robochart::SendEvent_strategy)
@settings(max_examples=50)
def test_robochart::sendevent_instantiation(instance):
    assert isinstance(instance, robochart::SendEvent)

@given(instance=robochart::IfStmt_strategy)
@settings(max_examples=50)
def test_robochart::ifstmt_instantiation(instance):
    assert isinstance(instance, robochart::IfStmt)

@given(instance=robochart::Wait_strategy)
@settings(max_examples=50)
def test_robochart::wait_instantiation(instance):
    assert isinstance(instance, robochart::Wait)

@given(instance=robochart::ParStmt_strategy)
@settings(max_examples=50)
def test_robochart::parstmt_instantiation(instance):
    assert isinstance(instance, robochart::ParStmt)

@given(instance=robochart::Assignment_strategy)
@settings(max_examples=50)
def test_robochart::assignment_instantiation(instance):
    assert isinstance(instance, robochart::Assignment)

@given(instance=robochart::Skip_strategy)
@settings(max_examples=50)
def test_robochart::skip_instantiation(instance):
    assert isinstance(instance, robochart::Skip)

@given(instance=robochart::Call_strategy)
@settings(max_examples=50)
def test_robochart::call_instantiation(instance):
    assert isinstance(instance, robochart::Call)

@given(instance=robochart::SeqStatement_strategy)
@settings(max_examples=50)
def test_robochart::seqstatement_instantiation(instance):
    assert isinstance(instance, robochart::SeqStatement)

@given(instance=robochart::TimedStatement_strategy)
@settings(max_examples=50)
def test_robochart::timedstatement_instantiation(instance):
    assert isinstance(instance, robochart::TimedStatement)

@given(instance=robochart::ClockReset_strategy)
@settings(max_examples=50)
def test_robochart::clockreset_instantiation(instance):
    assert isinstance(instance, robochart::ClockReset)

@given(instance=robochart::ConnectionNode_strategy)
@settings(max_examples=50)
def test_robochart::connectionnode_instantiation(instance):
    assert isinstance(instance, robochart::ConnectionNode)

@given(instance=robochart::Connection_strategy)
@settings(max_examples=50)
def test_robochart::connection_instantiation(instance):
    assert isinstance(instance, robochart::Connection)

@given(instance=robochart::Connection_strategy)
def test_robochart::connection_async__type(instance):
    assert isinstance(instance.async_, bool)


@given(instance=robochart::Connection_strategy)
def test_robochart::connection_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=robochart::Connection_strategy)
def test_robochart::connection_bidirec_type(instance):
    assert isinstance(instance.bidirec, bool)


@given(instance=robochart::Connection_strategy)
def test_robochart::connection_bidirec_setter(instance):
    original = instance.bidirec
    instance.bidirec = original
    assert instance.bidirec == original

@given(instance=Controller_strategy)
@settings(max_examples=50)
def test_controller_instantiation(instance):
    assert isinstance(instance, Controller)

@given(instance=robochart::ControllerRef_strategy)
@settings(max_examples=50)
def test_robochart::controllerref_instantiation(instance):
    assert isinstance(instance, robochart::ControllerRef)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=robochart::ExitAction_strategy)
@settings(max_examples=50)
def test_robochart::exitaction_instantiation(instance):
    assert isinstance(instance, robochart::ExitAction)

@given(instance=robochart::DuringAction_strategy)
@settings(max_examples=50)
def test_robochart::duringaction_instantiation(instance):
    assert isinstance(instance, robochart::DuringAction)

@given(instance=robochart::EntryAction_strategy)
@settings(max_examples=50)
def test_robochart::entryaction_instantiation(instance):
    assert isinstance(instance, robochart::EntryAction)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=robochart::Final_strategy)
@settings(max_examples=50)
def test_robochart::final_instantiation(instance):
    assert isinstance(instance, robochart::Final)

@given(instance=robochart::Action_strategy)
@settings(max_examples=50)
def test_robochart::action_instantiation(instance):
    assert isinstance(instance, robochart::Action)

@given(instance=Junction_strategy)
@settings(max_examples=50)
def test_junction_instantiation(instance):
    assert isinstance(instance, Junction)

@given(instance=robochart::Initial_strategy)
@settings(max_examples=50)
def test_robochart::initial_instantiation(instance):
    assert isinstance(instance, robochart::Initial)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=robochart::Junction_strategy)
@settings(max_examples=50)
def test_robochart::junction_instantiation(instance):
    assert isinstance(instance, robochart::Junction)

@given(instance=robochart::Statement_strategy)
@settings(max_examples=50)
def test_robochart::statement_instantiation(instance):
    assert isinstance(instance, robochart::Statement)

@given(instance=robochart::Trigger_strategy)
@settings(max_examples=50)
def test_robochart::trigger_instantiation(instance):
    assert isinstance(instance, robochart::Trigger)

@given(instance=robochart::Trigger_strategy)
def test_robochart::trigger__type_type(instance):
    assert isinstance(instance._type, str)


@given(instance=robochart::Trigger_strategy)
def test_robochart::trigger__type_setter(instance):
    original = instance._type
    instance._type = original
    assert instance._type == original

@given(instance=robochart::ProbabilisticJunction_strategy)
@settings(max_examples=50)
def test_robochart::probabilisticjunction_instantiation(instance):
    assert isinstance(instance, robochart::ProbabilisticJunction)

@given(instance=RoboticPlatform_strategy)
@settings(max_examples=50)
def test_roboticplatform_instantiation(instance):
    assert isinstance(instance, RoboticPlatform)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=robochart::NodeContainer_strategy)
@settings(max_examples=50)
def test_robochart::nodecontainer_instantiation(instance):
    assert isinstance(instance, robochart::NodeContainer)

@given(instance=NodeContainer_strategy)
@settings(max_examples=50)
def test_nodecontainer_instantiation(instance):
    assert isinstance(instance, NodeContainer)

@given(instance=robochart::State_strategy)
@settings(max_examples=50)
def test_robochart::state_instantiation(instance):
    assert isinstance(instance, robochart::State)

@given(instance=robochart::StateMachineBody_strategy)
@settings(max_examples=50)
def test_robochart::statemachinebody_instantiation(instance):
    assert isinstance(instance, robochart::StateMachineBody)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=robochart::BasicContext_strategy)
@settings(max_examples=50)
def test_robochart::basiccontext_instantiation(instance):
    assert isinstance(instance, robochart::BasicContext)

@given(instance=BasicContext_strategy)
@settings(max_examples=50)
def test_basiccontext_instantiation(instance):
    assert isinstance(instance, BasicContext)

@given(instance=robochart::Context_strategy)
@settings(max_examples=50)
def test_robochart::context_instantiation(instance):
    assert isinstance(instance, robochart::Context)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=robochart::StateMachineRef_strategy)
@settings(max_examples=50)
def test_robochart::statemachineref_instantiation(instance):
    assert isinstance(instance, robochart::StateMachineRef)

@given(instance=robochart::RoboticPlatformRef_strategy)
@settings(max_examples=50)
def test_robochart::roboticplatformref_instantiation(instance):
    assert isinstance(instance, robochart::RoboticPlatformRef)

@given(instance=robochart::Reference_strategy)
@settings(max_examples=50)
def test_robochart::reference_instantiation(instance):
    assert isinstance(instance, robochart::Reference)

@given(instance=StateMachineBody_strategy)
@settings(max_examples=50)
def test_statemachinebody_instantiation(instance):
    assert isinstance(instance, StateMachineBody)

@given(instance=OperationSig_strategy)
@settings(max_examples=50)
def test_operationsig_instantiation(instance):
    assert isinstance(instance, OperationSig)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=robochart::OperationRef_strategy)
@settings(max_examples=50)
def test_robochart::operationref_instantiation(instance):
    assert isinstance(instance, robochart::OperationRef)

@given(instance=ConnectionNode_strategy)
@settings(max_examples=50)
def test_connectionnode_instantiation(instance):
    assert isinstance(instance, ConnectionNode)

@given(instance=robochart::VariableList_strategy)
@settings(max_examples=50)
def test_robochart::variablelist_instantiation(instance):
    assert isinstance(instance, robochart::VariableList)

@given(instance=robochart::VariableList_strategy)
def test_robochart::variablelist_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=robochart::VariableList_strategy)
def test_robochart::variablelist_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=SetType_strategy)
@settings(max_examples=50)
def test_settype_instantiation(instance):
    assert isinstance(instance, SetType)

@given(instance=robochart::SeqType_strategy)
@settings(max_examples=50)
def test_robochart::seqtype_instantiation(instance):
    assert isinstance(instance, robochart::SeqType)

@given(instance=RelationType_strategy)
@settings(max_examples=50)
def test_relationtype_instantiation(instance):
    assert isinstance(instance, RelationType)

@given(instance=robochart::FunctionType_strategy)
@settings(max_examples=50)
def test_robochart::functiontype_instantiation(instance):
    assert isinstance(instance, robochart::FunctionType)

@given(instance=robochart::Parameter_strategy)
@settings(max_examples=50)
def test_robochart::parameter_instantiation(instance):
    assert isinstance(instance, robochart::Parameter)

@given(instance=robochart::Expression_strategy)
@settings(max_examples=50)
def test_robochart::expression_instantiation(instance):
    assert isinstance(instance, robochart::Expression)

@given(instance=TypedNamedElement_strategy)
@settings(max_examples=50)
def test_typednamedelement_instantiation(instance):
    assert isinstance(instance, TypedNamedElement)

@given(instance=robochart::Member_strategy)
@settings(max_examples=50)
def test_robochart::member_instantiation(instance):
    assert isinstance(instance, robochart::Member)

@given(instance=robochart::Type_strategy)
@settings(max_examples=50)
def test_robochart::type_instantiation(instance):
    assert isinstance(instance, robochart::Type)

@given(instance=NamedExpression_strategy)
@settings(max_examples=50)
def test_namedexpression_instantiation(instance):
    assert isinstance(instance, NamedExpression)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=robochart::Variable_strategy)
@settings(max_examples=50)
def test_robochart::variable_instantiation(instance):
    assert isinstance(instance, robochart::Variable)

@given(instance=robochart::Variable_strategy)
def test_robochart::variable_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=robochart::Variable_strategy)
def test_robochart::variable_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=robochart::Field_strategy)
@settings(max_examples=50)
def test_robochart::field_instantiation(instance):
    assert isinstance(instance, robochart::Field)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=robochart::SetType_strategy)
@settings(max_examples=50)
def test_robochart::settype_instantiation(instance):
    assert isinstance(instance, robochart::SetType)

@given(instance=robochart::TypeRef_strategy)
@settings(max_examples=50)
def test_robochart::typeref_instantiation(instance):
    assert isinstance(instance, robochart::TypeRef)

@given(instance=robochart::VectorType_strategy)
@settings(max_examples=50)
def test_robochart::vectortype_instantiation(instance):
    assert isinstance(instance, robochart::VectorType)

@given(instance=robochart::VectorType_strategy)
def test_robochart::vectortype_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=robochart::VectorType_strategy)
def test_robochart::vectortype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=robochart::RelationType_strategy)
@settings(max_examples=50)
def test_robochart::relationtype_instantiation(instance):
    assert isinstance(instance, robochart::RelationType)

@given(instance=robochart::AnyType_strategy)
@settings(max_examples=50)
def test_robochart::anytype_instantiation(instance):
    assert isinstance(instance, robochart::AnyType)

@given(instance=robochart::AnyType_strategy)
def test_robochart::anytype_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=robochart::AnyType_strategy)
def test_robochart::anytype_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=robochart::MatrixType_strategy)
@settings(max_examples=50)
def test_robochart::matrixtype_instantiation(instance):
    assert isinstance(instance, robochart::MatrixType)

@given(instance=robochart::MatrixType_strategy)
def test_robochart::matrixtype_columns_type(instance):
    assert isinstance(instance.columns, int)


@given(instance=robochart::MatrixType_strategy)
def test_robochart::matrixtype_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original

@given(instance=robochart::MatrixType_strategy)
def test_robochart::matrixtype_rows_type(instance):
    assert isinstance(instance.rows, int)


@given(instance=robochart::MatrixType_strategy)
def test_robochart::matrixtype_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original

@given(instance=robochart::ProductType_strategy)
@settings(max_examples=50)
def test_robochart::producttype_instantiation(instance):
    assert isinstance(instance, robochart::ProductType)

@given(instance=robochart::StateMachineDef_strategy)
@settings(max_examples=50)
def test_robochart::statemachinedef_instantiation(instance):
    assert isinstance(instance, robochart::StateMachineDef)

@given(instance=TypeDecl_strategy)
@settings(max_examples=50)
def test_typedecl_instantiation(instance):
    assert isinstance(instance, TypeDecl)

@given(instance=robochart::Literal_strategy)
@settings(max_examples=50)
def test_robochart::literal_instantiation(instance):
    assert isinstance(instance, robochart::Literal)

@given(instance=robochart::Enumeration_strategy)
@settings(max_examples=50)
def test_robochart::enumeration_instantiation(instance):
    assert isinstance(instance, robochart::Enumeration)

@given(instance=robochart::RecordType_strategy)
@settings(max_examples=50)
def test_robochart::recordtype_instantiation(instance):
    assert isinstance(instance, robochart::RecordType)

@given(instance=robochart::NameType_strategy)
@settings(max_examples=50)
def test_robochart::nametype_instantiation(instance):
    assert isinstance(instance, robochart::NameType)

@given(instance=robochart::PrimitiveType_strategy)
@settings(max_examples=50)
def test_robochart::primitivetype_instantiation(instance):
    assert isinstance(instance, robochart::PrimitiveType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=robochart::RoboticPlatform_strategy)
@settings(max_examples=50)
def test_robochart::roboticplatform_instantiation(instance):
    assert isinstance(instance, robochart::RoboticPlatform)

@given(instance=robochart::Operation_strategy)
@settings(max_examples=50)
def test_robochart::operation_instantiation(instance):
    assert isinstance(instance, robochart::Operation)

@given(instance=robochart::TypedNamedElement_strategy)
@settings(max_examples=50)
def test_robochart::typednamedelement_instantiation(instance):
    assert isinstance(instance, robochart::TypedNamedElement)

@given(instance=robochart::Transition_strategy)
@settings(max_examples=50)
def test_robochart::transition_instantiation(instance):
    assert isinstance(instance, robochart::Transition)

@given(instance=robochart::Event_strategy)
@settings(max_examples=50)
def test_robochart::event_instantiation(instance):
    assert isinstance(instance, robochart::Event)

@given(instance=robochart::Event_strategy)
def test_robochart::event_broadcast_type(instance):
    assert isinstance(instance.broadcast, bool)


@given(instance=robochart::Event_strategy)
def test_robochart::event_broadcast_setter(instance):
    original = instance.broadcast
    instance.broadcast = original
    assert instance.broadcast == original

@given(instance=robochart::WaitingCondition_strategy)
@settings(max_examples=50)
def test_robochart::waitingcondition_instantiation(instance):
    assert isinstance(instance, robochart::WaitingCondition)

@given(instance=robochart::TypeDecl_strategy)
@settings(max_examples=50)
def test_robochart::typedecl_instantiation(instance):
    assert isinstance(instance, robochart::TypeDecl)

@given(instance=robochart::Declaration_strategy)
@settings(max_examples=50)
def test_robochart::declaration_instantiation(instance):
    assert isinstance(instance, robochart::Declaration)

@given(instance=robochart::Clock_strategy)
@settings(max_examples=50)
def test_robochart::clock_instantiation(instance):
    assert isinstance(instance, robochart::Clock)

@given(instance=robochart::Node_strategy)
@settings(max_examples=50)
def test_robochart::node_instantiation(instance):
    assert isinstance(instance, robochart::Node)

@given(instance=robochart::OperationSig_strategy)
@settings(max_examples=50)
def test_robochart::operationsig_instantiation(instance):
    assert isinstance(instance, robochart::OperationSig)

@given(instance=robochart::OperationSig_strategy)
def test_robochart::operationsig_terminates_type(instance):
    assert isinstance(instance.terminates, bool)


@given(instance=robochart::OperationSig_strategy)
def test_robochart::operationsig_terminates_setter(instance):
    original = instance.terminates
    instance.terminates = original
    assert instance.terminates == original

@given(instance=robochart::StateMachine_strategy)
@settings(max_examples=50)
def test_robochart::statemachine_instantiation(instance):
    assert isinstance(instance, robochart::StateMachine)

@given(instance=robochart::Controller_strategy)
@settings(max_examples=50)
def test_robochart::controller_instantiation(instance):
    assert isinstance(instance, robochart::Controller)

@given(instance=robochart::NamedElement_strategy)
@settings(max_examples=50)
def test_robochart::namedelement_instantiation(instance):
    assert isinstance(instance, robochart::NamedElement)

@given(instance=robochart::NamedElement_strategy)
def test_robochart::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=robochart::NamedElement_strategy)
def test_robochart::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=robochart::Function_strategy)
@settings(max_examples=50)
def test_robochart::function_instantiation(instance):
    assert isinstance(instance, robochart::Function)

@given(instance=robochart::OperationDef_strategy)
@settings(max_examples=50)
def test_robochart::operationdef_instantiation(instance):
    assert isinstance(instance, robochart::OperationDef)

@given(instance=robochart::RCModule_strategy)
@settings(max_examples=50)
def test_robochart::rcmodule_instantiation(instance):
    assert isinstance(instance, robochart::RCModule)

@given(instance=robochart::ControllerDef_strategy)
@settings(max_examples=50)
def test_robochart::controllerdef_instantiation(instance):
    assert isinstance(instance, robochart::ControllerDef)

@given(instance=robochart::RoboticPlatformDef_strategy)
@settings(max_examples=50)
def test_robochart::roboticplatformdef_instantiation(instance):
    assert isinstance(instance, robochart::RoboticPlatformDef)

@given(instance=robochart::Interface_strategy)
@settings(max_examples=50)
def test_robochart::interface_instantiation(instance):
    assert isinstance(instance, robochart::Interface)

@given(instance=BasicPackage_strategy)
@settings(max_examples=50)
def test_basicpackage_instantiation(instance):
    assert isinstance(instance, BasicPackage)

@given(instance=robochart::RCPackage_strategy)
@settings(max_examples=50)
def test_robochart::rcpackage_instantiation(instance):
    assert isinstance(instance, robochart::RCPackage)

@given(instance=robochart::Import_strategy)
@settings(max_examples=50)
def test_robochart::import_instantiation(instance):
    assert isinstance(instance, robochart::Import)

@given(instance=robochart::Import_strategy)
def test_robochart::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=robochart::Import_strategy)
def test_robochart::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=robochart::BasicPackage_strategy)
@settings(max_examples=50)
def test_robochart::basicpackage_instantiation(instance):
    assert isinstance(instance, robochart::BasicPackage)

@given(instance=robochart::BasicPackage_strategy)
def test_robochart::basicpackage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=robochart::BasicPackage_strategy)
def test_robochart::basicpackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
