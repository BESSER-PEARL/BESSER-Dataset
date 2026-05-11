import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cardinality6::B,
    cardinality6::A,
    cardinality6::Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cardinality6::b_is_not_abstract():
    assert not inspect.isabstract(cardinality6::B)


def test_cardinality6::b_constructor_exists():
    assert callable(cardinality6::B.__init__)


def test_cardinality6::b_constructor_args():
    sig = inspect.signature(cardinality6::B.__init__)
    params = list(sig.parameters.keys())



def test_cardinality6::a_is_not_abstract():
    assert not inspect.isabstract(cardinality6::A)


def test_cardinality6::a_constructor_exists():
    assert callable(cardinality6::A.__init__)


def test_cardinality6::a_constructor_args():
    sig = inspect.signature(cardinality6::A.__init__)
    params = list(sig.parameters.keys())



def test_cardinality6::root_is_not_abstract():
    assert not inspect.isabstract(cardinality6::Root)


def test_cardinality6::root_constructor_exists():
    assert callable(cardinality6::Root.__init__)


def test_cardinality6::root_constructor_args():
    sig = inspect.signature(cardinality6::Root.__init__)
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
cardinality6::B_strategy = st.builds(
    cardinality6::B,
)
cardinality6::A_strategy = st.builds(
    cardinality6::A,
)
cardinality6::Root_strategy = st.builds(
    cardinality6::Root,
)

@given(instance=cardinality6::B_strategy)
@settings(max_examples=50)
def test_cardinality6::b_instantiation(instance):
    assert isinstance(instance, cardinality6::B)

@given(instance=cardinality6::A_strategy)
@settings(max_examples=50)
def test_cardinality6::a_instantiation(instance):
    assert isinstance(instance, cardinality6::A)

@given(instance=cardinality6::Root_strategy)
@settings(max_examples=50)
def test_cardinality6::root_instantiation(instance):
    assert isinstance(instance, cardinality6::Root)
