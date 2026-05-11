import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    D,
    case5::E,
    case5::B,
    case5::N,
    T,
    case5::D,
    case5::A,
    case5::T,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_d_constructor_exists():
    assert callable(D.__init__)


def test_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_case5::e_is_not_abstract():
    assert not inspect.isabstract(case5::E)


def test_case5::e_constructor_exists():
    assert callable(case5::E.__init__)


def test_case5::e_constructor_args():
    sig = inspect.signature(case5::E.__init__)
    params = list(sig.parameters.keys())



def test_case5::b_is_not_abstract():
    assert not inspect.isabstract(case5::B)


def test_case5::b_constructor_exists():
    assert callable(case5::B.__init__)


def test_case5::b_constructor_args():
    sig = inspect.signature(case5::B.__init__)
    params = list(sig.parameters.keys())



def test_case5::n_is_not_abstract():
    assert not inspect.isabstract(case5::N)


def test_case5::n_constructor_exists():
    assert callable(case5::N.__init__)


def test_case5::n_constructor_args():
    sig = inspect.signature(case5::N.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_case5::d_is_not_abstract():
    assert not inspect.isabstract(case5::D)


def test_case5::d_constructor_exists():
    assert callable(case5::D.__init__)


def test_case5::d_constructor_args():
    sig = inspect.signature(case5::D.__init__)
    params = list(sig.parameters.keys())



def test_case5::a_is_not_abstract():
    assert not inspect.isabstract(case5::A)


def test_case5::a_constructor_exists():
    assert callable(case5::A.__init__)


def test_case5::a_constructor_args():
    sig = inspect.signature(case5::A.__init__)
    params = list(sig.parameters.keys())



def test_case5::t_is_not_abstract():
    assert not inspect.isabstract(case5::T)


def test_case5::t_constructor_exists():
    assert callable(case5::T.__init__)


def test_case5::t_constructor_args():
    sig = inspect.signature(case5::T.__init__)
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
D_strategy = st.builds(
    D,
)
case5::E_strategy = st.builds(
    case5::E,
)
case5::B_strategy = st.builds(
    case5::B,
)
case5::N_strategy = st.builds(
    case5::N,
)
T_strategy = st.builds(
    T,
)
case5::D_strategy = st.builds(
    case5::D,
)
case5::A_strategy = st.builds(
    case5::A,
)
case5::T_strategy = st.builds(
    case5::T,
)

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=case5::E_strategy)
@settings(max_examples=50)
def test_case5::e_instantiation(instance):
    assert isinstance(instance, case5::E)

@given(instance=case5::B_strategy)
@settings(max_examples=50)
def test_case5::b_instantiation(instance):
    assert isinstance(instance, case5::B)

@given(instance=case5::N_strategy)
@settings(max_examples=50)
def test_case5::n_instantiation(instance):
    assert isinstance(instance, case5::N)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=case5::D_strategy)
@settings(max_examples=50)
def test_case5::d_instantiation(instance):
    assert isinstance(instance, case5::D)

@given(instance=case5::A_strategy)
@settings(max_examples=50)
def test_case5::a_instantiation(instance):
    assert isinstance(instance, case5::A)

@given(instance=case5::T_strategy)
@settings(max_examples=50)
def test_case5::t_instantiation(instance):
    assert isinstance(instance, case5::T)
