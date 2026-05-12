import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    E,
    A,
    astrans_B,
    astrans_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_e_is_not_abstract():
    assert not inspect.isabstract(E)


def test_e_constructor_exists():
    assert callable(E.__init__)


def test_e_constructor_args():
    sig = inspect.signature(E.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_astrans_b_is_not_abstract():
    assert not inspect.isabstract(astrans_B)


def test_astrans_b_constructor_exists():
    assert callable(astrans_B.__init__)


def test_astrans_b_constructor_args():
    sig = inspect.signature(astrans_B.__init__)
    params = list(sig.parameters.keys())



def test_astrans_a_is_not_abstract():
    assert not inspect.isabstract(astrans_A)


def test_astrans_a_constructor_exists():
    assert callable(astrans_A.__init__)


def test_astrans_a_constructor_args():
    sig = inspect.signature(astrans_A.__init__)
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
E_strategy = st.builds(
    E,
)
A_strategy = st.builds(
    A,
)
astrans_B_strategy = st.builds(
    astrans_B,
)
astrans_A_strategy = st.builds(
    astrans_A,
)

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=astrans_B_strategy)
@settings(max_examples=50)
def test_astrans_b_instantiation(instance):
    assert isinstance(instance, astrans_B)

@given(instance=astrans_A_strategy)
@settings(max_examples=50)
def test_astrans_a_instantiation(instance):
    assert isinstance(instance, astrans_A)
