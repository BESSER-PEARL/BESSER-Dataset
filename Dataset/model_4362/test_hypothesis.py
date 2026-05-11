import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Statement,
    mpl::Assignment,
    ArithmeticExpression,
    mpl::AddExpression,
    AtomicExpression,
    mpl::LiteralValue,
    Expression,
    mpl::AtomicExpression,
    mpl::ArithmeticExpression,
    mpl::ExpressionStatement,
    mpl::VariableRefrence,
    mpl::Expression,
    mpl::Variable,
    mpl::Statement,
    mpl::VariableDeclaration,
    mpl::Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_mpl::assignment_is_not_abstract():
    assert not inspect.isabstract(mpl::Assignment)


def test_mpl::assignment_constructor_exists():
    assert callable(mpl::Assignment.__init__)


def test_mpl::assignment_constructor_args():
    sig = inspect.signature(mpl::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_mpl::addexpression_is_not_abstract():
    assert not inspect.isabstract(mpl::AddExpression)


def test_mpl::addexpression_constructor_exists():
    assert callable(mpl::AddExpression.__init__)


def test_mpl::addexpression_constructor_args():
    sig = inspect.signature(mpl::AddExpression.__init__)
    params = list(sig.parameters.keys())



def test_atomicexpression_is_not_abstract():
    assert not inspect.isabstract(AtomicExpression)


def test_atomicexpression_constructor_exists():
    assert callable(AtomicExpression.__init__)


def test_atomicexpression_constructor_args():
    sig = inspect.signature(AtomicExpression.__init__)
    params = list(sig.parameters.keys())



def test_mpl::literalvalue_is_not_abstract():
    assert not inspect.isabstract(mpl::LiteralValue)


def test_mpl::literalvalue_constructor_exists():
    assert callable(mpl::LiteralValue.__init__)


def test_mpl::literalvalue_constructor_args():
    sig = inspect.signature(mpl::LiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "rawValue" in params, "Missing parameter 'rawValue'"

def test_mpl::literalvalue_has_rawValue():
    assert hasattr(mpl::LiteralValue, "rawValue")
    descriptor = None
    for klass in mpl::LiteralValue.__mro__:
        if "rawValue" in klass.__dict__:
            descriptor = klass.__dict__["rawValue"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mpl::atomicexpression_is_not_abstract():
    assert not inspect.isabstract(mpl::AtomicExpression)


def test_mpl::atomicexpression_constructor_exists():
    assert callable(mpl::AtomicExpression.__init__)


def test_mpl::atomicexpression_constructor_args():
    sig = inspect.signature(mpl::AtomicExpression.__init__)
    params = list(sig.parameters.keys())



def test_mpl::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(mpl::ArithmeticExpression)


def test_mpl::arithmeticexpression_constructor_exists():
    assert callable(mpl::ArithmeticExpression.__init__)


def test_mpl::arithmeticexpression_constructor_args():
    sig = inspect.signature(mpl::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_mpl::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(mpl::ExpressionStatement)


def test_mpl::expressionstatement_constructor_exists():
    assert callable(mpl::ExpressionStatement.__init__)


def test_mpl::expressionstatement_constructor_args():
    sig = inspect.signature(mpl::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_mpl::variablerefrence_is_not_abstract():
    assert not inspect.isabstract(mpl::VariableRefrence)


def test_mpl::variablerefrence_constructor_exists():
    assert callable(mpl::VariableRefrence.__init__)


def test_mpl::variablerefrence_constructor_args():
    sig = inspect.signature(mpl::VariableRefrence.__init__)
    params = list(sig.parameters.keys())



def test_mpl::expression_is_not_abstract():
    assert not inspect.isabstract(mpl::Expression)


def test_mpl::expression_constructor_exists():
    assert callable(mpl::Expression.__init__)


def test_mpl::expression_constructor_args():
    sig = inspect.signature(mpl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_mpl::variable_is_not_abstract():
    assert not inspect.isabstract(mpl::Variable)


def test_mpl::variable_constructor_exists():
    assert callable(mpl::Variable.__init__)


def test_mpl::variable_constructor_args():
    sig = inspect.signature(mpl::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mpl::variable_has_name():
    assert hasattr(mpl::Variable, "name")
    descriptor = None
    for klass in mpl::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mpl::statement_is_not_abstract():
    assert not inspect.isabstract(mpl::Statement)


def test_mpl::statement_constructor_exists():
    assert callable(mpl::Statement.__init__)


def test_mpl::statement_constructor_args():
    sig = inspect.signature(mpl::Statement.__init__)
    params = list(sig.parameters.keys())



def test_mpl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(mpl::VariableDeclaration)


def test_mpl::variabledeclaration_constructor_exists():
    assert callable(mpl::VariableDeclaration.__init__)


def test_mpl::variabledeclaration_constructor_args():
    sig = inspect.signature(mpl::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_mpl::program_is_not_abstract():
    assert not inspect.isabstract(mpl::Program)


def test_mpl::program_constructor_exists():
    assert callable(mpl::Program.__init__)


def test_mpl::program_constructor_args():
    sig = inspect.signature(mpl::Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mpl::program_has_name():
    assert hasattr(mpl::Program, "name")
    descriptor = None
    for klass in mpl::Program.__mro__:
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
Statement_strategy = st.builds(
    Statement,
)
mpl::Assignment_strategy = st.builds(
    mpl::Assignment,
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
mpl::AddExpression_strategy = st.builds(
    mpl::AddExpression,
)
AtomicExpression_strategy = st.builds(
    AtomicExpression,
)
mpl::LiteralValue_strategy = st.builds(
    mpl::LiteralValue,
    rawValue=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
mpl::AtomicExpression_strategy = st.builds(
    mpl::AtomicExpression,
)
mpl::ArithmeticExpression_strategy = st.builds(
    mpl::ArithmeticExpression,
)
mpl::ExpressionStatement_strategy = st.builds(
    mpl::ExpressionStatement,
)
mpl::VariableRefrence_strategy = st.builds(
    mpl::VariableRefrence,
)
mpl::Expression_strategy = st.builds(
    mpl::Expression,
)
mpl::Variable_strategy = st.builds(
    mpl::Variable,
    name=
        safe_text
)
mpl::Statement_strategy = st.builds(
    mpl::Statement,
)
mpl::VariableDeclaration_strategy = st.builds(
    mpl::VariableDeclaration,
)
mpl::Program_strategy = st.builds(
    mpl::Program,
    name=
        safe_text
)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=mpl::Assignment_strategy)
@settings(max_examples=50)
def test_mpl::assignment_instantiation(instance):
    assert isinstance(instance, mpl::Assignment)

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=mpl::AddExpression_strategy)
@settings(max_examples=50)
def test_mpl::addexpression_instantiation(instance):
    assert isinstance(instance, mpl::AddExpression)

@given(instance=AtomicExpression_strategy)
@settings(max_examples=50)
def test_atomicexpression_instantiation(instance):
    assert isinstance(instance, AtomicExpression)

@given(instance=mpl::LiteralValue_strategy)
@settings(max_examples=50)
def test_mpl::literalvalue_instantiation(instance):
    assert isinstance(instance, mpl::LiteralValue)

@given(instance=mpl::LiteralValue_strategy)
def test_mpl::literalvalue_rawValue_type(instance):
    assert isinstance(instance.rawValue, int)


@given(instance=mpl::LiteralValue_strategy)
def test_mpl::literalvalue_rawValue_setter(instance):
    original = instance.rawValue
    instance.rawValue = original
    assert instance.rawValue == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mpl::AtomicExpression_strategy)
@settings(max_examples=50)
def test_mpl::atomicexpression_instantiation(instance):
    assert isinstance(instance, mpl::AtomicExpression)

@given(instance=mpl::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_mpl::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, mpl::ArithmeticExpression)

@given(instance=mpl::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_mpl::expressionstatement_instantiation(instance):
    assert isinstance(instance, mpl::ExpressionStatement)

@given(instance=mpl::VariableRefrence_strategy)
@settings(max_examples=50)
def test_mpl::variablerefrence_instantiation(instance):
    assert isinstance(instance, mpl::VariableRefrence)

@given(instance=mpl::Expression_strategy)
@settings(max_examples=50)
def test_mpl::expression_instantiation(instance):
    assert isinstance(instance, mpl::Expression)

@given(instance=mpl::Variable_strategy)
@settings(max_examples=50)
def test_mpl::variable_instantiation(instance):
    assert isinstance(instance, mpl::Variable)

@given(instance=mpl::Variable_strategy)
def test_mpl::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mpl::Variable_strategy)
def test_mpl::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mpl::Statement_strategy)
@settings(max_examples=50)
def test_mpl::statement_instantiation(instance):
    assert isinstance(instance, mpl::Statement)

@given(instance=mpl::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_mpl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, mpl::VariableDeclaration)

@given(instance=mpl::Program_strategy)
@settings(max_examples=50)
def test_mpl::program_instantiation(instance):
    assert isinstance(instance, mpl::Program)

@given(instance=mpl::Program_strategy)
def test_mpl::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mpl::Program_strategy)
def test_mpl::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
