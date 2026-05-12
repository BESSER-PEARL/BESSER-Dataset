import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Statement,
    mpl_Assignment,
    ArithmeticExpression,
    mpl_AddExpression,
    AtomicExpression,
    mpl_LiteralValue,
    Expression,
    mpl_AtomicExpression,
    mpl_ArithmeticExpression,
    mpl_ExpressionStatement,
    mpl_VariableRefrence,
    mpl_Expression,
    mpl_Variable,
    mpl_Statement,
    mpl_VariableDeclaration,
    mpl_Program,
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



def test_mpl_assignment_is_not_abstract():
    assert not inspect.isabstract(mpl_Assignment)


def test_mpl_assignment_constructor_exists():
    assert callable(mpl_Assignment.__init__)


def test_mpl_assignment_constructor_args():
    sig = inspect.signature(mpl_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_mpl_addexpression_is_not_abstract():
    assert not inspect.isabstract(mpl_AddExpression)


def test_mpl_addexpression_constructor_exists():
    assert callable(mpl_AddExpression.__init__)


def test_mpl_addexpression_constructor_args():
    sig = inspect.signature(mpl_AddExpression.__init__)
    params = list(sig.parameters.keys())



def test_atomicexpression_is_not_abstract():
    assert not inspect.isabstract(AtomicExpression)


def test_atomicexpression_constructor_exists():
    assert callable(AtomicExpression.__init__)


def test_atomicexpression_constructor_args():
    sig = inspect.signature(AtomicExpression.__init__)
    params = list(sig.parameters.keys())



def test_mpl_literalvalue_is_not_abstract():
    assert not inspect.isabstract(mpl_LiteralValue)


def test_mpl_literalvalue_constructor_exists():
    assert callable(mpl_LiteralValue.__init__)


def test_mpl_literalvalue_constructor_args():
    sig = inspect.signature(mpl_LiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "rawValue" in params, "Missing parameter 'rawValue'"

def test_mpl_literalvalue_has_rawValue():
    assert hasattr(mpl_LiteralValue, "rawValue")
    descriptor = None
    for klass in mpl_LiteralValue.__mro__:
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



def test_mpl_atomicexpression_is_not_abstract():
    assert not inspect.isabstract(mpl_AtomicExpression)


def test_mpl_atomicexpression_constructor_exists():
    assert callable(mpl_AtomicExpression.__init__)


def test_mpl_atomicexpression_constructor_args():
    sig = inspect.signature(mpl_AtomicExpression.__init__)
    params = list(sig.parameters.keys())



def test_mpl_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(mpl_ArithmeticExpression)


def test_mpl_arithmeticexpression_constructor_exists():
    assert callable(mpl_ArithmeticExpression.__init__)


def test_mpl_arithmeticexpression_constructor_args():
    sig = inspect.signature(mpl_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_mpl_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(mpl_ExpressionStatement)


def test_mpl_expressionstatement_constructor_exists():
    assert callable(mpl_ExpressionStatement.__init__)


def test_mpl_expressionstatement_constructor_args():
    sig = inspect.signature(mpl_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_mpl_variablerefrence_is_not_abstract():
    assert not inspect.isabstract(mpl_VariableRefrence)


def test_mpl_variablerefrence_constructor_exists():
    assert callable(mpl_VariableRefrence.__init__)


def test_mpl_variablerefrence_constructor_args():
    sig = inspect.signature(mpl_VariableRefrence.__init__)
    params = list(sig.parameters.keys())



def test_mpl_expression_is_not_abstract():
    assert not inspect.isabstract(mpl_Expression)


def test_mpl_expression_constructor_exists():
    assert callable(mpl_Expression.__init__)


def test_mpl_expression_constructor_args():
    sig = inspect.signature(mpl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mpl_variable_is_not_abstract():
    assert not inspect.isabstract(mpl_Variable)


def test_mpl_variable_constructor_exists():
    assert callable(mpl_Variable.__init__)


def test_mpl_variable_constructor_args():
    sig = inspect.signature(mpl_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mpl_variable_has_name():
    assert hasattr(mpl_Variable, "name")
    descriptor = None
    for klass in mpl_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mpl_statement_is_not_abstract():
    assert not inspect.isabstract(mpl_Statement)


def test_mpl_statement_constructor_exists():
    assert callable(mpl_Statement.__init__)


def test_mpl_statement_constructor_args():
    sig = inspect.signature(mpl_Statement.__init__)
    params = list(sig.parameters.keys())



def test_mpl_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(mpl_VariableDeclaration)


def test_mpl_variabledeclaration_constructor_exists():
    assert callable(mpl_VariableDeclaration.__init__)


def test_mpl_variabledeclaration_constructor_args():
    sig = inspect.signature(mpl_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_mpl_program_is_not_abstract():
    assert not inspect.isabstract(mpl_Program)


def test_mpl_program_constructor_exists():
    assert callable(mpl_Program.__init__)


def test_mpl_program_constructor_args():
    sig = inspect.signature(mpl_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mpl_program_has_name():
    assert hasattr(mpl_Program, "name")
    descriptor = None
    for klass in mpl_Program.__mro__:
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
mpl_Assignment_strategy = st.builds(
    mpl_Assignment,
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
mpl_AddExpression_strategy = st.builds(
    mpl_AddExpression,
)
AtomicExpression_strategy = st.builds(
    AtomicExpression,
)
mpl_LiteralValue_strategy = st.builds(
    mpl_LiteralValue,
    rawValue=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
mpl_AtomicExpression_strategy = st.builds(
    mpl_AtomicExpression,
)
mpl_ArithmeticExpression_strategy = st.builds(
    mpl_ArithmeticExpression,
)
mpl_ExpressionStatement_strategy = st.builds(
    mpl_ExpressionStatement,
)
mpl_VariableRefrence_strategy = st.builds(
    mpl_VariableRefrence,
)
mpl_Expression_strategy = st.builds(
    mpl_Expression,
)
mpl_Variable_strategy = st.builds(
    mpl_Variable,
    name=
        safe_text
)
mpl_Statement_strategy = st.builds(
    mpl_Statement,
)
mpl_VariableDeclaration_strategy = st.builds(
    mpl_VariableDeclaration,
)
mpl_Program_strategy = st.builds(
    mpl_Program,
    name=
        safe_text
)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=mpl_Assignment_strategy)
@settings(max_examples=50)
def test_mpl_assignment_instantiation(instance):
    assert isinstance(instance, mpl_Assignment)

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=mpl_AddExpression_strategy)
@settings(max_examples=50)
def test_mpl_addexpression_instantiation(instance):
    assert isinstance(instance, mpl_AddExpression)

@given(instance=AtomicExpression_strategy)
@settings(max_examples=50)
def test_atomicexpression_instantiation(instance):
    assert isinstance(instance, AtomicExpression)

@given(instance=mpl_LiteralValue_strategy)
@settings(max_examples=50)
def test_mpl_literalvalue_instantiation(instance):
    assert isinstance(instance, mpl_LiteralValue)



@given(instance=mpl_LiteralValue_strategy)
def test_mpl_literalvalue_rawValue_setter(instance):
    original = instance.rawValue
    instance.rawValue = original
    assert instance.rawValue == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mpl_AtomicExpression_strategy)
@settings(max_examples=50)
def test_mpl_atomicexpression_instantiation(instance):
    assert isinstance(instance, mpl_AtomicExpression)

@given(instance=mpl_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_mpl_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, mpl_ArithmeticExpression)

@given(instance=mpl_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_mpl_expressionstatement_instantiation(instance):
    assert isinstance(instance, mpl_ExpressionStatement)

@given(instance=mpl_VariableRefrence_strategy)
@settings(max_examples=50)
def test_mpl_variablerefrence_instantiation(instance):
    assert isinstance(instance, mpl_VariableRefrence)

@given(instance=mpl_Expression_strategy)
@settings(max_examples=50)
def test_mpl_expression_instantiation(instance):
    assert isinstance(instance, mpl_Expression)

@given(instance=mpl_Variable_strategy)
@settings(max_examples=50)
def test_mpl_variable_instantiation(instance):
    assert isinstance(instance, mpl_Variable)



@given(instance=mpl_Variable_strategy)
def test_mpl_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mpl_Statement_strategy)
@settings(max_examples=50)
def test_mpl_statement_instantiation(instance):
    assert isinstance(instance, mpl_Statement)

@given(instance=mpl_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_mpl_variabledeclaration_instantiation(instance):
    assert isinstance(instance, mpl_VariableDeclaration)

@given(instance=mpl_Program_strategy)
@settings(max_examples=50)
def test_mpl_program_instantiation(instance):
    assert isinstance(instance, mpl_Program)



@given(instance=mpl_Program_strategy)
def test_mpl_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
