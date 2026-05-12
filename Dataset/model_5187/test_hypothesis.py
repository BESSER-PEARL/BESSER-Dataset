import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    B,
    A,
    doublemulti_D,
    doublemulti_C,
    doublemulti_B,
    doublemulti_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_doublemulti_d_is_not_abstract():
    assert not inspect.isabstract(doublemulti_D)


def test_doublemulti_d_constructor_exists():
    assert callable(doublemulti_D.__init__)


def test_doublemulti_d_constructor_args():
    sig = inspect.signature(doublemulti_D.__init__)
    params = list(sig.parameters.keys())



def test_doublemulti_c_is_not_abstract():
    assert not inspect.isabstract(doublemulti_C)


def test_doublemulti_c_constructor_exists():
    assert callable(doublemulti_C.__init__)


def test_doublemulti_c_constructor_args():
    sig = inspect.signature(doublemulti_C.__init__)
    params = list(sig.parameters.keys())



def test_doublemulti_b_is_not_abstract():
    assert not inspect.isabstract(doublemulti_B)


def test_doublemulti_b_constructor_exists():
    assert callable(doublemulti_B.__init__)


def test_doublemulti_b_constructor_args():
    sig = inspect.signature(doublemulti_B.__init__)
    params = list(sig.parameters.keys())



def test_doublemulti_a_is_not_abstract():
    assert not inspect.isabstract(doublemulti_A)


def test_doublemulti_a_constructor_exists():
    assert callable(doublemulti_A.__init__)


def test_doublemulti_a_constructor_args():
    sig = inspect.signature(doublemulti_A.__init__)
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
B_strategy = st.builds(
    B,
)
A_strategy = st.builds(
    A,
)
doublemulti_D_strategy = st.builds(
    doublemulti_D,
)
doublemulti_C_strategy = st.builds(
    doublemulti_C,
)
doublemulti_B_strategy = st.builds(
    doublemulti_B,
)
doublemulti_A_strategy = st.builds(
    doublemulti_A,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=doublemulti_D_strategy)
@settings(max_examples=50)
def test_doublemulti_d_instantiation(instance):
    assert isinstance(instance, doublemulti_D)

@given(instance=doublemulti_C_strategy)
@settings(max_examples=50)
def test_doublemulti_c_instantiation(instance):
    assert isinstance(instance, doublemulti_C)

@given(instance=doublemulti_B_strategy)
@settings(max_examples=50)
def test_doublemulti_b_instantiation(instance):
    assert isinstance(instance, doublemulti_B)

@given(instance=doublemulti_A_strategy)
@settings(max_examples=50)
def test_doublemulti_a_instantiation(instance):
    assert isinstance(instance, doublemulti_A)
