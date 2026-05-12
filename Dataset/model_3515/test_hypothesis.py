import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testtypesystem_Value,
    testtypesystem_State,
    testtypesystem_Expression,
    testtypesystem_Assignment,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testtypesystem_value_is_not_abstract():
    assert not inspect.isabstract(testtypesystem_Value)


def test_testtypesystem_value_constructor_exists():
    assert callable(testtypesystem_Value.__init__)


def test_testtypesystem_value_constructor_args():
    sig = inspect.signature(testtypesystem_Value.__init__)
    params = list(sig.parameters.keys())



def test_testtypesystem_state_is_not_abstract():
    assert not inspect.isabstract(testtypesystem_State)


def test_testtypesystem_state_constructor_exists():
    assert callable(testtypesystem_State.__init__)


def test_testtypesystem_state_constructor_args():
    sig = inspect.signature(testtypesystem_State.__init__)
    params = list(sig.parameters.keys())



def test_testtypesystem_expression_is_not_abstract():
    assert not inspect.isabstract(testtypesystem_Expression)


def test_testtypesystem_expression_constructor_exists():
    assert callable(testtypesystem_Expression.__init__)


def test_testtypesystem_expression_constructor_args():
    sig = inspect.signature(testtypesystem_Expression.__init__)
    params = list(sig.parameters.keys())



def test_testtypesystem_assignment_is_not_abstract():
    assert not inspect.isabstract(testtypesystem_Assignment)


def test_testtypesystem_assignment_constructor_exists():
    assert callable(testtypesystem_Assignment.__init__)


def test_testtypesystem_assignment_constructor_args():
    sig = inspect.signature(testtypesystem_Assignment.__init__)
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
testtypesystem_Value_strategy = st.builds(
    testtypesystem_Value,
)
testtypesystem_State_strategy = st.builds(
    testtypesystem_State,
)
testtypesystem_Expression_strategy = st.builds(
    testtypesystem_Expression,
)
testtypesystem_Assignment_strategy = st.builds(
    testtypesystem_Assignment,
)

@given(instance=testtypesystem_Value_strategy)
@settings(max_examples=50)
def test_testtypesystem_value_instantiation(instance):
    assert isinstance(instance, testtypesystem_Value)

@given(instance=testtypesystem_State_strategy)
@settings(max_examples=50)
def test_testtypesystem_state_instantiation(instance):
    assert isinstance(instance, testtypesystem_State)

@given(instance=testtypesystem_Expression_strategy)
@settings(max_examples=50)
def test_testtypesystem_expression_instantiation(instance):
    assert isinstance(instance, testtypesystem_Expression)

@given(instance=testtypesystem_Assignment_strategy)
@settings(max_examples=50)
def test_testtypesystem_assignment_instantiation(instance):
    assert isinstance(instance, testtypesystem_Assignment)
