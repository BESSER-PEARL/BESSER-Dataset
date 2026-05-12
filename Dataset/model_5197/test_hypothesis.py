import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    B,
    source_D,
    source_C,
    C,
    source_B,
    source_A,
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



def test_source_d_is_not_abstract():
    assert not inspect.isabstract(source_D)


def test_source_d_constructor_exists():
    assert callable(source_D.__init__)


def test_source_d_constructor_args():
    sig = inspect.signature(source_D.__init__)
    params = list(sig.parameters.keys())



def test_source_c_is_not_abstract():
    assert not inspect.isabstract(source_C)


def test_source_c_constructor_exists():
    assert callable(source_C.__init__)


def test_source_c_constructor_args():
    sig = inspect.signature(source_C.__init__)
    params = list(sig.parameters.keys())



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())



def test_source_b_is_not_abstract():
    assert not inspect.isabstract(source_B)


def test_source_b_constructor_exists():
    assert callable(source_B.__init__)


def test_source_b_constructor_args():
    sig = inspect.signature(source_B.__init__)
    params = list(sig.parameters.keys())



def test_source_a_is_not_abstract():
    assert not inspect.isabstract(source_A)


def test_source_a_constructor_exists():
    assert callable(source_A.__init__)


def test_source_a_constructor_args():
    sig = inspect.signature(source_A.__init__)
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
source_D_strategy = st.builds(
    source_D,
)
source_C_strategy = st.builds(
    source_C,
)
C_strategy = st.builds(
    C,
)
source_B_strategy = st.builds(
    source_B,
)
source_A_strategy = st.builds(
    source_A,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=source_D_strategy)
@settings(max_examples=50)
def test_source_d_instantiation(instance):
    assert isinstance(instance, source_D)

@given(instance=source_C_strategy)
@settings(max_examples=50)
def test_source_c_instantiation(instance):
    assert isinstance(instance, source_C)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=source_B_strategy)
@settings(max_examples=50)
def test_source_b_instantiation(instance):
    assert isinstance(instance, source_B)

@given(instance=source_A_strategy)
@settings(max_examples=50)
def test_source_a_instantiation(instance):
    assert isinstance(instance, source_A)
