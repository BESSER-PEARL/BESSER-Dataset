import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    reference::Y,
    reference::B1,
    reference::C,
    reference::X,
    reference::B,
    reference::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_reference::y_is_not_abstract():
    assert not inspect.isabstract(reference::Y)


def test_reference::y_constructor_exists():
    assert callable(reference::Y.__init__)


def test_reference::y_constructor_args():
    sig = inspect.signature(reference::Y.__init__)
    params = list(sig.parameters.keys())



def test_reference::b1_is_not_abstract():
    assert not inspect.isabstract(reference::B1)


def test_reference::b1_constructor_exists():
    assert callable(reference::B1.__init__)


def test_reference::b1_constructor_args():
    sig = inspect.signature(reference::B1.__init__)
    params = list(sig.parameters.keys())



def test_reference::c_is_not_abstract():
    assert not inspect.isabstract(reference::C)


def test_reference::c_constructor_exists():
    assert callable(reference::C.__init__)


def test_reference::c_constructor_args():
    sig = inspect.signature(reference::C.__init__)
    params = list(sig.parameters.keys())



def test_reference::x_is_not_abstract():
    assert not inspect.isabstract(reference::X)


def test_reference::x_constructor_exists():
    assert callable(reference::X.__init__)


def test_reference::x_constructor_args():
    sig = inspect.signature(reference::X.__init__)
    params = list(sig.parameters.keys())



def test_reference::b_is_not_abstract():
    assert not inspect.isabstract(reference::B)


def test_reference::b_constructor_exists():
    assert callable(reference::B.__init__)


def test_reference::b_constructor_args():
    sig = inspect.signature(reference::B.__init__)
    params = list(sig.parameters.keys())



def test_reference::a_is_not_abstract():
    assert not inspect.isabstract(reference::A)


def test_reference::a_constructor_exists():
    assert callable(reference::A.__init__)


def test_reference::a_constructor_args():
    sig = inspect.signature(reference::A.__init__)
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
reference::Y_strategy = st.builds(
    reference::Y,
)
reference::B1_strategy = st.builds(
    reference::B1,
)
reference::C_strategy = st.builds(
    reference::C,
)
reference::X_strategy = st.builds(
    reference::X,
)
reference::B_strategy = st.builds(
    reference::B,
)
reference::A_strategy = st.builds(
    reference::A,
)

@given(instance=reference::Y_strategy)
@settings(max_examples=50)
def test_reference::y_instantiation(instance):
    assert isinstance(instance, reference::Y)

@given(instance=reference::B1_strategy)
@settings(max_examples=50)
def test_reference::b1_instantiation(instance):
    assert isinstance(instance, reference::B1)

@given(instance=reference::C_strategy)
@settings(max_examples=50)
def test_reference::c_instantiation(instance):
    assert isinstance(instance, reference::C)

@given(instance=reference::X_strategy)
@settings(max_examples=50)
def test_reference::x_instantiation(instance):
    assert isinstance(instance, reference::X)

@given(instance=reference::B_strategy)
@settings(max_examples=50)
def test_reference::b_instantiation(instance):
    assert isinstance(instance, reference::B)

@given(instance=reference::A_strategy)
@settings(max_examples=50)
def test_reference::a_instantiation(instance):
    assert isinstance(instance, reference::A)
