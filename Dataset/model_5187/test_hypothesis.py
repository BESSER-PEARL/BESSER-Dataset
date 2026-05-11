import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    B,
    A,
    doublemulti::D,
    doublemulti::C,
    doublemulti::B,
    doublemulti::A,
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



def test_doublemulti::d_is_not_abstract():
    assert not inspect.isabstract(doublemulti::D)


def test_doublemulti::d_constructor_exists():
    assert callable(doublemulti::D.__init__)


def test_doublemulti::d_constructor_args():
    sig = inspect.signature(doublemulti::D.__init__)
    params = list(sig.parameters.keys())



def test_doublemulti::c_is_not_abstract():
    assert not inspect.isabstract(doublemulti::C)


def test_doublemulti::c_constructor_exists():
    assert callable(doublemulti::C.__init__)


def test_doublemulti::c_constructor_args():
    sig = inspect.signature(doublemulti::C.__init__)
    params = list(sig.parameters.keys())



def test_doublemulti::b_is_not_abstract():
    assert not inspect.isabstract(doublemulti::B)


def test_doublemulti::b_constructor_exists():
    assert callable(doublemulti::B.__init__)


def test_doublemulti::b_constructor_args():
    sig = inspect.signature(doublemulti::B.__init__)
    params = list(sig.parameters.keys())



def test_doublemulti::a_is_not_abstract():
    assert not inspect.isabstract(doublemulti::A)


def test_doublemulti::a_constructor_exists():
    assert callable(doublemulti::A.__init__)


def test_doublemulti::a_constructor_args():
    sig = inspect.signature(doublemulti::A.__init__)
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
doublemulti::D_strategy = st.builds(
    doublemulti::D,
)
doublemulti::C_strategy = st.builds(
    doublemulti::C,
)
doublemulti::B_strategy = st.builds(
    doublemulti::B,
)
doublemulti::A_strategy = st.builds(
    doublemulti::A,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=doublemulti::D_strategy)
@settings(max_examples=50)
def test_doublemulti::d_instantiation(instance):
    assert isinstance(instance, doublemulti::D)

@given(instance=doublemulti::C_strategy)
@settings(max_examples=50)
def test_doublemulti::c_instantiation(instance):
    assert isinstance(instance, doublemulti::C)

@given(instance=doublemulti::B_strategy)
@settings(max_examples=50)
def test_doublemulti::b_instantiation(instance):
    assert isinstance(instance, doublemulti::B)

@given(instance=doublemulti::A_strategy)
@settings(max_examples=50)
def test_doublemulti::a_instantiation(instance):
    assert isinstance(instance, doublemulti::A)
