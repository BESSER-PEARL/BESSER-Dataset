import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_A,
    test_B,
    test_Compo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_a_is_not_abstract():
    assert not inspect.isabstract(test_A)


def test_test_a_constructor_exists():
    assert callable(test_A.__init__)


def test_test_a_constructor_args():
    sig = inspect.signature(test_A.__init__)
    params = list(sig.parameters.keys())



def test_test_b_is_not_abstract():
    assert not inspect.isabstract(test_B)


def test_test_b_constructor_exists():
    assert callable(test_B.__init__)


def test_test_b_constructor_args():
    sig = inspect.signature(test_B.__init__)
    params = list(sig.parameters.keys())



def test_test_compo_is_not_abstract():
    assert not inspect.isabstract(test_Compo)


def test_test_compo_constructor_exists():
    assert callable(test_Compo.__init__)


def test_test_compo_constructor_args():
    sig = inspect.signature(test_Compo.__init__)
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
test_A_strategy = st.builds(
    test_A,
)
test_B_strategy = st.builds(
    test_B,
)
test_Compo_strategy = st.builds(
    test_Compo,
)

@given(instance=test_A_strategy)
@settings(max_examples=50)
def test_test_a_instantiation(instance):
    assert isinstance(instance, test_A)

@given(instance=test_B_strategy)
@settings(max_examples=50)
def test_test_b_instantiation(instance):
    assert isinstance(instance, test_B)

@given(instance=test_Compo_strategy)
@settings(max_examples=50)
def test_test_compo_instantiation(instance):
    assert isinstance(instance, test_Compo)
