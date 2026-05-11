import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::G,
    test::H,
    test::F,
    test::D,
    test::I,
    test::E,
    test::C,
    test::B,
    test::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::g_is_not_abstract():
    assert not inspect.isabstract(test::G)


def test_test::g_constructor_exists():
    assert callable(test::G.__init__)


def test_test::g_constructor_args():
    sig = inspect.signature(test::G.__init__)
    params = list(sig.parameters.keys())



def test_test::h_is_not_abstract():
    assert not inspect.isabstract(test::H)


def test_test::h_constructor_exists():
    assert callable(test::H.__init__)


def test_test::h_constructor_args():
    sig = inspect.signature(test::H.__init__)
    params = list(sig.parameters.keys())



def test_test::f_is_not_abstract():
    assert not inspect.isabstract(test::F)


def test_test::f_constructor_exists():
    assert callable(test::F.__init__)


def test_test::f_constructor_args():
    sig = inspect.signature(test::F.__init__)
    params = list(sig.parameters.keys())



def test_test::d_is_not_abstract():
    assert not inspect.isabstract(test::D)


def test_test::d_constructor_exists():
    assert callable(test::D.__init__)


def test_test::d_constructor_args():
    sig = inspect.signature(test::D.__init__)
    params = list(sig.parameters.keys())



def test_test::i_is_not_abstract():
    assert not inspect.isabstract(test::I)


def test_test::i_constructor_exists():
    assert callable(test::I.__init__)


def test_test::i_constructor_args():
    sig = inspect.signature(test::I.__init__)
    params = list(sig.parameters.keys())



def test_test::e_is_not_abstract():
    assert not inspect.isabstract(test::E)


def test_test::e_constructor_exists():
    assert callable(test::E.__init__)


def test_test::e_constructor_args():
    sig = inspect.signature(test::E.__init__)
    params = list(sig.parameters.keys())



def test_test::c_is_not_abstract():
    assert not inspect.isabstract(test::C)


def test_test::c_constructor_exists():
    assert callable(test::C.__init__)


def test_test::c_constructor_args():
    sig = inspect.signature(test::C.__init__)
    params = list(sig.parameters.keys())



def test_test::b_is_not_abstract():
    assert not inspect.isabstract(test::B)


def test_test::b_constructor_exists():
    assert callable(test::B.__init__)


def test_test::b_constructor_args():
    sig = inspect.signature(test::B.__init__)
    params = list(sig.parameters.keys())



def test_test::a_is_not_abstract():
    assert not inspect.isabstract(test::A)


def test_test::a_constructor_exists():
    assert callable(test::A.__init__)


def test_test::a_constructor_args():
    sig = inspect.signature(test::A.__init__)
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
test::G_strategy = st.builds(
    test::G,
)
test::H_strategy = st.builds(
    test::H,
)
test::F_strategy = st.builds(
    test::F,
)
test::D_strategy = st.builds(
    test::D,
)
test::I_strategy = st.builds(
    test::I,
)
test::E_strategy = st.builds(
    test::E,
)
test::C_strategy = st.builds(
    test::C,
)
test::B_strategy = st.builds(
    test::B,
)
test::A_strategy = st.builds(
    test::A,
)

@given(instance=test::G_strategy)
@settings(max_examples=50)
def test_test::g_instantiation(instance):
    assert isinstance(instance, test::G)

@given(instance=test::H_strategy)
@settings(max_examples=50)
def test_test::h_instantiation(instance):
    assert isinstance(instance, test::H)

@given(instance=test::F_strategy)
@settings(max_examples=50)
def test_test::f_instantiation(instance):
    assert isinstance(instance, test::F)

@given(instance=test::D_strategy)
@settings(max_examples=50)
def test_test::d_instantiation(instance):
    assert isinstance(instance, test::D)

@given(instance=test::I_strategy)
@settings(max_examples=50)
def test_test::i_instantiation(instance):
    assert isinstance(instance, test::I)

@given(instance=test::E_strategy)
@settings(max_examples=50)
def test_test::e_instantiation(instance):
    assert isinstance(instance, test::E)

@given(instance=test::C_strategy)
@settings(max_examples=50)
def test_test::c_instantiation(instance):
    assert isinstance(instance, test::C)

@given(instance=test::B_strategy)
@settings(max_examples=50)
def test_test::b_instantiation(instance):
    assert isinstance(instance, test::B)

@given(instance=test::A_strategy)
@settings(max_examples=50)
def test_test::a_instantiation(instance):
    assert isinstance(instance, test::A)
