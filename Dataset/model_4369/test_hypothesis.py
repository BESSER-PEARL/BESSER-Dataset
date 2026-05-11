import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    klangexpr::Statement,
    klangexpr::Expression,
    Statement,
    klangexpr::Sleep,
    klangexpr::ForeverLoop,
    klangexpr::If,
    klangexpr::SendMessage,
    klangexpr::WhileLoop,
    Operator,
    klangexpr::BinaryOperator,
    klangexpr::UnaryOperator,
    Expression,
    klangexpr::Operator,
    klangexpr::DoubleLiteral,
    klangexpr::VariableReference,
    klangexpr::IntegerLiteral,
    klangexpr::FunctionCall,
    klangexpr::StringLiteral,
    klangexpr::BooleanLiteral,
    UnaryOperator,
    klangexpr::UnaryMinus,
    klangexpr::ToDouble,
    klangexpr::ToInt,
    klangexpr::Not,
    BinaryOperator,
    klangexpr::Plus,
    klangexpr::LessThan,
    klangexpr::And,
    klangexpr::GreaterThan,
    klangexpr::GreaterThanOrEqual,
    klangexpr::LessThanOrEqual,
    klangexpr::Equal,
    klangexpr::Divide,
    klangexpr::Minus,
    klangexpr::Multiply,
    klangexpr::Or,
    klangexpr::VariableAssignment,
    klangexpr::Yield,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_klangexpr::statement_is_not_abstract():
    assert not inspect.isabstract(klangexpr::Statement)


def test_klangexpr::statement_constructor_exists():
    assert callable(klangexpr::Statement.__init__)


def test_klangexpr::statement_constructor_args():
    sig = inspect.signature(klangexpr::Statement.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::expression_is_not_abstract():
    assert not inspect.isabstract(klangexpr::Expression)


def test_klangexpr::expression_constructor_exists():
    assert callable(klangexpr::Expression.__init__)


def test_klangexpr::expression_constructor_args():
    sig = inspect.signature(klangexpr::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::sleep_is_not_abstract():
    assert not inspect.isabstract(klangexpr::Sleep)


def test_klangexpr::sleep_constructor_exists():
    assert callable(klangexpr::Sleep.__init__)


def test_klangexpr::sleep_constructor_args():
    sig = inspect.signature(klangexpr::Sleep.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::foreverloop_is_not_abstract():
    assert not inspect.isabstract(klangexpr::ForeverLoop)


def test_klangexpr::foreverloop_constructor_exists():
    assert callable(klangexpr::ForeverLoop.__init__)


def test_klangexpr::foreverloop_constructor_args():
    sig = inspect.signature(klangexpr::ForeverLoop.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::if_is_not_abstract():
    assert not inspect.isabstract(klangexpr::If)


def test_klangexpr::if_constructor_exists():
    assert callable(klangexpr::If.__init__)


def test_klangexpr::if_constructor_args():
    sig = inspect.signature(klangexpr::If.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::sendmessage_is_not_abstract():
    assert not inspect.isabstract(klangexpr::SendMessage)


def test_klangexpr::sendmessage_constructor_exists():
    assert callable(klangexpr::SendMessage.__init__)


def test_klangexpr::sendmessage_constructor_args():
    sig = inspect.signature(klangexpr::SendMessage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_klangexpr::sendmessage_has_name():
    assert hasattr(klangexpr::SendMessage, "name")
    descriptor = None
    for klass in klangexpr::SendMessage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_klangexpr::whileloop_is_not_abstract():
    assert not inspect.isabstract(klangexpr::WhileLoop)


def test_klangexpr::whileloop_constructor_exists():
    assert callable(klangexpr::WhileLoop.__init__)


def test_klangexpr::whileloop_constructor_args():
    sig = inspect.signature(klangexpr::WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(klangexpr::BinaryOperator)


def test_klangexpr::binaryoperator_constructor_exists():
    assert callable(klangexpr::BinaryOperator.__init__)


def test_klangexpr::binaryoperator_constructor_args():
    sig = inspect.signature(klangexpr::BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(klangexpr::UnaryOperator)


def test_klangexpr::unaryoperator_constructor_exists():
    assert callable(klangexpr::UnaryOperator.__init__)


def test_klangexpr::unaryoperator_constructor_args():
    sig = inspect.signature(klangexpr::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::operator_is_not_abstract():
    assert not inspect.isabstract(klangexpr::Operator)


def test_klangexpr::operator_constructor_exists():
    assert callable(klangexpr::Operator.__init__)


def test_klangexpr::operator_constructor_args():
    sig = inspect.signature(klangexpr::Operator.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(klangexpr::DoubleLiteral)


def test_klangexpr::doubleliteral_constructor_exists():
    assert callable(klangexpr::DoubleLiteral.__init__)


def test_klangexpr::doubleliteral_constructor_args():
    sig = inspect.signature(klangexpr::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_klangexpr::doubleliteral_has_value():
    assert hasattr(klangexpr::DoubleLiteral, "value")
    descriptor = None
    for klass in klangexpr::DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_klangexpr::variablereference_is_not_abstract():
    assert not inspect.isabstract(klangexpr::VariableReference)


def test_klangexpr::variablereference_constructor_exists():
    assert callable(klangexpr::VariableReference.__init__)


def test_klangexpr::variablereference_constructor_args():
    sig = inspect.signature(klangexpr::VariableReference.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_klangexpr::variablereference_has_variableName():
    assert hasattr(klangexpr::VariableReference, "variableName")
    descriptor = None
    for klass in klangexpr::VariableReference.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_klangexpr::integerliteral_is_not_abstract():
    assert not inspect.isabstract(klangexpr::IntegerLiteral)


def test_klangexpr::integerliteral_constructor_exists():
    assert callable(klangexpr::IntegerLiteral.__init__)


def test_klangexpr::integerliteral_constructor_args():
    sig = inspect.signature(klangexpr::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_klangexpr::integerliteral_has_value():
    assert hasattr(klangexpr::IntegerLiteral, "value")
    descriptor = None
    for klass in klangexpr::IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_klangexpr::functioncall_is_not_abstract():
    assert not inspect.isabstract(klangexpr::FunctionCall)


def test_klangexpr::functioncall_constructor_exists():
    assert callable(klangexpr::FunctionCall.__init__)


def test_klangexpr::functioncall_constructor_args():
    sig = inspect.signature(klangexpr::FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_klangexpr::functioncall_has_name():
    assert hasattr(klangexpr::FunctionCall, "name")
    descriptor = None
    for klass in klangexpr::FunctionCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_klangexpr::stringliteral_is_not_abstract():
    assert not inspect.isabstract(klangexpr::StringLiteral)


def test_klangexpr::stringliteral_constructor_exists():
    assert callable(klangexpr::StringLiteral.__init__)


def test_klangexpr::stringliteral_constructor_args():
    sig = inspect.signature(klangexpr::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_klangexpr::stringliteral_has_value():
    assert hasattr(klangexpr::StringLiteral, "value")
    descriptor = None
    for klass in klangexpr::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_klangexpr::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(klangexpr::BooleanLiteral)


def test_klangexpr::booleanliteral_constructor_exists():
    assert callable(klangexpr::BooleanLiteral.__init__)


def test_klangexpr::booleanliteral_constructor_args():
    sig = inspect.signature(klangexpr::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_klangexpr::booleanliteral_has_value():
    assert hasattr(klangexpr::BooleanLiteral, "value")
    descriptor = None
    for klass in klangexpr::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::unaryminus_is_not_abstract():
    assert not inspect.isabstract(klangexpr::UnaryMinus)


def test_klangexpr::unaryminus_constructor_exists():
    assert callable(klangexpr::UnaryMinus.__init__)


def test_klangexpr::unaryminus_constructor_args():
    sig = inspect.signature(klangexpr::UnaryMinus.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::todouble_is_not_abstract():
    assert not inspect.isabstract(klangexpr::ToDouble)


def test_klangexpr::todouble_constructor_exists():
    assert callable(klangexpr::ToDouble.__init__)


def test_klangexpr::todouble_constructor_args():
    sig = inspect.signature(klangexpr::ToDouble.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::toint_is_not_abstract():
    assert not inspect.isabstract(klangexpr::ToInt)


def test_klangexpr::toint_constructor_exists():
    assert callable(klangexpr::ToInt.__init__)


def test_klangexpr::toint_constructor_args():
    sig = inspect.signature(klangexpr::ToInt.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::not_is_not_abstract():
    assert not inspect.isabstract(klangexpr::Not)


def test_klangexpr::not_constructor_exists():
    assert callable(klangexpr::Not.__init__)


def test_klangexpr::not_constructor_args():
    sig = inspect.signature(klangexpr::Not.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::plus_is_not_abstract():
    assert not inspect.isabstract(klangexpr::Plus)


def test_klangexpr::plus_constructor_exists():
    assert callable(klangexpr::Plus.__init__)


def test_klangexpr::plus_constructor_args():
    sig = inspect.signature(klangexpr::Plus.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::lessthan_is_not_abstract():
    assert not inspect.isabstract(klangexpr::LessThan)


def test_klangexpr::lessthan_constructor_exists():
    assert callable(klangexpr::LessThan.__init__)


def test_klangexpr::lessthan_constructor_args():
    sig = inspect.signature(klangexpr::LessThan.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::and_is_not_abstract():
    assert not inspect.isabstract(klangexpr::And)


def test_klangexpr::and_constructor_exists():
    assert callable(klangexpr::And.__init__)


def test_klangexpr::and_constructor_args():
    sig = inspect.signature(klangexpr::And.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::greaterthan_is_not_abstract():
    assert not inspect.isabstract(klangexpr::GreaterThan)


def test_klangexpr::greaterthan_constructor_exists():
    assert callable(klangexpr::GreaterThan.__init__)


def test_klangexpr::greaterthan_constructor_args():
    sig = inspect.signature(klangexpr::GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(klangexpr::GreaterThanOrEqual)


def test_klangexpr::greaterthanorequal_constructor_exists():
    assert callable(klangexpr::GreaterThanOrEqual.__init__)


def test_klangexpr::greaterthanorequal_constructor_args():
    sig = inspect.signature(klangexpr::GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(klangexpr::LessThanOrEqual)


def test_klangexpr::lessthanorequal_constructor_exists():
    assert callable(klangexpr::LessThanOrEqual.__init__)


def test_klangexpr::lessthanorequal_constructor_args():
    sig = inspect.signature(klangexpr::LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::equal_is_not_abstract():
    assert not inspect.isabstract(klangexpr::Equal)


def test_klangexpr::equal_constructor_exists():
    assert callable(klangexpr::Equal.__init__)


def test_klangexpr::equal_constructor_args():
    sig = inspect.signature(klangexpr::Equal.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::divide_is_not_abstract():
    assert not inspect.isabstract(klangexpr::Divide)


def test_klangexpr::divide_constructor_exists():
    assert callable(klangexpr::Divide.__init__)


def test_klangexpr::divide_constructor_args():
    sig = inspect.signature(klangexpr::Divide.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::minus_is_not_abstract():
    assert not inspect.isabstract(klangexpr::Minus)


def test_klangexpr::minus_constructor_exists():
    assert callable(klangexpr::Minus.__init__)


def test_klangexpr::minus_constructor_args():
    sig = inspect.signature(klangexpr::Minus.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::multiply_is_not_abstract():
    assert not inspect.isabstract(klangexpr::Multiply)


def test_klangexpr::multiply_constructor_exists():
    assert callable(klangexpr::Multiply.__init__)


def test_klangexpr::multiply_constructor_args():
    sig = inspect.signature(klangexpr::Multiply.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::or_is_not_abstract():
    assert not inspect.isabstract(klangexpr::Or)


def test_klangexpr::or_constructor_exists():
    assert callable(klangexpr::Or.__init__)


def test_klangexpr::or_constructor_args():
    sig = inspect.signature(klangexpr::Or.__init__)
    params = list(sig.parameters.keys())



def test_klangexpr::variableassignment_is_not_abstract():
    assert not inspect.isabstract(klangexpr::VariableAssignment)


def test_klangexpr::variableassignment_constructor_exists():
    assert callable(klangexpr::VariableAssignment.__init__)


def test_klangexpr::variableassignment_constructor_args():
    sig = inspect.signature(klangexpr::VariableAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_klangexpr::variableassignment_has_variableName():
    assert hasattr(klangexpr::VariableAssignment, "variableName")
    descriptor = None
    for klass in klangexpr::VariableAssignment.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_klangexpr::yield_is_not_abstract():
    assert not inspect.isabstract(klangexpr::Yield)


def test_klangexpr::yield_constructor_exists():
    assert callable(klangexpr::Yield.__init__)


def test_klangexpr::yield_constructor_args():
    sig = inspect.signature(klangexpr::Yield.__init__)
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
klangexpr::Statement_strategy = st.builds(
    klangexpr::Statement,
)
klangexpr::Expression_strategy = st.builds(
    klangexpr::Expression,
)
Statement_strategy = st.builds(
    Statement,
)
klangexpr::Sleep_strategy = st.builds(
    klangexpr::Sleep,
)
klangexpr::ForeverLoop_strategy = st.builds(
    klangexpr::ForeverLoop,
)
klangexpr::If_strategy = st.builds(
    klangexpr::If,
)
klangexpr::SendMessage_strategy = st.builds(
    klangexpr::SendMessage,
    name=
        safe_text
)
klangexpr::WhileLoop_strategy = st.builds(
    klangexpr::WhileLoop,
)
Operator_strategy = st.builds(
    Operator,
)
klangexpr::BinaryOperator_strategy = st.builds(
    klangexpr::BinaryOperator,
)
klangexpr::UnaryOperator_strategy = st.builds(
    klangexpr::UnaryOperator,
)
Expression_strategy = st.builds(
    Expression,
)
klangexpr::Operator_strategy = st.builds(
    klangexpr::Operator,
)
klangexpr::DoubleLiteral_strategy = st.builds(
    klangexpr::DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
klangexpr::VariableReference_strategy = st.builds(
    klangexpr::VariableReference,
    variableName=
        safe_text
)
klangexpr::IntegerLiteral_strategy = st.builds(
    klangexpr::IntegerLiteral,
    value=
        st.integers()
)
klangexpr::FunctionCall_strategy = st.builds(
    klangexpr::FunctionCall,
    name=
        safe_text
)
klangexpr::StringLiteral_strategy = st.builds(
    klangexpr::StringLiteral,
    value=
        safe_text
)
klangexpr::BooleanLiteral_strategy = st.builds(
    klangexpr::BooleanLiteral,
    value=
        st.booleans()
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
klangexpr::UnaryMinus_strategy = st.builds(
    klangexpr::UnaryMinus,
)
klangexpr::ToDouble_strategy = st.builds(
    klangexpr::ToDouble,
)
klangexpr::ToInt_strategy = st.builds(
    klangexpr::ToInt,
)
klangexpr::Not_strategy = st.builds(
    klangexpr::Not,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
klangexpr::Plus_strategy = st.builds(
    klangexpr::Plus,
)
klangexpr::LessThan_strategy = st.builds(
    klangexpr::LessThan,
)
klangexpr::And_strategy = st.builds(
    klangexpr::And,
)
klangexpr::GreaterThan_strategy = st.builds(
    klangexpr::GreaterThan,
)
klangexpr::GreaterThanOrEqual_strategy = st.builds(
    klangexpr::GreaterThanOrEqual,
)
klangexpr::LessThanOrEqual_strategy = st.builds(
    klangexpr::LessThanOrEqual,
)
klangexpr::Equal_strategy = st.builds(
    klangexpr::Equal,
)
klangexpr::Divide_strategy = st.builds(
    klangexpr::Divide,
)
klangexpr::Minus_strategy = st.builds(
    klangexpr::Minus,
)
klangexpr::Multiply_strategy = st.builds(
    klangexpr::Multiply,
)
klangexpr::Or_strategy = st.builds(
    klangexpr::Or,
)
klangexpr::VariableAssignment_strategy = st.builds(
    klangexpr::VariableAssignment,
    variableName=
        safe_text
)
klangexpr::Yield_strategy = st.builds(
    klangexpr::Yield,
)

@given(instance=klangexpr::Statement_strategy)
@settings(max_examples=50)
def test_klangexpr::statement_instantiation(instance):
    assert isinstance(instance, klangexpr::Statement)

@given(instance=klangexpr::Expression_strategy)
@settings(max_examples=50)
def test_klangexpr::expression_instantiation(instance):
    assert isinstance(instance, klangexpr::Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=klangexpr::Sleep_strategy)
@settings(max_examples=50)
def test_klangexpr::sleep_instantiation(instance):
    assert isinstance(instance, klangexpr::Sleep)

@given(instance=klangexpr::ForeverLoop_strategy)
@settings(max_examples=50)
def test_klangexpr::foreverloop_instantiation(instance):
    assert isinstance(instance, klangexpr::ForeverLoop)

@given(instance=klangexpr::If_strategy)
@settings(max_examples=50)
def test_klangexpr::if_instantiation(instance):
    assert isinstance(instance, klangexpr::If)

@given(instance=klangexpr::SendMessage_strategy)
@settings(max_examples=50)
def test_klangexpr::sendmessage_instantiation(instance):
    assert isinstance(instance, klangexpr::SendMessage)

@given(instance=klangexpr::SendMessage_strategy)
def test_klangexpr::sendmessage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=klangexpr::SendMessage_strategy)
def test_klangexpr::sendmessage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=klangexpr::WhileLoop_strategy)
@settings(max_examples=50)
def test_klangexpr::whileloop_instantiation(instance):
    assert isinstance(instance, klangexpr::WhileLoop)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=klangexpr::BinaryOperator_strategy)
@settings(max_examples=50)
def test_klangexpr::binaryoperator_instantiation(instance):
    assert isinstance(instance, klangexpr::BinaryOperator)

@given(instance=klangexpr::UnaryOperator_strategy)
@settings(max_examples=50)
def test_klangexpr::unaryoperator_instantiation(instance):
    assert isinstance(instance, klangexpr::UnaryOperator)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=klangexpr::Operator_strategy)
@settings(max_examples=50)
def test_klangexpr::operator_instantiation(instance):
    assert isinstance(instance, klangexpr::Operator)

@given(instance=klangexpr::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_klangexpr::doubleliteral_instantiation(instance):
    assert isinstance(instance, klangexpr::DoubleLiteral)

@given(instance=klangexpr::DoubleLiteral_strategy)
def test_klangexpr::doubleliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=klangexpr::DoubleLiteral_strategy)
def test_klangexpr::doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=klangexpr::VariableReference_strategy)
@settings(max_examples=50)
def test_klangexpr::variablereference_instantiation(instance):
    assert isinstance(instance, klangexpr::VariableReference)

@given(instance=klangexpr::VariableReference_strategy)
def test_klangexpr::variablereference_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=klangexpr::VariableReference_strategy)
def test_klangexpr::variablereference_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=klangexpr::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_klangexpr::integerliteral_instantiation(instance):
    assert isinstance(instance, klangexpr::IntegerLiteral)

@given(instance=klangexpr::IntegerLiteral_strategy)
def test_klangexpr::integerliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=klangexpr::IntegerLiteral_strategy)
def test_klangexpr::integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=klangexpr::FunctionCall_strategy)
@settings(max_examples=50)
def test_klangexpr::functioncall_instantiation(instance):
    assert isinstance(instance, klangexpr::FunctionCall)

@given(instance=klangexpr::FunctionCall_strategy)
def test_klangexpr::functioncall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=klangexpr::FunctionCall_strategy)
def test_klangexpr::functioncall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=klangexpr::StringLiteral_strategy)
@settings(max_examples=50)
def test_klangexpr::stringliteral_instantiation(instance):
    assert isinstance(instance, klangexpr::StringLiteral)

@given(instance=klangexpr::StringLiteral_strategy)
def test_klangexpr::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=klangexpr::StringLiteral_strategy)
def test_klangexpr::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=klangexpr::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_klangexpr::booleanliteral_instantiation(instance):
    assert isinstance(instance, klangexpr::BooleanLiteral)

@given(instance=klangexpr::BooleanLiteral_strategy)
def test_klangexpr::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=klangexpr::BooleanLiteral_strategy)
def test_klangexpr::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=klangexpr::UnaryMinus_strategy)
@settings(max_examples=50)
def test_klangexpr::unaryminus_instantiation(instance):
    assert isinstance(instance, klangexpr::UnaryMinus)

@given(instance=klangexpr::ToDouble_strategy)
@settings(max_examples=50)
def test_klangexpr::todouble_instantiation(instance):
    assert isinstance(instance, klangexpr::ToDouble)

@given(instance=klangexpr::ToInt_strategy)
@settings(max_examples=50)
def test_klangexpr::toint_instantiation(instance):
    assert isinstance(instance, klangexpr::ToInt)

@given(instance=klangexpr::Not_strategy)
@settings(max_examples=50)
def test_klangexpr::not_instantiation(instance):
    assert isinstance(instance, klangexpr::Not)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=klangexpr::Plus_strategy)
@settings(max_examples=50)
def test_klangexpr::plus_instantiation(instance):
    assert isinstance(instance, klangexpr::Plus)

@given(instance=klangexpr::LessThan_strategy)
@settings(max_examples=50)
def test_klangexpr::lessthan_instantiation(instance):
    assert isinstance(instance, klangexpr::LessThan)

@given(instance=klangexpr::And_strategy)
@settings(max_examples=50)
def test_klangexpr::and_instantiation(instance):
    assert isinstance(instance, klangexpr::And)

@given(instance=klangexpr::GreaterThan_strategy)
@settings(max_examples=50)
def test_klangexpr::greaterthan_instantiation(instance):
    assert isinstance(instance, klangexpr::GreaterThan)

@given(instance=klangexpr::GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_klangexpr::greaterthanorequal_instantiation(instance):
    assert isinstance(instance, klangexpr::GreaterThanOrEqual)

@given(instance=klangexpr::LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_klangexpr::lessthanorequal_instantiation(instance):
    assert isinstance(instance, klangexpr::LessThanOrEqual)

@given(instance=klangexpr::Equal_strategy)
@settings(max_examples=50)
def test_klangexpr::equal_instantiation(instance):
    assert isinstance(instance, klangexpr::Equal)

@given(instance=klangexpr::Divide_strategy)
@settings(max_examples=50)
def test_klangexpr::divide_instantiation(instance):
    assert isinstance(instance, klangexpr::Divide)

@given(instance=klangexpr::Minus_strategy)
@settings(max_examples=50)
def test_klangexpr::minus_instantiation(instance):
    assert isinstance(instance, klangexpr::Minus)

@given(instance=klangexpr::Multiply_strategy)
@settings(max_examples=50)
def test_klangexpr::multiply_instantiation(instance):
    assert isinstance(instance, klangexpr::Multiply)

@given(instance=klangexpr::Or_strategy)
@settings(max_examples=50)
def test_klangexpr::or_instantiation(instance):
    assert isinstance(instance, klangexpr::Or)

@given(instance=klangexpr::VariableAssignment_strategy)
@settings(max_examples=50)
def test_klangexpr::variableassignment_instantiation(instance):
    assert isinstance(instance, klangexpr::VariableAssignment)

@given(instance=klangexpr::VariableAssignment_strategy)
def test_klangexpr::variableassignment_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=klangexpr::VariableAssignment_strategy)
def test_klangexpr::variableassignment_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=klangexpr::Yield_strategy)
@settings(max_examples=50)
def test_klangexpr::yield_instantiation(instance):
    assert isinstance(instance, klangexpr::Yield)
