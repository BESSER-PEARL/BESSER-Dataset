import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OclExpression,
    operators::IfExp,
    operators::OperationCallExp,
    operators::Type,
    operators::OclExpression,
    operators::OclType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_operators::ifexp_is_not_abstract():
    assert not inspect.isabstract(operators::IfExp)


def test_operators::ifexp_constructor_exists():
    assert callable(operators::IfExp.__init__)


def test_operators::ifexp_constructor_args():
    sig = inspect.signature(operators::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_operators::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(operators::OperationCallExp)


def test_operators::operationcallexp_constructor_exists():
    assert callable(operators::OperationCallExp.__init__)


def test_operators::operationcallexp_constructor_args():
    sig = inspect.signature(operators::OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_operators::operationcallexp_has_name():
    assert hasattr(operators::OperationCallExp, "name")
    descriptor = None
    for klass in operators::OperationCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_operators::type_is_not_abstract():
    assert not inspect.isabstract(operators::Type)


def test_operators::type_constructor_exists():
    assert callable(operators::Type.__init__)


def test_operators::type_constructor_args():
    sig = inspect.signature(operators::Type.__init__)
    params = list(sig.parameters.keys())



def test_operators::oclexpression_is_not_abstract():
    assert not inspect.isabstract(operators::OclExpression)


def test_operators::oclexpression_constructor_exists():
    assert callable(operators::OclExpression.__init__)


def test_operators::oclexpression_constructor_args():
    sig = inspect.signature(operators::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_operators::ocltype_is_not_abstract():
    assert not inspect.isabstract(operators::OclType)


def test_operators::ocltype_constructor_exists():
    assert callable(operators::OclType.__init__)


def test_operators::ocltype_constructor_args():
    sig = inspect.signature(operators::OclType.__init__)
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
OclExpression_strategy = st.builds(
    OclExpression,
)
operators::IfExp_strategy = st.builds(
    operators::IfExp,
)
operators::OperationCallExp_strategy = st.builds(
    operators::OperationCallExp,
    name=
        safe_text
)
operators::Type_strategy = st.builds(
    operators::Type,
)
operators::OclExpression_strategy = st.builds(
    operators::OclExpression,
)
operators::OclType_strategy = st.builds(
    operators::OclType,
)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=operators::IfExp_strategy)
@settings(max_examples=50)
def test_operators::ifexp_instantiation(instance):
    assert isinstance(instance, operators::IfExp)

@given(instance=operators::OperationCallExp_strategy)
@settings(max_examples=50)
def test_operators::operationcallexp_instantiation(instance):
    assert isinstance(instance, operators::OperationCallExp)

@given(instance=operators::OperationCallExp_strategy)
def test_operators::operationcallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=operators::OperationCallExp_strategy)
def test_operators::operationcallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=operators::Type_strategy)
@settings(max_examples=50)
def test_operators::type_instantiation(instance):
    assert isinstance(instance, operators::Type)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=operators::Type_strategy)
@settings(max_examples=30)
def test_operators::type_issupertypeof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSuperTypeOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSuperTypeOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSuperTypeOf' in operators::Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSuperTypeOf' in operators::Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSuperTypeOf' in operators::Type is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=operators::Type_strategy)
@settings(max_examples=30)
def test_operators::type_issametype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSameType(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSameType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSameType' in operators::Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSameType' in operators::Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSameType' in operators::Type is not implemented or raised an error")

@given(instance=operators::OclExpression_strategy)
@settings(max_examples=50)
def test_operators::oclexpression_instantiation(instance):
    assert isinstance(instance, operators::OclExpression)

@given(instance=operators::OclType_strategy)
@settings(max_examples=50)
def test_operators::ocltype_instantiation(instance):
    assert isinstance(instance, operators::OclType)
