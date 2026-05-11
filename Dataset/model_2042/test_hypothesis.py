import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StringExpression,
    urml::ConcatenateExpression,
    urml::StringExpression,
    urml::Identifiable,
    Literal,
    urml::BoolLiteral,
    urml::FunctionCall,
    urml::IntLiteral,
    Expression,
    urml::UnaryExpression,
    urml::Plus,
    urml::ConditionalOrExpression,
    urml::GreaterThanOrEqual,
    urml::LessThanOrEqual,
    urml::Literal,
    urml::Multiply,
    urml::Divide,
    urml::Minus,
    urml::ConditionalAndExpression,
    urml::Modulo,
    urml::GreaterThan,
    urml::NotEqual,
    urml::Equal,
    urml::Identifier,
    urml::LessThan,
    urml::NotBooleanExpression,
    Statement,
    urml::IfStatement,
    urml::Statement,
    urml::WhileLoop,
    urml::ActionCode,
    urml::Transition,
    urml::State::,
    StatementOperation,
    urml::ReturnStatement,
    urml::Invoke,
    urml::SendTrigger,
    urml::LogStatement,
    urml::NoOp,
    urml::IfStatementOperation,
    urml::Assignment,
    urml::Variable,
    urml::InformTimer,
    urml::WhileLoopOperation,
    urml::StatementOperation,
    urml::Trigger::out,
    Identifiable,
    urml::Assignable,
    urml::IncomingVariable,
    urml::Trigger::in,
    urml::Connector,
    urml::CapsuleInst,
    urml::LogPort,
    urml::TimerPort,
    urml::Port,
    urml::OperationCode,
    urml::StateMachine,
    urml::Operation,
    urml::Signal,
    urml::Expression,
    Assignable,
    urml::Attribute,
    urml::LocalVar,
    urml::Protocol,
    urml::Capsule,
    urml::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stringexpression_is_not_abstract():
    assert not inspect.isabstract(StringExpression)


def test_stringexpression_constructor_exists():
    assert callable(StringExpression.__init__)


def test_stringexpression_constructor_args():
    sig = inspect.signature(StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_urml::concatenateexpression_is_not_abstract():
    assert not inspect.isabstract(urml::ConcatenateExpression)


def test_urml::concatenateexpression_constructor_exists():
    assert callable(urml::ConcatenateExpression.__init__)


def test_urml::concatenateexpression_constructor_args():
    sig = inspect.signature(urml::ConcatenateExpression.__init__)
    params = list(sig.parameters.keys())



def test_urml::stringexpression_is_not_abstract():
    assert not inspect.isabstract(urml::StringExpression)


def test_urml::stringexpression_constructor_exists():
    assert callable(urml::StringExpression.__init__)


def test_urml::stringexpression_constructor_args():
    sig = inspect.signature(urml::StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "str" in params, "Missing parameter 'str'"

def test_urml::stringexpression_has_str():
    assert hasattr(urml::StringExpression, "str")
    descriptor = None
    for klass in urml::StringExpression.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)



def test_urml::identifiable_is_not_abstract():
    assert not inspect.isabstract(urml::Identifiable)


def test_urml::identifiable_constructor_exists():
    assert callable(urml::Identifiable.__init__)


def test_urml::identifiable_constructor_args():
    sig = inspect.signature(urml::Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isBool" in params, "Missing parameter 'isBool'"
    assert "isInt" in params, "Missing parameter 'isInt'"

def test_urml::identifiable_has_name():
    assert hasattr(urml::Identifiable, "name")
    descriptor = None
    for klass in urml::Identifiable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_urml::identifiable_has_isBool():
    assert hasattr(urml::Identifiable, "isBool")
    descriptor = None
    for klass in urml::Identifiable.__mro__:
        if "isBool" in klass.__dict__:
            descriptor = klass.__dict__["isBool"]
            break
    assert isinstance(descriptor, property)

def test_urml::identifiable_has_isInt():
    assert hasattr(urml::Identifiable, "isInt")
    descriptor = None
    for klass in urml::Identifiable.__mro__:
        if "isInt" in klass.__dict__:
            descriptor = klass.__dict__["isInt"]
            break
    assert isinstance(descriptor, property)



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_urml::boolliteral_is_not_abstract():
    assert not inspect.isabstract(urml::BoolLiteral)


def test_urml::boolliteral_constructor_exists():
    assert callable(urml::BoolLiteral.__init__)


def test_urml::boolliteral_constructor_args():
    sig = inspect.signature(urml::BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "true" in params, "Missing parameter 'true'"

def test_urml::boolliteral_has_true():
    assert hasattr(urml::BoolLiteral, "true")
    descriptor = None
    for klass in urml::BoolLiteral.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)



def test_urml::functioncall_is_not_abstract():
    assert not inspect.isabstract(urml::FunctionCall)


def test_urml::functioncall_constructor_exists():
    assert callable(urml::FunctionCall.__init__)


def test_urml::functioncall_constructor_args():
    sig = inspect.signature(urml::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_urml::intliteral_is_not_abstract():
    assert not inspect.isabstract(urml::IntLiteral)


def test_urml::intliteral_constructor_exists():
    assert callable(urml::IntLiteral.__init__)


def test_urml::intliteral_constructor_args():
    sig = inspect.signature(urml::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "int" in params, "Missing parameter 'int'"

def test_urml::intliteral_has_int():
    assert hasattr(urml::IntLiteral, "int")
    descriptor = None
    for klass in urml::IntLiteral.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_urml::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(urml::UnaryExpression)


def test_urml::unaryexpression_constructor_exists():
    assert callable(urml::UnaryExpression.__init__)


def test_urml::unaryexpression_constructor_args():
    sig = inspect.signature(urml::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_urml::plus_is_not_abstract():
    assert not inspect.isabstract(urml::Plus)


def test_urml::plus_constructor_exists():
    assert callable(urml::Plus.__init__)


def test_urml::plus_constructor_args():
    sig = inspect.signature(urml::Plus.__init__)
    params = list(sig.parameters.keys())



def test_urml::conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(urml::ConditionalOrExpression)


def test_urml::conditionalorexpression_constructor_exists():
    assert callable(urml::ConditionalOrExpression.__init__)


def test_urml::conditionalorexpression_constructor_args():
    sig = inspect.signature(urml::ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_urml::greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(urml::GreaterThanOrEqual)


def test_urml::greaterthanorequal_constructor_exists():
    assert callable(urml::GreaterThanOrEqual.__init__)


def test_urml::greaterthanorequal_constructor_args():
    sig = inspect.signature(urml::GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_urml::lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(urml::LessThanOrEqual)


def test_urml::lessthanorequal_constructor_exists():
    assert callable(urml::LessThanOrEqual.__init__)


def test_urml::lessthanorequal_constructor_args():
    sig = inspect.signature(urml::LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_urml::literal_is_not_abstract():
    assert not inspect.isabstract(urml::Literal)


def test_urml::literal_constructor_exists():
    assert callable(urml::Literal.__init__)


def test_urml::literal_constructor_args():
    sig = inspect.signature(urml::Literal.__init__)
    params = list(sig.parameters.keys())



def test_urml::multiply_is_not_abstract():
    assert not inspect.isabstract(urml::Multiply)


def test_urml::multiply_constructor_exists():
    assert callable(urml::Multiply.__init__)


def test_urml::multiply_constructor_args():
    sig = inspect.signature(urml::Multiply.__init__)
    params = list(sig.parameters.keys())



def test_urml::divide_is_not_abstract():
    assert not inspect.isabstract(urml::Divide)


def test_urml::divide_constructor_exists():
    assert callable(urml::Divide.__init__)


def test_urml::divide_constructor_args():
    sig = inspect.signature(urml::Divide.__init__)
    params = list(sig.parameters.keys())



def test_urml::minus_is_not_abstract():
    assert not inspect.isabstract(urml::Minus)


def test_urml::minus_constructor_exists():
    assert callable(urml::Minus.__init__)


def test_urml::minus_constructor_args():
    sig = inspect.signature(urml::Minus.__init__)
    params = list(sig.parameters.keys())



def test_urml::conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(urml::ConditionalAndExpression)


def test_urml::conditionalandexpression_constructor_exists():
    assert callable(urml::ConditionalAndExpression.__init__)


def test_urml::conditionalandexpression_constructor_args():
    sig = inspect.signature(urml::ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_urml::modulo_is_not_abstract():
    assert not inspect.isabstract(urml::Modulo)


def test_urml::modulo_constructor_exists():
    assert callable(urml::Modulo.__init__)


def test_urml::modulo_constructor_args():
    sig = inspect.signature(urml::Modulo.__init__)
    params = list(sig.parameters.keys())



def test_urml::greaterthan_is_not_abstract():
    assert not inspect.isabstract(urml::GreaterThan)


def test_urml::greaterthan_constructor_exists():
    assert callable(urml::GreaterThan.__init__)


def test_urml::greaterthan_constructor_args():
    sig = inspect.signature(urml::GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_urml::notequal_is_not_abstract():
    assert not inspect.isabstract(urml::NotEqual)


def test_urml::notequal_constructor_exists():
    assert callable(urml::NotEqual.__init__)


def test_urml::notequal_constructor_args():
    sig = inspect.signature(urml::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_urml::equal_is_not_abstract():
    assert not inspect.isabstract(urml::Equal)


def test_urml::equal_constructor_exists():
    assert callable(urml::Equal.__init__)


def test_urml::equal_constructor_args():
    sig = inspect.signature(urml::Equal.__init__)
    params = list(sig.parameters.keys())



def test_urml::identifier_is_not_abstract():
    assert not inspect.isabstract(urml::Identifier)


def test_urml::identifier_constructor_exists():
    assert callable(urml::Identifier.__init__)


def test_urml::identifier_constructor_args():
    sig = inspect.signature(urml::Identifier.__init__)
    params = list(sig.parameters.keys())



def test_urml::lessthan_is_not_abstract():
    assert not inspect.isabstract(urml::LessThan)


def test_urml::lessthan_constructor_exists():
    assert callable(urml::LessThan.__init__)


def test_urml::lessthan_constructor_args():
    sig = inspect.signature(urml::LessThan.__init__)
    params = list(sig.parameters.keys())



def test_urml::notbooleanexpression_is_not_abstract():
    assert not inspect.isabstract(urml::NotBooleanExpression)


def test_urml::notbooleanexpression_constructor_exists():
    assert callable(urml::NotBooleanExpression.__init__)


def test_urml::notbooleanexpression_constructor_args():
    sig = inspect.signature(urml::NotBooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_urml::ifstatement_is_not_abstract():
    assert not inspect.isabstract(urml::IfStatement)


def test_urml::ifstatement_constructor_exists():
    assert callable(urml::IfStatement.__init__)


def test_urml::ifstatement_constructor_args():
    sig = inspect.signature(urml::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_urml::statement_is_not_abstract():
    assert not inspect.isabstract(urml::Statement)


def test_urml::statement_constructor_exists():
    assert callable(urml::Statement.__init__)


def test_urml::statement_constructor_args():
    sig = inspect.signature(urml::Statement.__init__)
    params = list(sig.parameters.keys())



def test_urml::whileloop_is_not_abstract():
    assert not inspect.isabstract(urml::WhileLoop)


def test_urml::whileloop_constructor_exists():
    assert callable(urml::WhileLoop.__init__)


def test_urml::whileloop_constructor_args():
    sig = inspect.signature(urml::WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_urml::actioncode_is_not_abstract():
    assert not inspect.isabstract(urml::ActionCode)


def test_urml::actioncode_constructor_exists():
    assert callable(urml::ActionCode.__init__)


def test_urml::actioncode_constructor_args():
    sig = inspect.signature(urml::ActionCode.__init__)
    params = list(sig.parameters.keys())



def test_urml::transition_is_not_abstract():
    assert not inspect.isabstract(urml::Transition)


def test_urml::transition_constructor_exists():
    assert callable(urml::Transition.__init__)


def test_urml::transition_constructor_args():
    sig = inspect.signature(urml::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "init" in params, "Missing parameter 'init'"
    assert "universal" in params, "Missing parameter 'universal'"
    assert "name" in params, "Missing parameter 'name'"

def test_urml::transition_has_init():
    assert hasattr(urml::Transition, "init")
    descriptor = None
    for klass in urml::Transition.__mro__:
        if "init" in klass.__dict__:
            descriptor = klass.__dict__["init"]
            break
    assert isinstance(descriptor, property)

def test_urml::transition_has_universal():
    assert hasattr(urml::Transition, "universal")
    descriptor = None
    for klass in urml::Transition.__mro__:
        if "universal" in klass.__dict__:
            descriptor = klass.__dict__["universal"]
            break
    assert isinstance(descriptor, property)

def test_urml::transition_has_name():
    assert hasattr(urml::Transition, "name")
    descriptor = None
    for klass in urml::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml::state::_is_not_abstract():
    assert not inspect.isabstract(urml::State::)


def test_urml::state::_constructor_exists():
    assert callable(urml::State::.__init__)


def test_urml::state::_constructor_args():
    sig = inspect.signature(urml::State::.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "final" in params, "Missing parameter 'final'"

def test_urml::state::_has_name():
    assert hasattr(urml::State::, "name")
    descriptor = None
    for klass in urml::State::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_urml::state::_has_final():
    assert hasattr(urml::State::, "final")
    descriptor = None
    for klass in urml::State::.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_statementoperation_is_not_abstract():
    assert not inspect.isabstract(StatementOperation)


def test_statementoperation_constructor_exists():
    assert callable(StatementOperation.__init__)


def test_statementoperation_constructor_args():
    sig = inspect.signature(StatementOperation.__init__)
    params = list(sig.parameters.keys())



def test_urml::returnstatement_is_not_abstract():
    assert not inspect.isabstract(urml::ReturnStatement)


def test_urml::returnstatement_constructor_exists():
    assert callable(urml::ReturnStatement.__init__)


def test_urml::returnstatement_constructor_args():
    sig = inspect.signature(urml::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_urml::invoke_is_not_abstract():
    assert not inspect.isabstract(urml::Invoke)


def test_urml::invoke_constructor_exists():
    assert callable(urml::Invoke.__init__)


def test_urml::invoke_constructor_args():
    sig = inspect.signature(urml::Invoke.__init__)
    params = list(sig.parameters.keys())



def test_urml::sendtrigger_is_not_abstract():
    assert not inspect.isabstract(urml::SendTrigger)


def test_urml::sendtrigger_constructor_exists():
    assert callable(urml::SendTrigger.__init__)


def test_urml::sendtrigger_constructor_args():
    sig = inspect.signature(urml::SendTrigger.__init__)
    params = list(sig.parameters.keys())



def test_urml::logstatement_is_not_abstract():
    assert not inspect.isabstract(urml::LogStatement)


def test_urml::logstatement_constructor_exists():
    assert callable(urml::LogStatement.__init__)


def test_urml::logstatement_constructor_args():
    sig = inspect.signature(urml::LogStatement.__init__)
    params = list(sig.parameters.keys())



def test_urml::noop_is_not_abstract():
    assert not inspect.isabstract(urml::NoOp)


def test_urml::noop_constructor_exists():
    assert callable(urml::NoOp.__init__)


def test_urml::noop_constructor_args():
    sig = inspect.signature(urml::NoOp.__init__)
    params = list(sig.parameters.keys())



def test_urml::ifstatementoperation_is_not_abstract():
    assert not inspect.isabstract(urml::IfStatementOperation)


def test_urml::ifstatementoperation_constructor_exists():
    assert callable(urml::IfStatementOperation.__init__)


def test_urml::ifstatementoperation_constructor_args():
    sig = inspect.signature(urml::IfStatementOperation.__init__)
    params = list(sig.parameters.keys())



def test_urml::assignment_is_not_abstract():
    assert not inspect.isabstract(urml::Assignment)


def test_urml::assignment_constructor_exists():
    assert callable(urml::Assignment.__init__)


def test_urml::assignment_constructor_args():
    sig = inspect.signature(urml::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_urml::variable_is_not_abstract():
    assert not inspect.isabstract(urml::Variable)


def test_urml::variable_constructor_exists():
    assert callable(urml::Variable.__init__)


def test_urml::variable_constructor_args():
    sig = inspect.signature(urml::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "assign" in params, "Missing parameter 'assign'"

def test_urml::variable_has_assign():
    assert hasattr(urml::Variable, "assign")
    descriptor = None
    for klass in urml::Variable.__mro__:
        if "assign" in klass.__dict__:
            descriptor = klass.__dict__["assign"]
            break
    assert isinstance(descriptor, property)



def test_urml::informtimer_is_not_abstract():
    assert not inspect.isabstract(urml::InformTimer)


def test_urml::informtimer_constructor_exists():
    assert callable(urml::InformTimer.__init__)


def test_urml::informtimer_constructor_args():
    sig = inspect.signature(urml::InformTimer.__init__)
    params = list(sig.parameters.keys())



def test_urml::whileloopoperation_is_not_abstract():
    assert not inspect.isabstract(urml::WhileLoopOperation)


def test_urml::whileloopoperation_constructor_exists():
    assert callable(urml::WhileLoopOperation.__init__)


def test_urml::whileloopoperation_constructor_args():
    sig = inspect.signature(urml::WhileLoopOperation.__init__)
    params = list(sig.parameters.keys())



def test_urml::statementoperation_is_not_abstract():
    assert not inspect.isabstract(urml::StatementOperation)


def test_urml::statementoperation_constructor_exists():
    assert callable(urml::StatementOperation.__init__)


def test_urml::statementoperation_constructor_args():
    sig = inspect.signature(urml::StatementOperation.__init__)
    params = list(sig.parameters.keys())



def test_urml::trigger::out_is_not_abstract():
    assert not inspect.isabstract(urml::Trigger::out)


def test_urml::trigger::out_constructor_exists():
    assert callable(urml::Trigger::out.__init__)


def test_urml::trigger::out_constructor_args():
    sig = inspect.signature(urml::Trigger::out.__init__)
    params = list(sig.parameters.keys())



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_urml::assignable_is_not_abstract():
    assert not inspect.isabstract(urml::Assignable)


def test_urml::assignable_constructor_exists():
    assert callable(urml::Assignable.__init__)


def test_urml::assignable_constructor_args():
    sig = inspect.signature(urml::Assignable.__init__)
    params = list(sig.parameters.keys())



def test_urml::incomingvariable_is_not_abstract():
    assert not inspect.isabstract(urml::IncomingVariable)


def test_urml::incomingvariable_constructor_exists():
    assert callable(urml::IncomingVariable.__init__)


def test_urml::incomingvariable_constructor_args():
    sig = inspect.signature(urml::IncomingVariable.__init__)
    params = list(sig.parameters.keys())



def test_urml::trigger::in_is_not_abstract():
    assert not inspect.isabstract(urml::Trigger::in)


def test_urml::trigger::in_constructor_exists():
    assert callable(urml::Trigger::in.__init__)


def test_urml::trigger::in_constructor_args():
    sig = inspect.signature(urml::Trigger::in.__init__)
    params = list(sig.parameters.keys())



def test_urml::connector_is_not_abstract():
    assert not inspect.isabstract(urml::Connector)


def test_urml::connector_constructor_exists():
    assert callable(urml::Connector.__init__)


def test_urml::connector_constructor_args():
    sig = inspect.signature(urml::Connector.__init__)
    params = list(sig.parameters.keys())



def test_urml::capsuleinst_is_not_abstract():
    assert not inspect.isabstract(urml::CapsuleInst)


def test_urml::capsuleinst_constructor_exists():
    assert callable(urml::CapsuleInst.__init__)


def test_urml::capsuleinst_constructor_args():
    sig = inspect.signature(urml::CapsuleInst.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_urml::capsuleinst_has_name():
    assert hasattr(urml::CapsuleInst, "name")
    descriptor = None
    for klass in urml::CapsuleInst.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml::logport_is_not_abstract():
    assert not inspect.isabstract(urml::LogPort)


def test_urml::logport_constructor_exists():
    assert callable(urml::LogPort.__init__)


def test_urml::logport_constructor_args():
    sig = inspect.signature(urml::LogPort.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_urml::logport_has_name():
    assert hasattr(urml::LogPort, "name")
    descriptor = None
    for klass in urml::LogPort.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml::timerport_is_not_abstract():
    assert not inspect.isabstract(urml::TimerPort)


def test_urml::timerport_constructor_exists():
    assert callable(urml::TimerPort.__init__)


def test_urml::timerport_constructor_args():
    sig = inspect.signature(urml::TimerPort.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_urml::timerport_has_name():
    assert hasattr(urml::TimerPort, "name")
    descriptor = None
    for klass in urml::TimerPort.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml::port_is_not_abstract():
    assert not inspect.isabstract(urml::Port)


def test_urml::port_constructor_exists():
    assert callable(urml::Port.__init__)


def test_urml::port_constructor_args():
    sig = inspect.signature(urml::Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "conjugated" in params, "Missing parameter 'conjugated'"

def test_urml::port_has_name():
    assert hasattr(urml::Port, "name")
    descriptor = None
    for klass in urml::Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_urml::port_has_conjugated():
    assert hasattr(urml::Port, "conjugated")
    descriptor = None
    for klass in urml::Port.__mro__:
        if "conjugated" in klass.__dict__:
            descriptor = klass.__dict__["conjugated"]
            break
    assert isinstance(descriptor, property)



def test_urml::operationcode_is_not_abstract():
    assert not inspect.isabstract(urml::OperationCode)


def test_urml::operationcode_constructor_exists():
    assert callable(urml::OperationCode.__init__)


def test_urml::operationcode_constructor_args():
    sig = inspect.signature(urml::OperationCode.__init__)
    params = list(sig.parameters.keys())



def test_urml::statemachine_is_not_abstract():
    assert not inspect.isabstract(urml::StateMachine)


def test_urml::statemachine_constructor_exists():
    assert callable(urml::StateMachine.__init__)


def test_urml::statemachine_constructor_args():
    sig = inspect.signature(urml::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_urml::operation_is_not_abstract():
    assert not inspect.isabstract(urml::Operation)


def test_urml::operation_constructor_exists():
    assert callable(urml::Operation.__init__)


def test_urml::operation_constructor_args():
    sig = inspect.signature(urml::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isBool" in params, "Missing parameter 'isBool'"
    assert "isVoid" in params, "Missing parameter 'isVoid'"
    assert "isInt" in params, "Missing parameter 'isInt'"

def test_urml::operation_has_name():
    assert hasattr(urml::Operation, "name")
    descriptor = None
    for klass in urml::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_urml::operation_has_isBool():
    assert hasattr(urml::Operation, "isBool")
    descriptor = None
    for klass in urml::Operation.__mro__:
        if "isBool" in klass.__dict__:
            descriptor = klass.__dict__["isBool"]
            break
    assert isinstance(descriptor, property)

def test_urml::operation_has_isVoid():
    assert hasattr(urml::Operation, "isVoid")
    descriptor = None
    for klass in urml::Operation.__mro__:
        if "isVoid" in klass.__dict__:
            descriptor = klass.__dict__["isVoid"]
            break
    assert isinstance(descriptor, property)

def test_urml::operation_has_isInt():
    assert hasattr(urml::Operation, "isInt")
    descriptor = None
    for klass in urml::Operation.__mro__:
        if "isInt" in klass.__dict__:
            descriptor = klass.__dict__["isInt"]
            break
    assert isinstance(descriptor, property)



def test_urml::signal_is_not_abstract():
    assert not inspect.isabstract(urml::Signal)


def test_urml::signal_constructor_exists():
    assert callable(urml::Signal.__init__)


def test_urml::signal_constructor_args():
    sig = inspect.signature(urml::Signal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_urml::signal_has_name():
    assert hasattr(urml::Signal, "name")
    descriptor = None
    for klass in urml::Signal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml::expression_is_not_abstract():
    assert not inspect.isabstract(urml::Expression)


def test_urml::expression_constructor_exists():
    assert callable(urml::Expression.__init__)


def test_urml::expression_constructor_args():
    sig = inspect.signature(urml::Expression.__init__)
    params = list(sig.parameters.keys())



def test_assignable_is_not_abstract():
    assert not inspect.isabstract(Assignable)


def test_assignable_constructor_exists():
    assert callable(Assignable.__init__)


def test_assignable_constructor_args():
    sig = inspect.signature(Assignable.__init__)
    params = list(sig.parameters.keys())



def test_urml::attribute_is_not_abstract():
    assert not inspect.isabstract(urml::Attribute)


def test_urml::attribute_constructor_exists():
    assert callable(urml::Attribute.__init__)


def test_urml::attribute_constructor_args():
    sig = inspect.signature(urml::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_urml::localvar_is_not_abstract():
    assert not inspect.isabstract(urml::LocalVar)


def test_urml::localvar_constructor_exists():
    assert callable(urml::LocalVar.__init__)


def test_urml::localvar_constructor_args():
    sig = inspect.signature(urml::LocalVar.__init__)
    params = list(sig.parameters.keys())



def test_urml::protocol_is_not_abstract():
    assert not inspect.isabstract(urml::Protocol)


def test_urml::protocol_constructor_exists():
    assert callable(urml::Protocol.__init__)


def test_urml::protocol_constructor_args():
    sig = inspect.signature(urml::Protocol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_urml::protocol_has_name():
    assert hasattr(urml::Protocol, "name")
    descriptor = None
    for klass in urml::Protocol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml::capsule_is_not_abstract():
    assert not inspect.isabstract(urml::Capsule)


def test_urml::capsule_constructor_exists():
    assert callable(urml::Capsule.__init__)


def test_urml::capsule_constructor_args():
    sig = inspect.signature(urml::Capsule.__init__)
    params = list(sig.parameters.keys())
    assert "root" in params, "Missing parameter 'root'"
    assert "name" in params, "Missing parameter 'name'"

def test_urml::capsule_has_root():
    assert hasattr(urml::Capsule, "root")
    descriptor = None
    for klass in urml::Capsule.__mro__:
        if "root" in klass.__dict__:
            descriptor = klass.__dict__["root"]
            break
    assert isinstance(descriptor, property)

def test_urml::capsule_has_name():
    assert hasattr(urml::Capsule, "name")
    descriptor = None
    for klass in urml::Capsule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml::model_is_not_abstract():
    assert not inspect.isabstract(urml::Model)


def test_urml::model_constructor_exists():
    assert callable(urml::Model.__init__)


def test_urml::model_constructor_args():
    sig = inspect.signature(urml::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_urml::model_has_name():
    assert hasattr(urml::Model, "name")
    descriptor = None
    for klass in urml::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
StringExpression_strategy = st.builds(
    StringExpression,
)
urml::ConcatenateExpression_strategy = st.builds(
    urml::ConcatenateExpression,
)
urml::StringExpression_strategy = st.builds(
    urml::StringExpression,
    str=
        safe_text
)
urml::Identifiable_strategy = st.builds(
    urml::Identifiable,
    name=
        safe_text,
    isBool=
        st.booleans(),
    isInt=
        st.booleans()
)
Literal_strategy = st.builds(
    Literal,
)
urml::BoolLiteral_strategy = st.builds(
    urml::BoolLiteral,
    true=
        st.booleans()
)
urml::FunctionCall_strategy = st.builds(
    urml::FunctionCall,
)
urml::IntLiteral_strategy = st.builds(
    urml::IntLiteral,
    int=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
urml::UnaryExpression_strategy = st.builds(
    urml::UnaryExpression,
)
urml::Plus_strategy = st.builds(
    urml::Plus,
)
urml::ConditionalOrExpression_strategy = st.builds(
    urml::ConditionalOrExpression,
)
urml::GreaterThanOrEqual_strategy = st.builds(
    urml::GreaterThanOrEqual,
)
urml::LessThanOrEqual_strategy = st.builds(
    urml::LessThanOrEqual,
)
urml::Literal_strategy = st.builds(
    urml::Literal,
)
urml::Multiply_strategy = st.builds(
    urml::Multiply,
)
urml::Divide_strategy = st.builds(
    urml::Divide,
)
urml::Minus_strategy = st.builds(
    urml::Minus,
)
urml::ConditionalAndExpression_strategy = st.builds(
    urml::ConditionalAndExpression,
)
urml::Modulo_strategy = st.builds(
    urml::Modulo,
)
urml::GreaterThan_strategy = st.builds(
    urml::GreaterThan,
)
urml::NotEqual_strategy = st.builds(
    urml::NotEqual,
)
urml::Equal_strategy = st.builds(
    urml::Equal,
)
urml::Identifier_strategy = st.builds(
    urml::Identifier,
)
urml::LessThan_strategy = st.builds(
    urml::LessThan,
)
urml::NotBooleanExpression_strategy = st.builds(
    urml::NotBooleanExpression,
)
Statement_strategy = st.builds(
    Statement,
)
urml::IfStatement_strategy = st.builds(
    urml::IfStatement,
)
urml::Statement_strategy = st.builds(
    urml::Statement,
)
urml::WhileLoop_strategy = st.builds(
    urml::WhileLoop,
)
urml::ActionCode_strategy = st.builds(
    urml::ActionCode,
)
urml::Transition_strategy = st.builds(
    urml::Transition,
    init=
        st.booleans(),
    universal=
        st.booleans(),
    name=
        safe_text
)
urml::State::_strategy = st.builds(
    urml::State::,
    name=
        safe_text,
    final=
        st.booleans()
)
StatementOperation_strategy = st.builds(
    StatementOperation,
)
urml::ReturnStatement_strategy = st.builds(
    urml::ReturnStatement,
)
urml::Invoke_strategy = st.builds(
    urml::Invoke,
)
urml::SendTrigger_strategy = st.builds(
    urml::SendTrigger,
)
urml::LogStatement_strategy = st.builds(
    urml::LogStatement,
)
urml::NoOp_strategy = st.builds(
    urml::NoOp,
)
urml::IfStatementOperation_strategy = st.builds(
    urml::IfStatementOperation,
)
urml::Assignment_strategy = st.builds(
    urml::Assignment,
)
urml::Variable_strategy = st.builds(
    urml::Variable,
    assign=
        st.booleans()
)
urml::InformTimer_strategy = st.builds(
    urml::InformTimer,
)
urml::WhileLoopOperation_strategy = st.builds(
    urml::WhileLoopOperation,
)
urml::StatementOperation_strategy = st.builds(
    urml::StatementOperation,
)
urml::Trigger::out_strategy = st.builds(
    urml::Trigger::out,
)
Identifiable_strategy = st.builds(
    Identifiable,
)
urml::Assignable_strategy = st.builds(
    urml::Assignable,
)
urml::IncomingVariable_strategy = st.builds(
    urml::IncomingVariable,
)
urml::Trigger::in_strategy = st.builds(
    urml::Trigger::in,
)
urml::Connector_strategy = st.builds(
    urml::Connector,
)
urml::CapsuleInst_strategy = st.builds(
    urml::CapsuleInst,
    name=
        safe_text
)
urml::LogPort_strategy = st.builds(
    urml::LogPort,
    name=
        safe_text
)
urml::TimerPort_strategy = st.builds(
    urml::TimerPort,
    name=
        safe_text
)
urml::Port_strategy = st.builds(
    urml::Port,
    name=
        safe_text,
    conjugated=
        st.booleans()
)
urml::OperationCode_strategy = st.builds(
    urml::OperationCode,
)
urml::StateMachine_strategy = st.builds(
    urml::StateMachine,
)
urml::Operation_strategy = st.builds(
    urml::Operation,
    name=
        safe_text,
    isBool=
        st.booleans(),
    isVoid=
        st.booleans(),
    isInt=
        st.booleans()
)
urml::Signal_strategy = st.builds(
    urml::Signal,
    name=
        safe_text
)
urml::Expression_strategy = st.builds(
    urml::Expression,
)
Assignable_strategy = st.builds(
    Assignable,
)
urml::Attribute_strategy = st.builds(
    urml::Attribute,
)
urml::LocalVar_strategy = st.builds(
    urml::LocalVar,
)
urml::Protocol_strategy = st.builds(
    urml::Protocol,
    name=
        safe_text
)
urml::Capsule_strategy = st.builds(
    urml::Capsule,
    root=
        st.booleans(),
    name=
        safe_text
)
urml::Model_strategy = st.builds(
    urml::Model,
    name=
        safe_text
)

@given(instance=StringExpression_strategy)
@settings(max_examples=50)
def test_stringexpression_instantiation(instance):
    assert isinstance(instance, StringExpression)

@given(instance=urml::ConcatenateExpression_strategy)
@settings(max_examples=50)
def test_urml::concatenateexpression_instantiation(instance):
    assert isinstance(instance, urml::ConcatenateExpression)

@given(instance=urml::StringExpression_strategy)
@settings(max_examples=50)
def test_urml::stringexpression_instantiation(instance):
    assert isinstance(instance, urml::StringExpression)

@given(instance=urml::StringExpression_strategy)
def test_urml::stringexpression_str_type(instance):
    assert isinstance(instance.str, str)


@given(instance=urml::StringExpression_strategy)
def test_urml::stringexpression_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original

@given(instance=urml::Identifiable_strategy)
@settings(max_examples=50)
def test_urml::identifiable_instantiation(instance):
    assert isinstance(instance, urml::Identifiable)

@given(instance=urml::Identifiable_strategy)
def test_urml::identifiable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=urml::Identifiable_strategy)
def test_urml::identifiable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml::Identifiable_strategy)
def test_urml::identifiable_isBool_type(instance):
    assert isinstance(instance.isBool, bool)


@given(instance=urml::Identifiable_strategy)
def test_urml::identifiable_isBool_setter(instance):
    original = instance.isBool
    instance.isBool = original
    assert instance.isBool == original

@given(instance=urml::Identifiable_strategy)
def test_urml::identifiable_isInt_type(instance):
    assert isinstance(instance.isInt, bool)


@given(instance=urml::Identifiable_strategy)
def test_urml::identifiable_isInt_setter(instance):
    original = instance.isInt
    instance.isInt = original
    assert instance.isInt == original

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=urml::BoolLiteral_strategy)
@settings(max_examples=50)
def test_urml::boolliteral_instantiation(instance):
    assert isinstance(instance, urml::BoolLiteral)

@given(instance=urml::BoolLiteral_strategy)
def test_urml::boolliteral_true_type(instance):
    assert isinstance(instance.true, bool)


@given(instance=urml::BoolLiteral_strategy)
def test_urml::boolliteral_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original

@given(instance=urml::FunctionCall_strategy)
@settings(max_examples=50)
def test_urml::functioncall_instantiation(instance):
    assert isinstance(instance, urml::FunctionCall)

@given(instance=urml::IntLiteral_strategy)
@settings(max_examples=50)
def test_urml::intliteral_instantiation(instance):
    assert isinstance(instance, urml::IntLiteral)

@given(instance=urml::IntLiteral_strategy)
def test_urml::intliteral_int_type(instance):
    assert isinstance(instance.int, int)


@given(instance=urml::IntLiteral_strategy)
def test_urml::intliteral_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=urml::UnaryExpression_strategy)
@settings(max_examples=50)
def test_urml::unaryexpression_instantiation(instance):
    assert isinstance(instance, urml::UnaryExpression)

@given(instance=urml::Plus_strategy)
@settings(max_examples=50)
def test_urml::plus_instantiation(instance):
    assert isinstance(instance, urml::Plus)

@given(instance=urml::ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_urml::conditionalorexpression_instantiation(instance):
    assert isinstance(instance, urml::ConditionalOrExpression)

@given(instance=urml::GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_urml::greaterthanorequal_instantiation(instance):
    assert isinstance(instance, urml::GreaterThanOrEqual)

@given(instance=urml::LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_urml::lessthanorequal_instantiation(instance):
    assert isinstance(instance, urml::LessThanOrEqual)

@given(instance=urml::Literal_strategy)
@settings(max_examples=50)
def test_urml::literal_instantiation(instance):
    assert isinstance(instance, urml::Literal)

@given(instance=urml::Multiply_strategy)
@settings(max_examples=50)
def test_urml::multiply_instantiation(instance):
    assert isinstance(instance, urml::Multiply)

@given(instance=urml::Divide_strategy)
@settings(max_examples=50)
def test_urml::divide_instantiation(instance):
    assert isinstance(instance, urml::Divide)

@given(instance=urml::Minus_strategy)
@settings(max_examples=50)
def test_urml::minus_instantiation(instance):
    assert isinstance(instance, urml::Minus)

@given(instance=urml::ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_urml::conditionalandexpression_instantiation(instance):
    assert isinstance(instance, urml::ConditionalAndExpression)

@given(instance=urml::Modulo_strategy)
@settings(max_examples=50)
def test_urml::modulo_instantiation(instance):
    assert isinstance(instance, urml::Modulo)

@given(instance=urml::GreaterThan_strategy)
@settings(max_examples=50)
def test_urml::greaterthan_instantiation(instance):
    assert isinstance(instance, urml::GreaterThan)

@given(instance=urml::NotEqual_strategy)
@settings(max_examples=50)
def test_urml::notequal_instantiation(instance):
    assert isinstance(instance, urml::NotEqual)

@given(instance=urml::Equal_strategy)
@settings(max_examples=50)
def test_urml::equal_instantiation(instance):
    assert isinstance(instance, urml::Equal)

@given(instance=urml::Identifier_strategy)
@settings(max_examples=50)
def test_urml::identifier_instantiation(instance):
    assert isinstance(instance, urml::Identifier)

@given(instance=urml::LessThan_strategy)
@settings(max_examples=50)
def test_urml::lessthan_instantiation(instance):
    assert isinstance(instance, urml::LessThan)

@given(instance=urml::NotBooleanExpression_strategy)
@settings(max_examples=50)
def test_urml::notbooleanexpression_instantiation(instance):
    assert isinstance(instance, urml::NotBooleanExpression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=urml::IfStatement_strategy)
@settings(max_examples=50)
def test_urml::ifstatement_instantiation(instance):
    assert isinstance(instance, urml::IfStatement)

@given(instance=urml::Statement_strategy)
@settings(max_examples=50)
def test_urml::statement_instantiation(instance):
    assert isinstance(instance, urml::Statement)

@given(instance=urml::WhileLoop_strategy)
@settings(max_examples=50)
def test_urml::whileloop_instantiation(instance):
    assert isinstance(instance, urml::WhileLoop)

@given(instance=urml::ActionCode_strategy)
@settings(max_examples=50)
def test_urml::actioncode_instantiation(instance):
    assert isinstance(instance, urml::ActionCode)

@given(instance=urml::Transition_strategy)
@settings(max_examples=50)
def test_urml::transition_instantiation(instance):
    assert isinstance(instance, urml::Transition)

@given(instance=urml::Transition_strategy)
def test_urml::transition_init_type(instance):
    assert isinstance(instance.init, bool)


@given(instance=urml::Transition_strategy)
def test_urml::transition_init_setter(instance):
    original = instance.init
    instance.init = original
    assert instance.init == original

@given(instance=urml::Transition_strategy)
def test_urml::transition_universal_type(instance):
    assert isinstance(instance.universal, bool)


@given(instance=urml::Transition_strategy)
def test_urml::transition_universal_setter(instance):
    original = instance.universal
    instance.universal = original
    assert instance.universal == original

@given(instance=urml::Transition_strategy)
def test_urml::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=urml::Transition_strategy)
def test_urml::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml::State::_strategy)
@settings(max_examples=50)
def test_urml::state::_instantiation(instance):
    assert isinstance(instance, urml::State::)

@given(instance=urml::State::_strategy)
def test_urml::state::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=urml::State::_strategy)
def test_urml::state::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml::State::_strategy)
def test_urml::state::_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=urml::State::_strategy)
def test_urml::state::_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=StatementOperation_strategy)
@settings(max_examples=50)
def test_statementoperation_instantiation(instance):
    assert isinstance(instance, StatementOperation)

@given(instance=urml::ReturnStatement_strategy)
@settings(max_examples=50)
def test_urml::returnstatement_instantiation(instance):
    assert isinstance(instance, urml::ReturnStatement)

@given(instance=urml::Invoke_strategy)
@settings(max_examples=50)
def test_urml::invoke_instantiation(instance):
    assert isinstance(instance, urml::Invoke)

@given(instance=urml::SendTrigger_strategy)
@settings(max_examples=50)
def test_urml::sendtrigger_instantiation(instance):
    assert isinstance(instance, urml::SendTrigger)

@given(instance=urml::LogStatement_strategy)
@settings(max_examples=50)
def test_urml::logstatement_instantiation(instance):
    assert isinstance(instance, urml::LogStatement)

@given(instance=urml::NoOp_strategy)
@settings(max_examples=50)
def test_urml::noop_instantiation(instance):
    assert isinstance(instance, urml::NoOp)

@given(instance=urml::IfStatementOperation_strategy)
@settings(max_examples=50)
def test_urml::ifstatementoperation_instantiation(instance):
    assert isinstance(instance, urml::IfStatementOperation)

@given(instance=urml::Assignment_strategy)
@settings(max_examples=50)
def test_urml::assignment_instantiation(instance):
    assert isinstance(instance, urml::Assignment)

@given(instance=urml::Variable_strategy)
@settings(max_examples=50)
def test_urml::variable_instantiation(instance):
    assert isinstance(instance, urml::Variable)

@given(instance=urml::Variable_strategy)
def test_urml::variable_assign_type(instance):
    assert isinstance(instance.assign, bool)


@given(instance=urml::Variable_strategy)
def test_urml::variable_assign_setter(instance):
    original = instance.assign
    instance.assign = original
    assert instance.assign == original

@given(instance=urml::InformTimer_strategy)
@settings(max_examples=50)
def test_urml::informtimer_instantiation(instance):
    assert isinstance(instance, urml::InformTimer)

@given(instance=urml::WhileLoopOperation_strategy)
@settings(max_examples=50)
def test_urml::whileloopoperation_instantiation(instance):
    assert isinstance(instance, urml::WhileLoopOperation)

@given(instance=urml::StatementOperation_strategy)
@settings(max_examples=50)
def test_urml::statementoperation_instantiation(instance):
    assert isinstance(instance, urml::StatementOperation)

@given(instance=urml::Trigger::out_strategy)
@settings(max_examples=50)
def test_urml::trigger::out_instantiation(instance):
    assert isinstance(instance, urml::Trigger::out)

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=urml::Assignable_strategy)
@settings(max_examples=50)
def test_urml::assignable_instantiation(instance):
    assert isinstance(instance, urml::Assignable)

@given(instance=urml::IncomingVariable_strategy)
@settings(max_examples=50)
def test_urml::incomingvariable_instantiation(instance):
    assert isinstance(instance, urml::IncomingVariable)

@given(instance=urml::Trigger::in_strategy)
@settings(max_examples=50)
def test_urml::trigger::in_instantiation(instance):
    assert isinstance(instance, urml::Trigger::in)

@given(instance=urml::Connector_strategy)
@settings(max_examples=50)
def test_urml::connector_instantiation(instance):
    assert isinstance(instance, urml::Connector)

@given(instance=urml::CapsuleInst_strategy)
@settings(max_examples=50)
def test_urml::capsuleinst_instantiation(instance):
    assert isinstance(instance, urml::CapsuleInst)

@given(instance=urml::CapsuleInst_strategy)
def test_urml::capsuleinst_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=urml::CapsuleInst_strategy)
def test_urml::capsuleinst_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml::LogPort_strategy)
@settings(max_examples=50)
def test_urml::logport_instantiation(instance):
    assert isinstance(instance, urml::LogPort)

@given(instance=urml::LogPort_strategy)
def test_urml::logport_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=urml::LogPort_strategy)
def test_urml::logport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml::TimerPort_strategy)
@settings(max_examples=50)
def test_urml::timerport_instantiation(instance):
    assert isinstance(instance, urml::TimerPort)

@given(instance=urml::TimerPort_strategy)
def test_urml::timerport_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=urml::TimerPort_strategy)
def test_urml::timerport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml::Port_strategy)
@settings(max_examples=50)
def test_urml::port_instantiation(instance):
    assert isinstance(instance, urml::Port)

@given(instance=urml::Port_strategy)
def test_urml::port_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=urml::Port_strategy)
def test_urml::port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml::Port_strategy)
def test_urml::port_conjugated_type(instance):
    assert isinstance(instance.conjugated, bool)


@given(instance=urml::Port_strategy)
def test_urml::port_conjugated_setter(instance):
    original = instance.conjugated
    instance.conjugated = original
    assert instance.conjugated == original

@given(instance=urml::OperationCode_strategy)
@settings(max_examples=50)
def test_urml::operationcode_instantiation(instance):
    assert isinstance(instance, urml::OperationCode)

@given(instance=urml::StateMachine_strategy)
@settings(max_examples=50)
def test_urml::statemachine_instantiation(instance):
    assert isinstance(instance, urml::StateMachine)

@given(instance=urml::Operation_strategy)
@settings(max_examples=50)
def test_urml::operation_instantiation(instance):
    assert isinstance(instance, urml::Operation)

@given(instance=urml::Operation_strategy)
def test_urml::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=urml::Operation_strategy)
def test_urml::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml::Operation_strategy)
def test_urml::operation_isBool_type(instance):
    assert isinstance(instance.isBool, bool)


@given(instance=urml::Operation_strategy)
def test_urml::operation_isBool_setter(instance):
    original = instance.isBool
    instance.isBool = original
    assert instance.isBool == original

@given(instance=urml::Operation_strategy)
def test_urml::operation_isVoid_type(instance):
    assert isinstance(instance.isVoid, bool)


@given(instance=urml::Operation_strategy)
def test_urml::operation_isVoid_setter(instance):
    original = instance.isVoid
    instance.isVoid = original
    assert instance.isVoid == original

@given(instance=urml::Operation_strategy)
def test_urml::operation_isInt_type(instance):
    assert isinstance(instance.isInt, bool)


@given(instance=urml::Operation_strategy)
def test_urml::operation_isInt_setter(instance):
    original = instance.isInt
    instance.isInt = original
    assert instance.isInt == original

@given(instance=urml::Signal_strategy)
@settings(max_examples=50)
def test_urml::signal_instantiation(instance):
    assert isinstance(instance, urml::Signal)

@given(instance=urml::Signal_strategy)
def test_urml::signal_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=urml::Signal_strategy)
def test_urml::signal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml::Expression_strategy)
@settings(max_examples=50)
def test_urml::expression_instantiation(instance):
    assert isinstance(instance, urml::Expression)

@given(instance=Assignable_strategy)
@settings(max_examples=50)
def test_assignable_instantiation(instance):
    assert isinstance(instance, Assignable)

@given(instance=urml::Attribute_strategy)
@settings(max_examples=50)
def test_urml::attribute_instantiation(instance):
    assert isinstance(instance, urml::Attribute)

@given(instance=urml::LocalVar_strategy)
@settings(max_examples=50)
def test_urml::localvar_instantiation(instance):
    assert isinstance(instance, urml::LocalVar)

@given(instance=urml::Protocol_strategy)
@settings(max_examples=50)
def test_urml::protocol_instantiation(instance):
    assert isinstance(instance, urml::Protocol)

@given(instance=urml::Protocol_strategy)
def test_urml::protocol_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=urml::Protocol_strategy)
def test_urml::protocol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml::Capsule_strategy)
@settings(max_examples=50)
def test_urml::capsule_instantiation(instance):
    assert isinstance(instance, urml::Capsule)

@given(instance=urml::Capsule_strategy)
def test_urml::capsule_root_type(instance):
    assert isinstance(instance.root, bool)


@given(instance=urml::Capsule_strategy)
def test_urml::capsule_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original

@given(instance=urml::Capsule_strategy)
def test_urml::capsule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=urml::Capsule_strategy)
def test_urml::capsule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml::Model_strategy)
@settings(max_examples=50)
def test_urml::model_instantiation(instance):
    assert isinstance(instance, urml::Model)

@given(instance=urml::Model_strategy)
def test_urml::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=urml::Model_strategy)
def test_urml::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
