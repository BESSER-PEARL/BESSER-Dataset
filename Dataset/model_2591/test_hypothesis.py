import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    root::subpackage2::C,
    root::subsubpackage1::D,
    root::subpackage1::B,
    root::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root::subpackage2::c_is_not_abstract():
    assert not inspect.isabstract(root::subpackage2::C)


def test_root::subpackage2::c_constructor_exists():
    assert callable(root::subpackage2::C.__init__)


def test_root::subpackage2::c_constructor_args():
    sig = inspect.signature(root::subpackage2::C.__init__)
    params = list(sig.parameters.keys())



def test_root::subsubpackage1::d_is_not_abstract():
    assert not inspect.isabstract(root::subsubpackage1::D)


def test_root::subsubpackage1::d_constructor_exists():
    assert callable(root::subsubpackage1::D.__init__)


def test_root::subsubpackage1::d_constructor_args():
    sig = inspect.signature(root::subsubpackage1::D.__init__)
    params = list(sig.parameters.keys())



def test_root::subpackage1::b_is_not_abstract():
    assert not inspect.isabstract(root::subpackage1::B)


def test_root::subpackage1::b_constructor_exists():
    assert callable(root::subpackage1::B.__init__)


def test_root::subpackage1::b_constructor_args():
    sig = inspect.signature(root::subpackage1::B.__init__)
    params = list(sig.parameters.keys())



def test_root::a_is_not_abstract():
    assert not inspect.isabstract(root::A)


def test_root::a_constructor_exists():
    assert callable(root::A.__init__)


def test_root::a_constructor_args():
    sig = inspect.signature(root::A.__init__)
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
root::subpackage2::C_strategy = st.builds(
    root::subpackage2::C,
)
root::subsubpackage1::D_strategy = st.builds(
    root::subsubpackage1::D,
)
root::subpackage1::B_strategy = st.builds(
    root::subpackage1::B,
)
root::A_strategy = st.builds(
    root::A,
)

@given(instance=root::subpackage2::C_strategy)
@settings(max_examples=50)
def test_root::subpackage2::c_instantiation(instance):
    assert isinstance(instance, root::subpackage2::C)

@given(instance=root::subsubpackage1::D_strategy)
@settings(max_examples=50)
def test_root::subsubpackage1::d_instantiation(instance):
    assert isinstance(instance, root::subsubpackage1::D)

@given(instance=root::subpackage1::B_strategy)
@settings(max_examples=50)
def test_root::subpackage1::b_instantiation(instance):
    assert isinstance(instance, root::subpackage1::B)

@given(instance=root::A_strategy)
@settings(max_examples=50)
def test_root::a_instantiation(instance):
    assert isinstance(instance, root::A)
