import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mini::lang::Statement,
    mini::lang::Block,
    mini::lang::MiniLang,
    ComparisonExpression,
    mini::lang::EqualsExpression,
    mini::lang::NotEqualsExpression,
    Expression,
    mini::lang::NameExpression,
    mini::lang::FOLCallExpression,
    mini::lang::ComparisonExpression,
    mini::lang::Expression,
    Statement,
    mini::lang::AssignmentStatement,
    mini::lang::ReturnStatement,
    mini::lang::ExpressionStatement,
    mini::lang::IfStatement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mini::lang::statement_is_not_abstract():
    assert not inspect.isabstract(mini::lang::Statement)


def test_mini::lang::statement_constructor_exists():
    assert callable(mini::lang::Statement.__init__)


def test_mini::lang::statement_constructor_args():
    sig = inspect.signature(mini::lang::Statement.__init__)
    params = list(sig.parameters.keys())



def test_mini::lang::block_is_not_abstract():
    assert not inspect.isabstract(mini::lang::Block)


def test_mini::lang::block_constructor_exists():
    assert callable(mini::lang::Block.__init__)


def test_mini::lang::block_constructor_args():
    sig = inspect.signature(mini::lang::Block.__init__)
    params = list(sig.parameters.keys())



def test_mini::lang::minilang_is_not_abstract():
    assert not inspect.isabstract(mini::lang::MiniLang)


def test_mini::lang::minilang_constructor_exists():
    assert callable(mini::lang::MiniLang.__init__)


def test_mini::lang::minilang_constructor_args():
    sig = inspect.signature(mini::lang::MiniLang.__init__)
    params = list(sig.parameters.keys())



def test_comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(ComparisonExpression)


def test_comparisonexpression_constructor_exists():
    assert callable(ComparisonExpression.__init__)


def test_comparisonexpression_constructor_args():
    sig = inspect.signature(ComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_mini::lang::equalsexpression_is_not_abstract():
    assert not inspect.isabstract(mini::lang::EqualsExpression)


def test_mini::lang::equalsexpression_constructor_exists():
    assert callable(mini::lang::EqualsExpression.__init__)


def test_mini::lang::equalsexpression_constructor_args():
    sig = inspect.signature(mini::lang::EqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_mini::lang::notequalsexpression_is_not_abstract():
    assert not inspect.isabstract(mini::lang::NotEqualsExpression)


def test_mini::lang::notequalsexpression_constructor_exists():
    assert callable(mini::lang::NotEqualsExpression.__init__)


def test_mini::lang::notequalsexpression_constructor_args():
    sig = inspect.signature(mini::lang::NotEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mini::lang::nameexpression_is_not_abstract():
    assert not inspect.isabstract(mini::lang::NameExpression)


def test_mini::lang::nameexpression_constructor_exists():
    assert callable(mini::lang::NameExpression.__init__)


def test_mini::lang::nameexpression_constructor_args():
    sig = inspect.signature(mini::lang::NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mini::lang::nameexpression_has_name():
    assert hasattr(mini::lang::NameExpression, "name")
    descriptor = None
    for klass in mini::lang::NameExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mini::lang::folcallexpression_is_not_abstract():
    assert not inspect.isabstract(mini::lang::FOLCallExpression)


def test_mini::lang::folcallexpression_constructor_exists():
    assert callable(mini::lang::FOLCallExpression.__init__)


def test_mini::lang::folcallexpression_constructor_args():
    sig = inspect.signature(mini::lang::FOLCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "method" in params, "Missing parameter 'method'"
    assert "iterator" in params, "Missing parameter 'iterator'"

def test_mini::lang::folcallexpression_has_method():
    assert hasattr(mini::lang::FOLCallExpression, "method")
    descriptor = None
    for klass in mini::lang::FOLCallExpression.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_mini::lang::folcallexpression_has_iterator():
    assert hasattr(mini::lang::FOLCallExpression, "iterator")
    descriptor = None
    for klass in mini::lang::FOLCallExpression.__mro__:
        if "iterator" in klass.__dict__:
            descriptor = klass.__dict__["iterator"]
            break
    assert isinstance(descriptor, property)



def test_mini::lang::comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(mini::lang::ComparisonExpression)


def test_mini::lang::comparisonexpression_constructor_exists():
    assert callable(mini::lang::ComparisonExpression.__init__)


def test_mini::lang::comparisonexpression_constructor_args():
    sig = inspect.signature(mini::lang::ComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_mini::lang::expression_is_not_abstract():
    assert not inspect.isabstract(mini::lang::Expression)


def test_mini::lang::expression_constructor_exists():
    assert callable(mini::lang::Expression.__init__)


def test_mini::lang::expression_constructor_args():
    sig = inspect.signature(mini::lang::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_mini::lang::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(mini::lang::AssignmentStatement)


def test_mini::lang::assignmentstatement_constructor_exists():
    assert callable(mini::lang::AssignmentStatement.__init__)


def test_mini::lang::assignmentstatement_constructor_args():
    sig = inspect.signature(mini::lang::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_mini::lang::returnstatement_is_not_abstract():
    assert not inspect.isabstract(mini::lang::ReturnStatement)


def test_mini::lang::returnstatement_constructor_exists():
    assert callable(mini::lang::ReturnStatement.__init__)


def test_mini::lang::returnstatement_constructor_args():
    sig = inspect.signature(mini::lang::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_mini::lang::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(mini::lang::ExpressionStatement)


def test_mini::lang::expressionstatement_constructor_exists():
    assert callable(mini::lang::ExpressionStatement.__init__)


def test_mini::lang::expressionstatement_constructor_args():
    sig = inspect.signature(mini::lang::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_mini::lang::ifstatement_is_not_abstract():
    assert not inspect.isabstract(mini::lang::IfStatement)


def test_mini::lang::ifstatement_constructor_exists():
    assert callable(mini::lang::IfStatement.__init__)


def test_mini::lang::ifstatement_constructor_args():
    sig = inspect.signature(mini::lang::IfStatement.__init__)
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
mini::lang::Statement_strategy = st.builds(
    mini::lang::Statement,
)
mini::lang::Block_strategy = st.builds(
    mini::lang::Block,
)
mini::lang::MiniLang_strategy = st.builds(
    mini::lang::MiniLang,
)
ComparisonExpression_strategy = st.builds(
    ComparisonExpression,
)
mini::lang::EqualsExpression_strategy = st.builds(
    mini::lang::EqualsExpression,
)
mini::lang::NotEqualsExpression_strategy = st.builds(
    mini::lang::NotEqualsExpression,
)
Expression_strategy = st.builds(
    Expression,
)
mini::lang::NameExpression_strategy = st.builds(
    mini::lang::NameExpression,
    name=
        safe_text
)
mini::lang::FOLCallExpression_strategy = st.builds(
    mini::lang::FOLCallExpression,
    method=
        safe_text,
    iterator=
        safe_text
)
mini::lang::ComparisonExpression_strategy = st.builds(
    mini::lang::ComparisonExpression,
)
mini::lang::Expression_strategy = st.builds(
    mini::lang::Expression,
)
Statement_strategy = st.builds(
    Statement,
)
mini::lang::AssignmentStatement_strategy = st.builds(
    mini::lang::AssignmentStatement,
)
mini::lang::ReturnStatement_strategy = st.builds(
    mini::lang::ReturnStatement,
)
mini::lang::ExpressionStatement_strategy = st.builds(
    mini::lang::ExpressionStatement,
)
mini::lang::IfStatement_strategy = st.builds(
    mini::lang::IfStatement,
)

@given(instance=mini::lang::Statement_strategy)
@settings(max_examples=50)
def test_mini::lang::statement_instantiation(instance):
    assert isinstance(instance, mini::lang::Statement)

@given(instance=mini::lang::Block_strategy)
@settings(max_examples=50)
def test_mini::lang::block_instantiation(instance):
    assert isinstance(instance, mini::lang::Block)

@given(instance=mini::lang::MiniLang_strategy)
@settings(max_examples=50)
def test_mini::lang::minilang_instantiation(instance):
    assert isinstance(instance, mini::lang::MiniLang)

@given(instance=ComparisonExpression_strategy)
@settings(max_examples=50)
def test_comparisonexpression_instantiation(instance):
    assert isinstance(instance, ComparisonExpression)

@given(instance=mini::lang::EqualsExpression_strategy)
@settings(max_examples=50)
def test_mini::lang::equalsexpression_instantiation(instance):
    assert isinstance(instance, mini::lang::EqualsExpression)

@given(instance=mini::lang::NotEqualsExpression_strategy)
@settings(max_examples=50)
def test_mini::lang::notequalsexpression_instantiation(instance):
    assert isinstance(instance, mini::lang::NotEqualsExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mini::lang::NameExpression_strategy)
@settings(max_examples=50)
def test_mini::lang::nameexpression_instantiation(instance):
    assert isinstance(instance, mini::lang::NameExpression)

@given(instance=mini::lang::NameExpression_strategy)
def test_mini::lang::nameexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mini::lang::NameExpression_strategy)
def test_mini::lang::nameexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mini::lang::FOLCallExpression_strategy)
@settings(max_examples=50)
def test_mini::lang::folcallexpression_instantiation(instance):
    assert isinstance(instance, mini::lang::FOLCallExpression)

@given(instance=mini::lang::FOLCallExpression_strategy)
def test_mini::lang::folcallexpression_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=mini::lang::FOLCallExpression_strategy)
def test_mini::lang::folcallexpression_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=mini::lang::FOLCallExpression_strategy)
def test_mini::lang::folcallexpression_iterator_type(instance):
    assert isinstance(instance.iterator, str)


@given(instance=mini::lang::FOLCallExpression_strategy)
def test_mini::lang::folcallexpression_iterator_setter(instance):
    original = instance.iterator
    instance.iterator = original
    assert instance.iterator == original

@given(instance=mini::lang::ComparisonExpression_strategy)
@settings(max_examples=50)
def test_mini::lang::comparisonexpression_instantiation(instance):
    assert isinstance(instance, mini::lang::ComparisonExpression)

@given(instance=mini::lang::Expression_strategy)
@settings(max_examples=50)
def test_mini::lang::expression_instantiation(instance):
    assert isinstance(instance, mini::lang::Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=mini::lang::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_mini::lang::assignmentstatement_instantiation(instance):
    assert isinstance(instance, mini::lang::AssignmentStatement)

@given(instance=mini::lang::ReturnStatement_strategy)
@settings(max_examples=50)
def test_mini::lang::returnstatement_instantiation(instance):
    assert isinstance(instance, mini::lang::ReturnStatement)

@given(instance=mini::lang::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_mini::lang::expressionstatement_instantiation(instance):
    assert isinstance(instance, mini::lang::ExpressionStatement)

@given(instance=mini::lang::IfStatement_strategy)
@settings(max_examples=50)
def test_mini::lang::ifstatement_instantiation(instance):
    assert isinstance(instance, mini::lang::IfStatement)
