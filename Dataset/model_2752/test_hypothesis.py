import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    cardinality6_B,
    cardinality6_A,
    cardinality6_Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cardinality6_b_is_not_abstract():
    assert not inspect.isabstract(cardinality6_B)


def test_cardinality6_b_constructor_exists():
    assert callable(cardinality6_B.__init__)


def test_cardinality6_b_constructor_args():
    sig = inspect.signature(cardinality6_B.__init__)
    params = list(sig.parameters.keys())



def test_cardinality6_a_is_not_abstract():
    assert not inspect.isabstract(cardinality6_A)


def test_cardinality6_a_constructor_exists():
    assert callable(cardinality6_A.__init__)


def test_cardinality6_a_constructor_args():
    sig = inspect.signature(cardinality6_A.__init__)
    params = list(sig.parameters.keys())



def test_cardinality6_root_is_not_abstract():
    assert not inspect.isabstract(cardinality6_Root)


def test_cardinality6_root_constructor_exists():
    assert callable(cardinality6_Root.__init__)


def test_cardinality6_root_constructor_args():
    sig = inspect.signature(cardinality6_Root.__init__)
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
cardinality6_B_strategy = st.builds(
    cardinality6_B,
)
cardinality6_A_strategy = st.builds(
    cardinality6_A,
)
cardinality6_Root_strategy = st.builds(
    cardinality6_Root,
)

@given(instance=cardinality6_B_strategy)
@settings(max_examples=50)
def test_cardinality6_b_instantiation(instance):
    assert isinstance(instance, cardinality6_B)

@given(instance=cardinality6_A_strategy)
@settings(max_examples=50)
def test_cardinality6_a_instantiation(instance):
    assert isinstance(instance, cardinality6_A)

@given(instance=cardinality6_Root_strategy)
@settings(max_examples=50)
def test_cardinality6_root_instantiation(instance):
    assert isinstance(instance, cardinality6_Root)
