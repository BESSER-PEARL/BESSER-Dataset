import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    root::sub::D,
    root::sub::C,
    root::B,
    root::A,
    root::sub2::E,
    root::subsub::F,
    root::subsub::E,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root::sub::d_is_not_abstract():
    assert not inspect.isabstract(root::sub::D)


def test_root::sub::d_constructor_exists():
    assert callable(root::sub::D.__init__)


def test_root::sub::d_constructor_args():
    sig = inspect.signature(root::sub::D.__init__)
    params = list(sig.parameters.keys())



def test_root::sub::c_is_not_abstract():
    assert not inspect.isabstract(root::sub::C)


def test_root::sub::c_constructor_exists():
    assert callable(root::sub::C.__init__)


def test_root::sub::c_constructor_args():
    sig = inspect.signature(root::sub::C.__init__)
    params = list(sig.parameters.keys())



def test_root::b_is_not_abstract():
    assert not inspect.isabstract(root::B)


def test_root::b_constructor_exists():
    assert callable(root::B.__init__)


def test_root::b_constructor_args():
    sig = inspect.signature(root::B.__init__)
    params = list(sig.parameters.keys())



def test_root::a_is_not_abstract():
    assert not inspect.isabstract(root::A)


def test_root::a_constructor_exists():
    assert callable(root::A.__init__)


def test_root::a_constructor_args():
    sig = inspect.signature(root::A.__init__)
    params = list(sig.parameters.keys())



def test_root::sub2::e_is_not_abstract():
    assert not inspect.isabstract(root::sub2::E)


def test_root::sub2::e_constructor_exists():
    assert callable(root::sub2::E.__init__)


def test_root::sub2::e_constructor_args():
    sig = inspect.signature(root::sub2::E.__init__)
    params = list(sig.parameters.keys())



def test_root::subsub::f_is_not_abstract():
    assert not inspect.isabstract(root::subsub::F)


def test_root::subsub::f_constructor_exists():
    assert callable(root::subsub::F.__init__)


def test_root::subsub::f_constructor_args():
    sig = inspect.signature(root::subsub::F.__init__)
    params = list(sig.parameters.keys())



def test_root::subsub::e_is_not_abstract():
    assert not inspect.isabstract(root::subsub::E)


def test_root::subsub::e_constructor_exists():
    assert callable(root::subsub::E.__init__)


def test_root::subsub::e_constructor_args():
    sig = inspect.signature(root::subsub::E.__init__)
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
root::sub::D_strategy = st.builds(
    root::sub::D,
)
root::sub::C_strategy = st.builds(
    root::sub::C,
)
root::B_strategy = st.builds(
    root::B,
)
root::A_strategy = st.builds(
    root::A,
)
root::sub2::E_strategy = st.builds(
    root::sub2::E,
)
root::subsub::F_strategy = st.builds(
    root::subsub::F,
)
root::subsub::E_strategy = st.builds(
    root::subsub::E,
)

@given(instance=root::sub::D_strategy)
@settings(max_examples=50)
def test_root::sub::d_instantiation(instance):
    assert isinstance(instance, root::sub::D)

@given(instance=root::sub::C_strategy)
@settings(max_examples=50)
def test_root::sub::c_instantiation(instance):
    assert isinstance(instance, root::sub::C)

@given(instance=root::B_strategy)
@settings(max_examples=50)
def test_root::b_instantiation(instance):
    assert isinstance(instance, root::B)

@given(instance=root::A_strategy)
@settings(max_examples=50)
def test_root::a_instantiation(instance):
    assert isinstance(instance, root::A)

@given(instance=root::sub2::E_strategy)
@settings(max_examples=50)
def test_root::sub2::e_instantiation(instance):
    assert isinstance(instance, root::sub2::E)

@given(instance=root::subsub::F_strategy)
@settings(max_examples=50)
def test_root::subsub::f_instantiation(instance):
    assert isinstance(instance, root::subsub::F)

@given(instance=root::subsub::E_strategy)
@settings(max_examples=50)
def test_root::subsub::e_instantiation(instance):
    assert isinstance(instance, root::subsub::E)
