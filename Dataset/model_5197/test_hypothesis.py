import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    B,
    source::D,
    source::C,
    C,
    source::B,
    source::A,
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



def test_source::d_is_not_abstract():
    assert not inspect.isabstract(source::D)


def test_source::d_constructor_exists():
    assert callable(source::D.__init__)


def test_source::d_constructor_args():
    sig = inspect.signature(source::D.__init__)
    params = list(sig.parameters.keys())



def test_source::c_is_not_abstract():
    assert not inspect.isabstract(source::C)


def test_source::c_constructor_exists():
    assert callable(source::C.__init__)


def test_source::c_constructor_args():
    sig = inspect.signature(source::C.__init__)
    params = list(sig.parameters.keys())



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())



def test_source::b_is_not_abstract():
    assert not inspect.isabstract(source::B)


def test_source::b_constructor_exists():
    assert callable(source::B.__init__)


def test_source::b_constructor_args():
    sig = inspect.signature(source::B.__init__)
    params = list(sig.parameters.keys())



def test_source::a_is_not_abstract():
    assert not inspect.isabstract(source::A)


def test_source::a_constructor_exists():
    assert callable(source::A.__init__)


def test_source::a_constructor_args():
    sig = inspect.signature(source::A.__init__)
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
source::D_strategy = st.builds(
    source::D,
)
source::C_strategy = st.builds(
    source::C,
)
C_strategy = st.builds(
    C,
)
source::B_strategy = st.builds(
    source::B,
)
source::A_strategy = st.builds(
    source::A,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=source::D_strategy)
@settings(max_examples=50)
def test_source::d_instantiation(instance):
    assert isinstance(instance, source::D)

@given(instance=source::C_strategy)
@settings(max_examples=50)
def test_source::c_instantiation(instance):
    assert isinstance(instance, source::C)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=source::B_strategy)
@settings(max_examples=50)
def test_source::b_instantiation(instance):
    assert isinstance(instance, source::B)

@given(instance=source::A_strategy)
@settings(max_examples=50)
def test_source::a_instantiation(instance):
    assert isinstance(instance, source::A)
