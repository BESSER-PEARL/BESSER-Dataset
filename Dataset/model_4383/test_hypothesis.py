import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    minilang::Statement,
    minilang::VariableRef,
    VariableRef,
    IntOperation,
    minilang::Divide,
    minilang::Multiply,
    minilang::Minus,
    minilang::Plus,
    BooleanOperation,
    minilang::And,
    minilang::Or,
    minilang::BooleanExpression,
    minilang::If,
    IntComparison,
    minilang::LessOrEqual,
    minilang::Greater,
    minilang::Equal,
    BooleanExpression,
    minilang::BooleanOperation,
    minilang::BooleanVariableRef,
    minilang::Not,
    minilang::IntComparison,
    minilang::Boolean,
    IntExpression,
    minilang::IntOperation,
    minilang::IntVariableRef,
    minilang::Integer,
    minilang::IntExpression,
    minilang::Less,
    minilang::GreaterOrEqual,
    minilang::While,
    minilang::Block,
    Statement,
    minilang::IntAssignment,
    minilang::PrintStr,
    minilang::PrintVar,
    minilang::BooleanAssignment,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_minilang::statement_is_not_abstract():
    assert not inspect.isabstract(minilang::Statement)


def test_minilang::statement_constructor_exists():
    assert callable(minilang::Statement.__init__)


def test_minilang::statement_constructor_args():
    sig = inspect.signature(minilang::Statement.__init__)
    params = list(sig.parameters.keys())



def test_minilang::variableref_is_not_abstract():
    assert not inspect.isabstract(minilang::VariableRef)


def test_minilang::variableref_constructor_exists():
    assert callable(minilang::VariableRef.__init__)


def test_minilang::variableref_constructor_args():
    sig = inspect.signature(minilang::VariableRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minilang::variableref_has_name():
    assert hasattr(minilang::VariableRef, "name")
    descriptor = None
    for klass in minilang::VariableRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_variableref_is_not_abstract():
    assert not inspect.isabstract(VariableRef)


def test_variableref_constructor_exists():
    assert callable(VariableRef.__init__)


def test_variableref_constructor_args():
    sig = inspect.signature(VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_intoperation_is_not_abstract():
    assert not inspect.isabstract(IntOperation)


def test_intoperation_constructor_exists():
    assert callable(IntOperation.__init__)


def test_intoperation_constructor_args():
    sig = inspect.signature(IntOperation.__init__)
    params = list(sig.parameters.keys())



def test_minilang::divide_is_not_abstract():
    assert not inspect.isabstract(minilang::Divide)


def test_minilang::divide_constructor_exists():
    assert callable(minilang::Divide.__init__)


def test_minilang::divide_constructor_args():
    sig = inspect.signature(minilang::Divide.__init__)
    params = list(sig.parameters.keys())



def test_minilang::multiply_is_not_abstract():
    assert not inspect.isabstract(minilang::Multiply)


def test_minilang::multiply_constructor_exists():
    assert callable(minilang::Multiply.__init__)


def test_minilang::multiply_constructor_args():
    sig = inspect.signature(minilang::Multiply.__init__)
    params = list(sig.parameters.keys())



def test_minilang::minus_is_not_abstract():
    assert not inspect.isabstract(minilang::Minus)


def test_minilang::minus_constructor_exists():
    assert callable(minilang::Minus.__init__)


def test_minilang::minus_constructor_args():
    sig = inspect.signature(minilang::Minus.__init__)
    params = list(sig.parameters.keys())



def test_minilang::plus_is_not_abstract():
    assert not inspect.isabstract(minilang::Plus)


def test_minilang::plus_constructor_exists():
    assert callable(minilang::Plus.__init__)


def test_minilang::plus_constructor_args():
    sig = inspect.signature(minilang::Plus.__init__)
    params = list(sig.parameters.keys())



def test_booleanoperation_is_not_abstract():
    assert not inspect.isabstract(BooleanOperation)


def test_booleanoperation_constructor_exists():
    assert callable(BooleanOperation.__init__)


def test_booleanoperation_constructor_args():
    sig = inspect.signature(BooleanOperation.__init__)
    params = list(sig.parameters.keys())



def test_minilang::and_is_not_abstract():
    assert not inspect.isabstract(minilang::And)


def test_minilang::and_constructor_exists():
    assert callable(minilang::And.__init__)


def test_minilang::and_constructor_args():
    sig = inspect.signature(minilang::And.__init__)
    params = list(sig.parameters.keys())



def test_minilang::or_is_not_abstract():
    assert not inspect.isabstract(minilang::Or)


def test_minilang::or_constructor_exists():
    assert callable(minilang::Or.__init__)


def test_minilang::or_constructor_args():
    sig = inspect.signature(minilang::Or.__init__)
    params = list(sig.parameters.keys())



def test_minilang::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(minilang::BooleanExpression)


def test_minilang::booleanexpression_constructor_exists():
    assert callable(minilang::BooleanExpression.__init__)


def test_minilang::booleanexpression_constructor_args():
    sig = inspect.signature(minilang::BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_minilang::if_is_not_abstract():
    assert not inspect.isabstract(minilang::If)


def test_minilang::if_constructor_exists():
    assert callable(minilang::If.__init__)


def test_minilang::if_constructor_args():
    sig = inspect.signature(minilang::If.__init__)
    params = list(sig.parameters.keys())



def test_intcomparison_is_not_abstract():
    assert not inspect.isabstract(IntComparison)


def test_intcomparison_constructor_exists():
    assert callable(IntComparison.__init__)


def test_intcomparison_constructor_args():
    sig = inspect.signature(IntComparison.__init__)
    params = list(sig.parameters.keys())



def test_minilang::lessorequal_is_not_abstract():
    assert not inspect.isabstract(minilang::LessOrEqual)


def test_minilang::lessorequal_constructor_exists():
    assert callable(minilang::LessOrEqual.__init__)


def test_minilang::lessorequal_constructor_args():
    sig = inspect.signature(minilang::LessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_minilang::greater_is_not_abstract():
    assert not inspect.isabstract(minilang::Greater)


def test_minilang::greater_constructor_exists():
    assert callable(minilang::Greater.__init__)


def test_minilang::greater_constructor_args():
    sig = inspect.signature(minilang::Greater.__init__)
    params = list(sig.parameters.keys())



def test_minilang::equal_is_not_abstract():
    assert not inspect.isabstract(minilang::Equal)


def test_minilang::equal_constructor_exists():
    assert callable(minilang::Equal.__init__)


def test_minilang::equal_constructor_args():
    sig = inspect.signature(minilang::Equal.__init__)
    params = list(sig.parameters.keys())



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_minilang::booleanoperation_is_not_abstract():
    assert not inspect.isabstract(minilang::BooleanOperation)


def test_minilang::booleanoperation_constructor_exists():
    assert callable(minilang::BooleanOperation.__init__)


def test_minilang::booleanoperation_constructor_args():
    sig = inspect.signature(minilang::BooleanOperation.__init__)
    params = list(sig.parameters.keys())



def test_minilang::booleanvariableref_is_not_abstract():
    assert not inspect.isabstract(minilang::BooleanVariableRef)


def test_minilang::booleanvariableref_constructor_exists():
    assert callable(minilang::BooleanVariableRef.__init__)


def test_minilang::booleanvariableref_constructor_args():
    sig = inspect.signature(minilang::BooleanVariableRef.__init__)
    params = list(sig.parameters.keys())



def test_minilang::not_is_not_abstract():
    assert not inspect.isabstract(minilang::Not)


def test_minilang::not_constructor_exists():
    assert callable(minilang::Not.__init__)


def test_minilang::not_constructor_args():
    sig = inspect.signature(minilang::Not.__init__)
    params = list(sig.parameters.keys())



def test_minilang::intcomparison_is_not_abstract():
    assert not inspect.isabstract(minilang::IntComparison)


def test_minilang::intcomparison_constructor_exists():
    assert callable(minilang::IntComparison.__init__)


def test_minilang::intcomparison_constructor_args():
    sig = inspect.signature(minilang::IntComparison.__init__)
    params = list(sig.parameters.keys())



def test_minilang::boolean_is_not_abstract():
    assert not inspect.isabstract(minilang::Boolean)


def test_minilang::boolean_constructor_exists():
    assert callable(minilang::Boolean.__init__)


def test_minilang::boolean_constructor_args():
    sig = inspect.signature(minilang::Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minilang::boolean_has_value():
    assert hasattr(minilang::Boolean, "value")
    descriptor = None
    for klass in minilang::Boolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_intexpression_is_not_abstract():
    assert not inspect.isabstract(IntExpression)


def test_intexpression_constructor_exists():
    assert callable(IntExpression.__init__)


def test_intexpression_constructor_args():
    sig = inspect.signature(IntExpression.__init__)
    params = list(sig.parameters.keys())



def test_minilang::intoperation_is_not_abstract():
    assert not inspect.isabstract(minilang::IntOperation)


def test_minilang::intoperation_constructor_exists():
    assert callable(minilang::IntOperation.__init__)


def test_minilang::intoperation_constructor_args():
    sig = inspect.signature(minilang::IntOperation.__init__)
    params = list(sig.parameters.keys())



def test_minilang::intvariableref_is_not_abstract():
    assert not inspect.isabstract(minilang::IntVariableRef)


def test_minilang::intvariableref_constructor_exists():
    assert callable(minilang::IntVariableRef.__init__)


def test_minilang::intvariableref_constructor_args():
    sig = inspect.signature(minilang::IntVariableRef.__init__)
    params = list(sig.parameters.keys())



def test_minilang::integer_is_not_abstract():
    assert not inspect.isabstract(minilang::Integer)


def test_minilang::integer_constructor_exists():
    assert callable(minilang::Integer.__init__)


def test_minilang::integer_constructor_args():
    sig = inspect.signature(minilang::Integer.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minilang::integer_has_value():
    assert hasattr(minilang::Integer, "value")
    descriptor = None
    for klass in minilang::Integer.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minilang::intexpression_is_not_abstract():
    assert not inspect.isabstract(minilang::IntExpression)


def test_minilang::intexpression_constructor_exists():
    assert callable(minilang::IntExpression.__init__)


def test_minilang::intexpression_constructor_args():
    sig = inspect.signature(minilang::IntExpression.__init__)
    params = list(sig.parameters.keys())



def test_minilang::less_is_not_abstract():
    assert not inspect.isabstract(minilang::Less)


def test_minilang::less_constructor_exists():
    assert callable(minilang::Less.__init__)


def test_minilang::less_constructor_args():
    sig = inspect.signature(minilang::Less.__init__)
    params = list(sig.parameters.keys())



def test_minilang::greaterorequal_is_not_abstract():
    assert not inspect.isabstract(minilang::GreaterOrEqual)


def test_minilang::greaterorequal_constructor_exists():
    assert callable(minilang::GreaterOrEqual.__init__)


def test_minilang::greaterorequal_constructor_args():
    sig = inspect.signature(minilang::GreaterOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_minilang::while_is_not_abstract():
    assert not inspect.isabstract(minilang::While)


def test_minilang::while_constructor_exists():
    assert callable(minilang::While.__init__)


def test_minilang::while_constructor_args():
    sig = inspect.signature(minilang::While.__init__)
    params = list(sig.parameters.keys())



def test_minilang::block_is_not_abstract():
    assert not inspect.isabstract(minilang::Block)


def test_minilang::block_constructor_exists():
    assert callable(minilang::Block.__init__)


def test_minilang::block_constructor_args():
    sig = inspect.signature(minilang::Block.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_minilang::intassignment_is_not_abstract():
    assert not inspect.isabstract(minilang::IntAssignment)


def test_minilang::intassignment_constructor_exists():
    assert callable(minilang::IntAssignment.__init__)


def test_minilang::intassignment_constructor_args():
    sig = inspect.signature(minilang::IntAssignment.__init__)
    params = list(sig.parameters.keys())



def test_minilang::printstr_is_not_abstract():
    assert not inspect.isabstract(minilang::PrintStr)


def test_minilang::printstr_constructor_exists():
    assert callable(minilang::PrintStr.__init__)


def test_minilang::printstr_constructor_args():
    sig = inspect.signature(minilang::PrintStr.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minilang::printstr_has_value():
    assert hasattr(minilang::PrintStr, "value")
    descriptor = None
    for klass in minilang::PrintStr.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minilang::printvar_is_not_abstract():
    assert not inspect.isabstract(minilang::PrintVar)


def test_minilang::printvar_constructor_exists():
    assert callable(minilang::PrintVar.__init__)


def test_minilang::printvar_constructor_args():
    sig = inspect.signature(minilang::PrintVar.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minilang::printvar_has_value():
    assert hasattr(minilang::PrintVar, "value")
    descriptor = None
    for klass in minilang::PrintVar.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minilang::booleanassignment_is_not_abstract():
    assert not inspect.isabstract(minilang::BooleanAssignment)


def test_minilang::booleanassignment_constructor_exists():
    assert callable(minilang::BooleanAssignment.__init__)


def test_minilang::booleanassignment_constructor_args():
    sig = inspect.signature(minilang::BooleanAssignment.__init__)
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
minilang::Statement_strategy = st.builds(
    minilang::Statement,
)
minilang::VariableRef_strategy = st.builds(
    minilang::VariableRef,
    name=
        safe_text
)
VariableRef_strategy = st.builds(
    VariableRef,
)
IntOperation_strategy = st.builds(
    IntOperation,
)
minilang::Divide_strategy = st.builds(
    minilang::Divide,
)
minilang::Multiply_strategy = st.builds(
    minilang::Multiply,
)
minilang::Minus_strategy = st.builds(
    minilang::Minus,
)
minilang::Plus_strategy = st.builds(
    minilang::Plus,
)
BooleanOperation_strategy = st.builds(
    BooleanOperation,
)
minilang::And_strategy = st.builds(
    minilang::And,
)
minilang::Or_strategy = st.builds(
    minilang::Or,
)
minilang::BooleanExpression_strategy = st.builds(
    minilang::BooleanExpression,
)
minilang::If_strategy = st.builds(
    minilang::If,
)
IntComparison_strategy = st.builds(
    IntComparison,
)
minilang::LessOrEqual_strategy = st.builds(
    minilang::LessOrEqual,
)
minilang::Greater_strategy = st.builds(
    minilang::Greater,
)
minilang::Equal_strategy = st.builds(
    minilang::Equal,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
minilang::BooleanOperation_strategy = st.builds(
    minilang::BooleanOperation,
)
minilang::BooleanVariableRef_strategy = st.builds(
    minilang::BooleanVariableRef,
)
minilang::Not_strategy = st.builds(
    minilang::Not,
)
minilang::IntComparison_strategy = st.builds(
    minilang::IntComparison,
)
minilang::Boolean_strategy = st.builds(
    minilang::Boolean,
    value=
        st.booleans()
)
IntExpression_strategy = st.builds(
    IntExpression,
)
minilang::IntOperation_strategy = st.builds(
    minilang::IntOperation,
)
minilang::IntVariableRef_strategy = st.builds(
    minilang::IntVariableRef,
)
minilang::Integer_strategy = st.builds(
    minilang::Integer,
    value=
        st.integers()
)
minilang::IntExpression_strategy = st.builds(
    minilang::IntExpression,
)
minilang::Less_strategy = st.builds(
    minilang::Less,
)
minilang::GreaterOrEqual_strategy = st.builds(
    minilang::GreaterOrEqual,
)
minilang::While_strategy = st.builds(
    minilang::While,
)
minilang::Block_strategy = st.builds(
    minilang::Block,
)
Statement_strategy = st.builds(
    Statement,
)
minilang::IntAssignment_strategy = st.builds(
    minilang::IntAssignment,
)
minilang::PrintStr_strategy = st.builds(
    minilang::PrintStr,
    value=
        safe_text
)
minilang::PrintVar_strategy = st.builds(
    minilang::PrintVar,
    value=
        safe_text
)
minilang::BooleanAssignment_strategy = st.builds(
    minilang::BooleanAssignment,
)

@given(instance=minilang::Statement_strategy)
@settings(max_examples=50)
def test_minilang::statement_instantiation(instance):
    assert isinstance(instance, minilang::Statement)

@given(instance=minilang::VariableRef_strategy)
@settings(max_examples=50)
def test_minilang::variableref_instantiation(instance):
    assert isinstance(instance, minilang::VariableRef)

@given(instance=minilang::VariableRef_strategy)
def test_minilang::variableref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minilang::VariableRef_strategy)
def test_minilang::variableref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=VariableRef_strategy)
@settings(max_examples=50)
def test_variableref_instantiation(instance):
    assert isinstance(instance, VariableRef)

@given(instance=IntOperation_strategy)
@settings(max_examples=50)
def test_intoperation_instantiation(instance):
    assert isinstance(instance, IntOperation)

@given(instance=minilang::Divide_strategy)
@settings(max_examples=50)
def test_minilang::divide_instantiation(instance):
    assert isinstance(instance, minilang::Divide)

@given(instance=minilang::Multiply_strategy)
@settings(max_examples=50)
def test_minilang::multiply_instantiation(instance):
    assert isinstance(instance, minilang::Multiply)

@given(instance=minilang::Minus_strategy)
@settings(max_examples=50)
def test_minilang::minus_instantiation(instance):
    assert isinstance(instance, minilang::Minus)

@given(instance=minilang::Plus_strategy)
@settings(max_examples=50)
def test_minilang::plus_instantiation(instance):
    assert isinstance(instance, minilang::Plus)

@given(instance=BooleanOperation_strategy)
@settings(max_examples=50)
def test_booleanoperation_instantiation(instance):
    assert isinstance(instance, BooleanOperation)

@given(instance=minilang::And_strategy)
@settings(max_examples=50)
def test_minilang::and_instantiation(instance):
    assert isinstance(instance, minilang::And)

@given(instance=minilang::Or_strategy)
@settings(max_examples=50)
def test_minilang::or_instantiation(instance):
    assert isinstance(instance, minilang::Or)

@given(instance=minilang::BooleanExpression_strategy)
@settings(max_examples=50)
def test_minilang::booleanexpression_instantiation(instance):
    assert isinstance(instance, minilang::BooleanExpression)

@given(instance=minilang::If_strategy)
@settings(max_examples=50)
def test_minilang::if_instantiation(instance):
    assert isinstance(instance, minilang::If)

@given(instance=IntComparison_strategy)
@settings(max_examples=50)
def test_intcomparison_instantiation(instance):
    assert isinstance(instance, IntComparison)

@given(instance=minilang::LessOrEqual_strategy)
@settings(max_examples=50)
def test_minilang::lessorequal_instantiation(instance):
    assert isinstance(instance, minilang::LessOrEqual)

@given(instance=minilang::Greater_strategy)
@settings(max_examples=50)
def test_minilang::greater_instantiation(instance):
    assert isinstance(instance, minilang::Greater)

@given(instance=minilang::Equal_strategy)
@settings(max_examples=50)
def test_minilang::equal_instantiation(instance):
    assert isinstance(instance, minilang::Equal)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=minilang::BooleanOperation_strategy)
@settings(max_examples=50)
def test_minilang::booleanoperation_instantiation(instance):
    assert isinstance(instance, minilang::BooleanOperation)

@given(instance=minilang::BooleanVariableRef_strategy)
@settings(max_examples=50)
def test_minilang::booleanvariableref_instantiation(instance):
    assert isinstance(instance, minilang::BooleanVariableRef)

@given(instance=minilang::Not_strategy)
@settings(max_examples=50)
def test_minilang::not_instantiation(instance):
    assert isinstance(instance, minilang::Not)

@given(instance=minilang::IntComparison_strategy)
@settings(max_examples=50)
def test_minilang::intcomparison_instantiation(instance):
    assert isinstance(instance, minilang::IntComparison)

@given(instance=minilang::Boolean_strategy)
@settings(max_examples=50)
def test_minilang::boolean_instantiation(instance):
    assert isinstance(instance, minilang::Boolean)

@given(instance=minilang::Boolean_strategy)
def test_minilang::boolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=minilang::Boolean_strategy)
def test_minilang::boolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=IntExpression_strategy)
@settings(max_examples=50)
def test_intexpression_instantiation(instance):
    assert isinstance(instance, IntExpression)

@given(instance=minilang::IntOperation_strategy)
@settings(max_examples=50)
def test_minilang::intoperation_instantiation(instance):
    assert isinstance(instance, minilang::IntOperation)

@given(instance=minilang::IntVariableRef_strategy)
@settings(max_examples=50)
def test_minilang::intvariableref_instantiation(instance):
    assert isinstance(instance, minilang::IntVariableRef)

@given(instance=minilang::Integer_strategy)
@settings(max_examples=50)
def test_minilang::integer_instantiation(instance):
    assert isinstance(instance, minilang::Integer)

@given(instance=minilang::Integer_strategy)
def test_minilang::integer_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=minilang::Integer_strategy)
def test_minilang::integer_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=minilang::IntExpression_strategy)
@settings(max_examples=50)
def test_minilang::intexpression_instantiation(instance):
    assert isinstance(instance, minilang::IntExpression)

@given(instance=minilang::Less_strategy)
@settings(max_examples=50)
def test_minilang::less_instantiation(instance):
    assert isinstance(instance, minilang::Less)

@given(instance=minilang::GreaterOrEqual_strategy)
@settings(max_examples=50)
def test_minilang::greaterorequal_instantiation(instance):
    assert isinstance(instance, minilang::GreaterOrEqual)

@given(instance=minilang::While_strategy)
@settings(max_examples=50)
def test_minilang::while_instantiation(instance):
    assert isinstance(instance, minilang::While)

@given(instance=minilang::Block_strategy)
@settings(max_examples=50)
def test_minilang::block_instantiation(instance):
    assert isinstance(instance, minilang::Block)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=minilang::IntAssignment_strategy)
@settings(max_examples=50)
def test_minilang::intassignment_instantiation(instance):
    assert isinstance(instance, minilang::IntAssignment)

@given(instance=minilang::PrintStr_strategy)
@settings(max_examples=50)
def test_minilang::printstr_instantiation(instance):
    assert isinstance(instance, minilang::PrintStr)

@given(instance=minilang::PrintStr_strategy)
def test_minilang::printstr_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=minilang::PrintStr_strategy)
def test_minilang::printstr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=minilang::PrintVar_strategy)
@settings(max_examples=50)
def test_minilang::printvar_instantiation(instance):
    assert isinstance(instance, minilang::PrintVar)

@given(instance=minilang::PrintVar_strategy)
def test_minilang::printvar_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=minilang::PrintVar_strategy)
def test_minilang::printvar_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=minilang::BooleanAssignment_strategy)
@settings(max_examples=50)
def test_minilang::booleanassignment_instantiation(instance):
    assert isinstance(instance, minilang::BooleanAssignment)
