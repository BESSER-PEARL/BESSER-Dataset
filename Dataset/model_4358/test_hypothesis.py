import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mini_lang_Statement,
    mini_lang_Block,
    mini_lang_MiniLang,
    ComparisonExpression,
    mini_lang_EqualsExpression,
    mini_lang_NotEqualsExpression,
    Expression,
    mini_lang_NameExpression,
    mini_lang_FOLCallExpression,
    mini_lang_ComparisonExpression,
    mini_lang_Expression,
    Statement,
    mini_lang_ExpressionStatement,
    mini_lang_AssignmentStatement,
    mini_lang_ReturnStatement,
    mini_lang_IfStatement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mini_lang_statement_is_not_abstract():
    assert not inspect.isabstract(mini_lang_Statement)


def test_mini_lang_statement_constructor_exists():
    assert callable(mini_lang_Statement.__init__)


def test_mini_lang_statement_constructor_args():
    sig = inspect.signature(mini_lang_Statement.__init__)
    params = list(sig.parameters.keys())



def test_mini_lang_block_is_not_abstract():
    assert not inspect.isabstract(mini_lang_Block)


def test_mini_lang_block_constructor_exists():
    assert callable(mini_lang_Block.__init__)


def test_mini_lang_block_constructor_args():
    sig = inspect.signature(mini_lang_Block.__init__)
    params = list(sig.parameters.keys())



def test_mini_lang_minilang_is_not_abstract():
    assert not inspect.isabstract(mini_lang_MiniLang)


def test_mini_lang_minilang_constructor_exists():
    assert callable(mini_lang_MiniLang.__init__)


def test_mini_lang_minilang_constructor_args():
    sig = inspect.signature(mini_lang_MiniLang.__init__)
    params = list(sig.parameters.keys())



def test_comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(ComparisonExpression)


def test_comparisonexpression_constructor_exists():
    assert callable(ComparisonExpression.__init__)


def test_comparisonexpression_constructor_args():
    sig = inspect.signature(ComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_mini_lang_equalsexpression_is_not_abstract():
    assert not inspect.isabstract(mini_lang_EqualsExpression)


def test_mini_lang_equalsexpression_constructor_exists():
    assert callable(mini_lang_EqualsExpression.__init__)


def test_mini_lang_equalsexpression_constructor_args():
    sig = inspect.signature(mini_lang_EqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_mini_lang_notequalsexpression_is_not_abstract():
    assert not inspect.isabstract(mini_lang_NotEqualsExpression)


def test_mini_lang_notequalsexpression_constructor_exists():
    assert callable(mini_lang_NotEqualsExpression.__init__)


def test_mini_lang_notequalsexpression_constructor_args():
    sig = inspect.signature(mini_lang_NotEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mini_lang_nameexpression_is_not_abstract():
    assert not inspect.isabstract(mini_lang_NameExpression)


def test_mini_lang_nameexpression_constructor_exists():
    assert callable(mini_lang_NameExpression.__init__)


def test_mini_lang_nameexpression_constructor_args():
    sig = inspect.signature(mini_lang_NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mini_lang_nameexpression_has_name():
    assert hasattr(mini_lang_NameExpression, "name")
    descriptor = None
    for klass in mini_lang_NameExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mini_lang_folcallexpression_is_not_abstract():
    assert not inspect.isabstract(mini_lang_FOLCallExpression)


def test_mini_lang_folcallexpression_constructor_exists():
    assert callable(mini_lang_FOLCallExpression.__init__)


def test_mini_lang_folcallexpression_constructor_args():
    sig = inspect.signature(mini_lang_FOLCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "iterator" in params, "Missing parameter 'iterator'"
    assert "method" in params, "Missing parameter 'method'"

def test_mini_lang_folcallexpression_has_iterator():
    assert hasattr(mini_lang_FOLCallExpression, "iterator")
    descriptor = None
    for klass in mini_lang_FOLCallExpression.__mro__:
        if "iterator" in klass.__dict__:
            descriptor = klass.__dict__["iterator"]
            break
    assert isinstance(descriptor, property)

def test_mini_lang_folcallexpression_has_method():
    assert hasattr(mini_lang_FOLCallExpression, "method")
    descriptor = None
    for klass in mini_lang_FOLCallExpression.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)



def test_mini_lang_comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(mini_lang_ComparisonExpression)


def test_mini_lang_comparisonexpression_constructor_exists():
    assert callable(mini_lang_ComparisonExpression.__init__)


def test_mini_lang_comparisonexpression_constructor_args():
    sig = inspect.signature(mini_lang_ComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_mini_lang_expression_is_not_abstract():
    assert not inspect.isabstract(mini_lang_Expression)


def test_mini_lang_expression_constructor_exists():
    assert callable(mini_lang_Expression.__init__)


def test_mini_lang_expression_constructor_args():
    sig = inspect.signature(mini_lang_Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_mini_lang_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(mini_lang_ExpressionStatement)


def test_mini_lang_expressionstatement_constructor_exists():
    assert callable(mini_lang_ExpressionStatement.__init__)


def test_mini_lang_expressionstatement_constructor_args():
    sig = inspect.signature(mini_lang_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_mini_lang_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(mini_lang_AssignmentStatement)


def test_mini_lang_assignmentstatement_constructor_exists():
    assert callable(mini_lang_AssignmentStatement.__init__)


def test_mini_lang_assignmentstatement_constructor_args():
    sig = inspect.signature(mini_lang_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_mini_lang_returnstatement_is_not_abstract():
    assert not inspect.isabstract(mini_lang_ReturnStatement)


def test_mini_lang_returnstatement_constructor_exists():
    assert callable(mini_lang_ReturnStatement.__init__)


def test_mini_lang_returnstatement_constructor_args():
    sig = inspect.signature(mini_lang_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_mini_lang_ifstatement_is_not_abstract():
    assert not inspect.isabstract(mini_lang_IfStatement)


def test_mini_lang_ifstatement_constructor_exists():
    assert callable(mini_lang_IfStatement.__init__)


def test_mini_lang_ifstatement_constructor_args():
    sig = inspect.signature(mini_lang_IfStatement.__init__)
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
mini_lang_Statement_strategy = st.builds(
    mini_lang_Statement,
)
mini_lang_Block_strategy = st.builds(
    mini_lang_Block,
)
mini_lang_MiniLang_strategy = st.builds(
    mini_lang_MiniLang,
)
ComparisonExpression_strategy = st.builds(
    ComparisonExpression,
)
mini_lang_EqualsExpression_strategy = st.builds(
    mini_lang_EqualsExpression,
)
mini_lang_NotEqualsExpression_strategy = st.builds(
    mini_lang_NotEqualsExpression,
)
Expression_strategy = st.builds(
    Expression,
)
mini_lang_NameExpression_strategy = st.builds(
    mini_lang_NameExpression,
    name=
        safe_text
)
mini_lang_FOLCallExpression_strategy = st.builds(
    mini_lang_FOLCallExpression,
    iterator=
        safe_text,
    method=
        safe_text
)
mini_lang_ComparisonExpression_strategy = st.builds(
    mini_lang_ComparisonExpression,
)
mini_lang_Expression_strategy = st.builds(
    mini_lang_Expression,
)
Statement_strategy = st.builds(
    Statement,
)
mini_lang_ExpressionStatement_strategy = st.builds(
    mini_lang_ExpressionStatement,
)
mini_lang_AssignmentStatement_strategy = st.builds(
    mini_lang_AssignmentStatement,
)
mini_lang_ReturnStatement_strategy = st.builds(
    mini_lang_ReturnStatement,
)
mini_lang_IfStatement_strategy = st.builds(
    mini_lang_IfStatement,
)

@given(instance=mini_lang_Statement_strategy)
@settings(max_examples=50)
def test_mini_lang_statement_instantiation(instance):
    assert isinstance(instance, mini_lang_Statement)

@given(instance=mini_lang_Block_strategy)
@settings(max_examples=50)
def test_mini_lang_block_instantiation(instance):
    assert isinstance(instance, mini_lang_Block)

@given(instance=mini_lang_MiniLang_strategy)
@settings(max_examples=50)
def test_mini_lang_minilang_instantiation(instance):
    assert isinstance(instance, mini_lang_MiniLang)

@given(instance=ComparisonExpression_strategy)
@settings(max_examples=50)
def test_comparisonexpression_instantiation(instance):
    assert isinstance(instance, ComparisonExpression)

@given(instance=mini_lang_EqualsExpression_strategy)
@settings(max_examples=50)
def test_mini_lang_equalsexpression_instantiation(instance):
    assert isinstance(instance, mini_lang_EqualsExpression)

@given(instance=mini_lang_NotEqualsExpression_strategy)
@settings(max_examples=50)
def test_mini_lang_notequalsexpression_instantiation(instance):
    assert isinstance(instance, mini_lang_NotEqualsExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mini_lang_NameExpression_strategy)
@settings(max_examples=50)
def test_mini_lang_nameexpression_instantiation(instance):
    assert isinstance(instance, mini_lang_NameExpression)



@given(instance=mini_lang_NameExpression_strategy)
def test_mini_lang_nameexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mini_lang_FOLCallExpression_strategy)
@settings(max_examples=50)
def test_mini_lang_folcallexpression_instantiation(instance):
    assert isinstance(instance, mini_lang_FOLCallExpression)



@given(instance=mini_lang_FOLCallExpression_strategy)
def test_mini_lang_folcallexpression_iterator_setter(instance):
    original = instance.iterator
    instance.iterator = original
    assert instance.iterator == original



@given(instance=mini_lang_FOLCallExpression_strategy)
def test_mini_lang_folcallexpression_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=mini_lang_ComparisonExpression_strategy)
@settings(max_examples=50)
def test_mini_lang_comparisonexpression_instantiation(instance):
    assert isinstance(instance, mini_lang_ComparisonExpression)

@given(instance=mini_lang_Expression_strategy)
@settings(max_examples=50)
def test_mini_lang_expression_instantiation(instance):
    assert isinstance(instance, mini_lang_Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=mini_lang_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_mini_lang_expressionstatement_instantiation(instance):
    assert isinstance(instance, mini_lang_ExpressionStatement)

@given(instance=mini_lang_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_mini_lang_assignmentstatement_instantiation(instance):
    assert isinstance(instance, mini_lang_AssignmentStatement)

@given(instance=mini_lang_ReturnStatement_strategy)
@settings(max_examples=50)
def test_mini_lang_returnstatement_instantiation(instance):
    assert isinstance(instance, mini_lang_ReturnStatement)

@given(instance=mini_lang_IfStatement_strategy)
@settings(max_examples=50)
def test_mini_lang_ifstatement_instantiation(instance):
    assert isinstance(instance, mini_lang_IfStatement)
