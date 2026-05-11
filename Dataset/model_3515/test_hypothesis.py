import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testtypesystem::Value,
    testtypesystem::State,
    testtypesystem::Expression,
    testtypesystem::Assignment,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testtypesystem::value_is_not_abstract():
    assert not inspect.isabstract(testtypesystem::Value)


def test_testtypesystem::value_constructor_exists():
    assert callable(testtypesystem::Value.__init__)


def test_testtypesystem::value_constructor_args():
    sig = inspect.signature(testtypesystem::Value.__init__)
    params = list(sig.parameters.keys())



def test_testtypesystem::state_is_not_abstract():
    assert not inspect.isabstract(testtypesystem::State)


def test_testtypesystem::state_constructor_exists():
    assert callable(testtypesystem::State.__init__)


def test_testtypesystem::state_constructor_args():
    sig = inspect.signature(testtypesystem::State.__init__)
    params = list(sig.parameters.keys())



def test_testtypesystem::expression_is_not_abstract():
    assert not inspect.isabstract(testtypesystem::Expression)


def test_testtypesystem::expression_constructor_exists():
    assert callable(testtypesystem::Expression.__init__)


def test_testtypesystem::expression_constructor_args():
    sig = inspect.signature(testtypesystem::Expression.__init__)
    params = list(sig.parameters.keys())



def test_testtypesystem::assignment_is_not_abstract():
    assert not inspect.isabstract(testtypesystem::Assignment)


def test_testtypesystem::assignment_constructor_exists():
    assert callable(testtypesystem::Assignment.__init__)


def test_testtypesystem::assignment_constructor_args():
    sig = inspect.signature(testtypesystem::Assignment.__init__)
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
testtypesystem::Value_strategy = st.builds(
    testtypesystem::Value,
)
testtypesystem::State_strategy = st.builds(
    testtypesystem::State,
)
testtypesystem::Expression_strategy = st.builds(
    testtypesystem::Expression,
)
testtypesystem::Assignment_strategy = st.builds(
    testtypesystem::Assignment,
)

@given(instance=testtypesystem::Value_strategy)
@settings(max_examples=50)
def test_testtypesystem::value_instantiation(instance):
    assert isinstance(instance, testtypesystem::Value)

@given(instance=testtypesystem::State_strategy)
@settings(max_examples=50)
def test_testtypesystem::state_instantiation(instance):
    assert isinstance(instance, testtypesystem::State)

@given(instance=testtypesystem::Expression_strategy)
@settings(max_examples=50)
def test_testtypesystem::expression_instantiation(instance):
    assert isinstance(instance, testtypesystem::Expression)

@given(instance=testtypesystem::Assignment_strategy)
@settings(max_examples=50)
def test_testtypesystem::assignment_instantiation(instance):
    assert isinstance(instance, testtypesystem::Assignment)
